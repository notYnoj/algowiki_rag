<tbc>only monomial of _G+E_ that contains _z<sub>ij</sub>_ and no inner variable is _x<sub>i</sub>y<sub>j</sub>z<sub>ij</sub>_, with coefficient 1, so \((u_\ell,v_\ell)=(x_i,y_j)\).

Hence, the summands that remain are those where _u_ has inner set _Q_, the row _r_ of _w_ as its outer part, and some inner part \(\pi\), and where _v_ has inner set _Q_, the column _c_ of _w_ as its outer part, and the inner part \(\pi'\) with the same indices as \(\pi\). There is one such summand for each of the _D_ strings \(\pi\), and its coefficient is 1. Their sum is \(\sum_\pi X_Q[r,\pi]Y_Q[\pi',c]=(X_QY_Q)[w]\).

To summarize: one run of Full, which uses 10_<sup>L</sup>_ multiplications, computes all _K_ of the products _X<sub>Q</sub>Y<sub>Q</sub>_. The _K_ products can be completely independent: we are free to plug in any choices for _X<sub>Q</sub>_ and _Y<sub>Q</sub>_ and the algorithm will give us all _K_ products. In the next subsection we will end up plugging in the same matrix for different copies _X<sub>Q</sub>_ (and _Y<sub>Q</sub>_).

## 2.3.4 Tiling the \(N\times D\times N\) product by products of shape \(N_0\times D\times N_0\)

We now use our algorithm, which performs _K_ simultaneous multiplications of an \(N_0\times D\) matrix with a \(D\times N_0\) matrix, in order to do a single multiplication of an \(N\times D\) matrix _X_ with a \(D\times N\) matrix _Y_ . For our parameter setting, \(N\gg N_0\), so we can do this with a simple tiling approach. Tiling enlarges only the outer dimensions, so it handles a smaller inner dimension than Coppersmith’s algorithm from the same identity (at best _D≈N_<sup>0.1204</sup> rather than _N_<sup>0.1402</sup> \[Cop82\]). We use it because each entry of _XY_ is then a single output of a single run of Full, rather than a linear combination of many outputs as in Coppersmith’s algorithm. We will take advantage of this in our algorithm below (Section 2.4).

We cut _X_ into **_row blocks_** of _N_<sub>0</sub> consecutive rows and _Y_ into **_column blocks_** of _N_<sub>0</sub> consecutive columns. Thus, _XY_ consists of all the products of a row block by a column block,<tbc>

outer part x1x2x3x1: the row of u in XQ,
left string u:
X1
P11
X2
X3
P22
X1
inner part p11p22: its column,
so u indexes an entry of XQ
inner part q11q22: the row of v in YQ, outer part y3y1y3y2: its column,
right string v:
y3
q11
y1
y3
q22
y2
so v indexes an entry of YQ
row x1x2x3x1 and column y3y1y3y2, read off from its zij, so w indexes an entry of XQYQ
output string w:
Z13
Z0
Z21
Z33
Z0
Z12
levels 1 = 1,...,6 (shaded: the inner set Q = {2,5})
XQ: 81 x 16
YQ: 16 x 81
XQYQ: 81 x 81
row x1x2x3x1
(XQYQ)[w]
column y3y1y3y2
=

Figure 4: From strings to matrix entries, for _L_=6 and _m_=2. A string whose inner set is _Q_={2,5} has an inner variable (_p,q_, or _z_<sub>0</sub>) at the two levels of _Q_ and an outer one at the other four. One run of Full computes all \(\genfrac(){pt}{2}{6}{2}=15\) products _X<sub>Q</sub>Y<sub>Q</sub>_, one for each subset _Q_ of size 2.

