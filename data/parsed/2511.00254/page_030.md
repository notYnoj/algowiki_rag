**Lemma C.2** (Terminal Gadget, Figure 11)**.** _Let G,H be an instance of fractional uncrossed flow, with at least two demands s_<sub>1</sub>_t_<sub>1</sub>_, s_<sub>2</sub>_t_<sub>2</sub> _as described in Figure 11 (modified from Figure 10). Let G_<sub>1</sub> _be the subgraph induced by the nodes outside the circle. Then, for any fractional solution z to G,H,_

(_i)_ _s_<sub>1</sub>_t_<sub>1</sub> _is routed integrally inside G_<sub>1</sub>;<tbc>

(_ii)_ _either all the support paths for s_<sub>2</sub>_t_<sub>2</sub> _use c_<sub>1</sub>_x or they all use d_<sub>1</sub>_y;_<tbc>

_(iii)_ _no support path for any other demand uses an edge of G_<sub>1</sub> _(aside from s_<sub>1</sub>_t_<sub>1</sub>_, s_<sub>2</sub>_t_<sub>2</sub>_)._

_Proof._ By considering the cut {_c_<sub>1</sub>_x,d_<sub>1</sub>_y_}, which is crossed by the demand _s_<sub>2</sub>_t_<sub>2</sub>, at most half a unit of _s_<sub>1</sub>_t_<sub>1</sub>-flow can be routed on these edges. This implies that there exists a support _s_<sub>1</sub>_t_<sub>1</sub>- path contained in _G_<sub>1</sub>. There are 4 possible such paths, two of length 5 and two of length 7. Let _P=s_<sub>1</sub>_u_<sub>1</sub>_a_<sub>1</sub>_u_<sub>2</sub>_b_<sub>1</sub>_d_<sub>1</sub>_,v_<sub>1</sub>_t_<sub>1</sub> and suppose that _z(P)\>_0. Since less than 1 unit of capacity is now available on _u_<sub>2</sub>_b_<sub>1</sub> for _s_<sub>2</sub>_t_<sub>2</sub>, there must be an support _s_<sub>2</sub>_t_<sub>2</sub>-path _Q_ starting with _s_<sub>2</sub>_u_<sub>2</sub>_a_<sub>1</sub>. Hence _Q_ must continue to _u_<sub>1</sub> and _b_<sub>1</sub>, but this crosses _P_. Therefore _z(P_)=0, and there must be a support _s_<sub>1</sub>_t_<sub>1</sub>-path _P_<sub>1</sub> of length 5. We may assume _P_<sub>1</sub>=_s_<sub>1</sub>_u_<sub>1</sub>_a_<sub>1</sub>_c_<sub>1</sub>_v_<sub>1</sub>_t_<sub>1</sub>.

Suppose that there is a support _s_<sub>2</sub>_t_<sub>2</sub>-flow path _P_<sub>2</sub>, containing _c_<sub>1</sub>_x_. Then as _P_<sub>1</sub> and _P_<sub>2</sub> do not cross, _P_<sub>2</sub> must contain a subpath _b_<sub>1</sub>_u_<sub>1</sub>_a_<sub>1</sub>_c_<sub>1</sub>_x_. Because {_a_<sub>1</sub>_c_<sub>1</sub>_,b_<sub>1</sub>_d_<sub>1</sub>} is a tight cut and \(a_1c_1\in P_2\), _P_<sub>2</sub> does not contain _b_<sub>1</sub>_d_<sub>1</sub>. Hence _P_<sub>2</sub> starts with _s_<sub>2</sub>_u_<sub>2</sub>_b_<sub>1</sub>_u_<sub>1</sub>_..._ Because _z(P_<sub>2</sub>)_\>_0 and \(u_1a_1\in P_2\), there is a support _s_<sub>1</sub>_t_<sub>1</sub>-path _Q_<sub>1</sub> starting with _s_<sub>1</sub>_u_<sub>1</sub>_b_<sub>1</sub>. As _P_<sub>2</sub> and _Q_<sub>1</sub> do not cross, _Q_<sub>1</sub> continues with _b_<sub>1</sub>_u_<sub>2</sub>, but then it must cross _P_<sub>2</sub> at _u_<sub>2</sub>. Hence no support _s_<sub>2</sub>_t_<sub>2</sub>-path contains _c_<sub>1</sub>_x_, they must all contain _d_<sub>1</sub>_y_. Furthermore, this shows that no support _s_<sub>1</sub>_t_<sub>1</sub>-path intersects the cut {_c_<sub>1</sub>_x,d_<sub>1</sub>_y_}, since _s_<sub>2</sub>_t_<sub>2</sub> uses all the capacity of _d_<sub>1</sub>_y_, and hence the support path would have to use _c_<sub>1</sub>_x_ twice. So the only possible support _s_<sub>1</sub>_t_<sub>1</sub>-paths are _P_<sub>1</sub> and its symmetric \(P'_1=s_1u_1b_1d_1v_1t_1\).

Finally suppose that _z(P_<sub>1</sub>)_\>_0 and \(z(P'_1)>0\). As \(P_1\cup P'_1\) forms a circuit separating _s_<sub>2</sub> from _t_<sub>2</sub>, any active flow _s_<sub>2</sub>_t_<sub>2</sub>-path would cross either _P_<sub>1</sub> or \(P'_1\). Thus, (i) holds. Up to symmetry, we may assume _z(P_<sub>1</sub>)=1, \(z(P'_1)=0\). From there, any active _s_<sub>2</sub>_t_<sub>2</sub>-flow path must start with _s_<sub>2</sub>_u_<sub>2</sub>_b_<sub>1</sub>_d_<sub>1</sub>_y_, that is (ii) holds, and (iii) follows.

**Lemma C.3** (Coupled Arcs Gadget, Fig 12)**.** _Let G,H be an uncrossable flow instance, containing the gadget of Figure 12 as an induced subgraph. Let P<sub>xy</sub> and P<sub>wz</sub> be the top and bottom paths y_<sub>0</sub>_x_<sub>1</sub>_y_<sub>1</sub>_x_<sub>2</sub>_y_<sub>2</sub>_x_<sub>3</sub>_y_<sub>3</sub>_x_<sub>4</sub> _and z_<sub>0</sub>_w_<sub>1</sub>_z_<sub>1</sub>_w_<sub>2</sub>_z_<sub>2</sub>_w_<sub>3</sub>_z_<sub>3</sub>_w_<sub>4</sub> _respectively. Then in any solution x, there is_ \(Q\in\{P_{xy},P_{wz}\}\) _with the following property: for every external demand_ \(st\in E(H)\backslash\{s_1t_1,s_2t_2,s_3t_3\}\) _and for any support st-path P, the intersection of E(P_) _with the gadget is either empty or exactly Q. Thus, this gadget behaves as though we have only two edges y_<sub>0</sub>_x_<sub>4</sub>_, z_<sub>0</sub>_w_<sub>4</sub>_, such that at most one of them can be used by external demands._

a1
C1
x
y
u1
S1
S2
u2
V1
t1
t2
S2
X
b1
d1
y

Figure 11: Terminal Gadget. A gadget that forces the demand _s_<sub>2</sub>_t_<sub>2</sub> to be routed either entirely through _x_ or through _y_. The nodes outside the circle form an induced subgraph, and deleting _x_ and _y_ disconnect these nodes from the rest of the graph. Furthermore, no demand other than _s_<sub>1</sub>_t_<sub>1</sub> and _s_<sub>2</sub>_t_<sub>2</sub> can have a support path intersecting the edges of the gadget. The colored paths represent a possible routing. On the right, a schematic to represent the gadget on a terminal, using a blue circle to denote that all the flow must use one of the two incident arcs.

