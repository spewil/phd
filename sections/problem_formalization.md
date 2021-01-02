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