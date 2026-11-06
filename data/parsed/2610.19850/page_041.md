\(C_G(t,S')\). All pairs of vertices in \(S'\times S'\) see each other despite _X_ thanks to _C<sub>G</sub>(a,X_). We will fix some priority rules for selecting the protected vertex, the main one being that it belongs in priority to \(S'\), instead of \(X\backslash S'\).

Let \((s,s')\) be a pair in \(S_D\times(S\backslash S_D)\) separated by _D_ in \(G[\overline{\Omega}\cup\{s,s'\}]\): from Lemma 19, such pair exists. We fix \(s'\in S\backslash S_D\) as a protected vertex, and we remove first the vertex _s_: it can be done since \(s\notin S'\) and _s_ has a conflict with \(s'\). The obtained set is _X<sub>s</sub>=X_\\{_s_}. Let us pursue with a few connectivity remarks concerning _X<sub>s</sub>_.

Each pair \((u,v)\in(\Omega\backslash S_D)\times(\Omega\backslash S_D)\) is a reachable pair despite _X_: these vertices are connected in graph \(G[\overline{X}\cup\{u,v\}]\). Indeed, by Definition 23, pairs separated by _D_ contain at least one vertex from _S<sub>D</sub>_. As a consequence, pairs in \((\Omega\backslash S_D)\times(\Omega\backslash S_D)\) are also reachable despite \(X_s\unknown X\): they are not conflictual. Similarly, pairs in \(D\times D\) are not conflictual despite _X<sub>s</sub>_, since all of them are adjacent to _s_, and \(s\notin X_s\). Moreover, pairs in \(D\times(\Omega\backslash S_D)\) are not conflictual: let \(x\in(\Omega\backslash S_D)\), either _x_ saw _s_ despite _X_, and now it sees entirely _D_ despite _X<sub>s</sub>_, or _x_ was separated from _s_ by _D_. In this latter case, as _D_ was a minimal (_s,x_)-separator in \(G[\overline{\Omega}\cup\{s,x\}]\), by definition of minimal separators, vertex _x_ reaches every vertex of _D_ despite \(X\unknown X_s\).

In summary, the pairs \(D\times D\), \(D\times(\Omega\backslash S_D)\) and \((\Omega\backslash S_D)\times(\Omega\backslash S_D)\) are not conflictual for _X<sub>s</sub>_. Moreover, set _X<sub>s</sub>_ can be partitioned into three sets: _D_, \(\Omega\backslash S_D\) and _S<sub>D</sub>_\\{_s_}. Hence, for all remaining reachability conflicts in the process, at least one vertex of the conflict pair belongs to _S<sub>D</sub>_ (and thus not to \(S'\)). Remember that \(S'\cap S_D=\emptyset\). We can thus force that the removed vertex at each step belongs to _S<sub>D</sub>_, by taking in priority protected vertices first inside \(S'\) (to handle all \(S'\times S_D\) conflict pairs), second inside \((\Omega\backslash S_D)\) (to handle conflict pairs \((\Omega\backslash S_D)\times S_D\)) and eventually inside _S<sub>D</sub>_ (to handle the only remaining conflicts in \(S_D\times S_D\)). Since by Theorem 7 we are sure to obtain a PMC \(\Omega'\) via this process (native components of _X_ cannot be adjacent to both _D_ and _T_, while \(D\cup T\subseteq\Omega'\)), we have \(\Omega'\unknown X\) satisfying \(X\backslash S_D\subseteq\Omega'\). Consequently, \(\Omega'\) contains sets _D_ and \(\Omega\backslash S_D\). As announced, we have

\(D\cup(\Omega\backslash S_D)\subseteq\Omega'\unknown D\cup(\Omega\backslash S_D)\cup S_D.\)

Moreover, as \(S'\) was taken as the _X_-shy separator for the removal process, \(S'\unknown\Omega'\). Finally,<tbc>

2
X
a
y
t1
t2
t3
z
Ω'
w

Figure 13: Example of PMC \(\Omega'\) obtained, considering the PMC \(\Omega\) already presented in Figure 11. Here, _S<sub>D</sub>_={_z_}.

