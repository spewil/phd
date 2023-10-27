Meeting with Tiago

# Update

- realized we're not subtracting out the mean of the activity in the trials, so our variance analysis is flawed. we want to look at the variance of the residual activity, decoupled from the task (the mean)
- our claim for the ideal trajectory is essentially a step function-- you hold until you're ready to move, and then you excute a movement that "pushes" the cursor into the target
- going from ideal trajectory to EMG means making a claim, a model for the solution. The point of the task is redundancy, and we would have to propose a solution scheme for solving this task
- I tried using least squares, fitting a linear model, but this doesn't do what we want (we get a sort of trivial solution that doesn't take into account any of the priors we have about the EMG signal)

## Notes from chat

How to get the ideal trajectory
- Plot the step function thing for visualization purposes
    - this is the optimal outcome we're expecting
- Use the data itself -- try taking a mean from the best trials?
- Find the "best" trial -- the one closest to the ideal?
    - common for the subject not to have any perfect trials for a target
    - If we can do this for all/most subjects, codify this into steps
    - if we can't, can we limit ourselves to just these subject and targets for which they have "ideal" trajectories?
    - this can be at specific time points-- instantaneous EMG activities, nothing temporal
    - all the data can be treated *spatially*, we don't care about the time courses right now, make it simple!
        - imagine each set of trials (without the hold period) as samples from force/emg distrubution
        - any samples that aren't the target force level is error-- what is the shape of that error?
        - how do we get around the fact that it takes time, some dynamic, to produce the target activation?
- what if the "best" trial is defined as an optimal control solution? so we're explicitly defining a cost function?
    - we can quadratically penalize the position and control vectors
    - we can hack this to make it into something we expect in our task
    - can we try this, and compare it with the "best" subjects+targets?
- Compare the data-driven with the handmade
- Use that trajectory's corresponding EMG signal as the "mean"-- are we taking the mean of EMG?
    - this could work... we'd average out any activity that isn't task-relevant? but also means we're removing "idiosyncratic" movements if they're repeated, which we would like to see?
- Visualize the residuals-- what do we see across similar trials?
- Bonus -- test "zeroing" the EMG offsets? Does this matter for the mean?
- Go back to the nullspace analysis, using the residual, compare results

= 
- a definition for ideal trajectory
- pulling this ideal out of our data
- viz of using this to produce residuals
- 

- Bigger chunks of work right now
    - intro, motivation
    - methods, validation of the experiment
        - reconstruct the emg
    - Performance correlates -- still some work to do here, especially with the calibration task correlations
        - correlate what's happening in the calibration ("size" of the distribution (determinant of covar? moments?)) with performance
        - decoder work
    - nullspace variability -- paused until we can figure out how to get a reliable "residual" activity
        - ideal trajectory discussion here about what we're calling ideal
    - trial-to-trial, modes
        - looking at trajectories only?
        - how do individual trial modes compare to "best trials" and all modes?
        - how do you validate whether your mode analysis is sound?
    - optimality
        - ? 
        - what are people optimizing for? if people (or best learners?) are optimal, what is their cost function?
        - are people learning optimally trial to trial?
    - conclusion, outlook
        - great platform for motor learning
        - careful experimental design (provide some ideas about future experiments)

what big chunks do we have?

- intro
- methods, setup, hardware, confirming experiment
- description performance -- correlates of learning, why are some subjects better than others?
- nullspace variability -- can we prove / disprove this with our data? why/why not?
- PCA, modes -- peeling back trial to trial learning, WHAT are people learning (if they're learning model-free, brute force way?)
- optimality(?) -- if people are model-free / whatever, what does optimality mean for them? are they optimal?

review chunks
organize these into the PDF document
start writing simple bullets about each as we go, building up the document, like a lab notebook