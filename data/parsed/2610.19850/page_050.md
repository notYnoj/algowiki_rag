(1) \(T_i=\alpha_i\overline{\alpha_i}\),<tbc>

(2) \(T_i=\beta_i\overline{\beta_i}\)<tbc>

(3) \(T_i=\alpha_i\beta_i\) or \(\overline{\alpha_i\beta_i}\)

If all _x<sub>i</sub>_ are in the case (1), then we have \(C(b,\Omega)\) has a full component for \(\Omega\). Same for the case (2) and \(C(a,\Omega)\). If all _x<sub>i</sub>_ are in case (3), then \(C(a,\Omega)\) is a full component for \(\Omega\). If we mix only the cases (1) and (2), then we have the _b<sub>i</sub>_ of an index _i_ in case (1) that cannot see an \(a_{i^\prime}\) of an index \(i'\) in case (2) despite \(\Omega\). If we blend the case (1) and the case (3), then we have either no full component if there is a _C<sub>j</sub>_ such that \(B(C_j)\backslash\Omega=\emptyset\) but vertex _C<sub>j</sub>_ will not reach any \(b_{i^\prime}\) in the case (1). If we mix case (2) and the case (3), then _C(a,S_) is a full component for \(\Omega\).

In brief, we cannot have |_T<sub>i</sub>_|=2 for all indices \(1\le i\le n\). We finally show that we cannot have more than one _x<sub>i</sub>_ with |_T<sub>i</sub>_|=3. With |_T<sub>i</sub>_|=3, there is a vertex \(u\in T_i\) not adjacent to \(C(a,\Omega)\) and another vertex _v_ not adjacent to \(C(b,\Omega)\). For any pair of \(x_i,x_{i^\prime}\) such that \(|T_i|=|T_{i^\prime}|=3\), the vertex _u_ (resp. _v_) of _T<sub>i</sub>_ cannot reach the vertex \(v'\) (resp \(u'\)) of \(T_{i^\prime}\).

At last, if there is exactly one _x<sub>i</sub>_ with |_T<sub>i</sub>_|=3, then all other _x<sub>p</sub>_, with \(p\neq i\) have |_T<sub>p</sub>_|=2. Furthermore, variable gadgets with |_T<sub>p</sub>_|=2 cannot be in the case (1) or (2) because they would create a conflict pair with the gadget _T<sub>i</sub>_. Indeed, _T<sub>i</sub>_ contains exactly one vertex not adjacent to \(C(a,\Omega)\) and one vertex not adjacent to \(C(b,\Omega)\). Another gadget _T<sub>p</sub>_ in case (1) or (2) contains either a vertex not adjacent to \(C(a,\Omega)\) or a vertex not adjacent to \(C(b,\Omega)\). As a conclusion, all |_T<sub>p</sub>_|=2 are in the case (3). Furthermore, we have also that \(\forall j,B(C_j)\backslash\Omega\neq\emptyset\) because otherwise, gadgets in case (3) would only admit \(C(a,\Omega)\) as a full component. It follows that the vertex of the gadget with |_T<sub>i</sub>_|=3 which is disconnected to \(C(a,\Omega)\) would not reach one clause vertex with covered \(\beta\)-vertices.

These different elements on the structures of PMCs extending _M_ and avoiding _a,b_ reveal the form already found in Theorem 12: these PMCs seem strongly related to the truth assignment of the SAT formula \(\Phi\). We confirm this intuition, showing that PMC Extension and Minimal (_a,b_)-separator Extension are equivalent problems on this setting.

**Lemma 23.** _In_ \(G(\Phi)\)_, there exists a PMC_ \(\Omega\) _extending M and such that_ \(a,b\notin\Omega\) _iff there exist a minimal_ (_a,b)-separator S extending M._

_Proof._ **Only if direction.** Given a minimal (_a,b_)-separator _S_ of \(G(\Phi)\) extending _M_, \(G(\Phi)\backslash S\) admits two full components _C(a,S_) and _C(b,S_). We can add an extra vertex _x_ of any variable gadget into _S_: we say w.l.o.g. that \(x\in C(a,S)\). By Lemma 21, there exists \(v\in S\) such that \(N(v)\cap C(a,S)=\{x\}\), so for set \(X=S\cup\{a\}\), _C(a,X_) is not a full component for _X_. Moreover, _C(b,X_) is not a full component either for _X_, since \(x\in C(a,S)\). Set _X_ is shy. Moreover, as _C(a,S_) was a full component for _S_, vertex _x_ is enlightened for _X_. As _C(b,S_) was also a full component for _S_, vertices of _S_ see each other via this connected component. Consequently, _X_ has the reachability property and is a PMC.

**If direction.** Given a PMC \(\Omega\) satisfying \(M\unknown\Omega\) and \(\Omega\cap\{a,b\}=\emptyset\), we know by Lemma 22 that we have two vertices picked up in every gadgets except for one where there are three. By Lemma 20, we know that \(G(\Phi)\backslash\Omega\) has exactly two connected components: \(C(a,\Omega)\) and \(C(b,\Omega)\). Now consider the variable gadget with |_T<sub>i</sub>_|=3. We distinguish two cases:

• _T<sub>i</sub>_ contains all \(\beta\)-vertices: in this setting, the separator \(S=N(C(a,\Omega))\) contains every vertex of _M_. It follows, by Lemma 9, that _S_ is a minimal (_a,b_)-separator extending _M_.<tbc>

