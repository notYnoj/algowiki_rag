- When _x_=true, the edge \((c_x,d_x)\in M\) and so _g<sub>M</sub>(d<sub>x</sub>,u<sub>k</sub>_)=2 and we have \(\alpha_{d_x}=\alpha_{u_k}=1\). Then _y_=false, the edges \((c_y,d'_y),(c'_y,d_y)\) are in _M_ and so \(g_M(c_y,v_k)=g_M(d_y,u'_k)=-1\). It is easy to see that these edges are covered.<tbc>

- When _x_=false, the edge \((c'_x,d_x)\in M\) and so \(g_M(d_x,u_k)=-1=\alpha_{d_x}+\alpha_{u_k}\). Then _y_=true and the edge \((c_y,d_y)\in M\) and so \(g_M(c_y,v_k)=-1=\alpha_{v_k}+\alpha_{c_y}\) while \(g_M(d_y,u'_k)=2=\alpha_{d_y}+\alpha_{u_k^\prime}\).<tbc>

**-** The edges incident to _s_ and _t_ are covered in all cases.

Consider any positive clause, say \(C_\ell=x\vee y\vee z\) with 3 literals. We have three cases here: (i) _x_=true, (ii) _x_=false and _y_=true, (iii) _x=y_=false and _z_=true. For a positive clause with 2 literals, only cases (i) and (ii) occur.

Let \(a_x,b_x,a'_x,b'_x\) be the 4 vertices in _x_’s gadget in \(C_\ell\) and let \(a_y,b_y,a'_y,b'_y\) be the 4 vertices in _y_’s gadget in \(C_\ell\). The \(\alpha\)-values of these 8 vertices along with those of \(u_\ell,v_\ell,u'_\ell,v'_\ell\), and \(u''_\ell,v''_\ell\) in cases (i)-(iii) are given below.

Let \(a_z,b_z,a'_z,b'_z\) be the 4 vertices in _z_’s gadget in \(C_\ell\): \(\alpha\)-values of these 4 vertices in cases (i)-(iii) are described below.

- In case (i) and case (ii), _z_ could be either true or false: if _z_=true then set \(\alpha_{a_z}=\alpha_{b_z}=\alpha_{a_z^\prime}=\alpha_{b_z^\prime}=0\), else set \(\alpha_{a_z}=\alpha_{a_z^\prime}=1\) and \(\alpha_{b_z}=\alpha_{b_z^\prime}=-1\).<tbc>

**-** In case (iii), _z_=true: set \(\alpha_{a_z}=\alpha_{b_z}=\alpha_{a_z^\prime}=\alpha_{b_z^\prime}=0\).

See Fig. 11 for the assignment of \(\alpha\)-values in case (iii).

In the 3 cases above, it is easy to check that all edges in the 4-cycles corresponding to literal gadgets are covered by the above assignment of \(\alpha\)-values. Similarly, the _u-v_, \(u'\)-\(v'\), \(u''\)-\(v''\) edges are covered and the edges incident to _s_ and _t_ are also covered.

Claim 3 below shows that every _link_ edge (such as \((v_\ell,a_x)\) and \((b_x,u'_\ell)\)) is also covered.

**Claim 3** _Every link edge is covered in the 3 cases given above._

_Proof._ Consider case (i): here the edges \((a_x,b'_x)\) and \((a'_x,b_x)\) are in _M_. So \(g_M(a_x,v_\ell)=-1=\alpha_{v_\ell}+\alpha_{a_x}\). We have \(g_M(b_x,u'_\ell)=-1=\alpha_{b_x}+\alpha_{u_\ell^\prime}\). Regarding the other two literal gadgets:

- We have \(g_M(a_y,v'_\ell)\le 2=\alpha_{a_y}+\alpha_{v_\ell^\prime}\). Similarly, \(g_M(b_y,u''_\ell)=-1=\alpha_{b_y}+\alpha_{u_\ell^{\prime\prime}}\).<tbc>

**-** If \(z=\mathsf{false}\), then \(g_M(a_z,v''_\ell)=2=\alpha_{a_z}+\alpha_{v_\ell^{\prime\prime}}\); else \(g_M(a_z,v''_\ell)=-1\le\alpha_{a_z}+\alpha_{v_\ell^{\prime\prime}}\).<tbc>

\begin{tabular}{ccccccccccccccc}
 & \(\alpha_{u_\ell}\) & \(\alpha_{v_\ell}\) & \(\alpha_{a_x}\) & \(\alpha_{b_x}\) & \(\alpha_{a_x^\prime}\) & \(\alpha_{b_x^\prime}\) & \(\alpha_{u_\ell^\prime}\) & \(\alpha_{v_\ell^\prime}\) & \(\alpha_{a_y}\) & \(\alpha_{b_y}\) & \(\alpha_{a_y^\prime}\) & \(\alpha_{b_y^\prime}\) & \(\alpha_{u_\ell^{\prime\prime}}\) & \(\alpha_{v_\ell^{\prime\prime}}\) \\
_case(i_) & 0 & 0 & -1 & 1 & -1 & 1 & -2 & 2 & 0 & 0 & 0 & 0 & -1 & 1 \\
_case(ii_) & -1 & 1 & 1 & -1 & 1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 & -1 & 1 \\
_case(iii_) & -1 & 1 & 1 & -1 & 1 & -1 & 0 & 0 & 2 & -2 & 2 & -2 & 1 & -1 \\
\end{tabular}

0
ui
Vi
ax
bx
u'
Vi
ay
by
u''
u''
az
bz
0
S
-1
1
1
-1
0
0
2
1
-2
1
-1
0
0
t
-1
1
-2
2
0
0
b'
a'
a'
b'
a'
a
y
b'
a'
z

**Fig.11.** The \(\alpha\)-values we assigned in case (iii) for the gadget corresponding to \(C_\ell=x\vee y\vee z\) are indicated next to vertices. The solid edges are in _M_ and the edges \((a_x,v_\ell)\) and \((a_y,v'_\ell)\) are blocking edges to _M_.

