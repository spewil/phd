<!--

How does this document work?

Here is general stuff about the page. Below that add "mdmerge" CLI links to transclude other markdown documents into this one, similar to latex chapters/includes.

Then we run compile, a python script that invokes pypandoc, which adds a header and puts it all into a template which references pandoc.css

TODO:
	make the layout more small-screen friendly (rearrange the TOC)
	think about how to include footnotes in the sidebar?

 -->

## Where are you?

This is an experiment in creating an open kind of thesis. I would like to work together using the nonprofit <a href="https://web.hypothes.is/" target="_blank">Hypothes.is</a> toolkit to annotate this living document, for which we'll track changes using [git](www.github.com/spewil/). In less than two years, this page will represent the culminated collective effort of a few people to better understand the organizing principles of human motor learning.

To start adding comments to this page, just highlight some text, click `annotate` and start typing. Note that you will have to a <a href="https://web.hypothes.is/" target="_blank">Hypothes.is</a> account, but it only takes a second.

## What am I doing?

I'm working on my PhD at the Sainsbury Wellcome Centre for Neural Circuits and Behavior in London. I'm setting up a family of experiments that I hope will test hypotheses about the organizing principles of sensorimotor control and learning. I'm setting up a task where I record from participants' muscles in their arms and hands using `electromyography`. Subjects' arms and hands are fixed in a brace, but as they send signals from their brain down to their spinal cords and ultimately to their muscles, my electrodes will sense this change in electrical potential and relay this change to the computer, which will reflect these changes through visuals shown on a screen. The object of the game is for the participant to learn which muscle activations correspond to which changes in the visual scene. You can think about this as a video game you're playing directly with your muscles.

## PhD Timeline

- Year 1 (October 2018 - October 2019)
  - coursework (October 2018 - March 2019)
  - <a href="/phd/rotations/mouse_ball.html" target="_blank">mouse wheel task in Mrsic-Flogel Lab</a> (Jan 2019 - March 2019)
  - <a href="/phd/rotations/ctrl-labs.html" target="_blank">ctrl-labs rotation in NYC</a> (April 2019 - June 2019)
  - <a href="https://www.sainsburywellcome.org/web/groups/murray-lab" target="_blank">MurrayLab rotation</a> (July 2019 - August 2019)
  - <a href="https://github.com/swcphd/greyboxes" target="_blank">Organize SWC PhD Bootcamp</a> (September 2019)

- Year 2 (October 2019 - October 2020)
	- list of thesis committee members
	- project proposal with literature search
	- data club presentation / 6-month review (May)
	- SfN poster introducing setup, concept
	- final draft of project proposal
	- introduction and background chapters
	- upgrade / 2nd year review (October)
	- preliminary task data
- Year 3 (October 2020 - October 2021)
	- finer-grained experiments, supporting experiments
	- theory chapter
	- modeling chapter
- Year 4 (October 2020 - October 2021)

# Purpose

> The processes by which biological control solutions spanning large and continuous state spaces are constructed remain relatively unexplored. Future investigations may need to embed rich dynamical interactions between object dynamics and task goals in novel and complex movements [@McNamee2019].

We know surprisingly little about how this process unfolds in the brain. So little, in fact, that we haven't quite figured out what the brain is actually doing. We know that it is involved in these muscle contractions, but what sort of strategy do you use to explore this space of possible mappings between what you experience when you move and what you expect to see and feel as a result? This is the question I hope to make headway on.

To do this, I'll use the literature of reinforcement learning and optimal control theory to guide my theoretical understanding of what is happening when a subject begins to experience learning in this novel situation. I will model hypotheses of this learning process and compare these models to the large amounts of data my experimental setup will produce as we track learning of subjects over many sessions.


# Biological Background

Muscles are collections of fibers that contract when chemical gradients are produced at the neuromuscular junction by action potentials emanating from neurons in the ventral horn of the spinal cord.

Electromyography is the detection of changes in chemical potential using electrodes. In my setup, we use a total 64 monopolar surface electrodes and monopolar needle electrodes to record chemical potentials from muscles in the forearm and hand.

<<[/Users/spencerw/Google Drive/motor_control/writing/sections/hand_anatomy.md]

<<[/Users/spencerw/Google Drive/motor_control/writing/sections/cm_connections.md]


# Theory Background

<<[/Users/spencerw/Google Drive/motor_control/writing/sections/problem_formalization.md]

<<[/Users/spencerw/Google Drive/motor_control/writing/sections/motor_adaptation.md]

<<[/Users/spencerw/Google Drive/motor_control/writing/sections/feature_extraction.md]

<<[/Users/spencerw/Google Drive/motor_control/writing/sections/policy_gradient.md]


# Experimental Setup

<<[/Users/spencerw/Google Drive/motor_control/writing/sections/hardware.md]


## Bibliography