
# OUTLINE

- intro / background -- this is just what others have done, sets up vocabulary, importance of the program (USE this word in the conclusion! that this is a very rich line of work that's underexplored in the context of learning, etc...)

- methods -- how did we collect the data we got?

- performance -- do people do the task, is the task sound? what confounds did we check for? (also discuss the decoder, how it was fit!)

- manifold -- this is where we visualize our data, discuss its shape, build intuitions about subspaces, etc to set up the later analyses -- show the blobs, discuss PCA and why it's still useful, discuss why mixture models are a good choice. look at PCA and NMF modes within subjects to understand at a basic level what's happening with the data and to use as a comparison to other papers!
- Classification -- maybe this should go in the PCA section...?

- Mixture models -- more advanced analysis because we have deeper look into the EMG data

- Null space -- comparing to other papers, trying to understand learning from the task-redundancy angle


- [IMCOMPLETE] Modeling -- we're hoping there's time to extend the nullspace stuff with a very basic RL model to show how these models can be compared to human tasks... 





## INTRO 

- look at https://www.spewil.com/phd/ and copy + expand on this


## BACKGROUND

- look at https://www.spewil.com/phd/ for basic points -- think this is already copied verbatim?
- read some kandel for juice / ideas!


## METHODS

- [FIGURE] update "spaces" figure to easily explain task space, null space, decoder, activity spaces

- [WRITING] set up variance in the calibration task as a positive


## PERFORMANCE

- [WRITING] Put the reward histogram and the hits vs. reward plot earlier to discuss reward 
- [WRITING] reward is calculated using the active samples


## MANIFOLD

- UMAP is just for show, don't think too hard about it. The point of the UMAP is to get a basic intuition for structure before we dive into it.

- [WRITING] EMG activity lives in distinct subspaces (groups of channels). Each of these groups appears to be approximately lognormal. The degree to which these subspaces overlap, and the degree to which these subspaces "tile" the space of EMG activity is predictive of reward (can we back this up?)

- [WRITING] What does effective rank mean? Lower effective rank = mean of the rank of individual GMM components is small, more concentrated or directed in terms of spatial activity. All of the components could be the same, it's a measure of how "specific" the components are on average.

- [WRITING] PCA misses the component mixtures -- PCA is in a sense a measure of how orthogonal these components are, a kind of measure of subspace orthogonality? If each blob sat in its own subspace of channels, there would be a basis that aligned with the variance, one for each blob.** This is shown in the toy model figure, where if the blobs are orthogonal, PCA is happy. But when they start mixing, PCA can't extract them anymore, and serves as a measure of mixing, or subspace confinement! GMMs attempt to circumvent this problem by "demixing" (though not in the traditional sense?) and finding as many blobs as we can find. Then it's up to use to determine the "dimensionality" of these blobs. We introduce this "top two singular value" concept, connect it to the toy model \Cref{fig:toy_model} as an ``effective rank''. That this is a proxy for the rank of the components which make up the mixture of modes in the dataset. PCA can't demix these modes, so we use GMMs to try to demix.**


## MIXTURES

- [WRITING] ~~write down the math for the difference of component means plus the Frobenius. Here we pair the means of each component from one model to the next using the Euclidean distance in EMG space, then we compute the Frobenius difference between those pairs' covariances. Then we take the mean of that Frobenius difference. ~~ Let's go with the W2 distance here, easier to defend.

- [WRITING] why can't you sample from the log-transformed Gaussians? because they don't have the same distribution. The mean and covariance can be plotted, and this looks like the log-transformed data sampled from the original gaussian model fit in the normal space where it's a sum of Gaussians. when you take the exp to go back to the lognormal space, that sum becomes something else, a product, so it's not the same distribution.

- [WRITING] GMM rank -- explain how this relates to the sister figure with PCA, now instead of the whole dataset, we're looking at gaussian pieces of it. Why do we expect the opposite trend? What does effective rank mean here? It's a measure of how ellipsoidal or elongated the dataset is. One end of the spectrum is spherical gaussian, with a diagonal covariance (full rank!), the other is a line of data (rank-1, there's only activity along one direction/dimension/). Sphere is equal covariance, so equal PC weights. Line is 1 PC component. It's simply how many of the dimensions have variance and what's the weighting. How many channels are active in the data! That's literally it. So how "complex" is each mode is how much variance is in each dimension of this data, or how many dimensions are active.

- [WRITING] show where we got the Wasserstein distance from, explain the algorithm for finding the pairings -- https://github.com/judelo/gmmot

## NULL SPACE

[WRITING] NB for Tukey HSD: 
- The observations being tested are independent within and among the groups.
- The groups associated with each mean in the test are normally distributed.
- There is equal within-group variance across the groups associated with each mean in the test (homogeneity of variance).

[WRITING] If you project a spherical covariance and take the ratio, you will just get 1! because this is effectively x.TCx = x.Tx = norm(x) = 1 (orthonormal basis), averaged over the number of dimensions = 1 ... Write out this math to show how we're computing the variance ratio, and how a spherical gaussian will lead to this answer.

[WRITING] Write the math associated with the task and null space and the projection. refer to the figure in the methods section

[WRITING] (GMM null space figure) Think more about how this relates to the hit end results below. How do we expect these things to compare?

[WRITING] Decide whether this analysis makes sense. Should we instead use the ``error'' between the ideal, zero-null-space-activity solution and the actual subject solutions? These results don't show much shift in the task-null ratio, which might be interesting as it shows that people don't really seem to care about the null space over learning. In theory, using the error removes activity that is minimally task relevant, leaving you with what should be pure nullspace activity, or everything in the EMG that isn't required for the task. This is shown in \Cref{fig:error_nullspace_subjects}. We see a much higher ratio, suggesting that the distribution of error is more aligned to the task plane than the nullspace. **Ok, really the "error" signal is just a shifted version of the trials, asking how far from the target are you, and the task-null asks in what direction? So the ratio here being high says ok, the variation in the distance from the target tends to lie more in the task plane than the null space. PUT THIS BEFORE THE HITS-MISSES, it can serve as a kind of naive look at the null space.**

[WRITING] Introduce the hit end variance ratio before getting into misses and hits

[WRITING] write down the math for the pseudoinverse solution -- solution "e" which solves the equation target = De

[WRITING] strengthen the argument that the task isn't SIMPLY one of reproducing movements made in the calibration task. That yes it's capturing statistics of that task, it's not simply a recapitulation of prior movements. We do have to point out clearly that the task is designed by extracting a plane from subjects' calibration data, and thus the natural manifold is biased in the direction of the task. However, taken in combination with the GMM projections, we don't think this is merely an artefact of the task structure. (E.g. show the decoder weights relative to natural movement modes? Calibration modes?)

[WRITING] Think harder about why the GMM has a lower similarity to the subject solutions than the other solutions. I think this is simply an artefact of the GMMs being overfit, and thus these solutions are very ``specific'' to those datasets, while the other solutions are more generic. So subjects are generating solutions that are in line with their prior statistics, but that are unique to the target task itself, not just rehashings of movements that were made prior, on average.

~~TODO Change cosine ``distance'' to similarity (0 to 1)~~

~~??? TODO Is this again due to the amount of data we have for subjects? Can we normalize somehow normalize this by the number of hits to check?~~

[WRITING] Put all of these results together. What do they all point to? The best summary I have now is that subjects are fundamentally constrained by their underlying EMG manifold in succeeding in the task, and this is not taken into account in the way the decoder is computed. Despite this, however, subjects still learn to varying degrees. They are biased by their prior statistics, but not enough not to carve out new solutions for the task at hand. The solutions they do discover seem to mostly disregard the null space as task-irrelevant, pointing to a kind of model-free learning happening on this time scale.

??? I think it would be really strong to dig further into one or two subjects' solutions and visualize things as if I only had this data. This might give better context for the subject-averaged results, illustrating how this plays out for a single subject.

## RL Model

- make sure that we can recover very obvious solution using the KL penalty -- show this as proof that this works! and for our own benefit


## Conclusions

- things are long-tailed, probably more like pareto statistics -- this could be interesting to look at, how learning hinges on outlier events?

- we discussed the Grassmanian metric, this in general is a fruitful path forward, looking at the spaces of linear subspaces, or the spaces of covariance matrices. There is a rich litersature in the data science community dealing with this, most notably with techniques from tangent space analysis. This has been used with great success for EMG signals (Alex paper, Ctrl-labs paper) and would be an entry point into more geometric and algebraic grounding for future analysis of this and similar datasets.