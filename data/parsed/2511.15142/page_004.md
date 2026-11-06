## 1.1.3 Global Subspace Learning

Alongside the certification reduction, we develop a second, general algorithmic tool tailored for the case where the weights in the objective function are integers in the range \[-_B,B_\]. This Global Subspace Learning (GSL) algorithm is highly intuitive, and in fact, sorts all the feasible sets by their weight (in poly(|F|_,n_) time for now):

**Theorem 1.4** (Boolean Linear Optimization: Bounded-Weights)**.** _There is an algorithm that, for any family_ \(\mathcal{F}\subseteq 2^U\) _and unknown integer weight vector satisfying_ \(|w_e^*|\le B\)_, sorts the feasible sets according to their weight w_<sup>∗</sup>(_S_) _(and hence solves the optimization problem) using O(nB_log(_nB_)) _comparison queries, where n_=|_U|._

The main insight behind this result is the following: two sets \(S,T\in\mathcal{F}\) with the same weight satisfy \(\langle w^*,\unknown_S-\unknown_T\rangle=0\), and hence the vector (\(\unknown_S-\unknown_T\)) gives us information about the subspace orthogonal to _w_<sup>∗</sup>. Our algorithm maintains a subspace A spanned by these orthogonal directions (\(\unknown_S-\unknown_T\)), and uses it to infer the weight class of other sets in F without making any additional comparisons; the details appear in Section 4. While Theorem 1.4 relies on weights being integral and bounded, it highlights how the structure of linear optimization can be exploited.

This explicit linear-algebraic structure allows us to get efficient algorithms from Theorem 1.4:

**Theorem 1.5** (Efficient Optimization over Linear Matroids)**.** _Let_ F _be the bases of a rank-k linear matroid_ M=(_U,_I)_, represented by_ \(V\in\mathbb{R}^{k\times n}\) _with entry representation size_ poly(_n). For an unknown integer weight function w_<sup>∗</sup> _satisfying_ \(|w_e^*|\le B\)_, we can sort the bases according to their weight w_<sup>∗</sup>(_S), and hence find the minimum-weight basis_ \(argmin_{S\in\mathcal{F}}w^*(S)\) _in_ poly(_n,B_) _time. The number of comparison queries required is O(nB_log_nB_) _and more generally, O_((_n+C_)log_C), where_ \(C=|\{w^*(S):S\in\mathcal{F}\}|\) _is the number of distinct basis weights._

Moreover, we get new algorithms for the Subset Sum, _k_-Sum and Sorting _P+Q_ problems studied by \[KLM19\], with better bounds for the case when _B=o(n_); see Section 4.3 for details.

\begin{tabular}{cccc}
**Problem** & **Past Work** & \multicolumn{2}{c}{**Our Results**} \\
 & & **Comparisons** & **Equality queries** \\
_k_-SUM & _O(kn_log<sup>2</sup>_n_) & _O_((_n+kB_)log(_kB_)) & _O(kB(n+kB_)) \\
SUBSET-SUM & _O(n_<sup>2</sup>log_n_) & _O(nB_log(_nB_)) & _O(n_<sup>2</sup>_B_<sup>2</sup>) \\
Sorting _P+Q_ & _O(n_log<sup>2</sup>_n_) & _O_((_n+B_)log_B_) & _O(B(n+B_)) \\
Linear Matroids & - & _O(nB_log(_nB_)) & - \\
Min-cuts & - & \(\tilde{O}(|V|)\) & - \\
Graph reconstruction & - & _O_(|_V_|<sup>2</sup>,(|_E_|+|_V_|)log|_V_|) & - \\
Matroids & - & \(\tilde{O}(n)\) & - \\
Matroid Intersection & - & _O(n_<sup>4</sup>) & - \\
\end{tabular}

_ 2: Efficient algorithms and query complexities for problems in the comparison decision tree model. The first set of results are for integer values in_ \[-_B,B_\]_. Our algorithms are efficient, running in_ poly(_n,B_) _and_ poly(_n_) _time. The past work is from \[KLM19\]._

