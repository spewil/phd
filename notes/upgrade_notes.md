# wolpert + maneesh upgrade meeting

Why didn't you put prior muscle BMI work into the report?
	- Oops. Will add this section. Good that I had a slide about this. 

How will you address the issue that you don't actually know anything about what the hand is doing?
	- Building a "good" decoder is an incredibly difficult problem (it's Ctrl-Labs business model), and we don't intend to solve that. We think we can forgo prediction about hand behavior and treat the EMG signal as a neural signal containing information about the subject's motor outputs. Correlations between channels will reflect both physiological relationships as well as existing, learned activity patterns.

If the activity patterns aren't stable over days, you could either do a single-day task (which Wolpert said would be a strong experiment to start with) or try to rotate or align your mode space into a reference frame. 
	- I agree single day learning for thousands of trials would be a great start, but I do worry about effects of consolidation. Some studies have shown retention only after multi-day practice.
	- I'm not sure how I would construct an alignment procedure day-to-day. I guess it would be something like fitting a rotation matrix with a squared-error cost function? 

(Maneesh) I think there are two aspects here: re-aiming strategies where subjects use existing motor patterns in new combinations to achieve the task, and remapping where new motor patterns are formed. 
	- Yes, and the literature has inklings of each. I think the BMI work from Bautista's group will be most informative for teasing these two aspects apart. 

Since you're collecting surface EMG, you may only be getting access to a few superficial muscles, let's say 8 muscles optimistically. Why not use a Cyberglove, which has 19 dimensions?
	- Firstly, we are hoping for more than 8 dimensions as we hypothesize you'll develop submuscular activations. This remains to be seen, and would be quite a surprising result.
	- Nonetheless, we may be getting less than 19 dimensions, but we'll be directly reading out controls signals from the CNS which for the subject won't constrain them to produce activity patterns that are typical for joint movements. They will be encouraged to explore motor unit space rather than joint space. We think this is a richer and more informative signal than joints.

Why 64 channels? This seems like an overcomplication. Why not, say, 4 channels? 
	- With 64 channels we can get a more complete picture of the superficial muscle of the forearm. We can also use the redundancy to filter for noise, etc. to find modes that are  e're getting a picture of the surface of the forearm
		- this might be low end like 8DoFs, but would be interesting if it were higher?

Asking "are people like optimal feedback control" is no longer interesting. What's most interesting about your angle is the novelty of the setup and that you're going after trial-by-trial learning. Simplify the experiment as much as possible to focus on validating the rig and analyzing a rich dataset.
	- Agreed, we're interested here in learning. But we could validate OFC findings with (un)controlled manifold hypotheses on our way to learning, perhaps. 

Start with very simple models of learning as a baseline
	- model-free =  rescorla-wagner delta rule style models
	- model-based = bayesian, kalman filter models
	- Fit these types of models, see what happens, then work towards more complex models

(Wolpert) One way perhaps to simplify the task is to actually not show the subjects a continuous feedback cursor trajectory, but just show them whether or not they hit the target.

Don't do pupil and gaze recordings. It's an overcomplication and it won't tell you anything you need to make progress. 
	- If pupil does serve as a proxy for value, it might be interesting from an RL perspective. I'm not sure how confident we are in this correlation, and it isn't that much work to add it to the data collection... but ok. 
