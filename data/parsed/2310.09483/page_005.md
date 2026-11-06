The following tables summarize the previous results for the problems of approximate sorting and selection along with our contributions.

## 1.2 Related Work

Imprecise comparisons were first considered by Rényi \[Rén61\] and Ulam \[Ula91\] in the setting of binary search. The model described allows for a bounded number of incorrect comparisons. An optimal algorithm for this problem was given by Rivest, Meyer, Kleitman, Winklmann, and Spencer \[RMK<sup>+</sup>80\] that uses _O_(log_n_) comparisons. This problem was considered in the parallel setting by Negro, Parlati, and Ritrovato \[NPR95\] where they give optimal algorithms for a fixed number of rounds and errors.

Binary search has also been considered in the setting where comparisons are incorrect with some probability \(p<\frac{1}{2}\) \[Hor63, BZ74, FRPU94\]. Pelc \[Pel89\] gave an algorithm that uses _O_(log_n_) comparisons and gives the correct answer with probability \(1-\varepsilon\) if \(p<\frac{1}{3}\). For \(\frac{1}{3}\le p<\frac{1}{2}\), he gave an algorithm that uses _O_(log<sup>2</sup>_n_) comparisons. A later result from Borgstrom and Kosaraju \[BK93\] implies an optimal _O_(log_n_) algorithm for all \(p<\frac{1}{2}\).

Sorting with imprecise comparisons was first considered by Lakshmanan, Ravikuman, and Ganesan \[LRG91\] in the model where the number of incorrect comparisons is bounded by a function _e(n_). They gave a lower bound of \(\Omega(nlogn+en)\) comparisons and an upper bound of _O(n_log_n+en+e_<sup>2</sup>) comparisons. The upper bound was later improved to match the lower bound by Bagchi \[Bag92\] and Long \[Lon92\].

Sorting with comparisons that are incorrect with probability \(p<\frac{1}{2}\) was considered by Feige, Peleg, Raghavan, and Upfal \[FRPU94\] where they gave an algorithm that uses \(O(nlogn/\varepsilon)\)) queries and gives the correct answer with probability \(1-\varepsilon\).

Another common model is that of sorting networks with faulty comparisons. In the model where _e_ gates may be faulty (i.e. do nothing), Yao and Yao \[YY85\] gave an algorithm that uses _O(n_log_n+en_) gates. This model has been further studied in the cases where faulty gates may<tbc>

\begin{tabular}{cccccc}
Paper & Adversary & Randomized? & Approximation & Query Complexity & Round Complexity \\
\[AFJ<sup>+</sup>18\] & Non-Adaptive & Deterministic & 2 & _O(n_log_n_) & _O_(log_n_) \\
\[AFHN15\] & Adaptive & Deterministic & _k_ & _O_(4_<sup>k</sup>n_<sup>1+1/2_<sup>k</sup>_-1</sup>) & _O(n_<sup>1-1/(2_<sup>k</sup>_-1)</sup>) \\
Our Paper & Adaptive & Randomized & 4 & _O(n_log<sup>2</sup>_n_) & _O_(log_n_) \\
Our Paper & Adaptive & Deterministic & 2_d_ & _n_<sup>1+_O_(1_/d_)</sup>_d_ & _d_ \\
\end{tabular}

\begin{tabular}{cccccc}
Paper & Adversary & Randomized? & Approximation & Query Complexity & Round Complexity \\
\[AFJ<sup>+</sup>18\] & Non-Adaptive & Deterministic & 2 & _O(n_) & _O_(log_n_) \\
\[AFHN15\] & Adaptive & Deterministic & _k_ & _O_(2_<sup>k</sup>n_<sup>1+1/2_<sup>k</sup>_-1</sup>) & _O(n_<sup>1-1/(2_<sup>k</sup>_-1)</sup>) \\
Our Paper & Adaptive & Randomized & 4 & _O(n_log_n_) & _O_(log_n_) \\
Our Paper & Adaptive & Deterministic & 2_d_ & _n_<sup>1+_O_(1_/d_)</sup>_d_ & _d_ \\
Our Paper & Adaptive & Randomized & 202 & _n_<sup>1+_O_(1_/d_)</sup>_d_log_n_ & _d+O_(log_d_) \\
\end{tabular}

1: Sorting

2: Selection

