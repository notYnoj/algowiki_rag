<tbc>list of scores represents the formal problem). We tested two variants: **I.i.d Scoring** scores \(x_i\in X\) independently, and **autoregressive (AR) scoring** scores all strings in a single query, allowing the model to see the scores of other elements. The approach corresponds to _pointwise_ ranking approach \[Sun et al., 2023, Sachan et al., 2022\] in the RAG literature.

**Verbalized sorting approaches** correspond to _pairwise_ ranking approaches \[Qin et al., 2024\] in the RAG literature, but our contribution focuses on leveraging the theoretical properties of classical algorithms, which has been undermined in the literature. These approaches use the same binary comparison oracle used by verbalized maximum. **VA Bitonic** uses the _Bitonic sorting network_ \[Batcher, 1968\] from parallel sorting literature, which performs _O(n_(log_n_)<sup>2</sup>) comparisons in _O_((log_n_)<sup>2</sup>) time due to parallelism. **VA KwickSort** \[Ailon et al., 2008\] is an _approximate parallel sorting_ algorithm. It is analyzed on a more general FAS-Tournament task, which permits transitivity violations (\(a\le b\wedge b\le c\Rightarrow a\le c\)) in LLM-based oracles, and bounds the expected number of deordered pairs ((_...,j,...,i,..._) for _i\<j_) at most three times the optimal. Operationally, kwicksort works identically to quicksort. It runs _O(n_log_n_) comparisons in _O_(log_n_) expected parallel runtime because the input size halves in each recursion in expectation. To address runtime/accuracy tradeoff, we added early-stopping to the recursion which returns the input _X_ immediately if \(|X|\le\theta\in\{4,16\}\).

We evaluated the approaches above on the following benchmarks: Amazon Reviews \[Hou et al., 2024\], Yelp Open Dataset Reviews \[yel\], Stanford Sentiment Treebank \[Socher et al., 2013, SST\], and World Cities \[Bamwor, 2026\] (appendix for details). Each dataset contains 30 sets of 100 strings, sorted by ratings, sentiment scores, and population. We compute the Kendall-Tau score \[Kendall, 1938\] between the output _Y_ and the ground-truth sorted list _Y_<sup>∗</sup>, averaged over the dataset.

Fig. 3 shows the speed-accuracy Pareto front of Qwen3 models. All VAs use symmetrization. The baseline performed terribly in both the accuracy and the runtime. AR baseline was even worse, with x100 slowdown from the baseline, causing timeouts (1 hour). While the scoring obtained a reasonable accuracy with the largest 32B model, their performance degrades as the model gets smaller. AR scoring did not work as much and its performance is often comparable with the baseline. VA kwicksort (_O_(log_n_)) outperformed VA Bitonic (_O_((log_n_)<sup>2</sup>)) as predicted by the theory. _The strength of VA is most pronounced with the small models_. 4B VA Kwicksort outperformed 32B scoring on Amazon, Yelp, Cities, and on par in SST.

Next, we investigated the effect of thinking, symmetrization, threshold \(\theta\), and data parallelism on kwicksort. Fig. 3 shows that both thinking and symmetrization drastically improve the accuracy, but thinking significantly increases the runtime while symmetrization sometimes reduces the runtime because of the more balanced recursions in kwicksort. Larger \(\theta\in\{4,16\}\) reduces the runtime with slight accuracy degradation. Linear speedup from data parallelism (DP) shows the scalability of VAs.

Finally, the table on the right shows that there is no correlation between the model size and the number of sorting invariance violations (duplicates) by the baseline. Thinking appears to increase the violations. This<tbc>

\begin{tabular}{cccc}
dataset & 1.7B/think & 4B/think & 32B/think \\
Amazon & 5.0/7.2 & 2.1/7.7 & 2.5/8.3 \\
Yelp & 6.3/8.5 & 1.1/9.3 & 4.1/10.2 \\
SST & 0.1/3.2 & 0.1/5.2 & 2.1/9.8 \\
cities & 0.0/0.0 & 0.1/1.5 & 1.8/9.8 \\
\end{tabular}

