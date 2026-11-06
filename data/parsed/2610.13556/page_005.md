<tbc>The union has chromatic number three. For any three-color source _w_, let _N<sub>u</sub>(i),N<sub>v</sub>(i_) count the leaves of color _i_ at the two centers. Repairing the center colors to distinct labels _i,j_ has minimum tree cost

\(N_u(i)+N_v(j)+\mathbf{1}_{\{w(u)\neq i\}}+\mathbf{1}_{\{w(v)\neq j\}}.\)

Its average over the six ordered pairs is 2_s_+4/3. Some integer cost is therefore at most 2_s_+1. The triangle needs at most two changes, giving the required upper bound.

It follows that

\(B_\mathrm{w}(T_s)+B_\mathrm{w}(K_3)-B_\mathrm{w}(T_s\sqcup K_3)\ge 2\left\lfloor\frac{3s+1}{2}\right\rfloor-(2s+3)\ge s-3.\)

Choosing an integer _s\>C_+3 proves the stated strict inequality. □

For the ordinary parameter, the chromatic numbers can be equal and the two connected summands can even be isomorphic. We use the following general observation about a feasible profile **p** on _N_ vertices. If two proper targets of that profile have disjoint color-_X_ classes of size _p<sub>X</sub>_, then every source of profile **p** agrees with one of them on at least

\(\mathrm{max}\left\{0,\left\lceil\frac{3p_X-N}{2}\right\rceil\right\}\) (3.2)

vertices. Indeed, the source _X_-set has size _p<sub>X</sub>_, and its intersection with the union of the two target _X_-sets has size at least 3_p<sub>X</sub>-N_. One of the two intersections has at least half that size.

**Theorem 3.2.** _For every real C\>_0_, there exists a connected graph G with_ \(\chi(G)=3\) _such that_

\(B(G\sqcup G)<2B(G)-C.\)

_Here the union consists of two vertex-disjoint copies of G._

_Proof._ For each positive integer _t_, take

\(J_t=\overline{K_{5t}}\vee\left(K_{t,2t}\sqcup K_{t,3t}\right),\)

where the join adds every edge between its two arguments. This is a connected graph of order 12_t_ and chromatic number three. Denote its five independent vertex sets by _S,L_<sub>1</sub>_,R_<sub>1</sub>_,L_<sub>2</sub>_,R_<sub>2</sub>, of respective sizes 5_t,t,_2_t,t,_3_t_. The set _S_ is joined to all four other sets, and the remaining edges are those between _L<sub>i</sub>_ and _R<sub>i</sub>_ for _i_=1,2.

In a proper three-coloring, the bipartite remainder requires two colors, so _S_ must use only the third. Each of its two connected components then has its two possible binary colorings. The possible unordered profiles on _J<sub>t</sub>_ are precisely _t_(2,5,5) and _t_(3,4,5). The labeled profile (3_t,_4_t,_5_t_) has a unique proper realization: _C_ occupies _S_, _A_ occupies \(R_1\cup L_2\), and _B_ occupies \(L_1\cup R_2\). A source with this profile and no agreement is described by the matrix

\(t\left(\begin{array}{ c c c }
0 & 2 & 1 \\
0 & 0 & 4 \\
3 & 2 & 0
\end{array}\right),\)

whose rows are these target classes and whose columns count the source colors. Its row and column sums are (3_t,_4_t,_5_t_), and its diagonal vanishes. Hence _B(J<sub>t</sub>_)=12_t_.

Adding two permutations of the possible profiles gives exactly the following sorted profiles on 2_J<sub>t</sub>_, divided by _t_:

\((4,10,10),(5,9,10),(6,8,10),(6,9,9),(7,7,10),(7,8,9),(8,8,8).\)

For clarity, adding two copies of (2,5,5) gives the first or fifth; mixing the two types gives the second, third, or sixth; adding two copies of (3,4,5) gives the third through seventh. In every unbalanced case the table supplies two targets with disjoint _C_-classes. Each five-letter word assigns colors to (_S,L_<sub>1</sub>_,R_<sub>1</sub>_,L_<sub>2</sub>_,R_<sub>2</sub>) in one copy, and the separator distinguishes the two copies.

