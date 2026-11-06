<tbc>that the only left element is 1 in the last round, we have

\(\mathbb{P}(\mathcal{A})\ge 1-\mathbb{P}\left(\bigcup_{i=1}^{\lceil\mathrm{log}_2(K)\rceil}\mathcal{E}_i\right)\)<br>
\(\ge 1-\sum_{i=1}^{\lceil\mathrm{log}_2(K)\rceil}\mathbb{P}(\mathcal{E}_i)\)<br>
\(>1-\sum_{i=1}^{\lceil\mathrm{log}_2(K)\rceil}\delta^{2(2i-1)}\)<br>
\(>1-\frac{\delta^2}{1-\delta^2}.\)

We can upper bound the error probability under event A with \(\delta\). Thus the total failure probability is upper bounded by \(\delta+\delta^2/(1-\delta^2)<2\delta\) when \(\delta<1/2\).

The upper bound for SEARCH is due to Gu and Xu (2023), and is thus omitted here. The upper bound for SORT is based on that for SEARCH. We can design an insertion-based sorting algorithm by adding elements sequentially to an initially empty sorted set via noisy searching, as in Algorithm 1 in (Wang et al., 2023). Since the insertion step requires \(\mathcal{O}(\mathrm{log}(K)/(1-H(p))+\mathrm{log}(1/\delta)/D_\mathrm{KL}(p\|1-p))\) queries. Overall we know that one needs \(\mathcal{O}(\sum_{k=1}^K(\mathrm{log}(k)/(1-H(p))+\mathrm{log}(1/\delta)/D_\mathrm{KL}(p\|1-p)))=\mathcal{O}(K\mathrm{log}(K)/(1-H(p))+K\mathrm{log}(1/\delta)/D_\mathrm{KL}(p\|1-p))\) queries to achieve error probability at most \(K\delta\). Rescaling \(\delta\) gives the final rate.

