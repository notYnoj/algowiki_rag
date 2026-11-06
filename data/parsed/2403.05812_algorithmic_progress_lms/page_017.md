<tbc>decreases in loss, and we typically arrive at values between 10-60% of the overall algorithmic progress contribution.<sup>11</sup> We perform a similar analysis with the scaling relation described in Kaplan et al. 2020, with similar results. If this rough calculation is correct, it suggests that increasing context length may have been a fairly important dimension along which algorithms have been improving.

On top of measured reductions to averaged perplexity per token, one might also consider the increasing ability of language models to perform long-context tasks to be largely downstream of algorithmic progress in itself. Being able to handle long contexts is a key motivator for several recent algorithmic innovations (Liu et al. 2024; Gu and Dao 2023; Gemini Team 2024), and this has likely grown very substantially since the introduction of FlashAttention (Dao et al. 2022; Vries 2023). We consider this to be an important avenue for further investigation.

## E.2.2 Tokenization

One way to get a sense of the impact of tokenization on measured doubling times is to introduce a fixed effect that depends on the benchmark vocabulary size into our preferred model. In particular, we introduce an irreducible loss term to Equation 8, of the form \(\gamma log\)(vocabulary size).

As with the rest of our analysis, we perform bootstraps to obtain a distribution over estimated doubling times, and further fold this model into our cross validation analysis. In particular, this model predicts a median effective compute doubling time of 8.0 months, with a 95% confidence interval of 4.0 to 17.1 months. In cross validation, this model performs essentially as well as our preferred model, with a MSE loss of 0.0486 in both cases. Both of these results are very much in line with the results from our main model, lending some weight to the view that differences in tokenization schemes used in practice do not substantially change our core results.

One possible reason for this is that in practice, the tokenization schemes used for evaluating language models on the considered benchmarks (i.e. WT103, WT2 and PTB) are typically highly similar, and so including a contribution from vocabulary size has only a limited effect within each dataset. For example, typical tokenizers for PTB, WT2 and WT103 have vocabularies of roughly 10k, 22k, and 268k tokens respectively. We illustrate this in Figure 11, where for each benchmark, the majority of vocabularies fall into the same histogram bin.

## E.2.3 Inconsistencies in perplexity evaluations

Inconsistencies in benchmark evaluations is a well-known issue in the machine learning community. These issues can introduce noise (if inconsistencies are ‘random’), or bias if they systematically change over time. We curated data so that models were evaluated in roughly comparable ways, but often the precise details of evaluations were lacking, so that we could not verify the precise evaluation procedure. However, there are many other subtleties with evaluation setups that may also cause perplexity results to differ, such as pretraining data, test-time adaptation (Takase, Suzuki, and Nagata 2018), tokenization schemes, strides, and text preprocessing.

Overall, we do not see these issues substantially undermining our results. Our mainline estimates imply that 1 year of pre-training algorithmic progress amounts to a reduction of perplexity of around 10%, which is a much larger reduction than seems plausible to explain by changes in the average year-to-year evaluation procedures.

<sup>11</sup>This of course depends on variables like how quickly context lengths have expanded over time--details of this calculation can be found in this spreadsheet.

Number of models
60
PTB
WT2
WT103
50
40
30
20
10
0
1e4
3e4
1e5
3e5
1e6
1e4
3e4
1e5
3e5
1e6
1e4
3e4
1e5
3e5
1e6
Vocabulary

Figure 11: Histogram showing the most common vocabulary sizes for models in our dataset, separated by benchmark.

