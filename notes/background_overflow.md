1. System Identification: learning a transition function $p(y_t|x_t, u_t)$
- How do you learn the unknown observation model from data?

1. Policy Optimization
- Once dynamics are learned (or at least stable?), how do we form a policy that is generalizable to new tasks under these dynamics?
- This is the control problem.

It's safe to assume that these processes are happening in parallel. Because we have complete and arbitrary control over the observation mapping, we can ask the subject to interact through a  dynamic that is intuitive (informative prior) or unintuitive (uninformative or inhibitive prior). Each scenario, we hypothesize, will elicit different strategies for learning and control.


-- 



% OFC is the best we got for motor coordination, but there's no adaptation or learning

% The control setup writes a cost, environment has some dynamics. 

% What is changing in this scenario?
% What is being learned?
% What information is used to do this learning?

% Which model variables correspond to muscles? Movements?
% What does the resultant feedback controller compute? How does this relate to cognition?

% This model is lacking in ... 

% 

% ### nonlinear iLQG models

% these are more predictive if we're actually using reaches experimentally

% nagengast, braun, etc 2009
% https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000419


% ### Noise in OFC

% - Nagengast 2010 https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000857 -- subjects are risk averse in the face of noise. 



--


% From the physiology, we see that the motor system is highly distributed and constructs action based on a variety of state dependence. The theoretical question becomes *when does it make computational sense to construct action by composing control policies rather than selecting or tuning a single policy?* When is policy arbitration computationally advantageous?

% **The motor learning field does not yet possess an adequate computational model for practice-induced increases in motor acuity.** (Krakauer Motor Learning 2019)

%  Since the value function represents cost-to-go, it would be sensible to move down this landscape as quickly as possible. Indeed, is in the direction of steepest descent of the value function. However, not all directions are possible to achieve in state-space. represents precisely the projection of the steepest descent onto the control space, and is the steepest descent achievable with the control inputs . Finally, the pre-scaling by the matrix biases the direction of descent to account for relative weightings that we have placed on the different control inputs. Note that although this interpretation is straight-forward, the slope that we are descending (in the value function, ) is a complicated function of the dynamics and cost. (Tedrake http://underactuated.mit.edu/lqr.html)

%  A solution to the algebraic Riccati equation can be obtained by matrix factorizations or by iterating on the Riccati equation. One type of iteration can be obtained in the discrete time case by using the dynamic Riccati equation that arises in the finite-horizon problem: in the latter type of problem each iteration of the value of the matrix is relevant for optimal choice at each period that is a finite distance in time from a final time period, and if it is iterated infinitely far back in time it converges to the specific matrix that is relevant for optimal choice an infinite length of time prior to a final period—that is, for when there is an infinite horizon.  wiki riccati equation

%  The unknown mapping $M$ from muscle to task space looks like the observation matrix $H$ in the LQG probl

% \begin{align*}
% y_t &= Hx_t + v_t\,\,\,(\mathrm{LQG}) \\
% y_t &= Mx_t + v_t. \,\,\,(\mathrm{experiment})
% \end{align*}

% The state dynamics in the task are of the form:

% \begin{align*}
% x_{t} &= Ax_{t-1} + Bu_{t-1} + w_{t-1} \,\,\,(\mathrm{LQG}) \\
% x_t &= Dx_{t-1} + Iu_{t-1} + w_{t-1} \,\,\,(\mathrm{experiment})
% \end{align*}

% where $D$ is a diagonal decay matrix of with terms $\mathrm{e}^{-\lambda}$ and $I$ is the identity. The subject produces muscle contractions which add to the current latent (unobserved) state. In the absence of control signals, the state decays back to $0$ in line with the physics of your arm returning to a passive state in the absence of muscle contractions. The terms $w$ and $v$ are gaussian noise vectors with distributions $\mathcal{N}(0,Q)$ and $\mathcal{N}(0,R)$. If we combine the transition and observation models:

% \begin{align*}
% y_t &= MDx_{t-1} + Mu_{t-1} + Mw_{t-1} + v_t \\
% &= A^\prime x_{t-1} + B^\prime u_{t-1} + Mw_{t-1} + v_t.
% \end{align*}

% We can think of this as the combined system identification problem where $A^\prime=MD$ and $B^\prime=M$ are unknown and must be estimated. The noise covariances of this altered system are now non-trivial, however. We could also assume that the transition dynamic $D$ is known and that the identification problem is learning the mapping $M$ only. This might not be a poor assumption since the exponential decay is meant to serve as an intuitive passive dynamic.

% In each trial of the task, a subject will have some internal representation of the observation dynamic $M$ which may or may not be accurate. In order to make accurate predictions, $M$ must be estimated.

% Learning linear dynamical systems from data is a hot topic of research, most of which seems to focus on learning in the context of complete state observation ($M=I$, $y=x$). Algorithms to determine parameters of $A$ and $B$ are proposed (see Dean, Recht 2018).

% From LQG theory we know that the control law is a linear function of the state:

% \begin{align*}
% u_t = -L_tx_t
% \end{align*}

% and thus our combined system dynamic is:

% \begin{align*}
% y_t &= M(D-L_t)x_{t-1} + Mw_{t-1} + v_t.
% \end{align*}


% The noise covariance due to the observation Q is unchanged, but the new noise covariance for the latent process is now $MRM^T$. This may make things difficult. 





-- 

info bottleneck

- We can use this framework to distinguish between skill learning (increasing policy complexity) and adaptation (no change in policy complexity).
- In sensorimotor control, 'compression' may be more about being sloppy on the sensory end of things, rather than having a compact policy to store and retrieve.

> The hierarchical organization typical of earlier sensory areas is not adhered to everywhere. On the contrary, the anatomy of associative areas and prefrontal  cortex suggests a more "democratic"  organization, and  processing  appears to take place  in webs of strongly interacting networks (8). Decisions to act and the execution of plans and  choices  could be the outcome of a  system with  distributed control rather than  a single control center. Coming to grips  with systems having distributed control will require both new experimental techniques and new  conceptual advances. Perhaps more  appropriate  metaphors for this  type of processing will emerge from studying  models of interacting  networks of neurons.  (sejnowskiPerspectivesCognitiveNeuroscience1988)

Stephen Scott review \cite{scottOptimalFeedbackControl2004} look at the bullet points there, relate to our experiment:

\subsubsection{nonlinear iLQG models}\label{nonlinear-ilqg-models}

% these are more predictive if we're actually using reaches experimentally

% nagengast, braun, etc 2009
% https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000419

\subsubsection{Noise in OFC}\label{noise-in-ofc}

% \begin{itemize}
% \tightlist
% \item
%   Nagengast 2010
%   https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000857
%   -- subjects are risk averse in the face of noise.
% \end{itemize}




Adaptive control?

% Have to be careful about what is termed corrective, adaptive, and learned.

% \begin{quote}
% Mathematically, we can formalize an adaptive control problem as a mapping x t+1 = F(x t , u t , a) with unknown system parameters a that have to be estimated simultaneously with the control process (Sastry and Bodson, 1989; Åström and Wittenmark, 1995). (Braun 2009\ldots{} Wolpert)
% \end{quote}

% \begin{quote}
% In the following we will refer to changes in the control policy that occur within individual movements as ``adaptation'' to distinguish them from ``learning'' processes that improve these adaptive responses across trials. (Braun 2009\ldots{} Wolpert)
% \end{quote}

% \begin{quote}
% Online correction is, for example, required in the case of an unpredicted target jump. Under this condition the same controller can be used, i.e., the mapping from sensory input to motor output is unaltered. However, unexpectedly changing the hand--cursor relation (e.g., by a visuomotor rotation) requires the computation of adaptive control policies.
% \end{quote}

% \begin{quote}
% Strictly speaking, an adaptive control problem is a nonlinear control problem with a hyper-state containing state variables and (unknown) parameters. This means in principle no extra theory of adaptive control is required. In practice, however, there is a well established theory of adaptive control (Sastry and Bodson, 1989; Åström and Wittenmark, 1995) that is built on the (somewhat artificial) distinction between state variables and (unknown) parameters. The two quantities are typically distinct in their properties. In general, the state, for example the position and velocity of the hand, changes rapidly and continuously within a movement. In contrast, other key quantities change discretely, like the identity of a manipulated object, or on a slower timescale, like the mass of the limb. \end{quote}

% We're really interested here in the learning problem! And how we can test and model this within the framework of OFC.



\subsubsection{State-space Models of Motor Adaptation}\label{state-space-models-of-motor-adaptation}

% \emph{Modeling Sensorimotor Learning with Linear Dynamical Systems} by
% Cheng and Sabes, 2006. The goal is to model trial-by-trial learning by
% fitting data to a linear dynamical system model. Here we'll call \(F_t\)
% the \textbf{sensorimotor mapping} transforming inputs \(w_t\) to \(y_t\)
% outputs per trial:

% \[
% y_t = F_t(w_t, \gamma_t).
% \]

% This can be thought of as a mapping from inputs within a single trial
% to, for example, endpoint error. Noise is captured by the \(\gamma_t\).
% The trajectory in \(F\) space attempts to capture the process of
% learning. The learning rule \(L_t\) can be written

% \[F_{t+1} = L_t\left(\left\{F_\tau\right\}_{\tau=1}^{t}, u_t, \eta_t, t\right)\]

% where \(\left\{F_\tau\right\}_{\tau=1}^{t}\) is the history of the
% mapping, \(u_t\) is the history of the total inputs to learning which
% could encompass \(y\), \(w\), and exogenous inputs \(r\). Noise in the
% learning is captured by \(\eta\).

% We can approximate this learning problem using linear equations by
% assuming that \(L_t=L \ \forall \ t\) is stationary, \(F_t\) is
% parameterized by \(x_t\in\mathbb{R}^y\). Thus,

% \[
% \begin{aligned}
% y_t &= F(x_t, w_t, \gamma_t) \\
% x_{t+1} &= L(x_t, u_t, \eta_t).
% \end{aligned}
% \]

% The trial-to-trial input-output mapping \(F\) is now fixed, and is
% transformed by trial through its parameters \(x_t\) by \(L\). Note that
% both mappings are Markovian and there are two input vectors, one for
% within-trial and one between-trial. These can include overlap. We can
% now linearize these mappings around an equilibrium point:

% \[
% \begin{aligned}
% x_{t+1} - x_e &= A(x_t-x_e) + B(u_t-u_e) + \eta_t \\
% y_t - m_e &= C(x_t-x_e) + D(w_t-w_e) + \gamma_t
% \end{aligned}
% \]

% As shown by Cheng and Sabes, we can bundle the equilibrium terms into a
% bias term and drop this term if we mean-subtract our data
% (\(x_t, y_t, u_t, w_t\)) when it's time to fit. This gives us a simple
% linear dynamical system:

% \[
% \begin{aligned}
% x_{t+1} &= Ax_t + Bu_t + \eta_t \\
% y_t &= Cx_t + Dw_t + \gamma_t.
% \end{aligned}
% \]

% The first equation governs the evolution of parameters of the
% within-trial input-output mapping, while the second equation governs the
% trial output given the current within-trial mapping parameters \(x_t\)
% and learning inputs \(w_t\). The parameters \(x_t\) are hidden variables
% that are only observed through the output \(y_t\). The noise terms
% \(\eta_t\) and \(\gamma_t\) are normally distributed with covariances
% \(Q\) and \(R\), respectively. \(A\) governs the passive trajectory of
% \(x_t\). If \(A=\mathbb{I}\), \(x_t\) does not decay passively.

% There is a general form for this model which separates endogenous input
% \(y_t\) from exogenous input \(r_t\)

% \[
% \begin{aligned}
% x_{t+1} &= Ax_t + [G \ H][r_t \ y_t]^T + \eta_t \\
% y_t &= Cx_t + Dw_t + \gamma_t
% \end{aligned}
% \]

% where \(H\) governs biases in directions of the outputs. A unbiased
% output is isotropic. To add explicit stationary bias we write

% \[
% \begin{aligned}
% x_{t+1} &= Ax_t + Gr_t + Hy_t - Hb_x + \eta_t.
% \end{aligned}
% \]



\subsubsection{Example Models}\label{example-models}

% \paragraph{Feedback Error Learning}\label{feedback-error-learning}

% \[x_t+1 = Ax_t + [H\ H][-y_t^*\ y_t]^T\]

% The second term is simply the difference between the output \(y_t\) and
% the desired output \(y_t^*\).

% \paragraph{Prediction Error Learning}\label{prediction-error-learning}

% Let \(u_t = y_t - \hat{y}_t\) where \(\hat{y}_t\), the difference
% between the output and the predicted output such that

% \(\hat{y}_t = Cx_t + Dw_t\). Thus,\(\hat{y}_t\) is a kind of forward
% model. Plugging in,

% \[x_{t+1} = Ax_t + Bu_t + \eta_t\]

% becomes

% \[
% \begin{aligned}
% x_{t+1} &= Ax_t + B(y_t - Cx_t - Dw_t) + \eta_t \\
% x_{t+1} &= (A-BC)x_t + By_t - BDw_t + \eta_t
% \end{aligned}
% \]

% \paragraph{Target Prediction Error
% Learning}\label{target-prediction-error-learning}

% Now let \(u_t = \hat{y}_t - y^*_t\), the difference between predicted
% output and target output.

% \[
% \begin{aligned}
% x_{t+1} &= Ax_t + B(Cx_t + Dw_t - y^*_t) + \eta_t \\
% x_{t+1} &= (A+BC)x_t + BDw_t - By^*_t + \eta_t
% \end{aligned}
% \]

% \paragraph{Steady State}\label{steady-state}

% If we take the output and state vectors in expectation for constant
% inputs \(w\) and \(r\), we have

% \[
% \begin{aligned}
% y_\infty &= \lim_{t\to\infty}\mathbb{E}\left[Cx_\infty + Dw\right] \\
% x_\infty &= \lim_{t\to\infty}\mathbb{E}\left[Ax_\infty + Bu\right] \\
% &= Ax_\infty + Gr + Hy_\infty \\
% &= Ax_\infty + Gr + HCx_\infty + HDw \\
% -(A + HC - \mathbb{I})x_\infty &= HDw + Gr.
% \end{aligned}
% \]

% Thus, the eigenvalues of \(A + HC\) must be less than or equal to 1 for
% \(x_\infty\) to be stable in expectation.

\subsubsection{Critique}\label{critique}

% \begin{quote}
% It should be emphasized, however, that these models are not intended to
% provide a mechanistic explanation of adaptation---they do not explain
% why adaptation has the properties it does. They explain neither why
% compensation for a perturbation decays, nor why people learn at the rate
% they do. However, these models do encapsulate a set of simple
% assumptions about how learning might occur on a single-trial timescale,
% and allow us to predict behavior in response to sustained or fluctuating
% perturbations over many trials. (Krakauer)
% \end{quote}

% \begin{quote}
% {[}Bayesian theories of learning{]} hold that adaptation is essentially
% a problem of estimating the properties of the imposed perturbation,
% given uncertainty about sensory feedback and the state of the world.
% Mathematically, under certain assumptions (that the noise/variability is
% Gaussian in both cases), this Bayesian estimation framework becomes
% equivalent to a Kalman filter (219)---a common algorithm for optimally
% tracking dynamic states under noisy observations--- which is almost
% identical to a state-space model. (Krakauer)
% \end{quote}

\subsection{Two-rate models}\label{two-rate-models}

% \[
% \begin{aligned}
% X_{t+1} &= X^{s}_{t} + X^f_t \\
% X^s_{t+1} &= L_s \cdot e_t + R_s \cdot X^s_{t} \\
% X^f_{t+1} &= L_f \cdot e_t + R_f \cdot X^f_{t} \\
% \end{aligned}
% \]

% where we fit \(L_i and R_i\), the learning rate and retention
% parameters. (shadmehr 2006)

% \begin{quote}
% Observations have revealed that there is far more to how participants compensate for an imposed perturbation than just implicit recalibration of a pre-existing motor controller. Instead, multiple, qualitatively different processes occur during adaptation tasks; for example, processes driven by explicit, cognitive strategies. When it comes to studying implicit recalibration, these other processes can be a contaminant. At the same time, however, these additional processes likely reflect the involvement of similar mechanisms to those responsible for more general motor skill learning. (Krakauer 2019 Motor Learning Review)
% \end{quote}

% \begin{quote}
% it is unlikely that the underlying components that contribute to
% learning in adaptation paradigms only differ in terms of their learning
% and retention rates, as the two-state model suggests. The multiple
% components of learning instead correspond to entirely distinct learning
% processes that are simultaneously brought to bear on the same problem.
% (Krakauer 2019 Motor Learning Review)
% \end{quote}

% %  Since the value function represents cost-to-go, it would be sensible to move down this landscape as quickly as possible. Indeed, is in the direction of steepest descent of the value function. However, not all directions are possible to achieve in state-space. represents precisely the projection of the steepest descent onto the control space, and is the steepest descent achievable with the control inputs . Finally, the pre-scaling by the matrix biases the direction of descent to account for relative weightings that we have placed on the different control inputs. Note that although this interpretation is straight-forward, the slope that we are descending (in the value function, ) is a complicated function of the dynamics and cost. (Tedrake http://underactuated.mit.edu/lqr.html)

% %  A solution to the algebraic Riccati equation can be obtained by matrix factorizations or by iterating on the Riccati equation. One type of iteration can be obtained in the discrete time case by using the dynamic Riccati equation that arises in the finite-horizon problem: in the latter type of problem each iteration of the value of the matrix is relevant for optimal choice at each period that is a finite distance in time from a final time period, and if it is iterated infinitely far back in time it converges to the specific matrix that is relevant for optimal choice an infinite length of time prior to a final period—that is, for when there is an infinite horizon.  wiki riccati equation

% %  The unknown mapping $M$ from muscle to task space looks like the observation matrix $H$ in the LQG probl

% % \begin{align*}
% % y_t &= Hx_t + v_t\,\,\,(\mathrm{LQG}) \\
% % y_t &= Mx_t + v_t. \,\,\,(\mathrm{experiment})
% % \end{align*}

% % The state dynamics in the task are of the form:

% % \begin{align*}
% % x_{t} &= Ax_{t-1} + Bu_{t-1} + w_{t-1} \,\,\,(\mathrm{LQG}) \\
% % x_t &= Dx_{t-1} + Iu_{t-1} + w_{t-1} \,\,\,(\mathrm{experiment})
% % \end{align*}

% % where $D$ is a diagonal decay matrix of with terms $\mathrm{e}^{-\lambda}$ and $I$ is the identity. The subject produces muscle contractions which add to the current latent (unobserved) state. In the absence of control signals, the state decays back to $0$ in line with the physics of your arm returning to a passive state in the absence of muscle contractions. The terms $w$ and $v$ are gaussian noise vectors with distributions $\mathcal{N}(0,Q)$ and $\mathcal{N}(0,R)$. If we combine the transition and observation models:

% % \begin{align*}
% % y_t &= MDx_{t-1} + Mu_{t-1} + Mw_{t-1} + v_t \\
% % &= A^\prime x_{t-1} + B^\prime u_{t-1} + Mw_{t-1} + v_t.
% % \end{align*}

% % We can think of this as the combined system identification problem where $A^\prime=MD$ and $B^\prime=M$ are unknown and must be estimated. The noise covariances of this altered system are now non-trivial, however. We could also assume that the transition dynamic $D$ is known and that the identification problem is learning the mapping $M$ only. This might not be a poor assumption since the exponential decay is meant to serve as an intuitive passive dynamic.

% % In each trial of the task, a subject will have some internal representation of the observation dynamic $M$ which may or may not be accurate. In order to make accurate predictions, $M$ must be estimated.

% % Learning linear dynamical systems from data is a hot topic of research, most of which seems to focus on learning in the context of complete state observation ($M=I$, $y=x$). Algorithms to determine parameters of $A$ and $B$ are proposed (see Dean, Recht 2018).

% % From LQG theory we know that the control law is a linear function of the state:

% % \begin{align*}
% % u_t = -L_tx_t
% % \end{align*}

% % and thus our combined system dynamic is:

% % \begin{align*}
% % y_t &= M(D-L_t)x_{t-1} + Mw_{t-1} + v_t.
% % \end{align*}


% % The noise covariance due to the observation Q is unchanged, but the new noise covariance for the latent process is now $MRM^T$. This may make things difficult. 




% \section{Mathematical Theories of Motor Control and Learning}
  
%   What are ``normative models''?
  
%   \begin{quote}
%   Normative models suggest that the nervous system optimally adapts when
%   faced with an error. To determine this optimal adaptation, the normative
%   model must specify two key features of the world. First, how different
%   factors, such as tools or levels of fatigue, influence the motor system
%   --- the so-called generative model. Second, how these factors are likely
%   to vary over both space and time --- that is the prior distribution. The
%   structure of the generative model and the prior distribution together
%   determine how the motor system should attribute an error to the
%   underlying causes and, therefore, how it should adapt.
%   {[}@wolpertPrinciplesSensorimotorLearning2011{]}
%   \end{quote}
  
%   \$include includes/ofc.md
  
%   <!-- OFC MODELING AND DISCUSSION -->
%   $include includes/ofc.md
  
%   <!-- MODEL ADAPTATION VIA GRADIENT DESCENT -->
%   $include includes/model_adaptation.md
  
  
%   <!-- 
  
%   adaptive is within trial, as you move
%   episodic has endless access to a simulator
  
%   ## List of variants, etc 
  
%   - LQR + SDN
%   - robust control (?)
%   - KL-control + composition
%   - game theoretic control-- compare solutions

  
%   ## Policy Selection
  
%   each timestep you combine actions from component policies to choose an action
  
%   Here we'll review and discuss models of action selection and policy composition as a means of theorizing about how subjects learn novel skills. 
  
%   In a sense, we're setting up several different directions for our understanding of composition and action selection which can be experimentally tested. 
  
%   We have a direct selection algorithm, composition through policy addition, and composition through policy multiplication. 
  
  
%   ### KL-control Composition (1 day)
  
%   This setup is particular subset of OFC problems. 
  
%   Dynamics
%   Cost
  
%   Composable policies
  
%   PLOT OF INTUITIVE EXAMPLE
  
%   ### Multiplicative Policy Composition
  
%   Policies are distributionally weighted, as opposed to chosen each timestep? 
  
%   ### Temporal Composition
  
%   there is a spectrum of latency in the feedback response
  
%   can different controllers be used for different latencies, and adjusted accordingly?
  
%   ### Generalized Policy Selection (1 day)
  
%   This is in the MDP case
  
%   Learning happens in several ways-- reward regression, Q-learning
  
%   What are rewards? 
%   What are tasks?
%   What are actions?
  
%   Is GPI with LQRs / LQR-RL a good model for motor learning? Define a model and see if it recapitulates known motor learning phenomena on existing experiments + accounts for things that previous models don’t. (Similar in spirit to Geerts et al. (2020)). Can this model track the higher-order statistics of trajectories during motor learning?
  
%   ### Model-based Reinforcement Learning
  
%   Since we only have an approximate model of the system dynamic, we could simply work towards an optimal policy directly using gradient derivative-free optimization methods in a model-free approach. Since we have good evidence that humans leverage internal models to make decisions (at least in a motor problem domain), we need to define an algorithm which uses past observations and controls to update our approximation for the system dynamic. Here is a very general algorithm:
  
%   0. Define a base policy/controller and base system model ($L_0$ and $\hat{M}_0$)
%   1. Collect samples (by interacting with the true environment $M_{true}$) using the current policy/controller (collect $y_t,u_t,y_{t+1}$ triples using $L_i$ for $i \in \{0\dots N\}$
%   2. Use sample(s) / trajectories to update current system dynamical model $\hat{M}_i$
%   3. Update current policy/controller $L_i$ (using the system dynamics or using a direct policy method)
  
%   If the true system dynamics were known, we could solve the Algebraic Riccati Equation with a backwards pass, and compute our controls in a forward pass. This general algorithm structure highlights how the (unknown) system identification and controller design are intertwined: identifying a system appropriately must rely on sampling and fitting regions of the state space pertinent to adequate control in terms of cost (Ross ICML 2012). Otherwise, our approximation to the true system dynamic will only produce a valid controller in regions we have previously explored. The question is how we can effectively (sample and time efficiently) utilize new state transitions we encounter either online as feedback or between trials to update our model and policy. That is, the number of trials and/or trajectories to use before updating either the system model and/or policy is an important parameter.
  
%   In the LQG setting, this might be called "adaptive LQG".
  
%   \$include includes/model\_adaptation.md
  
%   Learning LQR controllers
  
%   \begin{verbatim}
%   Q-learning for LQR
%   policy gradient for LQR
%   what is an LQR-SR? what does this help us do?
%   \end{verbatim}
  
%   where does LQR break? - goal shift (is this true?) - task shift
%   (different goal? this isn't true) - goal uncertainty (this can't be
%   modeled\ldots) - LQR variants break more easily?
  
%   where does KL-LQR / control break? - one policy at a time\ldots?
%   re-optimize your single policy per task? (task could have multiple
%   goals) - could have multiple possible (terminal) goal states - not
%   continuous -- code this up and understand it in continuous would be a
%   good result - selection is done beforehand\ldots{} can this shift
%   online\ldots? - allows you to construct more interesting
%   policies\ldots{} - can we connect this to KL between passive and
%   dynamic? change this to planned and replanned?
  
%   is there a multiplicative LQR composition? - sergey levine
%   multiplicative paper?









% ### State-space Models of Motor Adaptation

% *Modeling Sensorimotor Learning with Linear Dynamical Systems* by Cheng and Sabes, 2006. The goal is to model trial-by-trial learning by fitting data to a linear dynamical system model. Here we'll call $F_t$ the **sensorimotor mapping** transforming inputs $w_t$ to $y_t$ outputs per trial:

% $$
% y_t = F_t(w_t, \gamma_t).
% $$

% This can be thought of as a mapping from inputs within a single trial to, for example, endpoint error. Noise is captured by the $\gamma_t$. The trajectory in $F$ space attempts to capture the process of learning. The learning rule $L_t$ can be written

% $$F_{t+1} = L_t\left(\left\{F_\tau\right\}_{\tau=1}^{t}, u_t, \eta_t, t\right)$$

% where $\left\{F_\tau\right\}_{\tau=1}^{t}$ is the history of the mapping, $u_t$ is the history of the total inputs to learning which could encompass $y$, $w$, and exogenous inputs $r$. Noise in the learning is captured by $\eta$.

% We can approximate this learning problem using linear equations by assuming that $L_t=L \ \forall \ t$ is stationary, $F_t$ is parameterized by $x_t\in\mathbb{R}^y$. Thus,

% $$
% \begin{aligned}
% y_t &= F(x_t, w_t, \gamma_t) \\
% x_{t+1} &= L(x_t, u_t, \eta_t).
% \end{aligned}
% $$

% The trial-to-trial input-output mapping $F$ is now fixed, and is transformed by trial through its parameters $x_t$ by $L$. Note that both mappings are Markovian and there are two input vectors, one for within-trial and one between-trial. These can include overlap. We can now linearize these mappings around an equilibrium point:

% $$
% \begin{aligned}
% x_{t+1} - x_e &= A(x_t-x_e) + B(u_t-u_e) + \eta_t \\
% y_t - m_e &= C(x_t-x_e) + D(w_t-w_e) + \gamma_t
% \end{aligned}
% $$

% As shown by Cheng and Sabes, we can bundle the equilibrium terms into a bias term and drop this term if we mean-subtract our data ($x_t, y_t, u_t, w_t$) when it's time to fit. This gives us a simple linear dynamical system:

% $$
% \begin{aligned}
% x_{t+1} &= Ax_t + Bu_t + \eta_t \\
% y_t &= Cx_t + Dw_t + \gamma_t.
% \end{aligned}
% $$

% The first equation governs the evolution of parameters of the within-trial input-output mapping, while the second equation governs the trial output given the current within-trial mapping parameters $x_t$ and learning inputs $w_t$. The parameters $x_t$ are hidden variables that are only observed through the output $y_t$. The noise terms $\eta_t$ and $\gamma_t$ are normally distributed with covariances $Q$ and $R$, respectively. $A$ governs the passive trajectory of $x_t$. If $A=\mathbb{I}$, $x_t$ does not decay passively.

% There is a general form for this model which separates endogenous input $y_t$ from exogenous input $r_t$

% $$
% \begin{aligned}
% x_{t+1} &= Ax_t + [G \ H][r_t \ y_t]^T + \eta_t \\
% y_t &= Cx_t + Dw_t + \gamma_t
% \end{aligned}
% $$

% where $H$ governs biases in directions of the outputs. A unbiased output is isotropic. To add
% explicit stationary bias we write

% $$
% \begin{aligned}
% x_{t+1} &= Ax_t + Gr_t + Hy_t - Hb_x + \eta_t.
% \end{aligned}
% $$

% ### Example Models

% #### Feedback Error Learning

% $$x_t+1 = Ax_t + [H\ H][-y_t^*\ y_t]^T$$

% The second term is simply the difference between the output $y_t$ and the desired output $y_t^*$.

% #### Prediction Error Learning

% Let $u_t = y_t - \hat{y}_t$ where $\hat{y}_t$, the difference between the output and the predicted output such that

% $\hat{y}_t = Cx_t + Dw_t$. Thus,$\hat{y}_t$ is a kind of forward model. Plugging in,

% $$x_{t+1} = Ax_t + Bu_t + \eta_t$$

% becomes

% $$
% \begin{aligned}
% x_{t+1} &= Ax_t + B(y_t - Cx_t - Dw_t) + \eta_t \\
% x_{t+1} &= (A-BC)x_t + By_t - BDw_t + \eta_t
% \end{aligned}
% $$

% #### Target Prediction Error Learning

% Now let $u_t = \hat{y}_t - y^*_t$, the difference between predicted
% output and target output.

% $$
% \begin{aligned}
% x_{t+1} &= Ax_t + B(Cx_t + Dw_t - y^*_t) + \eta_t \\
% x_{t+1} &= (A+BC)x_t + BDw_t - By^*_t + \eta_t
% \end{aligned}
% $$

% #### Steady State

% If we take the output and state vectors in expectation for constant
% inputs $w$ and $r$, we have

% $$
% \begin{aligned}
% y_\infty &= \lim_{t\to\infty}\mathbb{E}\left[Cx_\infty + Dw\right] \\
% x_\infty &= \lim_{t\to\infty}\mathbb{E}\left[Ax_\infty + Bu\right] \\
% &= Ax_\infty + Gr + Hy_\infty \\
% &= Ax_\infty + Gr + HCx_\infty + HDw \\
% -(A + HC - \mathbb{I})x_\infty &= HDw + Gr.
% \end{aligned}
% $$

% Thus, the
% eigenvalues of $A + HC$ must be less than or equal to 1 for $x_\infty$
% to be stable in expectation.

% ### Critique

% > It should be emphasized, however, that these models are not intended to provide a mechanistic explanation of adaptation—they do not explain why adaptation has the properties it does. They explain neither why compensation for a perturbation decays, nor why people learn at the rate they do. However, these models do encapsulate a set of simple assumptions about how learning might occur on a single-trial timescale, and allow us to predict behavior in response to sustained or fluctuating perturbations over many trials. (Krakauer)

% > [Bayesian theories of learning] hold that adaptation is essentially a problem of estimating the properties of the imposed perturbation, given uncertainty about sensory feedback and the state of the world. Mathematically, under certain assumptions (that the noise/variability is Gaussian in both cases), this Bayesian estimation framework becomes equivalent to a Kalman filter (219)—a common algorithm for optimally tracking dynamic states under noisy observations— which is almost identical to a state-space model. (Krakauer)
