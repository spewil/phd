0. precis for feedback

- concise intro to the task formulation
- framing of the problems faced by the learner
	- system identification / learning of a forward model
		- how is this process related in this context to the reaching context?
	- model-based primitive / component learning
		- is this actually a problem faced by the learner?
		- we might assume the learner has access to some muscle activation primitives already
	- construction of a composite movement from component primitives
- for each problem, discuss some basic normative hypothesis and their predictions in the setup
	- system ID
		- we should be able to describe what the optimal data collection strategy should be for a person faced with learning an entirely new set of dynamics in this virtual environment -- what is the model-learner optimizing for and how does it relate to the task?
		- is this a regression problem for x' = f(x)? what dataset x (and thus what action set u) is optimal to solve this regression problem?
		- can we use trial-to-trial dynamics of the learner's errors in the task to determine how this model acquisition proceeds?
	- learning primitives
		- this problem, if it is one, is more like the adaptation of a reach (in the case of a single target goal)
		- this might be framed by the adapting of certain gains for pre-existing primitive movements, but this depends on the muscle-to-force mapping
	- constructing composite movements


i. An introduction giving the context of the work
	- Why can't robots move like humans?
	- What is special about human movement?
	- Why is this the most interesting problem?
	- What is motor learning vs. motor control?
	- Goals and Aims (look at earlier proposals)
		- claim about control needing an extension for learning
		- use RL concepts to analyze motor learning experiments
		- can we defend this use of RL for learning?
ii. A literature review
	- Brief RL review connecting RL to control
		- general problem outline / setup
			- MDP domain
			- continuous case, curse of dimensionality
			- LQG case
			- value functions
			- bellman equations, dynamic programming
		- learning
			- what needs to be learned?
			- models and policies
			- what do we not have a model of yet?
	- Experimental motor learning
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
	- Motor system (why hands?) -- from muscles to cortex
		- basic CSN circuits
		- spinal circuits
		- motor cortex
		- corticomotoneuronal connections
		- muscles, recruitment curves
		- graziano experiments
		- synergies
			- multiple definitions
			- bizzi, mussa-ivaldi

iii. A research question and hypothesis
	- How do we learn new movements?
		- what is a new movement?
		- what is a motor skill?
		- is this a learning problem or a selection/combination problem?
			- how are existing movements combined to solve new goals?
			- how are tools "embodied"? new policies for a new tool but based on existing patterns of muscle activity?
		- is "learning" the dynamics of the environment more like an exploration problem?
			- what is the structure of this exploration?
	- We hypothesize that learning proceeds optimally under the data collected
		- we can try to model this optimality using linear control models
iv. A section on methodology
	- EMG rig
	- calibration, manifolds
	-
v. A substantial piece of work towards the thesis objectives
	- EMG rig data collected, analyzed in calibration task
	- basic learning task(s) described
	- advanced learning / transfer experiments described
	- LQR simulations and theory (vanilla, +SDN, learning)
	- Krakauer data analysis take-homes, modeling, thoughts
vi. A plan and timetable for the remainder of the work
	-
vii. A bibliography.
