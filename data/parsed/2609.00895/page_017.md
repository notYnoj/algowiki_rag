**Case B: marginal imbalance** _q<sub>e</sub>=q_+1 **or** _q<sub>o</sub>=q_+1<br>
Suppose first that<tbc>

\(q_e=q+1,q_o=q-1.\)

<tbc>Since \(W_E\in\mathcal{P}_q\) vanishes at _q_+1 distinct nodes, \(W_E\equiv 0\). Hence, by (36), \(\Phi^+=\Phi^-\), and therefore<tbc>

\(\Phi_q^+=\Phi_q^-.\)

<tbc>Using (31), this gives the compatibility condition

\(g_q^+=g_q^-,\)

which need not hold for a general _f_. Thus the leading-order system is degenerate; equivalently, \(\Lambda_0\) is singular.

Any invertibility of the full KEG-D matrix must therefore come from the _O_(1_/n_)-corrections in (34). For _p=r_=0, these corrections vanish, so the coefficient matrix remains singular for every _N_.

The case _q<sub>o</sub>=q_+1, _q<sub>e</sub>=q_-1 is analogous. Hence the subsequent analysis is restricted to the strict-balance condition _q<sub>e</sub>=q<sub>o</sub>=q_.

Finally, for odd _q_, the symmetric choice

\(\pm N,\pm(N-1),\dots\)

falls into the marginal case: among the 2_q_ selected indices, _q_+1 have the same parity as _N_, while _q_-1 have the opposite parity.

## 3.4 Asymptotic estimates for \(\widetilde{g}_k^\pm-g_k^\pm\)

We now restrict to the strictly balanced case and assume, in addition, that the limiting nodes are distinct within each parity class. Under these assumptions, the following lemma shows that a solution of (32) remains quantitatively close to the unique element of kerE whose coefficients of _x<sup>q</sup>_ are \(-g_q^+\) and \(-g_q^-\).

**Lemma 3.3** (Stability)**.** _Assume q<sub>e</sub>=q<sub>o</sub>=q, and let the indices satisfy_ (27) _with_<tbc>

\(lim_{N\rightarrow\infty}\frac{n_s}{N}=c_s\neq 0,s=1,\dots,2q.\)

<tbc>_Assume that the numbers_ \(\{c_s:s\in E\}\) _are pairwise distinct, as are_ \(\{c_s:s\in O\}\)_. Let_<tbc>

\(\Phi^\pm(x)=\sum_{k=0}^q\Phi_k^\pm x^k\)

<tbc>_satisfy_ (32) _with_<tbc>

\(\Phi_q^\pm=-g_q^\pm,\)

<tbc>_and put_<tbc>

\(\varepsilon:=max_s|\varepsilon_s|.\)

<tbc>_Then, for all sufficiently large N,_

\(\Phi_k^\pm+g_q^+U_k^\pm+g_q^-V_k^\pm=O\left(N^k\varepsilon+N^{k-q-1}\right),k=0,\dots,q-1,\) (39)

_where_ \(U_k^\pm\) _and_ \(V_k^\pm\) _denote the coefficients of x<sup>k</sup> in the polynomials_ \(U^\pm\) _and_ \(V^\pm\) _given by_ (38)_. Moreover, the matrix_ \(\Lambda_N\) _is invertible for all sufficiently large N._

