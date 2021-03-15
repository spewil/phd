# wolpert + maneesh upgrade meeting
- questions
	- theory
		- do we learn OFC?
		- or do we learn primitives and construct OFC?
		- what kinds of learning to model? how to approach?
		- why are there no solid normative motor learning models? 
	- experiment
		- what tasks will be highest impact?
		- what mappings? what calibration?
		- analysis within-trial
		- analysis across-trial


# andy 15/3/21

- ethics forms, research log
- upgrade meeting goals
	- recap, summary in mind (bullet points)
		- don't assume too much knowledge
	- high-level goals, questions, aims 
		- three prior EMG tasks, mine is way more advanced
		- so what do we do with it?
	- left on my own, I would do XYZ... what would you have me do?
		- freeform dataset + PCA + pick components + reach to targets
		- validation experiments?
			- holes you could poke in our rig
			- how to validate these during our data collection
			- baseline recordings? 
		- taskwise how do we get the biggest bang for our buck on the setup
			- i have these high-level questions
				- what is the underlying algorithms of motor skill learning?
					- use trial-level information
				- how can theory best complement this task?
			- push them to be specific
				- what calibrations? what tasks? what perturbations?
				- if i take dataset X, pick components Y, what are the pitfalls of this?
- sania bioinformatics roadmap
	- thousands of AAV capsid sequences with minute differences
	- visualizations of 
	- sequence (with uncertainty) --> contig --> compare with reference --> point mutation --> protein level effects

	- inputs 
		- original sequences (known wild AAVs)
		- reasonable ideas of regions of the sequence (e.g. binding sites, approx nine regions)
		- sequences we have and their mutations
	- output
		- did it infect?
		- how efficiently did it infect?
	- alba post-experiment
		- 100 sequences --> 20 of these random sequence popped up exactly the same
			- that sequence could be overrepresented in the library

	- input space -- sequence/mutation + infection efficiency
	- output space -- sequence regions of interest (variability entails interest)
	- way of doing that is clunky
		- streamline this process
		- missing out on sequences

# peter
- what scaling factor to use?
	- would need parameters of noise distributions per channel, over time
	 - do filtering using these statistics?
- just do basic filtering + PCA for now, this is the most basic thing to do
- next steps:
	- we know something about the EMG signal, can we build a Bayesian filtering approach?
	- inferring control signals from data?

# andy and dan 4/3/21

- catch up 
	- 
- complexity 
	 - of policy representation?
	 - representation == linear mapping weights
	 - entropy is a complexity == probabilistic weights / sampling
	 	- https://gist.github.com/GaelVaroquaux/ead9898bd3c973c40429
- regularizers over trials -- dan likes this idea
	- data driven approach?
	- hypothesis test -- choose regularizers and do model comparison
- dPCA
	- over blocks as the way to break it up
	- don't lose the within-trial dynamics of the EMG
	- treat EMG like firing rates are treated in shenoy et al. 
- hier- vs. heterachy
	- bouncing between levels 
	- high-level plan down to low-level, then repeat

# andy 1/3/21

- are you using 4 modes or 8 modes or something else?
	- can you product activations that span the space to begin with?
- are you combining modes in parallel or serially?
	- some transition from serial to parallel to minimal/bespoke?
- why not five modes?
	- how many primitives is optimal?
	- optimal for what cost function?
- cases
	- can't span the space -- you're screwed
	- something is difficult to achieve but not impossible (agonist-antagonist e.g.)
- modeling
	- we should be able to fit a model that includes regularization terms
	- our hypothesis would be that these regularization weights will change over time.
- nitpicks about muscle interface (starting with a fitted muscle-to-force mapping using a baseline dataset)
	- extreme perturbations to the mappings, some probably not biophysically available? 
		- we don't want to fall into this same trap
		- ideally we need to test what muscle activations are available in a calibration
	- not many sessions

- !!! what exactly is the mapping?
	- what are the 32 directions...? 

[ 0.      1.  ]
[ 0.71    0.71]
[ 1.      0.  ]
[ 0.71   -0.71]
[ 0.     -1.  ]
[-0.71   -0.71]
[-1.     -0.  ]
[-0.71    0.71]

[ 0.      1.  ]
[ 0.71    0.71]
[ 1.      0.  ]
[ 0.71   -0.71]
[ 0.     -1.  ]
[-0.71   -0.71]
[-1.     -0.  ]
[-0.71    0.71]

[ 0.      1.  ]
[ 0.71    0.71]
[ 1.      0.  ]
[ 0.71   -0.71]
[ 0.     -1.  ]
[-0.71   -0.71]
[-1.     -0.  ]
[-0.71    0.71]

[ 0.      1.  ]
[ 0.71    0.71]
[ 1.      0.  ]
[ 0.71   -0.71]
[ 0.     -1.  ]
[-0.71   -0.71]
[-1.     -0.  ]
[-0.71    0.71]

so each column is being mapped to one of eight directions
there are 32 targets though...

# ted 25/2/21

- fixed random features -- project through random matrix
- thesis 
	- two types of movement
	- first part is jargony
	- before -- explicitly say what I'm doing -- multiple systems, a little outline
		- one is rigid, flexible --> then how they interact
	- why is modularity mean a lack of flexible
		- operating at a high-level -- could even be a 1D input (graziano), but this needs to be dexterous with ongoing sensory input
		- high-level flexibility, low-level flexibility
			- plain language overview
			- introduce vocab more slowly
		- what does it mean to be fractionated?
		- where is the tradeoff?
	- right before 2.6 -- our system has the following desiderata-- a more precise list of things needed in a system, reflecting the earlier plain language intro
		- these bullet points could drive experiments/models
	- weakly interacting, parallel hierarchical systems
		- the big three-- BG, CRB, spinal --> internal dynamics within these parallel systems is more important 
		- not a strict hierarchy
		- simultaneous planning
- doc of stuff from sharing in chat
	- LQR OFC 
	- transfer/generalization --> reduce cognitive load to shift to a new task
	- neuroscience, control, RL review
- task phases of learning
	- known goal (move to X) --> known cost function == control
		- maybe moving blindly is a good perturbation for internal model?
	- unknown goal (moving to Y tends to be rewarded) --> RL 


# patrick

- catch up 
	- family, congrats, what's new 

phd project
	- general physiology claim of loops and heterarchy
		- graziano + strick figure
		- loops
		- heterarchy == composition of motor controllers and learning dynamics
			- we usually say "distributed and hierarchical"
	- big question is: can we develop tractable, testable, normative models for motor learning? 
		- place to start is look at motor control models, 
		- begin to add learning aspects to them
		- understand what learning computations the system must perform
		- understand what information the system uses to adapt?
	- how do we best tie experiment to physiology?
		- hardware setup -- photos, explanation
		- calibration -- unsupervised features for a simple decoder
		- task 
			- simple goals
			- no perturbations
			- careful perturbations
	- what do you make of the plan in general?
	- questions
		- what can we tease out about learning, how can we be careful here?
		- what's interesting in your team's work in terms of learning?
		- what kinds of gotchas do i need to think about with EMG? can i really hope to see something hierarchical in the signal and/or heterarchical in the learning?

startup
	- understanding the exit?
	- transitioning from phd to venture?
		- read UCL's guidelines on ventures
		- no equipment, no emails, don't go AWOL
		- was this done as part of your studies?
		- taking uni's resources?
		- how many uni people were involved?
	- when to incorporate?
		- graduated july, incorporated september
		- multiple people == good to incorporated, formalized
	- when to patent? what about other IP?
		- strategy depends on what you're trying to do
		- novel utility
	- how much funding?
		- runway vs. rate vs. equity
		- spread out valuations over demonstration points
	- competitive edge
		- what's preventing apple from just doing it?
		- what's your leverage in that discussion?
		- is this difficult to do? why?

feedback
- ask people to try to control low variance components
- warning from krakauer: motor not cognitive, add interesting dynamics
	- figure 8 from arbitrary electrodes
	- arbitrary PCs of activity
- control channel orthogonal to existing control
- 64x2 mapping only has two directions of interest, so it's just a matter of picking those
	- random
	- two movements
	- PCs from movement
- BMI -- argument that we're removing complexity, but we're also removing spinal cord and muscles
	- can my experiments set up something for a full-on monkey paper

# ted 

- learn features of the environment 
- systems level view from the models
- optimal arbiter between policies/controllers

- predictive system, value system, collection of controllers --> flexible control

- write out LQR internal model updates

- Ted's plans for Neurips
	- GPS thing (Ted leading, don't worry)
		- planning?
	- BGRL (co-lead)
	- Nat Gradients and exploration on loss surface (lead)
	- DDC implicit (not lead)
	- LQR-RL stuff (Spencer lead)
		- what does this model do?

# peter data club

- if we ask people to move towards a goal in an uncertain world, are we asking them to learn a new (internal?) generative model from goal-->synergies-->motor output?
- how do we define such a model?
- we're asking how motor activity / planning is represented
- what can the data tell us when viewed from the angle?

- peter's "motor" (keyboard) readout
	- is this "hierarchical"?
	- how do we define this, how do we analyze

- what kind of algorithms?
- what kind of computations?
- do these support bayesian inference?

# andy and dan

- van beers style experiments?
	- simple, behavioral...?
	- force pad, eye movements
- error-drive LQR adaptation?

# andy 5/2/21 + 8/2/21

- what is the strick figure of / what kind of visualizastion?
- posture -- different movement or differnt aparams of same movement?
- todo
	- add stuff to 2 
	- free-write on 3, go go go
	- analyze andy data (as a project?)
	- APT data (as a project?)
		- LQR fitting?
	- write up theory projects clearly (atomically for later replacement)
		- GPS
		- adaptive LQR
		- LQR-RL 
		- compositional LQR

feedback on ch1 and ch2
- im cherry picking evidence for a view of the motor system
- how does ch2 fit into my hypothesis/thread of the project 
- editing -- weave in my experiments and models 
- think: is this sentence/graph useful
	- for 
- heterarchical claim isn't clear -- should clarify this a central

- 
	- email maneesh wolpert
	- this week
		- chapter 3 drafted
		- chapter 4 blocked out

# ted 22/1

- look through GPS repo, 2D env plots
- overleaf GPS

# ted

- papers openai tasks
	- hindsight learning
	- deep successor features
- layout
	- nice result on 2D navigation --> 0-shot
	- given reward vector, learn reward vector
	- theoretical guarantee for convergence
		- transfer successor feature
		- GPI paper
		- what guarantees can we prove to our thing?
- policies are being combined somewhere in the brain, not sure where
	- mixing actual motor actions, as opposed to policies

- for Neurips
	- 2D env
	- robot
	- theoretical result

- how do we interpret action selection on the fly
- send me overleaf, repo

- future
	- what if policies are LQR?
	- add planning (e.g. tree search)

- compare to experiment
	- revaluation in motor task
- partial observability
	-

# andy

- ask goncalo for half the previous invoice
- make a PO for neurogears
	- myFinance, non-catalog

- don't put everything you know
- leave the extra for discussion
- look what i have already
	- consolidate
- if the world is LQR, does this demand that the LQR model work?
	- what free variables exist that mean it could break?
- what needs to be done to complete #1 ?
- background / intro
	- why is this question interesting?
	- why is this setup worthwhile? is there an easier way? why not cyberglove, reaching?
		- we have control over all dynamical variable
	- evidence for and against LQR model?
- calibration
	- try to "erase" the entire space of muscle activity, forcing you to "explore" the decorrelated electrode space
	- assuming we have this "whole space", we use some regularized dim reduction, choice of which is very important, to pick out modes that are interesting (independent? high variance? ???)
- #1
	- the rig should be able to ask you to perform unlikely movements/motor combinations
	- how do we define unlikely? need a calibration task that forces you to activate unlikely motor outputs (ideally)
- #2 -- graziano's claim
	- spell out this claim of overlapping feedback controllers


- three things
	- control -- todorov
	- something in between (flexible control?) -- graziano, combination of primitive controllers
		- flexible combination of existing movements
	- learning -- how do you obtain new controllers "from scratch"
		- this might not be well-defined...
		- what is a new controller?
- how do you dissociate these different classes of control/combination/learning?
	- clever perturbations to control output, state, environment, noise...

- prior work
	- adaptation to reaching -- model learning (sensory prediction error)
	- BMI work
	- myocontrol stuff -- dim reduction
	- LQR
	- basic RL -- q-learning, value-learning, policy-learning

- deadlines
	- first week of jan -- maneesh and wolpert date
	- jan 15 for draft
	- feb 15 for final
- goals
	- get the ideas down as concisely
	- do it for myself
	- constrain myself to my ideas, my setup as much as possible


# april 16/12/20

- survey results
- what is the nuanced goal?
- trad model doesnt work for lots of people
- empowerment
- bell labs tech journal
- kirstie whitaker -- article about bropenscience
- what gender split in the building?
- send
	- github proposals
	- survey results stuff
- what are people's motivations? what are their next steps?
	- not everyone
- hoping -- comms, public engagement, what's our mission, purpose, values
	- current website -- doesn't reflect core values
	- what makes us unique?

# tom 16/12/20

- individual labs / pairwise
- working group plan / larger iniative
- no specific scientific plan -- should we?
	- what is our goal/question?
- 10yrs principle of neuroscientists -- short, synthesis
	- more experiments or think more?
	- biological basis of intelligent behavior
		- mechanistic
		- adaptive, flexibility
		- planning
	- create a structure
		- different labs, people
	- working group for this?
- culture
	- science problems
	- institute opportunities
	- agency -- nurture spirit
- rally around a goal, what is the deliverable?
	- needs milestone
	- needs deadlines
- neural intelligence, here are the groups
	- each group should be contributing to this mission
	- sense of belonging to the institute mission
	- different levels --> across levels

- get drop-outs into talk (2x 20min)

- pure discovery
- make a name for myself
- hat trick of papers
- then what? are you fulfilled?

pillars in life
- focus on their life
-

# ted 15/12/20

## thinking about

- model v model-free,
- operator view of policy gradients -- might combine PG and value methods
- jesse's paper
- habit paper kevin miller

## phd ideas

- different rl systems -- how do those systems interact
- brain trades off between systems
- define arbitrator, produce value functions and policies
- what neural mechanism does the arbitration?
- what's the optimal combination of Q-learning and SR-based
- PG methods and value-based combined?

## swc

- chip on their shoulders, competitive
- this is why there isn't more collab w gatsby, not gatsby's fault...

## goals

1. Is LQR (as it’s claimed to be) a reasonable model for feedback control and error reduction + variability prediction for dimensionality reduction-based motor interface (task reads out from D muscles, find modes of that data; do PCA to get K < D dimensions, controller only responds to motion in those K directions)—does behavior + motor activity follow LQR? this question has already been asked, but it hasn’t been asked for this kind of high-to-low dim mapping. It’s been asked in tasks where muscles haven’t been directly in control (Bolero 2009). Todorov: do a task, look at muscle signal. Muscles that aren’t necessary for task have higher variability b/c they’re not being optimized for task (but does’t introduce perturbations). Also see Loeb (2012) for a negative result saying that muscle coordination is habitual rather than optimal, but it has issues (low # muscles). Can we replicate previous reaching optimality results in our set-up? What’s unique about our set-up is the PCA/dimensionality reduction in muscle activity space. This is important because you can create arbitrary muscle-cursor mappings, so you have to learn a new skill/mapping. This is different than perturbing a fundamental movement and forcing adaptation, which is what has been previously done. For our task, the participants actually have to learn a new task/mapping, rather than just do what they already know and be robust to perturbations. We test the LQR hypothesis once they’ve learned the task, because LQR isn’t a learning theory, it’s a theory about optimal control. We can see if, once people learn a new skill, their behavior is optimal wrt LQR theory. If we establish this, then we can think about how this LQR model is actually learned (enter RL).
2. Is GPI with LQRs / LQR-RL a good model for motor learning? Define a model and see if it recapitulates known motor learning phenomena on existing experiments + accounts for things that previous models don’t. (Similar in spirit to Geerts et al. (2020)). Can this model track the higher-order statistics of trajectories during motor learning?

# emma 15/12/20

unfriendly
arrogance

we're thiinking about scicnce in differnt ways because we want science to be a viable future
why are people at swc / in science?

PS people -- we needed a job

consensus relies on people operating in good faith towards the group

# jesse 9/12/20

- change noise parameters and predict changes to the controller?
	- change state noise vs. control noise
	- interesting because you can alter the actual input noise separately from the readout noise
- what in the model can be changed? WRITE DOWN THE MODEL CAREFULLY!

# manny 25/11/20

- what is optimal in the derivation and what isn't?
- is that solution for K assuming optimal?
- Q becomes a function of gain K
	- optimization

Q(x,u,K) = ??? depends only on known things
given that, what is K that optimizes that Q
K should be the same for all x and u

pick one K, apply that, re-evaluate

interpolation between K's is different from interpolating policies

does selection and combination become equivalent? probably not
- e.g. obstacle --> mixing policy might not work, but selection makes sense

code up LQR, LQR+SDN

end-state comfort --> pouring is less accurate
	- "comfort" is probably variability, risk

"policy map" not an "action map" just to be clear

maneesh would expect to learn a new policy over time
learning a new skill -- deliberate planning with intermediate steps, which then transfer to a smoother execution (embodiment of the tool)
	- hard to argue against the creation of new policy

what does it mean to select something that is blend

you need two things
	- train the actor that corresponds to the policy (pi(x))
		- lookup table, gain, something has to be in the brain
	- through selection, we learn the SR that goes to with this policy


# graziano 24/11/20

feedback remapping -- updating the feedback controller with new information
	- how is this approximated by optimal feedback control?
	- what is the kernel of the idea, how might we access it in behavior?

what about feedforward control?

state dependent feedback controllers?
here is our model:
	- state is kinematics
	- linear state dependent control
	- cost is quadratic (ish) encoding state goal
	- noise reflects muscle activity

- likes todorov work
- how are movements flexible -- are we flexible?
	- people are similar, we're constrained
	- learned chunks of behavior
- adapting the underlying repertoire on a slow timescale

- monkeys move to a certain posture
- refine the movement to finish

- posture is fixed
	- 8 rough synergies is fixed
	- honing in directly on the "long tail" movements

- set of policies, immediately derive a new policy given a new task
- if the cost isn't quadratic, need to ask

- "end state comfort"
	- reach for a cup upside down
	- everyone is computing the end state comfort

- are monkey repertoire's very different?
	- very similar across monkeys, average of that region

- what is the embedding function the brain

- e.g. typing
	- posture is very narrow
	- posture-constrained, with adjustments on top

- is the controller state dependent
	- the controller stays the same, but it depends on posture
	- more parameters

- "i dont really believe in ballistic movement"
	- spring-loaded shells might be ballistic

- internal simulation still influences as feedback
	- internal feedback even with anest
	- e.g. parietal lobe, somato, scooping out the model of the limb

- gaze probably subcortical, controlled by the superior colliculus

*what kinds of behavioral predictions can we make based on this thinking?
- are policies combined optimally?
- do policies (and their combinations) vary under different feedback conditions?
- if optimal composite policies aren't available, is an optimal workaround found (like a lesion study...)?


# maneesh lab meeting 18/11/20

- how to think about LQR controller
	- feedback gain is not state-dependent
	- can you rewrite u=Kx as u=K(x-x_goal)
	- feature function could be phi(x) - x-x*
	- underlying control problem
		- can you write the optimal control for a fixed dynamical system, quadratic noise and cose, can you write the optimal control as u=K(x-x_goal)
		- if so, would still change things by departing from normal noise model which would be more interesting
		- select between different policies -- use SR to tell you how you will perform under a specific task/cost
	- this comes from the thoughts in the RL setting
		- the GPI view of whats going on
			- motivation: GPI-like with 0 rollouts
			- what do we mean by a control policies?
				- some sets of gains? something else?
				- graziano's data? are the monkey movements quantified?
				-
		- lots of policies, SRs, evaluate for a given reward
	- hypothesis is that this scheme is matched to the BG-CTX loops -- more complexity
		- policies could be muscle contraction, to synergies
		- we could predict switching between policies, should be optimal according to the GPI/E framework
	- separate thing -- can we use the feature space to linearize things
		- e.g. cost functions, noise
		- this could complicate things, particularly wrt the noise
	- eszter's work
		- when we do inference for state, we can use the same basis

	- delayed, continuous control problem
		- these issues will become prevalent because we might smooth

	- GPE/I prior art
		- mosaic models from kawato
		- KL control composability

	- in the KL control setting **
		- SR for passive/active dynamics?
		- is there a smooth SR deformation in this world?
			- from passive to active?

	- calculate the payoffs of policies
		- if I can interpolated SR

	feature functions?
		- gaussian bumps?
		- maybe you pack into the feature function whatever is needed to make the reward linear in those features



# andy 12/11/20

- goncalo
	- can we bill on shorter time frame?
		= yes, bill nov-dec now to get cursor working, then pick things up in january.
	- hourly billing, etc
- goals with goncalo
	- get calibration working and confirmed
	- data saving in a nice format
	- can we get to a moving dot by christmas?
		- dynamics
		- mappings
		- YES -- this should be the goal
- reorder stuff on andy's code
- finish the frame attachment with simon
- room noise
	- live fourier plot in bonsai?
	- faraday cage around the frame?
	- shielding with martyn?
- recruiting people
	- do UCL ethics thing -- what does this require?
	- how long does this take to approve?
	- talk to athena?
	- how do we get people?

- nell
	- send krakauer paper
	- send motor learning review
	- send project context
	- a few tentative ideas

- what was maneesh talking about?
	- you already have a collection, a repertoire of motor outputs
	- the question is twofold
		1. how do you learn the dynamics of the environment?
			- this is an unsupervised problem
			- prediction of outputs on the dynamics
		2. how do you combine existing motor outputs to build control solutions?
			- how does information on each trial contribute to this construction

# maneesh + ted 11/11/20

- formalize the task mathematically
- try to formalize the learning problem, and the hypothesis?
- LQR ideas --> learning
- options
- SRs + SFs
- embeddings --> f(x,u), the important features of a trajectory (structure, reward-sensitive features)

this task might be called learning a new tool
	- "tool embodiment" connects to the idea of learning SRs through the tool
	- "through the trajectories" with the tool (not sure what through means)
	- out of primitive movements with the tool, completing an action is a selection process of primitives

two ways to proceed (that might not need to be decided now)
	- descriptive
		- try to "back out" LQR controllers from data under a model with assumptions
		- this seemed to be like my generative model thinking, but maybe not (Maneesh was skeptical about this)
	- normative
		- try to predict (generate?) controllers and data, then compare with actual data
		- this seems like Maneesh's preferred way, though he said you might try to generate trajectories, which would then help in the descriptive path

1 goal vs. multiple
	- if you have one single goal, you can simply cache an action-state value function and compute your actions from wherever
	- if you have multiple goals, or a variable goal, you can't simply cache and you need to build a solution from other pieces
	- LQG becomes a moot point if the controller for either of these cases is the same -- that is, it might be the case that if your cost is (x-x*)^TQ(x-x*) + u^TRu for some goal state x* and you have constant covariance noise, the controller is invariant to the goal state because of the linear and quadratic form. This should be doublechecked and worked out and thought about. Maneesh noted that the vanilla form of the LGQ is a sort of straw man, and shouldn't be said to be a bad model of motor control. Todorov has extended the LQG in several ways to better match data, and these cases might be more interesting and appropriate when thinking about combining controllers from primitives.

the experimental setup
	- "the most powerful part of the setup is the ability to impose probe or catch trials with different types of perturbations to the cursor and/or the muscles and/or the mapping" -- these probe trials can give you insight into the internal model and/or policy of the subject
	- think about training two tasks, then adding probe trials of a combined task

why do we need open-loop control?
	- feedback is slow, there are time delays
	- we need greater flexibility in our actions beyond a simple lookup/cache between state+goal and action sequences

two ways of computing policies
	- learn a model, then compute a lookup from goals to policies which is state dependent. again -- if im in a given state, use a lookup between my current goal and the right policy. this is hard in motor control because of time delays meaning you won't have a perfect belief about your current state. you can try to solve this by using your history to build a better belief state.
	- the other way is to directly compute a policy on the fly using dynamic programming for a given goal
	- i don't actually see how these are two separate things... should have asked.

Graziano
	- what work is he taking about? as i understood it:
	- as you move along rostral-caudal axis, policies/actions become increasingly complex, hinting that there are hierarchical motor actions stored in motor cortex, and the problem is learning or tweaking these and combining them to solve goals

overall impressions
	- the learning problem is kind of implicit in these questions, in that we never really talked about learning rules or things like that, but more about the right problem domain and making sure we were using the right words for things and the right frame for thinking about it
	- this probably makes sense, and manny's point at the end was that we should test something simple and build towards a principle for learning
	- but it might be that what's learned is actually the combination of primitive actions/policies and not actually basic motor movements
	- i'm inclined to agree that this is happening as well, but this must be in addition to acquiring forward models in the task

RL
	- "what is mostly called RL in the non-RL literature is really structure exploration. it's about what actions are taken to discover new trajectories, which really doesn't really happen directly in motor control"
	- i guess what he means here is we're not just wiggling all over the place (unless we're babies, which was the inspiration for this task)
	- i think we can talk about exploration in the early parts of the task (which I find the most interesting), but what we mostly talked about was how to do combine existing movements to build complex solutions, i think?
	- temporal credit assignment
		- this might work fine if you have a single control gain matrix to update
		- but if you have many to choose from, how do you know which to update?
		- i think this is manny's way of relating SRs to LQG -- if you have many primitive controllers, you need some way of solving credit assignment and it would help to have these compressed representations? not sure... :/

LQG+SR
	- assuming the "LQG" setup is interesting enough that it permits some notion of SRs to begin with... meaning that the control gain for the problem alters the dynamics such that you can have a structured state occupation density under that gain
	- each gain is optimal (but perhaps not unique) for a given goal; is each goal unique for a given gain? this should be answered and understood
	- for each feedback gain K in u=Kx, learn the SR for each gain (each gain is a policy here)
	- now for a given goal, pick the gain that is most aligned to that goal (somehow using the SR)

quick upgrade chat
	- daniel wolpert on upgrade panel
	- have concrete answers about the LQG stuff
	- have meaningful reasons why RL is useful for this task
		- one way of doing this is to back through the motor control/learning literature and do the translation to RL as much as possible, being reasonable, and see how those problems would be cast into RL framework. a lot of these problems will be very trivial, but some won't be. which ones aren't trivial and why? see where there is really "RL" going on in these tasks

take-aways after thinking: there are two things going on:
	- you update internal models using prediction errors, and this has a lot of support in the literature (one section of a lit review should be spent summarizing this using reaching studies). so you act, you know what you did, and you predict, and update the forward model based on sensory feedback and your prediction. the question there is what kind of structure exists in those initial actions-- this could be maneesh’s point about this being really a structured exploration problem.
	- simultaneously, you’re using your existing motor repertoire (sequences of muscle activations) to construct viable solutions to the current task. this framing means you’re talking about how the statistics of that repertoire (which movements are more likely) are related to the shape of your constructed policy. this is the search/selection problem... and this is something that hasn’t been framed in LQG as far as I know
	- the first problem is a study of the statistics of exploration and how they relate to the statistics of the natural repertoire
	- the second problem is twofold -- how you construct solutions to basic problems (moving in straight lines, for example) and then use those basic solutions in combination to solve more complex problems


# ted 6/11/20
- what would options describe in motor control context -- as temporal synergies, as feedforward control
- LQR-options -- as a mix of feedback/feedforward control
- same for SRs/SFs
- BGRL embeddings --> what do we throw away? does this change over learning?
- thinking about the learning dynamic in a bayesian way
	- bayesian LQR?
- hierarchical RL --> how do we port this to LQR?
	- multiple timescales (options)
	- state representations / hierarchy in space (coarseID?)
		- what is hierarchical state look like?
		- do we see hierarchy in the resulting LQR controller (synergies)
- ez-greedy == same action for N time steps (like dumb options)
- generalized policy selection
- learning multiple LQRs and (linearly) combining them (composition)

- boiled down ideas
	- normative learning dynamic for LQR (basic learning problem)
		- bayesian formalization
		- assumptions of task -- no model, no policy (e.g. coarseID)
	- temporal synergies == LQR options (temporal hierarchy, feedforward/feedback)
		- do these exist in data?
		- how are these learned?
	- spatial synergies == multiple LQR controllers?
		- what does a hierarchical LQR controller look like?
		- how do you combine controllers (task A, task B, task A+B=C?)
	- embeddings -- what information do you throw away?
		- how do you learn the right embedding?
		- (assuming you can construct a controller...)
- task / experimental constraints / focus
	-
	- we could buy a force probe and use that as well

- TODO
	- watch that will dabney talk X
	- put these ideas in the doc

# andy 4/11/20

- goncalo doing setup
	- struggling with time, as I want to work on RL stuff and integrating lots of findings, making figures, working with ted+maneesh
	- what would we need to pay him? how can we work out his time?
- phd logistics, timeline, upgrade, committee
	- what is an upgrade? can we enumerate what I have so far?
		- Sketch out an outline of this
			- Lit review bridge ML-RL
			- All the data I've collected / Krakauer data as model
			- All the physical setup
			- Task design
	- who is on the committee?
- buying pupil thing
	- pull the trigger?
	- GET IT
- maneesh+ted being involved -- how best to leverage?
	- ted is sort of bouncing around collaborating on multiple projects
	- he needs a very defined task to work on, I think, like developing and running models of a particular phenomenon
		- concrete plan for the two of us
		- make it clear I'm in for both sides, equally involved in modeling
		- continuous space? analogs of MDPs
- what do i do for the holidays?
	- write upgrade / thesis
		- make figures from krakauer data
		- make figures from old EMG data
		- make figures from new EMG data
		- intro motor learning, BMI learning, myocontrol
		- intro models of motor control + RL as adaptive control

TODO
	- Goncalo
		- milestones -- critical, priorities
	- Andy
		- Outline of upgrade draft --> by Friday lab meeting
		- Order Pupil Core X
	- Ted / Maneesh
		- LQR -- bayesian, RL
		- options
		- SRs/SFs

- Thesis Committee:
	- Maneesh Sahani
	- John Krakauer
	- Dario Farina
- Examiners
	- Internal: ???
	- External: Aaron Batista
- where do these people fit in?
	- Dan McNamee (Irish priest)
	- Adrian Haith (external data, gut check)

# michael arbel 3/11/20

- we see this relaxation to the mean
	- temporal synergy (useful covariant in muscle+time)
	- like an option? (a series of actions)
	- stereotypy -- model-free reinforcement, habitual
	- in continuous space == feedforward control?
- question is what feature/embedding is useful to acquire this behavior
- things needed for RL
	- dynamics of the environment
	- policy (parameterized or actions)
	- loss function
	- learning dynamic
		- regularization
		- gradient
		- ???
- **my question is not which model to fit, but how to say something meaningful about the learning process**
- learning dynamics -- think about these like bayesian inference? once you make assumptions about your distributions, you try to solve the model with SGD, variational infeference, sampling, etc. But the learning dynamics suit the Bayesian update perspective
- Bayesian updates have been seen to be optimal in perception, are they in control? Learning?
- **The principle we might see here is like in control where variability in task-relevant dimensions is lower than in task-irrelevant ones, learning proceeds by first biasing towards regions of reward while reducing variability in task-relevant dimensions first**
- the dynamics of this learning are unknown, and probably multifaceted
- behavioral embeddings are meant to throw away data that is irrelevant to the the learning task, in order to focus on learning task-relevant dimensions
- fitting a cost function to "expert" trajectories would allow us to then back out using this cost (assuming it is constant in the task) and track what features of the trajectory are sensitive to cost at different stages of learning
	- how do i write this down -- **gradient of task dimensions wrt cost**


# aaron batista 29/10/20

- the potential of RL is huge
- MatBot talks -- emotional valence, what motivates people to learn?
- adding emotional valence to AI helps them learn, value
	- what intrinsically motivates learning? curiosity?
- try to speak both languages, but ultimately in the work you'll have to pick a lane and your career will work out fine
	- Byron Yu wants neuroscience insights, doesn't build fancy models, but only works with data. Asks good questions
- in batista lab
	- jay hennig
		- objective function -- more links between NN learning and neurophys learning community -- what are the rules that govern learning rules?
		- possible costs / rewards:
			- error (CRB)
			- task reward
			- intrinsic measures of success (trajectory, jerk)
			- euclidean linearity (straight lines)
			- intrinsic value in exploration/noise/variability
			- energetic cost of movement, exploration (metabolic cost)
		- one shot learning is a fallacy -- rehearsals, simulations, preplay, replay-- all these things are important leading up to the "one shot"
- papers with arm models:
	- choudhury + miller
	- tim lillicrap + steve scott
- maneesh is 10yrs ahead of anyone, anticipating data that will exist in 10 years
	- black honda civic CRX

questions:
- how do you track learning over trials in MCI data?
- do you expect issues with this high-dim muscle space?
- what's the difficulty in modeling learning in general? why don't we see more overlap between RL and motor learning?
- optimal control, variability buffering -- you said you don't see this phenomenon in your BMI data-- what is your thinking around that?
- the yoking between output-potent and null could be the sample size?
- the deRugy paper presents a crazy incompatible synergy -- collapsing existing synergies onto one dimension
- how did you come up with incremental learning, and why this seems to help?
- advice on working with theoreticians, straddling experiment-theory


# ted 27/10/20

- what is maneesh+ted's plan/goals/constraints/assumptions?
	- GPI + transfer learning -- many policies for a given environment, each has an SRs
		- reward is linear combination of SRs and rewards
			- assume you're given this reward
			- regression to learn reward vector using known transitions
		- compute values by SRs for policy and new rewards == policy evaluation
		- generalized policy eval -- all values for all actions (Q value)
		- generalized policy iteration -- max value action over policies
		- maneesh's idea
			- algorithmic -- generalize GPE/GPI further using options framework (Sutton), assume you have a family of policies, optimal policy "selection" up to a rollout length k (in actions)
			- neural -- graziano reaching/grasping -- selection of motor primitives
	- RL + motor control
		- policy-based vs. value-based RL
		- methods are in concordance with nonlinear controllers-- what about linear controllers?
- what experimental predictions are offered by:
	- generalized policy improvements
	- successor representations
- the fundamental question(s) as I see it:
	- (how) do humans update policies in the direction of maximal reward?
	- what experimental predictions of RL are waiting to be tested? what phenomena are present in human motor learning data that might influence RL algorithms?
	- what is optimal about human motor learning/adaptation? (what are the cost functions, what is the policy improvement scheme, how are predictive models acquired, updated, and used to improve policies?)
- what known features of human motor learning are unexplained?
	- savings
	- fast-slow learning
	- speed-accuracy tradeoffs
	- learning an optimal mean, learning an optimal variance reduction (do these proceed in parallel or series?)
- **"The motor learning field does not yet possess an adequate computational model for practice-induced increases in motor acuity."**

- how does GPI work with options -- motor primitives as options
	- GPI + options is itself an ML paper
- what can we test?
- message maneesh


# maneesh (data club)

- latency of visual feedback 100-200ms
- proprioceptive feedback is faster (???ms)
- motor system is constantly updating using feedback
- people can seem to recover a different forward model faster (savings)
- motor command vs. sensory consequence
- predicting sensory outcomes of actions -- optimization of prediction of action's consequences (kawato localizes this in cerebellum, maneesh+shenoy theorized, hennequin has concrete model of this optimization)
- up/down reversal prisms -- at first completely fail, then aha moment and everything works -- perceptual adaptation (gravity goes up, etc), something about the prior of the world physics
- sensory deviations and control deviations are linked -- this is hard to map into an actual circuit
- updating a controller with errors that have just been learned

# dan

- TODO
	- fixed time warping for one-step-back X
	- this is the very first step, not much use in thinking about other things before doing these very basic analyses
	- think about showing the motor people these ideas, they have to be packaged correctly
	- if you show motor people that movements get slower over learning they won't believe anything else you say
- **maximally goal-related components change first == hierarchical learning**
- other (maybe distracting ideas)
	- "generative dPCA"
		- windowed dPCA over trials -- regularize latent through time
		- understand how the "latent" is regularized over trials
	- ginny's SCA method
	- model-based LFADS == similar to a generative LQR model
	- inverse RL leaving cost function as a free variable (constraint the dynamics and noise)
	- "slow feature analysis" -- analyze in Fourier space, dampen high-frequency components

- hard stuff
	- Dan will assist with whatever i want to do
	- Dan has more experience than I do
	- Dan doesn't want me to be his RA, to check my homework
	- Dan wants to work with me and support my interests
	- Dan wants me to build my novel setup, to say something insightful about motor learning


# ted 16/10/20

- trajectories are rollouts
- inferring embedding functions means learning a distribution Phi(x)
- behaviorally-guided RL means inferring the cost function, adding regularizer for embedding distance
- question -- does a windowed embedding function (window over trials) show that movement changes are regularized?
	- what is the best-fit regularizer?
- break cost function into scalar reward of the task (reinforcement) + inferred cost from inverse RL problem
- does the cumulative task reward actually matter to subjects changes?
	- **do we see an influence of the trajectory shift off the basis of the task reward feedback?**
	-
- (inverseRL cost - cumulative reward) = "internal constraints" beyond task constraint
	- does this internal constraint reflect a certain embedding function? a certain regularized shift in embedding function distribution shift?

# andy 16/10/20

- "it's a doctorate of philosophy, not of pipetting"
- keep delegating, keep that moving
- test Bonsai for Gonz
- order Pupil Core -- mostly for pupil, but active sensing?
- data analysis

- things to do / figure out:
	- dPCA / demixing influence of reward, influence of trial, influence of dynamics
	 	- we want some modes that are just temporal, but demixed over trials?
	 	- we want to see what the influence of reward is on top of temporal dynamics (we expect it to be small... people don't actually care about scalar reward)

- most relevant prior work:
	- BMI studies
	- myoelectric studies
	- error-based learning
	- birdsong learning


# maneesh 13/10/20
- look at Naija's stuff on motor unit recruitment in monkeys
- EMG isn't used mainly because monkey's pull out the probes, etc
- isn't EMG noisy? how do you filter the signal to be useful?
- main influence will be BMI decoding literature, look at what features are extracted there
- high-D data analysis usually doesn't apply to behavioral experiments, but look at Steve Scott's work analyzing high-dimensional joint angle data from robotic exoskeletons
- Lea has done time-warping using GPs
- nonlinear features over learning -- look at birdsong literature using tSNE
- apply inverse optimal control to understand why subjects are optimizing for the variance they're showing
- break apart failed trials further-- above or below tube, movement time, etc
- linear features will care what coordinate system you're in-- nonlinear features might not (x,y vs r,theta e.g.)
- **try doing PCA on the difference stacks!**
- analyze a smaller number of points in the trajectory at a time
- **LDA, dPCA-- can this unmix the influence of reward?**

# andy

- chop off the beginning of trials (when trajectory reaches a theta threshold)

- model-based == i will constrain myself where i'm able to control (low variance)
- model-free == assuming that you have complete control over trajectory
	- if it's easy and you're rewarded, you'll just use whatever you did when you were rewarded
	- not really moving to some optimal trajectory, just repeating what works
	- if you're not rewarded -->
- how do you start?
	- how do switch from a model-free to model-based system
	-

- you learn the gains of the controller
- you still need to learn the movement itself, the inputs/controls


# dan 25/9/20

- are you still down for this?
- hard to know what to do
- how do i get better at math? exploration/exploitation tradeoff
	- how much time to read textbooks / watch videos / rederive?
	- if i have a very clear goal, and i know why i'm going after it, i can feel motivated
	- your point is that if we knew where we were going, we would already be there
- really motivated by path integrals!
	- talk to me about the intuitive connections between path integrals, stat mech, correlation functions, gaussian processes?
	- help me understand the connection between path integral control and PMP?
		- PMP is deterministic limit...?

- i want to re-interpret motor learning results under the RL framework as much as possible
	- which papers come to mind?

- how do you embed policies?
	- path programming is saying SR is the wrong embedding
		- SR makes it easy to update policies in the direction of reward
	- sample the policies,
	- path programming -- i don't need to evaluate policies
		- what is the policy gradient
	- you give me policy, i tell you value
		- need to sample lots of policies


### adrian

- strong experimentally, archaic pre-behaviorism view (sherrington)
- disconnected from the rest of the world
- convince them that this task is a "real" motor task, all the controls
- re-interpreting old things
	- won't go to waste
	- but useful for thinking


# andy 23/9/20

email adrian haith
selection v execution

setup
- what about proprioception/cutaneous?
	- sensory error is in visual space
	- that proprioceptive signal is more about state estimation
- what would a test show that took away vision?
	- you have an internal sensory representation
	- but the error in task space is visual

- learning a language less like association between words and sounds and more like knowing a target sound and producing the right muscle patterns to achieve it

- humans don't care about KL regularization -- maybe they can change their policies willy-nilly...

- are these different systems?
	- selection / search (high temperature) -- is this cortical?
	- acuity / refinement (low temperature) -- is this cerebellar?

- in our task
	- first you figure out **what** to do it (selection/search)
	- then you figure **how** to do it ()

- the difficulty of the task matters
	- if task is difficult, search is prolonged
		- learning the forward the model?
		- constraining the policy (from random to suboptimal but coarse)
	- if easy, you'll internalize the model quickly

- you'll trust information from trials you did before if you are confident that you chose them
	- model-free learners should "trust" prior information (past trials)
	- model-based learners should weight prior information / past trials according their correlation with your output?
	- maybe the inverse? if model-based learners are perturbed, they will use that information
	- model-free learners might not, since they might see it as noise?
	- do they understand enough about the task to know the difference between noise
	- would you change your policy

- less unlikely but higher reward -->
- model-based learner is aware of unlikeliness of trajectories
- model-free learner is unaware and simply reinforced

- look at feedforward / feedback

- how do we achieve a unifying framework for thinking about motor learning
	- using the RL framework
	- think about the right papers

- company stuff
	- where to start with money?
	- andy needs 1.2M seed funding
	- make a list
		- main goal before raising next round
		- list of stuff, people, materials


# blam lab 18/9/20

- stereotypy is not motor acuity -- just because you do the exact same thing well out of habit, doesn't mean that you're optimal, or good at doing it?
	- what are the hallmarks of acuity?
- the big dichotomy
	- selection v. execution
	- what to do, how to do it
- look into vernier acuity -- this is a good definition of acuity, it gets better with practice but it's somewhat straightforward
- "a better policy is not better selection"
	- this is the idea that you can refine a given policy which misses the "Fosbury Flop" shift
- the APT task feels like one movement, and it's not discernible what's improving, it's not consciously available what's changing from trial to trials
- maybe a three-part structure of learning
	- selection
	- speed of selection (recall)
	- acuity of selection (refinement)
- finding motor outputs and reliably retrieving them are different from acuity
- length of experiments is important (think of de Rugy 2012)-- in order to see changes in policies, might take many trials
	- why is this so? what is constrained perturbed plants and limited their policy changes?
- think more about what we know from prior myocontrol work!!
- how is this task different from arbitrary visuomotor associations?
	- it's like language -- one level is which word for which context/meaning
	- another level is coordinating that output, producing sound

- i think i'm interested in how actions are constructed and refined over practice-- is this selection?
	- i want to know how you determine, through trial and error, *what* movements to make. how do you use the information you glean from acting to learn how to update your policy? how do choose actions in order to gain this information?


# andy (didn't meet)

- end of september
- hardware
	- frame -- 2 tweaks, attach to table
	- armband -- 3 test prints
- software
	- wait for goncalo to set aside time
	- block out python side (filenames, metadata, constants, messages, etc)
	- TEST TEST TEST

# dan 26/8/20

- Krakauer slides / strategy
	- is my policy gradient explanation ok?
	- DTW
		- normalizing time v. aligning time series
		- model vs. data
		- DTW all-to-all or all-to-target (model prediction)
			- the latter gives you error automatically
		- run this and compare to interpolation scheme
- 1-step-back analysis -- what is this?
	- it's a way of x-raying sequential decision-making
	- question is: **what's the learning rule?**
	- it's like a filter
		- prior experience -> filter -> next trial behavior
	- translate that into motor domain...
	- how does a random prior turn into an optimal controller?
	- learning rule has a signature, the N-step-back thinking tries to identify it
	- the output is a plot of how a policy changes due to previous experience
		- x-axis: current trial feature
		- y-axis: past trial feature
	- there is no model attached to it
		- select most "relevant" feature of each trial
	- the challenge here is selecting relevant features for the one-step back analysis
	- take a trial x time x state data block
		--> run your filter over trial dimension
		--> informative about behavioral adaptation and experience
	- more papers to look for: doing N step back analysis about how trial outcomes - influence future trial decisions
	- how do past trial trajectories influence future trials?
	- one way to do this is to stop thinking about models and just think about the problem that's being solved

- fast/slow, model-based/model-free
	- is this testable?
	- can a model be written that subsumes and explains two-rate stuff?

- The connection between OU processes / Langevin dynamics and the LQR solution. There is something that I can’t yet articulate that argues for less separation between exploration and exploitation— the changes in the parameters of your policy should directly reflect your current model of uncertainty in your state predictions. The update step to your policy should directly impact your sampling efficacy. It feels like this kind of “efficient/active/compressed sensing/sampling” stuff, but from a control perspective. Or maybe I don’t know anything and this is how these gradient update steps are designed? But it feels possible to write down an update step that maximizes your information gain from the next sample under your current uncertainty estimate of your model fit given past data.

# andy 20/8/20

- krakauer talk:
- dont skimp on my data
- present what I have here
- split half and half APT and EMG
- get feedback on the EMG


# dan 10/8/20

KL between an lqr and a random baseline controller
removing feedback might be non-ecological, focus first on the feedback data
feedforward v. feedback -- wolpert partial observability, neural comp 2020 -- not very good

model-based -- LQR produces trajectory distribution
	- how far is your trial from that distribution?
	- what is used to update the trajectory distribution?

model-free -- "one-step-back" analysis, one-step tasks in decision-making
	- e.g. p(stay ¦ previous trial)
	- bar plot -- model-based v. model-free
	- adapt this to motor control -- daw, gershman 2011 ???
	- exploratory

andy + co
	- definitive info about access to SWC
	- timeline for access, data collection, etc


# lior shmuelof

- arc task developed to study stroke rehab dexterity, task needed with dynamic range and trajectory
- motor can be described as the inverse problem of vision: discover a high D output to satisfy a low D goal, as opposed to discovering a low D input based on a high D scene
- submovements -- whats the interpretation here?
- subject-level analysis tracking subject-specific changes over trials
- interested in comparing muscle activation and trajectory control with artificial controllers, trajectory optimisation
	- what cost functions, feedback vs. Feedforward
	- generative models  minimum jerk model, Jason Friedman
	- building a better control policy
- imaging  something in the brain, decision rules are changing
- during consolidation the controller is changing
- Fitts Law
- subjects can learn the task without feedback! just given knowledge of performance
- feedforward planning with feedback on top depending on the state?
- was improvement test effect or something else exposure to the task
- how does the policy know the structure of the task? how is the task formalized?


# kraskov 21/7/20

width of the tube is the complexity of the task

producing a 1D solution

co-contraction --> less co-contraction
principle --> minimizing co-contracting
smoothness of kinematics

EMG --> kinematics

task should allow you to use the long

in the long tail,
how do you test whether yu can do the task without

mechanics of the hand
activity of the motor neurons

andy jackson (newcastle)

pruzynski -- johansson (monkey fine wire electrode motor units)

# dan 15/7/20

- new rules to prevent interaction with subjects?

tube task
- jordan taylor
- exponential learning curve
- once accuracy reaches a threshold, you don't get better, but there is still learning
- iterative LQR --> good for me but worth it?
- questions
	- how many sessions

modeling

- interface with current psychological theories of motor control
	- implicit/explicit == model-based/model-free == type 1 / type 2 == slow / fast
	- how does LQR models link with these

- current models are descriptive!

- two systems
	- model-free Q learner
	- model-based LQR..?

- hierarchical systems
	- top-level = model-based, low-level = model-free
	- e.g. option framework
		- hierarchy in your compression of the dynamics

- variations on the tube task
	- triangular
	- less curvy
	- braun -- structural learning? entropy-reg RL?
	- entropy-reg model based RL

- replay
	- multi-day stuff?

- transfer
	- rosenbaum block experiments
	- behavior might be captured by entropy-reg RL

# goncalo 13/7/20

evidence from the struggles of engineering reliable systems
feels wrong that the brain is "corrupted" by noise
they work insanely well, better than anything we have in silicon (in a sense)
what is the canonical problem -- a motor problem?
self-modifying programs
integrate and fire model
neuronal control of locomotion
- simple model systems
output of the motor system
the animal can be reliable, but it needs to be constrained by the task
behavior is the control of variability (the control of perception)

frame the problem in a way thats fair
like vision -- not a summer project
how would i apply these algorithms to a real agent?
what is the "Go" for motor control
Go can be solved in "autistic mode"

e.g. soccer
go + movement control?
no quite -- requires "cunning", deception, theory of mind...
contextual decision-making


send
- goncalo thesis
- mainen slice paper


# dan 11/7/20

krakauer / haith chat
	- data sharing for analysis / modeling
		- arc task data
		- ant game task data
	- collaborate to build the EMG setup
		- get help with the software setup potentially?
		- get good feedback on the experimental design
	- goncalo help with EMG setup

# krakauer 9/7/20

thanks for dana ballard and john rothwell
feel exactly the same about roger lemon

phd advice
career advice -- how did you decide what to do?
robots, connection to human learning/control
video games -- help with my task?

optimal control / modeling?
what do you see as fruitful directions for modeling?
what does it mean that cognition is dynamical? (van gelder)

what would you do with my task?

a divide between psychophysical/computational motor control and physiological motor control is still with us to this day. Per-haps a new book is needed that brings these two approaches together.

studying computers
	- hardware
	- software
	- abstraction

plot of time to expertise v. skill real-worldiness

crazy complexity idea -- rare events drive learning

cost functions -- inverse RL ?

## BLAM lab

Why does it take so long to become an expert musician or athlete?
What it is that practice is making better?
What is the role of verbal instruction and declarative/explicit processes in acquiring motor skills?

## ordinary

interpretations into results
formalization isn't conception

uncoupling between physiological and computational

## notes

argues with jorn D about sequences not being the same as continuous actions
david habadon -- ant car iPad task
Adrian Haith task -- bimanual left/right, up/down
James Murray -- Rui Costa, Larry Abbott
haith -- arc tracing task

de novo learning is
- action execution
- action selection

practice-induced acuity
different computations / learning rules at different levels of the hierarchy
	- we know this from pathophysiological cases -- different abilities to learn

difficulty arises
	- interference with prior mappings / movements

you can't call it transfer if you're choosing from an infinite space of movements

**what does progress look like? when do we know when we've learned something about learning?**
	- i think we can

why does the task need to be high-dimensional? (critique) maybe:
	- proxy for real-world tasks?
	- qualitatively different behavior at low and high dimensional mapping
	- longer training time means learning is stretched out
my answer:
	- need an environment that is totally unfamiliar
	- need a mapping that is completely controllable
	- want to record the entire picture of what's happening in the arm

recommended james murray
https://blogs.uoregon.edu/murraylab/publications/

# motor symposium

## Abi Person
underactuated / intermittent actuation
how do you test for underactuation?
"we learn to underactuate"
early: co-contraction
late: less co-contraction
"learning of economy"

## Andrew Pruzynzski
learn what's happening at the periphery
injection of lidocaine to cancel mechanoreceptors
contact events are feedbacks for ongoing motor plan

## Amy Bastian
- we should build a development "growth curve"
- infancy = 700 synapses per second (Conel 1959)
- 2yo has 2x synapes of an adult

## Chethan Pandarinath
- LFADS
- single-trial analyses
- dynamics = predictable

## Philip Sabes (very cool)
- how do we get so GOOD??
- architecture + learning
- genetics + experience
- Bostan and Strick 2018

## Lena Ting
- Richard Murray control lectures
- Ting 2015


# andy 24/6/20

### phd thoughts

phd is a grounding, a through-line, space to explore/learn
	it's purpose is to gain experience working on a long-term project, documenting everything
there are always limitations with a project -- finding those quickly is important
this is a hard area, something people shy away, but that's why it's really ripe

recalibrating, reframing how my phd fits into my life
the phd is ONE part of a bigger story

once i have an idea, i seem to let it run away and expand in my imagination until it's the singular narrative, then I get overwhelmed

work on not moving the bar up and up, but setting it a good height and jumping
maybe it's less like high jump, and more like hurdles? it's okay to stumble

can i find links between political activism in georgia and motor control?

how to split my time?
phd stuff + everything else
plan the week on sunday!
am / pm split? this is good for separating
we need some minimum amount of projects to do
	- retain sense of urgency, don't get overwhelmed with one thing
important to make incremental progress on the phd in the "background"
no blank space in calendar -- this inevitably gets filled up with dumb stuff

meet at the start of the week to plan (monday)
discuss project + politics together

ask goncalo for code review when the time comes

### VC meetings

meet people through network
UCL is on the first patent


# dan 22/6/20

### advice stuff

this could just be a rut, so don't do something you'll regret
clear that I want to developing new systems + modify existing systems for the better
bouncing short-term / long-term is not sustainable, have to stick with or bail
being too ambitious with the timeline -- EVERYONE does this
e.g. The Wellcome Trust Fellowship -- Peter D: "enough rope to hang yourself with"
 	Dan abandoned several projects after pushing too hard on them
		e.g. conformal diffusion flow -- model for neural coding -- already exists

ask yourself:
	- is this just a means to an end?
	- or could you be learning lessons now that will help you in future ambitious projects

"few but ripe" -- Gauss, on having so many unpublished ideas

one idea to shift:
characterize only behavior (vs. EMG) with more sophisticated models

we all find ways to distract ourselves to procrastinate

opinion:
i will regret leaving
might be the only chance in my life to have this level of total intellectual freedom


### work stuff

fundamental dichotomy -- open/closed loop, feedforward/feedback = do i need state information in my controller?

information bottleneck perspective in the control setting
e.g. high DOF forces/dynamics --> low DOF muscle coactivations/synergies --> higher DOF neural signal
bottleneck at the muscle activation to predict "synergies"

evolved the bottleneck to learn flexible skills -- the bottleneck produces efficient representations (at the muscle level) in order to produce distributions over trajectories

distribution of trajectories marginalized over all tasks
	- how do i design a controller
	- how do i design a plant
info bottleneck might be a good system-agnostic framework for this design:
	- input distribution is important for output distribution
	- motor cortex -- compressed representation (e.g. single neuron coding == latents)

why isn't info bottleneck SOTA?
	- not scaleable
	- need to know a lot of things about the system

what's achievable? what timeline
if the code is something like 50% done, then you should muscle it out

high-level years
1. know what you're doing (4 months -- EMG behavior modeling) = October 2020 goal
2. ?
3. ?


# josh merel 12/6/20

what does it mean that these solutions don't appear natural?
because we've built

interpretability - hope that principles fall out of your models? sergey levine versus emo todorov?
	- sparse neural sequences

connection to neuroscience - what would you want to know from a human experiment? what might a human motor control experiment help you do? reverse engineering? human motor control

- what if most of our motor skills are "structural" -- aren't actually learned? built into the system, constructed rather than built from scratch

what do you think is the greatsest unkonw?

neuroethology slide -- what about Lopes goncalo's work

shaping exploraton -- constrining the action distribution
constrain the exploration distribution on the action space?

how do you learn skills?
how do you represent them?

what is the distribution of behavior-- learning is shaping this distribution
we're making random movements all the time, but it's effective because of the distribution underlying that randomness

designing curricula for training to get the desired, complex behavior
(multi-task training with curricula)

hierarchy of movement

rapidly responding to new tasks / new environments

# andy 12/6/20

pitch bootcamp as two parallel streams

remote pair programming?

- i dont know what my job is
- job is to sell a story

view from outside uni:
academics are crazy people who don't want to make money
most unis in the UK take 50%
US unis usually 5-10%



# dan 8/6/20

- sfn abstract
- motor primitives / linear basis functions
	- let's make a prob. model of these and fit it across trials?
	- what is the hypothesis?

# matt 27/5/20
pain
sports
instruments
do people break into clades?
how do you measure frustration?
asking
- how well do you think you're doing?

# alison barth 26/5/20
- what are you doing here?
- do you like CMU / why?
- what's driving your work? what are your big questions?
	- what's needed to move towards understanding?
- advice for an engineer interested in neuroscience?
- what do you think we can say that reflects cortex?
- what would you want to know in this setup?
- how could this setup help you ask questions in the mouse model?
- what sort of models would be interesting for you to test? esp. relating to control, costs/optimization, representations?

## feedback
- start with something simple, a single finger moving
- if muscle activations are conserved, neural algorithm is probably conserved
- if muscle coactivations (strategies) are different, what do we learn?
	- what aspect can we say is common among subjects?
- how do you get the same muscles session to session?
- how many variables exist, and how many can you control for?

## people
- steve chase
- byron yu

# dan 26/5/20

## thought
- we could have people learn more than one game at once using the same mapping to test whether most of their learning is spent on the mapping or spent on something about the context of the game / visual information. think about this like making the exact same movements but with different visual feedback. as long as the two games lined up in muscle space, you can flip back and forth and see how fast people transfer to the new task.
	- this might be a good control to see if people are learning the mapping or the game contingencies
	- good check to compare transfer between feedbacks and actual mappings
	- what kinds of perturbations would prevent someone from learning the second task, even with the same mapping?

## discuss
- dan's idea
	- train you up on coordinated muscle activations (reach to point A) and (reach to point B) then test you on a linear combination (in visual space) A+B. But what if the corresponding A+B control signal rotates you out of the muscle manifold?
	- what does this training look like? maybe direct feedback?
- go through the spaces diagram, this might be good discussion of the geometry of linear spaces? which would help me come up with mappings, etc
	- we don't want to kill certain synergies, we want existing synergies to be suboptimal for the task, and different synergies to be optimal? We need a way to leverage the fact that synergies found through calibration won't reflect all synergetic action or all constraints in the system, and alter the mapping to allow you to use other synergetic action as well as producing new coactivations.

## feedback
- berger 2012 paper
	- too harsh, not enough information to learn new activations
	- if you're still holding the joystick, how can you explore new coactivations?
- barth feedback
	- lower dimensional output is less flexible, can't ask how you flexibly transfer, etc
- types of calibration
	- naturalistic (training then shifts out of naturalism)
	- eye calibration, driven by bounding the space of movements
- we're less interested in the limits of motor activation / physiology than the dynamics of activations
- paradigm could be 1. calibration/train then 2. calibration/train/test
- task with single muscle activation --> mapping A, mapping B --> single feedback
	- exploit mapping redundancy to see how a change in mapping affects learning?
	- what is it about the dynamics (mapping) that makes something easier to learn?
- **SRs-- how much variance is accounted for by the eigenvalues of the SR
	- can we tune a task this way? to design a task with different "width" of dynamics?**
- basic validation project
	- psychophysical sensitivity to e.g. noise in the feedback / mapping

# andy 22/5/10

# data club 20/5/20

## Dan

### presentation / slides
1. Maybe go through the “current status of motor learning” slides slower. Maybe you don’t need to do both force fields and visuomotor adaptations.
2. Would be nice to see a specific example of what we want from a better model e.g.
- can be predict the adaptation of an entire motor trajectory pre/post an environment interaction?
- Do people optimise different elements of the motor policy at different times?
- What order?
- Do people reduce variability in task-irrelevant dimensions first then task-relevant?

**make a more detailed cartoon of the model predictions**

3. Give people more time to think. Take more pauses etc.
4. Slides are a little busy, a lot going on in each one, maybe simplify.
5. In general, there was a significant emphasis on the flexibility of the experimental approach. This is cool, still early days etc. But I do think experimentalists (reasonably) will be left wondering what is the fundamental point. Just because you make up a simple concrete proposal doesn’t mean that will be the end product - just gives people something to latch on to and proves that the experimental result can be applied to a specific question.
6. No need to agree with people’s imagined “criticisms” without them saying anything :) Comes across slightly defensive. Just address the issue as your own criticism of your great idea that you are dealing with.
7. If you choose to, I think you can robustly present yourself as a neuroscientist even to ephys people.

### questions
Jorge’s question:
maybe nice rule of thumb regarding the computational world you presented -
motor adaptation -> systems identification + transfer
skill learning -> (complex) policy optimization

Alison Barth: good question. I would agree somewhat more with her than you did. The function of motor cortical activity is to control muscles. If we don’t know how muscles are adapted, then how can one hope to predict motor cortical representation/adaptation. State-space models based on error/velocity etc have not been terribly effective in that endeavour.

G.lopes: he hit upon a nice intuition. sequential DM is usually high-dimensional state-space to low-dimensional control space. Motor control is the opposite.

Jorge and G.lopes:
I think its an interesting suggestion to close the loop with an end-to-end system but maybe not a priority! (pixel based learning)

### task
I had another thought on (compositional) transfer:
Maybe an interesting experiment would be to test whether people can perform “congruent” and “incongruent” compositional transfers. I use the word “congruent” to mean “congruent” with the admissible correlative structure of the muscle activation space. So I train you up on coordinated muscle activations (reach to point A) and (reach to point B) then test you on a linear combination (in visual space) A+B. But what if the corresponding A+B control signal rotates you out of the muscle manifold? I think this might be particularly nice because (1) its not something that could be tested with mice or monkeys really and (2) turns the redundancy between motor cortex and muscles into a positive point.
Regarding cortex->muscle redundancy: part of the discussion (e.g. Barth/lopes) pertained to the ability of you to say something about motor cortex given an EMG readout. So a criticism along these lines would be that cortical model space is vast and maybe you can’t say much directly. However, you could argue that this redundancy gives you a useful degree of freedom when it comes to “neural problem-solving”. This is a term that I just made up that refers to the brain trying to solve incongruent BMI problems e.g. Byron Yu’s out of manifold rotation. Since Byron Yu records from motor cortex and asks this system to shift to an incongruent pattern, it can’t do so by definition. However, maybe motor cortex can use its redundancy wrt to muscles in order to neurally problem solve for muscle outputs. That is, motor cortex cant operate outside its own neural activation space, but it can shift muscle activations into novel regimes which equivocate to inaccessible muscle activations from the task perspective.

**cortical model space is vast, but is has constraints. the mapping from cortex to muscles is redundant-- does it/ is it able to leverage this redundancy in a task where it is required to do so?**

### notes
- motor control is high-dimensional control space to low dimensional task space
- most decision-making / perception is high dimensional input to low dimensional control/feature space
- motor adaptation is system identification and transfer (retuning an existing controller) while motor skill learning might be thought of as policy optimization
	- but doesn't skill learning too require system ID?


## Jorge
I’ve been playing with suboptimal feedback controllers where the dimensionality of the feedback is constrained. The idea is that, rather than learning the whole end-to-end feedback mapping from sensory input to muscle activity (or motor cortical activity in the BMI case), the subject is learning a mapping from sensory input to some low-dimensional space of “motor commands”. This could allow for rapid learning by massively reducing the dimensionality of the learning problem.
The tradeoff, however, is that the controllers that you can learn in this way are necessarily suboptimal, since you are constraining the dimensionality of the control input (formally, what is going on is you are constraining the rank of the L matrix in your LQG slide).
I haven’t done any modeling on the actual learning of these controllers, but I’ve been examining their suboptimality. From the BMI perspective, my question is whether this idea can replicate the Sadtler et al. “neural constraints on learning” result: do these low-dimensional suboptimal solutions work only for within-manifold perturbations but not for outside-manifold perturbations? I have some preliminary results suggesting that the answer is yes, but still to be fully fleshed out.
From the perspective of your setup, it could also be interesting to think about what behavioral consequences these suboptimal controllers would predict. It’s also a fascinating question to think about what this low-dimensional space of “motor commands” is (e.g. motor commands corresponding to different grasps), and how this relates to your movement onion. This question might also have some bearing on transfer learning/generalization. Because you’re working with humans, you could also think about manipulating this variable via verbal instruction.
You can also extend these ideas to state estimation, and ask about how low-dimensional (and thus suboptimal) internal models might bias behavior during and after learning.


## Alison Barth
For a decoding algorithm approach, why not focus on the muscles?  The signal is much less filtered.  Of course, muscle contractions will be driven by neurons, and so they are a proxy for an upstream computation.  (My research interests are in how the organization of cortical neurons enables specific computations or patterns of neural activity; specifically with respect to synaptic changes during learning, so I am accustomed to the bewildering task of trying to extract meaningful information from hundreds of spiking neurons.)


# dan 18/5/20

## optimal v. oracle control
- what does path programming's oracle need? do we care?
	- needs a model (transition probabilities)

## goals
- working towards first paper
	- stick with python spaghetti for now
		- fixes
			- reduce number of processes
			- separate simulation from rendering
			- sychronization of processes
				- use barriers
			- save game events
			- record game events
			-
- simple game, stable data acquisition
- specifics of task, setup
- validate
	- lag/latency
	- jitter frame-to-frame
- characterization/statistics of EMG
- simulate LQG policy gradients, basic versions

## go through slides

### feedback
- think about a biomechanical model from the motor unit level that we could use to validate / compare our activity manifold with
- Look at Byron Yu's factorization / reduction technique
- how sensitive are subject to parameters of the feedback?
	- noise / sensitivity / mass of the cursor vs. behavioral error / learning time
- think about force
	- with a 2D force joystick, you can think about how well EMG can predict force, or if subjects refine their control beyond just producing force output
- what is the control condition (the control B matrix?) and what is the experimental condition?
- i'm thinking of model comparison correctly

### next week
- how does that myocontrol paper define the null space of their task? understand the spaces diagram

# dan 11/5/20

## feedback

- GOAL: policy gradient over synergistic components
	- policy gradient -- reinforce, policy gradient theorem
	- components -- what are the components of the motoric representation
	- normative theory:
		- because representations are hierarchical, you will refine a motor plan, a controller, from coarse to fine
		- design a task that asks a subject to fill-in a motor plan in a new environment, leverage EMG to track components of the motor output
- two experiments
	- learning (learning models)
		- there is a lot to do in this space to develop process-level theory about motor learning, but this is a hard problem. will come in time?
	- control (learning policy) / planning
		- this problem is "easier" -- work on a continuous-space version of lesioned SR-type controller, or lesioned LQR
- there isn't much work on learning the SR
- motor trajectories as a cognitive readout
	- wolpert decision theory stuff -- change-of-mind paradigm
- two ways
	- plan + execute (shows the plan)
		- go before you know
	- online feedback control
- goal is to design an experiment where the multi-rate models can't capture some phenomenon
	- within-trial statistics
- SRs
	- Kim's paper (will be a classic)
	- SR eigendecomposition
	- Successor features, linear function approximation
- can we look for the motoric representations?

- work on notes being more readable
	- dont send something to read if it isn't polished enough to respond to
	- dont send/show figures without clear labels, etc

### setup plots
- show off cursor movement
- how to think about the geometry of this?

### data club slides
- is my explanation of this iterative LGQ solution okay?
	- what constraints does this place on the setup?
- why LGQ-PPP? what about model formation problem?
	- how to think about system ID and control together? (e.g. is wolperts model even about control? it seems more like robust state estimation? but how do you actually learn the control problem?)
	- what other models are in this class? what makes this impactful?
- what do you think about slow/fast, implicit/explicit, model-based/model-free?
	- in teasing apart model-based / model-free, can we build a model akin to a two-rate which supposes some cost-driven tradeoff between these strategies?
	- what is a normative model where rate-based models fall out? this would be a huge step forward, i think.
- these multirate, LDS error models
	- how would we directly compare-- what would we see on a given trial?
	- why don't these exist?
	- why hasn't someone done the lesioning thing?

### SR
- what feature of motor learning can be well-described by representation learning
- can we think about SR learning as a means to

### meta
- how can I get better at setting and achieving goals? feel like I'm bouncing around too much-- how do you do maintain focus?
- overwhelmed with setup work + theory learning -- how to compartmentalize?
	- i think by have much more concrete goals, achievable bite-sized tasks

- Mussa-Ivaldi learning task
- momennajad review
- wolpert motor memory / PGM model

# andy 8/5/20

- need to find a balance between theory and experiment
	- schedule in / reward myself with math
	- count hours
- weekly checkins
	- help with short term
	- make subgoals

- slides
	- bashing adam hantman -- ok, but it is "dexterous for a mouse"
	- circuit slides
		- focusing on unique
		- leave it as a question
		- make point that you couldn't really do this in mice
	- levine slide
		- know this model well enough to explain it
		- RL field thinks about this
	- 4 slides in -- what am I doing?
	- we have no model -- are you going to give it to us?
		- reframe as a challenge, let's work on it
		- this is worth thinking about, approaching with a new paradigm
	- X put goals after quote slides
	- background / lit review
	- address motor equivalence problem / bernstein
	- ADD
		- todorov EMG
		- why EMG? the last stop from the brain to movement
		- myocontrol paper key results (quotes)
		- here's where we're at with the EMG rig
		- citations


# jesse 6/5/20

### questions
- how to maximize effectiveness of having a busy and too-smort advisor
	- set up a weekly meeting
	- figure out how to get the best out of each

- what directions to pursue to adapt RL stuff to continuous space/time?
- how to think about the learning problem?

~

- DQN (even not deep) might even be possible with linear
- learning the model -- using prediction error
	-
- learning feature transitions vs feature --> state transition
	- mapping / representation from features --> state

- concrete task
	- two reward structures, same dynamics
	- task is to:
		- learn the dynamics in the first reward environment
		- move to the second environment and re-plan

- is planning an internal phenomenon or does it happen over trials?

- if over trials, is this noise in the estimation or control problem?
	- control = choosing actions, policy, maybe planning -- choosing steps
	- estimation = learning the state distribution, the value structure -- learning the latent
	- reward structure could reinforce the model

- learning to predict outputs from inputs knowing both is a supervised learning problem
	- e.g. R(s) = <phi(s),u> to learn u

# dan 2/5/20

### questions

#### math
- feel like I don't know exactly where to go, what I'm expecting to get
- feels like _you_ know where this should go, and I'm picking up the breadcrumbs
- can you try to dump everything you think about this, and what you don't know?
	- i don't know the known-knowns and known-unknowns
- how do counter functions map onto the continuous problem?
	- problem is I don't fully understand what these counters are serving
- where do I want to go? as specifically as possible, with model-based path-programming?
	- same goal as "explain LQG"
	- once I have a goal, let's design a dependency graph of what I need to learn to get there, including what I know already.
	- what is my next goal? what object do i need and why?
- there is a connection between OU, Langevin, Gaussian Process...path integrals? But what is this connection and why is it useful here?


# ginny slack chat 27/4/20

- make sure to check the anatomy for these things, maybe anatomy already tells us the answer to some questions
	- e.g. single finger = sum { multifinger } because muscles are tied to single and multiple fingers?
	- mapping this back to the actual anatomy gives it a particularly strong presentation-- linking theory back to physiology
- what makes a particular mapping easy or hard? does the difficult change the strategy?
- how do you titrate mapping difficulty in a systematic way?
	- follow the lead of BMI work?
- if you say you want to develop a normative principle, you have to say what that principle is


# dan meeting 6/3/20
- successor representation -- p(getting from k to i within episode) = D_ik
- natural gradient update (covariant gradient w/ fisher information)
- replay <==> planning, consolidation of planning
- you have a model of the world, and you have rewards from environment
	- this is all you need in order to learn!
- optimization -- geometric program is one that is convex under reparamaterization
- belief propagation is an approx method to propagate information around the state space, but it isn't really a normative principle for improvement at each step
- *** what directions in electrode/muscle space do you take to converge on an optimal policy? Hypothesis: the natural gradient in path space
	- is there any prior for this? what do error-based learning update models say you should move?

## path programming

(1) path programming is more general than KL-Control and formally applies to entropy-regularized MDPs in general (there is no controllability constraint).
(2) A key step is to have the path equations written in terms of occupation densities (this is like an “rosetta stone" representation to translate between paths and state-actions).

# dan 1on1 13/3/20
- computational
	- simple inference
		- bayes theorem update
		- perception
	- complex inference
		- planning-as-inference
		- control inferernce
		- PGMs with cycles
		- control
		- monte-carlo tree search
- algorithmic
	- simple inference
		- log-space drift diffusion bayesian models
	- complex inference
		- path programming -- gradients look like successor features
		- optimization
- RL for control
	- policy evaluation
	- policy improvement
- how does experience produce path programming gradients?
	- successor representations (1993, dayan)
	- universal value function approximators
	- universal successor features
- difference between theoretical and experimental work on learning and inference
	- theoretical -- models are learners and inferencers (EM algorithm)
	- experimental -- either learning or testing inference
- two stages
	1. learning stage -- learn the skill, new mapping, reach expert status
		- internalization of the model
		- ability to infer, predict dynamics
		- e.g. myocontrol papers of past / bmi papers
	2. planning / inference stage
		- given a goal, how does planning unfold?
		- how do you learn the optimal controls to reach the goal?
		- e.g. shenoy obstruction task, krakauer curved pipe task
		- compare at the end to the optimal control solution
		- over trials, compare to path programming solution
- the novelty of our setup
	- analyze the behavioral outcomes (the task space)
		- this is like the internal goal, top-level of hierarchy
		- what do you optimize first?
		- how do you transfer to a new goal?
	- analyze the peripheral latent
		- the underlying redundant actuation covariance
		- how do activations lower on the hierarchy generate optimal behaviors?
- on each trial
	- compare behavior to analogous optimal path programming solution
	- track what choices are made at the latent level (electrode level)
- how does the CNS overcome constraints to perform optimal planning?
- literature
	- BMI
		- batista, Yu
	- myo
		- todorov, etc
	- motor planning modeling
		- shenoy / churchland tasks
		- path programming / OFC
	- motor learning
		- Cisek model, euclidean error as metric
		- what other metrics for learning?
	- spinal circuits
		- how does cortex (high level motor planning) leverage low level covariance structure?
	- hierarchical RL
		- harnoja and levine, entropy-reg RL
		- all levels are controlled but there is a cost to directly control lower levels
- papers to write
	- EMG natural coactivations, dimensionality reduction, synergies
	- behavioral comparison for (continuous) path programming
	- EMG latent comparison to path programming -- how do we code path programming to solve a high-dim problem?

# najja columbia

churchland lab

how long -- 6th year

synergies are flexible
loadings on muscles change over time
synergies static or dynamic
synergies under voluntary control
	- trial by trial

pool is controlled as a pool
Farina blind source separation

implications for motor cortex
	--> dimensionality of descending output

recruitment --> absolves MC of controlling individual motor units

project:

monkey pacman
1D -- all manner of ramps/sinusoids
dynamic isometric constractions
recruitment during postures

> Roughly 102–103 motor units (MUs) control each muscle, providing myriad ways to generate a particular force profile. Nevertheless, MUs are believed to obey an orderly recruitment process, the ‘size principle’ (SP), wherein small MUs are recruited before larger MUs. Intriguingly, several studies report deviations from the SP during dynamic movements, but whether such deviations represent instances of a broader phenomenon remains unclear. We used mathematical optimization to develop predictions regarding optimal MU recruitment strategies. We tested those predictions using a new experimental paradigm and novel spike-sorting methods. Finally, we asked whether cortical recruitment of MUs extends beyond the single degree of freedom associated with the SP.
Predictions were derived from the recruitment strategy that best matched actual force to desired force. We modeled an idealized motor pool of five MUs of varying size. As observed empirically, larger MUs had briefer twitch responses. Optimization predicted that recruitment should obey the SP for steady forces, but deviate from the SP for rapidly changing forces. Specifically, there should be preferential recruitment of larger MUs, whose briefer twitch responses are better suited for rapid force fluctuations.
We trained a monkey to generate a variety of force profiles (steps, ramps, sinusoids, and chirps) via isometric contractions of the anterior deltoid, whose activity we recorded using 8 modified percutaneous electrodes. We leveraged Bayesian nonparametrics and optimal filtering to decompose EMG into the spike times of single MUs. For steady forces, MU activity lay on a 1-dimensional nonlinear manifold (as predicted by the SP), but departed from this manifold for higher frequency (>1 Hz) forces. MU activity in both steady and dynamic regimes were consistent with our model.
Our theoretical and empirical results suggest that MU recruitment depends both on instantaneous and future force commands. The need to consider the future suggests supra-spinal structures may play a role in recruitment. To test this, we used microstimulation of sulcal motor cortex, via a 32-channel linear array, combined with simultaneous EMG recordings as described above. Microstimulation produces artificial activation under experimenter control, yielding the potential to reveal degrees of freedom that are available but rarely used, and might be difficult to otherwise observe. We found that stimulation recruited MUs in ways that often deviated from the 1-dimensional manifold observed during steady force production. Thus, MU recruitment is flexible, force-profile specific, and can be influenced by descending control.

# andy meeting 12_11_19

i want to start a technology company
what do you want out of this? what helps you?
better engineer and networker than scientist


# David Holder emg clinic 27_1_20

this procedure takes about 10 minutes and will be uncomfortable but not painful
you will feel a slight scratch

normal conduction velocity
> 40m/s leg
> 50m/s arm (faster presumably because finer control?)
MUAPS 3-5mV

tibialis anterior -- 10k nerve fibers, 1k motor units
needle records volume  approx 1mm^3, records 10-20 MUs

amplifier has roughly 10uV of noise after filtering

carpal tunnel == trapped nerve in the wrist

brachius plexus:
ulnar nerve
radial nerve
medial nerve

Memorandum 45: Aids to the Examination of Peripheral Nervous System
Her Majesty's Stationer Office

moving the surface electrode less than a cm gives very different readings

people in pain often have no nerve damage, they just haven't learned to live with the pain, learned to ignore it

nerve autoimmune disorder-- antibodies for nerves themselves
demyelination of axons

conduction velocity slows by roughly 1m/s per 1degreeC

very little movement artifacts with needle EMG!

diagnosis types for nerve exam :
- neurogenic
- myopathic
- normal

# david holder meeting 1

He was really tough. He said I didn't have a clear objective, but from what I told him he thinks I have a choice:

1. Do behavioral tests and use whatever signal I want-- he seemed to think that just tracking the hand position with markers+IR would suffice. Try to improve the current models and maybe I can control a robot better. This, he said, is an engineering project.

2. "Do it properly" and use intramuscular recordings (or something else) to measure as many individual muscles in the hand/arm as possible. Think about how to measure motor cortex at the same time. Best thing would be to work with the Epilepsy Centre to ask patients with Utah array implants to do the task. He knows people there. He said this is "real neuroscience".

Now, I don't exactly agree with his dichotomy, but he has raised some valid points. He kept saying "I really don't understand what you're trying to achieve" but he liked my explanation of imagining you're a hand amputee and you need to relearn your muscle outputs because they've been randomly wired to a prosthetic hand.

His dichotomy rests on his argument that doing surface (or maybe even intramuscular) EMG tells you zip about what's happening in the brain, so it can't be proper neuroscience. I explained all about Todorov and how modeling the computation helps elucidate neural recordings, etc. He didn't buy it. He said without a clear hypothesis up front, you got nothing.

He suggested choosing one of the two aforementioned routes and writing a 2-page statement of purpose and what is known about that direction.

Lastly, he said he'd love to be involved if it wasn't purely maths and he would show me how to do intramuscular in humans in a clinical setting including how to find all the hand muscles.

I'm not discouraged, but I do have a constructive unsettling feeling. He said surface EMG will provide a "big mess".

Note that the amplifier we bought will work fine for intramuscular if it comes to that :)

also:
Nick Donaldson
3.06 Malet Place Eng Building
BCI neuroengineering work

also:
Art of the Soluble
Peter Medawar




PhD Proposal Draft Feedback

# Andy
- Try and tighten up the first page -- have all your main points up front.
- pull the three bullet point aims on the first page into one overall question
- too broad at the moment.
	- outline the aim as to “connect work on muscle synergies, corticomotoneuronal connections and algorithms of motor control to explore the limitations of human motor output and learning and develop mechanistic models”
	- towards one question
- I would remove the list of parameters on the first page, potentially move it to the end where it could fit in the “challenges” section?
- The list of questions at the top of page two I think is again a bit too much. Try and limit this down to 2-3 of the questions you think we can really make headway on.
- The part about CM connections and online error corrections is a great thought. Is there much on this?
“..the purpose of CM connections is dealing with online error corrections”. “Purpose” seems to be leading the section in the direction of saying that CM connections exist to help deal with the perturbations..is this what you’re thinking?
- Perhaps a similar point is
	- synergies may be set up to reduce the computational power required to generate specific common movements, but this comes at a cost of online corrections. So, how does the nervous system deal with this?
- The Prior Relevant tasks section does require some knowledge of each study to make the best use of your points. A line stating what each study looked at/their task design would be helpful.
- Second point in the challenges section. I see what you are saying here – but might need a little rewording. If you send it to someone who works on CM connections and say you want to resurrect the field they are working in, some people may take this the wrong way (I say this from experience,  having said similar things to people working in vestibular labs about how the field seemed to have gone cold, and it was often misinterpreted!)
- I agree the EMG is going to be an issue. I should probably read a bit more about surface EMG in humans as I really have no idea what people usually do in these tasks. Do people ever do combinations of fine wire and surface in the same subject? If you had one or two “ground truth” muscles in a recording, would that help validate/parse the signal from the surface electrode?

# Philip
- fine/flexible manipulation of objects is one of the big feats of human CNS evolution
- asking what are the (adaptive) constraints on a system is a wise question to ask.
- I don't get how you disentangle role of cortical from subcortical/spinal stuff in this study (other than by relating them to fractions and syns, which assumes the hypothesis is correct). Is that a major goal though?
- Would be good to see a specific task just as an example. Maybe even with a figure.
- What are a couple possible strategies for solving this task? Is the experiment you propose able to distinguish them? Even better, would the experiment also be able to demonstrate the existence of a third, unexpected strategy that could give you insight into control systems?
- "As far as we know, there is no prior work characterizing the difference between learning novel sensorimotor mappings which include perturbative elements." I feel like sensorimotor mapping and perturbations are psychophysics' bread and butter, respectively, so there must be some.
- Brief comments on prior tasks are unclear and depend on having already read those papers.
- 2nd to last sentence says "using direct electromyographic control" -- was this part of the plan the whole time, or just bringing it up at the end for fun? Would need more convincing for DEC.

# Kelly
- old/new M1: what method? What cortical layer? Know the details!
- Huk paper: what analysis? What statistical result?
- What is the key figure, abstract, summary of the ideal paper? the ideal result?
- Measure proxies for other things? EKG? Pupil? Skin conductance?
- Make intuitive, interesting visuals (a la Huk)
- What are our inbuilt priors? How do they help us learn?
- wisdom:
	- Measuring “learning” is difficult-- subject to subject variation is very high
	- The hand, even with pure EMG control, will have inbuilt, evolutionary constraints
	- Once you have the class of experiment-- take one specific case and run with it

# Nathan (25/7/19)
operational definitions of myocontrol and neurocontrol
this project provides a testable definition of myo- and neurocontrol
one mapping to start with:
- two motor units that are on the exact same muscle
- any sort of submuscular control that can be validated
Once you present a well thought through experiment, then we can offer specific feedback.