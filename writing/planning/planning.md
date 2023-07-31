# Planning



### Sprint 1 (Next week)

#### Set up, organize, orient, set goals

* [x] recruit Brett for research eng, analysis (max \~6hrs a week)
* [x] upload data to s3 for collaboration
* [x] make goals and timeline for Tiago to review
* [x] email Tiago, share planning and current state
* [ ] schedule Tiago meeting
* [ ] consolidate writing, notes, planning into github / gitbook
* [ ] put latest analysis code into git repo
* [ ] write up null space variability thoughts as a next concrete step to test "full stack" data analysis, visualization, etc.



### Goals

* [ ] publish a minimal paper about the experiment, presenting the new paradigm to the community and generating exploratory results towards suggestions for followup (confirmatory) studies
* [ ] finish thesis from the above work, pass viva
* [ ] project manage this well, to transition into my next job
* [ ] generate data and code for others to explore and use, add to portfolio



### Admin

* [ ] pick a rough exam date
* [ ] pick examiners and andy reached out to them
* [ ] examiner nomination forms (4mo before)
* [ ] send thesis to examiners 6wks before
* [ ] format thesis https://www.ucl.ac.uk/students/exams-and-assessments/research-assessments/format-bind-and-submit-your-thesis-general-guidance
* [ ] enter exam in Portico https://www.ucl.ac.uk/students/exams-and-assessments/research-assessments/examination-entry https://www.ucl.ac.uk/students/exams-and-assessments/research-assessments/viva



### Sprint 2 (August)

#### Task review, behaviour, comparisons to literature, optimal control

This sprint focuses on control, as opposed to learning. We're interested in how subjects behave in the task, their individual performances, motifs of their behavior and EMG signals, confounds of the setup. We want to compare our work to existing motor _control_ literature to see how well it stands up.

Questions:

* Are subjects optimal controllers? In what sense? What cost functions are subjects optimizing for?
* What does activity look like in the "null" vs. "non-null" space? How do we find each of these? How do we interpret the high-dim null space? look at classic nullspace variability papers)
* Do predictions from optimal control theory match what we see in our experiment? Synergies, least action, responses.
*   What kind of control are subjects exhibiting? Model-based? Model-free? A mix of both?&#x20;

    * To disambiguate model-based and model-free, we can look at "adjustments"-- online corrections in subject trajectories-- are these corrections made optimally? Scrutinize the movements made after the adjustment. In what "spaces" (geometric, position/velocity, etc.) are these corrections made?



### Sprint 3 (September)

#### Dig into the data in terms of learning to control, even if only descriptively

* For the questions asked above, now ask how control changes over the course of learning, if at all? How are subjects learning? Why are subjects learning?
* What are the “signatures” or “features” of learning? If these features fit the data well over the course of learning, why? Interrogate model fits as hypotheses about learning.
* What are the trial-to-trial dynamics of these features? Do they tell a story about strategy, types of control?
* E.g. What optimal control model would fit the data at each point? Can we reconstruct / fit the best controller over blocks?



### Sprint 4 (October)

#### Normative models of learning

Can we construct a model that explains our findings across subject learning?

* Why are people learning _what_ they’re learning? Why are people learning _how_ they’re learning?
* What is our theory of subjects' solution to the learning problem, and how are its significant features captured by our model?



### Sprint 5 (November)

#### Bring it all together, write it up!

