<tbc>proved a proximity result, with which an \(\widetilde{O}(nw_\mathrm{max}^2)\)-time algorithm for Knapsack can be obtained. Combining the proximity result \[16\] and the convolution framework \[3, 4, 21\], Polak et al. \[26\] showed that Knapsack can be solved in \(O(n+w_\mathrm{max}^3)\) time. There is also a conditional lower bound (for 0-1 Knapsack) of (_n+w_<sub>max</sub>)<sup>2-_o_(1)</sup> based on the (min,+)-convolution conjecture \[14, 23\]. It remains open whether Knapsack can be solved in \(O(n+w_\mathrm{max}^2)\) time \[8\].

For Subset Sum, Pisinger \[25\] improved the standard dynamic programming and obtained a running time of _O(Nw_<sub>max</sub>). We remark that the dense Subset Sum result by Galil and Margalit \[17\] implies an \(\widetilde{O}(n+w_\mathrm{max}^{3/2})\)-time algorithm, but their algorithm requires all _w<sub>i</sub>_ to be distinct and _u_<sub>max</sub>=1 and is not applicable for Bounded Subset Sum. Hence, we do not include it in  2. Nevertheless, Bringmann and Wellnitz \[11\] later refined and extended the dense Subset Sum result, and their result implies an \(\widetilde{O}(N+\mu_\mathrm{max}^{1/2}w_\mathrm{max}^{3/2})\)-time algorithm where \(\mu_\mathrm{max}=\mathrm{max}_w\sum_{i:w_i=w}u_i\). (Note that \(\sum_{i:w_i=w}u_i\) is the total number of item copies whose weight is _w_). Polak et al. \[26\] gave the first algorithm for Bounded Subset Sum that depends only on _n_ and _w_<sub>max</sub>. Their algorithm runs in \(\widetilde{O}(n+w_\mathrm{max}^{5/3})\)-time. There is a conditional lower bound of \(\Omega(n+w_\mathrm{max}^{1-o(1)})\) implied by the Set Cover Hypothesis \[6\] and Strong Exponential Time Hypothesis \[1\].

## 1.1 Our Results

Theorem 1.1. _There is an_ \(\widetilde{O}(n+w_\mathrm{max}^{12/5})\)_-time algorithm for Bounded Knapsack._

Our result significantly narrows the gap between the previous upper bound of \(O(n+w_\mathrm{max}^3)\) and the lower bound of \(\Omega(n+w_\mathrm{max}^{2-o(1)})\). Moreover, in the regime where _w_<sub>max</sub> is _O(n_), our algorithm outperforms all the previous<tbc>

\begin{tabular}{cc}
Bounded Knapsack & Reference \\
\(\widetilde{O}(n\cdot\mathrm{min}\{t,OPT\})\) & Bellman \[5\] \\
\(O(N\cdot w_\mathrm{max}\cdot p_\mathrm{max})\) & Pisinger \[25\] \\
\(O(n^3\cdot w_\mathrm{max}^2)\) & Tamir \[28\] \\
\(\widetilde{O}(n+w_\mathrm{max}\cdot t)\) & Kellerer and Pferschy \[21\], also \[3, 4\] \\
\(\widetilde{O}(n+p_\mathrm{max}\cdot t)\) & Bateni et al. \[4\] \\
\(\widetilde{O}(n\cdot w_\mathrm{max}^2\cdot\mathrm{min}\{n,w_\mathrm{max}\})\) & Bateni et al. \[4\] \\
\(O(N\cdot\mathrm{min}\{w_\mathrm{max}^2,p_\mathrm{max}^2\})\) & Axiotis and Tzamos \[3\] \\
\(\widetilde{O}(n\cdot\mathrm{min}\{w_\mathrm{max}^2,p_\mathrm{max}^2\})\) & Eisenbrand and Weismantel \[16\] \\
\(O(n+\mathrm{min}\{w_\mathrm{max}^3,p_\mathrm{max}^3\})\) & Polak et al. \[26\] \\
\(\widetilde{O}(n+(t+OPT)^{1.5})\) & Bringmann and Cassis \[8\] \\
\(\widetilde{O}(N\cdot\mathrm{min}\{w_\mathrm{max}\cdot p_\mathrm{max}^{2/3},p_\mathrm{max}\cdot w_\mathrm{max}^{2/3}\})\) & Bringmann and Cassis \[9\] \\
\(\widetilde{O}(n+\mathrm{min}\{w_\mathrm{max}^{12/5},p_\mathrm{max}^{12/5}\})\) & This Paper \\
\end{tabular}

\begin{tabular}{cc}
Bounded Subset Sum & Reference \\
\(\widetilde{O}(n\cdot\mathrm{min}\{t,OPT\})\) & Bellman \[5\] \\
\(O(N\cdot w_\mathrm{max})\) & Pisinger \[25\] \\
\(\widetilde{O}(n+\mathrm{min}\{\sqrt{n}\cdot t,t^{5/4}\})\) & Koiliaris and Xu \[22\] \\
\(\widetilde{O}(n+t)\) & Bringmann \[6\], Jin and Wu \[20\] \\
\(\widetilde{O}(N+\mu_\mathrm{max}^{1/2}\cdot w_\mathrm{max}^{3/2})*\) & Bringmann and Wellnitz \[11\] + \[6\] \\
\(\widetilde{O}(n+w_\mathrm{max}^{5/3})\) & Polak et al. \[26\] \\
\(\widetilde{O}(n\cdot w_\mathrm{max})\) & This Paper \\
\(\widetilde{O}(n+w_\mathrm{max}^{3/2})\) & This Paper \\
\end{tabular}

1: Pseudopolynomial-time algorithms for Bounded Knapsack.

2: Pseudopolynomial-time algorithms for Bounded Subset Sum. In (\*), \(\mu_\mathrm{max}=\mathrm{max}_w\{\sum_{i:w_i=w}u_i\}\).

