# Physiology of the Skilled Movement {#sec:physiology}

> *Even a simple movement is a global body event.*
>
> &mdash; Bizzi & Ajemian, *2020*

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

Muscle fibers are contained within muscle compartments, and each muscle may have one or more compartments. The fingers of the hand are extended by the extensor digitorum (ED) which contains four compartments, one for each of the tendons the muscle produces. Each tendon connects to the three joints of each digit. The fingers are flexed by two muscles, the flexor digitorum superficialis (FDS) and the flexor digitorum profundus (FDP). Like the ED, these muscles produce four tendons, one to each finger from each of their four compartments. Thus, one must coactivate these agonist and antagonist muscles in order to move only a single finger in isolation[@fuglevandMechanicalPropertiesNeural2011]. 

<!-- degrees of freedom stuff  -->

In total, the human hand, thumb, and forearm system contains more than 30 muscles and at least 20 degrees of freedom are theoretically able to be actuated. Nineteen of these muscles are intrinsic, having their origin and insertion points within the hand itself[@vanduinenConstraintsControlHuman2011]. Due to biomechanical coupling, the effective degrees of freedom is less 20, though an exact count is difficult due to the complexity of the anatomical structure of the hand's tendon network. One study showed that tendons of the fingers are arranged in such a way as to perform a kind of logical computation which expands the mechanical capabilities of the appendage by sharing force across its tendons[@Valero-Cuevas2007].

From our brief tour of the anatomy, we have seen how the motor system is highly distributed. We believe this structure exists in order to facilitate the adaptation and learning of new movements in a range of contexts. We don't take the fact that there are a small number of linear features of joint angles and velocities across behaviors to mean that humans are not capable of learning a wide range of motor outputs given the requisite feedback and training. The production of this variety lies in the motor system's ability to wield muscle coactivations, hardwired or not, as well as its ability to individuate movements in specific instances which require it.

For example, skilled piano performers have been found to exhibit a higher degree of independent movement among the fingers compared to control participants. Control groups displayed a hierarchical, presumably low-dimensional, organization of finger movement patterns, while pianists showed distinct but individuated movement patterns[@furuyaFlexibilityMovementOrganization2013] These results are imply that with skilled practice humans can produce finer and more independent movements of the fingers, and construct bespoke coactivations to solve specific goals. Similarly, studies have found that coherence between the index finger and thumb is greater on the dominant hand. Of course, this could imply a development lateralization, but use-dependent plasticity due to greater precision grip behavior of the dominant hand is a viable explanation[@fuglevandMechanicalPropertiesNeural2011].

<!-- These redundancies at the neurophysiological level play a role in "spillover", where contractions of one muscle or muscle compartment seem to spill over into neighboring muscles and muscle compartments. This is evident in the difficulty of moving single fingers individually. As mentioned previously, this may be a hardwired constraint or a byproduct of plasticity induced by behavioral requirements. -->

Overall, we are interested in investigating how the nervous system produces commands which excite 


## The Redundancy Problem

Nikolai Bernstein coined the phrase "the degrees-of-freedom problem" to describe the redundancy inherent in motor action stemming from a large number of degrees of freedom required coordination to achieve a goal [@Bernstein1967]. As we have seen, this redundancy exists at all scales of the motor system, from joints and muscles to motor units and their upstream synaptic partners. Rather than asking how the motor control system deals with this overwhelming complexity, we might instead ask why this complexity is evolutionarily advantageous to begin with. What does the availability of this redundancy afford the motor system? How does this redundancy enable dexterous movement?

A considerable amount of discussion has focused on the existence of synergies as a simplifying structure which allows the motor system to solve the redundancy problem. Motor synergy can be used as a descriptive term describing the spatiotemporal coactivation of muscles necessary for an ongoing task. It can also be used as a normative idea of neural control which implies a constraint in the dimensionality of the supraspinal controller, seen as an evolutionary means of simplifying the high-dimensional control task. 


Normative model of motor coordination

Many works promoting the concept of synergies as a hard-wired organizing feature of the motor system deal with low-dimensional movements mostly in non-primate and non-mammal preparations [@mussa-ivaldiMotorLearningCombination2000,@DAvella2003].

Studies have attempted to quantify the number of effective degrees of freedom of the hand with various methods. This has primarily been taken to be the number of linear features which contain a desired level of the original signal variance, where the signal is the joint angles of the hand engaged in various behaviors[@Ingram2009;TodorovDimensionality2005;@yanUnexpectedComplexityEveryday2020]. These methods have generally resulted in approximately 8 linear features of hand kinematics to solve a variety of tasks, with disagreements found in task and subject differences. The latter study argues that the motor repertoire required is hardly high-dimensional when compared to the dimensionality of the visual feature extraction system.

Overall, however, there is agreement in the literature that the effective number of degrees of freedom is markedly less than the theoretical maximum number. Whether this is due to hardwired upstream constraints or evidence of a motor control strategy remains debated.

<!-- Synergies, what are they, our definition and understanding --> 


While we do not deny the existence of synergistic muscle coactivation and constraints existent in the architecture of the hand and its control system, we believe that the concept of synergies is often attributed to the process of motor control as opposed to a straightforward structural constraint. 

Are synergies learned or are they hardwired? If they're hardwired, what physiological subsystem contains this hardwiring? We don't need to take a side because there is clear evidence that humans overcome synergies to adapt their motor outputs to solve novel tasks and overcome all types of changes in the motor loop (injury, fatigue, prism goggles, etc.) via well-studied (in laboratory tasks at least) adaptation mechanisms [Helmholtz, Wolpert, Todorov, newer work on synergy shifts such as [@DeRugy2012,Berger2013]. The more interesting questions ask on what timescales and by what mechanisms does learning occur, and can we reverse engineer paradigms and tasks that improve the learning rate.


In one study, "synergies" changed over the course of the experiment as subjects adapted to the novel perturbation. This is very promising. 

Our definition of synergy is simply a sequence of coordinated muscle activations. It has been shown that this arises spontaneously through an optimal feeback control system which contains redundancy.

Synergetic control implies control in the space of a low-dimensional set of synergy weights rather than independent control over the actuator dimensions themselves. The control dimensions are functionally coupled as a result of synergetic action, which both simplifies the control task and constrains behavior to the low-dimensional subspace defined by the synergy weights [@merelHierarchicalMotorControl2019a]. 



<!-- 
http://www.scholarpedia.org/article/Motor_coordination

Coordination is also achieved in a predictive, feed-forward manner. For example, to make a successful reaching movement, the muscular activity around the shoulder joint needs to be tightly coordinated with the muscular activity around the elbow joint to compensate for the interaction torques and to ensure a straight reaching trajectory. The term “synergy” is often introduced to explain coordination across different muscles. As a descriptive term, a synergy simply refers to the strong regularities in the spatiotemporal pattern of muscle commands, and the observation that large portions of the variance of recorded muscle activity can be described by a small number of linear components (d'Avella et al. 2006). As an explanatory term, a synergy refers to a neural controller that produces the correlated pattern of muscle activity. In the framework of Optimal Feedback Control, coordination in both feed-forward and feedback control is achieved by making the control policy of one effector dependent on an internal estimate of the state of another effector (Todorov et al. 2002, Diedrichsen et al. 2010). The difference between feed-forward or feedback control within this framework is gradual, and simply reflects the fact that the state estimate is informed by an internal prediction in the former, and actual sensory information in the latter case. 

-->


<!-- with CM connections, how synergies might they not be as rigid as we think when we're talking about the hand -->

<!-- The brain seems a thoroughfare for nerve-action passing on its way to the motor animal. It has been remarked that Life’s aim is an act, not a thought. Today the dictum must be modified to admit that, often, to refrain from an act is no less an act than to commit one, because inhibition is co-equally with excitation a nervous activity. (Sherrington, Rede Lecture, 1933) -->

Roger Porter and Roger Lemon's 1995 book *The Corticospinal Tract and Voluntary Movement* is a treasure trove of insights about the primate corticospinal tract. For our purposes, the key insight of the work is that "the organization of the spinal cord is based on relatively rigid muscular modes, and a mechanism to fractionate this is of particular importance for the muscles of the hands and digits which may need to be employed in a variety of flexible associations during voluntary movements." Monosynaptic corticospinal, or corticomotoneuronal (CM), connections offers the primate motor system a method of such fractionation, and careful anatomical work has shown how CM connections are well-developed in primates use tools requiring dexterity[@lemonStartingStoppingMovement2019]. This individuation is not one-to-one, and the hallmark of CM connections is their influence over multiple muscle compartments as well as multiple muscles, though typically agonist or antagonist sets[@cheneyFunctionalClassesPrimate1980]. Just as many fibers may be innervated by a single AMN, up to thousands of neurons contact single AMNs through corticomotoneuronal connections or a variety of spinal interneuron circuits. Experimental evidence in primates has show that the convergence of many CM collateral fibers onto AMNs driving the distal muscles in particular can produce a fine grading of activity over motor units driving the distal joints. Recent work has supported the idea that the corticomotoneuronal (CM) tract acts in coordination with synergistic muscle activations of the hand to achieve control that is balanced between modularity and flexibility. These findings suggest that there is a bipartite structure in human motor cortex driving dexterous control of the distal part of the upper limb which is due to evolutionary pressure to quickly generalize between tasks[@Rathelot2009; @Takei2017; @Yoshida2018; @griffinCorticomotoneuronalCellsAre2015]. 

CM connections are only present in the primate corticospinal tract. It appears that the rodent CST contains CM connections until they recede around P10[@kawasawaControlSpeciesdependentCorticomotoneuronal2017; @murabeHigherPrimatelikeDirect2018]

For our work, this is interesting as its physiological support that thre is something more to dexterous movement than the supraspinal activation of synergy weights, but a spectrum of movement from synergistic to individuated. 

There are very few tasks dealing with the hand in particular. What type of task would test the hypothesis that CM connections act to fractionate synergies of the hand such that we can tune a parameter of the task to require more or less influence of these direct connections? We would like to ask a user to fractionate synergies of the hand to different levels.

<!-- Individual corticomotoneurons contact multiple motor pools, and rarely (if ever) individual motor neurons. -->

It was found that even low-variance principle components displayed significantly higher correlation within condition (specific object grasp or specific ASL sign in this case) that across condition. This suggests that lower variance PCs carry more information than simply condition-independent, or task-irrelevant noise, but instead carry task-dependent signal. This might provide support for the idea that hand control, albeit biomechanically constrained, is controlled at a much higher dimensionality than 8. This would imply that the hand control algorithm is highly task-specific and relies on a hierarchical arrangement of control perhaps similar to what is seen in spatial navigation or sequential decision-making, for instance.


> It is generally believed that the direct corticomotoneuronal (CM) pathway, which is a phylogenetically newer pathway in higher primates, plays a critical role in the fractionation of muscle ac- tivity during dexterous hand movements. However, the present study demonstrated that PreM-INs, which are phylogenetically older, have spatiotemporal properties that correlate with muscle synergies during voluntary hand movements. Therefore, it is likely that these two systems have specialized functions for the control of primate hand movements, namely “fractionated control” and “synergistic control,” respectively. The interaction of these two putative control systems might be the source of the exceptional versatility of primate hand movements. [...] Optimization of balanced control may be an important factor also for the acquisition of new motor skills [@Takei2017].

The concept of a balanced control may prove to be a fruitful direction for modeling work. The goal would be to build a model which takes into account the bipartite structure of M1 into account, and find tasks that ostensibly require the direct descending connections to fractionate learned synergies. In effect, the hypothesis to test is that CM connections override the "consolidated" patterns putatively generated via spinal circuitry.


This notion of an "old" and "new" motor cortex is not conceptual, but has been shown using viral tracing techniques [@Rathelot2009].

There is work suggesting that CM connections synapse primarily on low threshold motor units that are recruited first. This would imply a difference in synergy fractionation at lower force as opposed to higher force. This can be tested by adding a force parameter within a task.




<!-- 
Spillover

>Spillover has been shown in experiments studying the ‘recruitment thresholds’ (defined below) of motor units ac ting on other digits during single digit contractions (Kilbreath & Gandevia, 1994; Butler et al. 2005; van Duinen et al. 2009). In these experiments, motor units were recorded from one (test) compartment of the respective muscles, while subjects were asked to contract the compartment of the other digits up to 50% of their maximal force. When the subjects contracted these other digits (one by one), motor units of the test compartment were often recruited. The amount of force produced by the other digits at the time of recruitment of the motor unit of the test compartment is termed the recruitment threshold. The general finding for all three muscles was that, the closer the contracting compartment to the test finger, the more motor units were recruited. [...] One has to ask whether this spillover is functional. Is the frequent recruitment of motor units ac ting on the little finger when we extend the thumb part of a fixed pattern of muscle activation, perhaps to balance forces around the wrist? (Duinen & Gandevia 2011) -->
<!-- 






















Two  mutually  non-exclusive  scenarios  can  be envisioned as to how corticospinal (and reticulospinal –see Baker, 2011, this issue) pathways might be organized to coordinate the activities of multiple muscles needed to perform finger movements (Schieber, 1990). In one,separate pathways operate on each of the requisite motor nuclei. In the other, selection of the muscles into functional groups is determined in part by the pattern of divergence of individual descending pathways across different motor nuclei in the spinal cord. This latter type of organization,while less flexible, might underlie the assemblage of muscles into synergistic groups that serve as the building blocks of the behavioural repertoire of an animal. In contrast to the extrinsic muscles of the dominant hand described above, virtually no short-term synchrony was observed across intrinsic muscles participating in the precision grip (McIsaac & Fuglevand, 2008). This result suggests that the descending pathways that control the activities of intrinsic muscles provide more concentrated input to individual motor nuclei than those pathways destined for motor nuclei innervating extrinsic hand muscles. The contrasting organizations of the descending pathways targeting extrinsic and intrinsic muscles seem in harmony with postulated functions of these two groups of muscles(Longet al.1970). Intrinsic muscles configure the digits to the unique dimensions of an object to be handled. HighlyFigure 5. Mean (SD) common input strength (CIS – index representing magnitude of short-term synchrony; Nordstrometal.1992) for pairs of motor units residing in the same compartment or adjacent compartments of three human multi-tendoned hand muscles, extensor digitorum (ED), flexor digitorum superficialis (FDS) and flexor digitorum profundus(FDP)Mean (SD) CIS values: ED same=0.70 (0.30), ED adjacent=0.41(0.18), FDS same=0.45 (0.30), FDS adjacent=0.27 (0.17), FDPsame=0.47 (0.19), FDP adjacent=0.36 (0.21). Values inside ofbars indicate number of motor unit pairs. Data compiled from:†Keen & Fuglevand (2004b); McIsaac & Fuglevand (2007); McIsaac& Fuglevand (unpublished data); Winges & Santello (2004).independent pathways, therefore, enable the fractionated actions of the digits needed for such a function. Extrinsic muscles provide the primary gripping forces during object manipulation. Because gripping necessitates the production of precisely counterbalanced forces between the thumb and one or more fingers, extrinsic muscles have their activities linked by divergent descending inputs. (Fuglevand 2011) -->



<!-- ## Bizzi Synergies, Supraspinal

Extracted Annotations (31/12/2020, 15:58:46)

"A major function of these synergies is to simplify the control of movements, a notoriously hard computational problem" (Bizzi and Ajemian 2020:1815)

"question of control" (Bizzi and Ajemian 2020:1815)

"the overarching" (Bizzi and Ajemian 2020:1815)

"how are these building blocks coordinated in time by the supraspinal system to generate goal-directed movements?" (Bizzi and Ajemian 2020:1815)

""we have some idea as to the intricate design of the puppet and the puppet strings, but we lack insight into the mind of the puppeteer" (Bizzi and Ajemian 2015)." (Bizzi and Ajemian 2020:1815)

"how are they influenced by motor skill learning" (Bizzi and Ajemian 2020:1816)

"far more speculative and difficult to find are detailed proposals as to how, even assuming the existence of synergies, the CNS manages to generate effective control signals, a problem we refer to as the problem of supraspinal pattern formation." (Bizzi and Ajemian 2020:1816)

"By "perspective of sensorimotor loops" the following is meant: 1) synergies likely constitute the fundamental building blocks for movement control, and their patterned recruitment is largely dictated by the cortical output regions that give rise to the corticospinal tract; 2) there exist multiple sensorimotor loops involving the cortex, other brain regions, the spinal cord, and the sensorimotor periphery, all of which include these cortical output regions along their path; 3) each of these loops serves distinct, yet crucially overlapping, functional roles in solving the supraspinal pattern formation problem; 4) the continuous convergence of these loop activities at the cortical output regions engenders the emergence of functionally appropriate movement commands by shaping both loop activity and motor output activity; and 5) the mathematical perspective from which to view this phenomenon is that of distributed representation and distributed control in a complex multiscale system (Kitano 2004)." (Bizzi and Ajemian 2020:1816)

"even a simple movement is a global body event." (Bizzi and Ajemian 2020:1816)

"two recent papers employing this type of approach provide evidence that preparatory activity is far from being an early indicator of movement-related activity and, instead, reflects a separate but facilitating computation. Elsayed et al. (2016) showed that at the population level preparatory and movement activity occupy orthogonal subspaces, although a simple transformation relates the two, suggesting that preparatory activity is crucial for putting the system in a state that enables the dynamic evolution of movement commands." (Bizzi and Ajemian 2020:1817)

"Although the dynamical systems approach has, in certain respects, been an improvement over the representational approach in understanding the role of preparatory activity, it too has shortcomings: dimensional reduction techniques make the relevant "variables" difficult to interpret and inconsistent from one study to the next; recording from dozens of neurons simultaneously is an improvement over recording from a single neuron but still falls orders of magnitude short of the number of neurons involved; and, in contrast to a feedback view of movement, the dynamical systems approach generally suggests that once a movement is prepared, motor cortical dynamics alone govern how movement dynamics unfold" (Bizzi and Ajemian 2020:1817)

"Kalaska 2019). Regarding this last point, a recent paper, Sauerbrei et al. (2020), suggests that a continuous flow of external inputs to the motor cortex is critical to making movements above and beyond intrinsic cortical dynamics." (Bizzi and Ajemian 2020:1817)

"The basal ganglia are involved in many cognitive-motor functions such as habit formation (Graybiel 2008) and the encoding and recoding of procedural memory (Barnes et al. 2005)." (Bizzi and Ajemian 2020:1817)

"Markowitz et al. (2018) and Wiltschko et al. (2015) used a confluence of machine learning techniques to detect a finite library of submovements represented in the" (Bizzi and Ajemian 2020:1817)

"basal ganglia of freely moving mice. These submovements embody recurring behavioral modules or motifs that exist at the subsecond timescale (350 ms), a scale sufficient to act as building blocks for volitional movements that occur on the scale of seconds. In essence, one can think of these modules as a kind of micro-pattern generators representing recognizable action segments." (Bizzi and Ajemian 2020:1818)

"Since muscle activity serves as the "ground truth" for the motor system's intended state, it is difficult to know whether the apparent kinematic chunking is likewise reflected in the composite muscle commands." (Bizzi and Ajemian 2020:1818)

"In a recent paper, muscle synergies were recorded from patients affected by cerebellar ataxia (Berger et al. 2020). The results indicated that, relative to a control group of healthy subjects, cerebellar damage disrupted in patients the temporal patterning by which synergies were recruited but left largely intact their underlying spatial structure. On the basis of these results, the authors speculate that the cortico-cerebellar loop is crucial to the temporal component of the supraspinal pattern formation problem, whereas the motor cortical areas are more likely involved with directly determining the spatial structure of synergies. This speculation is consistent with a long history of work implicating the cerebellum in timing problems (Ivry and Keele 1989)" (Bizzi and Ajemian 2020:1818)

"there has been a more recent focus on the dynamical systems approach, in which a group of recorded neurons dynamically interact to generate a functional spatiotemporal command (Shenoy et al. 2013)" (Bizzi and Ajemian 2020:1818)

"Aflalo and Graziano (2006) showed how external inputs form stereotypic and behaviorally relevant short trajectories of300- to 400-ms duration. This segmentation is somewhat reminiscent of that which Wiltschko et al. (2015) identified in the mouse putamen—that is, the presence of submovements at the subsecond timescale (350 ms) that were concatenated by cortico-striatal signals." (Bizzi and Ajemian 2020:1818)

"Stringer et al. (2019) and Musall et al. (2019) found that cognitive, sensory, and motor information were not confined to specifically designated cortical regions but were instead thoroughly intermixed across regions. As a consequence of combining multimodal information, diverse cortical patches of integrated activity were formed on the cortex and subcortex. These scattered sensorymotor patches may have a useful function because brain location might create a specific functional identity for these microcircuits to be utilized in sensory-motor coordination." (Bizzi and Ajemian 2020:1818)

"Neural activity in the putamen and cerebellum appears to follow the onset of neural activity in the cortical motor areas. This finding possibly suggests that the basal ganglia and cerebellum receive something akin to an efference copy from M1 and PMd." (Bizzi and Ajemian 2020:1819)

"During movements, the muscle synergies together with their muscle spindles and joint and skin receptors generate a flow of diverse sensory signals that, by way of multiple ascending pathways, provide M1 and PMd cells with the information necessary to adapt to the vagaries of the external world." (Bizzi and Ajemian 2020:1819)

"Muscle synergies are, presumably, neural coordinative structures that function to alleviate the computational burden associated with the control of movement and posture" (Bizzi and Ajemian 2020:1819)

"From an empirical standpoint, a factorization algorithm that takes as input all the recorded muscle EMG data is utilized to extract muscle synergies and activation coefficients. The factorization procedure essentially performs a dimensionality reduction by grouping muscles that tend to covary in the data set into synergies. (Fig. 1). In the last few years, many investigators have examined motor behaviors in humans (Ivanenko et al. 2004) and animals (Krouchev et al. 2006). The results show that combining a small set of muscle synergies appears to be a general strategy that the central nervous system utilizes for simplifying the control of movements" (Bizzi and Ajemian 2020:1819)

"At this point we do not have a mechanistic understanding as to how the supraspinal loops, possibly in conjunction with midbrain circuits, generate a series of commands that involve the selection of spinal synergies with their different timing and scaling factors." (Bizzi and Ajemian 2020:1820)

"The core question in motor control—what we call the problem of supraspinal pattern formation—is how the supraspinal system generates, across time, functional control signals." (Bizzi and Ajemian 2020:1821)

"Although pure feedforward control serves an important role in robotics, it has little place in biological motor control, where behavior arises more organically as a balancing act based on the continuous interplay between system inputs/outputs and behavioral predictions/realizations" (Bizzi and Ajemian 2020:1821)

"The sensorimotor loop perspective lends itself to a rigorous evaluation of robustness through computer simulation, since a concrete mathematical role must be proposed for each loop included in the model (e.g., the cerebellum embodies an expansion recoder perceptron that provides continuous adjustments to" (Bizzi and Ajemian 2020:1821)

"motor output based on the current inflow of system state (Albus 1971; Marr 1969" (Bizzi and Ajemian 2020:1821)

"given the presence of loops, there exists no single controlling authority but rather a highly distributed emergent control scheme about which we currently know little." (Bizzi and Ajemian 2020:1821)

"we have not dealt either with motor learning or motor generalization." (Bizzi and Ajemian 2020:1821)

"Nature needed millions of years to achieve the sublime level of performance of a tennis player or a gymnast, a level of adroitness that far surpasses state-of-the-art robotics capabilities." (Bizzi and Ajemian 2020:1821)

"Sauerbrei BA, Guo JZ, Cohen JD, Mischiati M, Guo W, Kabra M, Verma N, Mensh B, Branson K, Hantman AW. Cortical pattern generation during dexterous movement is input-driven. Nature" (Bizzi and Ajemian 2020:1823) -->













### Motor Maps

> We have some idea as to the intricate design of the puppet and the puppet strings, but we lack insight into the mind of the puppeteer. (Bizzi and Ajemian 2020)

How does the nervous system deal with new information during movement? How is this information used to update the ongoing plan?

If motor cortex relies on inputs to function, an input-driven dynamical system, motor cortex might be looked at like a 

<!-- In a standard stimulation experiment on motor cortex, the stimulation is applied in a brief burst for 50 ms or less. The result of this brief stimulation is a muscle twitch. But little if any behavior unfolds on such a short time scale. Neurons in motor cortex are not normally active in 50 ms bursts but instead, to a first approximation, are active throughout the duration of a movement. In the present case, the stimulation was applied for half a second, approximating the duration of a monkey’s reaching or grasping. As a result, instead of a muscle twitch, a complete movement unfolded.

the movement evoked by stimulation seemed to bring the hand toward the same final position as if in a goal-directed action.

The movement had nothing to do with the monkey’s behavioral context. It was as mechanical as clockwork. We appeared to have tapped into its control mechanism.

The behavioral repertoire of the animal seemed to be rendered onto the cortical sheet. One might say that the cortical motor system had an action map. The evoked movements were also roughly arranged across the cortex according to the location in space to which the movement was directed. The height of the hand was most clearly mapped across the cortical surface. Stimulation of the lower (ventral) regions of cortex commonly drove the hand into upper space, and stimulation of upper (dorsal) regions of cortex commonly drove the hand into lower space

A traditional view of the motor cortex is that it contains a map of the body. This map was famously depicted by Penfield, whose homunculus diagram is shown in Figure 1-3. This traditional topographic scheme, however, does not capture the actual pattern of overlaps, fractures, re-representations, and multiple areas separated by fuzzy borders. The homonculus does not adequately describe the topographic organization. A current view of the motor cortex is that it can be divided into many distinct areas with separate functions (Figure 1-4). Yet the functions are largely not known, and the properties described thus far tend to vary across cortex in a graded fashion without hard borders. Rather than a set of separate areas, the pattern resembles a statistical distribution with clustering. Labeling those clusters with acronyms, drawing borders around them, and assigning functions to them may provide a convenient description but does not explain the principles behind the organization.

Based on our stimulation results, we proposed an underlying topographic principle for the motor cortex: the reduction of the many-dimensional space of the animal’s movement repertoire onto the two-dimensional surface of the cortex. [...] The core of this theory of cortical organization is that local continuity is preserved as much as possible. Information processors that need to interact are arranged physically near each other in cortex, presumably gaining a connectional advantage.

we used a mathematical model that collapsed an approximate description of the monkey’s movement repertoire onto a two- dimensional sheet following the principle of maximizing local continuity (Aflalo and Graziano, 2006b; Graziano and Aflalo, 2007). -->

**A traditional view of the neuronal machinery of movement control is that activity at a site in motor cortex propagates down a fixed pathway through the spinal cord, activating a set of muscles. Based on our stimulation results, however, the underlying mechanism seems to be less of a simple feed-forward pathway and more of a network. The effect of the network is to create a specific class of mapping from the cortex to the muscles, a mapping that can change continuously on the basis of feedback about the state of the periphery. If the periphery is relatively still, the mapping from cortex to muscles appears fixed and resembles the traditional view. But once the state of the periphery is allowed to vary as in natural movement, the mapping from cortex to muscles becomes somewhat fluid in a manner that facilitates complex movement control.** (Graziano 2010)

<!-- Chapter 11 describes the proposal that the mechanism of movement control by the motor cortex can be understood as a feedback-remapping mechanism, a divergent mapping from neurons in cortex to muscles that is continuously remapped based on information about the changing state of the periphery.

the activity of a neuron in cortex might affect a set of muscles, activating some and inhibiting others (Cheney and Fetz, 1985)

the relationship between cortex and muscles [may be] more complex than a muscle map. Instead, the firing of a cortical neuron may carry instructions about useful control variables.

**A central proposal of this book is that different zones in motor cortex emphasize different modes of behavior that probably have different control requirements. It may be that one type of action, such as manipulation of objects, is more slanted toward muscle or joint control whereas another type of action, such as reaching toward objects, is more slanted toward control of spatial variables.**

**Fine control of the wrist and fingers may have evolved a specialized machinery. In primates that manipulate objects with a high degree of skill, the motor cortex projects directly to the spinal motoneurons that control the hand (Bortoff and Strick, 1993; Heffner and Masterton, 1975, 1983; Maier et al., 1997). The control of other body parts, such as the upper arm, involves mainly projections from the motor cortex to spinal interneurons. The direct cortical control of wrist muscles, implied by the Evarts result, therefore might not be directly applicable to other body parts.**

Kakei et al. (1999) found that if the arm is placed in different configurations, the mapping from cortical neurons to wrist muscles can change. A neuron that correlates with wrist extension, when the arm is in one orientation, may switch and correlate with wrist flexion when the arm is placed in another orientation. About half of the neurons in primary motor cortex showed some change in mapping to the wrist muscles caused by a change in arm configuration.

*I think feedback remapping is the idea of state-dependent feedback control where state includes all relevant sensors?*

In [the feedback remapping view], the mapping from cortex to muscles depends on a rich circuitry that includes the motor cortex, the spinal cord, and probably other structures. The state of this (p.73) circuitry can change depending on signals about the state of the periphery. If the feedback is constant, such as when the limb is maintained in a relatively fixed position, then the circuitry may remain more or less in one state and provide what appears to be a fixed mapping from cortical neurons to muscles. If the feedback from the periphery is changed, such as by putting the limb in a new configuration, then the circuitry is put into a different state and the apparent mapping from cortical neurons to muscles changes.

A study by Lemon et al. (1995) on the human motor cortex also suggested that the mapping from cortex to muscles can change depending on the state of the limb. In this study, the experimenters measured the connection strength between motor cortex and various muscles of the arm and hand. Their method was to activate the primary motor cortex with pulses of transcranial magnetic stimulation (a magnetic method of stimulating the brain through the skull) and to measure the evoked activity in limb muscles. A relatively larger amount of evoked activity indicated a stronger connection from cortex to muscles, and a relatively smaller amount of evoked activity indicated a weaker connection. At the same time, the participant performed a reaching and grasping task. The connection strength between motor cortex and the muscles changed markedly in different phases of the task, suggesting that the mapping from the cortex to the muscles was not fixed but instead was modulated continuously as the reaching task unfolded.

**Perhaps the central lesson in the research on descending pathways from cortex to muscles is that the term pathway is not quite the correct designation. Activity in motor cortex neurons is not merely transmitted downward to muscles along wires. Instead a rich network intervenes. This network is modulated by feedback from the periphery that influences the spinal and cortical circuitry. When the feedback is held more or less constant, then the circuitry is held in more or less one state, and each neuron in cortex appears to map through that circuitry to a fixed set of muscles. When the state of the periphery varies, the feedback modulates the circuitry, and therefore the mapping from each neuron in cortex through that circuitry to the muscles also changes. The caveat of feedback remapping is that it is not yet clear just how extensively feedback can alter the mapping from cortex to muscles. The experiments described above focused on feedback about static arm position and demonstrated some degree of change in the mapping from sites in cortex to muscles. How speed, tension, skin pressure, visual feedback from the arm, or other feedback signals might or might not alter the mapping from cortex to muscles remains untested. The usefulness of a feedback-dependent mapping from cortex to muscles is that it can in principle allow neurons in motor cortex to control a diversity of movement variables, such as direction, speed, hand position, or posture that transcend a fixed pattern of muscle activation. If the network receives feedback information about a specific movement variable, then it can learn to control that variable.**


**In the traditional view, the main cortical output is a single map of muscles in the primary motor cortex. That map represents individually meaningless movements that higher-order areas can combine into meaningful actions. In the modified scheme described here, many output zones exist, each one emphasizing a different meaningful action category. [...] The output zones are also not strictly on the same hierarchical level. For this reason they are depicted at different heights. Broadly speaking, they are part of the cortical output. Yet they emphasize movements with very different control requirements. It is likely that among the output zones are differences in complexity, in the level of abstraction of the information that is processed, (p. 52) and in the manner in which information flows laterally from one zone to another. For these reasons, it is probably not correct to think in terms of rigid hierarchies with absolute stages.**

Arguably nobody has done more to establish the organization of premotor cortex than Rizzolatti and colleagues. Most of their work has focused on the monkey motor cortex. They presented several lines of evidence to argue that the lateral premotor cortex exists as a separate motor area anterior to the primary motor cortex, and that it controls movement at a higher level of abstraction. They also proposed that the lateral premotor cortex is not a unitary area but is divisible into at least four subareas that participate in different though not fully understood aspects of movement control.

Strick and colleagues have gathered evidence that the lateral motor cortex contains at least three hand areas: one in traditional primary motor cortex, one in the ventral premotor cortex, and one in the dorsal premotor cortex, all three of which project to the spinal cord (Dum and Strick, 2005). Of the three hand areas, the most posterior one projects directly to the motor neurons in the spinal cord (Rathelot and Strick, 2006). The other two project mainly to interneurons in the spinal cord. This difference might be taken as evidence that the posterior area is more primary in its control of movement. A different explanation, however, may better account for the connectional pattern. The direct projection to the spinal motor neurons, bypassing the spinal interneurons, appears to relate to the control of dextrous manipulation of objects. Animals that are good at dextrous manipulation tend to have this direct projection, and animals that have poor manual dexterity lack the direct projection (Heffner and Masterton, 1975, 1983; see also Bortoff and Strick, 1993; Maier et al., 1997). The data suggest that the direct projection from cortex to spinal motor neurons is not an indication of a lower level in a hierarchy, but instead an indication of the control of a specific kind of action that requires a specific neuronal machinery. -->




<!-- 

### Muscle Spindles

Arm  movements  are  sensed  via  distributed  and  individually  ambiguous  activity  patterns  of  muscle  spindles,which depend on relative joint configurations rather than the absolute hand position.  Interpreting this high dimensional  input  (around  50  muscles  for  a  human  arm)  of  distributed information at the relevant behavioral level poses a challenging  decoding  problem  for  the  central  nervous  system. Proprioceptive information from the receptors undergoes several  processing  steps  before  reaching  somatosensory  cortex (3,8) - from the spindles that synapse in Clarke’s nucleus, to cuneate nucleus, thalamus (3,9), and finally to somatosensory cortex (S1).   In cortex,  a number of tuning properties have been observed, such as responsiveness to varied combinations of joints and muscle lengths (10,11), sensitivity to different loads and angles (12), and broad and unimodal tuning for movement direction during arm movements (11,13).The proprioceptive information in S1 is then hypothesized to serve as the basis of a wide variety of tasks, via its connections to motor cortex and higher somatosensory processing regions. (Sandbrink & Mathis, 2020) -->
