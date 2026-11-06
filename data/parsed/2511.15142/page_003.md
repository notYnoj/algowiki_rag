<tbc>could consider F to represent set covers, independent sets, cliques, or other NP-hard problems for which finding the optimal set is believed to be computationally hard--nonetheless, the number of comparisons required is still nearly quadratic! Indeed, while the query complexity of the procedure in Theorem 1.1 is polynomial, its running time could be exponential (under standard complexity- theoretic assumptions). This shows a large gap between the information complexity and the computational complexity in this model.

The key to proving Theorem 1.1 is to approach this query-complexity question from the correct perspective: we adapt the powerful active classification framework of \[KLMZ17\] to the optimization setting. We show how to use their classification framework to also optimize over arbitrary point sets (and not just Boolean point sets) in R_<sup>d</sup>_, with the number of queries being related to their "conic dimension".<sup>2</sup>

**Theorem 1.2** (General Linear Optimization)**.** _There is an algorithm that, for any point set_ \(\mathcal{P}\subseteq\mathbb{R}^d\) _with conic dimension k and unknown weights_ \(w^*\in\mathbb{R}^d\)_, returns the minimizer_ \(x^*=argmin_{x\in\mathcal{P}}\langle w^*,x\rangle\) _using at most O(k_log_k_log|P|) _comparisons._

Since the conic dimension of the Boolean hypercube {0,1}_<sup>n</sup>_ is known to be _O(n_log_n_), this result immediately implies Theorem 1.1. Moreover, it gives bounds on the query complexity when the point sets have bounded representation size, and for approximate optimization when they have bounded norm. We discuss these results in Section 2.

## 1.1.2 Optimization from Certification

While the approach of Theorem 1.1 provides strong query complexity bounds, we also provide a powerful alternative perspective via certification. In Section 3, we show an efficient reduction from optimization to certification using a Dual Ellipsoid Algorithm. This framework reduces the optimization problem to designing a Conic-Certification Oracle (CCO). If one can efficiently certify the optimality of a candidate solution (with the knowledge of _w_<sup>∗</sup>) using only comparisons, one can efficiently optimize. Moreover, this framework also yields a deterministic algorithm that uses poly(_n_) queries for the Boolean Linear Optimization problem.

**Theorem 1.3** (Optimization from Certification)**.** _There is a deterministic algorithm that, given access to a Conic-Certification Oracle_ (CCO) _for a family_ F _represented by points_ \(\mathcal{P}\subseteq\mathbb{R}^d\) _with bit complexity_ \(\langle\mathcal{P}\rangle\)_, finds the optimal solution_ \(S^*=argmin_{S\in\mathcal{F}}\langle w^*,\unknown_S\rangle\) _using_ \(O(d^3\langle\mathcal{P}\rangle)\) _calls to the_ CCO _and separating hyperplane updates._

See Section 3.5 for the proof of Theorem 1.3. The fact that this framework also yields a deterministic algorithm that uses poly(_n_) queries for the BLO problem follows from Corollary 3.9. We demonstrate the power of this reduction by using it to efficiently find minimum weight perfect matchings in complete bipartite graphs.

<sup>2</sup>The conic dimension is a slightly weaker variant of the "inference dimension" from \[KLMZ17\], specialized for linear optimization. The name reflects its reliance on the notion of conic independence (based on conic spans).

\begin{tabular}{ccc}
**Problem** & **Past Work** & **Our Results** \\
Any Boolean & - & _O(n_<sup>2</sup>log<sup>2</sup>_n_) \\
optimization problem & - & _O(nB_log(_nB_)) \\
\end{tabular}

_ 1: Our general results for query complexity. The second row is when weights are integers in_ \[-_B,B_\].

