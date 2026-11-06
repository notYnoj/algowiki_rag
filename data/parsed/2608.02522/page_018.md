\(\mathrm{min}\sum_{I\in\mathcal{I}(G)}x_I\) (P)

\(\text{s.t.}\sum_{I\in\mathcal{I}(G):v\in I}x_I\ge 1(\forall v\in V(G)),\)<br>
\(x_I\ge 0(\forall I\in\mathcal{I}(G)).\)

By linear programming duality, it is also equal to the optimal value of the following dual program.

\(\mathrm{max}\sum_{v\in V(G)}y_v\) (D)

\(\text{s.t.}\sum_{v\in I}y_v\le 1(\forall I\in\mathcal{I}(G)),\)<br>
\(y_v\ge 0(\forall v\in V(G)).\)

Based on these definitions, we now observe that \(\rho\) and \(\chi_f\) are indeed submultiplicative.

**Lemma 4.1.** _For all graphs G_<sub>1</sub> _and G_<sub>2</sub> _on the same vertex-set, we have_ \(\rho(G_1\cup G_2)\le\rho(G_1)\rho(G_2)\) _and_ \(\chi_f(G_1\cup G_2)\le\chi_f(G_1)\chi_f(G_2)\).

_Proof._ Let _H_ be any nonempty subgraph of \(G_1\cup G_2\). Let _H_<sub>1</sub> and _H_<sub>2</sub> be two spanning subgraphs of _H_ such that \(H=H_1\cup H_2\) and \(H_i\subseteq G_i\) for _i_=1,2. By definition of \(\rho(G_1)\), there exists an independent set _I_ in _H_<sub>1</sub> such that \(|I|\ge\frac{|V(H_1)|}{\rho(G_1)}\). Now consider the nonempty subgraph _H_<sub>2</sub>\[_I_\] of _G_<sub>2</sub>. By definition of \(\rho(G_2)\), there exists an independent set \(J\subseteq I\) in _H_<sub>2</sub> such that \(|J|\ge\frac{|V(H_2[I])|}{\rho(G_2)}=\frac{|I|}{\rho(G_2)}\ge\frac{|V(H_1)|}{\rho(G_1)\rho(G_2)}=\frac{|V(H)|}{\rho(G_1)\rho(G_2)}\). Then _J_ is independent in both _H_<sub>1</sub> and _H_<sub>2</sub>, and thus independent in \(H=H_1\cup H_2\). It follows that \(\alpha(H)\ge\frac{|V(H)|}{\rho(G_1)\rho(G_2)}\), or, equivalently, \(\frac{|V(H)|}{\alpha(H)}\le\rho(G_1)\rho(G_2)\). Since _H_ was initially chosen as an arbitrary subgraph of \(G_1\cup G_2\), this shows that \(\rho(G_1\cup G_2)\le\rho(G_1)\rho(G_2)\), as desired.

Let us now move on to the fractional chromatic number. For _i_=1,2, let us denote by \((x_I^{(i)})_{I\in\mathcal{I}(G_i)}\) an optimal solution to the linear program (P) for _G<sub>i</sub>_. Note that the independent sets in \(G_1\cup G_2\) are exactly the intersections of the members of I(_G_<sub>1</sub>) and I(_G_<sub>2</sub>).

Now, for each \(S\in\mathcal{I}(G_1\cup G_2)\), let us define<tbc>

\(x'_S:=\sum_{I\in\mathcal{I}(G_1),J\in\mathcal{I}(G_2):I\cap J=S}x_I^{(1)}x_J^{(2)}.\)

<tbc>One then easily checks that<tbc>

\(\sum_{S\in\mathcal{I}(G_1\cup G_2)}x'_S=\sum_{I\in\mathcal{I}(G_1),J\in\mathcal{I}(G_2)}x_I^{(1)}x_J^{(2)}=\sum_{I\in\mathcal{I}(G_1)}x_I^{(1)}\cdot\sum_{J\in\mathcal{I}(G_2)}x_J^{(2)}=\chi_f(G_1)\chi_f(G_2).\)

