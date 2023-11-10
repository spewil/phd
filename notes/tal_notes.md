tal feedback

log axes for performance plots
are people "exploring" in the calibration task?
what IS predicting performance in the task, if not the decoder correlation?
- constrained activity in the calibration task? PCA / covariance eigenvalues? how varied is the movement in the calibration?

- plot decoder alignment radially
- only plot one quadrant of the decoder-- these are literally the same for the sign-inverted directions (lol)
- do we see significance in the x-direction of the decoder and the y direction?

how similar are subject decoders?

moving left is hard? is this significant? why would this be the case? maybe something with how the decoder is computed?

factor in the length of the decoder directions into the performance prediction/correlation


NMF:
-x
+x
-y
+y

D = [+x - -x, +y - -y] 2x64

performance (hit or miss) over trials = A * decoder + b
A = trials x 2*channels

trial to trial correlations -- look at EMG correlations

-- 

make movies of subject trials! like philip's rat trials

-- 

1. most of the nullspace variance SHOULD be low, by design, because the decoder's job is to extract variance from a hi-D signal
2. BUT the subjects don't know anything about their decoder, so we would still expect to see some changes in relative task and null space variance

plot individual subject ratio means over blocks to see if there are trends?

i think there is a better metric, since we expect a priori for most of the signal variance within trials to lie within the task space based on the decoder being fit more or less to the EMG signal variance by design. subjects dont know this, and they're exploring to find what the decoder picks up, that is what channels are important or should be higher variance to succeed in the task. by that logic we would still expect people to find the task space, limit their variance to what's required to succeed in the task, and null space variance could creep up. but actually they might not even be able to produce null space variance at all, thus we'd expect it to stay low. 

just look at task space variance over trials? just at null space?

what is a perfect trial? (in terms of variance)

-- 

todos

- X make movies of the trajectories for a subject, split into targets, etc.
- X plot just task variance and null variance separately over trials
- X redo decoder correlation without normalizing length 
- look at calibration task PCA, measure of spread / variance -- distribution along axes

- fix target specific plots
    - means over subjects -- only need one quadrant
    - plot target specific -- 
- look at pairwise correlations between subject decoders -- why?

--- 

after looking at all trajectories:

- what correlates with task success? hits is a poor metric, looking at the plots, some subjects are all over the map, some are really honing their movements
- look at PCA over all trials, spatially, to see what the dominant spatial modes. compare each trial's spatial modes to the overall modes-- are we getting closer to "ideal"?
- look just at best subjects for trial / task ratio -- what happens for the "best" subjects? 

variance ratio
- the analysis doesn't make sense-- we dont want difference from the mean, we want dispersion around the mean of the residual between the "instructed" actvity and the activity produced. if we believe that the "desired" activity is constant, then we might be ok. but the analysis as-is basically just says that the activity in the task space is larger because that's what affects the task. we want to remove the task activity and just look at the "noise" between the two spaces. maybe if we somehow compute activity that's in the direction of the target and subtract this off, that would give us a kind of residual to look at?
    - each timestep, what "direction" are we pointing spatially? (is this the force_X, force_Y? or the derivative?)