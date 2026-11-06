always evaluated on the same benchmark, data is relatively sparse prior to 2017, and papers may not report relevant information such as parameter counts. Among other reasons this can result in our estimates being very noisy, yielding wide confidence intervals over doubling times. In addition, algorithmic improvements and scaling have historically been introduced concurrently, and this correlation between the two in our dataset can make it hard to disentangle their relative contributions to overall effective compute growth.<tbc>

• **Inconsistencies in model training and evaluations**. Inconsistencies in evaluations are well-known. While we have excluded non-standard evaluations from our dataset, our dataset spans models with different tokenization schemes, text preprocessing, stride lengths, and other details. This introduces noise and potential bias in our estimates of algorithmic progress, as researchers might have adopted more favorable evaluation schemes over time. However, our estimated reductions in perplexity from algorithmic improvements are large; likely larger than can be accounted for by changes in evaluation procedures. We expand on these points in Appendix E.2.3.<tbc>

• **Inability to distinguish between data quality and efficiency in data use**. The way that we define efficiency improvements in this paper is in terms of reductions in the amount of resources required to achieve a certain level of performance over time. However, in the case of data efficiency, this runs into a problem--are our measured reductions in data requirements due to improved data quality, or due to improvements in how well algorithms are able to use data? This is not a question that our model equips us to answer. It is therefore important to note that our measured reductions in compute requirements pertain to both algorithmic improvements and data quality improvements, the relative contributions of which could be a subject of future research.<tbc>

• **Reliance on the Chinchilla scaling law**. The scaling law from which our model is derived applies to dense transformers following a GPT-3 architecture (Hoffmann et al. 2022; Rae et al. 2021). However, we use this scaling law to model algorithmic improvements in different transformer architectures, recurrent neural networks, etc. Future algorithms might also follow different scaling laws (e.g. GPT-4 is rumored to be a mixture of experts). However, we believe it is likely that our core results should still hold: for one, neural scaling is not a phenomenon restricted to transformers (e.g. it is known to happen in RNNs as well, see Kaplan et al. 2020). We find that a wide range of statistical model structures provide consistent estimates, and that alternative methods of estimating pre-training algorithmic progress also give similar results (see e.g. appendix A), so it is probable that our core results are robust to the use of the scaling law from Hoffmann et al. 2022.<tbc>

• **Limited insight about future progress**. While the results from this paper could be used to inform one about future progress in language modeling, our paper focuses on historical improvements. Future rates of progress could be slower (e.g. if one thinks that historical progress consisted of picking "low hanging-fruit"), but they could potentially also be faster (e.g. due to increased research interest and investment). Expectations about future progress need to account for factors such as these, which we do not discuss in depth for the most part.<tbc>

Parameters
1012
2014
1011
2016
2018
1010
2020
109
2022
2024
2026
108
107
107
108
109
1010
1011
1012
Training Dataset Size (Tokens)

Parameters
1017
2014
1016
2016
1015
2018
1014
2020
1013
2022
1012
2024
2026
1011
1010
109
1010
1011
1012
1013
1014
1015
Training Dataset Size (Tokens)

Predicted requirements for GPT-2 performance

Predicted requirements for Chinchilla performance

Figure 6: Pareto frontiers for GPT-2 (Radford et al. 2019) and Chinchilla (Hoffmann et al. 2022) level performance on WT103. We truncate the frontiers to a factor of 1e3 greater or smaller than the existing training dataset size and parameter size of the actual model since extrapolating further out would not be reliable.

