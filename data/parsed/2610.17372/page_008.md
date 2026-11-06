<tbc>in the forward process, and similarly, _P<sup>B</sup>(i,j_) ¡_P<sup>B</sup>(k,l_) if _P<sup>B</sup>(i,j_) is calculated before _P<sup>B</sup>(k,l_) in the backward process.

A vertex in a path is said to be a minimum vertex if it is less than its predecessor and successor vertices in the path. A sequence of vertices \(p_1,p_2,\cdots,p_k\) in a path is said to form i) an upward sequence if \(p_1<p_2<\cdots<p_k\), ii) a downward sequence if \(p_1>p_2>\cdots>p_k\), and iii) a valley sequence if there is only one minimum vertex in the sequence and \(min(p_1,p_k)>max_j(p_j),j=2,3,\cdots,k-1\).

We now have the following lemma.

**Lemma 1.** _If the vertices which are in a shortest time path_ \(p_1p_2\cdots p_k\) _from a vertex p_<sub>1</sub> _to a vertex p<sub>k</sub> form an upward sequence or a downward sequence, then this shortest time path from p_<sub>1</sub> _to p<sub>k</sub> will be computed in the forward process of Algorithm 1._

_Proof._ If the vertices in order as in the path form an upward sequence, then \(p_1<p_2<\cdots<p_k\). Hence, in the forward process, _P<sup>F</sup>(p_<sub>1</sub>_,p_<sub>2</sub>) is computed first with the direct edge from _p_<sub>1</sub> to _p_<sub>2</sub> in the initialization phase itself. Then _P<sup>F</sup>(p_<sub>1</sub>_,p_<sub>3</sub>) is computed with the value of _P<sup>F</sup>(p_<sub>1</sub>_,p_<sub>2</sub>) and the direct edge from _p_<sub>2</sub> to _p_<sub>3</sub> by the operation \(P^F(p_1,p_2)\otimes P(p_2,p_3)\). Next, _P<sup>F</sup>(p_<sub>1</sub>_,p_<sub>4</sub>) will assume the final value from the operation \(P^F(p_1,p_3)\otimes P(p_3,p_4)\), and so on to get the order of computation as \(P^F(p_1,p_2)<P^F(p_1,p_3)<P^F(p_1,p_4)<\cdots<P^F(p_1,p_k)\) during the forward process itself. This fact is pictorially represented in Fig. 3(a) where the labels on dotted lines show the steps of computation and the solid lines show the availability of connecting edges during the time window under consideration.

Similarly, if the vertices in the shortest time path \(p_1p_2\cdots p_k\) form a downward sequence, then \(p_1>p_2>\cdots>p_k\). Thus, _P<sup>F</sup>(p_<sub>_k_-1</sub>_,p<sub>k</sub>_) is computed first with the direct edge from _p_<sub>_k_-1</sub> to _p<sub>k</sub>_, then _P<sup>F</sup>(p_<sub>_k_-2</sub>_,p<sub>k</sub>_) is computed using this value of _P<sup>F</sup>(p_<sub>_k_-1</sub>_,p<sub>k</sub>_) by the operation \(P^F(p_{k-1},p_k)\otimes P(p_{k-2},p_{k-1})\), and so on to get the order of computation as \(P^F(p_{k-1},p_k)<P^F(p_{k-2},p_k)<\cdots<P^F(p_2,p_k)<P^F(p_1,p_k)\) in the forward process itself. Fig. 3(b) pictorially represents this order of computation in the forward process corresponding to the upward sequence \(p_1>p_2>\cdots>p_k\) of vertices in the path.

**Lemma 2.** _If the vertices in a shortest time path_ \(p_1p_2\cdots p_k\) _from a vertex p_<sub>1</sub> _to a vertex p<sub>k</sub> form a valley sequence, then this shortest time path will be computed in the forward process of Algorithm 1._<tbc>

<tbc>_Proof._ Let _p<sub>j</sub>_ be the minimum of all vertices \(p_1,p_2,\cdots,p_k\) in the valley sequence. Then the sequence from _p_<sub>1</sub> to _p<sub>j</sub>_ will be a downward sequence and that from _p<sub>j</sub>_ to _p<sub>k</sub>_ will be an upward sequence. By Lemma 1, _P<sup>F</sup>(p_<sub>1</sub>_,p<sub>j</sub>_) will be computed in the forward process. Further, we note that during the forward process, \(P^F(p_1,p_j)<P^F(p_1,p_{j+1})<\cdots<P^F(p_1,p_k)\). Hence the proof.

For an arbitrary sequence of vertices in a shortest time path \(p_1p_2\cdots p_k\) from a vertex _p_<sub>1</sub> to a vertex _p<sub>k</sub>_, if there are multiple valley sequences within the sequence \(p_1,p_2,\cdots,p_k\), then each such valley sequence, say \(p_s,p_{s+1},\cdots,p_t\), the shortest time path from _p<sub>s</sub>_ to _p<sub>t</sub>_ will be computed in the forward process by virtue of Lemma 2. Let us delete all vertices in between _p<sub>s</sub>_ and _p<sub>t</sub>_ (keeping only _p<sub>s</sub>_ and _p<sub>t</sub>_) in the sequence and repeat this step for each such valley sequence in succession. If a new valley sequence is formed after this deletion process, then also the process is repeated to delete all intermediate vertices within such a valley sequence. Note that in every instance of such a valley sequence, the portion of the shortest time path \(p_1p_2\cdots p_k\) formed with the vertices of the valley sequence will be computed by virtue of Lemma 2. After such deletion process, eventually we will be left out with either i) an upward sequence, or ii) a downward sequence or ii) an upward sequence followed by a downward sequence. If the resulting reduced sequence is an upward or a downward sequence, the shortest time path with these vertices in the reduced sequence will be computed by virtue of Lemma 1. We now have the following lemma.

**Lemma 3.** _If the vertices in a shortest time path_ \(p_1p_2\cdots p_k\) _from p_<sub>1</sub> _to p<sub>k</sub> form an upward sequence followed by a downward sequence, then this shortest time path will be computed by the backward process of Algorithm 1._

_Proof._ Assume that the vertex _p<sub>j</sub>_ is maximum of all vertices \(p_1,p_2,\cdots,p_k\) in the path. Hence, \(p_1<p_2<\cdots<p_j\). From the order of execution of loops in the backward process, we get, \(P^B(p_{j-1},p_j)<P^B(p_{j-2},p_j)<P^B(p_{j-3},p_j)<\cdots<P^B(p_1,p_j)\). Thus the upward section of the shortest time path is computed in the backward process. Likewise, since \(p_j>p_{j+1}>\cdots>p_k\), we get, \(P^B(p_j,p_{j+1})<P^B(p_j,p_{j+2})<\cdots<P^B(p_j,p_k)\), i.e., the downward section of the shortest time path is also computed in the backward process. We further note that the computation order in the backward process leads us to the following result: \(P^B(p_1,p_j)<P^B(p_1,p_{j+1})<P^B(p_1,p_{j+2})<\cdots<P^B(p_1,p_k)\). Hence the proof.

All these discussions lead to the following result :

**Theorem 1.** _Algorithm 1 correctly computes the all-pairs shortest time paths in a temporal graph._

## 5.2 Time Complexity

Procedure _find\_next\_run_ needs at most _O(M_) steps of comparisons. However, the two _while_-loops in _initialize\_path\_matrix_ together with the procedure _find\_next\_run_ can take only _O(M_) time as the contacts from a vertex _p_ to a vertex _q_ are determined in ascending order of the intervals 0 through _M_-1. Hence, the amortized time required by the procedure _initialize\_path\_matrix_<tbc>

3
2
1
P1
P2
P3
P4
Pk
(a) Upward sequence
P1
P2
Pk-3
Pk-2
Pk-1
Pk
1
2
3
(b) Downward sequence

Fig. 3. Computation order of the elements of path matrix

