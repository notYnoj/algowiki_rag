### 4.3 Conclusion

Using a dataset of over 200 language model evaluations spanning 2012-2023 evaluated on Wikitext and Penn Treebank, we find that the compute required to reach a fixed performance threshold has halved approximately every 8 months. This is much faster than the rate associated with Moore’s law and many other domains of computing. While algorithmic innovations have occurred rapidly, compute scaling has expanded by over a million-fold in this same period, exceeding the gains from algorithms and constituting the predominant source of performance improvements in recent years.

Overall, our work provides a quantitative estimate of the rapid pace of progress in language modeling. It also reveals the dominant role of scale rather than algorithms for recent gains. Future work could benefit from extending this analysis to additional, specific benchmarks and more closely examining the impact of data quality improvements and the gains from additional specific innovations. Despite its limitations, this research demonstrates the valuable insights that can be gained from a detailed statistical analysis of extensive datasets of machine learning results. By identifying the main drivers of performance improvements, this work lays the groundwork for further exploration and understanding of these trends in the field.

## Appendices

### A Observing improvements in the data

Besides the statistical model that we presented in section 2.1, we can also attempt to obtain doubling time estimates more directly. For example, we can look at LLMs that achieve close to Megatron-LM’s or GPT-2’s level of performance over time, and see how much less compute is used. Doing so reveals that we need between 5-fold and 100-fold less compute per year in 2023 to achieve the same performance achieved is between 2019 and 2023, amounting to a halving time of between 6 and 15 months.

This approach provides some insight but it has its issues, which is why we do not rely on it. For instance, it depends on the particular choice of reference performance. As can be seen from the above figure, depending on the choice, the exact rate can differ by a factor of 2.5. Moreover, this approach requires identifying models with similar or better performance at later dates, where the training compute is known. However, the data for the latter is relatively limited. We thus opt for using an arguably more principled approach with our core model presented in section 2.1 for our main results.

### B The gains from better scaling laws

We estimated the compute savings afforded by the Chinchilla scaling law, as proposed by Hoffmann et al. 2022, in contrast to the previously dominant understanding based on the work of Kaplan et al. 2020. First, we defined loss functions _L(N,D_) for both the Kaplan and Chinchilla scaling laws. Following this, we minimized these loss functions across variables _D_ and _N_, considering different levels of compute budget. For each specified budget, we then calculated the amount of compute required under the Chinchilla scaling law to achieve a loss equivalent to the minimum loss<tbc>

Relative training compute
300%
Megatron-LM
HSO
100%
ALiBi
NMST +GPT-2
30%
DFWT
Transformer + RD
10%
Transformer + GFM
B2T connection
3%
Doubling Time: 14.9 months
1%
2019
2020
2021
2022
2023
Publication Date

Relative training compute
300%
GPT-2 (1542M)
100%
30%
Compressive Transformer
ALiBi
3%
Co-former
Doubling Time: 5.9 months
Transformer + RD
1%
2018
2019
2020
2021
2022
Publication Date

Relative training compute
300%
Chinchilla
100%
OPT-175B
Gopher
LLaMA-33B
30%
BLOOM-176B
OPT-66B
10%
+ RE-PLUG
3%
Doubling Time: 6.9 months
1%
2021
2022
2023
2024
2025
Publication Date

(a) Relative training compute needed for Megatron-LM level performance

(b) Relative training compute needed for GPT-2 level performance

(c) Relative training compute needed for Gopher level performance

Figure 7: Relative compute (relative to baseline model) used to train models that achieve the same evaluated perplexity as Megatron-LM, GPT-2, and Gopher respectively. Doubling times of effective compute are 14.9, 5.9, and 6.9 months using least squares regression for Megatron-LM (cross-entropy range 2.87-3.06), GPT-2 (cross-entropy range 2.79-2.93), and Gopher (cross-entropy range 1.87-2.32), respectively. Circles are proportional to the compute used during training.

