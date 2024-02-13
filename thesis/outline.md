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


# TODO 

### Get RL simulations for the task working
    Set this up locally
    Work out the math for the KL PG thing
    Code that up and test the prior
    Story: the kind of go-to, prior activity influences / correlates with ???
    Show this with prior bias and without, then compare
    Figure out how to compare with the data