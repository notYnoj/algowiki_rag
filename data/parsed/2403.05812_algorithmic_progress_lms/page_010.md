After preprocessing, our dataset contains 103 transformer models, and 127 non-transformer models, largely consisting of recurrent networks such as the LSTM. Fitting the model on this data reveals that the transformer architecture typically lowers reducible loss proportionally by 4.6% \[95% CI: 3.0%, 7.0%\].

We can calculate its contribution in terms of "compute-equivalent gains" numerically: we first calculate the predicted loss for a transformer with some _N_ and _D_, and the predicted loss for a non-transformer with the same inputs. We then determine reduction in _N_ and _D_ to match this difference in loss. Compute is then approximated as usual, as _C_≈6_ND_. In short, if an innovation halves the compute needed to achieve a specific loss, then that innovation has a compute-equivalent gain of 2.

Based on 100 bootstraps, we obtain a median estimate of 7.2\(\times\) \[95% CI: 3.3\(\times\), 45.7\(\times\)\] for the transformer’s compute- equivalent gain.<sup>8</sup> This substantial gain indicates that the efficiency offered by the transformer architecture is equivalent to around log(7)/log(2e4)≈20% of the total gains from algorithms in the past nine years, or nearly two years of algorithmic progress in the field.<sup>9</sup> Moreover, this could understand the gains if the transformer architecture also provides a convenient vehicle through which to productively channel compute, thereby facilitating some of the gains through the scaling of compute that have likely dominated the overall gains we have seen recently.

One caveat here is that the measured significance of the transformer may depend on how it is evaluated. For example, transformers may be better adapted to long contexts than recurrent networks, and evaluations using longer contexts (e.g. _\>_1000 tokens) may suggest a larger improvement from transformers than evaluations using shorter contexts (Kaplan et al. 2020). We have not explicitly controlled for context length here, and we discuss the potential impact of this assumption in more detail in appendix E.2.1.

## 4 Discussion and conclusion

### 4.1 Summary of our findings

This paper presents a comprehensive empirical analysis of algorithmic progress in language model pre-training from 2012 to 2023. By curating a dataset of over 200 language model evaluations on WikiText and Penn Treebank benchmarks, we quantify the relative contributions of compute scaling and algorithmic efficiency improvements to the overall performance gains. Our key findings are as follows:

First, we estimate that the compute required to reach a set language modeling performance level has halved every 8-9 months on average since 2012. This rate significantly exceeds hardware gains per Moore’s law and places language modeling among the fastest advancing domains in algorithmic progress, alongside computer vision and reinforcement learning. This supports the common intuition that language modeling is an unusually rapidly-advancing field of computer science.

Second, our work reveals that the majority of recent advancements in language modeling stem more from scaling models and datasets than from pre-training algorithmic innovations. A Shapley value-based analysis suggests that 60-95% of the performance gains stem from compute scaling, while algorithms contribute only 5-40%.

Third, the introduction of the transformer architecture in 2017 was a major algorithmic advance, representing between 3x and 46x in compute-equivalent gain, which accounts for more than 10% of the algorithmic innovation in pre- trained language models in the past decade. This highlights the significance of the transformer as a key architectural breakthrough in the field.

### 4.2 Limitations

While our analysis is an advance in quantifying algorithmic progress, several limitations reduce the precision of and temper our confidence in our estimates:

• **Lack of estimates of gains from specific innovations**. Our model is specified to quantify algorithmic progress over relatively large time periods (e.g. over several years). However, it is unable to give reliable fine-grained information, such as progress over shorter time scales, or the significance of specific innovations. Experimental work is better suited to estimating efficiency gains for specific algorithmic innovations.<tbc>

• **Limited availability of quality data**. The approach we use in our analysis relies heavily on having many data samples across many years. This proved to be very challenging for a number of reasons--e.g. models are not<tbc>

<sup>8</sup>This assumes compute budgets of frontier models today, at 10<sup>25</sup> FLOP. At lower compute budgets, such as 10<sup>22</sup> FLOP, the gain is still substantial at 6.6\(\times\) \[95% CI: 3.2\(\times\), 28.2\(\times\)\]. <sup>9</sup>Given the magnitude of this contribution, we also attempted to check the rate of algorithmic progress while subsetting our data to non-transformers only. However, this roughly halves the data available for fitting, and our resulting estimates are unfortunately extremely noisy. While our central doubling time estimate is 8.8 months, this result is no longer statistically significant, with a 95% confidence interval of -30.6 to 34.8 months.

