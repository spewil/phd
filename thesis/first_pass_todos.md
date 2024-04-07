
* = nice to have
** = strengthens the thesis considerably
*** == would leave a big gap in the story if missing

## intro
- [WRITING] look at https://www.spewil.com/phd/ and expand on this

## background
- [WRITING] read what's there, remove all the junk
- [WRITING] look at https://www.spewil.com/phd/ for basic points
- [WRITING] read kandel for juice!
- refer to results to highlight key texts and ideas


**Maybe turn all these model comparison plots into boxplots?**
- https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_test
- https://matplotlib.org/3.1.1/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py 

## Methods

Easy
*** [FIGURE_UPDATE_KEYNOTE] make some kind of visual to support explaining the task and null space. Even if it's just a plane with some projection lines and arrows. Look at that one paper for the "spaces" figure -- maybe combine this with the "Methods" spaces figure


Not easy

* [NEW_FIGURE_ANALYSIS] TODO? run NMF on the second calibration set for comparison -- need to find the best matching modes here (we wouldn't expect the chosen pairs to match between calibration sets) -- this needs work, as we need to write some code to make this sound... ~~but maybe opportunity to figure out comparing NMF subspaces?~~ We can use the Grassmanian metric to determine if two subspaces are aligned? **Use the Grassmann metric to compare NMF subspaces between first and second calibration runs**

Writing
[WRITING] **Set up the idea that variance or entropy in the calibration task is good (e.g. in \Cref{chap:methods} when introducing the tasks).**

- ~~TODO -- more NMF visualization. What if we fit different numbers of modes? Compare this to PCA modes? Compare to log-PCA-exp? The problem with PCA here is that it's unlikely to demix these modes?~~



## Performance

Easy:
- ~~Plot reward vs. (reach time, path length, and segments) to prove that these correlate with performance as expected~~
- ~~Plot the targets on fig:rotated_trajectories~~
- ~~Make a significance matrix for mean comparisons in fig:compare_subject_groups~~
- ~~Discuss degree of freedom freezing in the context of the segments-- segments can be a proxy measure of freezing!~~ -- added, but need to elaborate
- ~~Use reward where we're using hit count currently -- change all the performance plots to hits~~ -- think this is done...? Not sure what I was talking about... 

- ~~Make sure that reward is calculated using the active indices! Figure out how to do this with pandas? Compare hits vs. reward (on the same plot?) to make sure we're not going crazy~~ -- it is! we're using filtered trajectories


Not easy 

* [NEW_FIGURE_ANALYSIS] **A measure of performance for the calibration task-- how did people do?** 

*-* [NEW_FIGURE_VIZ] **Leave this for now, unclear how useful it is** The **trajectory variance** section is confused and needs rethinking or cutting. The point is to show that trajectory variance decreases over time. This isn't a very interesting point to make, as it's clear that this is the case from the earlier performance plots. Should we really only be looking at the $y$ coordinate since the $x$ coordinate has to vary in order to hit the target? Maybe ideate on this, and think about this as "task space" analysis-- what can we look at the in the task space across and within subjects? (TRAJECTORY VARIANCE) -- TODO should we show the right-tailed data here too? Should we fit this exponential, in order to say ``across subjects on average trajectory variance decreases'' We could try to relate this to performance, maybe showing correlation between early and late variance? There might be a point made here about exploration in the task space? The original idea here was to explore the task space statistics more fully before getting into the full EMG space. The decoder discussion about normality allows us to say that the decoder is a projection onto a 2d plane, but going from 64 to 2 dimensions also has this concentrating action, so the task space statistics are interesting on their own as well. This is still unrealized here. Unclear what the story can or should be. Make a staggered histogram plot over subjects and within a subject for the y component only? **After discussing with Tiago, we should try making a figure that's the variance over blocks of trials at each time point, so if we use our 5 trial blocks, we'll see 5 x n_normalized_timepoints lines for each subject. We could try collating all subjects and see... we could also look over time as well. Probably worth just looking at these in several ways-- across subjects, within...** 

Writing 
[WRITING] Put the reward histogram and the hits vs. reward plot earlier to discuss reward 

[IGNORE] ~~TODO? Plot the mean of all subjects' decoder arrows, which may help to explain the bias towards the left hand side of the screen? However, this is a weird average to take since the order of EMG channels will differ. I would need to do this using some kind of density plot, overlaying each subject's decoder arrows in 2D. Probably more trouble than it's worth.~~

[IGNORE] ~~TODO?: normality tests on histograms of reward and hit counts per subject, we can justify using the mean reward per subject as a measure of performance as there are not any glaring outliers and the curve is approximately normal, while the hit count curve is skewed~~

[IGNORE] we can just talk about trajectory segments... ~~FUTURE WORK: Look into the ``freezing degrees of freedom'' idea, defined as the size of the ``active'' EMG subspace within each trial. This could be done using NMF or PCA on each trial, e.g. many PCA components are active at once (how sparse are the component weights?), and how does this change over time? Sparsity (measured by the 1-norm) might imply that only a certain mode is active at a time, and this might change to more mixing over time. We would expect mixing to increase as people become more proficient and blend their activity modes together. This would be quite a rabbit hole, but interesting! We really want to know if people have distinct modes of activity early on, and how these blend into solutions over time. This is tricky to do, and currently lacking between the setup in the background chapters and the current results.~~




## Manifold

Easy

~~*-*-* [NEW_FIGURE] **Plot PCA rank vs. reward! This is a matching plot as the GMM models. We expect these to agree with the GMM results, as they're capturing a similar phenomenon, opposed to the comparison between models, which are capturing opposite features of the distributions.~~

Not Easy

~~*-*-* [NEW_FIGURE_ANALYSIS] Visualize the PCA modes from movement, calibration, trials and compare them! For a few subjects. Are natural movement modes relevant to the task? How do these modes change over time? Try NMF? Don't just say ``hey we can't use PCA'', use PCA as a starting point that's literally a broader view, then zoom in with the GMMs! Do this in the previous chapter. -- we can generate PCA subspaces for whatever we want... we can project data and look at it, we can look at the principle vectors, we can compare subspaces with the grassman metric... we can use the cross projection similarity after the sara solla paper... ~~(compare solla metric and grassman?)~~ -- this is waiting when we want to make it. This will give us a means of comparing linear subspaces of our data, comparison with the solla paper. Use the Solla metric first, then introduce the Grassman metric as a more general version of this, to determine how aligned any two subspaces are, not just PCA. If the subspace is the principle subspace of some data, these measures are equivalent (is this true? no, because they are not symmetric!)~~ **Use the Solla and grassman metrics for comparing PCA subspaces**

~~*-* [NEW_FIGURE_ANALYSIS] Are the NMF modes (of the calibration) related to the natural movement statistics? --- TODO? Run NMF on the natural movement stats and compare the subspaces between this and the calibration task, maybe just visually unless I can figure out a statistic... **Compare NMF subspaces for calibration, natural movement using Grassman metrics** We think this will indicate how similar these subspaces are~~


Writing 

[WRITING] In the case of the GMMs, the lower effective rank correlating with reward implies that higher performing subjects have more "buttons" that are spread across channels. So they have specific buttons (rank of each component is low) but those buttons live across the subspace, inhabiting different areas of it? How case 

- ~~Add GMM fits to each of the toy model examples~~

- [WRITING] Note that this analysis was done in the log-transformed space! Where PCA can be applied! What PCA misses is the mixture of low rank components.

- [WRITING] (More) Clearly explain the concept of the subspaces sooner to nail home the spikiness point, as this is becoming critical for the throughline of the thesis? Have we adequately supported the spiky, constrained manifold? EMG activity lives in distinct subspaces (groups of channels). Each of these groups appears to be approximately lognormal. The degree to which these subspaces overlap, and the degree to which these subspaces "tile" the space of EMG activity is predictive of reward (can we back this up?) -- where should this go?
    - I think one logical order is the order of discovery: we have the data we have. We visualize it and we develop a hunch about the data manifold. This tells us gives us ideas about what we might find when we do PCA, and that we may need to do something else. Also gives us an idea about how to pre-process our data (filtering, etc.). Manifold might be a discussion of these steps, getting strong intuitions about the shape of the data before going into actual results?
    - So:
        - intro / background -- this is just what others have done, sets up vocabulary, importance of the program (USE this word in the conclusion! that this is a very rich line of work that's underexplored in the context of learning, etc...)
        - methods -- how did we collect the data we got?
        - performance -- do people do the task, is the task sound? confounds? (also discuss the decoder here!)
        - manifold? this is where we visualize our data, discuss its shape, build intutions about subspaces, etc to set up the later analyses -- show the blobs, discuss PCA and why it's still useful, discuss why mixture models are a good choice.
        - "basic results" -- can we call this "linear analysis"? -- maybe "linear subspaces"? this is where we look at PCA and NMF modes within subjects to understand at a basic level what's happening with the data and to use as a comparison to other papers!
        - GMMS -- more advanced analysis because we have deeper look into the EMG data
        - Null space -- comparing to other papers, trying to understand learning from the task-redundancy angle
        - Classification -- maybe this should go in the PCA section...?
        - [IMCOMPLETE] Modeling -- we're hoping there's time to extend the nullspace stuff with a very basic RL model to show how these models can be compared to human tasks... 

~~TODO? Look at the sparsity of the components --- while the number of components needed may be low, those components may not be sparse, they may be spatially spread out? Look at the 1-norm of the component? 0-norm? Gini index?~~ Sparsity is a way to measure how confined these subspaces are, how much they share with other components... I think this can be captured with just the PCA variance... for PCA to capture multiple modes, they would have to be orthogonal. This is only the case when the components lie in completely separate subspaces of the EMG space? So:

- [WRITING] **PCA is in a sense a measure of how orthogonal these components are, a kind of measure of subspace orthogonality? If each blob sat in its own subspace of channels, there would be a basis that aligned with the variance, one for each blob.** This is shown in the toy model figure, where if the blobs are orthogonal, PCA is happy. But when they start mixing, PCA can't extract them anymore, and serves as a measure of mixing, or subspace confinement! GMMs attempt to circumvent this problem by "demixing" (though not in the traditional sense?) and finding as many blobs as we can find. Then it's up to use to determine the dimensionality of these blobs (looking at each blob's covariance structure, e.g. with PCA!)
**When we introduce this ``top two singular value'' concept, connect it to the toy model \Cref{fig:toy_model} and the concept of ``effective rank''. That this is a proxy for the rank of the components which make up the mixture of modes in the dataset. PCA can't unmix these modes, so we use GMMs to try to unmix.**

~~TODO? generate synthetic data to compare 64D Gaussian distribution with matching statistics from UMAP (this will look like a blob), compare that to subspace confined gaussians?~~ UMAP is just for show, don't think too hard about it. The point of the UMAP is to show that the manifold is pretty much in line with what we've said before.


## GMMs 

Easy:
- ~~Separate the colormaps of the two columns in \Cref{fig:gmm_vs_pca}, it doesn't make sense to share the scale as these will have different variances. The PCA variance is lower because the variance there is additive to reconstruct the empirical covariance.~~

~~*-*-* [FIGURE_COMBINE] combine \Cref{fig:example_gmms,fig:example_trial_gmms}, use the connecting lines to explain how we're pairing the means of the components including the movement and calibration models. Change the targets to unweighted (too much information)~~

~~*-*-* [FIGURE_COMPARE] **Test 2-Wasserstein distance pairing -- we need to be able to explain WHY we're doing using W2 vs. Frobenius, etc...** Decide on W2 vs. Frobenius, etc. Wasserstein is a more interesting metric, but what does it add that Fr doesn't have? W2 is equivalent to mean Euclidean when the covariances are the same... Why not use W2? Test with Frobenius to catch any inconsistencies or weirdness?~~

~~*-*-* [NEW_FIGURE] Show Wasserstein pairwise statistics for all trial chunks? Keep these plots, but show the significance matrix? So compute the pairwise wasserstein over "time" or chunks, and then show the significance matrix for this~~ Seems like overkill... 

~~*-*- [NEW_FIGURE_VIZ] **Visualize the GMM modes and point out comparison to the PCA modes shown earlier! (Plot means? Plot first PC component of the covariances?) ALSO Visualize the model components over time for one subject so we can get an idea about the change happening over time on a per-subject basis, this will help us build a more intuitive explanation!** This is a 64 x 12 x 5 plot? Add Natural movement for reference for a 3x2 subplots of 64x12?~~ -- OVERKILL, we've visualized them

*- [FIGURE_COMPARE] **Compare entropy to "weighted mean of total variance trace(cov(X))** if the total var is easier just use that! 

*- [NEW_FIGURE_EASY] **Sample from the model and compare the performance of the model to the subject's performance in terms of hits and reward. This would serve as a practical goodness of fit test and give us better grounds to assess the model fits.**

? [NEW_FIGURE???] How can we measure the "spread-out-ness" of the GMM fits? Or is this covered by the PCA? The GMMs are a zoom-in, a better way to track things over trials? We could look at the pairwise distances/angle between the means of the GMMs... but maybe it's better to look at the pairwise distances/angle between the GMM covariance subspaces OR the GMM distance/angle between the covariance top components pairwise -- so compute the top PC for each GMM component, pairwise cosine angle between those, then look at ..... ?? Maybe the mean?


Writing

- [WRITING] write down the math for the difference of component means plus the Frobenius. Here we pair the means of each component from one model to the next using the Euclidean distance in EMG space, then we compute the Frobenius difference between those pairs' covariances. Then we take the mean of that Frobenius difference. 

- [WRITING] why can't you sample from the log-transformed gaussians? because they don't have the same distribution. The mean and covariance can be plotted, and this looks like the log-transformed data sampled from the original gaussian model fit in the normal space where it's a sum of gaussians. when you take the exp to go back to the lognormal space, that sum becomes something else, a product. so it's not the same distribution.

- [WRITING] **GMM rank -- explain how this relates to the sister figure with PCA, now instead of the whole dataset, we're looking at gaussian pieces of it. Why do we expect the opposite trend? What does effective rank mean here? It's a measure of how ellipsoidal or elongated the dataset is. One end of the spectrum is sphere, the other is a perfect line. Sphere is equal covariance, so equal PC weights. Line is 1 PC component. It's simply how many of the dimensions have variance and what's the weighting. How many channels are active in the data! That's literally it. So how "complex" is each mode is how much variance is in each dimension of this data, or how many dimensions are active?**

- [WRITING] show where we got the wasserstein distance from, explain the algorithm for finding pairings -- https://github.com/judelo/gmmot

- ~~Are we clearly explaining the main hypothesis that subjects who are less ``constrained'' are expected to perform better? And how this constraint arises?~~ I think worked out above!





## Null Space

Easy 
~~*-*-* [FIGURE_UPDATE] (hits/misses vs reward) Think more carefully here. The correlation for hit ends versus reward may simply be due to lower performing subjects having fewer hits, and thus lower variance. Try normalizing by the number of samples/hits to get a standard error.~~

~~*-*-* [FIGURE_UPDATE_ANALYSIS] Is there a way to compare the variance projection of the error distribution to a null hypothesis? If subjects were to move randomly according to some simpler distribution? Or can we compare the error here to the natural movement or calibration data somehow? The problem with this is that there is no ``solution'' to use to compute an error signal. Need to think about this. **keep it simple! what's wrong with a Gaussian with matching covariance to the error solution? This would at least give us a comparison point?**~~ -- this doesn't make sense to do! but gives us a good thing to write about!

~~*-*-* [NEW_FIGURE_VIZ] (GMM null space figure) add significance matrix for the null space and task space without the ratio. This shows us what's happening to make the ratio higher. Combine with the other significance plot?~~

~~*-* [NEW_FIGURE_VIZ] Introduce the idea of the "hit end" by showing hit ends from a single subject. Explain the "hit end" for the miss trials, where we're taking the lowest task-space error sample in place of the hit end. We're calling this a ``miss end''.~~


Writing 

[WRITING] NB for Tukey HSD: 
- The observations being tested are independent within and among the groups.
- The groups associated with each mean in the test are normally distributed.
- There is equal within-group variance across the groups associated with each mean in the test (homogeneity of variance).

[WRITING] If you project a spherical covariance and take the ratio, you will get 0! because this is effectively x.TCx = x.Tx = norm(x) = 1 (orthonormal basis), averaged over the number of dimensions = 1 ... Write out this math to show how we're computing the variance ratio, and how a spherical gaussian will lead to this answer.

[WRITING] write the math associated with the task and null space and the projection. refer to the figure in the methods section

[WRITING] (GMM null space figure) Think more about how this relates to the hit end results below. How do we expect these things to compare?

[WRITING] Decide whether this analysis makes sense. Should we instead use the ``error'' between the ideal, zero-null-space-activity solution and the actual subject solutions? These results don't show much shift in the task-null ratio, which might be interesting as it shows that people don't really seem to care about the null space over learning. In theory, using the error removes activity that is minimally task relevant, leaving you with what should be pure nullspace activity, or everything in the EMG that isn't required for the task. This is shown in \Cref{fig:error_nullspace_subjects}. We see a much higher ratio, suggesting that the distribution of error is more aligned to the task plane than the nullspace. **Ok, really the "error" signal is just a shifted version of the trials, asking how far from the target are you, and the task-null asks in what direction? So the ratio here being high says ok, the variation in the distance from the target tends to lie more in the task plane than the null space. PUT THIS BEFORE THE HITS-MISSES, it can serve as a kind of naive look at the null space.**

[WRITING] Introduce the hit end variance ratio before getting into misses and hits

[WRITING] write down the math for the pseudoinverse solution -- solution "e" which solves the equation target = De

[WRITING] strengthen the argument that the task isn't SIMPLY one of reproducing movements made in the calibration task. That yes it's capturing statistics of that task, it's not simply a recapitulation of prior movements. We do have to point out clearly that the task is designed by extracting a plane from subjects' calibration data, and thus the natural manifold is biased in the direction of the task. However, taken in combination with the GMM projections, we don't think this is merely an artefact of the task structure. (E.g. show the decoder weights relative to natural movement modes? Calibration modes?)

[WRITING] Think harder about why the GMM has a lower similarity to the subject solutions than the other solutions. I think this is simply an artefact of the GMMs being overfit, and thus these solutions are very ``specific'' to those datasets, while the other solutions are more generic. So subjects are generating solutions that are in line with their prior statistics, but that are unique to the target task itself, not just rehashings of movements that were made prior, on average.

~~TODO Change cosine ``distance'' to similarity (0 to 1)~~

??? TODO Is this again due to the amount of data we have for subjects? Can we normalize somehow normalize this by the number of hits to check?

[WRITING] Put all of these results together. What do they all point to? The best summary I have now is that subjects are fundamentally constrained by their underlying EMG manifold in succeeding in the task, and this is not taken into account in the way the decoder is computed. Despite this, however, subjects still learn to varying degrees. They are biased by their prior statistics, but not enough not to carve out new solutions for the task at hand. The solutions they do discover seem to mostly disregard the null space as task-irrelevant, pointing to a kind of model-free learning happening on this time scale.

??? I think it would be really strong to dig further into one or two subjects' solutions and visualize things as if I only had this data. This might give better context for the subject-averaged results, illustrating how this plays out for a single subject.


## RL Model

- make sure that we can recover very obvious solution using the KL penalty -- show this as proof that this works! and for our own benefit


## Conclusions

- things are long-tailed, probably more like pareto statistics -- this could be interesting to look at, how learning hinges on outlier events?

- we discussed the Grassmanian metric, this in general is a fruitful path forward, looking at the spaces of linear subspaces, or the spaces of covariance matrices. There is a rich litersature in the data science community dealing with this, most notably with techniques from tangent space analysis. This has been used with great success for EMG signals (Alex paper, Ctrl-labs paper) and would be an entry point into more geometric and algebraic grounding for future analysis of this and similar datasets.