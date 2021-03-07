## Optimal Feedback Control

Talk up the python library for computing variants of optimal control, working towards a suite of optimal control stuff in python? Understanding the subtleties of these models, thinking about how they can be extended to capture features of motor learning data.

- prove that K is invariant to goal
    - just feed back the task error to reach a set point!
        - the cost want's the state, whatever it is, to go to zero.
    - K, S, etc is translation invariant to the goal state
    - to build this translation into the state/dynamics, we augment the state/cost with the target
        - this just computes the error from that state internally
    - write about this:
        - L is linear in state, we can apply linear operations to it?
        - S is quadratic in state, but we can also linearly transform it?
        - value functions and controllers are additive... but still linear/quadratic

Infinite horizon control

You can use the same controller and just feed back a different error, or you can build this error into your cost directly. You can change between one and the other through a a change of variable.

![Simulation of trajectories from uniform random initial positions for the simplest LQR controller. The diffusions are controlled such that their inputs are proportional to the positional error. The plain LQR controller is invariant (up to a translation) to the goal state, as explained in the text. Here the goal state is (0.5,0.5) denoted by a white star. red circles denote the initial position of the trajectory and green circles denote the endpoint after 200 increments. Arrows show the state-dependent control signal (force) vector $u = [f_x,f_y]$.](images/simulations/control_field.pdf){width=70% #fig:control_field}

![The same trajectory simulations as in {+@fig:control_field} atop the quadratic cost field.](images/simulations/cost_field.pdf){width=70% #fig:cost_field}

The question is: when would you need composition? When would you need to learn a new controller?