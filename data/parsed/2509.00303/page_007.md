<tbc>literature \[7, 17, 71\]. A recurring trend is the reliance on a subset of data samples or data summaries to inform algorithmic decision-making. Taking inspirations from the classical query optimizations, we build our optimizer by first sampling a subset of the data. Then, we run several candidate algorithms in parallel, analyze the resulting performance (e.g., monetary cost and accuracy) metrics, and determine the near-optimal configuration.

## 5.1 Cost Estimation

Before diving into the design of our optimizer, we first establish a methodology for monetary cost estimation. Unlike traditional database queries where the result is always 100% accurate, AI SQL queries have inherent quality and cost trade-offs. Often the user wants to obtain a high quality result constrained by a cost budget. Hence, our optimizer needs to select the algorithms with respect to the user’s cost constraint.

Estimating the monetary cost for each algorithm with fixed parameters is relatively straightforward. In  1, we list the number of LLM calls for each algorithm based on the number of input data points and algorithm parameters. After the sampling step, several algorithms are executed in parallel resulting in their running costs. This empirical measurement is crucial, as it provides the actual running cost to calibrate the theoretical cost models. Specifically, we can directly scale the observed cost per LLM call across the different algorithms and input sizes to accurately project the total expenditure for the original datasets. By the law of large numbers, the higher sample ratio will lead to lower estimation error. In our experimental section, we show that a small sample size can already provide quite accurate monetary cost estimation.

Example 5.1. _The cost of running the pointwise LLM based sorting on a sample of size 20 is_ $0.02_. With thelinear behavior, our estimation of running the pointwise LLM sorting over 1000 data points will be_ \(\$0.02\cdot\frac{1000}{20}=\$1\).

Example 5.2. _The cost of running the external bubble sort algorithm with batch size of four on the sample of size 20 is_ $0.05_. Since bubble sort has quadratic bevor, our estimation on running the external bubble sort algorithm with batch size of four over the 1000 data points will be_ \(\$0.05\cdot\frac{1000^2/4^2}{20^2/4^2}=\$125\).

## 5.2 Factual World Knowledge

In Section 4, we showed that for ordering based on factual world knowledge tasks, LLMs can directly recall factual data. The memorization of training corpora is an inherent characteristic of large language models and is essential for emergent reasoning abilities \[6, 41, 66\]. The value-based methods achieve high accuracy with minimal cost. Furthermore, as demonstrated in Section 4, pairing the pointwise approach with web search capabilities can achieve nearly perfect accuracy, grounding LLM results based on online sources.

Motivated by this observation, the challenge for ordering based on factual world knowledge becomes: _Can we successfully identify whether the information needed to order items is world knowledge?_ To address this question, we follow the methodology established in the field of membership inference in LLMs, and adopt the Inquiry Prompt from \[70\] as shown in Prompt 4, which achieves high membership inference accuracy and relies only on the generation REST API. In the evaluations, we find that the Inquiry Prompt effectively distinguishes between world knowledge and unknown entities.

We run the inquiry on a sample of the input data and if the LLM identified that this ranking task can be solved based on factual knowledge, the optimizer automatically uses **pointwise** with web search ranking strategy. If the LLM classifies the task as subjective or reasoning-dependent, the system safely falls back to the LLM-as-Judge or consensus aggregation approaches described later in this section. While the pointwise method is highly effective for factual sorting, its utility in broader semantic ordering is constrained by a lack of relative comparative context. By classifying the query upfront, we ensure that this method is deployed specifically when the model can function as a reliable knowledge retriever.

## 5.3 Candidate Algorithms

For LLM Order By, the initial candidate access paths include all value-based and comparison-based algorithms. Several candidates are parameterized: the external bubble and external merge sorts depend on a _batch size m_ (the number of keys packed into a single LLM comparison call), while quick sort with majority voting depends on an integer _vote_ count _v_ (the number of independent comparisons aggregated per partitioning decision); each hyperparameter setting yields a distinct candidate. Because the number of valid configurations is large, bounded only by the model’s context window and the budget, empirically evaluating every configuration over the entire dataset is prohibitively expensive.

We therefore appeal to our observation from Section 4 that **higher computation generally yields higher accuracy**. This principle justifies fully utilizing the available budget, favoring the more thorough access paths the budget can afford rather than defaulting to the cheapest path. To do so without executing every candidate in full, we estimate each candidate’s price from a small sample: we run it on a sample subset, measure the monetary cost per LLM invocation, and extrapolate to the full input size using the LLM-call complexity in  1. Candidates whose projected cost exceeds the user-specified budget are discarded, and the surviving within-budget candidates form the pool from which the final choice is made. This design is flexible and extensible: incorporating a new semantic sorting algorithm merely requires specifying its LLM-call cost function ( 1) to immediately include it in the competitive candidate pool.

**The main challenge.** Given a pool of candidate algorithms that satisfy the user’s cost budget, the remaining task is to select a subset that produces the highest-quality ranking. Each selected algorithm is executed over the full input exactly once. The core difficulty is that we must assess ranking quality _without_ ground- truth labels. We address this with two label-free methodologies, detailed in the next two subsections: an _LLM-as-a-judge_ approach that selects a single access path, and a _consensus_ approach based on reciprocal rank fusion (RRF) \[10\] that selects and aggregates an ensemble of access paths.

### 5.3.1 LLM-as-Judge Optimizer.

A common approach in evaluating complex tasks is the emergence of "LLM-as-a-Judge", where<tbc>

Prompt Block 4: Inquiry Prompt Can the following ranking task be solved using factual world knowledge? Task: {description} Examples: {examples}

