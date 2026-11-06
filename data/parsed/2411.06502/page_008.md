<tbc>Under Assumption A, suppose \(\mathrm{sim}(\mathbf{T},\mathbf{T}')\) maps _c<sub>i</sub>_ to \(c'_{i^\prime}\) and _c<sub>j</sub>_ to \(c'_{j^\prime}\) for _i\<j_, and no further node _c_<sub>_i_+1</sub>_,...,c_<sub>_j_-1</sub> is mapped. Then, the nodes from _l<sub>i</sub>,...,l_<sub>_j_-1</sub> are mapped to nodes from \(l'_{i^\prime},\dots,l_{j^\prime-1^\prime}\) as in \(\mathrm{sim}(L[i..j),L'[i'..j'))\), where \(L=l_1\cdots l_n,L'=l'_{1^\prime}\cdots l'_{n^\prime}\) are strings built from the left children of the central nodes. Similarly, the nodes from _r<sub>i</sub>,...,r_<sub>_j_-1</sub> are mapped to nodes from \(r'_{i^\prime},\dots,r_{j^\prime-1^\prime}\) as in \(\mathrm{sim}(R[i..j),R'[i'..j'))\), where \(R=r_1\cdots r_n,R'=r'_{1^\prime}\cdots r'_{n^\prime}\) are strings built from the right children of the central nodes.

This brings us to the visualization of \(\mathrm{sim}(\mathbf{T},\mathbf{T}')\) (under Assumption A) illustrated in Figure 1. Consider a \([1..(n+1)]\times[1..(n'+1)]\) grid, and overlay on it the alignment graphs for string edit distance for \((L,L')\) and \((R,R')\). Then, \(\mathrm{sim}(\mathbf{T},\mathbf{T}')\) can be visualized as two paths from (1,1) to \((n+1,n'+1)\) in the two respective alignment graphs. Whenever these paths intersect at a grid point \((i,i')\), \(\mathrm{sim}(\mathbf{T},\mathbf{T}')\) has the opportunity to map _c<sub>i</sub>_ to \(c'_{i^\prime}\), provided neither _c<sub>i</sub>_ nor \(c'_{i^\prime}\) has been mapped previously.

Henceforth, we denote by \(\mathrm{sim}((x,x'),(y,y'))\) the maximum value achievable by a sum of three terms:

(1) the weight of a path from \((x,x')\) to \((n+1,n'+1)\) in the alignment graph of \(\mathrm{sim}(L,L')\);<tbc>

(2) the weight of a path from \((y,y')\) to \((n+1,n'+1)\) in the alignment graph of \(\mathrm{sim}(R,R')\); and<tbc>

(3) a sum of values of the form \(\eta(c_i,c'_{i^\prime})\) for \((i,i')\) where the two paths intersect, provided each _c<sub>i</sub>_ and \(c'_{i^\prime}\) appears at most once.

By the previous discussion, \(\mathrm{sim}(\mathbf{T},\mathbf{T}')=\mathrm{sim}((1,1),(1,1))\) under Assumption A.

## Reduction of caterpillar TED (under Assumption A) to APSP.

To compute sim((1,1),(1,1)), we utilize a divide-et-impera scheme. Given a rectangle in the grid defined by the lower-left corner \((a,a')\) and the upper-right corner \((b,b')\), along with \(\mathrm{sim}((x,x'),(y,y'))\) for all \((x,x'),(y,y')\) on the upper-right border of the rectangle, our task is to determine \(\mathrm{sim}((x,x'),(y,y'))\) for all \((x,x'),(y,y')\) on the lower-left border of the rectangle. Note that computing the inputs becomes trivial when the rectangle we are considering is the whole grid.

Let _a\<r\<b_. We split the rectangle vertically into two smaller rectangles (see Figure 2): one with corners \((a,a')\) and \((r,b')\) and the other with corners \((r,a')\) and \((b,b')\). We aim to recurse on those two subrectangles.

7
T
T'
6
5
4
0
3
0
2
0
1
1
2
3
4
5
6
7
Figure 1 Overlaying the alignment graphs for string edit distance for (L, L') and (R, R') leads to an intuitive visualization of TED on caterpillar trees under the assumption that central nodes are only mapped to central nodes, left children only to left ones, and right children only to right ones (Assumption A). The problem can be visualized as two paths in the two graphs, which, whenever they intersect, allow mapping of central nodes to central nodes.

