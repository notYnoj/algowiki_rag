## C.1 Polynomial-Sized Solutions

Adding uncrossed-ness to the constraints of a multiflow problem means it is no longer a linear program, and it is not necessarily obvious that we should expect uncrossed solutions that are polynomial in the size of the input (i.e. in terms of |_V|,|E(G_)|,|_E(H_)|, and the bit-size of _u,d_).

We give a brief argument for why polynomial-sized solutions exist. Let _f_ be a feasible uncrossed (fractional) multiflow for a maximization or congestion instance. Consider a single commodity \(h=(s,t)\in E(H)\), and consider the single-commodity uncrossed multiflow _f<sup>h</sup>_, obtained by restricting _f_ to _h_. Let _P_<sub>1</sub>_,...,P<sub>k</sub>_ be the clockwise ordering of the support paths about _s_. Each sector (i.e. the region bounded between consecutive paths in this ordering) contains some face _F_ of _G_ that is not contained in any other sector. Hence there are at most _O_(|_V_|) sectors, and thus _O_(|_V_|) paths. Thus over all commodities the set of support paths P<sup>∗</sup> is at most _O_(|_V_||_E(H_)|). To obtain values of _f(P_) that have polynomial bit-size, we can set up restricted versions of the maximization/congestion linear programs that only have variables for \(P\in\mathcal{P}^*\). By standard linear programming theory there exists a solution for these problems that has polynomial bit-size, and any solution for these LPs is uncrossed as they draw support paths only from P<sup>∗</sup>.

A consequence of this argument is that the problem of determine whether (_G,H,u,d_) has a feasible (fractional) solution that is uncrossed is in NP, as promised by Theorem 1.7. Given a polynomial-sized candidate solution, it is straightforward to check that each pair of support paths is uncrossed and that the solution is feasible in polynomial time.

## C.2 Gadgets

Many of the ideas build on the structure of solutions for the instance in Figure 10 which we call Double Diamond.

**Lemma C.1** (Double Diamond Instance)**.** _Let G,H be the instance of fractional uncrossed flow from Figure 10. This instance has only two possible path-solutions, and both are integral._

_Proof._ Suppose there is a support path _P_ in a fractional solution starting with _s_<sub>1</sub>_u_<sub>1</sub>_,u_<sub>1</sub>_h_<sub>1</sub>_,h_<sub>1</sub>_u_<sub>2</sub>_,u_<sub>2</sub>_l_<sub>1</sub>. Then, because the support path are uncrossed, there is no support path starting by _s_<sub>2</sub>_u_<sub>2</sub>_,u_<sub>2</sub>_h_<sub>1</sub>, as such a flow path _Q_ would cross _P_ at either the subpath _Z=u_<sub>2</sub>_,h_<sub>1</sub> or _Z=u_<sub>2</sub>_,h_<sub>1</sub>_,u_<sub>1</sub>. Then all support paths for the demand _s_<sub>2</sub>_t_<sub>2</sub> uses _u_<sub>2</sub>_l_<sub>1</sub>, which, considering also _P_, implies that the total value of flow paths on that edge is more than 1, contradiction.

By similar arguments, one can show that the support paths use only one of the two highlighted paths from Figure 10 _P_<sub>1</sub> (in blue) and _P_<sub>2</sub> (in red) and their symmetric paths by a flip along an horizontal axis _Q_<sub>1</sub> and _Q_<sub>2</sub>. To conclude, notice that _P_<sub>1</sub> crosses _Q_<sub>2</sub> and _Q_<sub>1</sub> crosses _P_<sub>2</sub>, implying that the only two solutions are _P_<sub>1</sub>+_P_<sub>2</sub> and _Q_<sub>1</sub>+_Q_<sub>2</sub>.

We next discuss the Terminal Gadget, which is a modification of the Double Diamond Instance.

h1
h2
u1
S1
S2
u2
v1
t1
t2
v2
l1
l2

Figure 10: _Double Diamond Instance._ An instance for the fractional uncrossed flow problem that has only integral solutions (one of these solutions is given by the two colored paths with value 1).

