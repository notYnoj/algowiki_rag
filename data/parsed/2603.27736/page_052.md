still have entries in {0_,...,O(n_)}. Each row in _A_ forms a monotonically non-decreasing sequence, recalling that before the transformation any two adjacent entries in the same row differed by at most _c_. Similarly, each column in _B_ forms a monotonically non-increasing sequence. Note that _A_ also remains row-bounded-difference (though with a larger constant, 2_c_), and similarly _B_ remains column-bounded- difference. The min-plus product _A∗B_ remains unchanged, up to adding the fixed offset _nc_ to all entries.

The proof of Theorem 1.16 is now an immediate combination of Lemma 6.10 and Lemma 6.11.

### 6.6 Min-Witness Product

Finally, we consider the Min-Witness Product problem first introduced by Czumaj, Kowaluk, and Lingas \[45\]. It takes an important role in the class of intermediate-complexity problems as it is among the _simplest_ such problems: It can be solved in time \(\tilde{O}(n^{2+\mu})\) by fast rectangular matrix multiplication, and is known to reduce to many known intermediate problems (via typically very simple reductions). On the flip-side this means that it is among the _hardest_ intermediate problems to establish tight lower bounds. To date, only non-matching lower bounds are known--an _n_<sup>11/5-_o_(1)</sup>-time lower bound based on Strong APSP, and an _n_<sup>7/3-_o_(1)</sup>-time lower bound based on Directed Unweighted APSP \[35\]. Here we give a strengthened albeit still non-matching lower bound of _n_<sup>7/3-_o_(1)</sup> based on the APSP Hypothesis.

**Definition 6.12** (Min-Witness Product)**.** _The_ min-witness product _of two matrices_ \(A,B\in\{0,1\}^{n\times n}\) _is the matrix_ \(C\in([n]\cup\{\perp\})^{n\times n}\) _defined by_

\(C[i,j]=min\{k\in[n]:A[i,k]=B[k,j]=1\}\)

_(where we understand that the minimum is_ \(\perp\) _if there is no k with A_\[_i,k_\]=_B_\[_k,j_\]=1_). The_ Min-Witness Product _problem is to compute the min-witness product of two given matrices A,B._

**Lemma 6.13** (Min-Witness Product)**.** _Min-Witness Product cannot be solved in time_ \(O(n^{7/3-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the APSP Hypothesis fails._

**Proof.** Suppose that Min-Witness Product is in time \(O(n^{7/3-\epsilon})\) for some \(\epsilon>0\). We show that in this case \(MinPlus(n,n^{1/3},n|D\le n^{1/3})=O(n^{7/3-\epsilon})\) which contradicts the APSP Hypothesis by Corollary 5.10.

Let _A,B_ be the given matrices of respective sizes \(n\times n^{1/3}\) and \(n^{1/3}\times n\) (where we assume that _n_<sup>1/3</sup> is an integer), and let \(X\subseteq\mathbb{Z}\) denote the set of entries appearing in _A_ and _B_ with size \(|X|\le n^{1/3}\). Construct the following two augmented matrices \(A',B'\) indexed by \([n]\times([n^{1/3}]\times X\times X)\) and \(([n^{1/3}]\times X\times X)\times[n]\), respectively:

\(A'[i,(k,x,y)]=\left\{\begin{array}{ c c }
1 & \text{if}A[i,k]=x, \\
0 & \text{otherwise},
\end{array}\right.\)<br>
\(B'[(k,x,y),j]=\left\{\begin{array}{ c c }
1 & \text{if}B[k,j]=y, \\
0 & \text{otherwise}.
\end{array}\right.\)

Moreover, define an arbitrary order \(\le\) on triples \([n^{1/3}]\times X\times X\) satisfying that \((k_1,x_1,y_1)\le(k_2,x_2,y_2)\) whenever \(x_1+y_1\le x_2+y_2\). Then compute the min-witness product of \(A'\) and \(B'\), where we order the inner dimension \([n^{1/3}]\times X\times X\) by that order \(\le\). By construction, in the resulting min-witness product each entry (_i,j_) is a triple (_k,x,y_) where (_A∗B_)\[_i,j_\]=_x+y_, and where _k_ is a witness of (_A∗B_)\[_i,j_\]. In particular, we can easily read off the desired min-plus product _A∗B_.

## Acknowledgements

I am very grateful to Amir Abboud and Karl Bringmann for valuable discussions, to Amir Abboud and Leo Wennmann for many helpful comments on an earlier draft of this paper, and to Ernie Croot for answering some questions related to \[11\].

