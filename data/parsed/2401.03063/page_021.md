infer, more generally, a lower bound on the variance from a random perturbation that has an effect on the expectation. More specifically, here, the random perturbation is to pick, in the binary case, a random 1 from the letters (if there is at least one), and to turn it into a 0. The original letters are denoted by _Z_<sub>1</sub>_,...,Z_<sub>2_n_</sub>, the new letters (with a 1 turned into a 0) by \(\tilde{Z}_1,\dots,\tilde{Z}_{2n}\). We refer to \[19\] and \[13\] for a more formal definition of \(\tilde{Z}\). Theorem 2.2/Theorem 2.1 there implies, in particular, that for any \(\delta\in(0,\alpha_1-\alpha_2)\), where \(\alpha_1\), \(\alpha_2\) are constants defined there such that \(\alpha_1>\alpha_2\), for _n_ large enough,<tbc>

\(\mathbb{E}\left(LCS(Z)-LCS(\tilde{Z})\right)\ge\delta.\)

<tbc>From this, it is natural to try to prove that _B_<sub>2_n_</sub>(2_n_) is greater than some absolute constant, to infer that the variance has linear order. Let, for all \(z\in\{0,1\}^{2n}\), \(x\in\{0,1\}\) and \(k\in\{1,\dots,2n\}\), _z<sup>k,x</sup>_:=(_z_<sub>1</sub>_,...,z_<sub>_k_-1</sub>_,x,z_<sub>_k_+1</sub>_,...,z_<sub>2_n_</sub>). Consider the modifications of _Z_, _Z_<sup>_N,_1</sup> and _Z_<sup>_N,_0</sup>, with _N_ picked in {1_,...,n_} uniformly. Intuitively, this is "almost" like the previous pair \((Z,\tilde{Z})\). But it is easier to write _B_<sub>2_n_</sub>(2_n_) in terms of \(\mathbb{E}\left(LCS(Z^{N,1})-LCS(Z^{N,0})\right)\). Indeed, we have

\(B_{2n}(2n)=\mathbb{E}\frac{1}{2(2n)!}\sum_{i\in\mathfrak{S}_{2n}}(S-S^{i_{2n}})(S^{i_1,\dots,i_{2n-1}}-S^{i_1,\dots,i_{2n}})\)<br>
\(=\mathbb{E}\frac{1}{2(2n)}\sum_{k=1}^{2n}(S-S^k)(S^{\{1,\dots,2n\}\backslash\{k\}}-S^{\{1,\dots,2n\}}),\)

conditioning on \((Z_{i_{2n}},Z'_{i_{2n}})\) (first term when its (0,1), second term (1,0), the other terms are null) we get

\(B_{2n}(2n)=\mathbb{E}\frac{1}{2(2n)}\sum_{k=1}^{2n}\left(LCS(Z^{k,0})-LCS(Z^{k,1})\right)\left(LCS(Z^{k,0})-LCS(Z^{k,1})\right)p(1-p)\)<br>
\(+\mathbb{E}\frac{1}{2(2n)}\sum_{k=1}^{2n}\left(LCS(Z^{k,1})-LCS(Z^{k,0})\right)\left(LCS(Z^{k,1})-LCS(Z^{k,0})\right)p(1-p),\)

and by independence,<tbc>

\(B_{2n}(2n)=\frac{1}{2n}\sum_{k=1}^{2n}\left(\mathbb{E}\left(LCS(Z^{k,1})-LCS(Z^{k,0})\right)\right)^2p(1-p),\)

<tbc>so by the Cauchy-Schwarz inequality,

\(B_{2n}(2n)\ge\left(\mathbb{E}\left(LCS(Z^{N,1})-LCS(Z^{N,0})\right)\right)^2p(1-p).\) (4.2)

We next provide a lower bound on \(\mathbb{E}\left(LCS(Z^{N,0})-LCS(Z^{N,1})\right)\). First note that if _N_<sub>1</sub> denotes the number of ones, for any \(\ell\in\{1,\dots,2n\}\), (_Z_<sup>_N,_1</sup>_,Z_<sup>_N,_0</sup>) conditionally on \(N_1(Z^{N,1})=\ell\) has the same distribution as \((Z,\tilde{Z})\) conditionally on \(N_1(Z)=\ell\). Indeed, this is the uniform distribution on all the possible pairs of 2_n_ bits, the first one having _k_ ones and the second one being identical except exactly for a 1 turned into a 0. To simplify the notations, for \(\ell\in\{0,\dots,2n\}\), let<tbc>

\(f(\ell):=\mathbb{E}\left(LCS(Z)-LCS(\tilde{Z})|N_1(Z)\right).\)

<tbc>We have<tbc>

\(\mathbb{E}\left(LCS(Z)-LCS(\tilde{Z})\right)=\sum_{\ell=1}^{2n}f(\ell)\mathbb{P}(N_1(Z)=\ell)=\mathbb{E}\left(f(N_1(Z))\right),\)

<tbc>while, since _f_(0)=0,

