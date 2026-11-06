**Lemma 5.4.** _For each_ \(i\ge 0\)_, the nodes in_ \(T\langle U_i,x\rangle\) _with minimum label induce a connected subtree._

The next two lemmas will be used to conclude that the number of light queries performed by A<sub>_S_<sup>+</sup></sub> is bounded by 2log<sub>2</sub>_n_ (see Lemma 5.7).

**Lemma 5.5.** _If the i-th query of_ A<sub>_S_<sup>+</sup></sub> _is an R-query resulting in an ‘up’ reply, then_ \(C_{i+1}\ge C_i+1\).

_Proof._ By construction, _u<sub>i</sub>_ has the minimum label among all nodes in \(T\langle U_{i-1},x\rangle\). By Lemma 5.4, either _u<sub>i</sub>_ is the unique node with label \(\ell(u_i)\) in the tree \(T\langle U_{i-1},x\rangle\) or there are more nodes with this label and they all belong to a single extended heavy part in \(T\langle U_{i-1},x\rangle\) with _u<sub>i</sub>_ being closest to the root of \(T\langle U_{i-1},x\rangle\). In both cases, since the reply is ‘up’, we obtain that \(T\langle U_i,x\rangle\) has no node with label \(\ell(u)\), which proves the lemma.

**Lemma 5.6.** _If the i-th query of_ A<sub>_S_<sup>+</sup></sub> _is an R-query that results in a ‘down’ reply, then one of the two cases holds:_

(i) _if u<sub>i</sub> has no heavy child that belongs to_ \(T\langle U_i,x\rangle\)_, then_ \(C_{i+1}\ge C_i+1\),<tbc>

(ii) _if u<sub>i</sub> has a heavy child that belongs to_ \(T\langle U_i,x\rangle\)_, then_ \(C_{i+1}=C_i=\ell(u_i)\) _and for each j\>i such that C<sub>i</sub>=C_<sub>_j_+1</sub>_, all queries i_+1_,...,j are S-queries._

_Proof._ By Lemma 5.4, the nodes with label _C<sub>i</sub>_ induce a connected subtree in \(T\langle U_{i-1},x\rangle\). This immediately implies (i). By construction, if _u<sub>i</sub>_ has a heavy child \(u'\) that is in \(T\langle U_i,x\rangle\), then \(u'=r(T\langle U_i,x\rangle)\) and the labels of _u<sub>i</sub>_ and \(u'\) are the same. The latter is due to the fact that both _u<sub>i</sub>_ and \(u'\) belong to the same extended heavy part in _T_. Suppose for a contradiction that the _j_-th query (performed say on a node _z_) is an _R_-query and _C_<sub>_j_+1</sub>=_C<sub>i</sub>_, _j\>i_. This in particular implies that \(z\in R(r(T\langle U_{j-1},x\rangle))\). Due to Lemma 5.5, the reply to this query is ‘down’. By (i), _z_ has a heavy child that belongs to \(T\langle U_j,x\rangle\). By Observation 5.1, _z_ is a light node and therefore _z_ along with some of its descendants and _u<sub>i</sub>_ with some of its descendants form two different extended heavy parts in _T_. Since _z_ and _u<sub>i</sub>_ have the same label, there exists a light node \(u'_i\) in _T_ on the path between _u<sub>i</sub>_ and _z_ with label smaller than \(\ell(u_i)\). Assume without loss of generality that no other node of this path that lies between _u<sub>i</sub>_ and \(u'_i\) has label smaller than \(\ell(u'_i)\). The above-mentioned path is contained in \(T\langle U_{i-1},x\rangle\) since both _u<sub>i</sub>_ and _z_ belong to this<tbc>

T:
V1
TC:
4
V1
assignment R:
R(v1) = (v6, v3, v2)
v2
v3
h1
h2
R(v3) = (v6)
v2
H1
2
3
v4
V5
H2
v6
3
v6
v4
V5
v6
v9
1
v7
3
v7
v8
v8
R(v8) = (v10)
v9
2
v9
v10
h3
v10
H3
v11
3
v11
v11
v12
v13
v12
v13

Figure 5.1: A tree _T_ (on the left) has light vertices (marked as white nodes) and heavy ones (dark circles); also heavy extended parts are marked. The tree _T<sub>C</sub>_ (in the middle) is used together with its labeling (integers are the labels) to obtain the sequence assignment _R_ (on the right); here we skip the sequence assignment for each node _v_ for which \(R(v)=\emptyset\).

