# Background Experimental Methods{#sec:experiment}

<!-- doesn't have to be long, explain how we want to extend -->

- what are the most important concepts / results that inform our experiments?
- What do we think we know from experiments about motor control? motor adaptation? motor learning?

## Control

Is LQR (as it’s claimed to be) a reasonable model for feedback control and error reduction + variability prediction for dimensionality reduction-based motor interface

(task reads out from D muscles, find modes of that data; do PCA to get K < D dimensions, controller only responds to motion in those K directions)—does behavior + motor activity follow LQR? this question has already been asked, but it hasn’t been asked for this kind of high-to-low dim mapping. It’s been asked in tasks where muscles haven’t been directly in control (Bolero 2009). Todorov: do a task, look at muscle signal. Muscles that aren’t necessary for task have higher variability b/c they’re not being optimized for task (but does’t introduce perturbations). Also see Loeb (2012) for a negative result saying that muscle coordination is habitual rather than optimal, but it has issues (low # muscles). Can we replicate previous reaching optimality results in our set-up? What’s unique about our set-up is the PCA/dimensionality reduction in muscle activity space. This is important because you can create arbitrary muscle-cursor mappings, so you have to learn a new skill/mapping. This is different than perturbing a fundamental movement and forcing adaptation, which is what has been previously done. For our task, the participants actually have to learn a new task/mapping, rather than just do what they already know and be robust to perturbations. We test the LQR hypothesis once they’ve learned the task, because LQR isn’t a learning theory, it’s a theory about optimal control. We can see if, once people learn a new skill, their behavior is optimal wrt LQR theory. If we establish this, then we can think about how this LQR model is actually learned (enter RL).



> Our results are consistent with a recently described model in which an optimal feedback control policy is calculated independently for each potential target and a weighted average of these policies (that is, feedback gains) is computed at each point in time based on the relative desirability of each target50. Notably, this model, which pre-dicts averaging of feedback gains, can also account for spatial (that is, trajectory) averaging in go-before-you-know tasks. We submit that our result showing feedback gain averaging, coupled with previous work demonstrating trajectory averaging, provides strong support for the compelling idea that the CNS, under cases of target uncertainty, encodes in parallel multiple motor plans, along with their associated control policies, for competing action options. (Wolpert Nature 2018 competing control policies)



Nashed 2014 -- short-latency R1 and long-latency R2 responses (60ms; 45–75ms; 75–105 ms)
stretch responses R1 show dexterity (Andrew Pru 2019,2020) in holding and in reaching


### Adaptation of Reaching

Sinusoidal over trials visuomotor rotations allowed experimenters to disentangle perturbation error sequence over trials in "driven" and "undriven" dimensions by knowing the frequencies of the rotational perturbation. Explicit strategies were given by participants before moving, all errors based off this [@miyamotoImplicitAdaptationCompensates2020]. This is a very clever experimental design but leaves many questions. Particularly, implicit adaptation seems to be driven by a combination of performance error and sensory prediction error, but how can we tease this apart?

> Although little is known about the specific error signals that drive these different processes, an intriguing possibility is that distinct components of implicit learning are driven by performance errors and sensory-prediction errors.

> The convergent findings of the SEM and time lag analyses, based on the amplitudes and temporal structure of implicit and strategic adaptive responses, point to an implicit learning process that actively responds to compensate low-fidelity explicit strategy.

> Our simulation also reproduced the results of the SEM analysis and the temporal lag analysis, which demonstrates that the low-noise process (which models implicit learning) lags behind and effectively compensates for the inappropriate behavior of the high-noise process (which models strategy), a result that can be predicted by mathematical derivation (Supplementary Math Note).

In our experiment, we might call all learning implicit, since there is so much unknown what would we constitute as a strategy? Think we need to make clear the difference between learning and adaptation. Adaption, as used here, is correction to a perturbation over trials of a well-practiced movement. Learning is the discovery of unfamiliar movement patterns through trial and error.

> An important idea in motor skill learning research is that motor learning proceeds from predominantly explicit to implicit states as a learner develops from novice to expert.

This is interesting, as in our experiment we might think the opposite? Depends on how we define explicit and implicit. Here the definition is loosely deliberate and effortful versus automatic and intuitive. Their point here might be mirrored in overall muscle activation, early on it's actively searching. But what for? And how? We might think of this as a foraging task, searching for information about the unknown mapping-- movements as hypotheses.

- prisms
- rotations
- forcefield
- nothing -- van Beers variability





> The vast majority of research in motor learning studies this capacity through adaptation para- digms in which a systematic perturbation is introduced to disrupt a well-practiced behavior, such as point-to-point reaching. [@adrianTheoreticalModelsMotor2012]

- classic reaching adaptation --> this is a different goal
	- shadmehr
	- krakauer
- unperturbed movements
	- van beers

[@Krakauer2019;@Shadmehr2008]

There exist a handful of prior studies mapping EMG activity and finger joint angles directly to virtual stimuli, though few are focused on the learning process and none have the input dimensionality we aim to achieve in work proposed here.

[@manleyWhenMoneyNot2014
@vanbeersMotorLearningOptimally2009
@vanbeersRandomWalkMotor2013]










### Arbitrary Visuomotor Mappings

[@Mussa-IvaldiSensoryMotorRemapping2011]


There are several studies using non-EMG-driven sensorimotor mappings to study human motor control and learning.

* Remapping Hand Movements in a Novel Geometrical Environment
https://www.ncbi.nlm.nih.gov/pubmed/16148276

[@MosierRemappingHandMovements2005]
 

vocoder machine bell labs

Hinton, Fells

palsy study

takehome: humans are really good at learning tasks like these, especially with their hands. this type of dexterity is specific to primates if not humans. let's use this ability to understand and try to model how this learning process unfolds.

**_What does this give us that a force-field reaching task can't?_**

[@nazarpourFlexibleCorticalControl2012]


### Skill Learning Tasks

- skill learning tasks
	- ball and cup
	- dart throwing tasks









### Learning in Cortical Interfaces

- cortical BMI work
	- Batista papers, lee miller papers
- speech learning -- analogy to speech
- bird vocal learning

- we're doing the same experiment, at the muscle level
- try to convince why this is useful, but not too hard


















### Skill Learning in Myolectric Interfaces



"performance levels and rates of improvement were significantly higher for intrinsic hand muscles relative to muscles of the forearm."
[@Dyson2018] 




### Berger et al. 2013


[@BergerDifferencesInAdaptationRates2013a]

Berger et al.'s preprocessing
- lowpassed butterworth at 5Hz
- normalized to MVC calibration
- periodic baseline noise substraction
- choosing synergies by uniformity in force direction (pretty arbitrary)


Using EMG in a learning experiment is not unheard of. Berger et al. 2013 use EMG with 13 muscles to test whether learning new synergy combinations for a task is more difficult that recombining existing synergies@Berger2013a. As we would expect, learning new synergy combinations is more difficult. I would argue that the demand in their "incompatible virtual surgeries" is too strict, that we need to more carefully design synergy perturbations to develop a model of learning in such a task.

Berger et al. fit a muscle-space to force-space mapping $H$ using a force-driven calibration task, and a synergy-space to muscle-space mapping $W$ using NMF.

\begin{align*}
	f &= Hm \\
	m &= Wc
\end{align*}

$\dim(m)=M$ muscles, $\dim(c)=N$ synergies, and $\dim(f)=D$ dimensions of task space where $M>N>D$. Because $H$ and $W$ are rectangular, they have at most rank $D$ and $N$, and we constrain these matrices to be full rank. There are three key subspaces: the nullspace of $H$ mapping muscle activations to 0, the column space or range of $W$ mapping synergy activations to muscle activations, and the common subspace between these two. That is, there are synergy activations which generate muscle activations which lie in the null space of $H$. The paper uses this fact to develop mappings that specifically rotate muscle activations produced by synergies into the null space of $H$ which were not there prior to rotation. The dimensionalities of these subspaces are defined:

\begin{align*}
\dim(\mathrm{null}(H)) &= M - D && \text{muscle vectors $\rightarrow$ 0} \\
\dim(\mathrm{col}(W)) &= N && \text{synergy activations $\rightarrow$ muscle subspace}\\
\dim(\mathrm{null}(H)\cap\mathrm{col}(W)) &= N - D && \text{synergy activations $\rightarrow$ 0} \\
\end{align*}

In the paper, the authors find an orthonormal basis $W_o$ for the range (column space) of the synergy weight matrix $W$ (presumably using a QR factorization) and find the nullspace $H_{null}$ of $H$. These computations are done presumably through QR factorizations (an orthonormal basis multiplied by a rotation and scaling) by finding $Q$ in the first case and finding the latter $M-D$ columns $Q_2$ of $Q = [Q_1 \, Q_2]$ which are $H_{null}$ in the second case:

\begin{align*}
	W &= Q_W^{M\times M}R_W^{M\times N} \\
	  &= \left[Q_{W,1}^{M\times N}\,Q_{W,2}^{M\times M-N}\right]\begin{bmatrix}R_{W,1} \\ 0 \end{bmatrix} \\
	W_o &= Q_{W,1}^{M\times N} \\
	W_o^T &= Q_{W,1}^{T, N\times M} \\
	H^T_{M\times D} &= Q_H^{M\times M}R_H = \left[Q_{H,1}^{M\times D}\,Q_{H,2}^{M\times M-D}\right]\begin{bmatrix}R_{H,1} \\ 0 \end{bmatrix} \\
	H^T_{null} &= Q_{H,2}^{M\times M-D}
\end{align*}

To find each of the three subspace, we take the SVD of the composition $W^TH^T$

\begin{align*}
	W_o^TH^T_{null} &= Q_{W,1}^{T, N\times M} Q_{H,2}^{M\times M-D} \\
	&= Q^T_WQ_H && \dim(N \times M-D) \\
	&= U_{N\times N}\Sigma_{N \times M-D} V^T_{M-D\times M-D} \\
	H^T_{null}V &= W_oU\Sigma
\end{align*}

Now we can pick out the three subspaces using the SVD

\begin{align*}
	W_c &= W_oU[1:N-D] && \text{synergy activations $\rightarrow$ muscle activations in task null space}\\
	H_c &= H_{null}[1:N-D] && \text{synergetic muscle activations $\rightarrow$ 0} \\
	W_{nc} &= W_oU[N-D+1:N] && \text{synergy activations $\rightarrow$ nonzero muscle activations}\\
	H_{nc} &= H_{null}V[N-D+1:M-D && \text{non-synergetic muscle activations $\rightarrow$ 0} \\
\end{align*}

To construct new mappings, the authors construct rotations to alter muscle activation vectors by rotating them from $W_nc$ and remaining in $W_nc$ and from $W_nc$ into $H_nc$. In the first case this alters the mapping by changing the effective muscle activations produced by the existing (learned) synergetic actions. That is, muscle activations putatively produced by synergetic action will be altered to produce different forces in task space (compatible rotations). In the second case, muscle activations putatively produced by existing synergetic action (via W) will be mapped into the null space of $H$ and produce zero force in task space (incompatible rotations).

A key critique of this paper is that such a transformation is too harsh. The compatible rotation allows you to recombine the same muscle patterns, the incompatible doesn't allow you to use existing coactivation patterns at all. The authors do see new synergies emerging even after their training session, consisting of:

- 16 trials of maximum voluntary contraction in 8 directions (calibration)
- 72 trials using force control (calibration)
- 24 trials familiarization
- 144 trials baseline
- 288 trials surgery
- 144 trials washout
- 144 trials baseline

After 288 trials subjects aren't able to complete the task for some movement directions.

### Nazarpour 2012 J.Neuro


[@nazarpourFlexibleCorticalControl2012]

x Flexible Cortical Control of Task-Specific Muscle Synergies
https://www.jneurosci.org/content/32/36/12349

Fig. 4A -- cursor controlled muscles begin to dissociate from non cursor controlled muscles.

Feedforward processing to muscle fields / tunings in the presence of signal dependent noise

Feedback processing based on visual errors


### Radhakrishnan 2008

[@radhakrishnanLearningNovelMyoelectricControlled2008]


x Learning a Novel Myoelectric-Controlled Interface Task — Radhakrishnan, 2008
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2576223/

proprioception is not required to learn nonintuitive MCI mappings

several hundred trials subjects learned pointing with six muscles

prism adaption requires active movement; efference copy implicated if proprioception doesn't seem to be required

control models Fig 10

### de Rugy 2012 - Habitual not Optimal

[@derugyMuscleCoordinationHabitual2012]


just because it's harder to adapt to incompatible surgeries doesn't mean that there are fixed synergies, it just means there are multiple timescales of adaptation available in the neural control hierarchy -- diversity in the neural controller depending on context

learning inverse model may be separate from learning to optimize trajectories on top of that model -- some type of "fine tuning"

skill acquisition (slow, constructing novel synergies) vs. motor adaptation (less slow, adapting existing synergy activations)

It's a good test, but it pushes the optimal control framework too hard? perhaps we need a model for what "good enough" is? If we penalize moving to a new controller from a previously optimized movement, the findings make sense. An optimal control model would predict the exactly optimal coordination patterns for the new scenario, it wouldn't say anything about adaptation from an old solution to a new one. This is why we need to develop a model of adaptation that formalizes this scenario not of kinematic perturbations (noise during movement), but to a drastic change in the plant itself (e.g. muscle failure).


### Mussa-Ivaldi 2019

> Earlier theoretical work by Jordan and Rumelhart [14] considered how the learning of actions can be viewed as the concurrent learning of for- ward and inverse models of actions. **They introduced the concept of distal learning, where the learner has to find a mapping from desired outcomes to actions in order to achieve a desired outcome. To do so, the subject begins by forming a predictive forward model of the transformation from actions to distal outcomes. Such transformations are often not known a priori, thus the forward model must generally be learned by exploring the outcomes associated with particular choices of action. Once the forward model has been at least partially learned, it can be used to guide the learning of an inverse model that predicts the action needed to achieve the distal outcome.** Mussa-Ivaldi2019

> Our findings are consistent with the hypothesis that learning proceeds through the concurrent evolution of cou- pled forward and inverse models of the body-to-object mapping established by the BoMI. Mussa-Ivaldi2019

> Not being square, the matrix H does not have a unique inverse. But there exist infinite “right inverses” that combined with H yield the K x K identity matrix in the task space of exter- nal control signals. Each such right inverse transforms a desired position of the controlled object into one particular set of values for the body signals. We consider users to be competent when they are able to move their body successfully in response to a presented target for the controlled object. Mathematically, we consider this as finding one right inverse G of the map- ping H, out of a multitude of possible and equally valid choices. Mussa-Ivaldi2019

Gradient learning of a forward and inverse model (mapping):

\begin{align*}
	\hat{H}_{n+1} &= \hat{H}_n + \epsilon(p_n - H_nq_n)q_n^T  \\
	G_{n+1} &= G_n - \eta\hat{H}_n^Te_nu_n^T \\
	e_n &= p_n - u_n
\end{align*}

> The comparison between model predictions and actual data in Fig 3 indicates that our proposed model of learning is sufficient to explain the data. However, the mechanism we propose is not necessary; we cannot rule out other possibilities, such as reinforcement learning. [...] This agreement between model and experimental results does not exclude the possibility of alternative learning mechanisms, such as a direct learning of the inverse model [24] or the use of reinforcement learning [25] to acquire an action policy that would play the role of the inverse model. Mussa-Ivaldi2019

How do we break a simple gradient model? On a task that is more difficult? will learning take longer?
	- savings phenomenon
	-

> Although the interface forward map is linear (Methods, Eq (5)), this is a many-to-one map admitting a multitude of inverses. This “redundancy” opens the possibility of successful linear and nonlinear inverse maps. Redundancy also leads to an important consideration about gradient descent learning. The reaching error surface in the space of the inverse model elements does not have a unique minimum, but a continuously connected set of minima corresponding to the null space of the forward map. In the metaphor of a skier descending from a mountain following the gradient, this space of equivalent inverse models corresponds to a flat elongated valley at the bot- tom of the mountain. Anywhere along the valley is a valid end to the ride, as it corresponds to a valid inverse model. The inverse model on which the steepest descent ends depends on the initial conditions, as predicted by the dynamical model (see Fig 3b–evolution of the norm of the inverse model error), as well as on the realization of the noise employed in any given simulation of the learning model.

> Although the two-dimensional subspace formed by the first two PCs captured a large fraction of the total variance of body motions, it did not necessarily reflect the natural up-down/left-right orientation of the display monitor. Therefore, following calibration and PC extraction, there was a customization phase in which users were allowed to set the origin, orientation, and scaling of the coordinates in task space, based on their preference.

Subjects have prior knowledge of their directions in task space?


x 90% isn't enough -- Follow-up on the previous paper -- critiques “direct evidence”
https://www.biorxiv.org/content/10.1101/634758v1

* Structured variability of muscle activations supports the minimal intervention principle of motor control
https://www.ncbi.nlm.nih.gov/pubmed/19369362