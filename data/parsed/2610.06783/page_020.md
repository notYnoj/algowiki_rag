<tbc>and similarly \(\Psi_{\lambda\tau^\prime}(b)=\Psi_{\tau^\prime}(B_\lambda)\). Thus, by induction, the leaf \(\lambda\tau'\) multiplies \(\Phi_{\lambda\tau^\prime}(a)\) by \(\Psi_{\lambda\tau^\prime}(b)\), and \(C_\lambda[w']=\sum_{\tau^\prime}\Phi_{\lambda\tau^\prime}(a)\Psi_{\lambda\tau^\prime}(b)\), summed over the \(\tau'\) contributing to \(w'\). Step (4) is the decoding: the leaves contributing to \(zw'\) are the \(\lambda\tau'\) with \(\lambda\) contributing to _z_ and \(\tau'\) contributing to \(w'\), so \(c[zw']=\sum_{\lambda\text{contributing to}z}C_\lambda[w']\) agrees with (2).

Since one application of the identity computes the coefficients of _G+E_, we expect that _L_ recursive applications should compute products of _L_ such coefficients. For a left variable _s_, a right variable _t_, and an output variable _z_, let

\(\gamma(s,t,z):=\sum_{\lambda\text{contributing to}z}\varphi_\lambda(s)\psi_\lambda(t),\) (3)

the coefficient of the monomial _stz_ on the left-hand side of the identity. By Lemma 6, it is also the coefficient of _stz_ in _G+E_, and we know that \(\gamma(s,t,z)\in\{0,\pm 1\}\).

**Lemma 8.** _For all arrays a,b and every output string w,_

\(\text{Mult}(a,b)[w]=\sum_{u,v}\gamma(u_1,v_1,w_1)\gamma(u_2,v_2,w_2)\cdots\gamma(u_L,v_L,w_L)a[u]b[v],\)

_the sum over all left strings u and right strings v._

_Proof._ By the definitions of \(\Phi_\tau\) and \(\Psi_\tau\), the coefficient of _a_\[_u_\]_b_\[_v_\] in (2) is \(\sum_\tau\prod_{\ell=1}^L\varphi_{\tau_\ell}(u_\ell)\psi_{\tau_\ell}(v_\ell)\), summed over the leaves \(\tau\) contributing to _w_. These are the leaves whose term at level \(\ell\) contributes to \(w_\ell\), independently for each \(\ell\), so this sum of products is the product of sums

\(\prod_{\ell=1}^L\sum_{\tau_\ell\text{contributing to}w_\ell}\varphi_{\tau_\ell}(u_\ell)\psi_{\tau_\ell}(v_\ell)=\prod_{\ell=1}^L\gamma(u_\ell,v_\ell,w_\ell)\)

by (3).

We will use both descriptions of Mult: Lemma 8 to read matrix products off it (Section 2.3.3), and the sum over leaves in (2) to skip the leaves that do not contribute to the wanted entries (Section 2.4).

## 2.3.3 Batch computation of multiple matrix products

We now explain the claim from the beginning of Section 2.3.1, that our recursive algorithm is simultaneously computing many matrix products. We will also show that the error _E_ is harmless, using the fact that each of its monomials uses an outer output variable, but at least one inner input variable.

The **_inner set_** of a left string is the set of levels at which it has a _p_ (as opposed to an _x_). It will tell us which of the 2_<sup>L</sup>_ matrix products the string belongs to. Similarly, the inner set of a right string is the set of levels at which it has a _q_ (as opposed to a _y_), and the inner set of an output string is the set of levels at which it has _z_<sub>0</sub> (as opposed to a _z<sub>ij</sub>_). The **_inner part_** of a string is the string of its variables at the levels of its inner set, in the order of the levels, and its **_outer part_** is the string of its variables at the other levels. A string is determined by its inner set, its outer part, and its inner part.

Fix \(m\ge 1\), and let _N_<sub>0</sub>:=3<sup>_L-m_</sup> and _D_:=4_<sup>m</sup>_. Of the 2_<sup>L</sup>_ matrix products, one for each set \(Q\subseteq\{1,\dots,L\}\) of levels at which the inner product is chosen, we will use only the \(\genfrac(){pt}{2}{L}{m}\) products<tbc>

