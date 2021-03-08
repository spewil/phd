# Next Steps{#sec:next_steps}

> *When it comes to the problem of skilled movement, the algorithm is simply not known.*
>
> &mdash; Wolpert & Ghahramani, *2000*

## EMG Hardware

Our preliminary data confirms the working principle of the setup and highlights the next steps for producing a quality dataset. This is in accordance with the literature, where more advanced use of EMG is emerging as an important tool in understanding the complexities of motor computation[@Hug2011].

Our first concern is eliminating line noise in the recording setup. This is immediately achievable with investments in more elaborately shielded hardware, should be very low noise relative to our signal. Most EMG signals are heavily smoothed and trial-averaged due to noise, but we are confident that our records can be analyzed at the level of single trials, much like recent developments in neural data analyses [@churchlandNeuralVariabilityPremotor2006;@churchlandNeuralPopulationDynamics2012a].

Move to 64 channels!

<!-- > EMG activity was recorded using hook-wire electrodes (44 gauge with a 27 gauge cannula; Nicolet Biomedical, Madison, WI) placed in the muscle for the duration of single recording sessions. [...] Electrode voltages were amplified, bandpass filtered (150–500 Hz, four pole, 24 db/octave), sampled at 1000 Hz, and digitized. Off-line, raw traces were differentiated (to remove any remaining baseline), rectified, smoothed with a Gaussian (SD of 15 ms) and averaged. [@churchlandNeuralVariabilityPremotor2006] -->

## EMG Analyses

factor analysis + KF to match primate BMI work, but no need to do this

biggest question is how to design a task that asks the subject to explore the space of possible EMG activity

then we might ask someone to learn low-variance modes



EMG is not actually gaussian, but super-gaussian [@nazarpourNoteProbabilityDistribution2013]

some work using bayesian filtering methods to infer the signal envelope [@sangerBayesianFilteringMyoelectric2007]

Farina paper on EMG as convolution 

A window of EMG of length $T$ samples can be modeled as a convolution

$$
\mathbf{z} = \sum_t^T \mathbf{h} * \mathbf{s}
$$

where $\mathbf{h}$ is a motor unit activation template, which itself is a particular neural spike waveform, and $\mathbf{s}$ is the incidence of a spike, which might be modeled as a point process. 




We need more advanced EMG analyses in the task setting
  - autoencoders (farina paper) [@vujaklijaOnlineMappingEMG2018] 
  - bayesian inference techniques bespoke for EMG signals -- pull out control modes
    - choosing different aspects of the data model for inference
      - what kind of priors for tunings, latent space, prior over latent states, tuning models, and noise models. These choices depend on our intutions and requirements for the type of latents we wish to infer from the EMG data, as well as an analysis of the noise characteristics in our data, being careful not to attribute structured variability to unstructured noise.
      - we would need some kind of round truth? a different experiment...
  
- estimating kurtosis might be useful for inference [@nazarpourNoteProbabilityDistribution2013]
  - claims that higher order statistics may improve inference as EMG distribution as for low contration levels the distribution is far from gaussian, though it tends to a Gaussian as more motor units are recruited. This may influence the our choice of noise model for simulations if we wish to make predictions in EMG space.
  
- Sanger assumes a Laplacian distribution but this is only for a single channel, no work on multidimensional time series inference for EM, applying methods from neural data analysis would be an advancement [@sangerBayesianFilteringMyoelectric2007]



Another direction for analysis is to study long-range correlations in EMG data within and across trials through empirical correlation functions[@crevecoeurGoldstandardApproachAddress2010]. This work may inform features of models which attempt to recover aspects of trial-to-trial learning.




## Task Design

better techniques for developing mappings... maybe our task reaching task will do fine? Then why do we need 64 electrodes? Can we make a 64-dimensional task? tried the dot task already...

First completing a methodsy style piece of owrk about the setup, illlustrating the generation of bespoke control strategies by careful tracking of the EMG modes relative to task performance. nail down simple task to stabilize closed-loop analysis and processing methods for scaling up data collection-- a pure learning task to generate a large dataset around, investigating the complexity of EMG signal across learning, system id and control learning. settle on emg mapping protocol and online data filtering / analysis to start longer term task experiments
do pilot study over many sessions to test regularization models
Develop a series of experiments and scale up data collection across a range of tasks

## Data Collection at Scale

Scale up data collection with more subjects across many days

Investigate inter-subject variability -- we expect it will be high, but prior work shows individual strategies for movement [@crouzierIndividualDifferencesDistribution2019

## Modeling Control

We developed a Python implementation of the basic optimal feedback control framework, and this library will be expanded to include variants of the basic model. One relevant aspect of the basic optimal feedback control model is that the optimal controller that arises from specifying a quadratic state and control cost is invariant to the target state. In order to construct an optimal feedback controller 

The question is: when would you need composition? When would you need to learn a new controller? internalize multiple controllers?

more elaborate models for control with multiple targets, target uncertainty, noise models

- stochastic optimal control model comparisons
  - cost models 
  - perturbations in goal
  - go-before you know / goal uncertainty 
  - noise perturbations -- do reponses match the models?

- dynamics model fitting
  - internal model uncertainty 
  - modeled with robust optimal control? 

Then, Think of perturbations of these tasks: noise, goal, dynamics -- compare to optimal estimators and controllers. work towards. test the influence of reward on learning, whether subjects can learn through reinforcement alone [@vanderkooijLearningReachTrajectory2021]
analyze this data against control models?

Then formalize more elaborate task designs which link with our theoretical interests dealing with multiple controllers, composition, transfer. These might include go-before-you-know style tasks, goal uncertainty, controller composition and arbitration based on estimation and prediction [@gallivanParallelSpecificationCompeting2016]

constructing control from primitives for transfer (GPS, KL-control) 
stochastic control vs. robust control vs. adaptive control

(task reads out from D muscles, find modes of that data; do PCA to get K < D dimensions, controller only responds to motion in those K directions)—does behavior + motor activity follow LQR? this question has already been asked, but it hasn’t been asked for this kind of high-to-low dim mapping. It’s been asked in tasks where muscles haven’t been directly in control (Valero-Cuevas 2009). 

Todorov: do a task, look at muscle signal. Muscles that aren’t necessary for task have higher variability b/c they’re not being optimized for task (but does’t introduce perturbations). Also see Loeb (2012) for a negative result saying that muscle coordination is habitual rather than optimal, but it has issues (low # muscles). Can we replicate previous reaching optimality results in our set-up? What’s unique about our set-up is the PCA/dimensionality reduction in muscle activity space. This is important because you can create arbitrary muscle-cursor mappings, so you have to learn a new skill/mapping. This is different than perturbing a fundamental movement and forcing adaptation, which is what has been previously done. For our task, the participants actually have to learn a new task/mapping, rather than just do what they already know and be robust to perturbations. We test the LQR hypothesis once they’ve learned the task, because LQR isn’t a learning theory, it’s a theory about optimal control. We can see if, once people learn a new skill, their behavior is optimal wrt LQR theory. If we establish this, then we can think about how this LQR model is actually learned (enter RL).

## Modeling Learning

How do we adapt optimal control trial to trial?

<!-- gradient descent stuff -->

Next steps:

- Gain a better understanding of the loss landscape, including it's degeneracy. It may be possible to compute the optimum analytically.
- Corrupt the $A$ matrix in a more principled way, working to alter the passive dynamics in a physically realistic manner.
- Explore the action of the resulting gradient through it's eigenvalues and vectors. This can be done in two dimensions as a starting point.
- Compute second-order derivatives and work towards a Newton's method. 
- Compute derivatives with respect to the control law $K$ as a comparison. 
- Analyze results of the routine in comparison with the reaching adaptation literature.
- Think more about subspaces 
  - preparatory activity in one subspace, online control in another? 
  - learning in one subspace but not another?
  - compression of model to a subspace?

learning system dynamics 

Next is to work on models of learning by extending the framework of OFC through additions of composition and error-based adaptation.

nail down from data what is changing over trial

explore connections between spectral analysis perspective of optimal control and empirical correlation functions from data
make the connection between control and dynamics in model and experiment more tightly integrated.

learning control over trials
learning control via reward (RL) [@vanderkooijLearningReachTrajectory2021]

## Eye Tracking

Active learning, perception + action 

Track pupil and gaze correlates across learning, 

## Open Questions

The following questions need answers, to make progress we must form hypotheses around the most pressing of these questions and design experiments to test these hypotheses.

- how do we adapt LQR controllers trial-to-trial?
- how do we use existing controllers to construct movements?
- how do we construct controllers under dynamical and goal uncertainty?


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


- In a behavioral experiment, how can you disentangle system identification/estimation and control? Is suboptimality due to one or the other?
- How does the observation mapping relate to the latent state covariance? The task state covariance?
- How do we formalize this into a probabilistic graphical model? Why would we?
    - Would this make it easier to reason about what the goals are?
    - Would learning $M$ become an inference problem?
    - Would solving the control problem become an inference problem...?
- What noise assumptions can we make? Can we not make?
    - How can we incorporate signal-dependent noise?
