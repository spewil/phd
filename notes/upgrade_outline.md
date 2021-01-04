UCL guidelines:
	introduction and context
	lit review
	research question and hypothesis
	methodology
	substantial work towards objectives
	plan for remainder
	bibliography

4 -- intro, physiology, experimental methods
5 --
6
7
8
9
10
11
12
13


intro & aims
	- what are we interested in?
	- how are we going to approach this interest?
	- what do we hope to achieve?
	- Why can't robots move like humans?
	- What is special about human movement?
	- Why is this the most interesting problem?
	- What is motor learning vs. motor control?
	- Goals and Aims (look at earlier proposals)
		- claim about control needing an extension for learning
		- use RL concepts to analyze motor learning experiments
		- can we defend this use of RL for learning?
		- what do we mean by "RL" here?

motor physiology
	- **what do we know about brain and motor?**
		- graziano
		- synergies, bizzi
		- hands, cm connections
	- **why hands?**
		- from muscles to cortex
		- basic CSN circuits
		- spinal circuits
		- motor cortex
		- corticomotoneuronal connections
		- muscles, recruitment curves
		- graziano experiments
		- synergies
			- multiple definitions
			- bizzi, mussa-ivaldi
	- **how does what we know inform experiment?**
		- **things are very different depending on system, behavior**
		- hands (and maybe cortex) evolved to be flexible-- how is this achieved?
	- how does this inform theory?

prior work on motor control and learning
		- classic reaching adaptation --> this is a different goal
			- shadmehr
			- krakauer
		- unperturbed movements
			- van beers
		- skill learning tasks
			- ball and cup / kendama
			- throwing tasks
		- skill learning via BMI work using EMG, key findings
			- Mosier remapping experiments
			- Berger
			- Radakrishnan
			- de Rugy
		- cortical BMI work
			- Batista papers, lee miller papers
		- speech learning -- analogy to speech
		- bird vocal learning

experimental methods
	- goals / hypotheses
		- for each problem, discuss some basic normative hypothesis and their predictions in the setup
		- system ID
			- we should be able to describe what the optimal data collection strategy should be for a person faced with learning an entirely new set of dynamics in this virtual environment -- what is the model-learner optimizing for and how does it relate to the task?
			- is this a regression problem for x' = f(x)? what dataset x (and thus what action set u) is optimal to solve this regression problem?
			- can we use trial-to-trial dynamics of the learner's errors in the task to determine how this model acquisition proceeds?
		- learning primitives
			- this problem, if it is one, is more like the adaptation of a reach (in the case of a single target goal)
			- this might be framed by the adapting of certain gains for pre-existing primitive movements, but this depends on the muscle-to-force mapping
	- constructing composite movements
	- what kind of experiments do we need to learn something about motor control and learning?
	- hardware
		- recording 64 channels of EMG from multiple muscles the arm and hand with realtime feedback
		- in an isometric learning task
	- software
	- compare to previous approaches
		- myocontrol, etc
	- calibration
	- analysis -- feature extraction
	- testing
		- different tasks
		- data from tasks

data analysis
	- APT data
		- what is the goal here?
	-

theory of motor coordination
	- error adaptation, system ID
	- delay == prediction
	- feedback control policies
	- noise
	- selection
	- optimal control
		- what are the connections between optimal control and RL?
			- designing rewards vs. discovering rewards?
		- value based learning -- we know the brain uses this, model-based
		- habitual learning -- use-dependent learning, model-free?
	- is LQR a good model?

next steps
	- collect more data
	- test different types of tasks to narrow down phenomena
	- run more simulations





