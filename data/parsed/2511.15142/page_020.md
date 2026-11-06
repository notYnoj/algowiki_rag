## 4.3 Other Applications

In this section, we present several applications of Theorem 1.5 and Theorem 4.2 that yield low- query and efficient algorithms for well-studied problems such as _k_-SUM, SUBSET-SUM, and sorting sumsets _A+B_ (see \[KLM19\]). When the elements of the ground set take integer values in the range \[-_B,B_\], our algorithms achieve better query complexity while also being the first efficient algorithms in this setting.

### 4.3.1 Low-query and efficient comparison decision trees

1. _k_**-SUM:** In the _k_-SUM problem, the input elements in _U_ have unknown values \(w_e^*\), and the goal is to decide whether there exist _k_ distinct elements whose sum is zero. The comparison model considered in \[KLM19\] allows comparisons between _w_<sup>∗</sup>(_S_) and _w_<sup>∗</sup>(_T_) for \(S,T\in\genfrac(){pt}{2}{U}{k}\) and between _w_<sup>∗</sup>(_S_) and 0. They achieve a query complexity (decision tree depth) of _O(kn_log<sup>2</sup>_n_).<tbc>

<tbc>Using Theorem 1.5 with _C=kB_, we obtain an algorithm with query complexity _O_((_n+kB_)log(_kB_)) and running time poly(_n,B_), which improves both measures when _B=o(n_). Our algorithm first sorts all feasible _k_-sets by their weights using only comparison queries between solutions, and then performs a binary search using comparisons with 0 to check whether a subset of size _k_ has total weight zero.<tbc>

2. **SUBSET-SUM:** In the SUBSET-SUM problem, the goal is to determine whether there exists a subset \(S\subseteq U\) such that _w_<sup>∗</sup>(_S_)=_t_ for a given target _t_. Similar to _k_-SUM, the model allows comparisons between feasible sets (F=2_<sup>U</sup>_) and between a feasible set and the target _t_. The algorithm in \[KLM19\] achieves query complexity _O(n_<sup>2</sup>log_n_).<tbc>

<tbc>Using Algorithm Section 4.1.1 with the efficient separation step stated in Section 4.2.1, we obtain an algorithm with query complexity _O(nB_log(_nB_)) and running time poly(_n,B_), which again improves both parameters when _B=o(n_). As before, the algorithm first sorts all subset weights using comparison queries and then performs a binary search using comparisons with _t_ to determine whether a subset with total weight _t_ exists.<tbc>

3. **Sorting sumsets** _A+B_**:** In the _A+B_ sorting problem, we are given two sets _A_ and _B_, each of cardinality _n_, with unknown element values \(w_a^*\) and \(w_b^*\) for \(a\in A\) and \(b\in B\). The goal is to sort the set \(A+B=\{a+b:a\in A,b\in B\}\) using only comparisons between sums of the form _w_<sup>∗</sup>(_a_<sub>1</sub>)+_w_<sup>∗</sup>(_b_<sub>1</sub>) and _w_<sup>∗</sup>(_a_<sub>2</sub>)+_w_<sup>∗</sup>(_b_<sub>2</sub>).<tbc>

<tbc>The model in \[KLM19\] even allows stronger comparisons--such as comparing sums of four elements _w_<sup>∗</sup>(_a_<sub>1</sub>)+_w_<sup>∗</sup>(_b_<sub>1</sub>)+_w_<sup>∗</sup>(_a_<sub>2</sub>)+_w_<sup>∗</sup>(_b_<sub>2</sub>) versus _w_<sup>∗</sup>(_a_<sub>3</sub>)+_w_<sup>∗</sup>(_b_<sub>3</sub>)+_w_<sup>∗</sup>(_a_<sub>4</sub>)+_w_<sup>∗</sup>(_b_<sub>4</sub>)--which we do _not_ use. Their algorithm achieves a query complexity of _O(n_log<sup>2</sup>_n_).<tbc>

<tbc>To fit this problem into our framework, we set \(U=A\cup B\), and let F consist of the bases of a partition matroid over _U_ with parts _A_ and _B_, each having capacity one. Then comparing _w_<sup>∗</sup>(_a_<sub>1</sub>)+_w_<sup>∗</sup>(_b_<sub>1</sub>) with _w_<sup>∗</sup>(_a_<sub>2</sub>)+_w_<sup>∗</sup>(_b_<sub>2</sub>) corresponds exactly to comparing the weights of two feasible sets {_a_<sub>1</sub>_,b_<sub>1</sub>} and {_a_<sub>2</sub>_,b_<sub>2</sub>}. Since partition matroids are representable over the reals, and the element values lie in \[-_B,B_\], we can apply Theorem 1.5 with _C_=2_B_ to obtain an algorithm with query complexity _O_((_n+B_)log_B_) and running time poly(_n,B_). This improves on previous bounds when _B=o(n_) and uses only valid pairwise comparisons among elements of _A+B_.

Moreover, our results extend to an even weaker model in which only _equality_ queries are allowed. In this setting, the query complexities for the three problems above are _O(kB(n+kB_)), _O(n_<sup>2</sup>_B_<sup>2</sup>), and<tbc>

