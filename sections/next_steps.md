# Next Steps 

Big Things

First completing a methodsy style piece of owrk about the setup, illlustrating the generation of bespoke control strategies by careful tracking of the EMG modes relative to task performance. 

settle on emg mapping protocol and online data filtering / analysis to start longer term task experiments
do pilot study over many sessions to test regularization models 

Develop a series of experiments and scale up data collection across a range of tasks

analyze this data against control models?

Next is to work on models of learning by extending the framework of OFC through additions of composition and error-based adaptation.

test those models against data

## Data Collection at Scale

- scale up data collection with more subjects across many days
- intersubject differences


### Data Analysis

Our preliminary data confirms the working principle of the setup and highlights the next steps for producing a quality dataset. 


Address the noise concerns in the data -- better hardware, should be very low noise relative to our signal.


- more advanced EMG analyses in the task setting
  - autoencoders (farina paper) [@vujaklijaOnlineMappingEMG2018]
  - 
  - bayesian inference techniques bespoke for EMG signals -- pull out control modes
    - choosing different aspects of the data model for inference
      - what kind of priors for tunings, latent space, 
      - we would need some kind of round truth? a different experiment...
  - estimating kurtosis might be useful for inference [@nazarpourNoteProbabilityDistribution2013]
    - claims that higher order statistics may improve inference as EMG distribution as for low contration levels the distribution is far from gaussian, though it tends to a Gaussian as more motor units are recruited. This may influence the our choice of noise model for simulations if we wish to make predictions in EMG space.
  - Sanger assumes a Laplacian distribution [@sangerBayesianFilteringMyoelectric2007]

- better techniques for developing mappings

- long-range correlations in the data, correlation functions
  - [@crevecoeurGoldstandardApproachAddress2010]


- Dynamical modes in the data using dynamical systems analysis techniques




### Task Design


- formalize specific task designs which link with our theoretical interests

### Optimization

we want to stay close to models, testing them as we go
- optimization models (regularized regression) -- pure force learning
  - perturbations of this + predictions? mapping perturbation, noise perturbations

### Optimal Control

- stochastic optimal control model comparisons
  - cost models 
  - perturbations in goal
  - go-before you know / goal uncertainty 
  - noise perturbations -- do reponses match the models?

- dynamics model fitting
  - internal model uncertainty 
  - modeled with robust optimal control? 

stochastic control vs. robust control vs. adaptive control

learning control over trials
learning control via reward (RL) [@vanderkooijLearningReachTrajectory2021]
constructing control from primitives for transfer (GPS, KL-control) 

## Eye Tracking

Active learning, perception + action



## Open Questions

The following questions need answers, to make progress we must form hypotheses around the most pressing of these questions and design experiments to test these hypotheses.

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
