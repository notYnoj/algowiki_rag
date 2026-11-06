1: **Input:** A graph G and a shy set \(X\subseteq V(G)\).<br>
2: **Output:** A subset of X which is a brightening of X (proven in Theorem 5).<br>
3: \(U\leftarrow X\);<br>
4: **while** U _has at least one conflict pair_ **do**<br>
5: \(u\leftarrow\) any vertex of U involved in a conflict pair for U;<br>
6: **for all** \(v\in U\) _such that_ (u,v) _is a conflict pair for_ U **do**<br>
7: \(U\leftarrow U\backslash\{v\}\);<br>
8: **return** U;

<tbc>_U_ (line 8). If it is still shy, we restart the removal process until no conflict pair remain. Refer to Figure 6 as a visual aid on an iteration of conflict-greedy.

**Theorem 5** (Existence of a brightening)**.** _For any shy set_ \(X\subseteq V(G)\)_, the subset returned by_ conflict-greedy _is a brightening of X. As a consequence, each shy set admits at least one brightening, and, it can be computed in time O(n_<sup>3</sup>).

_Proof._ First, we prove that the result of conflict-greedy is a brightening of the input shy set _X_. To achieve it, we propose a loop invariant for the while loop in line 4. We index the iterations of this loop by index \(i\ge 1\), the first iteration being the one where _U_ is initially equal to _X_ and some of its vertices are withdrawn. For each iteration \(i\ge 1\), we fix _u<sub>i</sub>_ as the protected vertex selected in line 5, and _U<sub>i</sub>_ the set _U_ obtained at the end of the loop. To be consistent, we also fix _U_<sub>0</sub>=_X_. Our invariant proposal is the following:

**Invariant**: At iteration \(i\ge 1\), for any non-native connected component _C_ of graph _G_\\_U<sub>i</sub>_, there exists an enlightened vertex \(z_C\in U_i\) which is not visible from _C_, _i.e._ \(z_C\notin N_G(C)\).

We need to provide some explanations on this invariant. By "non-native connected component" _C_, we mean a connected component of _G_\\_U<sub>i</sub>_ which contains at least one vertex of _X_\\_U<sub>i</sub>_. In other words, _C_ is a connected component of _G_\\_U<sub>i</sub>_ but not of _G_\\_X_. Moreover, we recall that an enlightened vertex \(z_C\in U_i\) is a vertex visible from any other vertex of _U<sub>i</sub>_ despite _U<sub>i</sub>_, in brief _R<sub>G</sub>(z<sub>C</sub>,U<sub>i</sub>_)=_U<sub>i</sub>_. See Definition 7 for an exhaustive reminder on reachability vocabulary. We prove this invariant by induction, on the index _i_.

_Base case._ The base case is _i_=1. During the first iteration, we select a vertex \(u_1\in U_0\) which is involved in at least one conflict pair, and then we remove all vertices in conflict with _u_<sub>1</sub> for _U_<sub>0</sub>. We denote by _v_<sub>0</sub>_,v_<sub>1</sub>_,...,v<sub>r</sub>_ the sequence of removed vertices in this order, with \(r\ge 0\). We have {_v_<sub>0</sub>_,...,v<sub>r</sub>_}=_U_<sub>0</sub>\\_U_<sub>1</sub>. When _v_<sub>0</sub> is removed from the current _U=U_<sub>0</sub>, this forms a new connected component _C_<sub>0</sub> in _G_\\(_U_<sub>0</sub>\\{_v_<sub>0</sub>}) containing _v_<sub>0</sub>. Vertex _u_<sub>1</sub> is not adjacent to _C_<sub>0</sub>: since (_u_<sub>1</sub>_,v_<sub>0</sub>) is a conflict pair, \(v_0\notin R_G(u_1,U_0)\) and by Lemma 14, \(u_1\notin N_G(C_0)\). Again, when we remove _v_<sub>1</sub> from the current _U=U_<sub>0</sub>\\{_v_<sub>0</sub>}, we form a new connected component _C_<sub>1</sub> in graph _G_\\(_U_<sub>0</sub>\\{_v_<sub>0</sub>_,v_<sub>1</sub>}). Either _C_<sub>1</sub> is distinct from _C_<sub>0</sub>: again \(u_1\notin N_G(C_1)\) as (_u_<sub>1</sub>_,v_<sub>1</sub>) is a conflict pair (Lemma 14). Or _C_<sub>1</sub> contains _v_<sub>0</sub> and thus \(C_0\unknown C_1\): as _C_<sub>0</sub> did not see _u_<sub>1</sub> in _G_\\(_U_<sub>0</sub>\\{_v_<sub>0</sub>}) and (_u_<sub>1</sub>_,v_<sub>1</sub>) is a conflict pair, necessarily \(u_1\notin N_G(C_1)\). We can pursue the reasoning: for each newly-created connected component _C<sub>j</sub>_, with \(0\le j\le r\), either _C<sub>j</sub>_ is distinct from its predecessors or it is merged with at least one of them. In both cases, since<tbc>

**Algorithm 1:** conflict-greedy

