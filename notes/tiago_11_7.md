tiago_11_7

update
- go through variance ratio stuff
- we recover some expected and some surprising results from the variance subspace analysis
    - expected -- we're seeing that the "solutions" subjects find to their problem are in accordance with literature (low task / null variance)
        - based on looking at all hits for each target, ONLY taking last 5 samples from the "Hit" timepoint (5/200 = 0.25sec)
    - we're also seeing that "movement in general" ("active" emg samples) does not accord with the literature (high task / null variance)
        - though we need to think harder about the stats-- would using less data to produce the covariance ensure this was the case?
            - we could check this by computing a short slice of data from within the trial NOT at the end? what's the prediction here and why?
            - if we can sort of debunk this, what does that mean?
                - don't do the comparison! 
                - get tricky, only compare equal length slices?
    - we're not seeing variance change over the session in terms of task and null, over time
        - however hits do change over time, so something must be changing at the trajectory / emg level! what is it?
            - our hypothesis here is that what changes is something about the "effort" of the movement? but not necessarily in null/task space?
            - 

notes
- why more variance in the task space? because they have feedback there?
- more likely to move in the nullspace if moving randomly? assuming equal activity across channels
- moving optimally would mean getting feedback, which comes from moving in the task space
- over trials, look only act activity in the nullspace-- does it decrease (finding the task plane)
- our assumption is that people want to make smooth, cosine-velocity, straight-line rectilinear movements
- "Quadratic forms appear when studying the variance of a dataset. If C is the covariance matrix, then the variance in the direction defined by a unit vector u is u'Cu"
- note that the covariance is of course the dispersion around the mean-- we have to be careful to interpret this as such, think about what low- and high-var trials mean!
    - what would we expect from an optimal controller?

todo
- take more "hit ends" samples! does this change things?
    - yes, with 15 samples averaged: array([1.29356638, 0.99714795, 0.83137877, 1.35087351, 0.9906097, 1.11008976, 1.2794176 , 0.99457665, 0.97077403, 1.26228672, 1.16839835, 0.94437787])
    - with 10 samples averaged: array([0.86427778, 0.63130813, 0.51341782, 0.90867263, 0.60925327, 0.71606523, 0.84308134, 0.58683775, 0.59997757, 0.85101878, 0.72133085, 0.58348162])
    - with 5 samples averaged: array([0.40543724, 0.29683056, 0.23553798, 0.42920112, 0.27790572, 0.33274453, 0.38942939, 0.25033928, 0.27024989, 0.41164893, 0.31751965, 0.26080828])
- compare hit end ratio to short slice of data ratio to check 
    - ~~this WILL change things, because it's all based on the covariance of these samples~~
    - the more samples, the higher the covariance by definition...? 
    - Oh! but it's not each trial, it's ALL hit trials -- the numbers are the numbers of hits, so anything from 0 to 45
        - full trials are ~100s of samples... 
- over blocks, plot task and null variance itself, rather than ratio


next chunks
- cluster subjects? (do they cluster?)
    - look at the best performing subjects
        - what is best? hits, smoothest movements
        - composite subject across targets?
    - by variance ratio, other measures?
    - what numbers can we ascribe to subjects?

- trajectory variability in over trials
    - normalize the time within 
    - look at stddev of traj at each time point
    - should decrease?
    - plot the mean trajectory for each target and all stddev
    - plot stdev

- trajectory endpoint variability (a la van beers)
    - trajectory endpoints -- can we do this, since the target is so big?
        - plot these and see, for hits
    - emg endpoints -- just the last bit of the emg
        - how would we visualize this? does this even matter to us?
        - maybe over subjects we can 

- emg 
    - task / null space
        - plot the directions outright, look for temporal patterns here
            - make a heatmap of the variance in these directions over trials for a subject
            - think about how to reduce this? depending on what we see over subjects 
    - "structure" of the covariance per trial (but not caring about task/null)
        - task/null -- these are set directions in emg space by the task (but produced by NMF-->decoder)
        - SVD/PCA -- "highest variance directions/channels" --> ?
            - relate to natural movement?
            - how far are these high var directions from natural movement directions
            - does this change over time?
            - hyp: you start out with nat movement, and then you diverge
        - SVD/PCA -- "highest variance directions" --> ?
            - people figure out the task plane quickly, THEN learn to do the task with that subset of movement on the task plane
            - "clunky" movements (get some hits, find the plane) --> start making new movements exporing in the task plane --> 
            - are people exploring the null space to "find" the task space?
            - hyp: people are "rooting" their exploration on known movements -- but THEN what do they do?
    - variance of channels across trials
        - heatmap of variance 
    - variance in decoder task / null space dimensions
        - heatmap? 64 x 45 plot?

- dimensions of the data
    - subject 46
    - targets (12)
    - trials (540)
    - emg over time (N)
        - channels (64)
    - trajectory over time
        - dimensions (2)


other topics of interest:
- what do we predict happens over trials?
- what generates variability that we see? what would account for the "shape" of the variability?
- what is the variability for an optimal controller in the normal case?
    - can we "fix" the optimal controller by penalizing it from some natural repertoire?
    - the penalty here is a notion of "distance" from a "default policy" defined by the natural repertoire?
    - or perhaps literally a penalty for the controls being far from a representation of the natural repertoire?
    - "policy complexity"? 
- we see subjects making a lot of mistakes-- can we characterize these?