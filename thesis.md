---
title: Sensorimotor Learning in Virtual Environments
author: Spencer R. Wilson
date: 1/1/2021
toc-title: Contents
---

<!--

How does this document work?

Here is general stuff about the page. Below that add "mdmerge" CLI links to transclude other markdown documents into this one, similar to latex chapters/includes.

Then we run compile, a python script that invokes pypandoc, which adds a header and puts it all into a template which references pandoc.css

TODO:
	- make the layout more small-screen friendly (rearrange the TOC)
	- think about how to include footnotes in the sidebar? (tufte pandoc css)
		- combine tufte template with fixed table of contents (maybe on the left?)
	- how do we output to pdf?

 -->

## Where are you?

This is an experiment in creating an open kind of thesis. To start adding comments to this page, just highlight some text, click `annotate` and start typing. Note that you will have to a <a href="https://web.hypothes.is/" target="_blank">Hypothes.is</a> account, but it only takes a moment (and it's a nonprofit organization). Add as many comments as you like!

# Introduction

Named after roboticist Hans Moravec, the Moravec Paradox states that it is easier to generate artificially intelligent performance on tasks such as chess which we think of as intellectually challenging than to provide a machine with the faculties we take for granted such as movement. Under this lens, the human motor system is an incredible feat of evolution which produces not only only

This thesis attempts to make incremental progress on advancing the ability of machines to move naturally by studying the movement of human subjects in controlled experiments and working to test models of natural movement by comparing with the collected data.

dd

> The processes by which biological control solutions spanning large and continuous state spaces are constructed remain relatively unexplored. Future investigations may need to embed rich dynamical interactions between object dynamics and task goals in novel and complex movements [@McNamee2019].

We know surprisingly little about how this process unfolds in the brain. So little, in fact, that we haven't quite figured out what the brain is actually doing. We know that it is involved in these muscle contractions, but what sort of strategy do you use to explore this space of possible mappings between what you experience when you move and what you expect to see and feel as a result? This is the question I hope to make headway on.

To do this, I'll use the literature of reinforcement learning and optimal control theory to guide my theoretical understanding of what is happening when a subject begins to experience learning in this novel situation. I will model hypotheses of this learning process and compare these models to the large amounts of data my experimental setup will produce as we track learning of subjects over many sessions.

## proposal

Even inane tasks such as bringing a glass of water to your lips are routinely referred to in the control literature as a “problem” despite being effortless for the majority of people. A recent review provides a clear call to action:

> The processes by which biological control solutions spanning large and continuous state spaces are constructed remain relatively unexplored. Future investigations may need to embed rich dynamical interactions between object dynamics and task goals in novel and complex movements [@McNamee2019].

For my PhD project, I propose developing a real-time, high-dimensional electromyography (EMG) pipeline to create closed-loop virtual motor learning experiments with human sub- jects which involve tasks with precisely this kind of dynamical richness. We aim to build on our current understanding and models of continuous control in humans with an eye towards illustrating how the variability in our motor output evolves over learning a novel, highly-skilled task.
In particular, the human hand is a unique evolutionary invention that enables an unprece- dented ability to manipulate objects in a range of tasks. Recent work has shown that monosy- naptic cortical projections controlling the digits, the corticomotoneuronal (CM) tract, act in coordination with synergistic muscle activations of the hand to achieve control that is balanced between modularity and flexibility[20, 21, 27]. These findings suggest that this bipartite structure in human motor cortex driving dexterous control of the distal part of the upper limb is due to evolutionary pressure to quickly generalize between tasks. Thus, the control system governing movement of the human hand is an ideal testbed for quantifying changes in muscle activity during skill acquisition.
Classical laboratory tasks, such as reaching under perturbations, tend not to reflect the statistical richness of natural sensorimotor control and learning. Natural learning processes unfold across multiple timescales, and humans have a unique ability to quickly optimize internal parameters in response to external perturbations and new sensory information to achieve the goals of an ongoing plan. To engineer this flexible learning in silico, we must understand how humans adapt to a novel sensorimotor mapping. There exist a handful of prior studies mapping EMG activity and finger joint angles directly to virtual stimuli, though few are focused on the learning process and none have the input dimensionality we aim to achieve in work proposed here[3, 16, 19, 6, 14].
In one sense, our goal is to reverse-engineer our ability to acquire novel motor skills. This will require three sequential phases: characterizing the space of naturalistic motor behaviors recorded via surface EMG, determining the ability of healthy subjects to perform tasks outside of this space of naturalistic muscle activity, and modeling the learning process for tasks designed with knowledge from the first two phases.


## SfN abstract

A considerable amount of research has focused on  the existence of synergies as a simplifying structure in the motor system. We believe that the concept of synergies is often attributed to the process of motor control as opposed to a strict structural constraint. In this work, we use a bespoke experimental setup to track spatiotemporal dynamics of synergistic muscle activations across learning in a virtual, high-dimensional, electromyographic-driven task involving muscle contractions of the hand and forearm. We find that over trials the motor system adapts its synergistic action to fulfill the predefined task requirements in an optimal manner.

- engineering
	- recording 64 channels of EMG from multiple muscles the arm and hand with realtime feedback
	- in an isometric learning task
- dimensionality reduction
	- static weights
	- synergies shift
- novel rig / setup
- compare to previous approaches
- enables novel approaches to analysis of high dimensional neural data
- hypothesis: ?

abstract
We propose a high-density closed-loop EMG-driven setup to study human motor learning on a virtual task driven directly by muscle activation.


- rig methods
- task methods
	- calibration --> choice of movements/task
	- training --> choice of mappings/feedback
- analysis
	- existing constraints from calibration data?
	- learning curve in task space
	- shift in synergies -- time evolution of covariance?
	- perturbation response?
- modeling
	- LQG predictions
	- SDN? look at stats
	- choice of gradients
	- comparison of muscle-level stats
	- LQG lesioning


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

### Analysis of the synergies underlying complex hand manipulation (Todorov & Ghahramani 2005) blah blah blah blah blah blah

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

## Corticomotoneuronal Connections

* Subdivisions of primary motor cortex based on cortico-motoneuronal cells (Rathelot, Strick PNAS 2008)
https://www.pnas.org/content/106/3/918

x Corticomotoneuronal cells are “functionally tuned”
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4829105/

Although CM synapses exert powerful excitatory effectsonα-motoneurons, the same motoneurons also receivemany other inputs (Fuglevand, 2011), including thosefrom Ia afferents, spinal interneurons, propriospinalneurons, reticulospinal neurons and rubrospinal neurons(Mewes & Cheney, 1991; Flamentet al.1992; Porter& Lemon, 1993; Perlmutteret al.1998; Riddleet al.2009). Any individualα-motoneuron receives thousandsofsynapticcontacts.Thehandfulofsynapticcontactsfroma given CM cell therefore does not consistently drive thedischarge of any particularα-motoneuron. (Schieber 2011)

rathelot, strick?

- "Following a century of detailed anatomical tract-tracing, electrophysiological investigation and careful lesion studies, our knowledge of the executive pathways through which ‘commands’ for movement must pass is unrivalled, yet we are still some way from really understanding how a movement is generated, which structures and pathways are involved and how they interact during the period leading up to movement onset."

- The intense, synchronised output generated by electrical stimulation of macaque motor cortex evokes responses in hand and digit muscles with onset latencies of only approximately 10ms. These latencies are much shorter than the 60–100 ms between the onset of changes in M1 activity and the onset of muscle activity during voluntarily generated movements (Cheney and Fetz, 1980; Porter and Lemon, 1993).

- The discovery that M1 neurons can become active during observation of the actions of others, but without any overt signs of movement in the observer (Vigneswaran et al., 2013) adds to a long list of evidence that motor cortex can be active in a number of different states, all of which are quite distinct from movement itself (Schieber, 2011). These include preparation for movement (Shenoy et al., 2013), mental rehearsal and imagination (Cisek and Kalaska, 2004; Dushanova and Donoghue, 2010; Macuga and Frey, 2012).

- PTNs exhibit additional features that are consistent with a role as ‘command’ neurons. These include the fact that they make many collaterals to important subcortical motor structures, such as the red nucleus and the pontine nuclei (Ugolini and Kuypers, 1986), thereby providing ‘efference copy’ of ‘commands’ to the cerebellum.

- A further feature of some primate PTNs is that they make direct cortico-motoneuronal (CM) connections to alpha motoneurons (Porter and Lemon, 1993; Rathelot and Strick, 2006; Zinger et al., 2013), allowing the motor cortex direct access to spinal motoneurons. Of course, the CM system does not act alone, but in parallel with many other local interneuronal mechanisms and other descending pathways (Baker, 2011; Lemon, 2008), seg- mental (Takei and Seki, 2010) and propriospinal systems (Kinoshita et al., 2012). It is interesting that CM synapses on motoneurons are not subject to presynaptic inhibition (Jackson et al., 2006), suggesting that other systems (e.g. peripheral affer- ent inputs from the moving limb) do not use this mechanism to modify CM inputs to motoneurons, which would mean that infor- mation delivered by CM projections is allowed unfettered influ- ence over target motoneurons.

- CM cells show changes in activity long before movement onset, far longer than the esti- mated conduction delays: thus CM cells exert their influence long before movement starts, but at a level that is subthreshold for motoneuron activation and subsequent movement.

- __CM cells are active for a whole range of different limb move- ments, including reach-to-grasp, precision grip and during tool- use by macaques (McKiernan et al., 1998; Muir and Lemon, 1983; Quallo et al., 2012). CM connections are particularly well- developed in primates with a high level of dexterity and who use tools. Interestingly, CM cells are characterised by showing not only increases, but also decreases in activity before and during precision movements (Maier et al., 1993; Quallo et al., 2012). Indeed, one way that M1 appears to control the pattern of muscle activity during grasp is to ‘disfacilitate’ the excitatory drive to motoneurons.__ (Lemon Kraskov 2019)

- The primate corticospinal tract shows many interesting features that distinguish it rather sharply from the rodent pathway. These include the size and dis- tribution of fibres within the tract, with a small but probably very significant population of fast-conducting axons (Firmin et al., 2014).



*There are very few tasks dealing with the hand in particular. What type of task would test the hypothesis that CM connections act to fractionate synergies of the hand such that we can tune a parameter of the task to require more or less influence of these direct connections? We would like to ask a user to fractionate synergies of the hand to different levels.*

This requires first mapping the intrinsic available dynamics of the hand per user.

We then would like to present fixed mappings between hand output (either through direct muscle activity or through a controller such as a force pad).

There is work suggesting that CM connections synapse primarily on low threshold motor units that are recruited first. This would imply a difference in synergy fractionation at lower force as opposed to higher force. This can be tested by adding a force parameter within a task.

This hunch was bolstered specifically by the work of Takei et al. in their 2017 PNAS paper:

> It is generally believed that the direct corticomotoneuronal (CM) pathway, which is a phylogenetically newer pathway in higher primates, plays a critical role in the fractionation of muscle ac- tivity during dexterous hand movements. However, the present study demonstrated that PreM-INs, which are phylogenetically older, have spatiotemporal properties that correlate with muscle synergies during voluntary hand movements. Therefore, it is likely that these two systems have specialized functions for the control of primate hand movements, namely “fractionated control” and “synergistic control,” respectively. The interaction of these two putative control systems might be the source of the exceptional versatility of primate hand move- ments. For example, a power grip (e.g., gripping a hammer) is characterized by the predominant coactivation of hand muscles. It is known that power grip requires less involvement of the CM system, and therefore might result more from the PreM-IN system. Conversely, fine control of individual finger movements (e.g., control of a fingertip force of a single digit) requires higher fractionation of individual muscles and probably depends more on the CM system. Indeed, muscle synergies are not active during fine individual finger movements in some cases. Precision grip requires the fractionation of hand muscles as well as their coactivation, and thus might depend on cooperation of both the CM and PreM-IN systems. These examples suggest that the optimal balance of the two control systems may vary according to task requirements. Optimization of balanced control may be an important factor also for the acquisition of new motor skills. For example, Berger et al. demonstrated that learning a new movement that is compatible with existing muscle synergies occurs much more quickly than learning a movement requiring new muscle synergies. This implies that establishing, modifying, or masking muscle synergies requires more training. This might explain our everyday experience that highly fractionated movements require extensive practice (e.g., using chopsticks requires more extensive training than using spoons). This conceptual framework of balanced control systems may help future studies to clarify how our nervous system controls and acquires versatile hand functions. [@Takei2017]

This notion of an "old" and "new" motor cortex is not conceptual, but has been shown using viral tracing techniques [@Rathelot2009].

As I see it, the goal is to build a falsifiable model which takes into account the bipartite structure of M1 into account, and find tasks that ostensibly require the direct descending connections to fractionate learned synergies. In effect, the hypothesis to test is that CM connections override the "consolidated" patterns putatively generated via spinal circuitry.

Thus, this is a learning question, an experimental problem, and a modeling task rolled into one. We have a good hunch that is backed up by solid work. The question comes down to how much we can learn by recording as much muscle activity as we can and designing very clever tasks to test very clever models.


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

The goal of the project’s first phase is to develop a high-dimensional surface EMG recording rig to generate datasets with high signal-to-noise ratio and dense coverage over superficial muscles of the arm and hand. The first question of this phase is: what are the limitations of a closed-loop myocontrol experiment, and how can such constraints be avoided or leveraged? To answer this question we will develop a signal processing pipeline and diagnostics suite to identify constraints in the setup and aim to overcome, as much as possible, the limitations inherent in surface EMG recording such as muscle crosstalk and rigorous electrode placement[10].
The concept of the experimental setup is shown in Figure 1, where 64 monopolar electrodes are attached to a subject’s arm and hand to record muscle activity. The arm and hand are kinematically constrained in a custom fixture and motor activity is recorded during isometric muscle contractions at levels less than 20$%$ maximum voluntary contraction to lessen the risk of involuntary co-contractions. The setup circumvents the limb biomechanics by mapping muscle output directly to virtual stimuli shown on a computer monitor. Additionally, our study focuses on low-force, isometric contractions to avoid complications due to artifacts in dynamic, high- force movements.
We chose 64 channels in order to have at least two electrodes per muscle implicated in control of the hand in the event that we require differential recording. This choice limits our analysis to the motor pool level. If our questions require recording at the motor unit level, we will need to move to a higher channel count system. Literature in this field typically use a much lower number of channels. We believe that using 64 electrodes will help develop a more complete picture of the superficial muscle activity of the arm and hand across learning. A diagram of muscles relevant to thee control of the hand and wrist is shown in Figure 2 on page 4. We are not aware of a rigorous study testing which muscles of the arm and hand can be accurately captured using surface EMG.

The second question of this phase is: what is the manifold of activity in electrode space during natural hand use? To answer this question, we will record naturalistic activity by subjects completing a set protocol that covers the naturalistic space of electrode covariance. For comparison, we will record a dataset of naturalistic tasks using a separate, mobile setup with the same electrode placement pattern but without the isometric constraint. These datasets could be collected from a range subjects going throughout their daily tasks, or using a specific set of tasks in the laboratory such as handwriting and the use of various tools. Encouragingly, a recent review noted that “Similarly to the breakthroughs in understanding vision that followed the quantification of statistics of natural scenes, a clear description of the statistics of natural tasks might revolutionize our understanding of the neural basis of high-level learning and decision- making”[18].
By analyzing the structure of these naturalistic datasets, we can compute the dimensionality of naturalistic movement as a subspace within our electrode space, similar to work done using joint angles of the hand[24, 22, 11]. From this work we know that while the hand has 29 joints and is controlled by 34 muscles, the dimensionality of natural hand movements is closer to 8 in joint angle dimension space based on principle components analysis. This analysis will also help us determine the biomechanical constraints on hand output dimensionality. We hypothesize that this will be higher than 8 and lower than 23, which gives us a large task space to work with for generating learning tasks.
We aim to extend this prior work using learning algorithms that take into account time- varying dynamics of the signal in addition to common tools like components analysis and matrix factorization. This analysis will help generate an understanding of intersubject, intersession, and intertask variability. Both an analysis of dynamic correlations and a validation of dimensionality using EMG would be a novel contribution to the literature.
We anticipate that quantifying electrode placement and calibrating across sessions will be a major challenge. We aim to develop a mechanical fixture for recording as well as alignment tools to aid in placing electrodes in precisely the same location each session. Properly separating variability due to electrode placement from behavioral and physiological variability will be paramount to establish repeatability in our results. Once we have collected a naturalistic activity dataset, we can begin to design bespoke feedback mappings and perturbations, as discussed in Section .


## Unsupervised Feature Extraction

We want to determine a redundant control space from data taken during natural activity. The difficulty with this is that such a natural activity manifold may display spatial (channel-wise) correlations that are possibly physiologically separable. Thus, there are two aims   which must be addressed separately:

1. Expore subjects' ability to decorrelate descending output to the muscles which have been shown to be correlated in a natural activity dataset.
    - Such a structured exploration might provide support for the hypothesis that "synergies" are flexible correlations between muscles driven by task demands rather than (or in addition to) physiological structure. This needs to be done incredibly carefully to escape criticism of hard-wired synergy enthusiasts.
    - See *de Rugy 2012* for a critique of OFC and hard-wired synergies
2. Use common correlated outputs to develop a family of BMI-type learning tasks as a proxy for a "novel skill", then track motor planning of this new skill to compare with motor planning algorithms.
    - We might be able to get #1 for free by going after this goal if we're careful in the setup
    - This is arguably a more impactful focus as it connects low-level motor hierarchy data (EMG) to high-level planning with a normative hypothesis.

Electrode data from a single trial of a single session is held in a data matrix $X$ (n_electrodes, n_samples), and we wish to find a latent weight matrix $W$ (n_electrodes, n_components) which reconstructs $X$ by projecting latent trajectories $H$ (n_components, n_samples) into electrode space:

$$
X = W\cdot{H}
$$

$H$ is the activity of the latent processes, and $W$ is there mixing matrix. The columns of $W$ are the principal vectors spanning the latent subspace in electrode space. If we have new samples, we can project these new points onto this subspace:

$$
h_{new} = W^T\cdot{w_{new}}
$$

To justify this decomposition, we have to make some assumptions about the nature of the EMG signal, namely that the signal is linear instantaneous (each EMG sample can be instantly mapped to control space). The other assumption is that the basis $W$ should be orthonormal, that the columns of $W$ are orthogonal with unity norm. This ensures that the left inverse $W^{-1}$ is equal to the transpose $W^T$ such that:

$$
\begin{align}
X &= W\cdot{H} \\
W^{-1}\cdot{X} &= {H} \\
W^{T}\cdot{X} &= {H}
\end{align}
$$

See *Muceli 2014* for use of the Moore-Penrose pseudoinverse in place of the transpose when the columns of $W$ do not form an orthonormal basis. This would be the case for NMF. Is there a factorization that produces nonnegative, orthogonal coordinates? Or is the pseudoinverse okay? I will need to test this.

Stated in an information theoretic way, we want to minimize the reconstruction loss $\mathcal{L}$ for our derived encoder-decoder pair ($E$,$D$). We're decoding high dimensional activity into its latent dimensions, and encoding back into the high dimensional space. :

$$
\min_{E,D}{\mathcal{L}\left[X - EDX\right]}
$$

This way, forget about orthonormality and solve for an encoder and decoder directly. That is, $E\neq{D}$ is perfectly acceptable.

Each row of $D$ might be called a **spatial filter**, a linear combination of electrode activities into a surrogate, hopefully more intuitive space.

In general to find such a basis we must :

- Extract "natural activity manifold" from freeform data
- Use features of this natural subspace to derive control mapping
  - Linear iid features:
    - PCA
    - dPCA
    - NMF
    - ICA
  - Linear time-dependent features:
    - SSA
    - LDS model / PGM
  - Nonlinear
    - autoencoders
    - networks

The behaviors present in our calibration dataset are crucial, as they determine the spatial correlations used to generate the mapping. If only complex, multi-muscle movements are present in the calibration, it will be impossible to decode subtle movements involving few muscles. Additionally, because extraction is unsupervised, it will be impossible to know how to alter the control basis directions (if we wish to do so) such that they involve single muscles or the smallest sets of muscles.

Ultimately, we want to find reproducible features in our data that are due to muscle coordination alone, rather than volitional movements. We want the lowest level covariance that reflects physiology rather than a task-level behavioral description (see *Todorov, Ghahramani 2005* and *Ingram, Wolpert 2009*). The idea is that if we collect data from enough tasks, we can extract the common modes of muscle activity. This is true only if we are sampling uniformly from the space of tasks. Otherwise one task, and therefore one coordination pattern, will be overrepresented.

## Task Formalization

In this task, the subject's first goal is to interact through an unknown visuomotor mapping and internalize this model. The second problem is to use this model to solve a control problem.

1. System Identification -- learning a transition function $p(y_t|x_t, u_t)$
    - How do you learn the unknown observation model from data?

2. Policy Optimization
    - Once dynamics are learned (or at least stable?), how do we form a policy that is generalizable to new tasks under these dynamics?
    - This is the control problem.

It's safe to assume that these processes are happening in parallel. Because we have complete and arbitrary control over the observation mapping, we can ask the subject to interact through a  dynamic that is intuitive (informative prior) or unintuitive (uninformative or inhibitive prior). Each scenario, we hypothesize, will elicit different strategies for learning and control.

The unknown mapping $M$ from muscle to task space looks like the observation matrix $H$ in the LQG problem:

$$
\begin{align*}
y_t &= Hx_t + v_t\,\,\,(\mathrm{LQG}) \\
y_t &= Mx_t + v_t. \,\,\,(\mathrm{experiment})
\end{align*}
$$

The state dynamics in the task are of the form:

$$
\begin{align*}
x_{t} &= Ax_{t-1} + Bu_{t-1} + w_{t-1} \,\,\,(\mathrm{LQG}) \\
x_t &= Dx_{t-1} + Iu_{t-1} + w_{t-1} \,\,\,(\mathrm{experiment})
\end{align*}
$$

where $D$ is a diagonal decay matrix of with terms $\mathrm{e}^{-\lambda}$ and $I$ is the identity. The subject produces muscle contractions which add to the current latent (unobserved) state. In the absence of control signals, the state decays back to $0$ in line with the physics of your arm returning to a passive state in the absence of muscle contractions. The terms $w$ and $v$ are gaussian noise vectors with distributions $\mathcal{N}(0,Q)$ and $\mathcal{N}(0,R)$. If we combine the transition and observation models:

$$
\begin{align*}
y_t &= MDx_{t-1} + Mu_{t-1} + Mw_{t-1} + v_t \\
&= A^\prime x_{t-1} + B^\prime u_{t-1} + Mw_{t-1} + v_t.
\end{align*}
$$

We can think of this as the combined system identification problem where $A^\prime=MD$ and $B^\prime=M$ are unknown and must be estimated. The noise covariances of this altered system are now non-trivial, however. We could also assume that the transition dynamic $D$ is known and that the identification problem is learning the mapping $M$ only. This might not be a poor assumption since the exponential decay is meant to serve as an intuitive passive dynamic.

In each trial of the task, a subject will have some internal representation of the observation dynamic $M$ which may or may not be accurate. In order to make accurate predictions, $M$ must be estimated.

Learning linear dynamical systems from data is a hot topic of research, most of which seems to focus on learning in the context of complete state observation ($M=I$, $y=x$). Algorithms to determine parameters of $A$ and $B$ are proposed (see Dean, Recht 2018).

From LQG theory we know that the control law is a linear function of the state:

$$
\begin{align*}
u_t = -L_tx_t
\end{align*}
$$

and thus our combined system dynamic is:

$$
\begin{align*}
y_t &= M(D-L_t)x_{t-1} + Mw_{t-1} + v_t.
\end{align*}
$$

The noise covariance due to the observation Q is unchanged, but the new noise covariance for the latent process is now $MRM^T$. This may make things difficult.

#### Questions

- In a behavioral experiment, how can you disentangle system identification/estimation and control? Is suboptimality due to one or the other?
- How does the observation mapping relate to the latent state covariance? The task state covariance?
- How do we formalize this into a probabilistic graphical model? Why would we?
    - Would this make it easier to reason about what the goals are?
    - Would learning $M$ become an inference problem?
    - Would solving the control problem become an inference problem...?
- What noise assumptions can we make? Can we not make?
    - How can we incorporate signal-dependent noise?

### Model-based Reinforcement Learning

Since we only have an approximate model of the system dynamic, we could simply work towards an optimal policy directly using gradient derivative-free optimization methods in a model-free approach. Since we have good evidence that humans leverage internal models to make decisions (at least in a motor problem domain), we need to define an algorithm which uses past observations and controls to update our approximation for the system dynamic. Here is a very general algorithm:

0. Define a base policy/controller and base system model ($L_0$ and $\hat{M}_0$)
1. Collect samples (by interacting with the true environment $M_{true}$) using the current policy/controller (collect $y_t,u_t,y_{t+1}$ triples using $L_i$ for $i \in \{0\dots N\}$
2. Use sample(s) / trajectories to update current system dynamical model $\hat{M}_i$
3. Update current policy/controller $L_i$ (using the system dynamics or using a direct policy method)

If the true system dynamics were known, we could solve the Algebraic Riccati Equation with a backwards pass, and compute our controls in a forward pass. This general algorithm structure highlights how the (unknown) system identification and controller design are intertwined: identifying a system appropriately must rely on sampling and fitting regions of the state space pertinent to adequate control in terms of cost (Ross ICML 2012). Otherwise, our approximation to the true system dynamic will only produce a valid controller in regions we have previously explored. The question is how we can effectively (sample and time efficiently) utilize new state transitions we encounter either online as feedback or between trials to update our model and policy. That is, the number of trials and/or trajectories to use before updating either the system model and/or policy is an important parameter.

In the LQG setting, this might be called "adaptive LQG".

#### Questions

- how does a subject sample the state space as to efficiently learn? do they sample optimally? how does controller/policy optimization proceed based on system identification?
- how does a human subject use error information from each trial and feedback from each time step to update their model and/or policy?
    - how does a subject balance policy updates with model updates?
- On what scale (trials, timesteps) is the model altered? the policy?
    - Replanning at every timestep is a model predictive control algorithm
    - What prediction can we make for ID/learning every trial?
- how does a subject avoid "distribution mismatch" between their base policy and their optimal policy? How do they efficiently explore and use this new data to update their internal model?
    - what exploration strategy does a subject use to avoid mismatch?
    - what
- What is a subject's baseline/prior model? $y_{t} = \hat{f}_0(x_t,u_t)$ or $y_{t} \propto p_0(y_t|x_{t},u_t)$
- What is the base policy / prior policy? $u_t = \pi_0(\hat{x}_t)$
- How do we think about learning a distribution over trajectories in control law space, or perhaps equivalently, in covariance/precision space?
- We might hypothesize that a subject will act as randomly as possible while minimizing cost, a maximum entropy solution that converges to an optimal controller? $\mathcal{H}(p(u_t|x_t))$
- How does a subject penalize changes to their controllers? Do they follow a KL-divergence type of measurement when improving their policy?

# Theory

## Error-based Learning

## Optimal Feedback Control

## KL-control and Composition

## Generalized Policy Selection






## Bibliography
