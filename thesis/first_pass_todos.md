## Methods

- What is NMF optimizing for? (Compare to later, log-transformed PCA!) Generating additive components, thus can result in parts-based decomposition... Sum of the parts reconstructing the whole
- Might have to show this ourselves... Are the NMF modes related to the natural movement statistics?


## Performance

Easy:
- **Plot reward vs. (reach time, path length, and segments) to prove that these correlate with performance as expected**
- **Plot the targets on fig:rotated_trajectories**
- ~~Make a significance matrix for mean comparisons in fig:compare_subject_groups~~
- Discuss degree of freedom freezing in the context of the segments-- segments can be a proxy measure of freezing!
- Put the reward histogram and the hits vs. reward plot earlier, and use reward where we're using hits currently


Not easy:
- ~~Make sure that reward is calculated using the active indices! Figure out how to do this with pandas? Compare hits vs. reward (on the same plot?) to make sure we're not going crazy~~ -- it is! we're using filtered trajectories
- The trajectory variance section is confused and needs rethinking or cutting. The point is to show that trajectory variance decreases over time. This isn't a very interesting point to make, as it's clear that this is the case from the earlier performance plots. Should we really only be looking at the $y$ coordinate since the $x$ coordinate has to vary in order to hit the target? Maybe ideate on this, and think about this as "task space" analysis-- what can we look at the in the task space across and within subjects?

TODO should we show the right-tailed data here too? Should we fit this exponential, in order to say ``across subjects on average trajectory variance decreases'' We could try to relate this to performance, maybe showing correlation between early and late variance? There might be a point made here about exploration in the task space? The original idea here was to explore the task space statistics more fully before getting into the full EMG space. The decoder discussion about normality allows us to say that the decoder is a projection onto a 2d plane, but going from 64 to 2 dimensions also has this concentrating action, so the task space statistics are interesting on their own as well. This is still unrealized here. Unclear what the story can or should be.

TODO? Plot the mean of all subjects decoder arrows, which may help to explain the bias towards the left hand side of the screen? However, this is a weird average to take since the order of EMG channels will differ. I would need to do this using some kind of density plot, overlaying each subject's decoder arrows in 2D. Probably more trouble than it's worth.

TODO?: normality tests on histograms of reward and hit counts per subject, we can justify using the mean reward per subject as a measure of performance as there are not any glaring outliers and the curve is approximately normal, while the hit count curve is skewed

TODO?: Look into the ``freezing degrees of freedom'' idea, defined as the size of the ``active'' EMG subspace within each trial. This could be done using NMF or PCA on each trial, e.g. many PCA components are active at once (how sparse are the component weights?), and how does this change over time? Sparsity (measured by the 1-norm) might imply that only a certain mode is active at a time, and this might change to more mixing over time. We would expect mixing to increase as people become more proficient and blend their activity modes together. This would be quite a rabbit hole, but interesting! We really want to know if people have distinct modes of activity early on, and how these blend into solutions over time. This is tricky to do, and currently lacking between the setup in the background chapters and the current results.




## Manifold

- **Visualize the PCA modes from movement, calibration, trials and compare them! For a few subjects. Are natural movement modes relevant to the task? How do these modes change over time? Try NMF? Don't just say ``hey we can't use PCA'', use PCA as a starting point that's literally a broader view, then zoom in with the GMMs! Do this in the previous chapter.**
- ~~Add GMM fits to each of the toy model examples~~
- Note that this analysis was done in the log-transformed space! Where PCA can be applied! What PCA misses is the mixture of low rank components.
- (More) Clearly explain the concept of the subspaces sooner to nail home the spikiness point, as this is becoming critical for the throughline of the thesis? Have we adequately supported the spiky, constrained manifold?

TODO? Look at the sparsity of the components --- while the number of components needed may be low, those components may not be sparse, they may be spatially spread out? Look at the 1-norm of the component? 0-norm? Gini index?

TODO? generate synthetic data to compare 64D Gaussian distribution with matching statistics from UMAP (this will look like a blob), compare that to subspace confined gaussians?


## GMMs 

Easy:
- ~~Separate the colormaps of the two columns in \Cref{fig:gmm_vs_pca}, it doesn't make sense to share the scale as these will have different variances. The PCA variance is lower because the variance there is additive to reconstruct the empirical covariance.~~
- **combine \Cref{fig:example_gmms,fig:example_trial_gmms}, use the connecting lines to explain how we're pairing the means of the components including the movement and calibration models. Change the targets to unweighted (too much information)**
- write down the math for the difference of component means plus the Frobenius. Here we pair the means of each component from one model to the next using the Euclidean distance in EMG space, then we compute the Frobenius difference between those pairs' covariances. Then we take the mean of that Frobenius difference.

Less easy:
- **Test 2-Wasserstein distance pairing -- we need to be able to explain WHY we're doing these things...**
- **Sample from the model and compare the performance of the model to the subject's performance in terms of hits and reward. This would serve as a practical goodness of fit test and give us better grounds to assess the model fits.**
- Are we clearly explaining the main hypothesis that subjects who are less ``constrained'' are expected to perform better? And how this constraint arises?
- Visualize the GMM modes and point out comparison to the PCA modes shown earlier!


TODO: When we introduce this ``top two singular value'' concept, connect it to the toy model \Cref{fig:toy_model} and the concept of ``effective rank''. That this is a proxy for the rank of the components which make up the mixture of modes in the dataset. PCA can't unmix these modes, so we use GMMs to try to unmix.

TODO Visualize the model components over time for one subject so we can get an idea about the change happening over time on a per-subject basis, this will help us build a more intuitive explanation!

TODO keep thinking about this; not yet a very clear explanation. Needs to relate clearly to the mean and covariance of the model components.

TODO Plot PCA rank vs. reward! Same plot as the GMM models. We expect these to agree with the GMM results, as they're capturing a similar phenomenon, opposed to the comparison between models, which are capturing opposite features of the distributions.

TODO Set up the idea that variance or entropy in the calibration task is good (e.g. in \Cref{chap:methods} when introducing the tasks).


TODO? Show wasserstein pairwise statistics for all trial chunks? Keep these plots, but show the significance matrix?


## Null Space

TODO write the math associated with the task and null space and the projection. 

TODO make some kind of visual to support explaining the task and null space. Even if it's just a plane with some projection lines and arrows.

TODO Think more about how this relates to the hit end results below. How do we expect these things to compare?

TODO Introduce the idea of the ``hit end'' by showing hit ends from a single subject. Explain the ``hit end'' for the miss trials, where we're taking the lowest task-space error sample in place of the hit end. We're calling this a ``miss end''.

TODO Introduce the hit end variance ratio before getting into misses and hits

TODO Think more carefully here. The correlation for hit ends versus reward may simply be due to lower performing subjects having fewer hits, and thus lower variance. We should try normalizing by the number of samples/hits. 

TODO Decide whether this analysis makes sense. Should we instead use the ``error'' between the ideal, zero-null-space-activity solution and the actual subject solutions? These results don't show much shift in the task-null ratio, which might be interesting as it shows that people don't really seem to care about the null space over learning. In theory, using the error removes activity that is minimally task relevant, leaving you with what should be pure nullspace activity, or everything in the EMG that isn't required for the task. This is shown in \Cref{fig:error_nullspace_subjects}. We see a much higher ratio, suggesting that the distribution of error is more aligned to the task plane than the nullspace. 

TODO write down the math for the pseudoinverse solution

TODO strengthen the argument that the task isn't SIMPLY one of reproducing movements made in the calibration task. That yes it's capturing statistics of that task, it's not simply a recapitulation of prior movements. We do have to point out clearly that the task is designed by extracting a plane from subjects' calibration data, and thus the natural manifold is biased in the direction of the task. However, taken in combination with the GMM projections, we don't think this is merely an artefact of the task structure. (E.g. show the decoder weights relative to natural movement modes? calibration modes? )

TODO reflect all these results together to form a coherent story.

TODO Is there a way to compare the variance projection of the error distribution to a null hypothesis? If subjects were to move randomly according to some simpler distribution? Or can we compare the error here to the natural movement or calibration data somehow? The problem with this is that there is no ``solution'' to use to compute an error signal. Need to think about this.

TODO Think harder about why the GMM has a lower similarity to the subject solutions than the other solutions. I think this is simply an artefact of the GMMs being overfit, and thus these solutions are very ``specific'' to those datasets, while the other solutions are more generic. So subjects are generating solutions that are in line with their prior statistics, but that are unique to the target task itself, not just rehashings of movements that were made prior, on average.

TODO Change cosine ``distance'' to similarity (0 to 1)

TODO Is this again due to the amount of data we have for subjects? Can we normalize somehow normalize this by the number of hits to check?

TODO Put all of these results together. What do they all point to? The best summary I have now is that subjects are fundamentally constrained by their underlying EMG manifold in succeeding in the task, and this is not taken into account in the way the decoder is computed. Despite this, however, subjects still learn to varying degrees. They are biased by their prior statistics, but not enough not to carve out new solutions for the task at hand. The solutions they do discover seem to mostly disregard the null space as task-irrelevant, pointing to a kind of model-free learning happening on this time scale.

TODO? I think it would be really strong to dig further into one or two subjects' solutions and visualize things as if I only had this data. This might give better context for the subject-averaged results, illustrating how this plays out for a single subject.