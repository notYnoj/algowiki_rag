So if the original formula \(\psi\) was \(C_1\wedge\cdots\wedge C_m\), the transformed formula \(\psi=C_1\wedge\cdots\wedge C_m\wedge C_{m+1}\wedge\cdots\wedge C_{m+n}\wedge D_{m+n+1}\wedge\cdots\wedge D_{m+2n}\), where _C_<sub>1</sub>_,...,C<sub>m</sub>_ are the original _m_ clauses with negated literals substituted by new variables and for \(1\le i\le n\), _C_<sub>_m+i_</sub> is the clause \(X_i\vee X_{n+i}\) and _D_<sub>_m+n+i_</sub> is the clause \(\neg X_i\vee\neg X_{n+i}\).

\(G_\psi\) is essentially the parallel composition of _clause gadgets_, all sharing exactly two vertices _s_ and _t_. A _positive_ clause gadget corresponds to one of the _C<sub>i</sub>_’s and a _negative_ clause gadget corresponds to one of the _D<sub>i</sub>_’s. Each clause gadget is a series composition of _literal gadgets_ and the gadgets corresponding to positive and negative literals are different (see Fig. 9).

We now describe the preference lists of vertices in a positive clause \(C_\ell=x\vee y\vee z\) (see Fig. 7). We first describe the preference lists of \(u_\ell,v_\ell,u'_\ell,v'_\ell,u''_\ell,v''_\ell\).

\(u_\ell:v_\ell\succ su'_\ell:v'_\ell\succ b_xu''_\ell:v''_\ell\succ b_yv_\ell:a_x\succ u_\ellv'_\ell:a_y\succ u'_\ellv''_\ell:a_z\succ u''_\ell\)

Thus \(u_\ell\) has 2 neighbors: \(v_\ell\) (top choice) and _s_ (second choice). Other preference lists are analogous. Recall that we assumed _x_ to be the first literal, _y_ to be the second literal, and _z_ to be the third literal in \(C_\ell\). We next describe the preference lists of the 4 vertices \(a_x,b_x,a'_x,b'_x\) that occur in _x_’s gadget in \(C_\ell\).

\(a_x:b'_x\succ v_\ell\succ b_xa'_x:b_x\succ b'_x\succ\underline{d'_x}b_x:u'_\ell\succ a_x\succ\underline{c_x}\succ a'_xb'_x:a'_x\succ a_x\)

The underlined vertices _c<sub>x</sub>_ and \(d'_x\) will occur in the gadget of \(\neg x\) (similarly for vertices \(c_y,d'_y,c_z,d'_z\) below). Below are the preference lists of the 4 vertices \(a_y,b_y,a'_y,b'_y\) that occur in _y_’s gadget in \(C_\ell\).

\(a_y:b'_y\succ v'_\ell\succ b_ya'_y:b_y\succ b'_y\succ\underline{d'_y}b_y:u''_\ell\succ a_y\succ\underline{c_y}\succ a'_yb'_y:a'_y\succ a_y\)

The preference lists of the 4 vertices \(a_z,b_z,a'_z,b'_z\) that occur in _z_’s gadget in \(C_\ell\) are given below.

\(a_z:b'_z\succ v''_\ell\succ b_za'_z:b_z\succ b'_z\succ\underline{d'_z}b_z:a_z\succ\underline{c_z}\succ a'_z\succ tb'_z:a'_z\succ a_z\)

The preference lists of _s_ and _t_ are arbitrary (they do not matter for our arguments). The preference lists of vertices that occur in a clause gadget with 2 positive literals will be totally analogous to the preference lists of vertices in a clause gadget with 3 positive literals. In more detail, the edge \((u''_\ell,v''_\ell)\) will be missing and so will the third literal gadget. In particular, the vertex _t_ will be adjacent to the _b_-vertex in the gadget of the second literal and _t_ will be the last choice of this _b_-vertex.

uell
vell
ax
bx
u'ell
v'ell
ay
by
u'ell
v''ell
az
bz
S
t
b' x
a' x
b' y
a' y
b' z
a' z

**Fig.7.** A clause gadget corresponding to a positive clause \(C_\ell=x\vee y\vee z\). The endpoints of this path, i.e., _s_ and _t_, are common to all clauses. The solid edges have cost 0 while the dashed edges have cost 1.

