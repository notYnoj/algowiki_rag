<tbc>where _w(j,i_) is the cost of using one post office to serve villages _j_+1 to _i_. This gives a GLWS problem with _D_\[_i_\] as the lowest cost to serve the first _i_ villages and _E_\[_i_\]=_D_\[_i_\]. The DP recurrence enumerates all possible decisions _j_ such that the last post office serves the villages _j_+1 to _i_, and takes the minimum cost among all possible decisions _j_. Many cost functions _w_ used in practice (e.g., a fixed cost plus a linear or quadratic cost to the service range or sum of distances from villages to the post office) are _convex_, which implies decision monotonicity (DM) -- for two states _i_ and _j\>i_, their best decisions _i_<sup>∗</sup> and _j_<sup>∗</sup> satisfy \(j^*\ge i^*\). Symmetrically we can show that for _concave_ cost functions _w_, either \(j^*\ge i\) or \(j^*\le i^*\) holds, although concave cost functions are less common in the real-world applications of GLWS.

Given its high relevance in practice, convex GLWS has been studied in parallel. Apostolico et al. \[6\] showed an algorithm with _O(n_<sup>2</sup>log_n_) work and _O_(log<sup>2</sup>_n_) span. Later, Larmore and Przytycka \[69\] showed an improved algorithm with _O(n_<sup>1.5</sup>log_n_) work and \(O(\sqrt{n}logn)\) span. Despite the interesting algorithmic insights in these algorithms, the polynomial overhead in work limits their potential to outperform the classic sequential solutions with \(\tilde{O}(n)\) work \[37, 38, 41, 43, 44, 62\]. For the concave case, some work \[23, 25\] achieved near work-efficiency and polylog span on the original LWS, but the ideas cannot be applied to generalized LWS.

In this section, we show how to use the Cordon Algorithm to parallelize a well-known sequential GLWS algorithm with _O(n_log_n_) work, which works for both convex and concave DM. Although efficiently applying Cordon Algorithm here requires many sophisticated algorithmic techniques, our parallel algorithm (Alg. 1) remains practical and it indeed outperforms the sequential algorithm in a wide parameter range (see Sec. 6 for details). It is also the key building block for many other algorithms shown later in Sec. 5.

We start with preliminaries and the classic sequential algorithm, then discuss how to use Cordon Algorithm to parallelize it. We will use the convex case when describing the algorithm since it is used more often in practice, and discuss the concave case in Sec. 4.3.

## 4.1 Preliminaries

### _Convexity, Concavity and Decision Monotonicity._

The convexity of the cost function _w_ is defined by the Monge condition \[78\]. We say that _w_ satisfies the **_convex_** Monge condition (also known as quadrangle inequality \[96\]) if for all _a\<b\<c\<d_,

\(w(a,c)+w(b,d)\le w(b,c)+w(a,d).\) (5)

We say that _w_ satisfies the **_concave_** Monge condition (also known as inverse quadrangle inequality) if for all _a\<b\<c\<d_,

\(w(a,c)+w(b,d)\ge w(b,c)+w(a,d).\) (6)

Consider two states _i_ and _j\>i_ with best decisions _i_<sup>∗</sup> and _j_<sup>∗</sup>. A convex weight function leads to DM such that \(j^*\ge i^*\). A concave weight function leads to DM such that either \(j^*\ge i\) or \(j^*\le i^*\).

Another condition closely related to the Monge condition is the total monotonicity \[2\]. We say a \(n\times m\) matrix _A_ is **_convex totally monotone_** if for _a\<b_ and _c\<d_,<tbc>

\(A(a,c)\ge A(a,d)\Rightarrow A(b,c)\ge A(b,d).\)

<tbc>We say a \(n\times m\) matrix _A_ is **_concave totally monotone_** if for _a\<b_ and _c\<d_,<tbc>

\(A(a,c)\le A(a,d)\Rightarrow A(b,c)\le A(b,d).\)

<tbc>Let _c<sub>i</sub>_ be the column index such that _A_\[_i,c<sub>i</sub>_\] is the minimum value in row _i_. The convex total monotonicity of _A_ implies that \(r_1\le r_2\le\dots\le r_n\), while in the concave case \(r_1\ge r_2\ge\dots\ge r_n\) \[44\]. If _A_ is convex totally monotone, any submatrix _B_ of _A_ is convex totally monotone. The convex/concave Monge condition is the sufficient but not necessary condition for convex/concave total monotonicity.

In GLWS, we call _f<sub>i,j</sub>=E_\[_j_\]+_w(j,i_) a transition from _j_ to _i_. The convex/concave decision monotonicity is equivalent to the convex/concave total monotonicity of _f<sub>i,j</sub>_. Note that if _w_ satisfies the convex/concave Monge condition, so does _f<sub>i,j</sub>_. But the convex/- concave total monotonicity of _w_ does not guarantee the convex total monotonicity of _f<sub>i,j</sub>_. All the theorems in this paper only need the convex/concave total monotonicity of _f<sub>i,j</sub>_.

### _The Sequential Algorithm._

The best (sequential) work bound for convex GLWS is _O(n_) \[44, 62, 74\], and \(O(n\alpha(n))\) for the concave case \[63\]. However, both of them are mainly of theoretical interest since they are complicated and have large constants in both work and space usage. We parallelize a simpler and more practical algorithm with _O(n_log_n_) work \[44\]. This algorithm computes _D_\[1_..n_\] in order. It implicitly maintains the best decision array _best_\[1_..n_\]. When the algorithm finishes computing _D_\[_i_\], the algorithm updates _best_\[(_i_+1)_..n_\] using _D_\[_i_\], then _best_\[_j_\] (_j\>i_) will be the best decision of state _j_ among states 0 to _i_.

However, maintaining and updating this array of size _n_ for _n_ iterations require quadratic work. Observe that after computing _D_\[_i_\], _best_\[(_i_+1)_..n_\] must be non-decreasing in the convex case, and must be non-increasing in the concave case \[44\]. Hence, the algorithm maintains a "compressed" version of _best_\[(_i_+1)_..n_\] by a list of triples (\[_l,r_\], _j_), which indicates that all states between _l_ and _r_ have best decision _j_, i.e., \(\forall i'\in[l,r]\), \(best[i']=j\). The list is maintained by a _monotonic queue_, which is a classic data structure based on double-ended queue, and is inherently sequential. In the _i_-th iteration, we can directly find the decision of state _i_ from the queue. After obtaining _D_\[_i_\], the monotonic queue can be updated in _O_(log_n_) amortized cost to consider _i_ as a decision for all later states. In total, this algorithm costs _O(n_log_n_) work. Here we refer to the audience to the original paper for details of this algorithm. We will call this algorithm \(\Gamma_{lws}\). Making use of DM, \(\Gamma_{lws}\) only processes transitions between each state _i_ and its best decision. The DAG \(G_{\Gamma_{lws}}\) for this algorithm includes normal edges \(j\rightarrow i\) for all _j\<i_, and exactly _n_ effective edges \(best[i]\rightarrow i\) for all states _i_.

Due to simplicity, this algorithm is usually the choice of implementation in practice. We will show a parallel version of this algorithm using Cordon Algorithm.

## 4.2 Parallel Convex GLWS

We first give the parallel algorithm of convex GLWS. We will use the "post-office" problem mentioned above as a running example to explain the concepts, but our algorithm works for general cases.

Following the idea of the phase-parallel algorithm, with the current finalized states, the goal is to find all ready states as the frontier, where their true DP values can be computed from the finalized ones. We will use our Cordon Algorithm to find the frontier in each round. Naïvely, the recurrence suggests that a state depends on all states before it. However, note that a state is essentially ready<tbc>

