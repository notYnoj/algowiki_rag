<tbc>as a union of \(O((|S\cap X^{(\ell)}|/b+1)\mathrm{log}n)\) disjoint canonical subsets \(S_j^{(\ell)}\in\mathcal{C}^{(\ell)}\). We have \(|S_j^{(\ell)}\cap X'|,|S_j^{(\ell)}\cap X''|\le|S_j^{(\ell)}|/2+\widetilde{O}(\sqrt{b})\) for each such subset _S<sub>j</sub>_. Summing over \(S_j^{(\ell)}\) gives

\(\mathrm{max}\{|\hat{S}^{(\ell)}\cap X'|,|\hat{S}^{(\ell)}\cap X''|\}\le|\hat{S}^{(\ell)}|/2+\widetilde{O}((|S\cap X^{(\ell)}|/b+1)\cdot\sqrt{b})\)<br>
\(=|\hat{S}^{(\ell)}|/2+\widetilde{O}(|S\cap X^{(\ell)}|/\sqrt{b}+\sqrt{b}).\)

Let \(\hat{S}=\bigcup_\ell\hat{S}^{(\ell)}\). Then \(\sigma(\hat{S})=\sigma(S)\). Now, \(\frac{1}{1+\delta}\sigma(\hat{S}\cap X')\le\sum_\ell(1+\delta)^\ell|\hat{S}^{(\ell)}\cap X'|\), and \(\frac{1}{1+\delta}\sigma(\hat{S}\cap X'')\le\sum_\ell(1+\delta)^\ell|\hat{S}^{(\ell)}\cap X''|\). Thus,

\(\mathrm{max}\{\sigma(\hat{S}\cap X'),\sigma(\hat{S}\cap X'')\}\le\sum_\ell(1+\delta)^\ell\left(|\hat{S}^{(\ell)}|/2+\widetilde{O}(|S\cap X^{(\ell)}|/\sqrt{b}+\sqrt{b})\right)+O(\delta t)\)<br>
\(\le\sigma(\hat{S})/2+\widetilde{O}\left(\sigma(S)/\sqrt{b}+\sum_\ell(1+\delta)^\ell\sqrt{b}\right)+O(\delta t)\)<br>
\(=\sigma(\hat{S})/2+\widetilde{O}(t/\sqrt{b}+\sqrt{b}u/\delta+\delta t)=\sigma(\hat{S})/2+\widetilde{O}(t/\sqrt{b}+bu).\)

## 3.3 Putting everything together

We are now ready to derandomize Bringmann, Fischer, and Nakos’ algorithm \[BFN25\]. The algorithm is a multi-way divide-and-conquer, so we first extend halvers to split into _r_ parts:

**Definition 3.8.** _Given a set X of positive integers, and numbers t and_ \(\Delta\)_, a_ weighted _r_-way \((t,\Delta)\)-splitter _of X is a partition of X into r disjoint subsets X_<sub>1</sub>_,...,X<sub>r</sub> with the following property:_

_For every subset_ \(S\subseteq X\) _with_ \(\sigma(S)\le t\)_, there exists a subset_ \(\hat{S}\subseteq X\) _with_ \(\sigma(\hat{S})=\sigma(S)\)_, and_ \(\sigma(\hat{S}\cap X_j)\le\sigma(\hat{S})/r+\Delta\) _for each_ \(j\in\{1,\dots,r\}\).

**Corollary 3.9** (Fast _r_-way splitter construction)**.** _Given a set X of n integers in_ \[_u_\] _and numbers t,b,r, we can compute a weighted r-way_ \((t,\widetilde{O}((t/\sqrt{b}+bu)\mathrm{log}r))\)_-splitter of X in_ \(\widetilde{O}(rb^{O(1)}|\Sigma(X)\cap[t]|\sqrt{n})\) _deterministic time._

_Proof._ Just apply Lemma 3.7 recursively for log_r_ levels.

**Theorem 3.10.** _Given a set X of n integers in_ \[_t_\]_, we can compute_ \(\Sigma(X)\cap[t]\) _in_ \(\widetilde{O}(|\Sigma(X)\cap[t]|\sqrt{n})\) _deterministic time._

_Proof._ Let \(u_S=\lceil t/(r^6\mathrm{log}^ct)\rceil\) for a sufficiently large constant _c_. Let \(X_S=X\cap[u_S]\) and \(X_L=X\cap(u_S,t]\). The following is a reinterpretation of Bringmann, Fischer, and Nakos’ algorithm \[BFN25\]:

1. Compute a weighted _r_-way (_t,t/r_<sup>2</sup>)-splitter (_X_<sub>1</sub>_,...,X<sub>r</sub>_) of _X<sub>S</sub>_ in \(\widetilde{O}(r^{O(1)}|\Sigma(X)\cap[t]|\sqrt{n})\) deterministic time, by applying Corollary 3.9 with \(b=\widetilde{O}(r^4)\) and _u_ replaced by _u<sub>S</sub>_ (the parameters are chosen so that \((t/\sqrt{b}+bu_S)\mathrm{log}r\checkmark t/r^2\)).<tbc>

2. Recursively compute \(A_j=\Sigma(X_j)\cap[t/r+t/r^2]\) for each \(j\in\{1,\dots,r\}\).<tbc>

3. Compute the sumset \(A=A_1+\cdots+A_r\) by applying Lemma 3.1 _O(r_) times in \(\widetilde{O}(r|A|)\) deterministic time.<tbc>

