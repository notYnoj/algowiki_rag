Note that \(J_1^+\unknown J_1^-\unknown\cdots\unknown J_k^+\unknown J_k^-\) form a partition of \(\{i\in I_{\mathcal{W}_1}:\mathrm{rank}(i)\le 2^k-1\}\).

Denote<tbc>

\(J_{\le j}^+=J_1^+\cup\cdots\cup J_j^+,\)

<tbc>and

\(J_{\le j}^-=J_1^-\cup\cdots\cup J_j^-.\)

Note the the rank partitioning defined in Definition 3.5 can be computed in _O(n+w_<sub>max</sub>log_w_<sub>max</sub>) time.

Our rank partitioning is motivated by the following additive-combinatorial Lemma 3.6, which can be derived from the results of Bringmann and Wellnitz \[BW21\]. Recall the _r-support_ supp_<sub>r</sub>(X_) of a multiset _X_ is the set of items in _X_ with multiplicity at least _r_.

**Lemma 3.6.** _There is a constant C such that the following holds. Suppose two multisets A,B supported on_ \[_N_\] _satisfy_

\(|\mathrm{supp}_r(A)|\ge C\sqrt{N/r}\cdot\sqrt{\mathrm{log}(2N)}\) (10)

_for some_ \(r\ge 1\)_, and_

\(\Sigma(B)\ge\Sigma(A)-N.\) (11)

_Then,_ \(\mathcal{S}^*(A)\cap\mathcal{S}^*(B)\neq\varnothing\).

Lemma 3.6 is partly inspired by \[CLMZ24, Lemma 3.2\] which generalized their fine-grained proximity result (Lemma 3.1) from supp(_A_) to supp_<sub>r</sub>(A_).<sup>10</sup> We include a proof of Lemma 3.6 in Appendix B.3.

Using Lemma 3.6, we obtain the following structural lemma for the rank partitioning. Recall the definition of _I_<sub>W<sub>1</sub></sub>-optimal partial solutions from Definition 2.5.

**Lemma 3.7** (Rank partitioning structural lemma)**.** _For a universal constant C, the partition_ \(J_1^+\unknown J_1^-\unknown\cdots\unknown J_k^+\unknown J_k^-\subseteq I_{\mathcal{W}_1}\) _from Definition 3.5 satisfies the following properties for every I_<sub>W<sub>1</sub></sub>_-optimal partial solution_ \((A',B')\):

1. \(A'\subseteq J_{\le k}^+\) _and_ \(B'\subseteq J_{\le k}^-\).<tbc>

_2._ _For all_ \(1\le j\le k\), \(|A'\cap J_{\le j}^+|\le m_j\) _and_ \(|B'\cap J_{\le j}^-|\le m_j\)_, where_<tbc>

\(m_j:=C\cdot 2^{j/2}\cdot\sqrt{w_\mathrm{max}\mathrm{log}(2w_\mathrm{max})}.\) \(\text{(12)}\)

_3._ _For all_ \(1\le j\le k\),<tbc>

\(|\{w\in\mathcal{W}_1:I_{\{w\}}\cap J_{j-1}^+\subseteq A'\text{\textit{and}}I_{\{w\}}\cap J_j^+\neq\varnothing\}|\le b_j,\)

_and similarly_<tbc>

\(|\{w\in\mathcal{W}_1:I_{\{w\}}\cap J_{j-1}^-\subseteq B'\text{\textit{and}}I_{\{w\}}\cap J_j^-\neq\varnothing\}|\le b_j,\)

_where_<tbc>

\(b_j:=C\cdot 2^{-j/2}\cdot\sqrt{w_\mathrm{max}\mathrm{log}(2w_\mathrm{max})},\) \(\text{(13)}\)

_and_ \(J_0^+:=J_0^-:=\varnothing\).

<sup>10</sup>Their generalization of Lemma 3.1 is not applicable in our first-stage algorithm. Note that Lemma 3.6 is incomparable to Lemma 3.1 even when _r_=1.

