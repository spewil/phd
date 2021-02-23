# Background Theory{#sec:bg_theory}

**The motor learning field does not yet possess an adequate computational model for practice-induced increases in motor acuity.** (Krakauer Motor Learning 2019)

## Existing Models of Motor Control and Adaptation

### Optimal Feedback Control


<!-- The UCM is not a hard-and-fast principle, as nothing as in the motor system. Rather, as we've seen elsehwhere, there seems to be a spectrum of control. This could be explained through a composite cost function which penalizes deviations from prior movement strategies[@raczSpatiotemporalAnalysisReveals2013]. There is much research pushing back on optimal control, uncontrolled manifold hypothesis, and this will be addressed in {+@sec:experiment}. -->


<!-- Since the value function represents cost-to-go, it would be sensible to move down this landscape as quickly as possible. Indeed, is in the direction of steepest descent of the value function. However, not all directions are possible to achieve in state-space. represents precisely the projection of the steepest descent onto the control space, and is the steepest descent achievable with the control inputs . Finally, the pre-scaling by the matrix biases the direction of descent to account for relative weightings that we have placed on the different control inputs. Note that although this interpretation is straight-forward, the slope that we are descending (in the value function, ) is a complicated function of the dynamics and cost. (Tedrake http://underactuated.mit.edu/lqr.html)-->

<!-- A solution to the algebraic Riccati equation can be obtained by matrix factorizations or by iterating on the Riccati equation. One type of iteration can be obtained in the discrete time case by using the dynamic Riccati equation that arises in the finite-horizon problem: in the latter type of problem each iteration of the value of the matrix is relevant for optimal choice at each period that is a finite distance in time from a final time period, and if it is iterated infinitely far back in time it converges to the specific matrix that is relevant for optimal choice an infinite length of time prior to a final period—that is, for when there is an infinite horizon.  wiki riccati equation-->


OFC is the best we got for motor coordination, but there's no adaptation or learning

The control setup writes a cost, environment has some dynamics. 

What is changing in this scenario?
What is being learned?
What information is used to do this learning?

Which model variables correspond to muscles? Movements?
What does the resultant feedback controller compute? How does this relate to cognition?



This model is lacking in ... 

A key paper is `Valero-Cuevas 2009` which recording EMG from the seven muscles driving the finger in a force-feedback task. The authors found support for the "minimum intervention principle" [@Valero-Cuevas2009].


### Intuitive Example of the OFC framework

Here we see a feedback controller with three muscles such that we can plot the muscle activation trajectory.

This is the feedback controller K, we can understand it's action by plotting 

PLOT OF SIMPLE EXAMPLE 

PLOT OF APT DATA


### Error-based Adaptation

Error-based sdaption and state-space models have a great amount of precedent in the sensorimotor learning literature. We will summarize these models briefly and discuss our willingness to depart from them.

This is pretty much the best model we have that describe learning from error

Current models of motor learning 

x' = Ax + Bu 

This model describes...

The downsides of this model are that it describes a small aspect of our data.









## Motor Adaptation

Implicit / Explicit
Model-based / Model-free
Slow / Fast

Krakauer et al.'s categorization of motor learning places prior work into the following classes:
- Adaptation
- Sequence Learning
- De Novo Learning
- Motor Acuity
- Expertise

work in reaching
shadmehr, krakauer reviews



### State-space Models of Motor Adaptation

*Modeling Sensorimotor Learning with Linear Dynamical Systems* by Cheng and Sabes, 2006. The goal is to model trial-by-trial learning by fitting data to a linear dynamical system model. Here we'll call $F_t$ the **sensorimotor mapping** transforming inputs $w_t$ to $y_t$ outputs per trial:

$$
y_t = F_t(w_t, \gamma_t).
$$

This can be thought of as a mapping from inputs within a single trial to, for example, endpoint error. Noise is captured by the $\gamma_t$. The trajectory in $F$ space attempts to capture the process of learning. The learning rule $L_t$ can be written

$$F_{t+1} = L_t\left(\left\{F_\tau\right\}_{\tau=1}^{t}, u_t, \eta_t, t\right)$$

where $\left\{F_\tau\right\}_{\tau=1}^{t}$ is the history of the mapping, $u_t$ is the history of the total inputs to learning which could encompass $y$, $w$, and exogenous inputs $r$. Noise in the learning is captured by $\eta$.

We can approximate this learning problem using linear equations by assuming that $L_t=L \ \forall \ t$ is stationary, $F_t$ is parameterized by $x_t\in\mathbb{R}^y$. Thus,

$$
\begin{aligned}
y_t &= F(x_t, w_t, \gamma_t) \\
x_{t+1} &= L(x_t, u_t, \eta_t).
\end{aligned}
$$

The trial-to-trial input-output mapping $F$ is now fixed, and is transformed by trial through its parameters $x_t$ by $L$. Note that both mappings are Markovian and there are two input vectors, one for within-trial and one between-trial. These can include overlap. We can now linearize these mappings around an equilibrium point:

$$
\begin{aligned}
x_{t+1} - x_e &= A(x_t-x_e) + B(u_t-u_e) + \eta_t \\
y_t - m_e &= C(x_t-x_e) + D(w_t-w_e) + \gamma_t
\end{aligned}
$$

As shown by Cheng and Sabes, we can bundle the equilibrium terms into a bias term and drop this term if we mean-subtract our data ($x_t, y_t, u_t, w_t$) when it's time to fit. This gives us a simple linear dynamical system:

$$
\begin{aligned}
x_{t+1} &= Ax_t + Bu_t + \eta_t \\
y_t &= Cx_t + Dw_t + \gamma_t.
\end{aligned}
$$

The first equation governs the evolution of parameters of the within-trial input-output mapping, while the second equation governs the trial output given the current within-trial mapping parameters $x_t$ and learning inputs $w_t$. The parameters $x_t$ are hidden variables that are only observed through the output $y_t$. The noise terms $\eta_t$ and $\gamma_t$ are normally distributed with covariances $Q$ and $R$, respectively. $A$ governs the passive trajectory of $x_t$. If $A=\mathbb{I}$, $x_t$ does not decay passively.

There is a general form for this model which separates endogenous input $y_t$ from exogenous input $r_t$

$$
\begin{aligned}
x_{t+1} &= Ax_t + [G \ H][r_t \ y_t]^T + \eta_t \\
y_t &= Cx_t + Dw_t + \gamma_t
\end{aligned}
$$

where $H$ governs biases in directions of the outputs. A unbiased output is isotropic. To add
explicit stationary bias we write

$$
\begin{aligned}
x_{t+1} &= Ax_t + Gr_t + Hy_t - Hb_x + \eta_t.
\end{aligned}
$$

### Example Models

#### Feedback Error Learning

$$x_t+1 = Ax_t + [H\ H][-y_t^*\ y_t]^T$$

The second term is simply the difference between the output $y_t$ and the desired output $y_t^*$.

#### Prediction Error Learning

Let $u_t = y_t - \hat{y}_t$ where $\hat{y}_t$, the difference between the output and the predicted output such that

$\hat{y}_t = Cx_t + Dw_t$. Thus,$\hat{y}_t$ is a kind of forward model. Plugging in,

$$x_{t+1} = Ax_t + Bu_t + \eta_t$$

becomes

$$
\begin{aligned}
x_{t+1} &= Ax_t + B(y_t - Cx_t - Dw_t) + \eta_t \\
x_{t+1} &= (A-BC)x_t + By_t - BDw_t + \eta_t
\end{aligned}
$$

#### Target Prediction Error Learning

Now let $u_t = \hat{y}_t - y^*_t$, the difference between predicted
output and target output.

$$
\begin{aligned}
x_{t+1} &= Ax_t + B(Cx_t + Dw_t - y^*_t) + \eta_t \\
x_{t+1} &= (A+BC)x_t + BDw_t - By^*_t + \eta_t
\end{aligned}
$$

#### Steady State

If we take the output and state vectors in expectation for constant
inputs $w$ and $r$, we have

$$
\begin{aligned}
y_\infty &= \lim_{t\to\infty}\mathbb{E}\left[Cx_\infty + Dw\right] \\
x_\infty &= \lim_{t\to\infty}\mathbb{E}\left[Ax_\infty + Bu\right] \\
&= Ax_\infty + Gr + Hy_\infty \\
&= Ax_\infty + Gr + HCx_\infty + HDw \\
-(A + HC - \mathbb{I})x_\infty &= HDw + Gr.
\end{aligned}
$$

Thus, the
eigenvalues of $A + HC$ must be less than or equal to 1 for $x_\infty$
to be stable in expectation.

### Critique

> It should be emphasized, however, that these models are not intended to provide a mechanistic explanation of adaptation—they do not explain why adaptation has the properties it does. They explain neither why compensation for a perturbation decays, nor why people learn at the rate they do. However, these models do encapsulate a set of simple assumptions about how learning might occur on a single-trial timescale, and allow us to predict behavior in response to sustained or fluctuating perturbations over many trials. (Krakauer)

> [Bayesian theories of learning] hold that adaptation is essentially a problem of estimating the properties of the imposed perturbation, given uncertainty about sensory feedback and the state of the world. Mathematically, under certain assumptions (that the noise/variability is Gaussian in both cases), this Bayesian estimation framework becomes equivalent to a Kalman filter (219)—a common algorithm for optimally tracking dynamic states under noisy observations— which is almost identical to a state-space model. (Krakauer)


## Two-rate models

$$
\begin{aligned}
X_{t+1} &= X^{s}_{t} + X^f_t \\
X^s_{t+1} &= L_s \cdot e_t + R_s \cdot X^s_{t} \\
X^f_{t+1} &= L_f \cdot e_t + R_f \cdot X^f_{t} \\
\end{aligned}
$$

where we fit $L_i and R_i$, the learning rate and retention parameters. (shadmehr 2006)

> Observations have revealed that there is far more to how participants compensate for an imposed perturbation than just implicit recalibration of a pre-existing motor controller. Instead, multiple, qualitatively different processes occur during adaptation tasks; for example, processes driven by explicit, cognitive strategies. When it comes to studying implicit recalibration, these other processes can be a contaminant. At the same time, however, these additional processes likely reflect the involvement of similar mechanisms to those responsible for more general motor skill learning. (Krakauer 2019 Motor Learning Review)

> it is unlikely that the underlying components that contribute to learning in adaptation paradigms only differ in terms of their learning and retention rates, as the two-state model suggests. The multiple components of learning instead correspond to entirely distinct learning processes that are simultaneously brought to bear on the same problem. (Krakauer 2019 Motor Learning Review)