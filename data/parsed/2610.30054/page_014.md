<tbc>_and let_ \(\mu_2\) _be the induced map of_ \(\mu\) _on the subspaces,_<tbc>

\(\mu_2:U\times V_1\rightarrow W_1.\)

<tbc>_Let T, T_<sub>1</sub> _and T_<sub>2</sub> _be the tensors of_ \(\mu\), \(\mu_1\) _and_ \(\mu_2\)_. Then_

\(T\unknown_1T_1\oplus_1T_2.\)

_Proof._ Strassen’s proposition, applied to the filtrations \(V\supseteq V_1\supseteq 0\) and \(W\supseteq W_1\supseteq 0\) and the trivial filtration of _U_, gives \(T_1\oplus_1T_2\unknown T\). We give a proof for convenience of the reader, which also keeps the first leg fixed. Choose complements _V_<sub>2</sub> of _V_<sub>1</sub> in _V_ and _W_<sub>2</sub> of _W_<sub>1</sub> in _W_. Extending functionals on each summand of _V_ by zero on the other summand gives \(V^*=V_1^*\oplus V_2^*\), and \(W=W_1\oplus W_2\). The quotient maps restrict to isomorphisms \(V_2\cong V/V_1\) and \(W_2\cong W/W_1\). Since \(\mu(U\times V_1)\subseteq W_1\), the component of _T_ in \(U^*\otimes V_1^*\otimes W_2\) is zero. Under these isomorphisms, the components of _T_ in \(U^*\otimes V_2^*\otimes W_2\) and in \(U^*\otimes V_1^*\otimes W_1\) are _T_<sub>1</sub> and _T_<sub>2</sub>. So Lemma 2.3, applied with the first leg _U_<sup>∗</sup> and with the summands of the second and third legs in the orders \(V_2^*,V_1^*\) and _W_<sub>2</sub>_,W_<sub>1</sub>, gives \(T\unknown_1T_1\oplus_1T_2\).

More generally, we can use integer-valued weights to algebraically select a region to degenerate to, as follows.

**Lemma 2.6** (Strassen \[Str87, Theorem 6.1 and (6.6)\])**.** _Let_ \(n_1,n_2,n_3\ge 0\) _be integers, let_ \(S,T\in\mathbb{F}^{n_1}\otimes\mathbb{F}^{n_2}\otimes\mathbb{F}^{n_3}\) _be tensors, and write_ \(S=\sum_{a,b,c}S_{abc}e_a\otimes e_b\otimes e_c\) _and_ \(T=\sum_{a,b,c}T_{abc}e_a\otimes e_b\otimes e_c\) _in the standard bases. Suppose that there are functions_ \(w_i:[n_i]\rightarrow\mathbb{Z}\) _for_ \(i\in\{1,2,3\}\) _such that_ \(w_1(a)+w_2(b)+w_3(c)\ge 0\) _for all a, b and c with_ \(S_{abc}\neq 0\)_, and, for all a, b and c,_

\(T_{abc}=\left\{\begin{array}{ c c }
S_{abc} & \text{\textit{if}}w_1(a)+w_2(b)+w_3(c)=0, \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)

_Then_ \(S\unknown T\)_, and_ \(S\unknown_1T\) _if w_<sub>1</sub>=0.

_Proof._ For every \(i\in\{1,2,3\}\), let \(k_i\ge 0\) be an integer such that \(w_i(a)+k_i\ge 0\) for every \(a\in[n_i]\), with _k_<sub>1</sub>=0 if _w_<sub>1</sub>=0, and let _A<sub>i</sub>_ be the diagonal matrix with entries \(\varepsilon^{w_i(a)+k_i}\) for \(a\in[n_i]\). Let _k_:=_k_<sub>1</sub>+_k_<sub>2</sub>+_k_<sub>3</sub>. Then \((A_1\otimes A_2\otimes A_3)S=\sum_{a,b,c}\varepsilon^{w_1(a)+w_2(b)+w_3(c)+k}S_{abc}e_a\otimes e_b\otimes e_c\). Every nonzero term in this sum has exponent at least _k_, and the terms with exponent _k_ sum to \(\varepsilon^kT\). If _w_<sub>1</sub>=0, then _A_<sub>1</sub> is the identity.

Lemma 2.3 also follows from Lemma 2.6, applied in bases of _U_, _V_<sub>1</sub>, _V_<sub>2</sub>, _W_<sub>1</sub> and _W_<sub>2</sub> with _w_<sub>1</sub>=0, with _w_<sub>2</sub> equal to 1 on _V_<sub>1</sub> and 0 on _V_<sub>2</sub>, and with _w_<sub>3</sub> equal to -1 on _W_<sub>1</sub> and 0 on _W_<sub>2</sub>.

All the above degenerations are of a special kind, called _monomial degeneration_: in the chosen basis the degeneration matrices have at most one nonzero entry per row and per column, and that entry is a power of \(\varepsilon\). Strassen calls them _M_-degenerations \[Str87, Section 6\].

## 3 Degenerations among polynomial multiplication tensors

In this section we will construct, over every field, the degenerations that the proofs of Theorem 1.1 and Theorem 1.2 use: degenerations between unit tensors and polynomial multiplication tensors (Section 3.1), the degeneration from a partial direct sum to a direct sum (Section 3.2), and two degenerations between polynomial multiplication tensors (Section 3.3 and Section 3.4).

