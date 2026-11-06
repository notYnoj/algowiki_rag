Since for rank _r_, the input size is _nr_, one could have imagined a better running time than _O(n_<sup>_k_+1</sup>) for any \(r\checkmark n^k\); our lower bound shows that it is (conditionally) impossible even for the slightly super-constant \(r=2^{\Omega(log^*n)}\).

### 1.5.2 Slice Rank in kD LWS.

Slice rank is a another way to define tensor rank. If a tensor with rank _d_, then it trivially has slice rank at most _d_, which makes 2D LWS with slice rank more powerful. Indeed, we show that 2D LWS with slice rank becomes hard very quickly. Interestingly, this new hardness result builds on the APSP conjecture, rather than SETH; the APSP conjecture has not previously been connected to LWS problems to our knowledge.

**Theorem** (Theorem 3.5)**.** _Assuming the_ APSP _conjecture, there is no truly sub-cubic algorithm for_ 2D LWS _or_ \[Static\]2D LWS _with slice rank_ 3.

However, we can design a truly sub-cubic algorithm for 2D LWS with slice rank 1.

**Theorem** (Theorem 3.7,Theorem 3.6)**.** _There are truly sub-cubic time algorithms for_ 2D LWS _and_ \[Static\]2D LWS _with slice rank 1._

We then use this to design faster algorithms for natural dynamic programming problems. For instance, we generalize the nested boxes problem defined in \[KPS17\] to a multiple nested boxes problem and show that it can be formulated as kD LWS with slice rank 1, and thus it can be solved in time \(O(n^{k+1-\varepsilon})\) for some \(\varepsilon>0\).

**Theorem** (Theorem 5.6)**.** _Multiple nested boxes with dimension k can be solved in time_ \(O(n^{k+1-\varepsilon})\) _for some_ \(\varepsilon>0\).

We also show how to give a polynomial speedup for the airplane refueling problem in dimension _k_ if the cost only depends on where the airplane lands, since that would mean the tensor has slice rank 1. We discuss the details in Section 5.1.

### 1.5.3 Hardness of Polygon Triangulation.

We show similar algorithms and hardness for 2D LWS<sup>PT</sup>.

**Corollary** (Corollary 4.2)**.** _Under_ SETH_, there is no truly sub-cubic algorithm for_ 2D LWS<sup>PT</sup> _with weight function whose rank is_ 2<sup>_O_(log<sup>∗</sup>_n_)</sup> _or above._

**Corollary** (Corollary 4.4)**.** _Under_ APSP _conjecture, there is no truly sub-cubic algorithm for_ 2D LWS<sup>PT</sup> _with weight function whose slice rank is_ 3 _or above._

These results are proved by making use of a reduction to 2D LWS<sup>PT</sup> from a _special case_ of 2D LWS where the two tensors _w_<sub>1</sub>_,w_<sub>2</sub> must be equal. We then show that our previous hardness results hold even in this special case, yielding the above corollaries.

In fact, previous work shows that in some special cases when _w_ has rank 1, 2D LWS<sup>PT</sup> can be solved in truly sub-cubic time.

**Theorem** (\[HS82, HS84, HS02, LG21\])**.** _Suppose there exists_ \(x_i\in\mathbb{N},1\le i\le n\) _such that_ \(w[i,j,k]=x_i\cdot x_j\cdot x_k\) _for all_ \(1\le i,j,k\le n\)_, then_ 2D LWS<sup>PT</sup> _with tensor w can be solved in O(n_log_n_) _time._

Our results help explain why the examples of 2D LWS<sup>PT</sup> problems where faster algorithms are known correspond to tensors _w_ of rank or slice rank 1; see Section 6 for more details.

## 1.6 Organization

Section 2 contains the preliminaries: our notation, background on fine-grained complexity, and definitions of relevant problems. Section 3 discusses the kD LWS hierarchy and hardness, proving that a polynomial speedup over the standard DP algorithm is possible when the tensor rank is _O_(1) but impossible when the tensor rank is 2<sup>_O_(log<sup>∗</sup>_n_)</sup> (assuming SETH). Section 4 discusses the polygon triangulation problem 2D LWS<sup>PT</sup><tbc>

