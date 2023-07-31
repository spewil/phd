# Analysis Ideas



* [ ] defend: is this paradigm suitable for studying motor learning?
* [ ] how does the paradigm test the optimal control hypothesis? does it support or reject it?
* [ ] how does the paradigm help us untangle the speed of human learning? what enables humans to learn so quickly? how does the paradigm help build a picture of this?



what OFC model would fit the data at each point? reconstruct / fit the best controller?

to disambiguate model-based and model-free, look at "adjustments"-- online corrections find examples where noise or something deviates, and an adjustment is made have a rule for adjustments, and scrutinize the movements after the adjustment can we do this on multiple timescales? find a space where adjustments stand out (velocity?)

sensory prediction reward prediction (we know the reward structure)

calibration

* strategies low-to-high or high-to-low?
* any features across trials? (same strategy?)
* "null" and "non-null" space?

directions of modes relative to targets correlate with performance? alignment of dominant modes with target directions

* dominant modes-- projections of random emg? eigendirections?
* alignment = cosine distance

is the calibration the same each time? (the target bar order will be different, but the layout is the same?)

do people actually achieve the bar task? better than random? what is the metric of success? what is the null?

data organization

* how to ignore no-holds...?
* query the data without holding it in memory? (API for the data, effectively)

structure of variability learning curves along dimensions modularity -- which dimensions are controlled?

freezing DoFs?

quantify sample efficiency?

are cross-trial learning modes similar across subjects?

first movement as a plan/feedforward? hits per target (polar plot) movements in total (polar plot) score calibration task? SNR of baseline signal? correlates with success? classifier training on natural movement data? to then classify initial movements? hierarchy? dimensionality over time? feedback after initial movement what is a correction? time of day of recording correlates?

movements and their opposites (agonist/antagonist pairs) are a strong prior!

are similar movements made after they are rewarded?

are some decoders more aligned to the targets?

by friday

* behavior statistics
  * hits
  * misses
  * time to hit
  * length of trajectory?
* trajectory statistics

some directions are more difficult -- can still measure ability even without the hit (e.g. andrei whose force level kept him from moving left easily...:(

andrei -- level of required force? need to control for this as well

plot arm size vs X plot overall force / variance vs X action distribution statistics vs X

coffee drinkers and non hours from lunch sleep hours

bottleneck

* between trajectory (or some feature thereof) and target?
  * how well can we predict target from trajectory? or vice versa?
  * this means how well can subjects infer motor activations given target (the policy)

people tend to make other movements over learning, of the head and body, of the other hand. this may aid in memory of particular movements?

does "no hold" correlate with success? total number next trial

you could get lucky where the principle directions are directly to targets... in this case, do you keep doing what you're doing? or do you hone in the movement?

***

experimental - emg validation -- what features exist in the data? - skill learning -- is LQG a reasonable model for emg control? - perturbations post-learning -- what kind of modularity do we see in the data?

theoretical - lqg composition -- can this explain adaptation? - lqg selection -- can this explain perturbation response?

***

dec 15th

PCA on each trial -- look at dimensionality over trials?

* how do you control for different targets? or just look at the same target?
* does the dimensionality change?
* do the components change?

what data do i generate to learn trial-to-trial

1. what do people do?
2. what is "optimal"? are people optimal?

what distribution should I draw EMG samples from?

i have a policy each trial

this is a sampling problem?

* straightforward annealing? -- temperature goes down monotonically (PCA dimensionality as a proxy for "temperature"?)
* adaptive annealing? temperature changes based on performance, or some other feedback (i'm not doing well, I'll start exploring more)

loss function

* straight line movements in output space
* minimum variance movements in the input EMG space

sample transition function

* where do I sample from next?

optimal could be defined as the norm-minimizing inverse mapping, which would minimize the action in the null space?



\---



* [ ] get behavior
* [ ] transform emg and compare post hoc
* [ ] try UMAP to compare subjects?
* [ ] run NMF on other calibration task
* [ ] \--- plots ---
* [ ] arm size vs performance
* [ ] time of day vs. performance
* [ ] amount of force vs. performance
* [ ] decoder correlation vs. performance
* [ ] \--- fun ---
* [ ] amount of coffee vs. performance
* [ ] instruments / non vs. performance
* [ ] neuroscientist vs non
* [ ] — further afield —
* [ ] differential games?
* [ ] mean field games?
* [ ] VAE
* [ ] VIB -- on MNIST / images?
* [ ] Hopfield Network (MNIST) (associative learning rule)
* [ ] bottleneck / modular RNN?
* [ ] CCA -- IB (theory) -- projections across learning? what projections highest correlation across learning... ?
* [ ] non equilibrium system analysis -- dynamical modes?
* [ ] covariance decomposition over time?
* [ ] sequential components analysis -- code and test this!
* [ ] DCA (bottleneck type thing)
* [ ] slow features?



\---



* Basic overview of experiment and results
  1. Description of everything
* Learning
  1. Behavior statistics
     1. Hits
        1. Polar plot –– per target
     2. some directions are more difficult -- can still measure ability even without the hit
     3. Misses
     4. Time to hit
     5. does "no hold" correlate with success?
        1. total number
        2. next trial
  2. Trajectory statistics
     1. Length
     2. Noise / width of distribution?
     3. action distribution statistics vs ?
  3. What correlates with learning
     1. Aspects of the learning task itself
  4. Learning curves along (EMG) individual dimensions?
  5. To disambiguate model-based and model-free, look at "adjustments"-- online corrections
     1. find examples where noise or something deviates, and an adjustment is made
     2. have a rule for adjustments, and scrutinize the movements after the adjustment
     3. can we do this on multiple timescales?
     4. find a space where adjustments stand out (e.g. velocity?)
  6. EMG space
     1. "null" and "non-null" space? How do we find each of these? How do we interpret the high-dim null space?
  7. Calibration statistics
     1. strategies low-to-high or high-to-low? (total force)
     2. any features across trials? (same strategy?)
     3. is the calibration the same each time?
     4. (the target bar order will be different, but the layout is the same?)
     5. Score?
  8. Movement
     1. SNR of baseline signal? correlates with success?
     2. classifier training on natural movement data?
     3. to then classify initial movements?
  9. Hierarchy?
     1. dimensionality over time?
     2. What is a module?
     3. How many discrete movements? (behavioral modularity)
  10. Force
  11. Higher force initially (in calibration) seems to mean difficulty later
  12. E.g. andrei -- level of required force?
  13. Random Correlates
  14. Time of day
  15. plot arm size vs X
  16. plot overall force / variance vs X
  17. coffee drinkers and non
  18. hours from lunch
  19. sleep hours



* Analyses of learning
  1. EMG→behavior
  2. What / how are people learning?
     1. E.g. trial-to-trial reward
     2. What happens after rewarded trials (on average)
  3. What errors are at play?
     1. Prediction error (prediction of target?)
     2. Error in EMG space and in behavior space
  4. first movement (of each block?) as a plan/feedforward?
  5. Games’ modes (NMF factors, decoder)
     1. directions of modes relative to targets correlate with performance?
     2. alignment of dominant modes with target directions
     3. dominant modes-- projections of random emg? eigendirections?
     4. alignment = cosine distance
     5. you could get lucky where the principle directions are directly to targets... in this case, do you keep doing what you're doing? or do you hone in the movement?
  6. Bottleneck between trajectory (or some feature thereof) and target?
     1. how well can we predict target from trajectory? or vice versa?
     2. I.e. how well can subjects infer motor activations given target (the policy)?
  7. Freezing DoFs?
     1. How many e.g. PCA components are active at once, how does this change over time?
  8. “structure of variability”
     1. Which dimensions / space does variability live in?
     2. How does this change over trials?
  9. Modularity
     1. which dimensions are controlled?
     2. Controlled here maybe means lower variability… or it means more responsive to errors? Might be the same thing…
  10. agonist/antagonist pairs
  11. movements and their opposites are a strong prior!
  12. Can we connect modes to behavioral directions?
* Models of learning
  1. Why are people learning what they’re learning?
  2. Why are people learning how they’re learning
  3. what OFC model would fit the data at each point?
     1. reconstruct / fit the best controller?
