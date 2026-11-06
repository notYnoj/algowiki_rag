Since \(j_i+1\le t+1\) and \(\ell+1+\Lambda=K/2\),<tbc>

\(c_i\le(t+1)(\ell+1)+\Lambda\le(t+1)K/2.\)

<tbc>The first step uses \(c_i=(j_i+1)(\ell+1)+\Lambda\) and \(j_i+1\le t+1\). The second step uses \(\Lambda\ge 0\), \(t+1\ge 1\), and \(K=2(\ell+1+\Lambda)\). Consequently,<tbc>

\(|W|\ge 2^{1-c_i}|U_i|\ge 2^{1-(t+1)K/2-(K+1)(t+1)}N\ge 2.\)

<tbc>The first step was proved above. The second step uses the bound on _c<sub>i</sub>_ and Eq. (15). The third step uses \(N\ge 2^{(2K+1)(t+1)}\); after substitution, the exponent is \(1+K(t+1)/2\ge 1\). It follows that

\(|U_{i+1}|\ge|W|-1\ge|W|/2\ge 2^{-c_i}|U_i|.\)

The first step uses \(W\backslash\{v_i\}\subseteq U_{i+1}\), the second step uses \(|W|\ge 2\), and the third step uses \(|W|\ge 2^{1-c_i}|U_i|\). Together with invariant (c) at index _i_, this establishes invariant (c) at index _i_+1.

The product formula in invariant (b) follows from the definition of \(\tau_{i+1}\). Also, _W_\\{_v<sub>i</sub>_} is nonempty. For any _u_ in this set, the preceding conditioning bound gives \(\tau_{i+1}\le\mu_{S_{i+1}}(u)\), while Lemma 3.2-(a) gives \(\mu_{S_{i+1}}(u)\le 1\). The latter bound applies because \(\mu_{S_{i+1}}\) is a level-(_r-i_-1) pseudo-distribution and \(r-i-1\ge 1\). This establishes invariant (b) at the next index.

_Termination._ Each step adds at least log(3/2) to the sum in Eq. (13), while that sum is at most _t_+1. The construction must therefore reach an index _i_<sub>∗</sub> with \(d(U_{i_*})\le\delta\). Take _S_:=_S_<sub>_i_<sub>∗</sub></sub> and \(\tau:=\tau_{i_*}\). Invariant (a) and the bound \(i_*\le 2t+1\) establish the required properties of _S_. Invariant (b) gives \(\tau\in[2^{-(t+1)},1]\), and Eq. (15) gives the required size bound.

## 4.4 Computing a pseudo-distribution

The next lemma computes a feasible pseudo-distribution whose total marginal mass is at least half the promised lower bound on the independent-set size. Its rational entries allow the subsequent enumeration and threshold comparisons to use exact arithmetic.

**Lemma 4.4** (Computing a pseudo-distribution)**.** _Let_ \(r,t\ge 1\) _be integers with_ \(N\ge 2^t\)_. There is a deterministic algorithm running in time N_<sup>_O(r_)</sup> _that outputs a level-r pseudo-distribution_ \(\mu\) _with rational values. If_ \(\alpha(G)\ge 2^{-t}N\)_, then the output satisfies_ \(\sum_{u\in V}\mu(u)\ge 2^{-(t+1)}N\).

_Proof._ Let I_<sub>k</sub>_ be the family of independent sets of size at most _k_, and write \(n_k:=|\mathcal{I}_k|\le(N+1)^k\). Consider vectors \(y=(y_T)_{T\in\mathcal{I}_{2r}}\) with \(y_\emptyset=1\). Define \(\mu_y(T):=y_T\) for \(T\in\mathcal{I}_{2r}\), and \(\mu_y(T):=0\) for \(T\in\mathcal{V}_{2r}\) containing an edge. Let

\(M(y):=(m_{A,B})_{A,B\in\mathcal{I}_r},m_{A,B}:=\left\{\begin{array}{ c c }
y_{A\cup B}, & \text{if}A\cup B\text{is independent}, \\
0, & \text{otherwise}.
\end{array}\right.\)

This is well defined because \(|A\cup B|\le 2r\).

_Claim 1:_ \(\mu_y\) _is a level-r pseudo-distribution if and only if_ \(M(y)\unknown 0\). The conditions in Definition 3.1-(a) and Definition 3.1-(b) hold by construction. If \(A\in\mathcal{V}_r\) contains an edge, then \(A\cup B\) contains an edge for every _B_, so the row of \(M_r[\mu_y]\) indexed by _A_ is zero. Hence \(M_r[\mu_y]\) is positive semidefinite if and only if its principal submatrix on I_<sub>r</sub>_, which is _M(y_), is positive semidefinite.

Let<tbc>

\(F:=\{y:y_\emptyset=1,M(y)\unknown 0\},f(y):=\sum_{u\in V}y_{\{u\}},\text{OPT}:=max_{y\in F}f(y).\)

