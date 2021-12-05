# analysis ideas

what OFC model would fit the data at each point?
reconstruct / fit the best controller?

to disambiguate model-based and model-free, look at "adjustments"-- online corrections
find examples where noise or something deviates, and an adjustment is made
have a rule for adjustments, and scrutinize the movements after the adjustment
can we do this on multiple timescales? 
find a space where adjustments stand out (velocity?)

sensory prediction
reward prediction (we know the reward structure)

calibration 
- strategies low-to-high or high-to-low?
- any features across trials? (same strategy?)
- "null" and "non-null" space?

directions of modes relative to targets correlate with performance?
alignment of dominant modes with target directions
- dominant modes-- projections of random emg? eigendirections?
- alignment = cosine distance

is the calibration the same each time?
(the target bar order will be different, but the layout is the same?)

do people actually achieve the bar task? better than random?
what is the metric of success?
what is the null?

data organization
- how to ignore no-holds...?
- query the data without holding it in memory? (API for the data, effectively)

structure of variability
learning curves along dimensions
modularity -- which dimensions are controlled?

freezing DoFs? 

quantify sample efficiency?

are cross-trial learning modes similar across subjects? 

first movement as a plan/feedforward?
hits per target (polar plot)
movements in total (polar plot)
score calibration task?
SNR of baseline signal? correlates with success?
classifier training on natural movement data?
	to then classify initial movements? 
hierarchy?
	dimensionality over time?
feedback
	after initial movement
	what is a correction?
time of day of recording correlates?

movements and their opposites (agonist/antagonist pairs) are a strong prior!

are similar movements made after they are rewarded?

are some decoders more aligned to the targets?

by friday
- behavior statistics
	- hits
	- misses
	- time to hit
	- length of trajectory?
- trajectory statistics

some directions are more difficult -- can still measure ability even without the hit (e.g. andrei whose force level kept him from moving left easily...:(

andrei -- level of required force? need to control for this as well

plot arm size vs X
plot overall force / variance vs X
action distribution statistics vs X

coffee drinkers and non
hours from lunch
sleep hours

bottleneck
- between trajectory (or some feature thereof) and target?
  - how well can we predict target from trajectory? or vice versa?
  - this means how well can subjects infer motor activations given target (the policy)
 
people tend to make other movements over learning, of the head and body, of the other hand. this may aid in memory of particular movements?

does "no hold" correlate with success?
total number
next trial

you could get lucky where the principle directions are directly to targets... in this case, do you keep doing what you're doing? or do you hone in the movement?

