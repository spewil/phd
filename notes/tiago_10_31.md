tiago_10_31

update:
- way too long thinking about how to rotate EMG to compare across trials, did this for trajectories

- realized that the way the task works is subjects need to produce a force output-- the control signal IS the state
    - means optimal control stuff doesn't quite make sense
    - means they're directly learning some linear model of the mapping

- need some way of dealing with the time course of each trajectory-- boiling this down into something we can work with
    - probably getting rid of data, e.g. look at the "active" parts of the trajectory (movements near possible targets?)
    - tried filtering on trajectory, but this doesn't make sense, since you can have nullspace activity without moving in task space
    - people are going to do things that move them around in task space


ideas

- close out the nullspace stuff after finishing the activation filtering
    - filter for active parts of trajectories
    - are we taking the residual? need a good filter if so... 
    - just try this and write it up
    - re-run nullspace per trial? average trials?
    - write this up to understand the story
    - why we did this, what we tried, etc.

- focus on less data, e.g. the EMG-as-dart-throw metaphor
    - how do I deal with misses, or the other "attempts" by subjects?
    - I can look at the filtered version
    - whatever subjects produce is a "guess" at the solution
    - how do we define these "guesses" in a way that can be compared across trials?
    - try filtering the data to only get the "guesses"

- EMG variance over trials 
    - this is a kind of "modal analysis" -- where is the variance spatially along emg channels?
        - what distributions do we want to look at variance of?
    - relates to the nullspace-- that says along which dimensions does the variance lie
        - this is where spatially is the variance
        - what would we expect?
        - we might expect that over trials, subjects converge to the mean solution?
            - if we look at residuals, does variance go down for residuals over trials?

- focus on trajectory data only?
    - can rotate to compare all targets at once
    - normalized time per trajectory
    - variance over time (ellipses) -- over time, over trials (only in the task space)
    - where is the variance in a normalized trajectory? how does this change over trials?
        - can we compare this to the variance in EMG space? what is a good measure of variance in emg?
        - look at variance measure within trials for null and task?


todo
- X get some kind of "activation" filter defined
    - X look at trials with very few "active" samples, have a minimum
- X use that filter to compute nullspace between end of hits and active parts of all other trials
- break this down between hits and misses? but note there aren't that many misses... 
- X try this where we subtract the hit mean to generate a residual -- this doesn't make sense! 

- think about modes, variance in the signal over TRIALS -- consolidate over timepoints
- e.g. where is the variance in each trial spatially (covariance?), how can we plot this over trials
    - 64 x N_trials? 
    - can we relate this to target trials? can we look at the residuals?

things we're looking at
- avg var in task and null space directions
    - for the endpoints
    - for the "active" guesses by subjects

- var in task/null over trials
    - how do these evolve over trials?
    - are subjects exploring more in task or null? (is the var higher in task or null)

- over channels, where does variance live?
    - this isn't all that interesting, the spatial variance isn't super interpretable?
    - we're relating it to task-relevance and irrelevance through the decoder
    - this is the modes-- does the long-tail of the PCA modes change over trials? more or less "stereotyped"?
    - does activity correlate with natural modes more or less?

- looking at subject "solutions" -- what can we learn about how this relates to the decoder?

notes
- subtracting a mean to shift the signal does nothing for the covariance! it's an offset, get's rejected by the mean... lol
- think more about how to 

---

other things mixed in with nullspace
- recovering the emg -- clean this up in a new sheet to present the signal processing
- least squares stuff -- break this into a new sheet
- target rotation example
- all targets rotated, normalized in time, plot the trajectory variance over trial time, over trials, over subjects
- signal-dependent noise... not sure how to show this... trials with higher mean activity should have higher std? 

data we need
- number of hits per subject
- task,null,ratio variance of "active" emg activity per trial
- avg of each ^ per session
- task,null,ratio variance of "hit ends"

list of nullspace variability plots we want
- X activity filter example -- show two trial emg+traj and when it's active (short, long, etc)
all with "active" samples:
- number of total hits vs. mean [task var, null var, task/null ratio] for all subjects
- task, null, ratio var over blocks for all subjects, and subject mean per block
- example of one subject's hit ends emg, and mean/std
- per target task/null ratio of hit end projection across subjects, and their mean

todo
- put functions into `collection` so this is already done for us
    - null spaces
    - active samples
- make some convencience filtering functions for hit trials, etc.
    - 
    - add trial number in the big list
- produce some summary average plots -- consolidate null space work so far!!
- with those results, brain dump the current thinking, tidy up the plots, etc.
