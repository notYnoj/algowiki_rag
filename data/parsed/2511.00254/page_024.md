## A Uncrossing Procedures and Uncrossable Classes

By cycle we always mean simple cycle. For a cycle _C_, we use Int(_C_) and int(_C_) for the closed and open interior respectively of the region bounded by _C_.

### A.1 Fully-Compliant Layouts

Let _G_ be series-parallel. A demand _h_ is _fully-compliant_ if _G+h_ is series-parallel. We say (_G,H_) is _fully- compliant_ if every \(h\in E(H)\) is fully-compliant. This notion was introduced in \[7\], where it was also proven that such (_G,H_) are cut-sufficient. Here, we prove Theorem 3.2

_Proof of Theorem 3.2._ To show (_G,H_) is pairwise-planar, it suffices to show for each demand _h_=(_s,t_) that either \((s,t)\in E(G)\) or there exist two distinct faces _F_<sub>1</sub>_,F_<sub>2</sub> of _G_ such that \(s,t\in V(F_1)\) and \(s,t\in V(F_2)\). Suppose \((s,t)\notin E(G)\). Let _C_<sub>0</sub> be a cycle<sup>12</sup> containing both _s_ and _t_ (take two internally node-disjoint _st_-paths).

Now, select a cycle _C_ containing both _s_ and _t_ such that \(\mathrm{Int}(C)\subseteq\mathrm{Int}(C_0)\); subject to these constraints, choose _C_ such that Int(_C_) is minimal. Let _G<sub>C</sub>_ be the graph induced by _V_(Int(_C_)). Let _P,Q_ be the two internally node-disjoint _st_-paths comprising _C_.

Let _V<sub>P</sub>=V(P_)\\{_s,t_} and _V<sub>Q</sub>=V(P_)\\{_s,t_}. Since \((s,t)\notin E(G)\), neither of these sets is empty. Observe that there is no path in _G<sub>C</sub>_-{_s,t_} between _V<sub>P</sub>_ and _V<sub>Q</sub>_, as otherwise _G<sub>C</sub>+h_ contains a _K_<sub>4</sub>-minor, contradicting that _G+h_ is series-parallel. That is, {_s,t_} is a 2-cut of _G<sub>C</sub>_ separating _V<sub>P</sub>_ and _V<sub>Q</sub>_. Note that _G<sub>C</sub>_-{_s,t_} can only contain two connected components (one containing _V<sub>P</sub>_, another containing _V<sub>Q</sub>_), since if there were another in the interior of _G<sub>C</sub>_ then we could find a cycle \(C'\) containing _s,t_ such that \(\mathrm{Int}(C')\unknown\mathrm{Int}(C)\), contradicting our choice of _C_. Let _G<sub>P</sub>_ and _G<sub>Q</sub>_ denote the two connected components plus their respective edges to _s_ and _t_. Since _G<sub>P</sub>_ and _G<sub>Q</sub>_ are disjoint except at _s,t_, one can draw a curve in Int(_C_) between _s_ and _t_ that is disjoint from the embeddings of _G<sub>P</sub>_ and _G<sub>Q</sub>_ - this means there is a face _F_<sub>1</sub> of _G_ inside Int(_C_) containing both _s,t_.

Now, we can play the same game using cycle exteriors. Let _D_ be a simple cycle containing both _s_ and _t_ such that \(\mathrm{Ext}(D)\subseteq\mathrm{Ext}(C_0)\) (i.e. \(\mathrm{Int}(C_0)\subseteq\mathrm{Int}(D)\)); subject to these constraints, choose _D_ so that Ext(_D_)<tbc>

<sup>12</sup>Recall that by cycle we always mean simple cycle.

