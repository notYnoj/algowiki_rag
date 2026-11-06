3. Consider an STT rooted at a leaf: Again by symmetry, it suffices to consider only STTs rooted at 7.<tbc>

(a) If the child of the root is 3, then the remaining nodes divide again to independent legs, and we have a clear best STT among the four options. Its weighted depth is \(w\cdot[2,3,1,3,2,2,0]=6+6+0+6+6+6+6+0=30\).<tbc>

(b) If the child of the root is 6, then its subtree is a BST over the path of nodes 1 to 5, and as we analyzed a best option has depths \[1,0,3,2,1\] when rooted. In this case, the weighted depth is \(w\cdot[3,2,5,4,3,1,0]=9+4+0+8+9+3+0=33\).<tbc>

(c) If the child of the root is 4 (choosing 2 is symmetric): then 5 breaks-away to its own subtree, and the remainder is a BST over {1,2,3,6}. Since 3 can be pushed down (zero weight), one can verify that the best BST over {1,2,6} is rooted at 2. Overall, we get in this case a weighted depth of \(w\cdot[3,2,4,1,2,3,0]=9+4+0+2+6+9+0=30\).<tbc>

(d) If the child of the root is 5 (choosing 1 is symmetric):<tbc>

i. Rooting the sub-sub-tree at _v_ such that _v_ is either 1, 4 or 6 is sub-optimal: it leaves the remaining nodes as a single connected component, and even if we assume that the depth of each of them is only 3 (direct children of _v_), then the weighted depth is at least: \(0\cdot w_7+1\cdot w_5+2\cdot w_v+3\cdot(10-w_v)=33-w_v\ge 30\).<tbc>

ii. Rooting the sub-sub-tree at 3: two options remain due to the leg of (1,2), but the better weighted depth among them is \(w\cdot[3,4,2,3,1,3,0]=9+8+0+6+3+9+0=35\).<tbc>

\begin{tabular}{ccccccccc}
\(\left[\begin{array}{ c }
X \\
D
\end{array}\right]=\) & \(\left[\begin{array}{ c c c c c }
. & h & h & 0 & 0 & 0 & 0 & 0 \\
h & . & 1 & h & h & h & 0 \\
0 & 0 & . & 0 & 0 & 0 & 0 & 0 \\
h & h & 1 & . & h & h & 0 & 0 \\
0 & 0 & h & h & . & 0 & 0 & 0 \\
h & h & 1 & h & h & . & h & 0 \\
h & h & h & h & h & h & h & . \\
2 & 2 & 4.5 & 2 & 2 & 1.5 & 0.5
\end{array}\right]\) & \(\left[\begin{array}{ c }
Z_{213}=Z_{214}=Z_{215}=Z_{415}=Z_{216}=Z_{617}=h \\
Z_{314}=Z_{315}=Z_{316}=Z_{217}=Z_{317}=0 \\
Z_{425}=Z_{627}=h \\
Z_{324}=Z_{325}=Z_{326}=Z_{327}=0 \\
Z_{435}=Z_{637}=Z_{647}=Z_{456}=Z_{657}=h \\
Z_{346}=Z_{347}=Z_{356}=Z_{357}=Z_{457}=0
\end{array}\right]\) & \(\text{(1)}\) \\
\(\left[\begin{array}{ c }
X_{12}+X_{21} \\
X_{13}+X_{31}+Z_{213} \\
X_{14}+X_{41}+Z_{214}+Z_{314} \\
X_{15}+X_{51}++Z_{215}+Z_{315}+Z_{415} \\
X_{16}+X_{61}+Z_{216}+Z_{316} \\
X_{17}+X_{71}+Z_{217}+Z_{317}+Z_{617} \\
X_{23}+X_{32} \\
X_{24}+X_{42}+Z_{324} \\
X_{25}+X_{52}+Z_{325}+Z_{425} \\
X_{26}+X_{62}+Z_{326} \\
X_{27}+X_{72}+Z_{327}+Z_{627}
\end{array}\right]\) & \(=\left[\begin{array}{ c }
h+h \\
0+h+h \\
0+h+h+0 \\
0+0+h+0+h \\
0+h+h+0 \\
0+h+0+h \\
0+h+0+0+h \\
1+0 \\
h+h+0 \\
h+0+0+h \\
h+h+0 \\
0+h+0+h
\end{array}\right]\) & \(\left[\begin{array}{ c }
X_{34}+X_{43} \\
X_{35}+X_{53}+Z_{435} \\
X_{36}+X_{63} \\
X_{37}+X_{73}+Z_{637} \\
X_{45}+X_{54} \\
X_{46}+X_{64}+Z_{346} \\
X_{47}+X_{74}+Z_{347}+Z_{647} \\
X_{56}+X_{65}+Z_{356}+Z_{456} \\
X_{57}+X_{75}+Z_{357}+Z_{457}+Z_{657} \\
X_{67}+X_{76}
\end{array}\right]\) & \(=\left[\begin{array}{ c }
0+1 \\
0+h+h \\
0+1 \\
0+h+h \\
h+h \\
h+h+0 \\
0+h+0+h \\
0+h+0+h \\
0+h+0+0+h \\
h+h
\end{array}\right]\) & \(\left[\begin{array}{ c }
Z_{213}=Z_{214}=Z_{215}=Z_{216} \\
Z_{617}=Z_{627}=Z_{637}=Z_{647}=Z_{657} \\
Z_{415}=Z_{425}=Z_{435}=Z_{456}
\end{array}\right]\) & \(=h\le\left[\begin{array}{ c }
X_{21},X_{23},X_{24},X_{25},X_{26} \\
X_{61},X_{62},X_{63},X_{64},X_{65},X_{67} \\
X_{41},X_{42},X_{43},X_{45},X_{46}
\end{array}\right]\) & \(=\left[\begin{array}{ c }
h,1,h,h,h \\
h,h,1,h,h,h \\
h,h,1,h,h
\end{array}\right]\) & \(\text{(2)}\)

Figure 3: The vertex _P_. (Eq. 1) The values of _P_, where \(h=\frac{1}{2}\) (short for half). The _Z_ variables are separated to three pairs of rows (of values 0 and _h_). The first pair covers all _Z_<sub>_k_1_j_</sub>, the next pair covers all _Z_<sub>_k_2_j_</sub> and the last pair covers _Z<sub>kij</sub>_ for \(i\ge 3\). The vector _D_ is a column-sum of the matrix _X_. (Eq. 2) Proof of feasibility, listing all the ancestry-inequalities. Inequalities of the form \(Z_{kij}\le X_{ki},X_{kj}\) are verified in "bulk" (only non-trivial for _Z<sub>kij</sub>\>_0).

