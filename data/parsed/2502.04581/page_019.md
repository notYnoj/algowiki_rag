Let the co-clauses of \(\varphi\) be _V_<sub>1</sub>_,...,V<sub>h</sub>_. Thus, we aim to decide a formula of the form:

\(Q_1a'\in A'\forall b'\in B'\exists c'\in C':\vee_{i=1}^hV_i\) (2)

For each co-clause _V<sub>i</sub>_, \(i\in\{1,\dots,h\}\) it holds that _V<sub>i</sub>_ is of the form

\(\wedge_{k\in V_i^K}L_k\wedge\wedge_{j\in V_i^J}\neg L_j,\)

for some \(V_i^J,V_i^K\subseteq\{1,2,3\}\) and \(V_i^J\cap V_i^K=\emptyset\).

Let us consider for each fixed \(c'\in C'\) the following possibly empty orthant in R<sup>3</sup>.

\(\mathcal{S}(V_i,c'):=\{x\in\mathbb{R}^3:\wedge_{k\in V_i^K}x[k]\le c'[k]\wedge\wedge_{j\in V_i^J}x[j]\ge c'[j]+1\}.\)

By construction, it is immediate that for a fixed \(c'\) and \((a',b')\in A'\times B'\) that \((a',b',c')\) fulfill the co-clause _V<sub>i</sub>_ if and only if \(a'+b'\in\mathcal{S}(V_i,c')\). Thus, equivalently to (2), we ask

\(Q_1a'\in A'\forall b'\in B'\exists c'\in C':\vee_{i=1}^h(a'+b'\in S(V_i,c')).\)

Having a closer look, \(\vee_{i=1}^h(a'+b'\in S(V_i,c'))\) is true if and only if \(a'+b'\) lies in one of the orthants \(S(V_i,c')\).

We argue that we may represent the orthant \(\mathcal{S}(V_i,c')\) as an appropriately chosen cube in R<sup>3</sup>. To this end, let \(M:=2\cdot max\{\|a\|_1+\|b\|_1+\|c\|_1:a'\in A',b'\in B',c'\in C'\}\) be a sufficiently large number. We can interpret \(\mathcal{S}(V_i,c')\) as a cube of the type \(\mathcal{C}_{i,c^\prime}=[m_0,m'_0]\times[m_1,m'_1]\times[m_2,m'_2]\), where for \(u\in\{0,1,2\}\), we define:

\(m_u:=\left\{\begin{array}{ c c } -M & u\unknown\in V_i^K,u\unknown\in V_i^J, \\ -2M+c[u] & u\in V_i^K, \\ c[u]+1 & u\in V_i^J, \end{array}\right.m'_u:=\left\{\begin{array}{ c c } M & u\unknown\in V_i^K,u\unknown\in V_i^J, \\ c[u] & u\in V_i^K, \\ 2M+c[u]+1 & u\in V_i^J. \end{array}\right.\)

The cubes are axis-aligned and have side length 2_M_. Due to the large size of the cube we get for fixed \(c'\in C'\) that \(a'+b'\in\mathcal{S}(V_i,c')\) if and only if \(a'+b'\) lies inside the cube \(\mathcal{C}_{i,c^\prime}\).

By Lemma 27, we can decompose the collection of cubes \(\mathcal{C}_{i,c^\prime}\) for \(i\in\{1,\dots,H\},c'\in C'\) into _l=O(n_) disjoint boxes R:={_R_<sub>1</sub>_,...,R<sub>l</sub>_} in time _O(n_log<sup>2</sup>_n_). Let us now go through a case distinction based on the first quantifier.

If \(Q_1=\forall\), equivalent to \(\phi\) we ask

\(\forall a'\in A'\forall b'\in B'\exists i\in\{1,\dots,l\}:a'+b'\) lies in _R<sub>i</sub>_.

By replacing each \(i\in\{1,\dots,l\}\) by a 6-tuple denoting the dimensions of the box _R<sub>i</sub>_, we can reduce counting the number of \((a',b',R_i)\) with \(a'+b'\in R_i\) to 3-SUM using Corollary 3. Due to the disjointness of the boxes _R<sub>i</sub>_, we know that no \((a',b')\) can be in different boxes \(R_i,R_{i^\prime}\) with \(i\neq i'\). Thus, we can decide our original question by checking whether the number of such witnesses equals \(|A'|\cdot|B'|\), concluding the fine-grained reduction to 3-SUM.

Assume now that \(Q_1=\exists\). Thus, equivalently to \(\phi\), we ask.

\(\exists a'\in A'\forall b'\in B'\exists i\in\{1,\dots,l\}:a'+b'\) lies in _R<sub>i</sub>_.

