**Definition 2.5** (kMin-IP_<sub>n,d</sub>_)**.** _Given k sets of vectors_<tbc>

\(X_1=\{x_{11},\dots,x_{1n}\},\dots,X_k=\{x_{k1},\dots,x_{kn}\}\)

<tbc>_such that_ \(x_{ij}\in\{-W,\dots,W,\infty\}^d\) _for all i,j and a natural number_ \(r\in\mathbb{Z}\), kMin-IP_<sub>n,d</sub> asks to determine whether there exists_ \(1\le i_1,\dots,i_k\le n\) _such that_

\(\langle x_{1,i_1},x_{2,i_2},\dots,x_{k,i_k}\rangle\le r.\)

Just from the definitions, kOV trivially reduces to kMin-IP. In addition, it is not hard to show \(\mathsf{kOV}_{n,d}\rightarrow(\mathsf{k}-1)\mathsf{OV}_{n,d}\) and \(\mathsf{kMin-IP}_{n,d}\rightarrow(\mathsf{k}-1)\mathsf{Min-IP}_{n,d}\) for all \(k\ge 3\).

**Lemma 2.6.** _Suppose there exists an algorithm for_ (k-1)OV_<sub>n,d</sub> that runs in time_ \(O(n^{k-1-\varepsilon})\) _for some_ \(\varepsilon>0\)_, then there exists an algorithm for_ kOV_<sub>n,d</sub> that runs in time_ \(O(n^{k-\delta})\) _for some_ \(\delta>0\).

_Proof._ Given an kOV_<sub>n,d</sub>_ instance with sets _X_<sub>1</sub>_,...,X<sub>k</sub>_, we trivially compute \(\langle x_{1,i_1},x_{2,i_2}\rangle\) for all \(1\le i_1,i_2\le n\) using time _O(n_<sup>2</sup>_d_). Now for each \(1\le i_1\le n\), run the algorithm for (k-1)OV_<sub>n,d</sub>_ with \(x_{1,i_1}\cdot X_2,X_3,\dots,X_k\). If there are no zeros then output no; otherwise output yes.

This algorithm is correct because we have covered all possible \(\langle x_{1,i_1},x_{2,i_2},\dots,x_{k,i_k}\rangle\). The running time is \(O(n^2d)+O(n^{k-1-\varepsilon})\cdot n=O(n^{k-1-\varepsilon})\).

**Lemma 2.7.** _Suppose there exists an algorithm for_ (k-1)Min-IP_<sub>n,d</sub> that runs in time_ \(O(n^{k-1-\varepsilon})\) _for some_ \(\varepsilon>0\)_, then there exists an algorithm for_ kMin-IP_<sub>n,d</sub> that runs in time_ \(O(n^{k-\delta})\) _for some_ \(\delta>0\).

_Proof._ The proof is exactly the same as the proof of Lemma 2.6.

## 2.3 All Pair Shortest Path

All Pair Shortest Path (APSP) is a well-known problem in fine grained complexity and graph theory.

**Definition 2.8** (APSP)**.** _Given a directed graph G with nodes V_={_v_<sub>1</sub>_,...,v<sub>n</sub>}, the_ All Pair Shortest Path (APSP) _asks to determine the distance between v<sub>i</sub> and v<sub>j</sub> for all_ \(1\le i<j\le n\).

Currently there is no algorithm for APSP that runs in \(O(n^{3-\varepsilon})\) time for any \(\varepsilon>0\), and it is conjectured that no such algorithm exists.

**Conjecture 2.9** (APSP Conjecture)**.** _There is no truly sub-cubic algorithm for_ APSP.

It is known that APSP is sub-cubic equivalent to many problems such that min-plus matrix multiplication, negative triangle etc \[WW18\]. Therefore, assuming APSP conjecture, none of these problems are truly sub-cubic. We will use the hardness of these problems to obtain our hardness results.

**Definition 2.10** ((min,+)MM)**.** _Given two_ \(n\times n\) _matrices A,B, compute its min-plus product C where_

\(C[i,j]=min_{1\le k\le n}\{A[i,k]+B[k,j]\}\)

_for all_ \(1\le i,j\le n\).

**Definition 2.11** (NegativeTriangle)**.** _Given an undirected, weighted graph, determines whether there exists a triangle such that its weight (the sum of weights of three sides) is negative._

## 2.4 Least Weight Subsequence

We formally define LWS using the definition provided in \[KPS17\].

