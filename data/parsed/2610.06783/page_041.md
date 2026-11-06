<tbc>The **_value_** of a cube \(\pi\) is the sum of the products at its leaves,

\(val(\pi):=\sum_{\tau\text{a leaf of}\pi}\Phi_\tau(a)\Psi_\tau(b).\)

Every output entry is the value of a cube. Indeed, recall that the entry (_X<sub>Q</sub>Y<sub>Q</sub>_)\[_w_\] of an output string _w_ with inner set _Q_ is the sum of the products at the 10_<sup>m</sup>_ leaves contributing to _w_. These are the leaves of the **_cube of_** _w_, the cube \(\pi^w\) that has a star at each level where _w_ has _z_<sub>0</sub> (the levels of _Q_) and the term _P<sub>ij</sub>_ at each level where _w_ has _z<sub>ij</sub>_, so that \((X_QY_Q)[w]=val(\pi^w)\). In Figure 6, this cube is all the rows taken together. Figure 9 shows the cube of an output string, and the boxes defined next, in the recursion tree of a small example.

We will cut the cube of every output string into parts that are again cubes, in a way where each leaf of the cube lies in exactly one part, so that

\((X_QY_Q)[w]=val(\pi^w)=\sum_\text{parts}\pi\text{of}\pi^wval(\pi),\)

and the value of a part will be shared by all the output strings that have it as a part. In Lemma 28 below, we will prove this equation for the parts that we will choose. There will be two kinds of parts. Each leaf of small order will be a part on its own (recall that a single leaf is a cube without stars), whereas the leaves of large order will be grouped together into larger parts, which we call boxes.

## The definition of a box.

The order of a leaf tells us how widely it is shared between output entries. Recall that the order is _m_ minus the number of levels at which the leaf chooses _P_<sub>0</sub>, so that \(\alpha_d=\genfrac(){pt}{2}{m}{d}9^d\) leaves of order _d_ contribute to an output string, and that a leaf of larger order<tbc>

root
level 1 E Q
Po
P11
P12
P13
P21
P22
P23
P31
P32
P33
P21 is the term of w at level 2
level 2 Q
P21
P21
P21
P21
P21
P21
P21
P21
P21
P21
P21
Private leaf
Po
9 boxes Pij P21 Po
P11
P12
P13
P21
P21
level 3 E Q
9 boxes P21 Pij
P22
P23
P31
P32
P33
one subtree
order:
0
1
2
the cube πw = * P21 *

Figure 9: The cube and the boxes of the output string _w=z_<sub>0</sub>_z_<sub>21</sub>_z_<sub>0</sub> in the recursion tree, for _L_=3 and switching order _t_=1. Since _w_ has _z_<sub>0</sub> at levels 1 and 3, its inner set is _Q_={1,3} (so _m_=2). A query for _w_ reads the private leaf, which has order 0_\<t_, and the values of the \(\alpha_1=18\) boxes of _w_, which contain the other 99 leaves (of orders 1 and 2). A box with a star is not a subtree: it consists of the same leaf of every subtree.

