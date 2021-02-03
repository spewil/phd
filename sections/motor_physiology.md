# Physiology of the Skilled Movement{#sec:physiology}

> *Even a simple movement is a global body event.*
>
> &mdash; Bizzi & Ajemian, *2020*

The thesis of this section is that the motor system's organizing principle is redundancy at all levels, and that it's this redundancy that gives us flexibility. This flexibility is illustrated in the CNS's demonstrated hierarchy in both planning and execution of action.

<!-- - what can physiology tell us about the movement problem?
  - can it inform theory to describe motor solutions?
  - this will inform the shape our models
  - the constraints of our tasks, questions
  
- what do we know about brain and motor?
  - hands, thumbs, forearms anatomy
  - synergies, cm connections
    - bizzi
    - porter & lemon
    - from muscles to cortex
    - 
- loops and controllers
  - graziano
  - cerebellum
  - cortex, hantman
  - mouse, primate
  - basal ganglia -->

As our hope is to make progress engineering naturalistic artificial movement, it will be beneficial to review what is known about the biological movement system. Beginning with the architecture of the motor system and it's relation to dexterity will provide a scaffold on which we can hang our experimental and theoretical investigations. Specifically, we can use results from prior physiological investigations to ground our perspective on the computations relevant to skilled hand movements. The dexterous solutions produced by the human motor system rely on a incredibly complex architecture. Specifically, we believe that this system's spectrum of modularity and redundancy are crucial for this dexterity.

Here we are interested in illustrating in detail the computational burden the motor system faces when producing movement. In particular, we highlight the redundancies present at multiple levels in the motor system as well as the requirement to respond online to changing a environment during movement execution.

## Motor Units to Muscles

<!-- motor units to muscles, a spectrum of redundancy -->

<!-- build a picture of the staggering complexity of the hand's neuromuscular control structure -->

Muscles are composed of fibers which contract due to chemical gradients produced at the neuromuscular junction by action potentials emanating from alpha-motoneurons (AMN) in the ventral horn of the spinal cord. The quantum of motor output is the motor unit (MU), which is defined as a single motoneuron axon and the set of junctions its axon branches form with one or more muscle fibers. The innervation ratio of a particular muscle unit is the number of junctions it innervates. The number of MUs and their innervation ratios each range from tens to thousands per muscle. 

The motor unit provides the motor system with spatial redundancy at the muscle level: multiple muscle fibers contract due to a single AMN spike, and multiple AMNs may overlap in their innervations. The forces produced by motor units span several orders of magnitude, though most units produce very small forces. Here we find temporal redundancy: in order to produce movements motor units combine to generate a range of forces[@fuglevandMechanicalPropertiesNeural2011]. Since the innervation ratios of muscles in the forearm and hand are relatively small, the logarithmic recruitment and redundancy of motor units enables the hand to produce movements with very fine spatiotemporal resolution. Paradoxically, however, the well-known signal-dependent noise in models of motor output is higher for hand muscles than for more proximal muscles, likely due to small numbers of motor units compare to larger muscles[@fuglevandMechanicalPropertiesNeural2011;@harrisSignaldependentNoiseDetermines1998].

Muscle fibers are contained within muscle compartments, and each muscle may have one or more compartments. The fingers of the hand are extended by the extensor digitorum (ED) which contains four compartments, one for each of the tendons the muscle produces. Each tendon connects to the three joints of each digit. The fingers are flexed by two muscles, the flexor digitorum superficialis (FDS) and the flexor digitorum profundus (FDP). Like the ED, these muscles produce four tendons, one to each finger from each of their four compartments. Thus, one must coactivate these agonist and antagonist muscles in order to move only a single finger in isolation[@fuglevandMechanicalPropertiesNeural2011]. The excitatory and inhibitory role of these connection has been theorized for decades: "the activity of a neuron in cortex might affect a set of muscles, activating some and inhibiting others" [@cheneyFunctionalClassesPrimate1980].

<!-- degrees of freedom stuff  -->

In total, the human hand, thumb, and forearm system contains more than 30 muscles and at least 20 degrees of freedom are theoretically able to be actuated. Nineteen of these muscles are intrinsic, having their origin and insertion points within the hand itself[@vanduinenConstraintsControlHuman2011]. Due to biomechanical coupling, the effective degrees of freedom is less 20, though an exact count is difficult due to the complexity of the anatomical structure of the hand's tendon network. One study showed that tendons of the fingers are arranged in such a way as to perform a kind of logical computation which expands the mechanical capabilities of the appendage by sharing force across its tendons[@Valero-Cuevas2007].

From our brief tour of the anatomy, we have seen how the motor system is highly distributed. We believe this structure exists in order to facilitate the adaptation and learning of new movements in a range of contexts. We don't take the fact that there are a small number of linear features of joint angles and velocities across behaviors to mean that humans are not capable of learning a wide range of motor outputs given the requisite feedback and training. The production of this variety lies in the motor system's ability to wield muscle coactivations, hardwired or not, as well as its ability to individuate movements in specific instances which require it.

For example, skilled piano performers have been found to exhibit a higher degree of independent movement among the fingers compared to control participants. Control groups displayed a hierarchical, presumably low-dimensional, organization of finger movement patterns, while pianists showed distinct but individuated movement patterns[@furuyaFlexibilityMovementOrganization2013] These results are imply that with skilled practice humans can produce finer and more independent movements of the fingers, and construct bespoke coactivations to solve specific goals. Similarly, studies have found that coherence between the index finger and thumb is greater on the dominant hand. Of course, this could imply a development lateralization, but use-dependent plasticity due to greater precision grip behavior of the dominant hand is a viable explanation[@fuglevandMechanicalPropertiesNeural2011].

<!-- 

These redundancies at the neurophysiological level play a role in "spillover", where contractions of one muscle or muscle compartment seem to spill over into neighboring muscles and muscle compartments. This is evident in the difficulty of moving single fingers individually. As mentioned previously, this may be a hardwired constraint or a byproduct of plasticity induced by behavioral requirements. 

> Spillover has been shown in experiments studying the ‘recruitment thresholds’ (defined below) of motor units ac ting on other digits during single digit contractions (Kilbreath & Gandevia, 1994; Butler et al. 2005; van Duinen et al. 2009). In these experiments, motor units were recorded from one (test) compartment of the respective muscles, while subjects were asked to contract the compartment of the other digits up to 50% of their maximal force. When the subjects contracted these other digits (one by one), motor units of the test compartment were often recruited. The amount of force produced by the other digits at the time of recruitment of the motor unit of the test compartment is termed the recruitment threshold. The general finding for all three muscles was that, the closer the contracting compartment to the test finger, the more motor units were recruited. [...] One has to ask whether this spillover is functional. Is the frequent recruitment of motor units ac ting on the little finger when we extend the thumb part of a fixed pattern of muscle activation, perhaps to balance forces around the wrist? (Duinen & Gandevia 2011) 

-->

Overall, we are interested in investigating how the nervous system produces commands which excite 










## The Redundancy Problem

<!-- 
http://www.scholarpedia.org/article/Motor_coordination

Coordination is also achieved in a predictive, feed-forward manner. For example, to make a successful reaching movement, the muscular activity around the shoulder joint needs to be tightly coordinated with the muscular activity around the elbow joint to compensate for the interaction torques and to ensure a straight reaching trajectory. The term “synergy” is often introduced to explain coordination across different muscles. As a descriptive term, a synergy simply refers to the strong regularities in the spatiotemporal pattern of muscle commands, and the observation that large portions of the variance of recorded muscle activity can be described by a small number of linear components (d'Avella et al. 2006). As an explanatory term, a synergy refers to a neural controller that produces the correlated pattern of muscle activity. In the framework of Optimal Feedback Control, coordination in both feed-forward and feedback control is achieved by making the control policy of one effector dependent on an internal estimate of the state of another effector (Todorov et al. 2002, Diedrichsen et al. 2010). The difference between feed-forward or feedback control within this framework is gradual, and simply reflects the fact that the state estimate is informed by an internal prediction in the former, and actual sensory information in the latter case. 

-->


> *We have some idea as to the intricate design of the puppet and the puppet strings, but we lack insight into the mind of the puppeteer.*
>
> &mdash; Bizzi & Ajemian, *2020*

Nikolai Bernstein coined the phrase "the degrees-of-freedom problem" to describe the redundancy inherent in motor action stemming from a large number of degrees of freedom required coordination to achieve a goal [@Bernstein1967]. As we have seen, this redundancy exists at all scales of the motor system, from joints and muscles to motor units and their upstream synaptic partners. Rather than asking how the motor control system deals with this overwhelming complexity, we might instead ask why this complexity is evolutionarily advantageous to begin with. What does the availability of this redundancy afford the motor system? How does this redundancy enable dexterous movement?

A considerable amount of discussion has focused on the existence of synergies as a simplifying structure which allows the motor system to solve the redundancy problem. Motor synergy can be used as a descriptive term describing the spatiotemporal coactivation of muscles necessary for an ongoing task. It can also be used as a normative idea of neural control which implies a constraint in the dimensionality of the supraspinal controller, seen as an evolutionary means of simplifying the high-dimensional control task. 


Normative model of motor coordination

Many works promoting the concept of synergies as a hard-wired organizing feature of the motor system deal with low-dimensional movements mostly in non-primate and non-mammal preparations [@mussa-ivaldiMotorLearningCombination2000,@DAvella2003].

Studies have attempted to quantify the number of effective degrees of freedom of the hand with various methods. This has primarily been taken to be the number of linear features which contain a desired level of the original signal variance, where the signal is the joint angles of the hand engaged in various behaviors[@Ingram2009;@TodorovDimensionality2005;@yanUnexpectedComplexityEveryday2020]. These methods have generally resulted in approximately 8 linear features of hand kinematics to solve a variety of tasks, with disagreements found in task and subject differences. The latter study argues that the motor repertoire required is hardly high-dimensional when compared to the dimensionality of the visual feature extraction system.

Overall, however, there is agreement in the literature that the effective number of degrees of freedom is markedly less than the theoretical maximum number. Whether this is due to hardwired upstream constraints or evidence of a motor control strategy remains debated.



<!-- Synergies, what are they, our definition and understanding --> 


While we do not deny the existence of synergistic muscle coactivation and constraints existent in the architecture of the hand and its control system, we believe that the concept of synergies is often attributed to the process of motor control as opposed to a straightforward structural constraint. 

Are synergies learned or are they hardwired? If they're hardwired, what physiological subsystem contains this hardwiring? We don't need to take a side because there is clear evidence that humans overcome synergies to adapt their motor outputs to solve novel tasks and overcome all types of changes in the motor loop (injury, fatigue, prism goggles, etc.) via well-studied (in laboratory tasks at least) adaptation mechanisms [Helmholtz, Wolpert, Todorov, newer work on synergy shifts such as [@DeRugy2012,Berger2013]. The more interesting questions ask on what timescales and by what mechanisms does learning occur, and can we reverse engineer paradigms and tasks that improve the learning rate.

In one study, "synergies" changed over the course of the experiment as subjects adapted to the novel perturbation. This is very promising. 

Our definition of synergy is simply a sequence of coordinated muscle activations. It has been shown that this arises spontaneously through an optimal feeback control system which contains redundancy.

Synergetic control implies control in the space of a low-dimensional set of synergy weights rather than independent control over the actuator dimensions themselves. The control dimensions are functionally coupled as a result of synergetic action, which both simplifies the control task and constrains behavior to the low-dimensional subspace defined by the synergy weights [@merelHierarchicalMotorControl2019].


"the problem of supraspinal pattern formation" [@bizziMotorPlanningExecution2020] -- how the CNS produces control signals in a range of contexts and in response to continually changing task demands. 

there is never true feedforward control, in this sense. rather feedback control is modulated based on both internal predictions and incoming external data. cerebellum is thought of as a state prediction machine

rather than the CNS "choosing" synergetic action or "simplifying movement" through synergetic action, synergies fall out of a optimization strategy which trades off effort and accuracy. Effort, here, corresponds to independent control of individual control dimensions. 

Rather than corresponding to structures directly in the neural controller, we maintain that the structure of the neural controller is more complex for the hand, which most likely contains a spectrum of modularity in order to mainatain its role as a flexible instrument. synergetic action, then, is not the strategy per se, but rather the computation and structure of the human movement machine results in coordinative action as the obvious solution to a redundant system


If we limit ourselves to synergetic control, then we have simply passed the problem to a lower-dimensional one of the same fundamental nature, namely how synergies activations are activated in time by the supraspinal system to achieve task goals, what Bizzi and Ajemian refer to as a lack of "insight into the mind of the puppeteer"[@bizziMotorPlanningExecution2020].


there is a reason for this complexity, we believe it underlies dexterity and learning





<!-- with CM connections, how synergies might they not be as rigid as we think when we're talking about the hand -->



Roger Porter and Roger Lemon's 1995 book *The Corticospinal Tract and Voluntary Movement* is a treasure trove of insights about the primate corticospinal tract. For our purposes, 

Years of research has contributed to a more complex picture of hand function [@lemon1993;@lemon1997;@lemon2008]. The key insight of the work is that "the organization of the spinal cord is based on relatively rigid muscular modes, and a mechanism to fractionate this is of particular importance for the muscles of the hands and digits which may need to be employed in a variety of flexible associations during voluntary movements." Monosynaptic corticospinal, or corticomotoneuronal (CM), connections offers the primate motor system a method of such fractionation, and careful anatomical work has shown how CM connections are well-developed in primates use tools requiring dexterity[@lemonStartingStoppingMovement2019]. This individuation is not one-to-one, and the hallmark of CM connections is their influence over multiple muscle compartments as well as multiple muscles, though typically agonist or antagonist sets[@cheneyFunctionalClassesPrimate1980]. 

Just as many fibers may be innervated by a single AMN, up to thousands of neurons contact single AMNs through corticomotoneuronal connections or a variety of spinal interneuron circuits. Experimental evidence in primates has show that the convergence of many CM collateral fibers onto AMNs driving the distal muscles in particular can produce a fine grading of activity over motor units driving the distal joints. Recent work has supported the idea that the corticomotoneuronal (CM) tract acts in coordination with synergistic muscle activations of the hand to achieve control that is balanced between modularity and flexibility. These findings suggest that there is a bipartite structure in human motor cortex driving dexterous control of the distal part of the upper limb which is due to evolutionary pressure to quickly generalize between tasks[@Rathelot2009;@griffinCorticomotoneuronalCellsAre2015;@Takei2017].

Though there is evidence that this control isn't dichotomous, but a spectrum of overriding fractionation atop a vestigial system of synergistic action. motor dimensions much more complex than kinematics or dynamics

griffin finds that CM cells are functionally tuned to a muscle's mode of activity-- agonist, fixator, etc. “the direct access to motoneurons afforded by CM cells enables New M1 to bypass spinal cord mechanisms and sculpt novel patterns of motor output that are essential for highly skilled movements” [@griffinCorticomotoneuronalCellsAre2015]

CM connections are only present in the primate corticospinal tract. It appears that the rodent CST contains CM connections until they recede around P10[@kawasawa2017;@murabe2018]

For our work, this is interesting as its physiological support that there is something more to dexterous movement than the supraspinal activation of synergy weights, but a spectrum of movement from synergistic to individuated.

cells also play a role in the inhibition of antagonist muscles prior to contractions required for movement [@griffinMotorCortexUses2020]

The UCM is not a hard-and-fast principle, as nothing as in the motor system. Rather, as we've seen elsehwhere, there seems to be a spectrum of control. This could be explained through a composite cost function which penalizes deviations from prior movement strategies[@raczSpatiotemporalAnalysisReveals2013]. There is much research pushing back on optimal control, uncontrolled manifold hypothesis, and this will be addressed in {+@sec:experiment}.

There are very few tasks dealing with the hand in particular. What type of task would test the hypothesis that CM connections act to fractionate synergies of the hand such that we can tune a parameter of the task to require more or less influence of these direct connections? We would like to ask a user to fractionate synergies of the hand to different levels.

<!-- Individual corticomotoneurons contact multiple motor pools, and rarely (if ever) individual motor neurons. -->

It was found that even low-variance principle components displayed significantly higher correlation within condition (specific object grasp or specific ASL sign in this case) that across condition. This suggests that lower variance PCs carry more information than simply condition-independent, or task-irrelevant noise, but instead carry task-dependent signal. This might provide support for the idea that hand control, albeit biomechanically constrained, is controlled at a much higher dimensionality than 8. This would imply that the hand control algorithm is highly task-specific and relies on a hierarchical arrangement of control perhaps similar to what is seen in spatial navigation or sequential decision-making, for instance.


> It is generally believed that the direct corticomotoneuronal (CM) pathway, which is a phylogenetically newer pathway in higher primates, plays a critical role in the fractionation of muscle ac- tivity during dexterous hand movements. However, the present study demonstrated that PreM-INs, which are phylogenetically older, have spatiotemporal properties that correlate with muscle synergies during voluntary hand movements. Therefore, it is likely that these two systems have specialized functions for the control of primate hand movements, namely “fractionated control” and “synergistic control,” respectively. The interaction of these two putative control systems might be the source of the exceptional versatility of primate hand movements. [...] Optimization of balanced control may be an important factor also for the acquisition of new motor skills [@Takei2017].

The concept of a balanced control may prove to be a fruitful direction for modeling work. The goal would be to build a model which takes into account the bipartite structure of M1 into account, and find tasks that ostensibly require the direct descending connections to fractionate learned synergies. In effect, the hypothesis to test is that CM connections override the "consolidated" patterns putatively generated via spinal circuitry.


This notion of an "old" and "new" motor cortex is not conceptual, but has been shown using viral tracing techniques [@Rathelot2009].

There is work suggesting that CM connections synapse primarily on low threshold motor units that are recruited first. This would imply a difference in synergy fractionation at lower force as opposed to higher force. This can be tested by adding a force parameter within a task.

The take-home here is that the primate motor system has evolved specifically for a special kind of dexterous movement, and this should be theorized in order to develop dexterous movement algorithms

<!-- primate motor system is very different!! -->

















### Motor Maps

if synergies aren't the whole story with the hand, then how might we think about the neural controller? it isn't simply setting the gains of a few synergy modules, it's controlling flexibly...


feedback view of movement -- M1 is not an isolated movement-generating dynamical system, but a node in the network of a feedback-modulated, distributed movement machine. This is reflected in work in the rodent which suggests that task-relevant movement depends on these network connections [@sauerbreiCorticalPatternGeneration2019].

inputs to M1 include all types of sensory information as well

all of this information means the neural controller is continuously modulating itself

By studying patients with cerebellar ataxia, a recent study suggests that the cerebellum plays a role in the temporal recruitment of behavioral syllables, while motor cortex may be implicated in the spatial structure of synergetic action, though this study focused on 13 proximal muscles of the shoulder and arm [@bergerDoesCerebellumShape2020].





inputs to M1 produce stereotyped movements in primates similar to the concept of behavioral syllables [@grazianoORGANIZATIONBEHAVIORALREPERTOIRE2006;@wiltschkoMappingSubSecondStructure2015]


> We have some idea as to the intricate design of the puppet and the puppet strings, but we lack insight into the mind of the puppeteer. [@bizziMotorPlanningExecution2020]

How does the nervous system deal with new information during movement? How is this information used to update the ongoing plan?

If motor cortex relies on inputs to function, an input-driven dynamical system, motor cortex might be looked at like a field of feedback microcircuits, integrating and transforming external inputs to sculpt ongoing movement

Graziano found that with stimulations of 500ms, a behaviorally relevant timescale, entire movements reliably unfolded which were functional and stereotyped. They appeared to produce goal-oriented actions pulled out of other contexts such as bringing food to the mouth. Graziano refers to this as the cortical "action map", that these stimulations tapped into the control mechanisms of the primate's motor system. The movements seemed to be arrange topographic not as a homonculus, but in terms of spatial endpoints. 

the organization of cortex reflects a topographical arrangement of behaviorally relevant movements

**A traditional view of the neuronal machinery of movement control is that activity at a site in motor cortex propagates down a fixed pathway through the spinal cord, activating a set of muscles. Based on our stimulation results, however, the underlying mechanism seems to be less of a simple feed-forward pathway and more of a network. The effect of the network is to create a specific class of mapping from the cortex to the muscles, a mapping that can change continuously on the basis of feedback about the state of the periphery. If the periphery is relatively still, the mapping from cortex to muscles appears fixed and resembles the traditional view. But once the state of the periphery is allowed to vary as in natural movement, the mapping from cortex to muscles becomes somewhat fluid in a manner that facilitates complex movement control.** [@grazianoIntelligentMovementMachine2009]

cortex as a feedback-remapping mechanism that uses ongoing information to transform descending output to the muscles. The idea of feedback remapping is the idea of state-dependent feedback control where state includes all relevant sensors, with varying degrees of synergistic action

the variables of interest in this view, rather than being fixed in a particular coordinate system, depend on the context, goals, and perturbations of the intended movement

for control of the hand, the variables of interest may include muscle-level dimensions, or perhaps even submuscular control signals at the level of motor units for very fine control. 

the relationship between cortex and muscles [may be] more complex than a muscle map. Instead, the firing of a cortical neuron may carry instructions about useful control variables.

posture or musculoskeletal configuration may alter the feedback remapping by producing varying inputs to the neural control system

"The usefulness of a feedback-dependent mapping from cortex to muscles is that it can in principle allow neurons in motor cortex to control a diversity of movement variables, such as direction, speed, hand position, or posture that transcend a fixed pattern of muscle activation. If the network receives feedback information about a specific movement variable, then it can learn to control that variable."

muscle activity is a readout from a network not controlling movement per se, but transforming state-dependent inputs into movement

rather than playing chords, the motor system is improvising

the motor system wields its complexity to construct a movement fit to purpose, to suit its context and the information it recieves. rather than choosing muscle patterns in reconfigurable blocks, it creatively sculpts movements 

the hierarchy is also not rigid, but information flows between levels of the hierarchy as well, and each level of the hierarchy receives similar inputs

<!-- **A central proposal of this book is that different zones in motor cortex emphasize different modes of behavior that probably have different control requirements. It may be that one type of action, such as manipulation of objects, is more slanted toward muscle or joint control whereas another type of action, such as reaching toward objects, is more slanted toward control of spatial variables.** -->

<!-- **Fine control of the wrist and fingers may have evolved a specialized machinery. In primates that manipulate objects with a high degree of skill, the motor cortex projects directly to the spinal motoneurons that control the hand (Bortoff and Strick, 1993; Heffner and Masterton, 1975, 1983; Maier et al., 1997). The control of other body parts, such as the upper arm, involves mainly projections from the motor cortex to spinal interneurons.** -->


direct connection in motor cortex which projects to alpha-motoneurons is for specific movement types, not the lowest level of the hierarchy, the other two subdivisions proejct to interneurons and are thus suited to recruit groups of muscles in function movements [@dumCorticospinalSystemStructural2011]

"there exist multiple sensorimotor loops involving the cortex, other brain regions, the spinal cord, and the sensorimotor periphery, all of which include these cortical output regions along their path; 3) each of these loops serves distinct, yet crucially overlapping, functional roles in solving the supraspinal pattern formation problem" (Bizzi)

Preparatory states for movements seem to set the system at the initial state for subsequent execution which allows the appropriate dynamics to unfold complete with information from the periphery and connected spinal and supraspinal systems such as cerebellum and premotor cortex. 

The idea here is not that movement primitives constitute a modular set of behavioral outputs, played like keys on a keyboard. Instead, we suggest that primitives are themselves input-driven dynamical systems modulated by context (goal, environment, sensation). While this does not neg

Reasoning in the space of feedback control systems, or feedback control trajectories. Rather than reasoning moment-to-moment, the neuromotor control system might reason with respect to feedback dynamics. The phenomenal thing about the system is that it is able to tune itself rapidly with both high-dimensional sensory inputs and sparse reward signals[@bahlNeuralDynamicPoliciesfor2020;@ijspeertDynamicalMovementPrimitives2013]. This has some precendence in the literature and will be discussed further in {+@sec:theory}.

"reconciling the frameworks of kinematic MPs and kinetic/synergy MPs into a unified compositional scheme remains difficult" [@giszterMotorPrimitivesNew2015]

"Strong predictions of an MP framework are that the underlying neural circuitry should involve interneurons assembling the synergies and driving them as units."

"it is unknown whether these interneuron projections to motor pools occur in specific patterns that cluster into discrete sets, as happens in the frog."

"reimagine muscle synergies as reflecting the statistics of the external world (that includes the peripheral level) that might provide useful behaviors based on regularities"
[@brutonSynergiesCoordinationComprehensive2018]

predictions about synergetic primitives remain predictions, and the evidence accumulated here suggests that the situation is much more complex for control of the hand and wrist

Cerebellar loops provide information about predicted sensory states
Basal Ganglia loops provide information about the value of particular movement variables 

<!-- 

### Muscle Spindles

Arm  movements  are  sensed  via  distributed  and  individually  ambiguous  activity  patterns  of  muscle  spindles,which depend on relative joint configurations rather than the absolute hand position.  Interpreting this high dimensional  input  (around  50  muscles  for  a  human  arm)  of  distributed information at the relevant behavioral level poses a challenging  decoding  problem  for  the  central  nervous  system. Proprioceptive information from the receptors undergoes several  processing  steps  before  reaching  somatosensory  cortex (3,8) - from the spindles that synapse in Clarke’s nucleus, to cuneate nucleus, thalamus (3,9), and finally to somatosensory cortex (S1).   In cortex,  a number of tuning properties have been observed, such as responsiveness to varied combinations of joints and muscle lengths (10,11), sensitivity to different loads and angles (12), and broad and unimodal tuning for movement direction during arm movements (11,13).The proprioceptive information in S1 is then hypothesized to serve as the basis of a wide variety of tasks, via its connections to motor cortex and higher somatosensory processing regions. (Sandbrink & Mathis, 2020) -->
