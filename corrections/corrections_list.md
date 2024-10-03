MINOR ERRORS
[DONE] P17.  The list of figures is fine, but for Ch 8 only it is a catenation of captions.  This is not correct.
[DONE] P43: about -> amount TYPO
[DONE] P44 what computations are -> what computations is the brain.. TYPO
[DONE] P54 “Wireless recording permit” TYPO
[DONE] P89 All possible version TYPO
[DONE] P99 “We concludes” TYPO
[DONE] P112 “principle subspace”->”principal subspace”
[DONE] 118 solutions are learning -> solutions are learned TYPO
[DONE] P159 “that decoders statistic are not indicative of performance” TYPO
[DONE] P168 “compare to” TYPO – compared to
[DONE] P173 “Here we see the find the same pattern” TYPO
[DONE] P176 “subjects null space activity” TYPO subjects’
[DONE] P177 Reinforce learning TYPO Reinforcement???
[DONE] P195 “[@crevecoeurGoldstandardApproachAddress2010” REFERENCE
[DONE] P196 “Analyze the geometry of this trajectory may expose underlying dynamical modes” TYPO


Throughout
    Attend to labelling figures, units, captions, and terminology, esp. wrt consistency with text.
    --> [TODO] read through, updated plot labels, etc

Ch 1 -- Intro 
    - Minor rewording and editing

Ch 2 -- Background Theory
    EMG literature presentation lacks argumentation and needs an organizing principle.  Suggest discussing these papers in the context of desiderata of a learning experiment.
    - Added much more context in the first paragraphs to motivate why the topics reviewed are relevant and useful in following chapters, so the reader has a better scaffold to follow along.
    - Added context for each EMG study to preempt the methodological aims


Ch 3 -- Methods -- 
    Provide single EMG traces and comments on quality and consistency across trials in natural movement task
    - Provided a representative trace of a single channel of EMG across filtering steps to show form and quality of the raw and filtered data 
    - Plotted a UMAP embedding of the natural movement data for one subject with two blocks overlaid -- this indicates repeatability of the movements, and segregation of the movements
    - added elaboration on word choice when referring to the task and EMG "spaces", as well decoding, projecting, etc. in an effort to make it clear that these terms are used synonymously.
    - made it more clear that the task is isometric, and why this is interesting/unique/important
    - clarified the terms policy, inverse model, forward model and how they relate to one another
    - added references to "neural manifold" BCI papers, explained inspiration from these
    [DONE] p 64 -- change "hand open" to "hand grasp"


Ch 4 -- Performance
    - made it clearer what "reward" refers to and why, and its subtleties 
    - updated figure captions, labels, legends for consistency as noted in viva discussion


Ch 5 -- Data Manifold
    - Clarified, in text, captions, and figures labels, the use of "subspace confinement" and "effective rank"
    - Cleaned up discussion of the Grassmannian


Ch 6 -- Mixture Modeling

    Minor:
        - Reworded entropy and total variance sections
        - Figure legend of total variance figure mislabeling
        - Adjusted legends and relabeled axes for clarity (rank figure)

    Major: 
        Validate of mixture modelling with quantitative evaluation of goodness of fit
            --> [DONE] plotted the likelihood of a single gaussian under the data v. a mixture of gaussians model -- the mixture model yields a higher likelihood fit than a simple gaussian
                - This is an interpretable comparison showing that a simple Gaussian has a lower likelihood under the data, compared to the mixture model. That is, with added components (increasing parameters), we increase the likelihood of our model parameters. If fits diverged from the data, we would not see such a clear increase in likelihood.
            --> [DONE] plotted the elbow curve for mixture model components -- likelihood increases as the number of components increases
                - To understand if there is an optimal number of components, we fit the data with an increasing number up to the 12 components we used in the analysis. We see that the likelihood increases monotonically as the number of components increases. This implies that there is not a straightforward optimal number of components, that the data is better fit in terms of likelihood with more components. With 12 components, we see diminishing returns in likelihood as we continue to add components

        Potentially improve visualization of mixture models (e.g., heatmaps, propagation from log to EMG space) 
            --> [DONE] remove existing GMM plots...? 
                - I removed these for clarity, mentioned above
            --> [DONE] added kernel density plots of the data next to samples from the fitted models
                - I made many visualizations using individual components as before, but as you pointed out they tend to be visually overwhelming which distracts from the purpose; I made the decision to visualize the simple comparison of the overall mixture next to the subject data
                - I just plotted the raw data. It turns out that plotting the statistics of a distribution of a multivariate lognormal variable which has been projected into a linear subspace is a very deep topic beyond the scope of what we require here. I handled this numerically, plotting a region of high density.
            --> [DONE] added captions for KDE plots

        Entropy lower bound is not correctly described: re-check analysis results in light of this 
            --> [DONE] updated the lower bound derivation citing huber and gershman papers
                - using a jensen's inequality argument
            --> [DONE] updated plots for entropy using the updated derivation 
                - only changes the scale of the values, not the results
            --> [DONE] update writing around entropy and total variance

Ch 7 -- Null Space Variability
    - Clarified what is meant by "variance" where appropriate
    - Removed the term "accumulate" for variance
    - Added further discussion in line with feedback from the viva on the "miss end" variance ratio result to put this in broader context with other results.
    - Elaboration of figure captions for clarity
    - Rewrote summary to clarify findings


Ch 8 -- Reinforcement Learning Model
    - Minor rewording throughout for clarity.


Ch 9 -- Conclusion
    Return to research question and constructs of introduction
        Completely rewrote the discussion to clearly interpret findings in the context of goals of the study and prior literature.


References
    [DONE] Several unusual references which do not give standard publication details (e.g., 69, 70).  Some note on the reference format may be required if you are referencing non-standard material

    Revamped bibliography styling and corrected missing bibliographic data.