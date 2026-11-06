Let _N_ be a positive integer and index the _N<sup>d</sup>_ bits of INDEX<sub>_N<sup>d</sup>_</sub> by the vectors \(u=(u_1,\dots,u_d)\in[N]^d\). For each \(i\in[d]\), create a group of variables \(X_i=\{x_{i,p}:p\in[N]\}\). The variable _x<sub>i,u<sub>i</sub></sub>_ will occupy coordinate _i_ of the constraint associated with _u_.

We also need variables for the coordinates in \[_k_\]\\\[_d_\]. These coordinates must receive the basepoint 0 in Bob’s assignments. Using one variable in every constraint would give that variable degree _N<sup>d</sup>_, which is too large for Lemma 4.6. We instead create variables _w<sub>j,p</sub>_ for every \(j\in[k]\backslash[d]\) and \(p\in[N]\), and use _w_<sub>_j,u_<sub>1</sub></sub> in coordinate _j_ of the constraint associated with _u_.

Formally, for \(u\in[N]^d\), define \(C_u=R(v_1^u,\dots,v_k^u)\) by setting \(v_i^u=x_{i,u_i}\) for \(i\in[d]\) and \(v_j^u=w_{j,u_1}\) for \(j\in[k]\backslash[d]\).

Alice receives \(b\in\{0,1\}^{[N]^d}\) and streams _C<sub>u</sub>_ exactly when _b<sub>u</sub>_=1. Let _P<sub>b</sub>_ be the resulting instance. It uses at most _kN=O<sub>R</sub>(N_) variables and at most _N<sup>d</sup>_ constraints. Every variable belongs to at most _N_<sup>_d_-1</sup> of the constraints _C<sub>u</sub>_. Fixing the index of that variable fixes at least one coordinate of _u_. The constraints have distinct ordered scopes because the variables from the groups _X_<sub>1</sub>_,...,X<sub>d</sub>_ determine _u_. They also have distinct unordered scopes. Indeed, the groups _X_<sub>1</sub>_,...,X<sub>d</sub>_ are disjoint. If _C<sub>u</sub>_ and \(C_{u^\prime}\) had the same unordered scope, then for every \(i\in[d]\) they would contain the same variable from _X<sub>i</sub>_. This would give \(x_{i,u_i}=x_{i,u_i^\prime}\), and hence \(u_i=u'_i\), for every _i_. Therefore \(u=u'\). This last fact is relevant when _R_ is symmetric.

Bob receives \(q=(q_1,\dots,q_d)\in[N]^d\) and wants to recover _b<sub>q</sub>_. His goal is to make _C<sub>q</sub>_ see all 2_<sup>d</sup>_ tuples from Lemma 7.4. At the same time, every constraint _C<sub>u</sub>_ with \(u\neq q\) should miss at least one of the _d_ choices, so that its positive and negative contributions cancel. To achieve this, Bob changes only the variable _x<sub>i,q<sub>i</sub></sub>_ in each group _X<sub>i</sub>_ and leaves every other variable at the basepoint.

For each \(S\subseteq[d]\), Bob considers the following assignment. In group _X<sub>i</sub>_, the variable indexed by _q<sub>i</sub>_ receives _a<sub>i</sub>_ if \(i\in S\), and all other variables receive 0. Every variable _w<sub>j,p</sub>_ also receives 0. In symbols,

\(\alpha^S(x_{i,p})=\left\{\begin{array}{ c c }
a_i, & \text{if}i\in S\text{and}p=q_i, \\
0, & \text{otherwise},
\end{array}\right.\alpha^S(w_{j,p})=0.\)

Consider first the queried constraint _C<sub>q</sub>_. In coordinate \(i\in[d]\), it receives _a<sub>i</sub>_ when \(i\in S\) and 0 otherwise, while every coordinate in \[_k_\]\\\[_d_\] receives 0. Thus, as _S_ ranges over all subsets of \[_d_\], this constraint sees exactly the 2_<sup>d</sup>_ tuples from Lemma 7.4, and its signed contribution is _c_.

Now consider _C<sub>u</sub>_ for \(u\neq q\). Choose _i_ for which \(u_i\neq q_i\). The variable _x<sub>i,u<sub>i</sub></sub>_ always receives 0, whether or not _i_ belongs to _S_. Hence the satisfaction of _C<sub>u</sub>_ is unchanged when we replace _S_ by \(S\triangle\{i\}\). These two sets have opposite signs, so the contribution of _C<sub>u</sub>_ cancels. We have proved that<tbc>

\(\sum_{S\subseteq[d]}(-1)^{d-|S|}\mathbf{1}[C_u\text{is satisfied by}\alpha^S]=\left\{\begin{array}{ c c }
c, & \text{if}u=q, \\
0, & \text{if}u\neq q.
\end{array}\right.\)

<tbc>Summing this identity over the constraints that Alice streamed gives<tbc>

\(\sum_{S\subseteq[d]}(-1)^{d-|S|}\mathrm{val}_{P_b}(\alpha^S)=cb_q.\)

<tbc>This identity determines _b<sub>q</sub>_ from the 2_<sup>d</sup>_ numbers \(\mathrm{val}_{P_b}(\alpha^S)\) because \(c\neq 0\). The difficulty is that an Exact-CSP algorithm returns an optimum, not the value of a chosen assignment. By Lemma 4.6, Bob can append constraints that hard-pin a complete assignment and make the optimum reveal any one of these values. More precisely, for each \(S\subseteq[d]\), Lemma 4.6 gives an instance \(H_{\alpha^S}\) satisfying<tbc>

\(\mathrm{OPT}_\mathrm{max}(P_b\cup H_{\alpha^S})=|H_{\alpha^S}|+\mathrm{val}_{P_b}(\alpha^S).\)

