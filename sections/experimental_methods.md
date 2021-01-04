# Experimental Methods

## Prior Work


## Goals

The goal of the project’s first phase is to develop a high-dimensional surface EMG recording rig to generate datasets with high signal-to-noise ratio and dense coverage over superficial muscles of the arm and hand. The first question of this phase is: what are the limitations of a closed-loop myocontrol experiment, and how can such constraints be avoided or leveraged? To answer this question we will develop a signal processing pipeline and diagnostics suite to identify constraints in the setup and aim to overcome, as much as possible, the limitations inherent in surface EMG recording such as muscle crosstalk and rigorous electrode placement[10].
The concept of the experimental setup is shown in Figure 1, where 64 monopolar electrodes are attached to a subject’s arm and hand to record muscle activity. The arm and hand are kinematically constrained in a custom fixture and motor activity is recorded during isometric muscle contractions at levels less than 20\% maximum voluntary contraction to lessen the risk of involuntary co-contractions. The setup circumvents the limb biomechanics by mapping muscle output directly to virtual stimuli shown on a computer monitor. Additionally, our study focuses on low-force, isometric contractions to avoid complications due to artifacts in dynamic, high- force movements.
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