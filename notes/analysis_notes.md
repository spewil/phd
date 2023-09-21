analysis_notes.md

quirks
- if you No Hold x4, you skip that target for the session..... this is awkward.
- for a No Hold, the data is recorded with the same trial prefix, this is the "target" prefix... 

data mgmt
- make a "rules" list to check when going through the data? (e.g. skip session 3 for X, etc.)
- make it such that I can use Paths and pull things that way from my s3 buckets or locally

todo
- determine how many no-holds for the same target in behavorial outcomes-- produce a picturre of "cleaned" outcomes 
- make sure the session naming is correct-- i.e. svenja's numbering if off by one. how should we fix this for consistency across subjects?
    - look at what's in the folder, do some checking at that point, then re-number everything once we have the files (have a "recorded" numbering and a normal one?)
    - what checks do we need to do?

what predictions are we making?
- forward model, dynamics, p(state' | state)
- inverse model, actions, p(motor command | state, behavioral goal / future state)

questions
- what is the sample rate? how long in time is a single step in the data?
    -  I think it's 1/60th of a second, because it's driven by the framerate of the game

slow!
- pulling anything from s3 is slow
- switch to local data store for speed!

PCA idea (talfan discussion)
- are people exploring with bias towards their "natural statistics"? we can look at this by comparing e.g. PCA from natural movements ("modes") with center-hold modes. are their game modes aligned to their natural modes?
- compare modes looking at correlations / cosine distance / does activity lie on the PCA subspace, manifold?

system ID
- how are people doing system ID? can we explain Ho-Kalman, how it works? can we explain how this relates to bayesian inference? how are people inferring their model? how does this relate to certainty-equivalence, kalman filtering, tracking?
- how does this compare to random searching?

---

theory stuff

**If the model identification procedure is aimed at control purposes, what really matters is not to obtain the best possible model that fits the data, as in the classical system identification approach, but to obtain a model satisfying enough for the closed-loop performance. This more recent approach is called identification for control, or I4C in short.**

**A forward model is equal to a physics engine used in game programming. The model takes an input and calculates the future state of the system.**

**The workflow for creating a forward model is called system identification.**

https://en.wikipedia.org/wiki/System_identification#:~:text=The%20field%20of%20system%20identification,as%20well%20as%20model%20reduction.


In the design of experiments for estimating statistical models, optimal designs allow parameters to be estimated without bias and with minimum variance. A non-optimal design requires a greater number of experimental runs to estimate the parameters with the same precision as an optimal design. In practical terms, optimal experiments can reduce the costs of experimentation.

The inverse matrix of the variance-matrix is called the "information matrix".
The traditional optimality-criteria are invariants of the information matrix; algebraically, the traditional optimality-criteria are functionals of the eigenvalues of the information matrix.

Since the optimality criterion of most optimal designs is based on some function of the information matrix, the 'optimality' of a given design is model dependent.

optimality = variance minimizing criteria
the criteria here is something like a cost? cost is to do with variance? but only in the task-relevant dimensions?

https://en.wikipedia.org/wiki/Optimal_design


"System Identification is the determination, on the basis of input and output, of a system within a specified class of systems to which the system under test is equivalent."
Klein 1989 (ESTIMATION OF AIRCRAFT AERODYNAMIC PARAMETERS FROM FLIGHT DATA) quoting Zadeh 1962 (From circuit theory to system theory)

DoE --> input/output data --> model structure determination and parameter estimation --> model verification

--- 

Astrom system ID primer

Loss function = L(process output, model output)
try to match the model prediction to the process


---

italian SI slides
https://indico.chem.polimi.it/event/27/contributions/12/attachments/89/212/2.3%20System%20Identification%20-%20Linear%20methods.pdf

The process of SI requires some steps, such as
(i) measurement of the IO signals of the system,
(ii) selection of a candidate model structure,
(iii) choice and application of a method to estimate the value of the adjustable
parameters in the candidate model structure,
(iv) validation and evaluation of the estimated model to see if the model is right for the
application needs, which should be done preferably with a different set of data.

Box-Jenkins model --> ARX or ARMAX depending on simplifications

these aren't state space models! these are autoregressive moving average things

-- 

state space models based on the hankel matrix of output data
how do you get from hankel to state space? SVD of the hankel
why? what is the statistical interpretation of this?

are we exploring in the dimensions of the PCs?
project activity along PC dimensions -- 
same as projectking activity along the null-space and task-space via the decoder