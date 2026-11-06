## 6 Reducing Uncrossed Edge-Disjoint Paths to Planar Node-Disjoint Paths

In this section we prove Theorem 1.8. An instance of edge-disjoint paths or node-disjoint paths consists of _G,H_ (we can think of these as having unit capacities and demands). We must find (integral) edge- or node- disjoint paths respectively that fully route _H_ in _G_. The problem of interest for Theorem 1.8 is _uncrossed_ edge-disjoint paths, where _G_ is planar and we add the extra constraint that the paths are uncrossed. We reduce to the standard planar node-disjoint paths problem, and then use a result of Schrijver \[29\] which says that node-disjoint paths can be solved in polynomial time in planar graphs if the number of faces the demand edges are incident upon is bounded.

Our proof uses contractions. We let _G/e_ to denote the graph obtained by contracting edge _e_ in a graph _G_; we use similar notation for a multiflow _f_.

**Lemma 6.1.** _Let f be an uncrossed flow in G and e some supply edge. Then f/e is uncrossed for G/e,H/e._

We first present a gadget that reduces the degree of an arbitrary vertex of degree at least 5, by one, adding vertices of maximum degree 4. Using this gadget repeatedly, we get an equivalent instance with maximum degree 4. Then every degree-4 vertex can be replaced by a _C_<sub>4</sub>, as illustrated in Figure 8, to obtain a graph with maximum degree 3.

Consider a vertex _v_ with \(deg(v)\ge 5\). In order to obtain maximum degree 4, the natural approach replaces _v_ by a grid large enough to make any routing incident to _v_ feasible in that grid. This is more straightforward in instances where the terminals are leaves. As we have seen however, creating leaves may destroy uncrossability. We need to be more careful then because _v_ can be a terminal for some of the demand pairs. Therefore we must pre-specify some vertices in the grid to substitute _v_ in those demand pairs. Because of the uncrossed constraint, the choice of these new terminals is more delicate. We give an explicit construction, presented in a recursive fashion: by showing how to decrease the degree of _v_ by one in _G_ and _H_ simultaneously.

**Proposition 6.2.** _Let G,H be an instance of the uncrossed edge-disjoint paths problem, and v be a vertex of G with_ deg_<sub>G</sub>(v)\>_4_, or_ \(deg_G(v)\ge 2\) _and_ \(deg_H(v)\ge 1\)_. Define_ \(G',H'\) _from G,H by replacing v in G by the spider web gadget from Figure 9. If_ \(deg_H(v)\ge 1\)_, then replace arbitrary demand_ (_s,v_) _in H by a demand_ (_s,t_) _where t is the red terminal in the gadget (which then has degree_ 1 _in_ \(H'\)_). Any other terminals at v are located at_ \(v'\)_. Then G,H admits an uncrossed routing if and only if_ \(G',H'\) _does._

_Proof._ Let _d_=deg(_v_). We label each vertex except _v_ in the spider web as _u<sub>i,j</sub>_ such that _u<sub>i,j</sub>_ is at the polar coordinate \((\frac{2i\pi}{d},j)\) (for instance _t=u_<sub>0,1</sub>), with \(i\in\{0,\dots,d-1\}\) and \(j\in\{1,\dots,d-1\}\). Let _v_<sub>0</sub>_,...,v_<sub>_d_-1</sub> be the neighbours of _v_, with _v<sub>i</sub>_ adjacent to _u_<sub>_i,d_-1</sub>. To avoid confusion, we will call \(v'\) the central vertex in the spider web, and _v_ the original vertex in _G_. Also we will consider all indices modulo _d_. Given a routing in \(G',H'\) by contracting all new vertices in the web (and deleting loops) they become the original _v_, and we obtain a routing in _G,H_, proving the _if_ implication.

Consider an uncrossed routing P in _G,H_. We compute a corresponding uncrossed routing in \(G',H'\). The first case is when _H_ does not contain a demand ending at _v_. We claim then there is a routing that does not use \(v'\). Note that our figure does not depict this case and in particular \(v'\) will not be used and can be safely removed, so that all of the new nodes have degree at most 4. Indeed to see this routing, consider a support flow path _P_ containing _v<sub>i</sub>v_, _vv<sub>j</sub>_ (with _i\<j_). Let \(P'\) be the flow path obtained from _P_ by replacing<tbc>

u
u

Figure 8: A gadget to replace a degree-4 vertex by 4 degree-3 vertices.

