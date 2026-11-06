▶ Definition B.6. _For a subpermutation s of length n, define the_ distance matrix _Ms of size_ \((n+1)\times(n+1)\) _such that_ \(M_{i,j}^s\) _for any_ \(i,j\in[0..n]\) _is equal to the length of the longest path in G<sup>s</sup> from_ (_i,_0) _to_ (_j,|s_<sup>∗</sup>|).

Note that the matrix _Ms_ is well-defined because, for every \(i,j\in[0..n]\), there is a path from (_i,_0) to (_j,|s_<sup>∗</sup>|) in _G<sup>s</sup>_, and since _G<sup>s</sup>_ does not contain any cycles of nonnegative length by Lemma B.5, there exists a longest such path. Furthermore, the matrix _Ms_ is anti-Monge by the following fact. (If we negate the weights in _G<sup>s</sup>_, we obtain that the matrix -_Ms_ of the shortest paths in such a graph is Monge.)

▶ Fact B.7 ([20, Section 2.3]). _Consider a weighted directed planar graph G. For vertices_ _u_<sub>0</sub>_,...,u_<sub>_p_-1</sub>_,v_<sub>_q_-1</sub>_,...,v_<sub>0</sub> _lying (in this cyclic order, potentially with repetitions) on the outer face of G, define a_ \(p\times q\) _matrix D with Di<sub>i,j</sub>_=dist_<sub>G</sub>(u<sub>i</sub>,v<sub>j</sub>), where_ dist_<sub>G</sub> denotes the shortest path distance in G. If all entries of D are finite, then D is a Monge matrix._

Proof Sketch. We need to prove \(D_{i,j}+D_{i+1,j+1}\le D_{i,j+1}+D_{i+1,j}\) for \(i\in[0..p-1)\) and \(j\in[0..q-1)\). Note that _D<sub>i,j</sub>_+1=dist_<sub>G</sub>(u<sub>i</sub>,v_<sub>_j_+1</sub>) and _D<sub>i+1,j</sub>_=dist_<sub>G</sub>(u_<sub>_i_+1</sub>_,v<sub>j</sub>_). Fix a

5
4
3
2
1
0
0
1
2
3
4
5
6

u+1
Q
vj+1
w
P
ui
vj

**Figure 4** The alignment graph for _s_=[1,0,3,★,2,4], with red edges of weight 0, green edges of weight 1, and blue edges of weight -2.

**Figure 5** The sum of the distances from _u<sub>i</sub>_ to _v_<sub>_j_+1</sub> and from _u_<sub>_i_+1</sub> to _v<sub>j</sub>_ is not smaller than the sum of the distances from _u<sub>i</sub>_ to _v<sub>j</sub>_ and from _u_<sub>_i_+1</sub> to _v_<sub>_j_+1</sub>.

