from os import F_TLOCK
import mdp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from numpy.core.fromnumeric import _searchsorted_dispatcher
matplotlib.use('TkAgg')


def sfa(data_matrix, num_features):
    sfa_node = mdp.nodes.SFANode(output_dim=num_features)
    sfa_node.train(data_matrix)
    features = sfa_node.execute(data_matrix)
    weights = sfa_node.sf
    return features, weights


# must have less dimensions / features than data (T<R)
# otherwise covariances will be singular
variable_dim = 200
temporal_dim = 500
F = 100
F_to_plot = 1

noise_multiplier = 0.1
amplitude = 0

# make fake data
# sinusoid curves of <variable_dim> points
# phase shifted over <temporal_dim> points
phase = np.linspace(0, np.pi / 2, temporal_dim, dtype=np.float)
x = np.linspace(0, 2 * np.pi, variable_dim, dtype=np.float)
base_feature = lambda p: amplitude * np.sin(x + p)

# d is a stack of trials of noisy time series x
d = np.array([np.sin(x) * p
              for p in phase])  #np.array([base_feature(p) for p in phase])
noise = np.random.randn(*d.shape) * noise_multiplier
d += noise
print("data", d.shape, (temporal_dim, variable_dim))

# plt.figure()
# plt.title("data")
# plt.plot(d.T[:, -1])
# plt.plot(d.T[:, 250])
# plt.plot(d.T[:, 0])

# sfa finds linear projections of each datapoint (trial)
# that minimize the derivative covariance within trials
# features will be over trials (R-dimensional)
# weights will project trials into feature space (T-dimensional)

# variables on the columns
# observations on the rows

# SFA finds the slowly varying features of a high-dimensional time
# series. Take x = (variable, temporal) and extract slow features
# In our case, the variables are themselves time series, and we're
# looking for slowly varying features of each

# http://scholarpedia.org/article/Slow_feature_analysis
# https://github.com/ibalazevic/slow_feature_analysis/blob/5234f973d0f7988f3f56b7ea859596e24ff66de3/sfa.py#L88
# http://mdp-toolkit.sourceforge.net/api/mdp.nodes.SFANode-class.html#train
# https://www.ini.rub.de/PEOPLE/wiskott/Teaching/Material/NonlinearExpansion-LectureNotesPublic.pdf
# http://www.gatsby.ucl.ac.uk/~turner/Publications/turner-and-sahani-2007a.pdf
# https://www.ini.rub.de/PEOPLE/wiskott/Reprints/WiskottSejnowski-2002-NeurComp-LearningInvariances.pdf

sfs, w = sfa(d, F)

print("weights", w.shape, (variable_dim, F))
print("features", sfs.shape, (temporal_dim, F))

# plt.figure()
# plt.title("weights")
# plt.plot(w[:, :F_to_plot])

# plt.figure()
# plt.title("features")
# plt.plot(sfs[:, :F_to_plot])

# sanity check
plt.figure()
plt.title("features")
plt.plot(sfs[:, :F_to_plot])
e = d - d.mean(axis=0) + noise * 10
y = e @ w[:, :F_to_plot]
print(y.shape)
plt.plot(y[:, :F_to_plot])

plt.show()