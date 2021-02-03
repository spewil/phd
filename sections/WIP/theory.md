# Theory

Optimal Feedback Control

<!-- The UCM is not a hard-and-fast principle, as nothing as in the motor system. Rather, as we've seen elsehwhere, there seems to be a spectrum of control. This could be explained through a composite cost function which penalizes deviations from prior movement strategies[@raczSpatiotemporalAnalysisReveals2013]. There is much research pushing back on optimal control, uncontrolled manifold hypothesis, and this will be addressed in {+@sec:experiment}. -->


## Error-based Learning (1 day)

Error-based sdaption and state-space models have a great amount of precedent in the sensorimotor learning literature. We will summarize these models briefly and discuss our willingness to depart from them.

Current models of motor learning 

x' = Ax + Bu 

This model describes...

The downsides of this model are that it descibes a small aspect of our data.

## Optimal Feedback Control

The control setup writes a cost, environment has some dynamics. 

What is changing in this scenario?
What is being learned?
What information is used to do this learning?

Which model variables correspond to muscles? Movements?
What does the resultant feedback controller compute? How does this relate to cognition?

Is LQR (as it’s claimed to be) a reasonable model for feedback control and error reduction + variability prediction for dimensionality reduction-based motor interface (task reads out from D muscles, find modes of that data; do PCA to get K < D dimensions, controller only responds to motion in those K directions)—does behavior + motor activity follow LQR? this question has already been asked, but it hasn’t been asked for this kind of high-to-low dim mapping. It’s been asked in tasks where muscles haven’t been directly in control (Bolero 2009). Todorov: do a task, look at muscle signal. Muscles that aren’t necessary for task have higher variability b/c they’re not being optimized for task (but does’t introduce perturbations). Also see Loeb (2012) for a negative result saying that muscle coordination is habitual rather than optimal, but it has issues (low # muscles). Can we replicate previous reaching optimality results in our set-up? What’s unique about our set-up is the PCA/dimensionality reduction in muscle activity space. This is important because you can create arbitrary muscle-cursor mappings, so you have to learn a new skill/mapping. This is different than perturbing a fundamental movement and forcing adaptation, which is what has been previously done. For our task, the participants actually have to learn a new task/mapping, rather than just do what they already know and be robust to perturbations. We test the LQR hypothesis once they’ve learned the task, because LQR isn’t a learning theory, it’s a theory about optimal control. We can see if, once people learn a new skill, their behavior is optimal wrt LQR theory. If we establish this, then we can think about how this LQR model is actually learned (enter RL).

This model is lacking in ... 

### Intuitive Example of the OFC framework

Here we see a feedback controller with three muscles such that we can plot the muscle activation trajectory.

This is the feedback controller K, we can understand it's action by plotting 

PLOT OF SIMPLE EXAMPLE 

PLOT OF APT DATA

## Composition and Selection

Here we'll review and discuss models of action selection and policy composition as a means of theorizing about how subjects learn novel skills. 

In a sense, we're setting up several different directions for our understanding of composition and action selection which can be experimentally tested. 

We have a direct selection algorithm, composition through policy addition, and composition through policy multiplication. 

### KL-control Composition (1 day)

This setup is particular subset of OFC problems. 

Dynamics
Cost

Composable policies

PLOT OF INTUITIVE EXAMPLE

<!-- ### Multiplicative Policy Composition

Policies are distributionally weighted, as opposed to chosen each timestep? -->

### Generalized Policy Selection (1 day)

This is in the MDP case

Learning happens in several ways-- reward regression, Q-learning

What are rewards? 
What are tasks?
What are actions?