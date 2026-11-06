In the next section, it will be proved that the triangular graphs are integral.

Before that, it is worth recalling the following notions which appear in \[4\].

An edge clique partition (ECP for short) of a graph _G_ is a partition of the set of edges such that each part induces a complete graph. Considering a graph _G_ and an ECP \(P=\{E_i|i\in I\}\), it follows that _V<sub>i</sub>=V(G_\[_E<sub>i</sub>_\]) is a clique of _G_ for every \(i\in I\). For any \(v\in V(G)\), the clique degree of _v_ relative to _P_, denoted _m<sub>v</sub>(P_), is the number of cliques _V<sub>i</sub>_ containing the vertex _v_, and the maximum clique degree of _G_ relative to _P_, denoted _m<sub>G</sub>(P_), is the maximum of clique degrees of the vertices of _G_ relative to _P_.

It is also worth to recall the next theorem which also appears in \[4\].

**Theorem 2.2.** \[4\] _Let_ \(P=\{E_i|i\in I\}\) _be an ECP of a graph G, m=m<sub>G</sub>(P_) _and m<sub>v</sub>=m<sub>v</sub>(P_) _for every_ \(v\in V(G)\)_. Then_

1. _If_ \(\mu\) _is an eigenvalue of G, then_ \(\mu\ge-m\).<tbc>

_2._ _-m is an eigenvalue of G if and only if there exists a vector_ \(x\neq\mathbf{0}\) _such that_<tbc>

(_a)_ \(\sum_{j\in V(G[E_i])}x_j=0\)_, for every_ \(i\in I\) _and_<tbc>

_(b)_ \(\forall v\in V(G)x_v=0\) _whenever_ \(m_v\neq m\).<tbc>

_In the positive case, x is an eigenvector associated with -m._

## 3 Spectral properties of T(_n_)

Since the vectors in this section have a triangular number of components, they are written over T_<sub>n</sub>_, as in the previous section. Therefore, the _a_<sup>th</sup> coordinate of a vector _v_ will be displayed at the entry (_i,j_) of T_<sub>n</sub>_ for _a=T(i_-1)+_j_ and it will be denoted by _v<sub>a</sub>_ or _v_<sub>(_i,j_)</sub>.

**Example 3.1.** _The vector v_=\[1,2,3,4,5,6,7,8,9,10\]_<sup>T</sup> consists of T_(4)=10 _components. This type of vector will be displayed on a triangular board, as illustrated in Figure 3. So, for example, the_ 5_<sup>th</sup> component of v, which is_ 5_, will_<tbc>

<tbc>_be denoted v_<sub>(3,2)</sub> _because it is in the_ 3_<sup>th</sup> row and_ 2_<sup>nd</sup> column._

Consider the following definition.

1
2
3
v =
4
5
6
7
8
9
10

Figure 3: A vector on the triangular board.

