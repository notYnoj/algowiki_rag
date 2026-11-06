<tbc>_u_<sub>1</sub> is not adjacent to the predecessors and as (_u_<sub>1</sub>_,v<sub>j</sub>_) is a conflict pair, then \(u_1\notin N_G(C_j)\). In summary, for each non-native connected component \(C\in\{C_j\}_{0\le j\le r}\) created during the first iteration, vertex _u_<sub>1</sub> is not visible from _C_ despite _U_<sub>1</sub>. Furthermore, as all vertices in conflict with _u_<sub>1</sub> for _U_<sub>0</sub> belong to _U_<sub>0</sub>\\_U_<sub>1</sub>, vertex _u_<sub>1</sub> is enlightened for _U_<sub>1</sub>.

_Induction step._ We consider now any index \(i\ge 1\). We assume the invariant true for \(i\ge 1\) and prove it for _i_+1. As _U_<sub>_i_+1</sub> exists, then we know that _U<sub>i</sub>_ has a conflict pair. Set _U<sub>i</sub>_\\_U_<sub>_i_+1</sub> is thus nonempty and contains all vertices in conflict with _u_<sub>_i_+1</sub> for _U<sub>i</sub>_. Let _C_ be a non-native connected component of _G_\\_U_<sub>_i_+1</sub>. We distinguish two cases.

**Case A**: _C_ was already a connected component of _G_\\_U<sub>i</sub>_, said differently \(C\cap(U_i\backslash U_{i+1})=\emptyset\). In this case, _C_ is non-native as it contains vertices from _X_\\_U<sub>i</sub>_ but not from _U<sub>i</sub>_\\_U_<sub>_i_+1</sub>. By induction hypothesis on index _i_, an enlightened vertex \(z_C\in U_i\) is not visible from _C_. As _z<sub>C</sub>_ is enlightened, it is not involved in any conflict pair of _U<sub>i</sub>_. So, _z<sub>C</sub>_ is still enlightened in _U_<sub>_i_+1</sub>.

**Case B**: _C_ contains vertices from _U<sub>i</sub>_\\_U_<sub>_i_+1</sub>. Here, the reasoning is identical to the one provided for the base case. At each removal of a vertex in conflict with _u_<sub>_i_+1</sub>, either the newly- created connected component is distinct from its predecessors in iteration _i_+1, or it contains one of its predecessors. In both cases, as the vertex removed is in conflict with _u_<sub>_i_+1</sub> and that predecessors are too, we maintain the property that the connected components created by this vertex removals do not see _u_<sub>_i_+1</sub>. In brief, \(u_{i+1}\notin N_G(C)\). Furthermore, vertex _u_<sub>_i_+1</sub> is enlightened for _U_<sub>_i_+1</sub> as all its conflicts for _U<sub>i</sub>_ belong to _U<sub>i</sub>_\\_U_<sub>_i_+1</sub>.

_Conclusion._ The invariant property that any non-native connected component _C_ does not see some enlightened vertex of _U<sub>i</sub>_ is maintained. Moreover, conflict-greedy necessarily stops because set _U_ is finite and, at each iteration, at least one vertex is removed until no conflict pairs remains. As a consequence, the subset \(U\subseteq X\) returned by conflict-greedy exists, is nonempty, and all non-native components of _U_ are not full components for _U_. This<tbc>

U = X
U = X \ {x3}
U = X \ {x3, x4}
X1
X6
X1
X6
X1
X6
X2
X5
X2
X5
X2
X5
native
C1
C3
X4
Co
X4

Figure 6: The first iteration of conflict-greedy on some example: set _X_={_x_<sub>1</sub>_,...,x_<sub>6</sub>} is shy, no connected component of _G_\\_X_ is fully adjacent to _X_. There are several conflict pairs for _U=X_: (_x_<sub>1</sub>_,x_<sub>3</sub>),(_x_<sub>1</sub>_,x_<sub>4</sub>),(_x_<sub>1</sub>_,x_<sub>5</sub>),(_x_<sub>2</sub>_,x_<sub>6</sub>),(_x_<sub>3</sub>_,x_<sub>6</sub>). We select arbitrarily _u_<sub>1</sub>=_x_<sub>1</sub> as the protected vertex, hence we remove successively vertices _x_<sub>3</sub>_,x_<sub>4</sub>_,x_<sub>5</sub>. We remove first vertex _v_<sub>0</sub>=_x_<sub>3</sub>: we obtain a non-native connected component _C_<sub>0</sub> which is not full for _X_\\{_x_<sub>3</sub>} as it does not see _x_<sub>1</sub>. Note that _X_\\{_x_<sub>3</sub>} admits another connected component which is native. Second, we remove _v_<sub>1</sub>=_x_<sub>4</sub> and obtain a connected component _C_<sub>1</sub> which is merged with _C_<sub>0</sub>: again, it does not see _x_<sub>1</sub>. Removing finally _v_<sub>2</sub>=_x_<sub>5</sub> makes us obtain a shy subset without conflict pairs: {_x_<sub>1</sub>_,x_<sub>2</sub>_,x_<sub>6</sub>} is a PMC.

