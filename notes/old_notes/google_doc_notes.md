# Google Doc Notes

Meta 
Come up with a 1 page document outlining your idea composed of the following
* A few sentences on the motivation for the idea
* A figure for the motivation of the method (e.g. an example of a scenario where existing methods fail) articulating some challenge
* Describe the 3 most relevant works, no more.
* A list of contributions (3) that describe how your work is different from related work.
* A list of deliverables (1-3) that should naturally emerge from the list of contributions.


Strategies for admin meetings
leverage the continuation aspect of the work
Show that i know where i’m going: building on a foundation
bring slides!!!!
project goal
prior art
outline / plan
lingering questions
what is the specific question/experiment?


Inspiring Quotes


“Donald Michie (who later founded the Department of Machine Intelligence and Perception at the University of Edinburgh), remembers Turing talking often about the possibility of computing machines (1) learning from experience and (2) solving problems by means of searching through the space of possible solutions, guided by rule-of-thumb principles.“


In 1945 Turing joined the National Physical Laboratory (NPL) in London, his brief to design and develop an electronic stored-program digital computer for scientific work. (Artificial Intelligence was not far from Turing's thoughts: he described himself as ‘building a brain’ and remarked in a letter that he was ‘more interested in the possibility of producing models of the action of the brain than in the practical applications to computing’.)




________________
Pre-Research Talk Goals 
* get Sessantaquattro set up 
* code up acquisition / control pipeline 
* record prelim 64ch data
* Basic analysis of grid data 
* reverse engineer 64ch connector -- single electrodes
   * What 64pin connector is this, and how do we hack it? 
* buy single electrodes -- size? Type? 
* determine electrode map


Two versions of naturalistic analysis
1. Anatomical
   1. group electrodes into "muscles", find correlations through time for muscle sets?
2. Unsupervised -- 
   1. interpret various dimensionality reduction methods
   2. build a map of available electrode space -- how much of electrode space do "natural" tasks have access to?
      1. how can we visualize this?
      2. scatter of windowed covariance?
   3. map orthogonalization in this space -- do we want to decorrelate individual electrodes?
      1. no... then we might as well use two electrodes…
      2. we want to learn a new covariance trajectory?
________________
Setup Notes 
Electrode Array Connector: 
* https://www.digikey.co.uk/product-detail/en/jae-electronics/KX14-70K5DE/670-1274-ND/1283399 
* The device is single-ended referred to a reference placed in a point without EMG activity e.g. wrist
* From Sessantaquattro you have an adapter that is passive and in between the electrode and the device, we can give you the type of connector that we mount on our matrices and if you want you can develop your own matrices
* We have the design of the 64SE connector itself, which we can replicate 
* Electrode Setup
   * Active v passive 
   * Silver v gold 
   * Size
   * Reusable vs disposable 
   * Built into a fixture / textile v. reconfigurable
Generating Data 
* First Try 
   * 1D periodic “latent” function (can be sampled over and over  
   * “Sources” have Gaussian tuning functions
   * Linear mixing from sources to electrodes, where |s| < |e| 
      * e = Ms   
      * M is a mixture of Gaussians 


Visualizing Data 
* Tried updating a matplotlib function, too slow 
* Tried PyQtGraph, also too slow after profiling
* Now leveraging the GPU to make a basic oscilloscope  
Key papers 
* EMG Mapping
   * Remapping Hand Movements in a Novel Geometrical Environment
https://www.ncbi.nlm.nih.gov/pubmed/16148276 
   * Flexible Cortical Control of Task-Specific Muscle Synergies https://www.jneurosci.org/content/32/36/12349 
   * Differences in Adaptation Rates after Virtual Surgeries Provide Direct Evidence for Modularity 
https://www.jneurosci.org/content/33/30/12384 
   * Follow-up on the previous paper -- critiques “direct evidence” 
https://www.biorxiv.org/content/10.1101/634758v1 


* Physiology
   * Subdivisions of primary motor cortex based on cortico-motoneuronal cells (Rathelot, Strick PNAS 2008)  https://www.pnas.org/content/106/3/918 
   * Neural basis for hand muscle synergies in the primate spinal cord
https://www.ncbi.nlm.nih.gov/pubmed/28739958 
   * Corticomotoneuronal cells are “functionally tuned” https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4829105/ 
   * (Un)tangled population trajectories M1 (Churchland) https://www.sciencedirect.com/science/article/pii/S0896627318300072 
   * Hand Use Predicts Sensorimotor Representation https://www.nature.com/articles/nn.4038 
   * Roger Lemon descending output motor control review https://www.ncbi.nlm.nih.gov/pubmed/18558853 


* Synergies 
   * Structured variability of muscle activations supports the minimal intervention principle of motor control 
https://www.ncbi.nlm.nih.gov/pubmed/19369362 


* Naturalistic hand movement
   * The statistics of natural hand movements (Wolpert) https://www.ncbi.nlm.nih.gov/pubmed/18369608 
   * Analysis of the synergies underlying complex hand manipulation (Ghahramani) 
https://ieeexplore.ieee.org/document/1404285 
   * Statistics of Natural Movements Are Reflected in Motor Errors (Wolpert)
https://www.ncbi.nlm.nih.gov/pubmed/19605616 


* Theory -- RL / OFC 
   * Dan’s ARN review with Daniel Wolpert
https://www.annualreviews.org/doi/abs/10.1146/annurev-control-060117-105206 
* Structural Learning, Wolpert+Braun+Mehring 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2692080/ 
* Levine  S. Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review. (2018).
* Tirumala  D. et al. Exploiting Hierarchy for Learning and Transfer in KL-regularized RL. \textit{arXiv} 1903.07438v1 (2019).
Tasks 
* Space using the Cyberglove + Linear mappings / subspaces 
* Synergies using individual muscles 
Notes 
* Synergies have two defining characteristics in addition to being task dependent; sharing and flexibility/stability.
* Micael Turvey, Mark Latash Dexterity and its development / edited by Mark L. Latash, Michael T. Turvey. With On dexterity and its development by Nicholai A. Bernstein.
* Nikolai Bernstein https://en.wikipedia.org/wiki/Nikolai_Bernstein 


Focus 
* how humans are so good at learning sensorimotor feedback mappings
* Use EMG as a learning signal readout 


Literature 
* Learning new mappings (~10 papers) 
* Synergies and their constraints (a lot, be judicious) 
* Physiology of primate lateral corticospinal tract (a lot, but key refs) 
* Naturalistic movements (2 papers)
* High-profile papers leveraging EMG
* High-profile papers about the hands in particular 
* Optimal feedback control / classic motor control literature 
   * Adaptation 
   * Perturbation response 
   * Internal models 
* Reinforcement learning for continuous control -- policy gradient methods as graphical model inference 
* Churchland / shenoy / yu folks thinking about neural manifolds and constraints on learning 


Task 


Sources of Structure
* Time/Space varying mapping
* Time/Space varying noise of mapping 
* Stationary/Nonstationary latent variable model for sensory feedback


Two ways (not mutex) 
* Take EMG → target data and run statistics on it (a la Draguwitsch) 
* Model (factorially?) an actor/controller/planner which fits the heuristic/approximated output of the subjects 


Questions
* How can we generalize this game? 
* What questions are meaningful to start working towards? 
* Is there a fruitful relationship between physiology and computational theory? 
* What strategies exist to compare sensorimotor learning? 
   * Sampling methods /  Stochastic posteriors? 
* A lot of the papers discussing suboptimality come from perceptual inference, how can we think about suboptimality in the case of inference as control? “Suboptimal feedback control theory”?


More complex environments 
* Direct control vs. control over the parameters of the passive dynamics of the cursor 
* Perhaps the transformations aren’t the interesting aspect? 
* How can we add time-varying behavior?
* How can we add passive nonlinear dynamics that are constrained into the workspace? 
* How can this generalize to 3D / VR environment? 
* Daniel Braun’s work with VR environments is very promising, but still requires manipulanda 
* The work by Draguwitsch showing that most perceptual variability is in the inference process-- how might this relate to sensorimotor tasks? Can we test the processing power? Can we reverse-engineer the approximations to advance our algorithms? Know this paper! 
* Implies learning the internal model of the passive dynamics? (Forward model)
* You need inference for inferring latent state of noisy observations 
* Ideal observers and ideal planners-- what are ideal controllers/actors? Does it make a difference? Take for example the paper with visual search and tactile search, where the search strategy is different. Can we take a task where you either watch passively and categorize and actively 


First stage
Learn fixed mapping between some control outputs and some environmental parameters
Second stage
Perturbing that mapping appropriately based on the question of interest


How do you create EMG → feedback mappings in a principled manner?
Think muscle → output → (feedback), less about the game itself
Literature on activating single muscles in the hand/forearm? Single digit control?
Are synergies learned or developed or both?
Two questions
Learning / unlearning of synergies? Mappings?
Perturbations to learned mappings
Goal
Design a game that provides the right feedback to tease apart our hypothetical spinal and supraspinal controllers-- make a claim that there are both synergies and not synergies-- perhaps voluntary control overrides these synergies, and once they are learned (the modules are combined in a sequence or on a manifold) they form a new module / synergy. That is, synergies are neither learned nor set in development, they are two facets of the same system. They appear as a result of the brain’s solution to the redundant control problem at any given time.
Design a task that recruits synergies, breaks synergies apart, and reforms synergies. Show that a controller that generates this behavior is a hierarchical one that leverages these modules for combination, recombination, consolidation to learn new motor skills and adapt skills to new inputs and environments.
________________
Meetings


Imperial 16/10/19
Hristo
* Does lower leg prosthetic, mechanical + MU control algorithms 
* Most people get stuck on the first step of generating intuitive and non-intuitive mappings in a principled manner, but often because a grant runs out
   * Takeaway -- get something that works “OK” so that you can start to set up the actual motor learning experiment 
* Sessantaquattro is easy, and gives comparable signal quality without the headaches (once you get the TCP communication working) -- main problem is for acquisition and subsequent closed loop, have to tell the amp when to start and stop recording 
* Will need to rig up some kind of electrode cabling solution-- want the unity gain preamp as close to the electrode as we can, and use shielding everywhere.
* Very clear mains interference in the signal 


Irina Higgins
* Symmetry groups to vector representations 
* Intermediate features
* Task agnostic, composable, dynamic/adaptable features 
* Symmetry == unalterable by transformation
* Color transformation can be thoughts of as symmetry of shape
* Untangled representations -- Todorov 2012
* Abstraction = hierarchical + compositional 
* Beta Variational autoencoder 
* “Euclideanization” 
* Geometry of cognitive space 


Tim Behrens talk 
* Can we relate perceptual inference representations to (optimal) solutions of control problems? 
* Find the structure of the problem 
* Path integration of arbitrary spaces
* How does representation of abstract spaces predict action/behavior?
* Helmholtz machine -- generative + inference/prediction
* All problems can be represented as a graph problem 
* Factorization -- leads to generalization, composition 


Patrick meeting thoughts 
* They’re going after submuscular because they see it as the direct way to achieve “high dimensional control”-- by learning to activate your individual motor units in a new way. 
* I think is that no one will do that, but that regular folks have tons of dimensions that can be tapped just by learning to break apart individual muscles from each other, that is, activate multiple units per muscle and over multiple muscles 
* you don’t actually use your muscles in a big variety of ways because there’s no behavioral need to do so normally
* you don’t need to make single units, you just need to learn how to make uncommon contractions that you don’t normally make in your day to day life when a task arises (like in a virtual environment) that demands you to do so 
   * Like navigating some new abstract space (building an internal model of such a space) 
* Questions then arise
   * How “uncommon” is uncommon? 
      * How far from some manifold can you stray with your muscles?
      * What is the timescale of straying off this common manifold? 
   * If handed a dataset of naturalistic movements, or even of some large number of tasks, what would we do? 
      * Run some dimensionality reduction 
      * Try to think about how to develop mappings from these embeddings 


First Step? 
* Take a dataset of naturalistic movement 
   * Where do you place electrodes?
      * Too few and you don’t capture motor-unit level activity 
   * How do you get high-dim recording without lugging around a giant amplifier? 
      * Bioelettronica has a 64 channel Wifi version? 
* Using a naturalistic movement dataset, you can generate embeddings that allow you to produce mappings in a principled manner that stem from this baseline


Patrick 11/9/19
* Multi-muscle
   * Natural behavioral constraints -- what’s in the long tail?
   * Timescales of this learning? 
   * Experiments are narrow in scope 
* Submuscular
   * Byproduct plasticity of the nervous system 
   * Capacity for learning 
   * Subsets of motor units 
* Progress at Ctrl-Labs
   * Submuscular → continuous control 
   * Spike decomp → grouping into muscles 
   * Python SDK 
      * Into high dim → learn to control 
* Simplify electrode session to session in a lab task
* Long term recording → hasn’t been done 
   * Synergies across tasks?
* Fancier Dim reduction on longitudinal data 


Dan 6/9/19
* Perturbations in muscle space, task space, goals
   * In the learned and unlearned case 
      * The distribution of responses -- are we minimizing KL between responses?        
* The Valero-Cuevas+todorov result is how humans solve the DoF problem at a muscle level with a finger, but doesn’t ask subjects to directly activate muscles 
* Steps to project 
   * Emg setup
   * Representational dynamics
   * Transfer b/w movements
   * Planning / preparation
      * Go before you know tasks?
      * Use this for internal representation, fMRI 
* Hypothesis -- default model + 15% variance for exploration/learning 
   * What is the normalized model for this hypothesis




Andy 4/9/19
* Farina -- how open OTBio 64, 384 systems?
   * Single reference electrode? 
* Why only 8 bipolar channels on the Sessantaquattro? 
* Look at other EMG systems -- not much… 
* Data club
   * Screenshot of SpikeTrainer
* How long are electrodes stable (O(hrs)?) 




Sasha 30/8/19
* Skeptical about EMG-- how much signal will you get, can you get actual single units? 
   * Talk to Farina, see what’s reasonable to get?
   * Is it sufficient for your hypothesis?
   * How many weights do you have to tune (as opposed to the cortex BMI where its basically infinite...)
* It’s cooler to center on learning new skills
* What “algorithms” do you use (what’s in the data) 
* There is a continuum of synergy -- fractionated (“states of control”) -- is fractionated “easier”? 
* Really likes Valero-cuevas&todorov finger task-- how can we follow-up on this? 
* PT tract damage 
   * Whole-hand grasp is still there, probably through reticular formation
   * Look at stewart baker for reticular formation
   * Precision grasp is usually lost… 
* CM connections aren’t actually direct, they’re in addition to other AMNs-- but they are much stronger than anything else (which is what you see when you electrically stimulate cortex and measure EMG) 
* 8 PCs results-- we’re not asking “how many dimensions”, we’re asking what that other 15% is doing. How is that fractionated, ostensibly CM connection-driven, 15% of hand movement controlled? In what contexts? You use 80% to get you close, and 15% to make sure it lands-- this is not just a hierarchical controller, it’s multiple modules with distinct, but intertwined, functional roles. 


Tom 30/8/19
* Committee: 
   * Andy as a home, 
   * Neil B to ground you
   * Tim Behrens in orbit? 
   * Get these three in a room once a month?
* Chapters
   * First EMG task 
   * VR+EMG task
   * Perturbations (goal, mapping)
   * Same task in a mouse
   * Same task in fMRI 
* Essentially EMG BMI 
* Perturbations -- to goal and to mapping -- different representations? Different pathways? (e.g. CRB vs CTX vs BG?)  
* Proposal
   * 2 pages, no fluffy language, exactly what the first task is
      * Granularity of tasks-- muscle activation differences between mappings? 




Andy 21/8/19
* Spec EMG setups
   * Price
   * Channels 
* Reach out to Patrick 
   * How long will he talk
   * What are his topics 
   * My idea -- Lit review historical
* Bug Kraskov again 
* Make date with Maneesh (after bootcamp)




Kraskov Pre-meeting Notes 
* Questions
   * How much are we to think about a connection between CM fractionation and a computational hypothesis we can experimentally test? 
   * What  sorts of computational principles can we derive from physiology? We’ve seen things like how we deal with uncertainty at a computational level, but how can we test this, armed with physiological knowledge?
   * That is, what physiological evidence might we take to form a hypothesis for a computational principle. 
   * E.g. todorov’s minimum intervention principle was tested on individual muscles of the finger in one experiment, but how might we extrapolate this to the hand or the arm in general, and how might out hypotheses be constrained by our physiological knowledge? 
   * For instance, how might a mirror neurons among PTNs work into a computational theory of the motor system? 


Dan email notes 
* I would postpone finalizing the MDP details until a hypothesis has been decided upon. 
* LQR with signal-dependent noise is the natural starting point for motor control.
* I think an interesting result at the interface of artificial/biological motor learning, would be to experimentally verify a computational principle in human motor performance, integrate it into an RL algorithm, and show that humans perceive the resulting policies as more “natural”. Usually, this would manifest as an increased inability to distinguish between human-generated and computer-generated policies.
   * “Cognitive AI” 
   * Science paper of Brendan Lake
   * BBS review of Lake/Ullman/Tenenbaum/Gershman
* VR can be used to interrogate the inductive biases in learning and implicit perception-action loops in motor control. This approach is being pursued heavily in rodents/zebrafish etc. I would suggest aiming to develop a research program that could integrate VR as a second step i.e. 
   * your first paper should focus on leveraging high-dimensional EMG
   * your second paper could be EMG+VR
* My bias is that the human motor system is extremely efficient representationally. That is, there is a deep latent hierarchy which can be flexibly modulated at many levels. Thus, regardless of the details of the optimization process, it can be completed in very few samples. Information-wise, the motor model is such that a huge range of optimal policies have very short description lengths. I suspect that EMG is better suited to studying representational efficiencies (e.g. hierarchy, transfer, modularity).




Dan post-meeting notes 19/8/19


“In RL, the root problem is the curse of dimensionality. Continuous control is particularly affected by this. Policy optimization can end degenerating into random search due to gradient estimation noise. All RL methods are basically ways to get around this - deep representations, imitation learning, trust regions etc. These methods sometimes lead to ok but inflexible (overfitted) policies. Thus, flexible/multi-task/transfer principles are at a premium. Progress on how the brain represents policy sets in an efficient/modular/hierarchical/relational way would be of interest. Translating such principles into inductive biases during learning even more so.”


Ultimately, mujoco tasks would be the benchmarks to test any new bio-inspired continuous control ideas. Also, I wonder if you could directly code up your task in mujoco taking advantage of the unity plugin for a really immersive exciting interface with the added advantage of being able to “plug” models into mujoco. This approach would probably facilitate the extension of your task paradigms to VR too…


On the weaknesses of EMG: 
“You could treat it like EEG for the muscles, as long as you have some signal, you’re controlling something” 
How do you compare the muscle activations to an agent with complete control over the signal? 


Dan Suggested Papers 
Lightest intro to entropy-regularised RL (via the linearly-solvable MDP framework):
Todorov  E. Efficient computation of optimal actions. \textit{Proceedings of the National Academy of Sciences of the United States of America} \textbf{106}  11478-11483 (2009).


Review on entropy-regularised RL:
Levine  S. Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review. (2018).


Default policy model for transfer:
Tirumala  D. et al. Exploiting Hierarchy for Learning and Transfer in KL-regularized RL. \textit{arXiv} 1903.07438v1 (2019).


Hierarchical entropy-reg RL model:
Haarnoja  T.  Hartikainen  K.  Abbeel  P. \& Levine  S. Latent Space Policies for Hierarchical Reinforcement Learning. \textit{arXiv} 1804.02808v1 (2018).


Policy composition in entropy-reg RL:
Hunt  J. J.  Barreto  A.  Lillicrap  T. P. \& Heess  N. Entropic Policy Composition with Generalized Policy Improvement and Divergence Correction. \textit{arXiv} (2018).


Dan pre-meeting notes 19/8/19


“Which approximations does the nervous system use? It may have evolved efficient approximate solutions towards solving problems in the areas of Bayesian statistics, decision making and control. The approximations used by the CNS may inform future algorithm developments.” (Kording & Wolpert 2006)


“Most of this work assumes a generative model of the task imposed by the experiment, but how does the subject build that internal model? What approximations does it use when constructing that model? Or do we know already that the model it constructs is effectively close to the optimal one? For what tasks?” (Denison 2018)


This work began by my curiosity about the limits of motor control coming off Ctrl-Labs work (not to mention my getting sidetracked working on mouse stuff). The most parsimonious explanation of the synergy “debate” is that we have a balance of control between fractionated at the muscle level and multi-muscle coordinations that are both innate and learned, but we won’t know for sure unless we dissect the spinal circuits. Beyond that, there may be submuscular control at the unit level but we don’t have enough evidence to confirm or deny this. 


“By analyzing the structure of an EMG time series directly, we can both build a model of behavior that tests hypotheses at the muscle level and leverage a higher-dimensional control signal to generate complex, interactive virtual environments.” — How, exactly? 


EMG signals from the hand → complex structured task → muscle-level predictions encompassing synergy+fractionation controller in a Bayesian framework? 
* In an RL-as-probabilistic-inference framework? 
________________
People
* PIs 
   * Daniel Wolpert (Columbia) 
   * Emo Todorov (UW) 
   * Michael Jordan (Berkeley)
   * https://mvlab.yale.edu/ 
   * Jorn Diedrichson (W. Ontario) 
   * Daniel Braun (https://www.kyb.tuebingen.mpg.de/71685/sensorimotor-learning-decision-making) U. of Ulm, Germany  


* UCL
   * Sasha Kraskov / Roger Lemon 
   * Simon Farmer (Institute of Neurology) 
   * Daniel McNamee d.mcnamee@ucl.ac.uk (theory, RL postdoc) 
   * Kevin Miller (Harris Carandini) https://kevinjmiller.org/


* Postdocs 
   * Meghan Huber (MIT)
   * Other 
   * Jeff Seely -- worked on M1 untangled response paper 
      * What are we meant to believe based on this? What is a better model? 
________________
Unity 
* Physics Engines have quirks because they’re discrete dynamics solvers 
   * https://www.youtube.com/watch?v=NwPIoVW65pE 
   * Check your 
      * Gravity 
      * Units 
      * Time step 
   * Change your
      * Masses
      * Iteration
      * Non-resolvable scenarios 
      * Drag forces (linear to quadratic) 
   * Uses a MIDI controller to tweak parameters of the game to make it less “floaty” 
* Still unclear when the middleware will run out, if/when we have to roll our own physics to engineer the feedback we want 
* VR
   * https://docs.unity3d.com/Manual/OpenVRControllers.html
   * https://forum.unity.com/threads/any-example-of-the-new-2019-1-xr-input-system.629824/ 
* https://www.raywenderlich.com/980-introduction-to-unity-scripting 
________________
Papers / Books 
Random / Historical  
Bernstein, N. (1967) The Co-Ordination and Regulation of Movement.
Kenneth Craik 
Karl Lashley 
Developmental Robotics — Cangelosi & Schlesinger 
Bodies and Other Objects: The Sensorimotor Foundations of Cognition — R Ellis
Representation
Hand use predicts the structure of representations in sensorimotor cortex
* Together, our results suggest that hand use shapes the relative arrangement of finger-specific activity patterns in sensory-motor cortex.
* Pattern distances correlates with structure of finger enslaving
* Natural statistics of hand use predicts single-finger pattern distances
Suboptimality / Bayesian Models 
Suboptimality in perceptual decision making (Rahnev & Denison 2018)
* We therefore advocate that the field drop its emphasis on whether observed behavior is optimal and instead concentrate on building and testing detailed observer models that explain behavior across a wide range of tasks.
* Romain Brette follow-up: To deny that human perception is optimal is not to claim that it is suboptimal. Rahnev & Denison (R&D) point out that optimal- ity is often ill defined. The fundamental issue is framing percep- tion as a statistical inference problem. Outside of the lab, the real perceptual challenge is to determine the lawful structure of the world, not variables of a predetermined statistical model.
* The disagreements among commentators may appear substantial, but much of the debate seems to stem from inconsistent use of the term optimality. Optimality can be used to indicate sensible behavior (adapted to the environment), globally optimal behavior (fully predicted from optimality considerations alone), locally optimal behavior (conforming to a specific model), and optimality as an empirical strategy (a tool for studying behavior). Distinguishing among these different concepts uncovers consid- erable common ground in the optimality debate.
* LPCD -- likelihood, prior, cost function, decision (d = sum( LxPxC))


Computational Precision of Mental Inference as Critical Source of Human Choice Suboptimality (Draguwitsch et al. 2016) 
* Really intense data analysis of sequential cue categorization task 
* Maybe inference is screwy because the task is completely uninteresting and has zero behavioral/ethological relevance? Would this change if the task were fun? If it were active? What about reward? Does introducing reward structure play into the “attention” factor, producing more “neural resources” to the problem? 
   * For attention, see Whiteley+Sahani 2012
* Extremely clever experimental design to control for sensory noise and decision noise
* imperfections in inference alone accounted for about 90% of human suboptimal choices in our task, whereas imperfections in sensory processing and response selection together form a negligible fraction. Thus, inferential imperfections constitute an important source of human choice suboptimality, which may have been underestimated by previous studies and confounded with imperfections in sensory processing or response selection.
                
Bayesian decision theory in sensorimotor control (Kording, Wolpert 2006) 
* “Which approximations does the nervous system use? It may have evolved efficient approximate solutions towards solving problems in the areas of Bayesian statistics, decision making and control. The approximations used by the CNS may inform future algorithm developments.” 


On the Origins of Suboptimality in Human Probabilistic Inference (Acerbi...Wolpert 2014)
* Good resource for observer models in practice, and comparisons of behavior to models 
* Our results are compatible with a proper sampling approach, in which an empirical distribution is built out of a small number of samples from the posterior, and then the expected loss is computed from the sampled distribution [19]. As a more cognitive explanation, decision variability may have arisen because subjects adopted a probabilistic instead of determin- istic strategy in action selection as a form of exploratory behavior. In reinforcement learning this is analogous to the implementation of a probabilistic policy as opposed to a deterministic policy, with a ‘temperature’ parameter that governs the amount of variability [50]. Search strategies have been hypothesized to lie behind suboptimal behaviors that appear random, such as probability matching [51]. While generic exploratory behavior is compatible with our findings, our analysis rejected a simple posterior-matching strategy [25,26].
* Our analysis ruled out an observer whose decision-making process consists in taking the average of k samples from the posterior – operation that implicitly assumes a quadratic loss function – showing that averaging samples from the posterior is not a generally valid approach, although differences can be small for unimodal distributions.
* In summary, we show that a decision strategy that implements a ‘stochastic posterior’ that introduces variability in the computation of the expected loss has several theoretical and empirical advantages when modelling subjects’ perfor- mance, demonstrating improvement over previous models that implemented variability only through a ‘posterior-matching’ approach or that implicitly assume a quadratic loss function (sampling-average methods).


Physiology                                 
Hand function: peripheral and central constraints on performance (Schieber 2003)
* Synchronization between muscles acting on different fingers or between motor units in regions of multitendoned muscles serving different fingers, how- ever, indicates that single premotor input neurons make connections to motoneuron pools or subpools that act on different fingers. These diverging premotor input neurons may produce part of the “spillover” that causes adjacent fingers to move when a normal subject voluntarily moves a given finger. Indeed, EMG studies have shown that, during flexion of a given finger, EMG activity appears not only in the region of FDP acting on that finger but also in regions acting on adjacent fingers (40, 66). Theoretically, the premotoneurons responsible for short-term synchronization of motor units could be any last-order inputs to the motoneuron pools, such as Ia afferents, spinal interneurons, or corticomotoneu- ronal axons. In humans, lesions of the corticospinal system elim- inate the majority of short-term synchronization between motor units, implying that most of the synchronizing input comes from the cortex itself (14, 20).
* To summarize, most of the time, the human hand is used for grasping objects. In grasping, a number of coordination pat- terns have been identified that might simplify the control of the large number of mechanical degrees of freedom and muscles of the hand. These coordination patterns emerge as kinematic and kinetic relationships among the simultaneous motion and/or force of multiple fingers, ensuring that the fundamental task of grasping can be performed simply, frequently, and reliably. As the hand is used for increasingly fine manipulation and as more and more fine finger movements are considered, the need for independent control of individual degrees of freedom in- creases. Each degree of freedom becomes necessary for some particular manipulative finger movement. Higher order princi- pal components are needed to describe the increasingly indi- viduated motion of the fingers, and a limited set of coordina- tion patterns constraining the behavior of multiple degrees of freedom becomes less helpful as a control strategy.
Statistics 
Statistics of Natural Movements Are Reflected in Motor Errors (Wolpert 2009) 
* It is well known that training on a task improves performance, but with diminishing returns as training increases (Newell and Rosenbloom 1981). Specifically, relative performance is often related to the log of the number of training trials. This logarithmic dependence of performance on training appears to be a universal law of learning that applies to a wide range of cognitive problems such as multiplication, visual search, movement-sequence learning, rule learning, and mental rotation (Heathcote et al. 2000).
* Synergies 


Endpoint Force Fluctuations Reveal Flexible Rather Than Synergistic Patterns of Muscle Cooperation (Kutch 2008) 
* the pattern of cooperation across target directions indicates that muscles are recruited flexibly in accordance with their mechanical action, rather than in fixed groupings.


Neural basis for hand muscle synergies in the primate spinal cord
* Our results suggest that the phylogenetically older premotor interneuron system provides synergistic control of hand movements upon which the newer corticomotoneuronal system superimposes more fractionated control.
* It is generally believed that the direct corticomotoneuronal (CM) pathway, which is a phylogenetically newer pathway in higher primates, plays a critical role in the fractionation of muscle activity during dexterous hand movements (19–21). However, the present study demonstrated that PreM-INs, which are phyloge- netically older, have spatiotemporal properties that correlate with muscle synergies during voluntary hand movements. Therefore, it is likely that these two systems have specialized functions for the control of primate hand movements, namely “fractionated control” and “synergistic control,” respectively.
* Optimization of balanced control may be an important factor also for the acquisition of new motor skills.
* Future studies should combine spinal recordings with different movements. These should aim to elucidate (i) how the clusters of PreM-INs identified in the present study are generalized to the other types of hand movements, (ii) how many and what variety of clusters can be identified when a wider variety of hand movements are tested, and (iii) the long-term plasticity of clusters required to acquire new motor skills.
* Notes 
   * This isn’t about learning-- the Berger paper is a great reference though, but that isn’t about CM. This paper makes the connection between CM fractionization and learning. How do CMs drive learning? 


The neural origin of muscle synergies
* While we do not know the maximum number of in-born and learned motor tasks each species may produce, it is conceivable that in any individual, the numbers of all task- specific and shared synergies combined may exceed the number of relevant muscles, in which case the EMGs recorded over all possible behaviors are not expected to exhibit a low dimensionality. This theoretical possibility raises the question of how muscle synergies of neural origin “simplify” movement control. We think muscle synergies simplify the production of posture and move- ment in the following senses. First, for tasks that can be executed by many possible trajectories or muscle activation patterns, a set of pre-existing muscle synergies can serve as a preferred channel through which the motor commands are specified. Muscle synergies thus effectively remove any musculoskeletal redundancy at the levels of posture (Santello et al., 1998; Weiss and Flanders, 2004; Bicchi et al., 2011), kinematics (Flash and Hochner, 2005), and muscle activation, by constraining how the muscles can be activated (Bernstein, 1967; Full and Koditschek, 1999; McKay and Ting, 2008). Second, for a single given task, the total number of shared and task-specific muscle synergies needed for its execution is still expected to be smaller than the total number of muscles. The set of synergies thus reduces the volume of the space of possible motor commands that the CNS needs to search through by defining a sub- space of a lower dimensionality. This is equivalent to a previous suggestion that preformed neural coordinative structures, such as muscle synergies, function to automatically eliminate muscle patterns that lead to uncoordinated or inappropriate movements (Tuller et al., 1982; Turvey et al., 1982). Such a reduction in search- space volume allows efficient transformation between task-level variables and muscle activations (Ting et al., 2012). This advantage conferred by a synergy-based control scheme may be particularly important for a task for which only a very small set of motor patterns is compatible with fulfilling the task requirements. For such a task, given the very large volume of the high-dimensional muscle-activation space defined by the many muscles of the limb, without any neural coordinative structures in place it would be very difficult for the motor system to discover, every time, a very small subspace of suitable motor patterns starting from any initial point in the space. The muscle synergies required could be a mixture of shared and task-specific muscle synergies either acquired through motor learning, or inherited over the course of evolution of the species (Giszter et al., 2007). Generating motor outputs by activating these synergies ensures an efficient and robust execution of a difficult task.
* One fruitful direction of future research is to determine precisely how the CNS integrates non-synergy-based mechanisms with the existing muscle synergies for the execution of a wide range of movements. In the higher primates and humans, there are two subdivisions of the primary motor cortex: a rostral, phylogenetically older region that contains descending efferents destined to the spinal interneurons, and a caudal, phylogenetically newer region that contains cortico-motoneuronal (CM) cells with monosynaptic innervations to the motoneurons of individual shoulder, elbow, and finger muscles (Rathelot and Strick, 2009). It is plausible that while the “old” motor cortex contributes to motor output by providing activation drives for the spinal modules, the “new” motor cortex further sculpts the activations of specific muscles by bypassing the spinal mechanisms through the CM cells. Controlling movement by combining muscle synergies and other proposals based on independently controlled muscles (Kutch et al., 2008; Valero-Cuevas et al., 2009) are not necessarily mutually exclusive.
* Ideally, a strong case supporting the neural origin of the muscle synergies extracted from the EMGs should come from a compari- son between the number of experimentally derived synergies and the dimensionality of the space of all muscle patterns suitable for the selected tasks.
* while the extent of synergy merging correlated with the severity of motor impairment (which reflects the extent of motor cortical damage), the degree of synergy fractionation var- ied with the temporal distance from stroke onset (which reflects how long the motor system had been influenced by post-stroke plasticity).
* While the precise roles of genetic control in motor development remains to be established, it is conceivable that sen- sory feedback from muscles and tendons triggers adaptive changes in the spinal interneuronal circuitry to tune or create modules specifically tailored to the limb biomechanics of the individual, and informs other areas of the CNS of these modifications. At the termination of these developmental processes, the biomechanical properties of the limb are fully incorporated into the architecture of the motor modules, thus resulting in a match between the plant and its neural controllers that allows high-caliber motor performance.
* It remains to be seen to what extent difficult and unusual movements are also executed by recruiting the synergies utilized in well-practiced behaviors.
* Also, at least for humans, with sufficient training even individual motor units of a single muscle could be voluntarily controlled (Basmajian, 1963). These and other additional mechanisms of motor-output generation further augment the flexibility of the motor system, and could conceivably play a role during the acquisition of motor skills (Kargo and Nitz, 2003).
* One fruitful direction of future research is to determine pre- cisely how the CNS integrates non-synergy-based mechanisms with the existing muscle synergies for the execution of a wide range of movements. In the higher primates and humans, there are two subdivisions of the primary motor cortex: a rostral, phylogenetically older region that contains descending efferents destined to the spinal interneurons, and a caudal, phylogeneti- cally newer region that contains cortico-motoneuronal (CM) cells with monosynaptic innervations to the motoneurons of individual shoulder, elbow, and finger muscles (Rathelot and Strick, 2009). It is plausible that while the “old” motor cortex contributes to motor output by providing activation drives for the spinal modules, the “new” motor cortex further sculpts the activations of spe- cific muscles by bypassing the spinal mechanisms through the CM cells. Controlling movement by combining muscle synergies and other proposals based on independently controlled muscles (Kutch et al., 2008; Valero-Cuevas et al., 2009) are not necessarily mutually exclusive.
* The synergies identified by NMF are time invariant non-negative vectors whose linear combination is found, through an iterative update rule, to minimize the error of EMG reconstruction, with the additional assumption that this error follows a Gaussian distribution (Cheung and Tresch, 2005). The extracted synergies thus reflect spatially fixed regularities (Kargo and Giszter, 2008; Safavynia and Ting, 2012) embedded within diverse muscle patterns.
* While we do not know the maximum num- ber of in-born and learned motor tasks each species may produce, it is conceivable that in any individual, the numbers of all task- specific and shared synergies combined may exceed the number of relevant muscles, in which case the EMGs recorded over all possible behaviors are not expected to exhibit a low dimensionality.
* This advantage conferred by a synergy-based control scheme may be particularly important for a task for which only a very small set of motor patterns is compatible with fulfilling the task requirements. For such a task, given the very large volume of the high-dimensional muscle-activation space defined by the many muscles of the limb, without any neural coordinative structures in place it would be very difficult for the motor system to discover, every time, a very small subspace of suitable motor patterns starting from any initial point in the space.


90% isn't enough
* the role of muscle synergies could be viewed as a source of flexibility in the repertoire of possible motor commands and stability in movement execution, as opposed to a way to simplify the control of movement by limiting the number of control inputs
* muscle synergy extraction has mainly focused on describing muscle activity in the input space, but has neglected the reconstruction of forces and movements in the task space
* assumptions of linearity were made in the relationship between input and task spaces, that is, muscle activations and forces


Early Skill Learning Is Expressed through Selection and Tuning of Cortically Represented Muscle Synergies Kargo and Nitz 2003
* Adaptation occurred at the level of both individual muscles and muscle synergies. Animals ap- peared to reconfigure preexisting muscle synergies with training (Porter and Lemon, 1993; Nudo et al., 1996; Wolpert et al., 2001). We quantified this by determining how the distribution of coher- ent muscle activities (IC weights) changed during training rela- tive to the weights of locomotor ICs, which are likely to be stable. Animals modified the weights of one or two synergies during training, and most animals modified one synergy in particular, which was distributed to extrinsic hand muscles and activated just before pellet contact. These weight changes were associated with changes in hand and finger kinematics before pellet contact and with improved grasping. The adaptation of IC weights pro- vides evidence that animals regulated motor patterns at the level of individual muscles.
* we found that animals commonly adjusted the amplitude of several stable synergies in parallel (e.g., Fig. 10, in which IC2 was increased in amplitude and IC3 was simulta- neously decreased during training). Animals reduced the ampli- tude of one synergy in particular that was distributed to antago- nistic muscles around the shoulder, elbow, and wrist. This adjustment was associated with straighter hand paths, reduced movement times, and improved targeting. Humans similarly regulate the amplitude of a widespread co-contraction signal during motor learning and thus rely less on viscoelastic properties of the limb (Thoroughman and Shadmehr, 1999; Osu et al., 2002).
learning new gait patterns
* * NMF on Lokomat walking
* if the control of individual muscles in locomotion was achieved by controlling a smaller number of motor modules, then there should be preferential exploration along these modules when attempting to learn a new task. We created a condition where participants had to learn a novel gait pattern by changing the foot trajectory to match a target template. Participants were able to learn this task, as indicated by a reduction in their error and variability over several blocks of practice, and also showed associated changes in the hamstrings muscle activity. However, our results showed no evidence of any preferential exploration – we found motor modules during baseline walking and target-tracking were substantially different and these differences were observed almost immediately at the beginning of target-tracking. These results provide evidence against the hypothesis that the muscle activity during locomotion is regulated through motor modules where muscle weightings are invariant.
* not only are the modules different under different mechanical demands, the change in composition of the modules happens in rather short time scales during the initial exploration phase of the new gait pattern, and therefore the identified modules are unlikely to reflect a neural control strategy.
* these results suggest that future tests of the hypothesis should focus on behavioral predictions of the motor module hypothesis


Robustness of muscle synergies underlying three-dimensional force generation at the hand in healthy humans (Roh, 2012)
* There is also emerging evidence that the nervous system uses independent strategies to control movement and force generation, which suggests that one cannot conclude a priori that isometric force generation is accomplished by combining muscle synergies, as shown in movement control.
* Four synergies were sufficient to explain, on average,95% of the variance in EMG datasets. Furthermore, we found that muscle synergy composition was conserved across biomechanical task conditions, experimental protocols, and subjects.


Analysis of the synergies underlying complex hand manipulation (Todorov, Ghahrahmani 2004)
* The  structure  of  the  synergies  we  extracted  (via  PCA)  was  task-dependent,  and  their number significantly exceeded previous observations in a simpler  grasping  task.  Our  results  lend  support  to  an  optimal  control explanation rather than a ìsimplicityî explanation.
* * synergies fall out of optimal control, line up with muscle activation
Tasks 


Learning and adaptation in speech production without a vocal tract (Thompson 2019) 
* mappings can be learned by remembering the motor commands that successfully produced desired target speech sounds. Furthermore, in many models, these mappings are contin- uous, allowing for generalization of previously-gained production experience to enable the production of novel speech targets. Once learned, these mappings are assumed to be maintained by comparing the auditory predictions made from the mappings with incoming actual auditory feedback during speaking. Mismatches with predictions can drive immediate corrective motor responses, and consistent mismatches drive update of the audiomotor map. This is called sensorimotor adaptation.
* Double exponential learning curve 
* Learning plateau in ~60 trials
* adding additional dimensions to the task for participants to learn would greatly hinder the learnability of the task. Indeed, the need to control many more acoustic factors than just F1 and F2 to produce full speech is a likely reason why the motor production of speech generally takes humans years to master. Thus, adding control of additional acoustic factors beyond F1 and F2 might have made the time to learn the task impractically long for a single-session experiment. Indeed, scientists have been attempting to produce electronically synthesized speech from component sounds as far back as Bell Labs’ Voice Demonstrator, “Voder”, a machine consisting of a series of filters that could be manipulated by a highly trained operator to produce speech sounds. This served as an early demonstration of non-linear mapping between circuit resonance and acoustic out- put production, albeit one with so many degrees of freedom that it was very difficult to learn and required a highly trained operator. More recently, other studies have produced alternate modalities for adults to learn to produce speech in the absence of the vocal tract. However, these modalities either provided visual feedback to facilitate production or required extensive, prolonged training to successfully synthesize speech sounds. In addition to lacking the ability to produce many speech sounds, touchscreen-based vowel productions are currently of fixed length and volume, which is not reminiscent of the continuous and highly variable nature of speech. Future iterations of the task could closer replicate the continuous motor demands of speech by creating a more dynamic touchscreen that would require continued contact for continued vocalization and would update continuously with changing touch location. This would allow for the dynamic vowel production seen in vocal speech and give us the ability to investigate such phenomena as participants’ responses to transient, within-trial feedback perturbations.
* A further consideration in our experiments is the nature of how motor goals required to produce correct auditory feedback are represented and learned, for example in muscle activations, joint angles, and endpoint finger positions etc.


Nazarpour https://www.jneurosci.org/content/32/36/12349  
* Able to produce new “synergies” between two muscles to complete tasks, respond to perturbations
* Uncontrolled manifold supportive 


Radhakrishnan https://www.jneurosci.org/content/32/36/12349 
* Anatomical mapping to force direction 
* More control over distal muscles (mentions CM) 
* Perturbations show increased usage of the hand, not output efficiency outright


Muscle Coordination Is Habitual Rather than Optimal de Rugy 2012


* The data show that contrary to predictions from optimal con- trol theory, motor coordination is not continuously optimized at the level of individual muscles. Instead, habitual muscle coordi- nation is surprisingly robust to various real and virtual manipu- lations of the limb’s biomechanics. Furthermore, the finding that muscle coordination is tied to the actual limb posture suggests that good-enough solutions to muscle redundancy are generated by a hierarchical control scheme in which muscle activity is partly determined by low-level networks whose regulatory functions are shaped by sensory feedback representing the current posture. In this type of scheme, control processes are distributed over sensori- motor networks at multiple levels, with high-order levels acting as controllers for lower levels, and low-order levels acting as regulators for higher levels (Raphael et al., 2010). The processes of evolution, development, and adaptation determine in parallel both the struc- ture of the circuitry within each level and the characteristics of the musculoskeletal system. Even low-order levels of the hierarchical control scheme should therefore carry useful information about the nature of the plant and the set of likely tasks to be encountered, such that explicit specification of muscle activations from the brain may not be required for successful task performance in most conditions.
* One advantage of an internal model is that it can be used to compute solutions to problems more rapidly than they can be discovered by trial-and-error learning, but this begs the question of how rapidly the model itself can be updated. A persistently inadequate internal model could be a source of persistently suboptimal motor habits.
* The behavior actually observed suggests that the central controller learns associations between tasks and control strategies that are locally optimal in the sense that they tend to increase performance and/or reduce cost for regularly encountered conditions, but that these associations then become motor habits that are not readily changed. Such a phenomenon would explain the emergence of synergies them- selves, as learned rather than hard-wired patterns of muscle use. The fact that various subjects exhibit similar synergies would then reflect similarities in their biomechanical constraints and in the circumstances in which they learned such habits.
* Our results argue against the view that muscle coordination is specified online by optimal control. This raises the broader ques- tion of whether motor commands of any sort (i.e., those repre- senting higher order features of movement) are computed by optimization in the brain or emerge from recalled control strat- egies operating on a hierarchical control system (Loeb et al., 1999; Raphael et al., 2010). Although the outcomes of both processes might often be well described by optimal control models, they have very different implications for the nature of processing per- formed by the brain, and therefore for applied fields such as neural prosthetics, brain-machine interfaces, telerobots and re- habilitation. Is the massive circuitry and processing power of the human brain devoted to computation of globally optimal solu- tions, or to classification, recall, and generalization of good- enough solutions? If the argument for computation is based on optimal control, then the evidence is mixed at best. Task goals are achieved in a near-optimal way in response to some types of perturbations (Chhabra and Jacobs, 2006; Izawa et al., 2008) but not to others (Ganesh et al., 2010; Kistemaker et al., 2010). Recent theoretical work demonstrated the capabilities of a hierarchical control scheme to simplify both motor execution, by acting on a low-level controller that judiciously augments the dynamics of the plant (Todorov et al., 2005), and motor learning, by exploiting the multiple solutions that arise while randomly adjusting the gains of a complex but highly evolved spinal net- work (Raphael et al., 2010). Such hierarchical systems would ac- count for the persistence of habitual coordination patterns that remained clearly suboptimal to all of the perturbations tested in this study.


Learning Optimal Adaptation Strategies in Unpredictable Motor Tasks
Braun et al. 2009


* the forward model of the system dynamics F depends in a nonlinear way on the rotation parameter between the hand and cursor position. This parameter is unknown to subjects before each trial and must be estimated online during each movement.
* Importantly, optimal feedback control requires knowledge of the environmental dynamics in the form of an internal model.
* online adaptation is different from online error correction (Diedrichsen et al., 2005), since the rules of the control process—i.e., the “control policy” that maps sensory inputs to motor outputs— has to be modified. Importantly, the mod- ification of the control law is a learning process, whereas online error correction, e.g., to compensate for a target jump, can take place under the same policy without learning a new controller. To enforce online adaptation the vast majority of trials had a standard hand/cursor relationship and only occasional trials were perturbed.
* To test for the possibility that subjects simply became nonspecifically better at feedback control, a second group of participants per- formed a target jump task for the first 2000 trials. In direct cor- respondence to the random rotation task 20% of the trials were random target jump trials. Since a target jump does not require learning a new policy but simply an update of the target position in the current control law, we would expect to see no major learning processes in this task. This is indeed what we found. In Figure 2 we show the same features that we evaluated in the random rotation trials to assess over-trial evolution of sensori- motor response patterns.
* we show that such adaptive responses can be explained by adaptive optimal feedback control strategies. Thus, our results provide evidence that the motor system is not only capable of learning nonadaptive optimal control policies (Todorov and Jordan, 2002; Diedrichsen, 2007) but also of learning optimal simultaneous adaptation and control. This shows that the learning process of finding an optimal adaptive strategy can be understood as an optimi- zation process with regard to similar cost criteria as proposed in nonadaptive control tasks (Ko ̈ rding and Wolpert, 2004).
* Another recent study (Chen-Harris et al., 2008) has shown that optimal feedback control can be suc- cessfully combined with models of motor learning (Donchin et al., 2003; Smith et al., 2006) to understand learning of internal models over the course of many trials. Here we show that learning and control can be understood by optimal control principles within individual trials.
* As already described, online adaptation should not to be con- fused with online error correction (Diedrichsen et al., 2005). On- line correction is, for example, required in the case of an unpre- dicted target jump. Under this condition the same controller can be used, i.e., the mapping from sensory input to motor output is unaltered. However, unexpectedly changing the hand– cursor re- lation (e.g., by a visuomotor rotation) requires the computation of adaptive control policies. This becomes intuitively apparent in the degenerate case of 180° rotations, as any correction of a naive controller leads to the opposite of its intended effect. However, it should be noted that the distinction between adaptation and er- ror correction can be blurry in many cases. Strictly speaking, an adaptive control problem is a nonlinear control problem with a hyper-state containing state variables and (unknown) parame- ters. This means in principle no extra theory of adaptive control is required. In practice, however, there is a well established theory
* of adaptive control (Sastry and Bodson, 1989; Åstro ̈m and Wit- tenmark, 1995) that is built on the (somewhat artificial) distinc- tion between state variables and (unknown) parameters. The two quantities are typically distinct in their properties. In general, the state, for example the position and velocity of the hand, changes rapidly and continuously within a movement. In contrast, other key quantities change discretely, like the identity of a manipu- lated object, or on a slower timescale, like the mass of the limb. We refer to such discrete or slowly changing quantities as the “parameters” of the movement. Therefore, state variables change on a much faster timescale than system parameters and the latter need to be estimated to allow for control of the state variables. This is exactly the case in our experiments where the parameters (rotation angle) change slowly and discretely from trial to trial, but the state variables (hand position, velocity, etc.) change con- tinuously over time (within a trial). Thus, estimating uncertain parameters can subserve continuous control in an adaptive manner.


Differences in Adaptation Rates after Virtual Surgeries Provide Direct Evidence for Modularity
Berger et al. 2013


* a reaching task using myoelectric signals to control the simulated force applied on a virtual mass
* Surface EMG activity was recorded from 13 muscles acting on the shoulder and elbow
* EMG activity was recorded with active bipolar electrodes
* If the arm is in a fixed posture, the force gen- erated at the hand is approximately a linear function of the activation of muscles acting on shoulder and elbow.
* Muscle synergies were identified by nonnegative matrix factorization (Lee and Seung, 1999) from EMG patterns recorded during force control from the go signal to target acquisition (dynamic phase)
* Muscle patterns diverge from synergy structure during incompatible surgery
* These results support the no- tion that a specific adaptation process is in- volved in overcoming incompatible surgeries and that this process is active when the set of synergies usually used for a task becomes ineffective.
* the muscle pat- terns at the end of the incompatible virtual surgeries were captured by synergies that were different from those extracted before any surgery.
* stud- ies have suggested that motor adaptation involves adjustments in the parameters of internal models of the body and the environ- ment driven by sensory prediction errors (Shadmehr et al., 2010) as well as changes of the control policies due to reward and rep- etition (Krakauer and Mazzoni, 2011; Wolpert et al., 2011).
* the observation of low dimensionality does not provide, per se, definitive evidence for modularity
* ***Our results suggest that two distinct adaptive processes with different learning rates operate in a modular controller. A fast process may be responsible for reducing the error between the force generated by the synergy combination and the force target by adjusting the synergy activation coefficients, i.e., adapting the sensorimotor transformation, possibly implemented in the cere- bellum (Shadmehr and Krakauer, 2008; Taylor et al., 2010; Galea et al., 2011). In our task, such a process is effective in gradually reducing the force error when adapting to compatible virtual surgeries, and it is likely that the same process is involved in adaptation to visuomotor (Martin et al., 1996) and dynamic (Shadmehr and Mussa-Ivaldi, 1994) perturbations. Indeed, in the washout phase after compatible virtual surgeries, clear nega- tive aftereffects were observed, indicating that a modification in the internal model had occurred. In contrast, incompatible sur- geries remap synergy forces along a single dimension, and no adjustment of the synergy activation coefficients can reduce the force error in all directions. For this special class of perturbations, a second slower process may be responsible for changing the structure of the synergies to recover their capability of generating forces in all directions. Such a process may require exploring new muscle coordination patterns and acquiring new task-specific synergies. New synergies may be stored in the motor cortex and expressed through the corticospinal connectivity (Kargo and Nitz, 2003; Gentner and Classen, 2006; Rathelot and Strick, 2006; Reis et al., 2009; Gentner et al., 2010; Overduin et al., 2012). Synergy learning might be engaged only when the existing syner- gies are unable to perform a task, such as after a major change in the musculoskeletal system due to injury or when learning a new motor skill. ***
* The study by Nazarpour et al. (2012) tested the flexibility of the patterns of trial-by-trial cova- riation in the activity of an arbitrary pair of finger and wrist muscles around a single target level of activity, and not the flexibility of the muscle synergies underlying the modulation of a large number of elbow and shoulder muscles across multiple tar- get directions. While it is not clear whether the shaping of trial- by-trial covariation in repetitions of the same task and the modulation of muscle patterns across task conditions share the same mechanisms, the notion of flexible muscle synergies is in line with our idea of an adaptive process underlying synergy ex- ploration and reorganization after an incompatible virtual sur- gery. However, our results suggest that flexibility is present in a modular architecture both in the synergy combinations and in the synergy structure, yet it is expressed at different time scales.
* novel biologically inspired adaptive controllers for skilled robots.




Remapping Hand Movements in a Novel Geometrical Environment
Mosier et al. 2005


* ***The novel and arbitrary linear mapping used to transform glove signals into cursor locations allowed us to examine how the CNS learns to represent and control the redundant trans- formation from hand to cursor space, without the confounding effects of previously experienced movements. Other studies have proposed to resolve redundancy by decomposing move- ment variables into null-space and controlled variables, typi- cally through some form of the generalized inverse. For exam- ple, the concept of controlled and uncontrolled manifolds used by Scholz and Scho ̈ner (1999) is, in fact, an application of the generalized inverse. Generalized inverses have been familiar for a long time to robotic researchers investigating the control of kinematically redundant manipulators (Baillieul 1985; Baker and Wampler 1988; Burdick 1989; Klein and Huang 1983). They allow one to regularize the inversion of ill- conditioned linear maps by minimizing a quadratic form (Ben- Israel and Greville 1980). In particular, for an underconstrained linear transformation, the Moore–Penrose pseudoinverse finds a unique inverse map that satisfies the additional requirement of minimizing the (Euclidean) norm of the solution vector among infinite alternatives. It has been well established that this type of operation fails to produce repeatable (or, more technically, integrable) motions when applied in differential form to nonlinear kinematic transformations, as for example, in attempting to invert the transformation from joint angles to endpoint coordinates of a redundant arm (Klein and Huang 1983; Mussa-Ivaldi and Hogan 1991; Shamir and Yomdin 1988). This is a rather important issue that has often been overlooked in studies of biological motor control. However, this issue does not affect our investigation because we use a linear transformation from glove to screen coordinates. In our case, the pseudoinverse generates a family of regular inverse solutions. The map we use has the property of affine transfor- mations in that it maps straight lines into straight lines. Be- cause hand configurations and glove signals are related by a nonlinear isomorphism, rectilinear motions of the cursor on the monitor are not compatible with rectilinear motions in the space of finger-joint coordinates. However, the generation of well-behaved inverse maps from desired screen coordinates to finger configurations circumvents the challenge to derive a repeatable inverse map that would be associated with a non- linear map from glove signals to screen coordinates. The investigation of how more complex maps may be learned is deserving of a separate study.***
* The null space generated by our glove-cursor map had effectively 17 dimensions (19   2). We observed a marked tendency of subjects to reduce the amount of motion in this null space (Fig. 4). The selective reduction of null-space motion is particularly important because it may reveal how the Euclidean metric of the task space (the monitor) is effectively “imported” into the coordination of hand. The tendency to generate finger motions with smaller null-space components suggests that the movements tend to remain confined to subspaces that are minimum-norm images of the cursor space. This observation provides us with further evidence that the motor system is effectively capturing the metric structure of the controlled space and that it uses this metric as a basis to form coordinated motions of the fingers.
* Our data also show a strong and progressive decrease of movement variability from day to day along the entire motion. This is in sharp contrast with the hypothesis that, through practice, subjects learn to export increasing amounts of vari- ability into the null space to achieve a less-variable task execution. Because this hypothesis has supporting evidence in a variety of natural tasks (Balasubramaniam et al. 2000; Cole and Abbs 1986; Latash et al. 2001), it is possible our finding stems from the unusual nature of the task at hand. Under such novel conditions, the control system may be mostly concerned with formation of an internal model of the metric properties of task space— consistent with increasingly repeatable perfor- mance and trajectories.
* To the extent that the patterns of synergy and coupling that are present in natural tasks are preserved in a new mapping, one may expect to see that a reduction of variability in task coordinates would be mirrored by a similar reduction in null- space coordinates. (Because these two coordinates would be linked by the synergy, not just the task-relevant / irrelevant coordinates)
* By controlling the amount of dimensionality reduction, our paradigm allows us to explore by simple and noninvasive means the mecha- nisms by which feed-forward control of a highly redundant system is reorganized when presented with a novel coordinate transformation. An important difference between our experi- mental conditions and the operation of a BMI is the presence of proprioception of hand configuration for subjects engaged in our task. There is no such sensory input for the neural activities in a population of the cerebral cortex. Although proprioceptive information certainly facilitates the task of creating a new map, it may not be necessary for map formation because in both cases the neural controller must reorganize the natural pattern of commands and activities to cope with a novel geometrical environment.
* An unavoidable limit of this study stems from the use of only one particular type of hand-to-screen mapping. Under- standing in more general terms the impact of this mapping on motor learning and performance is an important goal for future studies.




Structured Variability of Muscle Activations Supports the Minimal Intervention Principle of Motor Control
Valero-Cuevas et al. 2009


* It is important to note that even when motor variability is convincingly shown to be structured, it can originate without any task-relevant control or it can be structured for a number of reasons. We now underscore several previously unaddressed confounds unrelated to task-relevant control. 1) Musculo-skel- etal coupling, especially in the tendons of the hand (Valero- Cuevas et al. 1998, 2007), can induce complex correlations on the behavioral level without correlated drive to individual muscles. We avoid this confound by recording muscle activity, as approximated by fine-wire EMGs. 2) Motor noise is known to be signal-dependent (Harris and Wolpert 1998; Sutton and Sykes 1967) and can therefore create structure in the variability that does not directly reflect the control law. For example, endpoint errors in reach are larger in the movement direction (Gordon et al. 1994) not because that direction is task-irrele- vant but because muscles pulling along the movement axis are more active and therefore more strongly affected by signal- dependent noise. Here we rule out such confounds by showing that a signal-dependent noise model does not capture the variability pattern in our experimental data. 3) The motor system may purposefully vary task-irrelevant aspects of the movement from trial to trial, so as to minimize fatigue or explore different control strategies. Such trial-to-trial variabil- ity can inflate measures of task-irrelevant variability without having any origins in the control strategy. This type of con- found is avoided here by analyzing the moment-to-moment fluctuations in motor output within a trial.
* Activating muscles maximally in isola- tion can be difficult for subjects given the complexity of the hand, and obtaining maximal EMG activity in each muscle does not necessitate eliminating EMG activity from other muscles.
* our hypothesis is expressed mathematically as testing whether the vari- ance in normalized muscle tension (as quantified Pn, Dn, Sn matrices) is preferentially channeled into the null space of the biomechanical transformation (i.e., the matrix An). See Valero-Cuevas (2009) and Strang (1980) for a review of these concepts. Briefly, if the variability of muscle activations is structured in such a way to reduce its effect on the relevant elements of the task (in this case, the magnitude of the three components of force), then the majority of the variability in normalized muscle tension is part of the family of motor commands that do not cause a change in the force normal to the surface (i.e., they belong to the nullspace of the biomechanical transformation An). The nullspace can be described intuitively as the task-irrelevant subspace: the set of all possible normalized muscle tension combinations that do not produce a fingertip force output.
* Our experiment has some limitations, which point to direc- tions for future work but do not challenge the validity of our results. First, the limited time window of opportunity, charac- teristic of experiments with fine-wire electrodes, prevented us from repeating the dynamic templates. This complicated the variance analysis in the time-varying phase. Second, subjects had to control the fingertip forces in all three directions accurately, and so the task-relevant 3D subspace was quite generic. This issue could be addressed in future work by rigidly fixing the fingertip to the target surface—making the fine control of tangential forces unnecessary, and thus creating a less generic 1D task-relevant subspace. However, investigating motor variability in unloaded finger movements and during object manipulation task would be stronger tests of whether this approach to understanding variability is useful in tasks of daily life. Third, in isometric tasks, it is difficult to separate state variables from control variables—a separation that is essential if feedback control analyses are to be applied (recall that a feedback control law is a mapping from states to controls). Movement tasks would be more suitable for such analyses.
* *** one might think that correlated drive to motor units of hand muscles (for a review of this extensive literature, see Schieber and Santello 2004) is a confound in this study. However, this is not so. Correlated drive is a mechanis- tic explanation of the same phenomenon we are trying to explain in computational terms. Every computational model must have an underlying neural mechanism. Indeed if the control laws used by the sensorimotor system were task- specific in the way we envision (Liu and Todorov 2007; Todorov 2004), their neural implementation would involve the kind of correlated drive that has been reported—with the caveat that the correlations would have to be task-specific. So these two explanations are complementary: one tells us what the control law is and why, the other tells us how that control law is implemented. ***
* given that all coefficients of the first principal component have the same sign (which to our knowledge has never been observed in previous studies), this first principal component may simply reflect overall modulation of fingertip force as well as stiffness. Or it could imply there was no dimensionality reduction because each of the seven principal components explains a nontrivial amount of variance.
* This finding can be reconciled with the existing literature by noting that there may be differences between open- and closed- loop control as well as between planning and execution. Previous studies, focusing on between-trial variability that is mostly driven by changes in task parameters, have emphasized planning and open-loop control. Even though these movements were executed under closed-loop control, averaging over mul- tiple trials in the same condition is likely to eliminate within- trial variability. In contrast, our analysis emphasizes variability within a trial, where the task conditions are kept constant and the only fluctuations are internally generated—presumably reflecting noise as well as closed-loop corrections. So it may be that planning and open-loop control rely on synergies while execution and closed-loop control do not. Of course it is also possible that our task is too simple, and the closed-loop controller is not as rich as it may be in other tasks where synergies might be revealed. However, to the extent that synergies are low-level mechanisms that are mostly task- independent, we should see evidence for them in every task.
* Both the open- and closed-loop point of view of synergies are in principle valid, and a more thorough comparison be- tween the two is likely to be illuminating. Because prior studies have almost exclusively emphasized the former approach, here we present some arguments in favor of the latter with the hope of stimulating a more balanced treatment in future work. In analyses of between-trial variability, it is difficult to dissociate the unavoidable consequences of task variation and musculo- skeletal structure from the intrinsic properties of the neural controller. For example, consider the EMG patterns during a center-out reaching task. Suppose for a moment that there is no inherent variability in the sensorimotor system and all variabil- ity is imposed by the task—meaning that reaches in different directions require different EMG patterns. Suppose also that the control strategy is such that small changes in target location correspond to small changes in EMG and the mapping between the two is smooth. Then the observed EMG patterns will lie on a 1D manifold embedded in the high-dimensional EMG space simply because the reach targets lie on a 1D manifold (i.e., a circle). An ideal and necessarily nonlinear dimensionality re- duction algorithm will be able to explain all EMG data in this hypothetical experiment with a single muscle synergy. Linear dimensionality reduction algorithms such as PCA are not ideal, so we should expect them to find a subspace with more than one dimension—but still it should be a very low-dimensional subspace. The same reasoning applies to tasks like locomotion, where the behavior is very complex but nevertheless remains close to a 1D limit cycle embedded in some high-dimensional space. The findings from such studies are useful in the sense that they tell us what the low-dimensional space is, but the fact that the space is low-dimensional is hardly surprising given the low-dimensionality inherent in the task. This confound is largely avoided in analyses of within-trial variability.






Structured Variability of Muscle Activations Supports the Minimal Intervention Principle of Motor Control
* 1D continuous tracking, 7D EMG recording 
* …it may be that planning and open-loop control rely on synergies while execution and closed-loop control do not. Of course it is also possible that our task is too simple, and the closed-loop controller is not as rich as it may be in other tasks where synergies might be revealed. However, to the extent that synergies are low-level mechanisms that are mostly task- independent, we should see evidence for them in every task.
* The motor system may purposefully vary task-irrelevant aspects of the movement from trial to trial, so as to minimize fatigue or explore different control strategies. Such trial-to-trial variability can inflate measures of task-irrelevant variability without having any origins in the control strategy. This type of con- found is avoided here by analyzing the moment-to-moment fluctuations in motor output within a trial.


Remapping Hand Movements in a Novel Geometrical Environment
* 19D → 2D cursor ballistic target movement 
* We will show that when subjects learn to control an overabundant set of hand signals in the presence of a novel transformation between these signals and the controlled endpoint, they become both more accurate in the task and more consistent in their finger and cursor motions. This finding is not consistent with the model of motor control proposing that the motor system increases variability in the redundant degrees of freedom to improve accuracy of the motor task.
* Other studies have proposed to resolve redundancy by decomposing move- ment variables into null-space and controlled variables, typically through some form of the generalized inverse. For exam- ple, the concept of controlled and uncontrolled manifolds used by Scholz and Scho ̈ner (1999) is, in fact, an application of the generalized inverse. Generalized inverses have been familiar for a long time to robotic researchers investigating the control of kinematically redundant manipulators (Baillieul 1985; Baker and Wampler 1988; Burdick 1989; Klein and Huang 1983).
* The investigation of how more complex maps may be learned is deserving of a separate study.
* By controlling the amount of dimensionality reduction, our paradigm allows us to explore by simple and noninvasive means the mecha- nisms by which feed-forward control of a highly redundant system is reorganized when presented with a novel coordinate transformation.
* An unavoidable limit of this study stems from the use of only one particular type of hand-to-screen mapping. Under- standing in more general terms the impact of this mapping on motor learning and performance is an important goal for future studies. This is a difficult problem because, even in the simple case presented here, the space of possible linear maps is spanned by 38 parameters. However, the same hand postures were used at different screen coordinates in the learning and generalization experiments and thus the resulting maps dif- fered. Nevertheless we observed similar learning trends in the two experiments; thus the learning of rectilinear movements is not contingent on one particular hand-to-screen mapping.


Exploiting the geometry of the solution space to reduce sensitivity to neuromotor noise (PloS 2018) 
* Evidently, subjects were unaware of the mapping from workspace to solution space and could only probe this mapping by trial and error. Further, each throw is likely to be executed open-loop as the movements are very fast. Note also that exploration across trials via following an error gradient in solution space can only be successful in neighborhoods close to the solution manifold. The solution spaces in the present conditions show a set of minima and discontinuities that would pose significant problems to simple gradient descent algorithms. 
* Task difficulty is  determined by how the arm trajectory can be oriented with respect to the solution manifold.


Meghan Huber’s PhD Thesis 2016
* Ball throwing —> Ball bouncing —> Ball on stick balancing
* Independent momentary control —> Non-independent momentary control —> Continuous control
* All three experimental paradigms involved interaction with an object and thereby exemplified different aspects of tool use, a fundamental human skill. They form a logical progression in the physics they involve: In skittles, the trajectory of the thrown ball is fully determined at the moment of release; there is no further interaction with the ball. Every trial is a new start, setting new initial conditions. In ball bouncing, subjects again contact the ball at a very brief moment that fully determines the subsequent ball trajectory. However, unlike in skittles, the successive ball contacts are not independent: the ball’s trajectory from the previous impact influences the next ball impact. Lastly, in the cup-and-coffee task, the force applied to the cup and the force exerted by the sloshing coffee onto the cup are in continuous and complex interplay. In this continuous dynamical system, every moment in human control matters. Due to this increasing complexity, the methods for analysis in the three paradigms need to be different. Nevertheless, even though the models are different and render different variables, all three experiments pursued one core hypothesis: Humans seek stable solutions where intrinsic noise matters less.
* Each experimental task was designed to allow an infinite number of solutions to a given task. Given these multiple options, it is necessary to have a model as reference to evaluate the observed variability within subjects across practice, but also across subjects. It is essential that the model described not only the physics of the task, but also how the subject interacted with the physics, i.e., how the subject executed the task to achieve a result. If the functional relationship between execution and result is known, the space of all solutions is known and the manifold of zero error solutions can be calculated. With this knowledge, not only can the practice-induced progression in performance be characterized, but individual differences can also be studied in a more principled way. For example, a person with high variability may prefer safer strategies, while a person with low intrinsic noise may prefer a more risky strategy. While this is a first start, more work is needed to better understand inter-individual differences(Cesqui, d’Avella, Portone, & Lacquaniti, 2012).
* Key Results 
1. Virtual tasks present an ideal and versatile platform for theoretically-grounded and fine-grained quantitative assessment of motor behavior during complex skill learning.
2. Strategies used to learn simple tasks are different than those used to learn complex tasks with redundancy due to the possibility of noise-tolerant solutions in complex tasks.
3. Guidance approaches for complex skills should be distinct from those used to enhance simple task learning due to differences in the solution space. Irrespective of the task, guidance methods should be designed to promote persistence of the learned behavior upon removal of the assistance.
4. Increasing motivation through verbal instruction has differential effects on task performance depending on the control strategy and the type of task.
* Rendering a real-world task in a virtual environment requires that the task first be mathematical modeled. Not only does the model allow for dynamic interaction with the virtual task, it also simplifies the real phenomenon by formalizing the assumptions and removing the irrelevant aspects present in the real-life task. As a result, more direct and informative measures of control and learning over practice can be extracted.
* Prior work of Sternad and colleagues has demonstrated support for the tenet that in complex tasks with redundancy, learners “seek solutions where their noise matters less”.
* ...humans are sensitive to the redundancy of a task and utilize different approaches for learning based on whether or not the redundancy offers “noise-tolerant” solutions.
* contrary to the results of (Kawai et al., 2015), human studies suggest that the motor cortex is needed for the retention of motor memories, whereas the cerebellum is required for learning (Galea et al., 2015; Galea, Vazquez, Pasricha, de Xivry, & Celnik, 2011).
* Moving forward, this thesis emphasized that more attention should be paid to complex skills, not only because they are relevant to everyday life, but also because tasks with high degrees of redundancy afford different learning strategies than tasks without redundancy.
* A next step for research on skills is to gain a better understanding how humans learn to interact with objects that have complex dynamics (Hasson, Shen, et al., 2012; Hasson & Sternad, 2014; Nasseroleslami, Hasson, & Sternad, 2014). Additionally, the influence of cognitive processes should be considered and quantified during skill learning, especially as task complexity increases (Lee et al., 1994). Again, virtual tasks provide a perfect platform for this type of research as they afford ecologically relevant and stimulating environments, while maintaining systematic control (Sveistrup, 2004). Furthermore, mathematical models and analyses of virtual tasks afford more fine-grained measures of behavior and control, as task success alone may not be enough to determine the effectiveness of an intervention.
* We advocated to study more complex tasks to understand the acquisition of novel skills, which is an essential and ubiquitous process that enables humans not only to perform extraordinary actions, such as skateboarding, but also to eat with knife and fork or drive a car. How the brain changes and stores such infinitely many new skills that essentially define our human existence remains one of the core open questions in human neuroscience.We proposed that the minimal ingredient for skill is redundancy, in particular extrinsic or task redundancy that allows individuals to make choices or even decisions about how they perform the task. This contrasts with much of the previous work in motor neuroscience that has tended to focus on simple and well-defined movements with a single goal. These experimental paradigms are well suited to study simpler forms of learning, including habituation and sensitization, classical and operant conditioning and motor adaptation. In order to extend the realm of scientific study and address more high- level skills, we developed a methodological approach that still afforded hypothesis-driven research.


Zach Danziger Thesis (2011) 
* Chapter 4: Trackball mouse → spherical projection ⇒ testing whether task space and articulation space geometries are related in learning, but seems unfinished. 
* Chapter 3 -- showing the user the kinematics of the articulated object encourages their exploitation of its geometry. Users with “complete vision” use geodesics of a linkage, but users with only a cursor move rectilinearly-- this could be a priors question as well. 
* Primarily, we must discover whether the motor system views BCIs as transformation series at all, or if they are handled as a single inverse function approximation problem from device feedback to system input.
* This study begins to consider the processes involved in learning a novel series of coordinate transformations, the likes of which appear during human interaction with sophisticated systems, such as brain‐computer interfaces (BCIs), myoelectric prosthetics, complex machinery or other human‐machine interfaces (HMIs). Human interaction with these systems often involves working in a previously unexplored state space and requires the user to develop a new series of coordinate transformations from the unfamiliar control signals to the device output by using visual feedback 57, 90, 91. While many HMIs have been recently developed with encouraging results 50, 68, 92‐94, few meet user’s expectations for ease of operation, and none are at present ready for long term use outside a laboratory setting 48, 95‐97. It is believed that “research on brain‐computer interfaces can be successful to the extent that we understand how sensory‐motor transformations are learned and encoded by the nervous system 98.” Primarily, we must discover whether the motor system views BCIs as transformation series at all, or if they are handled as a single inverse function approximation problem from device feedback to system input. [...] This result seems to be in agreement with modeling99 and empirical 100, 101 studies that have confirmed that subjects who have become proficient with unseen nonlinear transformations are not explicitly aware of the structure of the transformation. This further suggests that the motor system does not decompose the task into intermediate elements, but rather executes a single composite transformation.
* But they use SOMETHING about the visual structure of the task in their formation of trajectories, of outputs. 
* With this result comes the notion that, in any experiment where subjects are forced to learn a novel dimensionality reduction task or visuomotor transformation, suppressing all but the essential task feedback cannot be considered a default or standard procedure. Withholding non‐essential visual feedback is itself a choice made by the scientist, and carries with it a prejudice toward a particular motor learning strategy.
* Ultimately, for studies at the behavioral level, the interface between the task and the body is taken to be the articulation space.
CM Connections
Functional Organization of Information Flow in the Corticospinal Pathway (J. Neuroscience 2012) 
* Our results suggest that finger-related cortical commands are processed very little by spinal interneurons. Instead, finger-related information is transmitted to more ventral sites where motoneurons are situated, to activate a rather nonspecific set of upper limb muscles. This indicates that spinal activation during finger movement is probably induced either by a feedback response or as a result of the corecruitment of additional (non-finger related) cortical sites needed for stabilizing more proximal joints during finger tasks. Another implication of this finding is that the control of arm movements cannot be directly inferred from studies of finger-related motor tasks (Valero-Cuevas et al., 2009) because the difference in use of spinal circuitry in varying motor tasks may imply different control algorithms.


Corticomotoneuronal synaptic connections in normal man: An electrophysiological study (Brain, 1999)
* Contrary to the findings of Pierrot-Deseilligny and his colleagues, we were unable with the present method to demonstrate activation by cortical stimulation of oligosynaptic corticomotor neuronal pathways to low-threshold forearm SMUs (Gracies et al., 1991; Burke et al., 1994; Pauvert et al., 1998). Even with near-threshold stimuli, PSTH peaks remained narrow, without significant latency or duration shortening when increasing stimulus intensities. Also, the range and mean PSTH peak duration (see Table 1) were not significantly different in forearm and more distal or proximal muscles. This does not imply that such non-monosynaptic connections do not exist, but that they do not seem to play a major role in the corticospinal activation of low-threshold, early recruited motor neurons by descending inputs. However, with the present method, most motor units recruited during moderate and strong contraction cannot be studied, so that definitive conclusions cannot be drawn. 


Subdivisions of primary motor cortex based on cortico-motoneuronal cells (Rathelot, Strick PNAS 2008) 
* Retrograde trace from spinal, tricep, hand muscles leads to two sections of M1 
* Maps are intermingled, but all monosynaptic connections, proximal and distal, are in caudal M1. 
* 



Reviews 
Learning task-state representations (Yael Niv 2019 Nat Neuro)
* We argue that the brain solves seemingly complex tasks by learning efficient, low-dimensional representations that simplify these tasks. [...] That is, correctly ignoring irrelevant aspects of the environment will allow learning from one experience to inform decision-making in other scenarios that share relevant features with the current experience.
* In model-based RL, instead of learning values from experience, one uses experience to learn a model of the task: the transition probabilities between states and the probability of reward in each state. The internal model is then used in a mental simulation to calculate the expected long-term return from different action options and to choose the most rewarding one.
* The overwhelming majority of RL implementations, whether used to play backgammon or to model animal learning, assume a state space and are not concerned with learning it. A question then remains regarding how living agents know what to represent in order to use neural RL to solve these (and other) tasks.
* A useful state representation for RL can be derived from the true causal structure of the task: it should include all the environmen- tal features that determine (causally) whether actions will lead to (long-term) task-relevant outcomes (rewards and punishments), while any dimension or feature of the environment that is not causal to these outcomes can be ignored and generalized over. 
* while the environment typically provides feed- back for actions, there is no direct feedback for the representations underlying these actions, making it harder to determine whether our current state representation is suitable for the task at hand or can be further improved. Nevertheless, the brain seems to learn appropriate representations for new tasks almost effortlessly and in few trials. 
* Computationally, it is not known what statistics of the task (and our performance on it) convey that we are focusing on the wrong task dimensions.
* ...we do not yet know what constraints our brain has adapted to and been able to take advantage of: what are the statistics of natural tasks? Can the brain safely assume that, even in highly multidimensional environments, only a few dimensions are relevant to any given task? Presumably, decision-making systems evolved to be tailored to the set of tasks that we are routinely faced with. Similarly to the breakthroughs in understanding vision that followed the quantification of statistics of natural scenes, a clear description of the statistics of natural tasks might revolutionize our understanding of the neural basis of high-level learning and decision-making.
* Reinforcement learning—how feedback from the world, and par- ticularly unexpected feedback, is incorporated into future predic- tions—is fairly well understood in the brain. What is less clear is the fundamental process of representation learning: how we learn to carve streams of ongoing experience into task states that cor- rectly encompass all that is relevant to the task at hand in a minimal representation that generalizes learning as widely as possible. 
* A small prediction error will lead to little learning. A very large prediction error will lead to generation of a new state. Thus, to impact an old state with new information, the information must be unexpected, but not too much so.
* In sum, we suggest a dynamic interplay between RL in the basal ganglia, adaptive attention processes in the frontoparietal atten- tion control network and memory processes that reflect the learned structure of the environment and shape orbitofrontal state representations. In this framework, selective attention is not a limitation of the neural learning system, but an adaptive mechanism that allows rapid learning. Memory is similarly seen as an active process that does not simply mirror the external environment, but rather reflects inference regarding causal relationships in the environment.




Internal Models in Biological Control (McNamee&Wolpert 2019)
* Some behavioral signatures and neural correlates of the computational principles by which plans are formed have been identified, but this has occurred primarily in tasks containing relatively small state and action spaces, such as sequential decision- making and spatial navigation. By contrast, the processes by which biological control solutions spanning large and continuous state spaces are constructed remain relatively unexplored. Future investigations may need to embed rich dynamical interactions between object dynamics and task goals in novel and complex movements. Such task manipulations may generate new insights into motor planning since the planning process may then depend on significant cognitive input, and so may reveal a more integrative form of planning across the sensorimotor hierarchy.
* Connection to Henneman, size principle:
   * When small forces are generated, motor neurons that innervate a small number of muscle fibers are active. When larger forces are generated, additional motor neurons that innervate a larger number of muscle fibers are also active. This is known as Henneman’s size principle. Recruiting a larger number of muscle fibers from a single alpha motoneuron (the final neuronal output of the motor system) increases the variability of the output, leading to variability in the force that is proportional to the average force produced by that muscle (61, 62).
* Approximations to optimality 
* Predictability over chaos
* The main shortcoming of such model-free methods for learning optimal control policies is that they are prohibitively slow. When these methods are applied to naturalistic motor control tasks with high-dimensional, nonlinear, and continuous state spaces (corresponding to the roughly 600 muscles controlled by the nervous system), potentially combined with complex object manipula- tion, it becomes clear than human motor learning is unlikely to be based on these methods alone due to the time required to produce control policies with human-level performance. Furthermore, environment dynamics can transform unexpectedly, and the goals of an organism may change de- pending on a variety of factors. Taken together, all of this suggests that humans and animals must integrate alternative algorithms in order to flexibly and rapidly adapt their behavior.
* Use of primitives to simplify control 
* In tasks involving complex object interactions, it may be particularly important to internally simulate the impact of different control strategies on the environment dynamics in order to avoid catastrophic outcomes, as envisaged by Craik.
* Future Problems 
   *  it is unclear how a task specifies a cost function
   * although OFC can consider arbitrarily long (even infinite) horizons, people clearly plan their actions under finite-horizon assumptions by establishing a task-relevant temporal context. It is unclear how the brain temporally segments tasks and the extent to which each task is solved independently
   * The brain must use approximations to the optimal solution that are still unknown, although a variety of probabilistic machine learning methods (141) may provide inspiration for such investigations.
   * the processes by which biological control solutions spanning large and continuous state spaces are constructed remain relatively unexplored. Future investigations may need to embed rich dynamical interactions between object dynamics and task goals in novel and complex movements




Decision-Making in Sensorimotor Control
* Shaping, selection, revision, and sequencing of movements 
* Selection of a control policy 
* Brain may represent multiple movement plans
* There are delays in presentation of stimulus and accumulation of evidence
* Motor system influences how sensory information is related to decision variables 
* Most tasks use independent movements, not movements that are dependent
* Active sensing—considering the future movement
   * A lot of work on eye movements for this subfield 


Restoring sensorimotor function through intracortical interfaces: progress and looming challenges (Bensmaia 2014 NRN)
* Monkeys, and presumably humans, can thus learn new mappings between the activity of neurons and movement — a process that may be analogous to normal motor learning. Remarkably, these results indicate that some learning occurs even at the level of individual neurons during BMI control. Nonetheless, one might assume that a biomimetic decoder that closely approximates the normal mapping from brain to movement would yield faster learning and perhaps better ultimate performance than a non‑biomimetic mapping, but this remains an important question for future research.


Optimality principles in sensorimotor control (Todorov, 2004) 
* An important step toward understanding how this complex mosaic produces integrated action was Bernstein’s analysis104, translated in part only recently105. It suggested a four-level functional hierarchy for human motor con- trol: posture and muscle tone, muscle synergies, dealing with three- dimensional space, and organizing complex actions that pursue more abstract goals. It also suggested that any one behavior involves at least two levels of neural feedback control: a leading level that monitors progress and exploits the many different ways of achieving the goal, and a background level that provides automatisms and corrections without which the leading level could not function.
* Computational modeling that aims to capture the essence of feed- back control hierarchies—via optimization or otherwise—is still in its infancy. Anatomically specific models emphasize the distinction between spinal and supra-spinal processing and take into account our partial understanding of spinal circuitry; such models may prove very useful in elucidating spinal cord function, especially in lower species. Models that aim to explain complex behavior emphasize a functional hierarchy: the low level of neural feedback augments or transforms the dynamics of the musculo-skeletal system, so that the high level ‘sees’ a composite dynamical system that is easier to (learn how to) control optimally. One way to construct an appropriate low level is through unsupervised learning, which captures the statistical regularities present in the flow of motor commands and corresponding sensory data.
* Another approach is inspired by the minimal intervention principle: if we guess the task- relevant features that the optimal feedback controller will use in the context of a specific task, then we can design a low-level feedback controller that extracts those features, sends them to the high level, and maps the descending commands (which signal desired changes in the task features) into appropriate muscle activations32. When coupled with optimal feedback control on the high level, both of these approaches yield hierarchical controllers that are approxi- mately optimal—at a fraction of the computational effort required to optimize a non-hierarchical feedback controller.


Descending Pathways in Motor Control (Lemon, 2008) 
* Some reviewers have taken the view that the CM input is unimportant because its excita-tory input is rather small, rather like that of other monosynaptic inputs from other descend-ing pathways (Baldissera et al. 1981, Grillner& Wallen 2004). An informed answer to this question requires the following issues to be ad-dressed: (a) How extensive is the CM projec-tion? (b) How many CM cells project to a given motoneuron or to a given muscle? And (c) how large are the postsynaptic CM effects in a given motoneuron?
* The cortico-motoneuronal (CM) system provides the capacity for fractionation of move-ments and the control of small groups of muscles in a highly selective manner, an im-portant feature of skilled voluntary movements in the acquisition of new motor skills.The CM system may provide an efferent pathway that is accessed by the extensive motornetwork of the primate brain for development of adaptive motor programs.
* Even single CM cells can produce detectable changes in the discharge of both single motor units and mul-tiunit EMGs recorded from hand and forelimb muscles, and the total CM input to motoneu-rons could provide a significant proportion of the facilitatory drive needed to maintain its steady discharge (Cheney et al. 1991).