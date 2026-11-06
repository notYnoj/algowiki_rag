We proceed to the second point of the lemma. By Lemma 8, there exists a solution _X_ of I with _S_:=_E(T_)\\_E(X_) such that the weight of

\(B':=\bigcup_{s_1,s_2\in Ss_1\neq s_2}(\mathrm{Inv}(s_1)\cap\mathrm{Inv}(s_2))\)

is at most (**w**(_A_)+_k_)<sup>2</sup>. Moreover, since I is Inv-respecting, we can assume that _X_ is also Inv- respecting. Hence, \(X=T-S+\mathrm{Inv}(S)+A'\) for some \(A'\subseteq A\). Since _X_ is a solution of I, it is acyclic (and hence so is \(X':=X-A'\)). Then Claim 14 guarantees that there exists a set \(\overline{P}\subseteq V'\times V'\) such that:

• the graph \(G'\) constructed by <o>_P_</o> and \(A'\) is acyclic;<tbc>

• for each \((u,v)\in\overline{P}\), \(X'\) has no directed path from _u_ to _v_.

By the definition of \(B'\), for each \((a,b)\in B'\), we have at least two edges \(s\in S\) such that \((a,b)\in\mathrm{Inv}(s)\). Moreover, by Observation 1, all such _s_ lie on the path from _b_ to _a_ in _T_. For each \((a,b)\in B'\), take the first and the last edge on this path that belong to _S_. Note that during the construction of \(\mathcal{C}_{A^\prime}\), we have considered these <o>_P_</o>, \(B'\), and these pairs of edges for each \((a,b)\in B'\). Let _F_<sub>0</sub> and _R_<sub>0</sub> be the sets constructed by \(B'\) and these pairs of edges. Then \(X'\) satisfies \(\mathcal{R}:=(F_0,R_0,B')\). Indeed, by construction, each edge from _F_<sub>0</sub> does not belong to _S_, while each edge from _R_<sub>0</sub> is in _S_. The remaining property follows directly from the definition of \(B'\). Additionally, recall that for each \((u,v)\in\overline{P}\), \(X'\) does not contain a path from _u_ to _v_. Then by Lemma 9, \(X'\) satisfies C<sub>R_,u,v_</sub>. Let \((F_{u,v},R_{u,v},B'')\in\mathcal{C}_{\mathcal{R},u,v}\) be a satisfied triple. Again, this lemma guarantees that \(B''=B'\). Consequently, \(X'\) (and therefore _X_) satisfies \((\bigcup F_{u,v},\bigcup R_{u,v},B')\), which belongs to \(\mathcal{C}_{A^\prime}\).

Finally, we prove the last point of the lemma. Consider a restriction triple \((\bigcup F_{u,v},\bigcup R_{u,v},B')\in\mathcal{C}_{A^\prime}\) and the corresponding sets <o>_P_</o>, _F_<sub>0</sub> and _R_<sub>0</sub>. By the choice of \(B'\), we have \(\mathbf{w}(B')\le(\mathbf{w}(A)+k)^2\). We show the needed property for the set \(F:=\bigcup F_{u,v}\), the argument for \(\bigcup R_{u,v}\) is identical. Let \(\mathcal{R}:=(F_0,R_0,B')\). Since for each \((u,v)\in\overline{P}\), we know that \((F_{u,v},R_{u,v},B')\in\mathcal{C}_{\mathcal{R},u,v}\), where C<sub>R_,u,v_</sub> is constructed using Lemma 9, it follows that \(F_0\subseteq F_{u,v}\). If \(\overline{P}=\emptyset\), then \(F=\emptyset\) as well. Otherwise, we have<tbc>

\(F=\left(\bigcup(F_{u,v}\backslash F_0)\right)\cup F_0\)

<tbc>By Lemma 9, each _F<sub>u,v</sub>_\\_F_<sub>0</sub> can be represented as a union of at most \(|B'|+1\) directed paths in _T_. Since \(\overline{P}\subseteq V'\times V'\), it holds that \(|\overline{P}|\le|V'|^2\le(2|A'|)^2\) (last inequality follows from the definition of \(V'\)). Recall that _F_<sub>0</sub> is a union of at most \(2|B'|\) directed paths in _T_. This implies that _F_ is a union of at most<tbc>

\(4|A'|^2\cdot(|B'|+1)+2|B'|\)

<tbc>directed paths in _T_. Because all edge weights in _G_ are at least one, we have \(|B'|\le\mathbf{w}(B')\le(\mathbf{w}(A)+k)^2\) and \(|A'|\le|A|\le\mathbf{w}(A)\). Consequently, we obtain the following bound:

\(4|A'|^2\cdot(|B'|+1)+2|B'|\le 4\mathbf{w}(A)^2\cdot((\mathbf{w}(A)+k)^2+1)+2(\mathbf{w}(A)+k)^2\)<br>
\(\le 4(\mathbf{w}(A)+k)^2\cdot((\mathbf{w}(A)+k)^2+1)+4(\mathbf{w}(A)+k)^2\)<br>
\(\le 4((\mathbf{w}(A)+k)^2+1)^2\)<br>
\(\le 4(\mathbf{w}(A)+k+1)^4\)

The proof is completed.

