• Second, note that C<sub>1</sub> is an indexed set that approximates C well. Indeed, for any \(c\in\mathcal{C}\), there exists \(c_1\in\mathcal{C}_1\) such that \(c-c_1\in\mathcal{I}\), where \(\mathcal{I}=\{(0,0),\dots,(0,\sqrt{n})\}\). Hence, we can expand X<sub>1</sub> to X so that \(\mathcal{X}_1+\mathcal{X}_1+\mathcal{I}\subseteq\mathcal{X}+\mathcal{X}\), which will then imply \(\mathcal{C}\subseteq\mathcal{X}+\mathcal{X}\). To achieve this, we set<tbc>

<tbc>\(\mathcal{X}=\mathcal{X}_1\cup\left\{(0,0),(0,1),\dots,(0,n^{1/4})\right\}\cup\left\{(0,n^{1/4}),(0,2\cdot n^{1/4}),\dots,(0,\sqrt{n})\right\}.\)<tbc>

<tbc>Finally, \(r(\mathcal{C})\le|\mathcal{X}|\le O(n^{1-\epsilon/4})\).

In summary, our low-rank 3SUM algorithm (Theorem 4.1) can solve the 3SUM instance (A,B,C) in subquadratic time \(O(n^{2-\epsilon^\prime})\).

## 2 Preliminaries

We use \[_n_\] to denote {1,2_,...,n_} for any integer \(n\ge 0\).

### 2.1 Additive Combinatorics

For two sets \(A,B\subseteq\mathbb{Z}\), define their _sumset_ \(A+B=\{a+b:a\in A,b\in B\}\) and _difference set_ \(A-B=\{a-b:a\in A,b\in B\}\). Let \(-A=\{-a:a\in A\}\). The _k_-fold sumset _kA_ is recursively defined by _kA_=(_k_-1)_A+A_ with 1_A=A_. Denote \(r_{A+B}(z)=|\{(x,y)\in A\times B:x+y=z\}|\). We often conveniently refer to _r_<sub>_A+B_</sub>(_z_) as the _multiplicity_ of _z_ in the sumset _A+B_. Similarly, the _multiplicity_ of _z_ in the _k_-fold sumset _kA_ means \(|\{(x_1,\dots,x_k)\in A^k:x_1+\cdots+x_k=z\}|\).

**Lemma 2.1** (Plünnecke-Ruzsa Inequality)**.** _For two sets A,B, if_ \(|A+B|\le K|A|\)_, then for any integers_ \(n,m\ge 0\), \(|mB-nB|\le K^{m+n}|A|\).

**Lemma 2.2** (Sparse Convolution, \[BFN22\])**.** _There is a deterministic algorithm that, given_ \(A,B\subseteq[-u,u]\)_, computes the sumset A+B along with the multiplicities r_<sub>_A+B_</sub> _in time_ \(|A+B|\cdot(\mathrm{log}u)^{O(1)}\).

The _additive energy_ between two sets \(A,B\subseteq\mathbb{Z}\) is<tbc>

\(E(A,B)=|\{(a_1,a_2,b_1,b_2)\in A^2\times B^2:a_1+b_1=a_2+b_2\}|=\sum_zr_{A+B}(z)^2.\)

<tbc>The additive energy of a set \(A\subseteq\mathbb{Z}\) is _E(A_)=_E(A,A_). We also define the following standard higher-order analogue of the additive energy, for any integer \(k\ge 1\):

\(T_k(A)=|\{(a_1,\dots,a_k,b_1,\dots,b_k)\in A^{2k}:a_1+\cdots+a_k=b_1+\cdots+b_k\}|.\)

The Balog-Szemerédi-Gowers (BSG) Theorem was originally proved in \[BS94, Gow01\]. We use the following algorithmic version of the BSG theorem appearing in \[ABF23, Theorem 3.3\] (which is an adaptation of \[CL15\]).

**Theorem 2.3** (BSG Theorem)**.** _If set A has additive energy_ \(E(A)\ge|A|^3/K\)_, then there exists a subset_ \(A'\subseteq A\) _such that_

• \(|A'|\ge\Omega(K^{-2}|A|)\)_, and_<tbc>

• \(|A'+A'|\le O(K^{24}|A|)\).<tbc>

