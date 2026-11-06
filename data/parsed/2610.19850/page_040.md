• _for any pair_ (_v,w_) _of vertices separated by D in_ \(G[\overline{\Omega}\cup\{v,w\}]\)_, at least one among these two vertices belongs to S<sub>D</sub>._<tbc>

• _If_ \(v\in S_D\)_, then v is fully adjacent to D,_ i.e. \(D\subseteq N_G(v)\).<tbc>

• _If_ \(v\in S_D\)_, then v is not adjacent to_ \(C_G(a,\Omega\cup D)\).

As for classic shutter-close sets, it can be shown with the same arguments that there is a pair in \(S_D\times(S\times S_D)\) which is separated by _D_, where _S<sub>D</sub>_ is an extended shutter-close set.

**Lemma 19** (Property of extended shutter-close sets)**.** _Consider an a-nice PMC_ \(\Omega\) _of G,_ \(S=N(C_G(a,\Omega))\) _and an a-shutter D,_ \(a\notin D\)_, with extended shutter-close set S<sub>D</sub>. There is at least one pair_ \((x,y)\in S\times S\) _separated by D in_ \(G[\overline{\Omega}\cup\{x,y\}]\)_, such that_ \(x\in S_D\) _and_ \(y\notin S_D\).

_Proof._ The proof comes from the fact that _S<sub>D</sub>_ is inclusion-wise minimal: if no such pair exists, set _S<sub>D</sub>_ could be reduced. The reasoning is identical to the one used for Lemma 18.

The graph analogy we established for shutter-close sets also holds for the extended version. Consider the same graph \(H(\Omega,D)\) but with different colors: now the vertices in blue are the vertices not only fully adjacent to _D_ but also not adjacent to \(C_G(a,\Omega\cup D)\). Other vertices are in red. From Definition 21, we know that the blue vertices form a vertex cover of \(H(\Omega,D)\). Definition 23 is thus quite natural: the extended shutter-close set is an inclusion-wise minimal blue vertex cover of \(H(\Omega,D)\).

**Theorem 10.** _Consider an a-nice PMC_ \(\Omega\), \(S=N(C_G(a,\Omega))\), \(T=\Omega\backslash S\)_, and an a-shutter D satisfying_ \(a\notin D\)_. Let S<sub>D</sub> be an extended shutter-close set of_ \(\Omega\) _relative to D. There exists a PMC:_

\(\Omega'=D\cup(\Omega\backslash S_D)\cup S'_D,\)

_where_ \(S'_D\) _is a subset of S<sub>D</sub>,_ i.e. \(S'_D\subseteq S_D\).

_Therefore,_ \(a\notin\Omega'\)_. We also have that the separator_ \(S'=N(C_G(a,\Omega'))\) _satisfies_ \(C_G(a,S')\unknown C_G(a,S)\)_. Furthermore,_ \((\Omega',\Omega)\in\mathcal{N}\).

_Proof._ As for Theorem 9, we will terminate the proof by showing that \((\Omega',\Omega)\in\mathcal{N}\). The first part of the proof consists in showing the existence of \(\Omega'\) and the property over \(S'\).

We consider the PMC superset \(X=\Omega\cup D\). We show how vertex removals in _S<sub>D</sub>_ allows us to obtain the announced PMC \(\Omega'\), distinguishing several cases. We define \(S'\) as the _X_-close (_a,t_)-separator, where \(t\in T\). Naturally, \(S'\) exists as \(S\unknown X\) separates _a_ from _t_. However, \(S'\) is different from _S_ as it does not contain \(S_D\neq\emptyset\): from Definition 23, vertices of _S<sub>D</sub>_ are not adjacent to _C<sub>G</sub>(a,X_). Furthermore, \(S'\) is _X_-shy with regards to \(C_G(t,S')\). Indeed, assume by way of contradiction that it is not. There would be a connected component \(C\unknown C_G(t,S')\) of _G_\\_X_ such that \(S'\subseteq N(C)\). This is impossible as \(D\unknown S'\) and _t_ are separated by \(S\unknown X\), so _C_ cannot be adjacent to all vertices of \(S'\). By Theorem 7, we can identify a PMC which is a subset of _X_ by following conflict removals.

As a last property, we have \(C_G(a,S')\unknown C_G(a,S)\) because \(S'\neq S\) both separate pair (_a,t_) in _G_, \(S\unknown X\) and \(S'\) is the _X_-close (_a,t_)-separator. Less formally, both separators are included into _X_ but \(S'\) is the closest to _a_.

We start the removal process of _X_ by forcing, as it was achieved in the proof of Theorem 7: the shy separator \(S'=N(C_G(t,S'))\) to be maintained, and removing vertices from \(X\backslash S'\subseteq\)<tbc>

