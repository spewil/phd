# Introduction

I'm working on my PhD at the Sainsbury Wellcome Centre for Neural Circuits and Behavior in London. I'm setting up a family of experiments that I hope will test hypotheses about the organizing principles of sensorimotor control and learning. I'm setting up a task where I record from participants' muscles in their arms and hands using `electromyography`. Subjects' arms and hands are fixed in a brace, but as they send signals from their brain down to their spinal cords and ultimately to their muscles, my electrodes will sense this change in electrical potential and relay this change to the computer, which will reflect these changes through visuals shown on a screen. The object of the game is for the participant to learn which muscle activations correspond to which changes in the visual scene. You can think about this as a video game you're playing directly with your muscles.

> The processes by which biological control solutions spanning large and continuous state spaces are constructed remain relatively unexplored. Future investigations may need to embed rich dynamical interactions between object dynamics and task goals in novel and complex movements [@McNamee2019].

We know surprisingly little about how this process unfolds in the brain. So little, in fact, that we haven't quite figured out what the brain is actually doing. We know that it is involved in these muscle contractions, but what sort of strategy do you use to explore this space of possible mappings between what you experience when you move and what you expect to see and feel as a result? This is the question I hope to make headway on.

To do this, I'll use the literature of reinforcement learning and optimal control theory to guide my theoretical understanding of what is happening when a subject begins to experience learning in this novel situation. I will model hypotheses of this learning process and compare these models to the large amounts of data my experimental setup will produce as we track learning of subjects over many sessions.

## BMI

## Arbitrary Visuomotor Mappings

There are several studies using non-EMG-driven sensorimotor mappings to study human motor control and learning.

x * Remapping Hand Movements in a Novel Geometrical Environment
https://www.ncbi.nlm.nih.gov/pubmed/16148276

vocoder machine bell labs

Hinton, Fells

palsy study

takehome: humans are really good at learning tasks like these, especially with their hands. this type of dexterity is specific to primates if not humans. let's use this ability to understand and try to model how this learning process unfolds.

**_What does this give us that a force-field reaching task can't?_**



## Muscle Synergies

* Neural basis for hand muscle synergies in the primate spinal cord
https://www.ncbi.nlm.nih.gov/pubmed/28739958

Two  mutually  non-exclusive  scenarios  can  be envisioned as to how corticospinal (and reticulospinal –see Baker, 2011, this issue) pathways might be organized to coordinate the activities of multiple muscles needed to perform finger movements (Schieber, 1990). In one,separate pathways operate on each of the requisite motor nuclei. In the other, selection of the muscles into functional groups is determined in part by the pattern of divergence of individual descending pathways across different motor nuclei in the spinal cord. This latter type of organization,while less flexible, might underlie the assemblage of muscles into synergistic groups that serve as the building blocks of the behavioural repertoire of an animal. In contrast to the extrinsic muscles of the dominant hand described above, virtually no short-term synchrony was observed across intrinsic muscles participating in the precision grip (McIsaac & Fuglevand, 2008). This result suggests that the descending pathways that control the activities of intrinsic muscles provide more concentrated input to individual motor nuclei than those pathways destined for motor nuclei innervating extrinsic hand muscles. The contrasting organizations of the descending pathways targeting extrinsic and intrinsic muscles seem in harmony with postulated functions of these two groups of muscles(Longet al.1970). Intrinsic muscles configure the digits to the unique dimensions of an object to be handled. HighlyFigure 5. Mean (SD) common input strength (CIS – index representing magnitude of short-term synchrony; Nordstrometal.1992) for pairs of motor units residing in the same compartment or adjacent compartments of three human multi-tendoned hand muscles, extensor digitorum (ED), flexor digitorum superficialis (FDS) and flexor digitorum profundus(FDP)Mean (SD) CIS values: ED same=0.70 (0.30), ED adjacent=0.41(0.18), FDS same=0.45 (0.30), FDS adjacent=0.27 (0.17), FDPsame=0.47 (0.19), FDP adjacent=0.36 (0.21). Values inside ofbars indicate number of motor unit pairs. Data compiled from:†Keen & Fuglevand (2004b); McIsaac & Fuglevand (2007); McIsaac& Fuglevand (unpublished data); Winges & Santello (2004).independent pathways, therefore, enable the fractionated actions of the digits needed for such a function. Extrinsic muscles provide the primary gripping forces during object manipulation. Because gripping necessitates the production of precisely counterbalanced forces between the thumb and one or more fingers, extrinsic muscles have their activities linked by divergent descending inputs. (Fuglevand 2011)

### Precision Grip

Results imply that descending pathways diverge extensively to operate on the two motor nuclei supplying thumb and index finger muscles as a unit and thereby compel them to operate in unison. Interestingly, such across-muscle synchrony was seen only in the dominant but not in the non-dominant hand (Fig. 4). Whether such lateralized differences are laid down early in development or represent plastic changes associated with chronic usage are questions currently under investigation. (Fuglevand 2011)

Statistics of Natural Movements Are Reflected in Motor Errors (Wolpert)
https://www.ncbi.nlm.nih.gov/pubmed/19605616

Structural Learning, Wolpert+Braun+Mehring
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2692080/

### Skilled Piano Performance

In piano performance, for keystrokes with each of the four fingers during playing various tone sequences, the hand kinematics was characterized by three distinct patterns of finger joint coordination (Furuya et al., 2011a). The motion of the striking finger was consistent across these patterns, whereas the motion of the non-striking fingers differed across them. This was interpreted as evidence for the independence of movements across fingers. In addition, the amount of movement covariation between the striking and non-striking fingers was similar, independent of which finger was used for a keystroke. The finding was in contrast to non-musicians who displayed a hierarchy of independence of finger movements, the middle and ring fingers being less individuated than the index and little fingers (Häger-Ross and Schieber, 2000; Zatsiorsky et al., 2000). The equal independence of movements across fingers can be therefore achieved by extensive piano training. This idea is supported by superior independence of finger movement control for pianists as compared to non-musicians (Slobounov et al., 2002; Aoki et al., 2005), which possibly occurs due to changes at biomechanical and neural levels (Chiang et al., 2004; Smahel and Klimová, 2004). (Shinichi Furuya* and Eckart Altenmüller 2013)

In piano performance, not all digits necessarily move for the production of a tone. Depending on contexts and task demands, some digits either move anticipatorily to facilitate production of upcoming acoustic events or even do not have to move. The former anticipatory modification of the movements is called coarticulation and serves as a mechanism that ensures smooth succession of sequential movements such as speech (Ostry et al., 1996) and finger spelling (Jerde et al., 2003). This coarticulation was also evident in piano playing, particularly when the hand posture changes dynamically (Engel et al., 1997). For example, the fingers and wrist initiated preparatory motions 500 ms prior to the thumb-under maneuver, which facilitated the subsequent horizontal translation of the hand. Finger muscular activity also provided evidence supportive for co-articulation in piano playing (Winges et al., 2013). The balance of burst amplitudes across multiple muscles depended on the characteristics of the preceding and subsequent keypresses, forming neuromuscular co-articulation throughout the time course of sequential finger movements. (Shinichi Furuya* and Eckart Altenmüller 2013)



### Muscular and Postural Synergies of the Human Hand (Weiss & Flanders 2004)

> Single motor units receive a variety of motor commands, and the net result may be that neighboring units in the same muscle are preferentially recruited to produce forces in different directions 3D space or to hold the hand in different static postures. The corollary to this is that a given force or posture involves a collection of units that spans many muscles.

The motor system is distributed in order to solve the redundancy problem as well as to learn new control schemes.

### Analysis of the synergies underlying complex hand manipulation (Todorov & Ghahramani 2005)

> Remarkably, the dimensionality in the individuated joint task was 8.7, or only 2 higher. The latter task is designed to reveal the maximal number of degrees of freedom humans have access to. Why this number is not 20 is unclear; the most likely reason is biomechanical coupling, although limitations in neural control may also play a role. Furthermore, the number 8.7 intuitively seems too low ñ suggesting that such counting methods may underestimate the true dimensionality.

### The statistics of natural hand movements (Ingram & Wolpert 2008)


### Neural Basis of Muscle Synergies, Bizzi Cheung 2013


### Greg Wayne Deep Learning Motor Control

> There are many variations on the motor synergy concept61; here we mean functional couplings of different joints or muscles such that motor control operates at the level of multi-joint coordination patterns ratherthan through independent control of all joints. Producing actionsat this slightly higher level of abstraction can facilitate explorationand learning of new skills as well as simplify planning. (Wayne Nature Comms Hierarchical Motor Control)

There is a longstanding debate about the origins of muscle synergies that strongly mirrors the nature-nuture debate. Are synergies learned or are they hardwired? If they're hardwired, what physiological subsystem contains this hardwiring? We don't need to take a side because there is clear evidence that humans overcome synergies to adapt their motor outputs to solve novel tasks and overcome all types of changes in the motor loop (injury, fatigue, prism goggles, etc.) via well-studied (in laboratory tasks at least) adaptation mechanisms [Helmholtz, Wolpert, Todorov, newer work on synergy shifts such as [@DeRugy2012,Berger2013]. The more interesting questions ask on what timescales and by what mechanisms does learning occur, and can we reverse engineer paradigms and tasks that improve the learning rate.

Note that there are a great number of tasks, and the case for synergies in the motor system cannot be answered simply. Here we are concerned with motions of the hand because we know that this is the endpoint of CM connections. There are many fewer tasks dealing with this system in particular. Most tasks deal with arm reaching, though the most highly cited synergy paper deals with a 1DOF kick [@DAvella2003].


### Todorov 2009

From a 2009 review suggesting exactly the work that our hunch is leading us towards:

> First, analyses such as that performed by Valero-Cuevas et al. [42] and Kutch et al. [40] should be done across many different behaviors and a wider range of behavioral conditions to evaluate whether the structure in the variability of muscle activation patterns is consistent with the muscle synergy hypothesis. Although the analyses used in those experiments exploit some ideal features of finger control, similar experiments should be possible in other behaviors and would help address concerns about synergies arising from task constraints. Second, it should be possible to use synergies to explain suboptimal performance of the CNS [70]. If the CNS has access to a limited set of synergies at a particular time based on the tasks that it currently is able to accomplish, this should suggest that some new tasks should be easier to perform than others [44 ]: if the muscle activation patterns required by the new task lay within the space defined by existing muscle synergies, learning the new task should be relatively easy. In contrast, if the required activations lay outside that space, then the learning should be more difficult and initial performance should be suboptimal. Designing such tasks requires an accurate musculoskeletal model along with knowledge of the existing muscle synergies which would make it possible to predict which tasks would be easy and which would be difficult to learn.

Additionally, the review authors provide an argument for a developmental basis of the synergies we find in EMG recordings:

> Rather than considering muscle synergies as reflecting a strategy for the simplification of control, we suggest that synergies might be considered in the larger context of the intimate interactions between the properties of the musculoskeletal system and neural control strategies. In this context, muscle synergies could be considered as reflecting the statistics of the external world, acknowledging the fact that the external world also consists of the musculoskeletal system itself. In the same way that properties of natural scenes might influence the structure of the visual system, we suggest that statistics of the musculoskeletal system and external world might influence the structure of motor systems.

Note that the authors' second suggestion has been tested in a reaching task. The results concorded with the hypothesis from the quoted review, as we would expect:

> After compatible virtual surgeries, a full range of movements could still be achieved recombining the synergies, whereas after incompatible virtual surgeries, new or modified synergies would be required. Adaptation rates after the two types of surgery were compared. If synergies were only a parsimonious description of the regularities in the muscle patterns generated by a nonmodular controller, we would expect adaptation rates to be similar, as both types of surgeries could be compensated with similar changes in the muscle patterns. In contrast, as predicted by modularity, we found strikingly faster adaptation after compatible surgeries than after incompatible ones.

However, seeing that the mapping between the recorded EMG and the output was a multilinear regression based on a calibration dataset which was grossly altered for the surgery, I do not find it surprising that the learning curves were different after the two surgeries.