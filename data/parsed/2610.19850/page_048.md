<tbc>have \(|S\cap A_i|\le 1\), otherwise there is an (_a,b_)-path in _G_\\_S_. On the other hand, \(|S\cap A_i|\ge 3\) would contradict the minimality of _S_. W.l.o.g., let \(S\cap A_i=\{\alpha_i,\beta_i,\overline{\beta_i}\}\): there is no simple (_a,b_)-path in _G_ whose intersection with _S_ is the single vertex \(\alpha_i\), contradicting Lemma 2. Hence, \(|S\cap A_i|=2\). Cases \(S\cap A_i=\{\alpha_i,\overline{\beta_i}\}\) or \(\{\beta_i,\overline{\alpha_i}\}\) are not possible, otherwise _S_ is not an (_a,b_)-separator. Similarly, cases \(\{\alpha_i,\overline{\alpha_i}\}\) and \(\{\beta_i,\overline{\beta_i}\}\) contradict the minimality of _S_ (either _a<sub>i</sub>_ or _b<sub>i</sub>_ do not satisfy Lemma 2). All in all, the only possible choice for each \(S\cap A_i\) is either \(\{\alpha_i,\beta_i\}\) or \(\{\overline{\alpha_i},\overline{\beta_i}\}\), confirming the form of sets \(T_i(\Phi,\sigma)\). In brief, we just proved that any minimal (_a,b_)-separator is formed as \(M\cup\{T_i(\Phi,\sigma)\}_{1\le i\le n}\), where \(\sigma\) is a variable assignment. Let us show that \(\sigma\) is indeed a truth assignment.

For each clause vertex _C<sub>j</sub>_, there must be a \(\beta\)-vertex, _i.e._ \(\beta_i\) or \(\overline{\beta_i}\), adjacent to _C<sub>j</sub>_ which does not belong to _S_: otherwise, Lemma 2 would be contradicted. In summary, if \(\sigma\) is not a truth assignment, _S_ cannot be a minimal (_a,b_)-separator. For sure, \(\sigma\) is a truth assignment, fulfilling the claim.

As a conclusion, there exists a minimal (_a,b_)-separator extending _M_ in \(G(\Phi)\) iff the 3-SAT formula \(\Phi\) admits a truth assignment.

## 5.2 NP-hardness of PMC extension

b
β1
β1
β2
β2
β3
β3
β4
β4
β5
β5
α1
α1
α2
α2
α3
α3
α4
α4
α5
α5
a
C1
C2
C3
Figure 18: Graph G(Φ) for the 3-SAT formula Φ: (x1 x2 x3) (x1 x2 x5) (x3 x4 x5). Here, M can be extended into S(σ): vertices of S(σ) M are drawn in blue. The truth assignment (σ is: x1, x2 are fixed True, x3, x4, x5 are fixed False.

Figure 18: Graph \(G(\Phi)\) for the 3-SAT formula \(\Phi\): \((x_1\vee x_2\vee x_3)\wedge(\overline{x_1}\vee x_2\vee x_5)\wedge(\overline{x_3}\vee\overline{x_4}\vee\overline{x_5})\). Here, _M_ can be extended into \(S(\sigma)\): vertices of \(S(\sigma)\backslash M\) are drawn in blue. The truth assignment \(\sigma\) is: _x_<sub>1</sub>_,x_<sub>2</sub> are fixed True, _x_<sub>3</sub>_,x_<sub>4</sub>_,x_<sub>5</sub> are fixed False.

