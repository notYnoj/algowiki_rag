We attempt to account for this possibility in the cross validation analysis. In particular, we introduce three models (models 13 to 15) which account for different kinds of scaling exponents, including the possibility of changing exponents over time. Our chosen main model (model 7) outperforms these models in cross validation, but these alternatives also perform similarly well, typically with an _R_<sup>2</sup> of between 0.88 and 0.91. This analysis is described in more detail in appendix J.

We also consider other factors that could potentially impact measured perplexity, and thereby measured rates of algorithmic progress. For example, different tokenization schemes during preprocessing have been found to improve WT103 perplexity in some instances (Radford et al. 2019), and training models for multiple epochs has been a common way of improving performance (Muennighoff et al. 2023). We find that our core results are broadly the same while varying these degrees of freedom--we provide more details on these experiments in the appendices.<sup>3</sup>

Finally, in order to account for uncertainty in our model specification in doubling times, we compare model predictions across the different models that we consider in our cross validation analysis.

#### 2.2.2 Data

Our dataset contains over 400 language models evaluated on WikiText-103 (WT103), WikiText-2 (WT2), and Penn Treebank (PTB), about 60% of which we are able to use in our analysis. In particular, relevant information was retrieved from around 200 different papers, as well as evaluations of 25 models that we performed ourselves using the framework from Gao, Tow, et al. 2021. We then consider the subset of the data that contains the information necessary to fit our proposed model structure in equation 3: token-level test perplexity (which determines the cross-entropy loss), publication date, number of model parameters, and training dataset size. This leaves us with around 231 models for analysis.

In some instances, multiple models are retrieved from the same paper, even if they constitute similar algorithmic innovations. This could pose problems around autocorrelation, which could result in underestimating the uncertainty in our individual parameter estimates. In the following main analysis, we therefore only include up to three models per paper, which results in approximately 50 more models being excluded. To verify the robustness of this approach, we also consider an alternative technique that directly accounts for autocorrelation in the analysis, which yields doubling time and confidence interval estimates that are consistent with our main results (see Appendix I).

## 3 Empirical results

### 3.1 Models require 2\(\times\) less compute roughly every eight months

How quickly are the algorithms underpinning language models improving? Our core approach is to back out doubling times based on fitting the augmented scaling law introduced in equation (8), and using the definitions of effective data, effective parameters, and effective compute we introduced in section 2.1. Here the effective data is given by<tbc>

<sup>3</sup>In particular, we consider tokenization in appendix E.2.2, epochs in appendix F, and context length in E.2.1.

Log perplexity
Wikitext
Penn Treebank
5.5
LBL
GCRN-M1, dropout
Training FLOP
5.0
LSTM
LSTM
Multi-cell LSTM
1a22
1a19
4.5
LSTM-300units
RNN+weight noise+dynamic eval
Pythia-160m
1a16
4.0
Large regularized LSTM
LSTM
3.5
3.0
Transformer (Adaptive Input Embeddings)
2.5
GPT-2 (762M)
LLaMA-33B
2.0
GPT-2 (1542M)
Turing-NLG GPT3-6.7B
1.5
Chinchilla
1.0
Gopher (7.1B)
LLaMA-65B
0.5
0.0
2012
2014
2016
2018
2020
2022
2024
Publication date

Figure 2: Log of perplexity of models used in our work, of over 231 language models analyzed in our work spanning over 8 orders of magnitude of compute, with each shape representing a model. The size of the shape is proportional to the compute used during training. Comparable perplexity evaluations are curated from the existing literature and from our own evaluations.

