# Analysis Ideas


Big chunks
- Decoder analyses
- Uncontrolled manifold hypothesis, do we accept or reject?
- Dimensionality, hierarchical, feature learning... one solution or many?
- OFC hypothesis, do we accept or reject?
- The "sampling" perspective
- The "policy" perspective


## Defending the Paradigm

* Is this paradigm suitable for studying motor learning? What are its strengths and weaknesses? Why does the paradigm help build a picture of human motor learning beyond the state of the art? Are subjects actually learning the task? Is the task difficult enough to pose a learning challenge for subjects? What unique vantage does this paradigm offer that existing paradigms do not?
   - 

* How do we define performance in this task?
   - hit percentage (total, per target (polar plot))
   - length of trajectory
   - trajectory difference from straight-line path? "Curviness" of trajectory?

* Performance correlates, based on various measures of performance
   - Arm size vs performance; Issues with the band on larger arms? Less decoupling of channels?
   - Baseline EMG SNR vs. performance; How does noise influence performance?
   - Force/variance/power vs. performance; How does self-generated noise influence performance?
   - Signal magnitude in the calibration (variance.bin) vs. performance
   - "No hold" vs. performance; Do subjects who fail more at the start do better or worse?
   - Amount of coffee vs. performance


## Analyzing the task structure: digging into the decoder

* Transform emg with the decoder and confirm that saved data matches

* Do the directions of decoder directions correlate with performance?
   If the dominant modes align with the target directions, is performance predictably higher? (Alignment can be defined as the cosine distance, for instance)
   If the principle directions are aligned to targets... in this case, do you keep doing what you're doing? or do you hone in the movement?

* We used NMF to produce decoders from one of the calibration task datasets. Run NMF on the second calibration task dataset and compare the results to confirm that the EMG space was captured. Determine a difference between the two decoders and see if this correlates with success metrics.

* Are people better than random at the calibration (bar) task? How do we define success? What is the null hypothesis (e.g random EMG)? This task defines the decoder, and thus it is worth confirming that it is successful in endouraging subjects to explore their EMG space. We can compare their activity to the natural movement datasets as a baseline.


## Uncontrolled Manifold Hypothesis

* What does activity look like in the "null" vs. "non-null" space? How do we find each of these? How do we interpret the high-dim null space? look at classic nullspace variability papers

* Which dimensions / space does variability live in? How does this change over trials? PCA captures the dominant dimensions of variance. “structure of variability”


## Structure within trials 

* Structure of variability learning curves along dimensions modularity -- which dimensions are controlled? how "modular" or "hierarchical" are movements (in space and time)-- can we simplify movements?

* Freezing DoFs? How many e.g. PCA components are active at once, how does this change over time?

* Can we take the first movement segment (of each block?) as a plan/feedforward? Does this give us an indication of subjects' forward models? Or of their discrete policy decision memory? Do these get better over trials?

* Optimality could be defined as the norm-minimizing inverse which minimizes action in the null space? This has a time component, it is a trajectory. What is the space of optimal trajectories that are norm-minimizing inverse? Note that there is no need to "stop" at the target, only to move through it.

* How many discrete movements make up a trajectory? How do we define a discrete movement? (behavioral modularity, maybe look at velocity of trajectory split it into chunks?)


## Optimal Feedback Control Hypothesis

* Is the LQR a reasonable model for EMG control? if the mapping is linear-gaussian, does the control solution developed by subjects match the data? Particularly if we "test" the synthetic controller on "actual" perturbations from subjects' trials? (Run real data through the controller and compare responses?)

* Are subjects optimal controllers? In what sense? What cost functions are subjects optimizing for?

* Do predictions from optimal control theory match what we see in our experiment? Synergies, least action, responses to perturbations

* What kind of control are subjects exhibiting? Model-based? Model-free? A mix of both? How can we tell the difference? To disambiguate model-based and model-free, we can look at "adjustments"-- online corrections in subject trajectories-- are these corrections made optimally? Scrutinize the movements made after the adjustment. In what "spaces" (geometric, position/velocity, etc.) are these corrections made?


## Optimality, Inverse Optimal Control

* What are subjects' cost functions? Is it straight line movements in the task space? Is it minimum-variance movements in the EMG space? 

* If subjects aren't optimal (based on our normative models), what is our hypothesis for why not? What cost functions fit the data, and how do they differ from the OFC models'?


## Adaptation and Learning over trials

* How does general signal power change over trials? Does variance in general increase / decrease? Are subjects applying more or less force over trials? Are they fine-tuning their movements?

* If we do PCA on each trial, does the dimensionality increase, decrease, or something else over trials? The answer points to exploration vs. exploitation, hierarchical or mixed-controller solutions. This shows how the structure of the variability might develop over trials. Do subjects "freeze" degrees of freedom in order to simplify the learning process (consciously lower variability in certain dimensions)? Do we see a shift in dimensionality of their output over the course of learning?

* What influences updates to subjects' policies? Are subjects doing some kind of annealing towards a general solution? -- temperature goes down monotonically (PCA dimensionality may be a rough measure of "temperature"-- how spread out over dimensions are subjects' solutions?) Or are subjects doing a kind of adaptive annealing, where "temperature" changes based on performance, or some other feedback ("I'm not doing well, I'll start exploring more").

* How do subject cost functions change over trials? We can fit cost functions across trials to produce a measure of adaptation.

* How does control changes over the course of learning, if at all? How are subjects learning? Why are subjects learning?

* What OFC model would fit the data at each point? Can we find a best-fit controller at each trial? Can we fit an adaptive controller over trials? What adaptive model has a best fit? How does this support our theory of how subjects are learning?

* Does the composition of optimal controllers explain adaptation? Are subjects using one controller or several? Are they composing them or switching between them? Are they learning which controller to switch between or are they developing a single controller to solve for all targets? Does this change over trials? Might this explain perturbation response? Subjects might be building p(best_controller | target, state), that is choosing from distinct policies, rather than developing a de novo policy.

* How "sample efficient" are subjects in solving the learning task? That is, what is the optimal/normative sample efficiency? Given a single trial's worth of experience, what should subjects be able to achieve (if they are optimal) on subsequent trials? What does a "perfect" learning algorithm look like when provided with subjects' data over trials? Look at this like a sampling problem: what is the optimal sampling distribution? Do subjects' distributions look like this optimal? What would an optimal update to the sampling distribution look like, given subjects' experiences over trials? What is the transition function of my sampling distribution over trials?


## Model-based and Model-free learning

* Are subjects learning an internal model? Or are they learn rote movements? Or both?

* Analyze subjects' errors-- what correlates with policy updates? Missing/hitting the target or a large deviation? What provides the most "signal" for learning?

* Model-free learning prediction would imply that similar movements made after they are rewarded? Is this what we see? Are movements that are rewarded more similar to the subjects' "policies" than non-rewarded? That is, are subjects using the binary reward to learn? Breakdown by trial type: how does having a no-hold influence the next trial? A miss? What trial-to-trial differences do we find in these different cases?

* What is the relationship between sensory prediction and reward prediction? (We (think we) know the reward structure of the task, to move directly to the target) Sensory prediction error is theorized to drive updates to forward models.

* Is the transition function for sample/policy different after rewarded trials vs. unrewarded trials? What is the difference, and what does this imply about the influence of reward? Is the reward of hitting the target playing a role here?

* Can we reliably predict trajectory given the target (the policy, p(solution | goal))? Can we predict trajectory from current state? (the forward model, p(x' | x))?



## Data Particularities

- Can we rotate subjects' movements so that we can compare easily over targets?
- Is the calibration the "same" in both sessions? (the target bar order will be different, but the layout is the same?)
- What is our decision on no-holds? How do we treat them?
- How do you control for different targets? or just look at the same target?

## Notes

* Subjects tend to make other movements over learning, of the head and body, of the other hand. this may aid in memory of particular movements?

* Agonist/antagonist pairs are a strong prior on movements. If we can connect natural movements to modes to behavioral directions, we can understand if people are preferentially exploring opposing movements.

* Train a classifier on the natural movement dataset, then try to segment movements in later tasks based on classifier? Why would we go through the work of doing this?

* Analysis ideas
   * [ ] information bottleneck?
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

* time of day vs. performance
* hours from lunch vs. performance
* instruments / non vs. performance
* neuroscientist vs non-neuroscientists in terms of performance