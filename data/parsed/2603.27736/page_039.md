to _B_\[_k,j_\]+_u_, and where we delete all edges with \(A[i,k]=\perp\) or \(B[k,j]=\perp\). Observe that the _I-J_ distances in the resulting graph are exactly _A∗B_ plus an additive offset of 2_u_ (except that for distances larger than 2_u_ which correspond to \(\perp\)-entries in _A∗B_). The reason is that any path of length more than 2 has length at least 4 and thus weight at least 4_u_, which exceeds any entry in _A∗B_ plus 2_u_.

But \(\mathrm{MinPlus}(n,n,n|u<n^\delta/2)=O(n^{2+\delta-\epsilon})\) contradicts the Strong APSP Hypothesis by Corollary 5.4 applied with \(\alpha=\delta\) (observing that the constant factor 1/2 in the universe bound can easily be removed).

## 5.3 Doubling Reduction

Next, we prove the following "doubling reduction" which allows to reduce from arbitrary instances of Min-Plus Product to Low-Doubling instances.

**Lemma 5.7** (Doubling Reduction)**.** _For all parameters n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>_,K with_ \(n_2\le n_1,n_3\) _it holds that:_

\(\mathrm{MinPlus}(n_1,n_2,n_3|u)\le\big(K\cdot\mathrm{MinPlus}(n_1,n_2,n_3|u;D\le n_2;\rho\le 1/D;K)+\frac{n_1n_2n_3}{K^{1/300000}}\big)^{1+o(1)}\cdot\mathrm{log}u.\)

**Proof.** Let \(L=\lceil\mathrm{log}u\rceil\). The proof of the lemma relies on a scaling trick over _L_ scales, and requires some notational setup. In analogy to Lemma 5.3, we call _k_ a _witness_ of (_A∗B_)\[_i,j_\] if (_A∗B_)\[_i,j_\]=_A_\[_i,k_\]+_B_\[_k,j_\], and we call _k_ an _q-pseudo-witness_ if _A_\[_i,k_\]+_B_\[_k,j_\]_\<(A∗B_)\[_i,j_\]+_q_. (Note that the definition of pseudo- witness differs slightly from Lemma 5.3.)

For each \(0\le\ell\le L\), define the matrices \(A_\ell=\lfloor A/2^\ell\rfloor\) and \(B_\ell=\lfloor B/2^\ell\rfloor\). We partition each such matrix into two submatrices, \(A_\ell=A_{\ell,0}\sqcup A_{\ell,1}\), where \(A_{\ell,0}\) retains all entries with \(A[i,k]\mathrm{mod}2^\ell<2^{\ell-1}\), and \(A_{\ell,1}\) retains all other entries. Similarly, partition \(B_\ell=B_{\ell,0}\sqcup B_{\ell,1}\). A observation related to this scaling setup is the following:

**Claim 5.8.** _For each_ \((i,j)\in[n_1]\times[n_3]\) _and each scale_ \(0\le\ell\le L\)_, there is some pair_ \(x,y\in\{0,1\}\) _such that:_

(_i)_ \((A_{\ell,x}*B_{\ell,y})=\lfloor((A*B)[i,j]-(x+y)2^{\ell-1})/2^\ell\rfloor\),<tbc>

_(ii)_ _some witness of_ \((A_{\ell,x}*B_{\ell,y})[i,j]\) _is a witness of_ (_A∗B_)\[_i,j_\]_, and_<tbc>

_(iii)_ _every witness of_ \((A_{\ell,x}*B_{\ell,y})[i,j]\) _is a_ \(2^\ell\)_-pseudo-witness of_ (_A∗B_)\[_i,j_\].

**Proof.** To see this, let _k_<sup>∗</sup> be an arbitrary witness of (_A∗B_)\[_i,j_\]. By construction each non-\(\perp\) entry in \(A_\ell\) shows up either in \(A_{\ell,0}\) or \(A_{\ell,1}\). Take \(x\in\{0,1\}\) such that \(A_{\ell,x}[i,k^*]\neq\perp\). Similarly, take \(y\in\{0,1\}\) so that \(B_{\ell,y}[k^*,j]\neq\perp\). Now consider an arbitrary \(k\in[n_2]\) with \(A_{\ell,x}[i,k]\neq\perp\) and \(B_{\ell,y}[k,j]\neq\perp\), and note that<tbc>

\(A_{\ell,x}[i,k]+B_{\ell,y}[k,j]=\big\lfloor\frac{A[i,k]}{2^\ell}\big\rfloor+\big\lfloor\frac{B[k,j]}{2^\ell}\big\rfloor=\frac{A[i,k]+B[k,j]-(A[i,k]\mathrm{mod}2^\ell)-(B[k,j]\mathrm{mod}2^\ell)}{2^\ell}.\)

<tbc>By definition, \(A[i,k]\mathrm{mod}2^\ell\) falls into the range \(x2^{\ell-1}+[0,2^{\ell-1})\), and \(B[k,j]\mathrm{mod}2^\ell\) is in \(y2^{\ell-1}+[0,2^{\ell-1})\). In particular, we obtain the upper bound<tbc>

\(A_{\ell,x}[i,k]+B_{\ell,y}[k,j]\le\frac{A[i,k]+B[k,j]-(x+y)2^{\ell-1}}{2^\ell},\)

<tbc>and the lower bound<tbc>

\(A_{\ell,x}[i,k]+B_{\ell,y}[k,j]>\frac{A[i,k]+B[k,j]-(x+y)2^{\ell-1}-2^\ell}{2^\ell}=\frac{A[i,k]+B[k,j]-(x+y)2^{\ell-1}}{2^\ell}-1,\)

<tbc>Recalling that this is an integer, we must have<tbc>

\(A_{\ell,x}[i,k]+B_{\ell,y}[k,j]=\big\lfloor\frac{A[i,k]+B[k,j]-(x+y)2^{\ell-1}}{2^\ell}\big\rfloor.\)

