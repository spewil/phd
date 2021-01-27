# Physiology of the Motor System {#sec:physiology}

- what can physiology tell us about the movement problem?
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
  - basal ganglia

If we wish to make progress engineering naturalistic artificial movement, it will be beneficial to review what is known about the biological movement system. Beginning with the architecture of the motor system and it's relation to dexterity will provide a scaffold on which we can hang our experimental and theoretical investigations. Specifically, we can use results from prior physiological investigations to ground our perspective on the computations relevant to skilled hand movements. The dexterous solutions produced by the human motor system rely on a incredibly complex architecture. Specifically, we believe that this system's spectrum of modularity paired with its redundancy in the space of feedback controllers are crucial for its dexterity.





## Basic Anatomy of the Hand, Thumb, and Forearm

Muscles are composed of fibers which contract due to chemical gradients produced at the neuromuscular junction by action potentials emanating from alpha-motoneurons (AMN) in the ventral horn of the spinal cord. The atom of motor output is the motor unit, which is defined as a single motoneuron axon and all of the junctions it makes with one or more muscle fibers. There is thus a potential redundancy already at this level: it is possible for multiple muscle fibers to contract due to a single AMN. Fibers are contained within muscle compartments, and each muscle may have one or more compartments. The fingers of the hand are extended by the extensor digitorum (ED) which contains four compartments, one for each of the tendons it produces. Each tendon connects to the three joints of each digit. The fingers  

The human hand, thumb, and forearm contains more than 30 muscles and at least 20 degrees of freedom. Nineteen of these muscles are intrinsic, their origin and insertion points contained within the hand itself[@vanduinenConstraintsControlHuman2011]. Due to biomechanical coupling, the effective degrees of freedom is less 20, though an exact count is difficult due to individual variability. Studies have attempted to quantify the number of effective degrees of freedom of the hand with various methods.

The movements of each digit rely on 






The human thumb confers great scope for dexterity and its long length relative to the index gives it the highest ‘opposability index’ among primates (Napier, 1972), while its rotated first metacarpal and unique carpometacarpal joint enhance its range of movement for grasping and manipulation (Wood-Jones, 1949). Furthermore, the thumb is moved by a muscle in the forearm, ﬂexor pollicis longus (FPL), which provides the only way to ﬂex its distal joint and is rudimentary in apes. (Hiske van Duinen and Simon C. Gandevia 2011)

The presence of FPL in humans is associated with a high capacity to s ense thumb voluntary forces at remarkably low levels compared even to intrinsic hand muscles (muscles with their origin and insertion in the hand; Kilbreath & Gandevia, 1993) and to detect length changes at its distal joint (Refshauge et al. 1998). (Hiske van Duinen and Simon C. Gandevia 2011)

the deep flexor attaches to the distal phalanx
the superficial flexor attaches to the middle phalanx

The main finger extensor, extensor digitorum (ED), when active generates torque about the elbow, wrist, metacarpalphalanegeal, proximal interphalangeal and distal interphalangeal joints simultaneously (Anet  al.1981). Moreover, ED, likeits flexor counterparts, flexor digitorum superficialis and flexor digitorum profundus, gives rise to four distal tendons that insert into each of the fingers.Therefore, attempts to move a single finger in isolation require that other muscles be co-activated to counteract the unwanted  actions produced by the agonist (Schieber, 1995; Valero-Cuevas, 2000). (Fuglevand 2011)

Three major forearm muscles consist of multiple muscle bellies with tendons to each finger so that the muscles have four ‘compartments’ (Duinen & Gandevia 2011)

Force and displacement interactions can occur within muscles, an issue of particular concern given that ﬂexor digitorum profundus (FDP), ﬂexor digitorum superficialis (FDS) and extensor digitorum (ED) are muscles with tendons to each of the fingers. These interactions may occur, for example, because a motor unit’s territory is such that force is ‘injected’ into more than one distal tendon. This sort of ‘lateral’ force transmission exerted by individual muscle fibres and motor units can be significant in some animal preparations (e.g. Street, 1983; see also Young et al. 2000). The topic of lateral force transmission is controversial but it appears that such an effect can even result in inter-muscle force transfer (e.g. for review Patel & Lieber, 1997; Huijing, 1999, 2009). This process has been most studied in the lower limb for gastrocnemius and soleus in animals (for details see Maas & Sandercock, 2008) but some evidence exists for it in humans (e.g. Bojsen-Moller et al. 2010). However, the unresolved issues are the magnitude of these effects and the conditions under which they are functionally significant. (Duinen & Gandevia 2011)

If hand muscles do not always behave as simple in-line motors, then the spread of their mechanical effects must depend on the links of force–length curve, viscoelastic properties, and the changes induced by muscle contractions. Such detailed biomechanical information is largely lacking. (Duinen & Gandevia 2011)

Spillover has been shown in experiments studying the ‘recruitment thresholds’ (defined below) of motor units ac ting on other digits during single digit contractions (Kilbreath & Gandevia, 1994; Butler et al. 2005; van Duinen et al. 2009). In these experiments, motor units were recorded from one (test) compartment of the respective muscles, while subjects were asked to contract the compartment of the other digits up to 50% of their maximal force. When the subjects contracted these other digits (one by one), motor units of the test compartment were often recruited. The amount of force produced by the other digits at the time of recruitment of the motor unit of the test compartment is termed the recruitment threshold. The general finding for all three muscles was that, the closer the contracting compartment to the test finger, the more motor units were recruited. (Duinen & Gandevia 2011)

One has to ask whether this spillover is functional. Is the frequent recruitment of motor units ac ting on the little finger when we extend the thumb part of a fixed pattern of muscle activation, perhaps to balance forces around the wrist? (Duinen & Gandevia 2011)

Until recently, most studies looked at either flexion or extension, but when we compare the amount of enslavement in flexion and extension, the enslaved forces in extension are higher than in flexion, when recorded in the same apparatus. We hypothesise that the level of enslavement might depend on the amount of individual daily usage (for data on usage see Ingram et al. 2008). (Duinen & Gandevia 2011)

When multiple digits had to contract, the subjects were not able to reach their maximal force, thus showing a force ‘deﬁcit’. These deﬁcits may be comparable to those when trying to produce force with two hands or arms, a phenomenon known as the bilateral deﬁcit (Gandevia, 2001).


The intrinsic hand muscles can also be activated almost maximally (e.g. Merton, 1954; Herbert & Gandevia, 1996), but they are special in that they can be ‘controlled’ at very low levels, even below the recruitment threshold for the earliest recruited units (Gandevia & Rothwell, 1987). (Duinen & Gandevia 2011)


## Functional Anatomy of Hand Control

What's interesting here is that the hand isn't controlled simply by synergetic action, it's unique in this regard

### Motor Units

> The motor unit, namely a motoneurone and the many muscle fibres singularly innervated by branches of the motoneurone’s axon, is the quantal element underlying the transduction of neural commands driving the exquisite motor behaviours produced by the hand. (Fuglevand 2011)

Experimental work characterizing motor unit properties in humans and other mammals has been consistent with regard to two findings(see Fuglevandet al.1993). First, twitch or tetanic forces of motor units that constitute a muscle vary over an extremely wide range, usually 100-fold or greater. And second, the frequency distribution of motor units according to force capacity is markedly skewed toward motor units that produce small forces, with few units that generate large forces. (Fuglevand 2011)

One consequence of this organization is that fine resolution of force is an in-built control feature, such that when performing delicate motor tasks involving weak muscle contractions, subtle adjustments in force can be accomplished by drawing upon a large population of weak motor units. (*this is logarthmic in the number of units recruited*) (Fuglevand 2011)

**Motor unit number itself seems to play a critical role in determining precision of muscle force. When human subjects attempt to produce a constant force during isometric contractions, the force inadvertently fluctuates about the specified target level. Such force variability increases in roughly in proportion to the target force(Enoka et  al.2003). Unexpectedly, this noise in force control is greater for hand muscles compared to more proximal muscles (Hamilton et al.2004). Furthermore,based on available estimates of motor unit numbers and computer simulation, a key factor underlying greater noisiness in hand muscles was relatively low numbers of motor units (Jones et al.2002; Hamilton et al.2004). In addition, augmented force variability in hand muscles maybe related to greater variability and common modulation in motor unit discharge rate compared to more proximal muscles (Negro et al.2009). Therefore, the widely held view that hand muscles are optimally designed for fine control may require reconsideration.** (Fuglevand 2011)

While there are anatomical (Feinsteinet  al.1955) and electrophysiological (McComaset  al.1971; Bromberg,2007) means to estimate motor unit numbers in humans,both methods are susceptible to several sources of error.Perhaps the most reliable information at present available about relative numbers of motor units supplying different muscles comes from retrograde labelling of motoneurones in non-human primates. In such studies, intrinsic hand muscles have been shown to be innervated by approximately 50–200 motoneurones, while more proximal muscles like biceps and triceps brachii are each supplied by more than 1000 motoneurones (Jenny & Inukai, 1983). (Fuglevand 2011)


### Porter & Lemon

It is clear that humans have the capacity to learn single motor unit (SMU) activation of the digits. Given what we know about voluntary movement and human digit control it is likely that this activation is under motor cortical control. This ability is somewhat surprising for two reasons:

1. Individual corticomotoneurons contact multiple motor pools, and rarely (if ever) individual motor neurons.
2. There is no physiological reason for the nervous system to have the ability to control individual muscles. The CNS (motor cortex in particular) is more likely to generate “complex” movements requiring simultaneous control of multiple synergistic muscle groups.

Given the fact that most CM cells appear to facilitate activity in several muscles, inhibition would appear to be essential for the recruitment of an individual muscle without any concurrent activity in its functional or anatomical synergists. But how is this inhibition recruited and maintained during and after learning?

I see two opportunities with this project. The first is practical: if we can generate definitive experimental evidence and a working theory for what is involved in voluntary control of single MUs in the forearm, we can build a ground-truth dataset for spike waveforms of various muscles under various conditions. The second is experimental: we can manipulate pertinent types of sensory feedback with the goal of answering interesting questions about the interplay between proprioception, agonist-antagonist interaction, and Renshaw cell functionality while building an understanding of how dynamics can be shifted for voluntary action to reverse engineer a learning process from the cellular level.

I’ve written below a little more background and detail on what I am thinking about, and would welcome your feedback and critique.

insights from studying the corticospinal tract

The brain seems a thoroughfare for nerve-action passing on its way to the motor animal. It has been remarked that Life’s aim is an act, not a thought. Today the dictum must be modified to admit that, often, to refrain from an act is no less an act than to commit one, because inhibition is co-equally with excitation a nervous activity. (Sherrington, Rede Lecture, 1933)

Since we’re working with a voluntary movement ostensibly of the digits, we know that we’re going to be dealing with the corticospinal tract. I discovered a book called The Corticospinal Tract and Voluntary Movement by Porter and Lemon (1995) – it’s awesome. I highly recommend it, especially Chapter 4. The book focuses mainly on the hand, and Roger Lemon seems to be a living legend.

The key insights from P&L:

The spinal cord’s neuronal organization is based on relatively rigid muscular synergies, and a mechanism to fractionate this is of particular importance for the muscles of the hands and digits which may need to be employed in a variety of flexible associations during voluntary movements.

[Obviously] the structure of corticospinal connectivity places a constraint on the number of possible output arrangements that can be employed by the cortex...

We can conclude that the fundamental organizing principle of the cortico-motoneuronal output is one of influence over activity in multiple muscles.

[Fetz 1980] found that 67 percent of their corticomotoneuronal cells contacted more than 2 of the 5–6 different muscles sampled, and that the mean number of muscles facilitated per cortico-motoneuronal cell was 2.4. [...] The majority of CM neurones (59 per cent) produced pure facilitation of either an agonist or antagonist, and cofacilitation of both was extremely rare. The second most common pattern (30 percent of CM cells) was facilitation of agonists and postspike suppression of antagonists.

Findings suggest that CM cell axons branch to innervate many (if not all) motor units within the motor nucleus of its target muscle.

The widespread synaptic impacts made within the motor nucleus of a single muscle would allow a single CM cell to exert a facilitatory influence over many different motoneurones, and therefore to contribute to motoneuronal activity over a range of EMG and force levels. A similar distributed system of synaptic connections has also been observed for muscle spindle afferents (Mendell and Hennemann 1971).

There are a large number of possible sources of common input to spinal motoneurones, including segmental afferent inputs from muscle spindles and other peripheral receptors. However, several lines of evidence suggest that, at least for hand muscle motoneurones, much of the short-term synchrony has a corticospinal origin.

Both refined histological and electro-anatomical observations on single corticomotoneuronal fibres in the monkey indicate significant divergence of the intraspinal collaterals of these fibres to impact on a large number of motoneurones. It is possible that, for some muscles acting about the distal joints of the limb, most or all of the motoneurones are engaged by synapses from each cortico-motoneuronal fibre which includes that muscle within its muscle field. The synaptic boutons that generate the cortico-motoneuronal synapses are small in size and only one or a few boutons are contributed to the motoneuron’s dendritic surface by each cortico-motoneuronal collateral. The contribution to the synaptic excitation of a motoneurone that is made by any one cortico- motoneuronal fibre is small. However, because of the high degree of convergence of intraspinal collaterals from a large colony of cortico-motoneuronal neurones on to each motoneurone of a distally acting muscle, this synaptic influence could allow fine grading of the depolarization of the motoneurone, contribute to the selective activation of motor units during voluntary movement and be critically effective in the fractionation of muscle usage during different motor tasks.

other literature (work on the extensor digitorum communis)

Things we still don’t fully know (that are probably beyond the scope of this project):

1. How extensive is the CM projection?
2. How many CM cells project to a given motoneuron or to a given muscle?
3. how large are the postsynaptic CM effects in a given motoneuron? [Lemon 2008]

Renshaw cells might play a role in isolating single MUs:

It is concluded that Renshaw cells de-correlate discharge patterns of different motoneurones of the same pool by injecting uncorrelated signals into them. This decorrelation is an important prerequisite for distortion suppression of signal transmission in a multi-channel system, like that of stretch reflex, and for its linearization. [Adam 1978]

Another report that people don’t know how they’re learning to isolate SMUs:

Although subjects used auditory synchrony feedback, they were generally unable to evaluate their success in modulating the amount of MU synchrony; nor could they describe any conscious strategy used during the successful sessions. They concentrated on the

occurrence of the synchrony pulses, rather than on the amount of EDC contraction or the concurrent force output. [Schmeid, 1993]

Implications that CM cells are responsible for fast changes in MU dynamics:

The present changes in short-term synchronization were detected in the course of the conditioning session and must reflect rapid alterations in the relative contributions of common inputs. One direct mechanism would involve a change in the proportion of descending monosynaptic input, such as the corticomotoneuronal cells that strongly affect EDC motoneurons (Phillips and Porter 1977; Fetz and Cheney 1980). [Schmeid, 1993]

Statement of unknowns about how dynamics are shifted at the MU level in terms of spinal circuitry:

Indirect control of MU synchronization might also be mediated by supraspinal modulation of the Renshaw decorrelating action (Gelfand et al. 1963; Adam et al. 1978), or by enhanced activity of spindle afferents via selective activation of gamma-motoneurons (Rudomin 1989). These possibilities suggest further experiments to resolve the neural mechanisms by which humans could rapidly alter short-term synchrony of MUs and, by implication, control the proportion of last-order common inputs to motoneurons. [Schmeid, 1993]





### Muscle Spindles

Arm  movements  are  sensed  via  distributed  and  individually  ambiguous  activity  patterns  of  muscle  spindles,which depend on relative joint configurations rather than the absolute hand position.  Interpreting this high dimensional  input  (around  50  muscles  for  a  human  arm)  of  distributed information at the relevant behavioral level poses a challenging  decoding  problem  for  the  central  nervous  system. Proprioceptive information from the receptors undergoes several  processing  steps  before  reaching  somatosensory  cortex (3,8) - from the spindles that synapse in Clarke’s nucleus, to cuneate nucleus, thalamus (3,9), and finally to somatosensory cortex (S1).   In cortex,  a number of tuning properties have been observed, such as responsiveness to varied combinations of joints and muscle lengths (10,11), sensitivity to different loads and angles (12), and broad and unimodal tuning for movement direction during arm movements (11,13).The proprioceptive information in S1 is then hypothesized to serve as the basis of a wide variety of tasks, via its connections to motor cortex and higher somatosensory processing regions. (Sandbrink & Mathis, 2020)



## Supraspinal Architecture of Hand Control







### Graziano motor maps

In a standard stimulation experiment on motor cortex, the stimulation is applied in a brief burst for 50 ms or less. The result of this brief stimulation is a muscle twitch. But little if any behavior unfolds on such a short time scale. Neurons in motor cortex are not normally active in 50 ms bursts but instead, to a first approximation, are active throughout the duration of a movement. In the present case, the stimulation was applied for half a second, approximating the duration of a monkey’s reaching or grasping. As a result, instead of a muscle twitch, a complete movement unfolded.

the movement evoked by stimulation seemed to bring the hand toward the same final position as if in a goal-directed action.

The movement had nothing to do with the monkey’s behavioral context. It was as mechanical as clockwork. We appeared to have tapped into its control mechanism.

The behavioral repertoire of the animal seemed to be rendered onto the cortical sheet. One might say that the cortical motor system had an action map. The evoked movements were also roughly arranged across the cortex according to the location in space to which the movement was directed. The height of the hand was most clearly mapped across the cortical surface. Stimulation of the lower (ventral) regions of cortex commonly drove the hand into upper space, and stimulation of upper (dorsal) regions of cortex commonly drove the hand into lower space

A traditional view of the motor cortex is that it contains a map of the body. This map was famously depicted by Penfield, whose homunculus diagram is shown in Figure 1-3. This traditional topographic scheme, however, does not capture the actual pattern of overlaps, fractures, re-representations, and multiple areas separated by fuzzy borders. The homonculus does not adequately describe the topographic organization. A current view of the motor cortex is that it can be divided into many distinct areas with separate functions (Figure 1-4). Yet the functions are largely not known, and the properties described thus far tend to vary across cortex in a graded fashion without hard borders. Rather than a set of separate areas, the pattern resembles a statistical distribution with clustering. Labeling those clusters with acronyms, drawing borders around them, and assigning functions to them may provide a convenient description but does not explain the principles behind the organization.

Based on our stimulation results, we proposed an underlying topographic principle for the motor cortex: the reduction of the many-dimensional space of the animal’s movement repertoire onto the two-dimensional surface of the cortex. [...] The core of this theory of cortical organization is that local continuity is preserved as much as possible. Information processors that need to interact are arranged physically near each other in cortex, presumably gaining a connectional advantage.

we used a mathematical model that collapsed an approximate description of the monkey’s movement repertoire onto a two- dimensional sheet following the principle of maximizing local continuity (Aflalo and Graziano, 2006b; Graziano and Aflalo, 2007).

**A traditional view of the neuronal machinery of movement control is that activity at a site in motor cortex propagates down a fixed pathway through the spinal cord, activating a set of muscles. Based on our stimulation results, however, the underlying mechanism seems to be less of a simple feed-forward pathway and more of a network. The effect of the network is to create a specific class of mapping from the cortex to the muscles, a mapping that can change continuously on the basis of feedback about the state of the periphery. If the periphery is relatively still, the mapping from cortex to muscles appears fixed and resembles the traditional view. But once the state of the periphery is allowed to vary as in natural movement, the mapping from cortex to muscles becomes somewhat fluid in a manner that facilitates complex movement control.**

Chapter 11 describes the proposal that the mechanism of movement control by the motor cortex can be understood as a feedback-remapping mechanism, a divergent mapping from neurons in cortex to muscles that is continuously remapped based on information about the changing state of the periphery.

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

Strick and colleagues have gathered evidence that the lateral motor cortex contains at least three hand areas: one in traditional primary motor cortex, one in the ventral premotor cortex, and one in the dorsal premotor cortex, all three of which project to the spinal cord (Dum and Strick, 2005). Of the three hand areas, the most posterior one projects directly to the motor neurons in the spinal cord (Rathelot and Strick, 2006). The other two project mainly to interneurons in the spinal cord. This difference might be taken as evidence that the posterior area is more primary in its control of movement. A different explanation, however, may better account for the connectional pattern. The direct projection to the spinal motor neurons, bypassing the spinal interneurons, appears to relate to the control of dextrous manipulation of objects. Animals that are good at dextrous manipulation tend to have this direct projection, and animals that have poor manual dexterity lack the direct projection (Heffner and Masterton, 1975, 1983; see also Bortoff and Strick, 1993; Maier et al., 1997). The data suggest that the direct projection from cortex to spinal motor neurons is not an indication of a lower level in a hierarchy, but instead an indication of the control of a specific kind of action that requires a specific neuronal machinery.


### Corticomotoneuronal Connections

CM connections thus afford us a greater degree of flexibility in our movements by providing a means of fractionation. One example of this fractionation is the movements of skilled piano players. These performers have been found to exhibit a higher degree of indepenent movement among the fingers compared to control participants. Control groups displayed a hierarchical organization of finger movement patterns, while pianists showed distinct but individuated movement patterns[@furuyaFlexibilityMovementOrganization2013]. Studies of the dynamics of piano performance find complex patterns of coarticulation among the fingers and thumb which produce hand posture adjustments in anticipation of future actions[@furuyaFlexibilityMovementOrganization2013]. These results are informative that with extensive skilled practice humans can produce finer and more independent movements of the fingers. In everyday life, these movements are not immediately advantageous. However, they are not unachievable with practice.






Recent work has shown that monosynaptic cortical projections controlling the digits, the corticomotoneuronal (CM) tract, act in coordination with synergistic muscle activations of the hand to achieve control that is balanced between modularity and flexibility. These findings suggest that this bipartite structure in human motor cortex driving dexterous control of the distal part of the upper limb is due to evolutionary pressure to quickly generalize between tasks.

Jean-Alban Rathelot and Peter L. Strick. Subdivisions of primary motor cortex based on cortico-motoneuronal cells. Proceedings of the National Academy of Sciences, 106(3):918– 923, 2009.

Tomohiko Takei, Joachim Confais, Saeka Tomatsu, Tomomichi Oya, and Kazuhiko Seki. Neural basis for hand muscle synergies in the primate spinal cord. Proceedings of the National Academy of Sciences, 114(32):8643–8648, 2017.

Yutaka Yoshida and Tadashi Isa. Neural and genetic basis of dexterous hand movements. Current Opinion in Neurobiology, 52:25–32, 2018.


* Subdivisions of primary motor cortex based on cortico-motoneuronal cells (Rathelot, Strick PNAS 2008)
https://www.pnas.org/content/106/3/918

x Corticomotoneuronal cells are “functionally tuned”
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4829105/

Although CM synapses exert powerful excitatory effectson alpha-motoneurons, the same motoneurons also receivemany other inputs (Fuglevand, 2011), including thosefrom Ia afferents, spinal interneurons, propriospinalneurons, reticulospinal neurons and rubrospinal neurons(Mewes & Cheney, 1991; Flamentet al.1992; Porter& Lemon, 1993; Perlmutteret al.1998; Riddleet al.2009). Any individual alpha-motoneuron receives thousandsofsynapticcontacts.Thehandfulofsynapticcontactsfroma given CM cell therefore does not consistently drive thedischarge of any particularalpha-motoneuron. (Schieber 2011)

rathelot, strick?

- "Following a century of detailed anatomical tract-tracing, electrophysiological investigation and careful lesion studies, our knowledge of the executive pathways through which ‘commands’ for movement must pass is unrivalled, yet we are still some way from really understanding how a movement is generated, which structures and pathways are involved and how they interact during the period leading up to movement onset."

- The intense, synchronised output generated by electrical stimulation of macaque motor cortex evokes responses in hand and digit muscles with onset latencies of only approximately 10ms. These latencies are much shorter than the 60–100 ms between the onset of changes in M1 activity and the onset of muscle activity during voluntarily generated movements (Cheney and Fetz, 1980; Porter and Lemon, 1993).

- The discovery that M1 neurons can become active during observation of the actions of others, but without any overt signs of movement in the observer (Vigneswaran et al., 2013) adds to a long list of evidence that motor cortex can be active in a number of different states, all of which are quite distinct from movement itself (Schieber, 2011). These include preparation for movement (Shenoy et al., 2013), mental rehearsal and imagination (Cisek and Kalaska, 2004; Dushanova and Donoghue, 2010; Macuga and Frey, 2012).

- PTNs exhibit additional features that are consistent with a role as ‘command’ neurons. These include the fact that they make many collaterals to important subcortical motor structures, such as the red nucleus and the pontine nuclei (Ugolini and Kuypers, 1986), thereby providing ‘efference copy’ of ‘commands’ to the cerebellum.

- A further feature of some primate PTNs is that they make direct cortico-motoneuronal (CM) connections to alpha motoneurons (Porter and Lemon, 1993; Rathelot and Strick, 2006; Zinger et al., 2013), allowing the motor cortex direct access to spinal motoneurons. Of course, the CM system does not act alone, but in parallel with many other local interneuronal mechanisms and other descending pathways (Baker, 2011; Lemon, 2008), seg- mental (Takei and Seki, 2010) and propriospinal systems (Kinoshita et al., 2012). It is interesting that CM synapses on motoneurons are not subject to presynaptic inhibition (Jackson et al., 2006), suggesting that other systems (e.g. peripheral affer- ent inputs from the moving limb) do not use this mechanism to modify CM inputs to motoneurons, which would mean that information delivered by CM projections is allowed unfettered influence over target motoneurons.

- CM cells show changes in activity long before movement onset, far longer than the esti- mated conduction delays: thus CM cells exert their influence long before movement starts, but at a level that is subthreshold for motoneuron activation and subsequent movement.

- __CM cells are active for a whole range of different limb move- ments, including reach-to-grasp, precision grip and during tool- use by macaques (McKiernan et al., 1998; Muir and Lemon, 1983; Quallo et al., 2012). CM connections are particularly well- developed in primates with a high level of dexterity and who use tools. Interestingly, CM cells are characterised by showing not only increases, but also decreases in activity before and during precision movements (Maier et al., 1993; Quallo et al., 2012). Indeed, one way that M1 appears to control the pattern of muscle activity during grasp is to ‘disfacilitate’ the excitatory drive to motoneurons.__ (Lemon Kraskov 2019)

- The primate corticospinal tract shows many interesting features that distinguish it rather sharply from the rodent pathway. These include the size and dis- tribution of fibres within the tract, with a small but probably very significant population of fast-conducting axons (Firmin et al., 2014).

### Synergies

### Muscular and Postural Synergies of the Human Hand (Weiss & Flanders 2004)

> Single motor units receive a variety of motor commands, and the net result may be that neighboring units in the same muscle are preferentially recruited to produce forces in different directions 3D space or to hold the hand in different static postures. The corollary to this is that a given force or posture involves a collection of units that spans many muscles.

The motor system is distributed in order to solve the redundancy problem as well as to learn new control schemes.

### Analysis of the synergies underlying complex hand manipulation (Todorov & Ghahramani 2005)

> Remarkably, the dimensionality in the individuated joint task was 8.7, or only 2 higher. The latter task is designed to reveal the maximal number of degrees of freedom humans have access to. Why this number is not 20 is unclear; the most likely reason is biomechanical coupling, although limitations in neural control may also play a role. Furthermore, the number 8.7 intuitively seems too low suggesting that such counting methods may underestimate the true dimensionality.

### The statistics of natural hand movements (Ingram & Wolpert 2008)


### Neural Basis of Muscle Synergies, Bizzi Cheung 2013

Note that there are a great number of tasks, and the case for synergies in the motor system cannot be answered simply. Here we are concerned with motions of the hand because we know that this is the endpoint of CM connections. There are many fewer tasks dealing with this system in particular. Most tasks deal with arm reaching, though the most highly cited synergy paper deals with a 1DOF kick [@DAvella2003].


A considerable amount of research has focused on  the existence of synergies as a simplifying structure in the motor system. We believe that the concept of synergies is often attributed to the process of motor control as opposed to a strict structural constraint. In this work, we use a bespoke experimental setup to track spatiotemporal dynamics of synergistic muscle activations across learning in a virtual, high-dimensional, electromyographic-driven task involving muscle contractions of the hand and forearm. We find that over trials the motor system adapts its synergistic action to fulfill the predefined task requirements in an optimal manner.

> There are many variations on the motor synergy concept61; here we mean functional couplings of different joints or muscles such that motor control operates at the level of multi-joint coordination patterns ratherthan through independent control of all joints. Producing actionsat this slightly higher level of abstraction can facilitate explorationand learning of new skills as well as simplify planning. (Wayne Nature Comms Hierarchical Motor Control)

There is a longstanding debate about the origins of muscle synergies that strongly mirrors the nature-nuture debate. Are synergies learned or are they hardwired? If they're hardwired, what physiological subsystem contains this hardwiring? We don't need to take a side because there is clear evidence that humans overcome synergies to adapt their motor outputs to solve novel tasks and overcome all types of changes in the motor loop (injury, fatigue, prism goggles, etc.) via well-studied (in laboratory tasks at least) adaptation mechanisms [Helmholtz, Wolpert, Todorov, newer work on synergy shifts such as [@DeRugy2012,Berger2013]. The more interesting questions ask on what timescales and by what mechanisms does learning occur, and can we reverse engineer paradigms and tasks that improve the learning rate.

*There are very few tasks dealing with the hand in particular. What type of task would test the hypothesis that CM connections act to fractionate synergies of the hand such that we can tune a parameter of the task to require more or less influence of these direct connections? We would like to ask a user to fractionate synergies of the hand to different levels.*

This requires first mapping the intrinsic available dynamics of the hand per user.

We then would like to present fixed mappings between hand output (either through direct muscle activity or through a controller such as a force pad).

There is work suggesting that CM connections synapse primarily on low threshold motor units that are recruited first. This would imply a difference in synergy fractionation at lower force as opposed to higher force. This can be tested by adding a force parameter within a task.

This hunch was bolstered specifically by the work of Takei et al. in their 2017 PNAS paper:

> It is generally believed that the direct corticomotoneuronal (CM) pathway, which is a phylogenetically newer pathway in higher primates, plays a critical role in the fractionation of muscle ac- tivity during dexterous hand movements. However, the present study demonstrated that PreM-INs, which are phylogenetically older, have spatiotemporal properties that correlate with muscle synergies during voluntary hand movements. Therefore, it is likely that these two systems have specialized functions for the control of primate hand movements, namely “fractionated control” and “synergistic control,” respectively. The interaction of these two putative control systems might be the source of the exceptional versatility of primate hand move- ments. For example, a power grip (e.g., gripping a hammer) is characterized by the predominant coactivation of hand muscles. It is known that power grip requires less involvement of the CM system, and therefore might result more from the PreM-IN system. Conversely, fine control of individual finger movements (e.g., control of a fingertip force of a single digit) requires higher fractionation of individual muscles and probably depends more on the CM system. Indeed, muscle synergies are not active during fine individual finger movements in some cases. Precision grip requires the fractionation of hand muscles as well as their coactivation, and thus might depend on cooperation of both the CM and PreM-IN systems. These examples suggest that the optimal balance of the two control systems may vary according to task requirements. Optimization of balanced control may be an important factor also for the acquisition of new motor skills. For example, Berger et al. demonstrated that learning a new movement that is compatible with existing muscle synergies occurs much more quickly than learning a movement requiring new muscle synergies. This implies that establishing, modifying, or masking muscle synergies requires more training. This might explain our everyday experience that highly fractionated movements require extensive practice (e.g., using chopsticks requires more extensive training than using spoons). This conceptual framework of balanced control systems may help future studies to clarify how our nervous system controls and acquires versatile hand functions. [@Takei2017]

This notion of an "old" and "new" motor cortex is not conceptual, but has been shown using viral tracing techniques [@Rathelot2009].

As I see it, the goal is to build a falsifiable model which takes into account the bipartite structure of M1 into account, and find tasks that ostensibly require the direct descending connections to fractionate learned synergies. In effect, the hypothesis to test is that CM connections override the "consolidated" patterns putatively generated via spinal circuitry.

Thus, this is a learning question, an experimental problem, and a modeling task rolled into one. We have a good hunch that is backed up by solid work. The question comes down to how much we can learn by recording as much muscle activity as we can and designing very clever tasks to test very clever models.

* Neural basis for hand muscle synergies in the primate spinal cord
https://www.ncbi.nlm.nih.gov/pubmed/28739958

Two  mutually  non-exclusive  scenarios  can  be envisioned as to how corticospinal (and reticulospinal –see Baker, 2011, this issue) pathways might be organized to coordinate the activities of multiple muscles needed to perform finger movements (Schieber, 1990). In one,separate pathways operate on each of the requisite motor nuclei. In the other, selection of the muscles into functional groups is determined in part by the pattern of divergence of individual descending pathways across different motor nuclei in the spinal cord. This latter type of organization,while less flexible, might underlie the assemblage of muscles into synergistic groups that serve as the building blocks of the behavioural repertoire of an animal. In contrast to the extrinsic muscles of the dominant hand described above, virtually no short-term synchrony was observed across intrinsic muscles participating in the precision grip (McIsaac & Fuglevand, 2008). This result suggests that the descending pathways that control the activities of intrinsic muscles provide more concentrated input to individual motor nuclei than those pathways destined for motor nuclei innervating extrinsic hand muscles. The contrasting organizations of the descending pathways targeting extrinsic and intrinsic muscles seem in harmony with postulated functions of these two groups of muscles(Longet al.1970). Intrinsic muscles configure the digits to the unique dimensions of an object to be handled. HighlyFigure 5. Mean (SD) common input strength (CIS – index representing magnitude of short-term synchrony; Nordstrometal.1992) for pairs of motor units residing in the same compartment or adjacent compartments of three human multi-tendoned hand muscles, extensor digitorum (ED), flexor digitorum superficialis (FDS) and flexor digitorum profundus(FDP)Mean (SD) CIS values: ED same=0.70 (0.30), ED adjacent=0.41(0.18), FDS same=0.45 (0.30), FDS adjacent=0.27 (0.17), FDPsame=0.47 (0.19), FDP adjacent=0.36 (0.21). Values inside ofbars indicate number of motor unit pairs. Data compiled from:†Keen & Fuglevand (2004b); McIsaac & Fuglevand (2007); McIsaac& Fuglevand (unpublished data); Winges & Santello (2004).independent pathways, therefore, enable the fractionated actions of the digits needed for such a function. Extrinsic muscles provide the primary gripping forces during object manipulation. Because gripping necessitates the production of precisely counterbalanced forces between the thumb and one or more fingers, extrinsic muscles have their activities linked by divergent descending inputs. (Fuglevand 2011)

## Loops, cerebellum

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

"Sauerbrei BA, Guo JZ, Cohen JD, Mischiati M, Guo W, Kabra M, Verma N, Mensh B, Branson K, Hantman AW. Cortical pattern generation during dexterous movement is input-driven. Nature" (Bizzi and Ajemian 2020:1823)


## Precision Grip

Results imply that descending pathways diverge extensively to operate on the two motor nuclei supplying thumb and index finger muscles as a unit and thereby compel them to operate in unison. Interestingly, such across-muscle synchrony was seen only in the dominant but not in the non-dominant hand (Fig. 4). Whether such lateralized differences are laid down early in development or represent plastic changes associated with chronic usage are questions currently under investigation. (Fuglevand 2011)

Statistics of Natural Movements Are Reflected in Motor Errors (Wolpert)
https://www.ncbi.nlm.nih.gov/pubmed/19605616

Structural Learning, Wolpert+Braun+Mehring
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2692080/





In piano performance, not all digits necessarily move for the production of a tone. Depending on contexts and task demands, some digits either move anticipatorily to facilitate production of upcoming acoustic events or even do not have to move. The former anticipatory modification of the movements is called coarticulation and serves as a mechanism that ensures smooth succession of sequential movements such as speech (Ostry et al., 1996) and finger spelling (Jerde et al., 2003). This coarticulation was also evident in piano playing, particularly when the hand posture changes dynamically (Engel et al., 1997). For example, the fingers and wrist initiated preparatory motions 500 ms prior to the thumb-under maneuver, which facilitated the subsequent horizontal translation of the hand. Finger muscular activity also provided evidence supportive for co-articulation in piano playing (Winges et al., 2013). The balance of burst amplitudes across multiple muscles depended on the characteristics of the preceding and subsequent keypresses, forming neuromuscular co-articulation throughout the time course of sequential finger movements. (Shinichi Furuya* and Eckart Altenmüller 2013)


