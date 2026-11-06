## D Proof of Lemma 6.3

Lemma 6.3.

\(\mathcal{S}(X)=\sum_{i=0}^\ell 2^i\mathcal{S}(X_i)=2^0\mathcal{S}(X_0)+\cdots+2^\ell\mathcal{S}(X_\ell).\)

_That is, for any_ \(t\in\mathcal{S}(X)\)_, there exist_ \(t_i\in\mathcal{S}(X_i)\) _such that_ \(t=\sum_{i=0}^\ell 2^it_i\).

_Proof._ It is obvious that \(\mathcal{S}(X)\supseteq\sum_{i=0}^\ell 2^i\mathcal{S}(X_i)\). We prove below that \(\mathcal{S}(X)\subseteq\sum_{i=0}^\ell 2^i\mathcal{S}(X_i)\), and Lemma 6.3 follows. Take an arbitrary \(t'\in\mathcal{S}(X)\), by definition there exist \(\eta_j\unknown u_j=\sum_{i=0}^\ell u_j[i]\cdot 2^i\) for all \(1\unknown j\unknown n\) such that

\(t'=\sum_jw_j\eta_j.\)

We claim that

Claim D.1. _If_ \(\eta_j\unknown u_j=\sum_{i=0}^{\ell_j}u_j[i]\cdot 2^i\)_, then there exist_ \(\eta_j[i]\)_’s such that_ \(\eta_j=\sum_{i=0}^{\ell_j}\eta_j[i]\cdot 2^i\) _and_ \(\eta_j[i]\unknown u_j[i]\) _for all_ \(0\unknown i\unknown\ell_j\).

Suppose the claim is true, then since _X<sub>i</sub>_ contains _u<sub>j</sub>_\[_i_\] copies of weight _w<sub>j</sub>_, we know that \(\sum_j\eta_j[i]w_j\in\mathcal{S}(X_i)\). Thus, \(\sum_j\eta_j[i]\cdot 2^iw_j\in 2^i\mathcal{S}(X_i)\), and consequently \(t'=\sum_i\sum_j\eta_j[i]\cdot 2^iw_j\in\sum_i2^i\mathcal{S}(X_i)\), and Lemma 6.3 is proved.

It remains to prove Claim D.1. We prove by induction on \(\ell_j\). Claim D.1 is obviously true for \(\ell_j=0\). Suppose it is true for \(\ell_j=h-1\), we prove that it is also true for \(\ell_j=h\). Towards this, let \(r_t\in\{0,1\}\) be the residue of _t_ modulo 2. Recall that \(u_j[i]\in[2,4)\) for \(0\unknown i\unknown\ell_j-1\). There are two possibilities: (i). If \(r_t\unknown u_j[0]-2\), then we let \(\eta_j[0]=r_t+2\); (ii). If \(u_j[0]-2<r_t\unknown u_j[0]\), then we let \(\eta_j[0]=r_t\). It is clear that \(\eta_j[0]\unknown u_j[0]\) is always true. Meanwhile, we also have \(\eta_j[0]+2>u_j[0]\).

By the fact that \(\eta_j[0]\equiv\eta_j\) (mod 2) and \(u_j[0]\equiv u_j\) (mod 2), \(\eta_j-\eta_j[0]\) and _u<sub>j</sub>-u<sub>j</sub>_\[0\] are multiples of 2. Using that \(\eta_j\unknown u_j\) and \(\eta_j[0]+2>u_j[0]\), we have<tbc>

\(\eta_j-\eta_j[0]<u_j-u_j[0]+2.\)

<tbc>Thus,<tbc>

\(\frac{\eta_j-\eta_j[0]}{2}<\frac{u_j-u_j[0]}{2}+1.\)

<tbc>Since \(\frac{\eta_j-\eta_j[0]}{2}\) and \(\frac{u_j-u_j[0]}{2}\) are both integers, we have that

\(\frac{\eta_j-\eta_j[0]}{2}\unknown\frac{u_j-u_j[0]}{2}=\sum_{i=0}^{\ell-1}u_j[i+1]\cdot 2^i.\)

Using the induction hypothesis, there exists \(\bar{\eta}_j[i]\) such that \(\frac{\eta_j-\eta_j[0]}{2}=\sum_{i=0}^{\ell-1}\bar{\eta}_j[i]\cdot 2^i\) where \(\bar{\eta}_j[i]\unknown u_j[i+1]\). Recall that \(\eta_j[0]\unknown u_j[0]\). Consequently, Claim D.1 is true. \(\square\)

## References

