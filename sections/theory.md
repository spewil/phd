# Theoretical Contributions {#sec:bg_experiment}

- how do we adapt LQR controllers trial-to-trial?
- how do we use existing controllers to construct movements?
- how do we construct controllers under dynamical and goal uncertainty?


$include includes/model_adaptation.md


Think more about subspaces 
- preparatory activity in one subspsce, online control in another? 
- learning in one subspace but not another?
- compression of model to a subspace?


## Policy Selection

each timestep you combine actions from component policies to choose an action

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

### Temporal Composition

there is a spectrum of latency in the feedback response

can different controllers be used for different latencies, and adjusted accordingly?

### Generalized Policy Selection (1 day)

This is in the MDP case

Learning happens in several ways-- reward regression, Q-learning

What are rewards? 
What are tasks?
What are actions?

