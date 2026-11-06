### 2.4 Subset Query Problems

**Definition 2.10** (Subset Query)**.** _The Subset Query problem is defined as follows. Given N sets_ \(S_1,\dots,S_N\subset[d]\) _and a query_ \(Q\subset[d]\)_, distinguish between the following two cases:_

• _(YES) There exists_ \(i\in[N]\) _such that_ \(Q\subseteq S_i\).<tbc>

• _(NO) For all_ \(i\in[N]\), \(Q\unknown\subseteq S_i\).

**Definition 2.11** (Bichromatic Subset Query)**.** _The Bichromatic Subset Query problem is defined as follows. Given two collections of sets_ \(S_1,\dots,S_N\subset[d]\) _and_ \(T_1,\dots,T_N\subset[d]\)_, distinguish between the following two cases:_

• _(YES) There exists_ \(i,j\in[N]\) _such that_ \(T_i\subseteq S_j\).<tbc>

• _(NO) For all_ \(i,j\in[N]\), \(T_i\unknown\subseteq S_j\).

It is well-known that Bichromatic Subset Query is SETH-hard (as it is equivalent to Orthogonal Vectors) due to the following celebrated result of Williams \[Wil05\].

**Theorem 2.12** (\[Wil05, Theorem 5.1\])**.** _Assuming SETH, for any_ \(\delta>0\)_, there exists a constant_ \(c=c(\delta)\) _such that Bichromatic Subset Query cannot be solved in_ \(N^{2-\delta}\) _time on instances with d=c_log_N._

## 3 Proof of Main Theorems

We give two simple reductions that imply the hardness of \(\gamma\)-ANN assuming SETH. To this end, we first present a reduction from Bichromatic Closest Pair to ANN. Then, we reduce \(\mathsf{SVP}_\infty^{\{0,1\}}\) and Bichromatic Subset Query to Bichromatic Closest Pair, thereby showing the conditional quantitative hardness of \(\gamma\)-ANN. Furthermore, we show that the hard approximation factor of 3, which our reduction from Bichromatic Subset Query achieves, is the best possible for any "natural" reduction from the Orthogonal Vectors problem (See Theorem 3.9). Since most known SETH-based hardness results are obtained via a reduction from Orthogonal Vectors, our result implies that showing hardness for approximation factor larger than 3 would require new techniques.

### 3.1 Bichromatic Closest Pair to ANN

A standard reduction from \[WW18\] shows that a sublinear algorithm for \(\gamma\)-ANN with polynomial preprocessing time implies a subquadratic algorithm for \(\gamma\)-approximate Bichromatic Closest Pair. We include a short proof of this fact for completeness.

**Lemma 3.1.** _Given numbers_ \(\delta>0\) _and C\>_1_, if there exists an algorithm for_ \(\gamma\)_-ANN under the_ \(\ell_p\) _norm with preprocessing time N<sup>C</sup> and query time_ \(N^{1-\delta}\)_, where N denotes the number of data points, then there exists a_ \(N^{2-\Omega\big(\frac{\delta}{C-1}\big)}\)_-time algorithm for_ \(\gamma\)_-approximate Bichromatic Closest Pair under_ \(\ell_p\).

_Proof._ Consider the following algorithm for \(\gamma\)-approximate Bichromatic Closest Pair under the \(\ell_p\) norm for two sets \(A=\{p_1,\dots,p_N\}\subset\mathbb{R}^d\) and \(B=\{q_1,\dots,q_N\}\subset\mathbb{R}^d\).

• Divide _A_ into \(N/\ell\) batches, each of size \(\ell\).<tbc>

• Preprocess each batch separately, constructing \(N/\ell\) many data structures.<tbc>

• For each query point _q<sub>j</sub>_, query each data structure created by the preprocessing step.<tbc>

