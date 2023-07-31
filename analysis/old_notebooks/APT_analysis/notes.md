## self-organization thing

- we start noisy and we end up constraining noise (variance at each time point decreases)
    - we assume that this is happening because of the influence of reward
    - this is like a physical system (producing trajectories) quenching, solidifying
- this says something about how correlations change?
- we want to capture using our data...
    - time correlations within trajectories, averaged over some window
        - how do you visualize changing (nonstationary) covariance?
- you can have a "correlation" for each (trial_i,time_t,trial_j,time_s)
    - what do you want to know?
    - we want to know/measure the correlation length over trials?
    -

## inverseRL thing

- sticking to LQR I can learn a lot, implement the basic existing algorithms, then start to understand what is being optimized and how to adapt things if necessary
- compare to data, see how much sense things make, try to get curves to overlap
- compare subjects
- do some basic cross-val (what are we measuring?)
- compare cost function "residuals" (|fitted cost - task cost| = "internal cost")
- because LQR has a parameterized controller, we start to think about how to update this controller based on experienced trajectory samples?


## thoughts

The goal here is to extract information from trials that correlate with learning strategy.

### question

- How is a trial's outcome related to the previous trial's outcome?

### mb/mf

Model-free should respond to reward prediction error signals. In this case, this is the trial's binary success, and possibly the manner of unsuccess-- time limit and spatial error.

Model-based should respond to sensory prediction error signals. This may happen per timestep, but is more likely to happen over some fixed time interval, the rate at which feedback is dealt with-- this might be related to the 2012 paper's number of submovements finding.

### trajectory distribution

If each trial is a distribution of decisions about updates to spatial position, we want to understand how this distribution shifts trial-to-trial depending on its success.

We want to understand how subjects change their decision-making criteria depending on what they've experienced. If subjects believe that they were responsible for the error, that they made a wrong choice, they will show a bigger change in the next trial. If the error was perceived as being outside of their control, they will show little change.

We don't have any control over the outcome probabilities of the task, so we would need to assign probabilities to trajectories under some kind of trajectory distribution? Each trajectory would be a sample from a distribution with parameters showing

If you fit a cost to expert trajectories, you would then have a controlled diffusion that roughly matched the data, giving you a trajectory probability by way of a kind of path distribution?

Similarly, you could fit a trajectory distribution to expert/trained pointers and then use this to assign trajectory probabilities.

The idea I think is if the controller fits the data well, then the controlled process induces a trajectory distribution. We can fit noise parameters of this controller to the data? Then we have a trajectory distribution. We have to do this since we aren't (or can't) impose this distribution on the problem.

How can we track/measure the changes to each of these distributions?
How can we connect each trial (new datapoint) to the shift of these distributions?
    - How can we measure the impact of each new data point on the distribution?
    - How do we measure the update?
    - Is there a difference in this update measure after rewarded and unrewarded trials? (We would expect so)

We might expect the subject to make "bayesian" updates, but I'm not sure what this means, and I'm not sure how it's related to reward...
    - if a model fits the data well, matching it's updates, maybe the model serves as an intuition or a claim about the nature of the updates
    - but if a much simpler (less complex) model fits the data better, does that mean our intuition is wrong?


- you should update your movement distribution (?) in ways that matter under the current goal / cost / reward
- update = grad_R (current policy) --> you do this
- in the same way that you optimize movements (with a perfect model / policy) under a cost (Todorov)

- hypothesis is that we optimize learning / policy adjustment in the direction of cost
    - this is reinforcement learning
    - what do we not know about RL in motor learning?
        -

one trial:
P(tau) = ? (probability of one trajectory)
tau = [x1,x2,...,xT] (trajectory)
P(tau) = Product(p(x_i+1|x_i))_i=1...T = p(x1,x2,...,xT)

on the next trial:
    P(tau)_i -?-> P(tau)_i+1
    [x1,...xT]_i -?-> [x1,...,xT]_i+1
    in control
    [u1,...uT]_i -?-> [u1,...,uT]_i+1
    x_t ~ dynamics
    u_t ~ choice of input

x_t+1 = Ax_t + Bu_t + w_t
p(x_t+1) = N(x_t ; E_w)
p(tau) = Prob(Normal distributions)

if you model P(tau) as a _____:
    compute p(sample | model)
    do bayes:
    p(sample|model) ~ prob(model|sample)p(sample)
    do gradient descent


- mahalanobis is how far are you from the target trajectory distribution
- mahalanobis
- is the center of the tube the "target"?
    - should we fit a cost function to the data?
- is movement isotropic?


### information gain

One hypothesis is that each trial, you will maximize information gain while constraining variance enough to increase the probability of tasks success.

We need a measure of information gain trial-to-trial?


### variance

Each trial you're choosing which directions to constrain variance. Trial outcome should influence which dimensions are constrained and by what amount?

On a single trial level, there's the radial variance (very noisy) for all timesteps.

## data organization

These are the subjects in each group -
Test group: 301-310, 321-323, 325-328
Control group: 312-320 (No training, only test sessions on days 1 and 5)

The names of the files indicate pretty clearly the stage in the experiment.
Therefore, if you're looking for the training sessions you should examine the files ending with Train.1/Train.2/Train.3

Each .mat file contains a data structure called DATA,
each line is a single trial with all relevant information for that trial.
The trajectories coordinations are in the x and y fields.
Please note that these vectors (DATA.x, DATA.y) were predefined as long zeros vectors,
and only the first 100 or so samples contain real data, so you need to make sure you truncate these vectors correctly.

- Subject
    - Warmup + Test Day1
        - session (Train.X)
            - block (X)
                - right trial (+ve startpoint)
                - left trial (-ve startpoint)
                - ...

    - Train
        - day (Day2/3/4)
            - session (Train.X)
                - block (X)
                    - right trial (+ve startpoint)
                    - left trial (-ve startpoint)
                    - ...

    - Warmup + Test Day5
        - session (Train.X)
            - block (X)
                - right trial (+ve startpoint)
                - left trial (-ve startpoint)