import scipy as sp
import numpy as np
import ot
import pickle

def load_log_trial_models(subject_idx):
    with open(f"../gmm_models_log_trial/subject_{subject_idx}.pkl","rb") as handle:
        return pickle.load(handle)

def load_trial_models(subject_idx):
    with open(f"../gmm_models_trial/subject_{subject_idx}.pkl","rb") as handle:
        return pickle.load(handle)
    
def load_log_calibration_models(subject_idx):
    with open(f"../gmm_models_log_calibration/subject_{subject_idx}.pkl","rb") as handle:
        return pickle.load(handle)
    
def load_log_movement_models(subject_idx):
    with open(f"../gmm_models_log_movement/subject_{subject_idx}.pkl","rb") as handle:
        return pickle.load(handle)

def gaussian_entropy(cov):
    # https://gregorygundersen.com/blog/2020/09/01/gaussian-entropy/
    assert cov.shape == (64,64)
    # (D/2)*(1 + log(2pi)) + (1/2)*log(det(C))
    # return 32*(1 + np.log(2*np.pi)) + 0.5*np.log(np.linalg.det(cov))
    return np.log(np.linalg.det(cov)**(1/64))

def total_gmm_entropy(model):
    assert len(model.covariances_) > 0
    return np.sum([gaussian_entropy(c)*w for c, w in zip(model.covariances_,model.weights_)])

def transform_mean(decoder, mean):
    assert decoder.shape == (2,64)
    return decoder @ mean

def transform_covariance(decoder, covariance):
    assert decoder.shape == (2,64)
    return decoder @ covariance @ decoder.T

def make_lognormal_mean(normal_mean, normal_covariance):
    dim = normal_mean.shape[0]
    assert dim >= normal_mean.shape[1]
    assert dim == normal_covariance.shape[0] and dim == normal_covariance.shape[1]
    return np.exp(normal_mean + 0.5*np.diag(normal_covariance).reshape(-1,1))

def make_lognormal_covariance(normal_mean,normal_covariance):
    dim = normal_mean.shape[0]
    assert dim >= normal_mean.shape[1]
    assert dim == normal_covariance.shape[0] and dim == normal_covariance.shape[1]
    cov = np.zeros(shape=(dim,dim))
    cov[:] = np.nan
    for i in range(dim):
        for j in range(dim):
            cov[i,j] = (np.exp(normal_mean[i] + normal_mean[j] + 0.5*(normal_covariance[i,i] + normal_covariance[j,j]))*(np.exp(normal_covariance[i,j]) - 1)).reshape(-1)[0]
    assert np.all(np.isfinite(cov))
    return cov

def zero_ch_56_mean(mean):
    mean = mean.copy()
    mean[56,0] = 0
    return mean

def zero_ch_56_cov(cov):
    cov = cov.copy()
    cov[:,56] = 0
    cov[56,:] = 0
    return cov

class log_model():
    def __init__(self, model) -> None:
        self.means = np.array([zero_ch_56_mean(make_lognormal_mean(mean.reshape(-1,1), covariance)).reshape(-1) for mean, covariance in zip(model.means_, model.covariances_)])
        self.covariances = np.array([zero_ch_56_cov(make_lognormal_covariance(mean.reshape(-1,1), covariance)) for mean, covariance in zip(model.means_, model.covariances_)])
        self.weights = model.weights_

class model_2d():
    def __init__(self,model,decoder) -> None:
        self.means = np.array([transform_mean(decoder,mean) for mean in model.means])
        self.covariances = np.array([transform_covariance(decoder,cov) for cov in model.covariances])
        self.weights = model.weights

def GaussianW2(m0,m1,Sigma0,Sigma1):
    # compute the quadratic Wasserstein distance between two Gaussians with means m0 and m1 and covariances Sigma0 and Sigma1
    Sigma00  = sp.linalg.sqrtm(Sigma0)
    Sigma010 = sp.linalg.sqrtm(Sigma00@Sigma1@Sigma00)
    return np.linalg.norm(m0-m1)**2+np.trace(Sigma0+Sigma1-2*Sigma010)

# original from the GMM W2 paper 
# def GW2(pi0,pi1,mu0,mu1,S0,S1):
#     # return the GW2 discrete map and the GW2 distance between two GMM
#     K0 = mu0.shape[0]
#     K1 = mu1.shape[0]
#     d  = mu0.shape[1]
#     S0 = S0.reshape(K0,d,d)
#     S1 = S1.reshape(K1,d,d)
#     M  = np.zeros((K0,K1))
#     # First we compute the distance matrix between all Gaussians pairwise
#     for k in range(K0):
#         for l in range(K1):
#             M[k,l]  = GaussianW2(mu0[k,:],mu1[l,:],S0[k,:,:],S1[l,:,:])
#     # Then we compute the OT distance or OT map thanks to the OT library    
#     wstar     = ot.emd(pi0,pi1,M)         # discrete transport plan
#     distGW2   = np.sum(wstar*M)
#     return wstar,distGW2

def closest_pairs_euclidean(models,mean_weight=1.0, weight_weight=0.0,cov_weight=0.0):
    model_mean_pairs = []
    for model_1, model_2 in zip(models[:-1],models[1:]):
        lower_tris1 =  np.array([cov[np.tril_indices(64)] for cov in model_1.covariances_])
        lower_tris2 =  np.array([cov[np.tril_indices(64)] for cov in model_2.covariances_])
        model_1_vec = np.concatenate([model_1.means_*mean_weight,lower_tris1*cov_weight,model_1.weights_.reshape(-1,1)*weight_weight],axis=1)
        model_2_vec = np.concatenate([model_2.means_*mean_weight,lower_tris2*cov_weight,model_2.weights_.reshape(-1,1)*weight_weight],axis=1)
        pairs, distance_sum = closest_pairs(model_1_vec, model_2_vec)
        model_mean_pairs.append(pairs)
    return np.array(model_mean_pairs)

def wasserstein_matrix(mu0,mu1,S0,S1):
    # Compute the distance matrix between all Gaussians pairwise
    K0 = mu0.shape[0]
    K1 = mu1.shape[0]
    d  = mu0.shape[1]
    S0 = S0.reshape(K0,d,d)
    S1 = S1.reshape(K1,d,d)
    M  = np.zeros((K0,K1))
    for k in range(K0):
        for l in range(K1):
            M[k,l]  = GaussianW2(mu0[k,:],mu1[l,:],S0[k,:,:],S1[l,:,:])
    return M

def GW2(pi0,pi1,mu0,mu1,S0,S1):
    M = wasserstein_matrix(mu0,mu1,S0,S1)
    # Compute the OT distance or OT map thanks to the OT library    
    wstar     = ot.emd(pi0,pi1,M)         # discrete transport plan
    distGW2   = np.sum(wstar*M)
    return wstar, distGW2
    
def gmm_wasserstein(pi0,pi1,mu0,mu1,S0,S1):
    _, d = GW2(pi0,pi1,mu0,mu1,S0,S1)
    return d

def closest_pairs_wasserstein(mu0,mu1,S0,S1):
    # assert points1.shape[0] > points1.shape[1]
    # assert points2.shape[0] > points2.shape[1]
    # distances between 1 and 2
    distance_matrix = wasserstein_matrix(mu0,mu1,S0,S1)
    # indexes for rows and columns
    i1, i2 = np.indices((mu0.shape[0],mu1.shape[0]))
    # pair the indexes [row,col],[row,col], ...
    index_pairs = np.column_stack([i1.reshape(-1),i2.reshape(-1)])
    # flatten distance matrix the same way as indexes
    distances = distance_matrix.reshape(-1)
    # sort distances
    sorted_distance_indices = np.argsort(distances)
    stored_pairs = []
    used_pairs_1 = []
    used_pairs_2 = []
    # for every pairwise distance, shortest to longest
    for _, pair_idx in enumerate(sorted_distance_indices):
        # grab the original index pair to know which points
        pair = index_pairs[pair_idx]
        # check if we've seen either of these points before
        if (not pair[0] in used_pairs_1) and (not pair[1] in used_pairs_2):
            # if we haven't, store them
            stored_pairs.append(pair)
            used_pairs_1.append(pair[0])
            used_pairs_2.append(pair[1])
    return stored_pairs

def closest_pairs_over_models_wasserstein(models):
    pairs = []
    for model1, model2 in zip(models[:-1],models[1:]):
        pairs += [closest_pairs_wasserstein(model1.means_, model2.means_,model1.covariances_,model2.covariances_)]
    return np.array(pairs)

def closest_pairs(points1, points2):
    # assert points1.shape[0] > points1.shape[1]
    # assert points2.shape[0] > points2.shape[1]
    # distances between 1 and 2
    distance_matrix = sp.spatial.distance.cdist(points1, points2)
    # indexes for rows and columns
    i1, i2 = np.indices((points1.shape[0],points2.shape[0]))
    # pair the indexes [row,col],[row,col], ...
    index_pairs = np.column_stack([i1.reshape(-1),i2.reshape(-1)])
    # flatten distance matrix the same way as indexes
    distances = distance_matrix.reshape(-1)
    # sort distances
    sorted_distance_indices = np.argsort(distances)
    stored_pairs = []
    used_pairs_1 = []
    used_pairs_2 = []
    distance_sum = 0
    # for every pairwise distance, shortest to longest
    for _, pair_idx in enumerate(sorted_distance_indices):
        # grab the original index pair to know which points
        pair = index_pairs[pair_idx]
        # check if we've seen either of these points before
        if (not pair[0] in used_pairs_1) and (not pair[1] in used_pairs_2):
            # if we haven't, store them
            stored_pairs.append(pair)
            distance_sum += distance_matrix[pair[0],pair[1]]
            used_pairs_1.append(pair[0])
            used_pairs_2.append(pair[1])
    return stored_pairs, distance_sum

