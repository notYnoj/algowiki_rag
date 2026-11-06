We choose this metric for two primary reasons. First, this is a commonly reported measure of performance, which allows us to gather a large dataset for our analysis. Second, the simple relation between perplexity and cross entropy _L_ allows us to easily relate our model to neural scaling laws.

If a paper reports the perplexity of just one model, we collect that singular data point. However, when a paper presents multiple models, only those meeting any of the following criteria are included in our dataset:

1. The model is trained or evaluated on a different benchmark dataset. A model trained on two different datasets can be used as a reference to understand how perplexity metrics reported on different benchmarks relate to one another. This can be helpful e.g. for data imputation<tbc>

2. The model is constructed with a drastically different parameter size, as such data inform the impact of scaling<tbc>

3. The model has a significant difference in the algorithms used than other models in the paper

For papers presenting many (10 or more) models, we exclude some from our dataset to prevent possible bias from over-representing results from a few studies. We prioritize models with the lowest perplexity in their category, often highlighted in bold within tables. We also exclude minor algorithm alterations and ablations that do not impact the parameter count. In Appendix I, we take an alternative approach by including all models from each paper and explicitly modelling the autocorrelation structure from results from the same paper. In doing so, we find results highly similar to those we present in the paper.

## E.2.1 Context length

Another consideration when analyzing algorithmic innovation in language models pertains to the context length. For one, measured perplexity on benchmarks can depend on the context length (Kaplan et al. 2020; Xiong et al. 2023). Different systems may have been trained or evaluated using different context lengths, and this might make model perplexity scores less directly comparable.

One way to try and quantify the magnitude of this effect is to look at studies that compare the change in perplexity given a change in context length. For example, based on the scaling relations relating loss and context length from Xiong et al. 2023 and Kaplan et al. 2020, back-of-the-envelope calculations suggest that loss reductions each year due to increasing context length could be 10-60% as large as the loss reductions from algorithmic progress.

In particular, Xiong et al. 2023 finds a relation between context length _c_ and validation loss for different versions of the LLaMa 2 language model. We can estimate ballpark values for context length over time based on data from Vries 2023, and use this to roughly estimate how expanding context lengths has decreased loss over time (e.g. a decrease of a few percent per year). We can then compare the magnitude of this effect to the contribution of algorithmic progress to<tbc>

Compute Equivalent Gain (CEG)
104
103
102
101
100
10 (0.001)
7 (0.0025)
15 (0.01)
8 (0.005)
15 (0.005)
7 (0.01)
12 (0.02)
10 (0.0025)
10 (0.005)
12 (0.005)
Model (delta)
Better cross-validation performance
Worse cross-validation performance

Figure 10: Contribution of the transformer in terms of Compute Equivalent Gain, as by introducing the structure in equation 7 to the top 10 models in leave-one-out cross validation.

