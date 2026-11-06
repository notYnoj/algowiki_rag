<tbc>to \(\eta\). Moreover, Claims 7-12 imply that there are no other blocking edges with respect to \(\eta\). Hence, in total there are \(k'=k+k(k-1)/2\) blocking edges with respect to \(\eta\). Thus, we can conclude that the forward direction is proved (\(\Rightarrow\)).

(\(\Leftarrow\)) In the reverse direction, let \(\eta\) be a matching of size at least \(|\mu|+k+k(k-1)/2\) such that \(\eta\) has at most _k_+<sup>_k(k_-1)</sup>/2 blocking edges. Due to the size of \(\eta\), we can infer that it is a perfect matching.

Let \(\mathtt{B}_\eta\) be the set of blocking edges with respect to \(\eta\). We first note some properties of matching \(\eta\) and the set \(\mathtt{B}_\eta\). We start by identifying the edges in \(\mathtt{B}_\eta\).

Note that in our instance, the static edges in \(G'\) are of the following type: For any \(u\in V(G)\), edge _u_<sub>1</sub>_u_<sub>2</sub> in \(G'\) is a static edge and is called the _u-type static edge_; for any \(e\in E(G)\), edge \(e\tilde{e}\) in \(G'\) is a static edge and is called the _e-type static edge_.

In the following claims, we prove that a blocking edge with respect to \(\eta\) is either a u-type static edge or e-type static edge. In fact, for each \(i\in[k]\), there is unique u-type static edge which is a blocking edge, and for each \(\{i,j\}\subseteq[k]\), there is unique e-type static edge which is a blocking edge.

**Claim 14 (u-type static edge)** _For each_ \(i\in[k]\)_, there exists_ \(u\in V_i\)_, such that u_<sub>1</sub>_u_<sub>2</sub> _is a blocking edge with respect to_ \(\eta\).

_Proof._ Since \(\eta\) is a perfect matching, for each \(i\in[k]\) and _j_=log<sub>2</sub>(_n/_2), vertex \(b_{j,1}^i\) is saturated by \(\eta\). Recall that \(N(b_{j,1}^i)=\langle a_{j,1}^i,a_{j,2}^i\rangle\). Therefore, there exists a (unique) \(z\in[2]\), such that \(b_{j,1}^ia_{j,z}^i\in\eta\).

Since \(\eta\) is a perfect matching and \(b_{j-1,z}^i\) has two other neighbors \(a_{j-1,2z-1}^i\) and \(a_{j-1,2z}^i\), it follows that either \(b_{j-1,z}^ia_{j-1,2z-1}^i\in\eta\) or \(b_{j-1,z}^ia_{j-1,2z}^i\in\eta\). We view the index _j_ as indicating a level, the highest being log<sub>2</sub>(_n/_2). As we go down each level starting from the highest, we obtain a matching edge in \(\eta\). The lowest level is reached when for some value \(h\in[n/4]\), we reach the vertex \(b_{1,h}^i\). For this vertex, there are two possible matching partners in \(\eta\): \(a_{1,2h-1}^i\) or \(a_{1,2h}^i\). Thus, for some value \(h'\in\{2h-1,2h\}\), edge \(b_{1,h}^ia_{1,h^\prime}^i\in\eta\).

Since \(\eta\) is a perfect matching, \(p_{h^\prime}^i\) must be matched to either _x_<sub>1</sub> or _y_<sub>1</sub> (its other two neighbors) in \(\eta\), where \(x=V_i(2h'-1)\) and \(y=V_i(2h')\) i.e, _x_ is the \(2h'-1^{st}\) element of _V<sub>i</sub>_ and _y_ is the 2_h<sup>th</sup>_ element of _V<sub>i</sub>_. If \(p_{h^\prime}^ix_1\in\eta\), then since _x_<sub>1</sub> and _x_<sub>2</sub> are each others first preference, the edge \(x_1x_2\in\mathtt{B}_\eta\). Otherwise, if \(p_{h^\prime}^iy_1\in\eta\), then with analogous argument, it follows that the edge \(y_1y_2\in\mathtt{B}_\eta\). Hence, the result is proved.

**Claim 15 (e-type static edge)** _For each_ \(\{i,j\}\subseteq[k]\)_, there exists_ \(e\in E_{ij}\)_, such that_ \(e\tilde{e}\) _is a blocking edge with respect to_ \(\eta\) _and_ \(q_{\lceil\epsilon/2\rceil}^{ij}e\in\eta\)_, where e is the_ \(\ell^{th}\) _element of E<sub>ij</sub>._

_Proof._ Since \(\eta\) is a perfect matching, for each \(\{i,j\}\subseteq[k]\) and _h_=log<sub>2</sub>(_m/_2), the vertex \(d_{h,1}^{ij}\) must be saturated by \(\eta\). Recall that \(N(d_{h,1}^{ij})=\langle c_{h,1}^{ij},c_{h,2}^{ij}\rangle\). Therefore, there exists a (unique) \(z\in[2]\), such that \(d_{h,1}^{ij}c_{h,z}^{ij}\in\eta\).

