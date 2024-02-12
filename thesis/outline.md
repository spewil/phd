# NOTES AND MESS

## internal model <> nullspace
- based on the variance ratio results, we think (most?) people aren't internalizing the decoder, we don't see a reduction in variance in the task space. people aren't honing a flexible strategy because they don't seem to be "finding" the decoder
- this leads us to think that people are learning rote movements, they're not learning the decoder directly. 
- we don't see people honing the decoder, as theyre disregarding the null space.

## evidence supporting "model-free" learning in the task
- do we see evidence that people are using memory of rote movements to succeed in the task?

## what would support model-based learning?
- corrections allowing for variance in the nullspace-- maybe a more finegrained analysis of individual movements
    - could we do this quickly with e.g. the top performing subject?
    - do null space trajectories correlate for hits?
        - **do PCA on individual trials' nullspace covariances**
        - look at the spatial PCA modes for each trial-- which channels are active in that trial contributing to the nullspace
        - are these similar over trials? 
        - alternative-- nullspace is gaussian noise

## alternative model
- take the task space projection, then add gaussian noise as the null space, using the same mean and channel-wise variance as the null space!
- 


# OUTLINE 


# Intro & Motivation & Lit Review

- What are our goals? What are we trying to achieve? Why are we setting up this task? 
    - We think this will “stretch out” learning and let us look at the redundancy problem from a new perspective. We want to give subjects a more naturalistic environment in which to solve a motor problem.
    - This is at odds with typical motor tasks, gives us more control at the redundnancy problem 
-  We want to look at intersubject variability– do people use similar “strategies”? 
- Do subjects end up using statistically similar solutions? 
- What separates learners into high and low performers? What predicts differences in performance?
- Explain learning from a statistical point of view– what is actually being learned? Is there a general learning principle across subjects?
- How do subjects fare with identifying the task plane/decoder?
- Presentation of the paradigm; What’s come before? What did they find?
- Background on what’s been done – lots of experimental control, lots of RL, some redundant mapping tasks (cyberglove, other EMG work), but not much combining questions of how subjects learn, and what their learning updates look like– what shape do solutions take, and is there a generality in this shape?
- While motor control has many results, most of which focus on optimal control, we’re interested in motor learning– how can we stretch learning to get from “zero” (or do we ever start at zero?) to performant? How do we develop a new skill? How do we learn to control in a new context/environment/contingency? If subjects in motor tasks tend to reach certain definitions of optimal performance, what comes before optimality?
- What kind of task/experiment should we devise to tackle these questions? What unique vantage would this paradigm offer that existing paradigms do not?


## What’s the goal of this project? What are the driving questions?


What do subjects learn? Do they learn specific rote movements, or are they flexible in their solutions? 
How do subjects learn? What “route” do they take?
What did we do? Did it work?
What does the “raw” data look like? Trajectories and EMG, measures of dimensionality, topology/UMAP
How can we filter data to show only active samples?
Did subjects learn the task? What correlates with their performance?
What happens to subjects' trajectories over trials?
Mean, variance, task/null space
Why does the data manifold have the shape it has? 
What is behind the X pattern from EMG to trajectory?
Can we fit a model to this data to capture the shape of this manifold?
How do subjects’ EMG solutions compare to optimization-derived solutions with varying levels of prior influence? I.e. Are subjects biased towards their prior data?
Do the variances of subject errors (subject solution - optimization solution) lie in the null space directions on average or not? I.e. Where do subjects expend most of their variance beyond 


# TODO 

Work back through the activity filter thing to make sure it makes sense statistically and we can defend it
Norm of EMG → histogram per trial → look at the distribution of this, should we log-transform it into a rough gaussian? → what is the variance cutoff we should use here? Mean +/ N*sigma, what is N to reject outliers? What do we do if the data isn’t gaussian even after log transforming?
Once we have our cutoff, we mask emg leaving only samples 
that fit within our defined activity window
Visualize norm histograms to check for outliers, weirdness
Make a rejected subject list
Pick a low and high threshold and stick with it
Make sure the subject ordering is alphabetical / same as “subjects”

Lognormal mixture? Or log transform then fit?
PDF when transforming gaussian rv to log-gaussian rv https://stats.stackexchange.com/questions/214997/multivariate-log-normal-probabiltiy-density-function-pdf
PDF when exponentiating gaussian to get lognormal? gauhttps://stats.stackexchange.com/questions/89970/exponential-of-a-standard-normal-random-variable

### GMM elbow analysis – choose a number of components
Make sure to deal with 56 being 0 
Compare raw and log’d data
Do this for highest, lowest, and median reward subjects
Do this for movement, calibration, chunks of trials
Calculate scores for choosing the number of clusters… 
Pick a number of clusters! But then need to re-run these… 
Looks like 8 based on silhouette scores… 

(Refit and) check validity of prior and trial GMM fits
Refit for log’d data
Transform log’d fits back to EMG space
Plot reconstructions of covariance
Plot means and covariances
Plot on top of datapoints

Compare subject EMG solutions to optimization solutions
NB https://math.stackexchange.com/questions/2028698/
Hypothesis: subject error ratio of err_pinv / err_weighted will be > 1 as subjects tend to minimize their error to the prior-weighted solution rather than the pinv solution.
Todo – use a metric
Check if fitting different subsets of the prior data with GMMs makes the distance thing work out! 
Try calibration only
Try movement only
There is a result here regardless of the outcome!!!
This is about choosing a cost function and comparing to the data
Can I fit a cost function to the data? This is like fitting a model… 
We know subject solutions hit the target, but what do they minimize over time?
Can we regress these solutions against potential regressors?

### Dimensionality with PCA

Toy lognormal model to show X-pattern

Visualize trajectories and their statistics nicely
Visualize trajectories
Figure out how to compare across targets (rotating?)
Trends in trajectory stats? Means and variances of histograms

Get RL simulations for the task working, including prior
Set this up locally
Work out the math for the KL PG thing
Code that up and test the prior
Story: the kind of go-to, prior activity influences / correlates with ???
Show this with prior bias and without, then compare
Figure out how to compare with the data

Write up math for everything… This shows your theory thinking is sound

Compare Prior GMMs to Trial GMMs – statistical distance / KL… 
Look at samples from these next to real data 
Relationship to trial GMMs?
Larger variance?
Similar means?
Distance?
Alignment?

Dig into trial GMMs
Null/task space – where do the gaussian fits live? Project the covariances independently, show change over time? But note that this is NOT the “noise” of the error, it’s the noise around the mean solution to the problem.

Compare subject activity to computed solutions
Nonnegative min-norm solution - activity = mostly in the null space or task space? This says something about the error! Does the error live in the null space or task space, does this change over time?
Look at the subspace projections of this error – this should tell us whether we’re in the null space or not! Since what’s required for the task will be subtracted out
Does this change over time?
