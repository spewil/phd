analysis_notes.md

quirks
- if you No Hold x4, you skip that target for the session..... this is awkward.
- for a No Hold, the data is recorded with the same trial prefix, this is the "target" prefix... 

data mgmt
- make a "rules" list to check when going through the data? (e.g. skip session 3 for X, etc.)
- make it such that I can use Paths and pull things that way from my s3 buckets or locally

todo
- determine how many no-holds for the same target in behavorial outcomes-- produce a picturre of "cleaned" outcomes 

what predictions are we making?
- forward model, dynamics, p(state' | state)
- inverse model, actions, p(motor command | state, behavioral goal / future state)

questions
- what is the sample rate? how long in time is a single step in the data?
    -  I think it's 1/60th of a second, because it's driven by the framerate of the game