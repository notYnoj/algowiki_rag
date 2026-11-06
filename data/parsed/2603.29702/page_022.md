**Definition 5.4** (Rotated LCS Grid Graph)**.** We use \(\langle\langle x,y\rangle\rangle\) to denote a vertex in the (original) LCS Grid Graph at the intersection of column _x_ and row _y_ and \(\langle x,y\rangle\) to denote a vertex in the Rotated LCS Grid Graph at the intersection of column _x_ and row _y_. The description of the new graph on the rotated grid is as follows:

**Vertices** The vertex for \(\langle\langle u,v\rangle\rangle\) in the original grid corresponds to \(\langle u+v,v-u+n_X\rangle\) on the new grid;

**Edges** We start with the same set of edges as in the original graph. Then, we divide each shortcut edge with weight \(w\left(\in\{0,1\}\right)\) from \(\langle u,v\rangle\) to \(\langle u+2,v\rangle\) into two edges, one from \(\langle u,v\rangle\) to \(\langle u+1,v\rangle\) with weight 0 and the other from \(\langle u+1,v\rangle\) to \(\langle u+2,v\rangle\) with weight _w_.

**Objective** The length of the longest path from \(\langle 0,n_X\rangle\) to \(\langle n_X+n_Y,n_Y\rangle\) equals LCS(_X,Y_).

For the remainder of the paper, a _path_ refers to a route from any \(\langle l,y_l\rangle\) to any \(\langle r,y_r\rangle\). Due to the split edges, any path _p_ in the grid graph from any column _l_ to any column _r_ visits each column \(x\in[l,r]\) exactly once. We denote by _p(x_) the y-coordinate (row) of the vertex \(\langle x,p(x)\rangle\) where the path crosses column _x_. By the construction of the rotated grid graphs, \(|p(x)-p(x-1)|\le 1\) for every \(l<x\le r\). For an interval \((l',r']\subset(l,r]\), we write \(p(l',r']\) to denote the sub-path of _p_ from \(l'\) to \(r'\). We define _w(p_) as the length (total weight of edges) of _p_.

We have the following observation:

**Observation 5.5.** For a path _p_, and for any two columns \(i\le j\) that the path visits,

\(|p(i)-p(j)|\le j-i.\)

_Proof._ We prove this by induction by increasing value of _j-i_. When _i=j_, the claim is trivially true since the path visits each column exactly once. Now suppose that the claim holds for _i,j_-1. The only edges from \(\langle j-1,p(j-1)\rangle\) go to \(\langle j,p(j-1)\rangle\), and (possibly) \(\langle j,p(j-1)\pm 1\rangle\). Therefore,

\(|p(i)-p(j)|\le|p(i)-p(j-1)|+1\le(j-1-i)+1=j-i.\)

Due to Observation 5.5, given two vertices \(\langle l,y_l\rangle\) and \(\langle r,y_r\rangle\), if \(\langle r,y_r\rangle\) is reachable from \(\langle l,y_l\rangle\), we must have \(|y_l-y_r|\le r-l\).

## 5.2 Reduction to Query-Based Approximations on Sparse Grids

We now show that the problems on the Rotated Grid Graphs can be further reduced to query-based approximation problems on sparsified versions of these grid graphs defined just now in Section 5.1.2.

Let \(M:=2\left\lfloor log(log^{0.109(n)})\right\rfloor=\Theta(log^{0.109}(n))\) and \(S:=3\cdot\left\lfloor log_M(n^{0.01})\right\rfloor\)<sup>15</sup>. Let _n_:=_n<sub>X</sub>+n<sub>Y</sub>_<sup>16</sup>. Similar to Section 4, for each scale \(s\in[S]\), we consider the partition of \[_n_\] into disjoint intervals (_l,r_\] of length _I<sub>s</sub>_:=_n/M_<sup>_S-s_</sup>, and we say that (_l,r_\] is a _scale-s interval_. Every interval (_l,r_\] that is involved in the recursive partitioning (i.e., is a scale-_s_ interval for some scale \(s\in[S]\)) is called a _recursion interval_.

Naïvely, we can design an _M_-way _S_-scale divide-and-conquer scheme to compute the length of the shortest \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path where (_l,r_\] is a scale-_s_ interval for \(s\in[S]\cup\{0\}\)<sup>17</sup>, henceforth notated by<tbc>

<sup>15</sup>Making _S_ divisible by 3 is convenient for our algorithm for LCS. <sup>16</sup>Notice that this is different from the high-level overview where the last column had index 2_n_. <sup>17</sup>As an edge case, sometimes we also use consider scale-0 intervals which are the sub-intervals of scale-1 intervals. We usually ignore scale 0 unless specified otherwise.

