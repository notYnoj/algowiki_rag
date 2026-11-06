## 4 Faster Weighted and Unweighted Tree Edit Distance and APSP Equivalence

We also resolve Question 3 by providing an \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) time algorithm for unweighted TED. This is a significant improvement over Mao’s result \[Mao22\].

We achieve our result via a tight reduction to the Bounded Monotone Min-Plus product problem.

**Bounded Monotone Min-Plus Matrix Multiplication (MonMUL)**<br>
**Input:** An \(m\times n\) matrix _A_=(_a<sub>i,j</sub>_) and an \(n\times\ell\) matrix _B_=(_b<sub>i,j</sub>_) such that either for all \(i\in[m],j\in[n]\), \(a_{i,j}\le a_{i,j+1}\) ("row-monotone") or for all \(i\in[m],j\in[n]\), \(a_{i,j}\le a_{i+1,j}\) ("column-monotone").<br>
**Output:** The distance matrix _C=A⋆B_, where _C_=(_c<sub>i,j</sub>_) is defined as \(c_{i,j}=min_{k\in[1..n]}\{a_{i,k}+b_{k,j}\}\).

When \(m=n=\ell\) and _D_=O(_n_), MonMUL can be solved in \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) \[CDXZ22\].

We denote by \(\mathsf{T}_\mathsf{MonMUL}(m,n,\ell,D)\) the running time for computing MonMUL. When \(m=n=\ell=D\), we simply write T<sub>MonMUL</sub>(_m_) for the running time of MonMUL.

**Main Theorem 2.** _Let_ \(\mathbf{F},\mathbf{F}'\) _be two forests of size_ \(n=|\mathbf{F}|,m=|\mathbf{F}'|\) _with_ \(n\ge m\)_. Suppose that_ T<sub>_MonMUL_</sub>(_N,N,N,_D)=O(_f(N)g_(D))_. Then, there is an algorithm computing Unweighted Tree Edit Dis tance between_ \(\mathbf{F},\mathbf{F}'\) _in time_ \(\tilde{\mathcal{O}}\left((n/m)^{1+o(1)}\cdot\left(\mathsf{T}_\mathsf{_MonMUL}(m)+m^{2+o(1)}g(m)\right)\right)\).

The best known bound for the MonMUL running time \[CDXZ22, Dür23\] is \(\mathsf{T}_\mathsf{MonMUL}(N,N,N,D)=\tilde{\mathcal{O}}(N^{(2+\omega)/2}D^{1/2})\). Hence, Main Theorem 2 implies that given two forests of equal size, we can compute Unweighted Tree Edit Distance in \(\tilde{\mathcal{O}}(m^{(3+\omega)/2})\) time, matching the complexity of bounded monotone min-plus product \[CDXZ22\] and resolving Question 3.

More generally, we obtain the following result.

**Corollary 1.2.** _There is an algorithm for Unweighted TED running in time_ \(n^{1+o(1)}m^{(1+\omega)/2}\)_, where_ \(n=max(|\mathbf{F}|,|\mathbf{F}'|),m=min(|\mathbf{F}|,|\mathbf{F}'|)\).

**At the core of our results: TED alignment graphs.** The edit distance between two length-_n_ strings can be represented by examining the classical dynamic computation on an \[1_..(n_+1)\] \(\times\) \[1_..(n_+1)\] grid. The solution is then traced by following the shortest path from (1,1) to (_n_+1_,n_+1). Such graph-based representation is commonly referred to as an _alignment graph_.

The power of this representation is evident in the numerous results for string ED that have either emerged directly from this visualization or can be clearly illustrated through it (including but not limited to \[LV88, Tis06, CKW23, GKS19, CKW23, KNW24, GJKT24, CKM20, DGH<sup>+</sup>23, GK24\]). Consequently, it is not surprising that specific properties of alignment graphs, such as border-to-border distances, play a central role. For string ED, these distances can be computed in O(_n_<sup>2</sup>) time \[Sch95, Tis06, ACS08, Kle05\].

Alignment graphs for TED were introduced as a counterpart to those for ED and serve as a visualization tool for TED solutions. However, they appear predominantly in less recent works \[Tou05, BCH<sup>+</sup>07, MTWZU09\] and have played a less central role than in ED.

In this work, we reestablish the alignment graph for TED as a central tool and demonstrate that it provides a more powerful language and visualization framework for capturing the combinatorial structure of solutions than previously recognized. As a technical contribution, we show that in the alignment graph for TED, border-to-border distances can be computed in APSP time, while for unweighted TED, they can be determined in \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\).

**Prior attempts to reduce TED to APSP and MUL.**

At least two prior papers have attempted to leverage min-plus products for computing TED. The first of these works was by Chen \[Che01\], who introduced a dynamic programming scheme formulated using<tbc>

