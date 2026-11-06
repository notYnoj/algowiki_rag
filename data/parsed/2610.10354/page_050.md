**Theorem 1.12** (Min-Witness Convolution)**.** _Min-Witness Convolution cannot be solved in time_ \(O(n^{4/3-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong Min-Plus Convolution Hypothesis fails._

**Proof.** Suppose Min-Witness Convolution can be solved in \(O(n^{4/3-\epsilon})\) time for some \(\epsilon>0\) by an algorithm A. In order to show this contradicts the Strong Min-Plus Convolution Hypothesis, by Corollary 5.2 with \(\gamma=\frac{2}{3}\), it suffices to give a truly sub-quadratic time algorithm for \(\text{MPConvList}(n,n^{2/3}|u\le n^{1/3})\). Let (_A,B_) be such a Min-Plus Convolution Listing instance. By Lemma 6.1, we can further assume no elements in _B_ appear more than \(n^{2/3+\epsilon/3}\) times. Let _C=A∗B_, which can be computed in \(\widetilde{O}(n^{4/3})\) time.

For every \(b\in[n^{1/3}]\), we solve a sub-instance between (_A,B<sub>b</sub>_), where _B<sub>b</sub>_\[_j_\]=0 if _B_\[_j_\]=_b_, and \(B_b[j]=\infty\) otherwise. Using Lemma 6.4 with \(\ell=1/3+2\epsilon/3\), we can list up to \(n^{1/3+2\epsilon/3}\) witnesses per output in _C<sub>b</sub>=A∗B<sub>b</sub>_. The total cost for calling Lemma 6.4 over \(b\in[n^{1/3}]\) is \(O(n^{5/3+2\epsilon/3-\epsilon}\cdot n^{1/3})=O(n^{2-\epsilon/3})\).

If _C<sub>b</sub>_\[_k_\]=_C_\[_k_\]-_b_, and Lemma 6.4 lists fewer than \(n^{1/3+2\epsilon/3}\) witnesses for _C<sub>b</sub>_\[_k_\], then we have listed all witnesses (_i,j_) satisfying _B_\[_j_\]=_b_ for _C_\[_k_\]. Otherwise, if we have not listed _n_<sup>2/3</sup> witnesses for _C_\[_k_\], we enumerate all non-\(\infty\) indices in _B<sub>b</sub>_ (there can be at most \(n^{2/3+\epsilon/3}\) such indices), and check whether it forms a witness for _C_\[_k_\]. The total number of such enumerations is \(O(n\cdot n^{1/3-2\epsilon/3})\), as for each _C_\[_k_\], one such enumeration increases the number of witnesses found for it by at least \(n^{1/3+2\epsilon/3}\). Hence, the total cost is \(O(n\cdot n^{1/3-2\epsilon/3}\cdot n^{2/3+\epsilon/3})=O(n^{2-\epsilon/3})\), which is truly subquadratic as desired.

## 7 Asymmetric BSG Theorem

In this section, we show an algorithmic version of the Asymmetric BSG Theorem (originally proved by Tao and Vu \[TV06, Section 2.6\]), stated as follows.

**Theorem 2.4** (Asymmetric BSG Theorem)**.** _Let_ \(\epsilon>0\) _and_ \(0<\alpha\le 1\)_. Let_ \(A,B\subseteq\mathbb{Z}\) _be sets with energy_ \(E(A,B)\ge\alpha|A|^2|B|\)_. Then there are sets_ \(H,\Lambda\subseteq\mathbb{Z}\) _and some_ \(K\le O_\epsilon(\alpha^{-O_\epsilon(1)}(1+|B|/|A|)^\epsilon)\) _such that:_

• \(|H+H|\le K|H|\),<tbc>

• \(|H||\Lambda|\le K|B|\),<tbc>

• \(|A\cap H|\ge|A|/K\) _and_ \(|B\cap(H+\Lambda)|\ge|B|/K\).

_Moreover, there is a randomized algorithm to compute_ \(H,\Lambda\) _in time_ \(\widetilde{O}((|A|+|B|)K)\).

### 7.1 Preliminary Lemmas

Our algorithmic proof of Theorem 2.4 is heavily based on the original proof for the non-algorithmic version by Tao and Vu \[TV06, Section 2.6\]. We turn each step into an efficient algorithm using mostly basic ideas.

We start with the following definition from \[TV06, Definition 2.32\]:

**Definition 7.1** (Symmetry Sets)**.** For \(A\subseteq\mathbb{Z}\) and \(0<\alpha\le 1\), we define the _symmetry set_<tbc>

\(\text{Sym}(A;\alpha)=\{x\in A-A:r_{A-A}(x)\ge\alpha|A|\}.\)

