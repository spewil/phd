# Experimental Contributions {#sec:experiment}

<!-- I would be most interested to hear how u are thinking of approaching the analysis. I.e. u have a bunch of channels, movements, tasks what is the workflow to get from that raw data into something manageable/useful. -->

- shape of the data
- structure of variability in the EMG compared to the structure of variability in the behavior?


> we know how to design and interpret experiments that involve many repetitions of the same movement however there is limited role for online optimization in that context. instead we need experiments where subjects are required to come up with new movements all the time. how can we get experimenters to do such experiments? show cool movies of robots doing cool things,and hopefully get the experimenters excited. (todorov online optimization slides)


## Experimental Setup

My setup records EMG from the forearm.

The goal of the project’s first phase is to develop a high-dimensional surface EMG recording rig to generate datasets with high signal-to-noise ratio and dense coverage over superficial muscles of the arm and hand. The first question of this phase is: what are the limitations of a closed-loop myocontrol experiment, and how can such constraints be avoided or leveraged? To answer this question we will develop a signal processing pipeline and diagnostics suite to identify constraints in the setup and aim to overcome, as much as possible, the limitations inherent in surface EMG recording such as muscle crosstalk and rigorous electrode placement.

The concept of the experimental setup is shown in Figure 1, where 64 monopolar electrodes are attached to a subject’s arm and hand to record muscle activity. The arm and hand are kinematically constrained in a custom fixture and motor activity is recorded during isometric muscle contractions at levels less than 20\% maximum voluntary contraction to lessen the risk of involuntary co-contractions. The setup circumvents the limb biomechanics by mapping muscle output directly to virtual stimuli shown on a computer monitor. Additionally, our study focuses on low-force, isometric contractions to avoid complications due to artifacts in dynamic, high- force movements.

We chose 64 channels in order to have at least two electrodes per muscle implicated in control of the hand in the event that we require differential recording. This choice limits our analysis to the motor pool level. If our questions require recording at the motor unit level, we will need to move to a higher channel count system. Literature in this field typically use a much lower number of channels. We believe that using 64 electrodes will help develop a more complete picture of the superficial muscle activity of the arm and hand across learning. A diagram of muscles relevant to thee control of the hand and wrist is shown in Figure 2 on page 4. We are not aware of a rigorous study testing which muscles of the arm and hand can be accurately captured using surface EMG.

We aim to extend this prior work using learning algorithms that take into account time- varying dynamics of the signal in addition to common tools like components analysis and matrix factorization. This analysis will help generate an understanding of intersubject, intersession, and intertask variability. Both an analysis of dynamic correlations and a validation of dimensionality using EMG would be a novel contribution to the literature.

We anticipate that quantifying electrode placement and calibrating across sessions will be a major challenge. We aim to develop a mechanical fixture for recording as well as alignment tools to aid in placing electrodes in precisely the same location each session. Properly separating variability due to electrode placement from behavioral and physiological variability will be paramount to establish repeatability in our results. Once we have collected a naturalistic activity dataset, we can begin to design bespoke feedback mappings and perturbations, as discussed in Section .

![Prototype of recording hardware. Monopolar recording with reference electrode at the wrist.](images/hardware/setup.pdf)

Goal here is to use the linear dynamics environment to isolate the control strategies of the CNS under these constraints-- how does the CNS adapt to this environment? How does it construct solutions to control problems of various dimensionalities? How does it produce dexterous responses to perturbations of these solutions?






### Hardware

### etc

what experiments do we need to do?
experimental setup
i made a thing, it works like this, here's the data
- detail how this works
	- what are the constraints?
	- what perturbations can be achieved?
- prelim data from the rig
- figures of this data
- thoughts about how versions of the task
- hardware
- recording 64 channels of EMG from multiple muscles the arm and hand with realtime feedback
- in an isometric learning task
- software
- pictures n stuff





## Feature Extraction

We want features that are:
  - smooth; having low spatial frequency
  - equal in the variance that they capture; equally likely to exist in - future data
      - Perhaps use CCA to find N features that are maximally dissimilar?
      - Use ICA to find independent features?


The second question of this phase is: what is the manifold of activity in electrode space during natural hand use? To answer this question, we will record naturalistic activity by subjects completing a set protocol that covers the naturalistic space of electrode covariance. For comparison, we will record a dataset of naturalistic tasks using a separate, mobile setup with the same electrode placement pattern but without the isometric constraint. These datasets could be collected from a range subjects going throughout their daily tasks, or using a specific set of tasks in the laboratory such as handwriting and the use of various tools. Encouragingly, a recent review noted that “Similarly to the breakthroughs in understanding vision that followed the quantification of statistics of natural scenes, a clear description of the statistics of natural tasks might revolutionize our understanding of the neural basis of high-level learning and decision- making”[18].

By analyzing the structure of these naturalistic datasets, we can compute the dimensionality of naturalistic movement as a subspace within our electrode space, similar to work done using joint angles of the hand[24, 22, 11]. From this work we know that while the hand has 29 joints and is controlled by 34 muscles, the dimensionality of natural hand movements is closer to 8 in joint angle dimension space based on principle components analysis. This analysis will also help us determine the biomechanical constraints on hand output dimensionality. We hypothesize that this will be higher than 8 and lower than 23, which gives us a large task space to work with for generating learning tasks.



![Raw EMG data from a minimal finger flexion before preprocessing.](images/data_analysis/fingers/raw_data.pdf)

![Raw EMG data from a minimal finger flexion before preprocessing.](images/data_analysis/fingers/preprocessed_data.pdf)

![Raw EMG data from a minimal finger flexion before preprocessing.](images/data_analysis/fingers/PCA_variances.pdf)

![Raw EMG data from a minimal finger flexion before preprocessing.](images/data_analysis/fingers/PCA_components.pdf)






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

\begin{align*}
X &= W\cdot{H} \\
W^{-1}\cdot{X} &= {H} \\
W^{T}\cdot{X} &= {H}
\end{align*}

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

## Center Hold, Reach Out Task

In this task, the muscles of a subject's arm are recorded using 32 channels of surface EMG. This EMG vector is mapped to a 2D force acting on a point mass shown on the screen. The mapping $M\in\mathbb{R}^{2x32}$ maps 8 "columns" each consisting of 4 electrodes placed in a line down the length of the forearm each to one of 2D root of unity. Each column of electrodes is thus mapped to one of 8 two-dimensional forces. Additionally, the point mass has zero inertia and zero friction and as such displays a direct, though redundant, readout of the EMG signal. The task asks the subject to reach one of 32 equally spaced targets on each trial.

While there are 8 possible force vectors the subject can modulate by controlled the electrode activity on each of her 8 columns, the EMG mapping is ultimately a projection onto the 2D plane. Since the EMG signal is nonnegative, the subject could technically modulate just four modes of electrode activity, the minimum number needed to span the task space, to reach all 32 targets.

We can model the subject as selecting an EMG signal $x$ which minimizes the distance between a target position $b$ and the projection of the EMG signal through the mapping $M$ as well as minimizes the norm of $x$ in order to conserve metabolic energy. This optimization can be written as a regularized least squares problem:  

$$
\min_x\frac{1}{2}||Mx - b||^2_2 + \frac{\lambda}{2}||x||_2^2.
$$

This problem is known to have a unique minimum for $\lambda>0$ which is an approximation $Mx\approx b$ regardless of the shape or rank of $M$. This implies that the subject, if they are biophysically capable to do so, will learn distinct motor outputs for each target rather than reusing modes for multiple targets with different activation levels. That is the subject will, over time, learn to fractionate their muscle output to reach their goal in order to minimize effort. For instance, to reach the the target at position $(1,0)$ in Cartesian coordinates, the subject could activate a bespoke activity mode or activity the combination of two modes for targets at $\pm45^\circ$ from this central target. If this is the case, the model predicts that the dimensionality of the EMG signal will increase over the course of training as the subject learns to construct bespoke activity modes for each of the eight targets.

![Point mass position trajectories in two-dimensional task space during the center-hold, reach-out task with 8 targets spaced evenly around the unit circle. Training was conducted over 3 blocks each with 32 trials, 4 trials per target. The first block shows roughly four modes, the second block shows four modes more clearly, and the third blocks may show the beginnings of fractionation.](images/data_analysis/center_hold/trajectories.pdf)

![Raw EMG data from a minimal finger flexion before preprocessing.](images/data_analysis/center_hold/hit_fraction.pdf)

![Raw EMG data from a minimal finger flexion before preprocessing.](images/data_analysis/center_hold/PCA_trial_variance.pdf)

![Raw EMG data from a minimal finger flexion before preprocessing.](images/data_analysis/center_hold/PCA_concat_variance.pdf)


Preliminary data for this task, through the mapping: 

$$
\tilde{M} = \begin{bmatrix}M & M & M & M\end{bmatrix} \\
M =
\begin{bmatrix}
0  & 0.71  & 1   & 0.71   & 0  & -0.71  & -1  & -0.71 \\
1  & 0.71  & 0  & -0.71  & 1   & -0.71   & 0   & 0.71
\end{bmatrix}
$$

In this task, the subject's first goal is to interact through an unknown visuomotor mapping and internalize this model. The second problem is to use this model to solve a control problem.

1. System Identification -- learning a transition function $p(y_t|x_t, u_t)$
    - How do you learn the unknown observation model from data?

2. Policy Optimization
    - Once dynamics are learned (or at least stable?), how do we form a policy that is generalizable to new tasks under these dynamics?
    - This is the control problem.

It's safe to assume that these processes are happening in parallel. Because we have complete and arbitrary control over the observation mapping, we can ask the subject to interact through a  dynamic that is intuitive (informative prior) or unintuitive (uninformative or inhibitive prior). Each scenario, we hypothesize, will elicit different strategies for learning and control.

The unknown mapping $M$ from muscle to task space looks like the observation matrix $H$ in the LQG problem:

\begin{align*}
y_t &= Hx_t + v_t\,\,\,(\mathrm{LQG}) \\
y_t &= Mx_t + v_t. \,\,\,(\mathrm{experiment})
\end{align*}

The state dynamics in the task are of the form:

\begin{align*}
x_{t} &= Ax_{t-1} + Bu_{t-1} + w_{t-1} \,\,\,(\mathrm{LQG}) \\
x_t &= Dx_{t-1} + Iu_{t-1} + w_{t-1} \,\,\,(\mathrm{experiment})
\end{align*}

where $D$ is a diagonal decay matrix of with terms $\mathrm{e}^{-\lambda}$ and $I$ is the identity. The subject produces muscle contractions which add to the current latent (unobserved) state. In the absence of control signals, the state decays back to $0$ in line with the physics of your arm returning to a passive state in the absence of muscle contractions. The terms $w$ and $v$ are gaussian noise vectors with distributions $\mathcal{N}(0,Q)$ and $\mathcal{N}(0,R)$. If we combine the transition and observation models:

\begin{align*}
y_t &= MDx_{t-1} + Mu_{t-1} + Mw_{t-1} + v_t \\
&= A^\prime x_{t-1} + B^\prime u_{t-1} + Mw_{t-1} + v_t.
\end{align*}

We can think of this as the combined system identification problem where $A^\prime=MD$ and $B^\prime=M$ are unknown and must be estimated. The noise covariances of this altered system are now non-trivial, however. We could also assume that the transition dynamic $D$ is known and that the identification problem is learning the mapping $M$ only. This might not be a poor assumption since the exponential decay is meant to serve as an intuitive passive dynamic.

In each trial of the task, a subject will have some internal representation of the observation dynamic $M$ which may or may not be accurate. In order to make accurate predictions, $M$ must be estimated.

Learning linear dynamical systems from data is a hot topic of research, most of which seems to focus on learning in the context of complete state observation ($M=I$, $y=x$). Algorithms to determine parameters of $A$ and $B$ are proposed (see Dean, Recht 2018).

From LQG theory we know that the control law is a linear function of the state:

\begin{align*}
u_t = -L_tx_t
\end{align*}

and thus our combined system dynamic is:

\begin{align*}
y_t &= M(D-L_t)x_{t-1} + Mw_{t-1} + v_t.
\end{align*}


The noise covariance due to the observation Q is unchanged, but the new noise covariance for the latent process is now $MRM^T$. This may make things difficult.

