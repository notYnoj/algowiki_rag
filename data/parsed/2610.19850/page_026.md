_Proof._ As _X_ is a PMC superset, there exists a PMC \(\Omega\subseteq X\). According to Lemma 15, \(\Omega\) admits a shy decomposition \((S',T')\), where separator \(S'\) is \(\Omega\)-shy with regards to \(C'\), which is the connected component in \(G\backslash S'\) containing \(T'\). We fix arbitrarily \(a\in T\subseteq C'\) and _b_ as a vertex belonging to any other full component for \(S'\) in _G_. By definition of both of these vertices, \(S'\) is a minimal (_a,b_)-separator, and \(S'\unknown X\). See Figure 8 for an illustration.

Let _S_ be the _X_-close (_a,b_)-separator. Since \(S'\unknown X\), from Lemma 6, _S_ and \(S'\) are parallel and \(C_G(a,S)\subseteq C_G(a,S')=C'\). We fix _C=C<sub>G</sub>(a,S_). Assume by way of contradiction that _S_ is not _X_-shy with regards to _C_. Then, there exists a connected component _B_ of _G_\[_C_\[_X_\] which is fully adjacent to _S_. As \(B\subseteq C\backslash X\), we also have \(B\subseteq C'\backslash\Omega\) because \(C\backslash X\subseteq C'\backslash X\subseteq C'\backslash\Omega\), using the inclusion properties stated so far. Let us call \(B'\) the connected component of \(G[C'\backslash\Omega]\) containing _B_. We show that \(S'\subseteq N_G(B')\).

Let \(s\in S'\). If \(s\in S'\cap S\), then _s_ is adjacent to \(B\subseteq B'\) because _B_ is full for _S_. Otherwise, assume \(s\in S'\backslash S\). Since \(\Omega\) is a PMC of _G_ and has the reachability property, there exists an (_a,s_)-path _P<sub>s</sub>_ whose internal vertices belong to \(\overline{\Omega}\) (if there are). As _S_ is closer to _a_ than \(S'\), _i.e._ \(C_G(a,S)\subseteq C_G(a,S')\), path _P<sub>s</sub>_ intersects _S_. Said differently, _P<sub>s</sub>_ contains a vertex \(v\in S\cap\overline{\Omega}\). Since _B_ is fully adjacent to _S_ and \(v\notin\Omega\), we have \(v\in B'\). Due to the presence of the internal vertex \(v\in B'\) in path _P<sub>s</sub>_ - which has internal vertices in \(\overline{\Omega}\) - then all internal vertices of _P<sub>s</sub>_ belong to \(B'\) and thus _s_ is adjacent to \(B'\).

In summary, \(B'\) is a connected component of \(G[C'\backslash\Omega]\) full for \(S'\): a contradiction since we assumed that \(S'\) is \(\Omega\)-shy with regard to \(C'\). Consequently, _S_ is _X_-shy with regard to _C_, completing the proof.

Based on subsection 3.1, we focus now on the "only if" part. We show, given a shy set _X_ together with a shy separator \(S\unknown X\), how our algorithm conflict-greedy allows us to compute a PMC inside _X_, proving by the way that _X_ is a PMC superset.

X
S'
S
T'
b
a
C'

Figure 8: Illustration of separators _S_ and \(S'\) on some graph, with shy set _X_ (given by the three purple areas - one big and two small with a single vertex) and PMC \(\Omega=S'\cup T'\subseteq X\). Separator \(S'\) is \(\Omega\)-shy with regard to \(C'\): no connected component of \(G[C'\backslash T']\) (surrounded by dashed blue lines) is full for \(S'\). Set _S_ (orange vertices) is the _X_-close (_a,b_)-separator: note that it is _X_-shy with regards to _C=C<sub>G</sub>(a,S_), which is represented with blue vertices.

