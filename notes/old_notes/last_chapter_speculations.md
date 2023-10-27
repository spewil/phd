﻿# Last Chapter Speculation

The control of complex movement, and the learning of new movements, fundamentally hinges on a deep hierarchy built into the structure of the motor system. This isn’t simply a MuJoCo humanoid model, it’s layers upon layers of evolution with intelligence at each layer, from the sarcomeres to the dendrites.


A central claim might be:


  



Another: The current robotics paradigm will soon hit a ceiling. Fully autonomous robotics with the flexibility to move and adapt to its environment is off-limits to the current paradigm?


To construct robots with the requisite flexibility to work alongside humans to accomplish important goals, we must think biologically. We have to create materials and structures that embed the hardest problems of robotics into this substrate. 


Questions:
* Who would we describe the “current” paradigm without creating a straw man?
* What are the most difficult computational tasks in robotics?
   * Sampling posteriors…?
* What is flexibility? Why is it important?


Theory
* What kinds of toy models can we show that make our point?
* How is this different from what deep networks are doing? Is this not distributed, parallel processing?


Inspirations:
* Distributed, Hierarchical, Recurrent -- I think what’s missing is the embedding of computation into the physical structure. The point is that there remains a Cartesian dualism inherent in these ideas, in “solutions” to the “problem” of movement. https://www.nature.com/articles/nrn.2017.7 
* Metastability -- a very  “complex systems” view of brains in general, claims evidence (it’s weak) for features of metastability in movement. https://www.sciencedirect.com/science/article/pii/S0896627313011835 




Thinking about the corticospinal tract cord, what do we know? Why is the human motor system so much better at movement than robotic systems? The bandwidth isn’t in the processing power or even our algorithms, it’s with the relationship between the “software” and the “hardware”. So how does the spinal cord work, and why is it important to understand? What can complexity in the physical plant offer? 


the punch line is essentially that in order to make true progress in robotics (and thus flexible AI) we need to both study the complexities inherent to biology systems such as the motor system for robotics, and then actually construct physical systems which combine structure and computation.


"how is this different from have a giant neural net taking in tons of pixels and telling the motors what to do?" my answer is that ultimately the physical system won't be able to fully realize the flexibility in behavior biological systems do -- biological systems adapt and evolved physically, not just computationally...


connectionism vs. computationalism:i think there's something to that debate, but my point is that without physically realizing these systems, we just won't get there. take, for example Boston Dynamics -- it's super amazing what they do, but it's not biological motion and i don't think it ever will be. it will always be about overcoming the limitations of the physical plant


Uncovering a system’s modes and then modulating those modes to perform task is a fundamental part of the control of biological systems . 


Locomotion is an example -- as speed increases, the phase of the dynamics transitions sharply between strategies. A run to a 


1. How the motor system functions
   1. Nielsen, graziano, lemon
2. The problem with robot motion
   1. Lack of flexibility?
3. Why is this different from neural net → actuators?
   1. Could have readout neurons / integrators with 10k+ inputs.
   2. The difference is firstly in the number of actuated elements in the movement system. Different postures use different circuits. Thinking in terms of movement circuits, building this capability up from scratch phylogenetically is a promising research direction. 
   3. The second kind of difference is in the parallelization of control circuits-- 
4. How the future of robots could look (bio-hybrid)
5. How we can start
   1. Studying the motor system and constructing systems that follow it’s design principles, rather than focusing on abstract problems