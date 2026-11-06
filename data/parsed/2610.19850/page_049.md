Our proof that PMC Extension is NP-hard is strongly related to the construction of \(G(\Phi)\) in the previous subsection. We proceed by showing that identifying a PMC extending _M_ in \(G(\Phi)\) is equivalent to finding a minimal (_a,b_)-separator extending _M_ in \(G(\Phi)\). First, we establish some properties of PMCs in graph \(G(\Phi)\).

**Lemma 20.** _In graph_ \(G(\Phi)\)_, we have_ \(N[a]\cup N[b]=V(G(\Phi))\)_. For any_ \(MC\Omega\) _of_ \(G(\Phi)\) _such that_ \(\Omega\cap\{a,b\}=\emptyset\)_, there are exactly two connected components in_ \(G\backslash\Omega\)_, which are_ \(C(a,\Omega)\) _and_ \(C(b,\Omega)\).

_Proof._ From graph construction, \(N[a]\cup N[b]=V(G(\Phi))\) and \(N[a]\cap N[b]=\emptyset\). Assume that _a_ and _b_ belong to the same connected component _C_ of \(G\backslash\Omega\), then _C_ is necessarily a full component for \(\Omega\) since \(\Omega\subseteq N(a)\cup N(b)\), contradicting Theorem 4. So, \(G\backslash\Omega\) admits at least two connected components, containing respectively _a_ and _b_. There cannot be a third one \(C'\), since \(C'\subseteq N(a)\cup N(b)\).

**Lemma 21.** _For any_ (_a,b)-separator S of_ \(G(\Phi)\) _extending M and any vertex_ \(x\in C(a,S)\) _(resp._ \(\in C(b,S)\)_), there is_ \(v\in S\) _such that_ \(N(v)\cap C(a,S)=\{x\}\) _(resp._ \(N(v)\cap C(b,S)=\{x\}\)_)._

_Proof._ Any (_a,b_)-separator _S_ of \(G(\Phi)\) is a superset of some minimal (_a,b_)-separator of \(G(\Phi)\), which is, from the claim of Theorem 12, some \(S(\sigma)\). Hence, for some truth assignment \(\sigma\), \(S(\sigma)\subseteq S\). Consider any \(x\in C(a,S)\): it can thus be either _a_ or some vertex in \(\{\alpha_i,\overline{\alpha_i}\}_{1\le i\le n}\). If _x=a_, then pick _v_ as any vertex \(\alpha_i\) or \(\overline{\alpha_i}\) belonging to _S_. The neighborhood of _v_ in _C(a,S_) contains only _a_. Else, if \(x=\alpha_i\) w.l.o.g. (case \(x=\overline{\alpha_i}\) works similarly by symmetry), then it means that \(\overline{\beta_i}\) belongs necessarily to _S_, hence with \(v=\overline{\beta_i}\), we have \(N(v)\cap C(a,S)=\{\alpha_i\}\). We can achieve the same reasoning on side _C(b,S_), the only difference being the adjacency between vertices in \(\{\beta_i,\overline{\beta_i}\}_{1\le i\le n}\) with clause vertices, but since the latter belongs to \(M\unknown S\), it has no impact.

We pursue with a key lemma which presents the form of PMCs in \(G(\Phi)\) which both extends _M_ and do not contain _a_ and _b_. In fact, they are very close to the separators \(S(\sigma)\) introduced in Theorem 12. In the remainder, for any \(1\le j\le m\), we denote by _B(C<sub>j</sub>_) the set of \(\beta\)-vertices adjacent to the clause vertex _C<sub>j</sub>_, formally \(B(C_j)=N(C_j)\cap\{\beta_i,\overline{\beta_i}\}_{1\le i\le n}\).

**Lemma 22.** _If_ \(\Omega\) _is a PMC of_ \(G(\Phi)\) _extending M and such that_ \(a,b\notin\Omega\)_, then the following statements hold:_

• _there is exactly one index_ \(1\le i\le n\) _such that_ |_T<sub>i</sub>_|=3 _with_ \(T_i=\{\alpha_i,\overline{\alpha_i},\beta_i,\overline{\beta_i}\}\cap\Omega\);<tbc>

• _for all other indices_ \(1\le p\neq i\le n\)_, we have_ |_T<sub>p</sub>_|=2 _with_ \(T_p=\{\alpha_p,\beta_p\}\) _or_ \(T_p=\{\overline{\alpha_p},\overline{\beta_p}\}\).<tbc>

• _for any_ \(1\le j\le m\), \(B(C_j)\backslash\Omega\neq\emptyset\).

_Proof._ We proceed by case disjunction. From Lemma 20, vertices _a_ and _b_ cannot belong to the same connected component. For any \(1\le i\le n\), if |_T<sub>i</sub>_|=0 or 1, there would be an (_a,b_)- path in \(G\backslash\Omega\), which is impossible. Case |_T<sub>i</sub>_|=4 cannot occur either because there would be neither a direct edge nor a path with internal vertices in \(\overline{\Omega}\) between \(\alpha_i\) and \(\beta_i\). Indeed, we are blocked not only by vertices in _T<sub>i</sub>_ but also by clause vertices.

In the following, we show that we cannot have |_T<sub>i</sub>_|=2 for all \(1\le i\le n\). First, we exclude the case where \(\Omega\) contains, for some index _i_, pairs \(\alpha_i\overline{\beta_i}\) or \(\overline{\alpha_i}\beta_i\) because it leads to a path from _a_ to _b_ in \(G\backslash\Omega\) (Lemma 20). Then, there is only three configurations for each _i_ to consider :<tbc>

