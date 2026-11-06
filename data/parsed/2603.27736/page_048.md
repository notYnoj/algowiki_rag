**Definition 6.6** (Min-Equality Product)**.** _The_ min-equality product _of two matrices_ \(A,B\in\mathbb{Z}^{n\times n}\) _is the matrix_ \(C\in\mathbb{Z}^{n\times n}\) _defined by_

\(C[i,j]=min\{A[i,k]:k\in[n],A[i,k]=B[k,j]\}.\)

_The_ Min-Equality Product _problem is to compute the min-equality product of two given matrices A,B._

**Lemma 6.7** (Min-Equality Product)**.** _Min-Equality Product cannot be solved in time_ \(O(n^{2.5-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the APSP Hypothesis fails._

**Proof.** Suppose that Min-Equality Product is in time \(O(n^{2.5-\epsilon})\) for some \(\epsilon>0\). We show that in this case \(MinPlus(n,\sqrt{n},n|D\le\sqrt{n};K\le n^{\epsilon/4})=O(n^{2.5-\epsilon/2})\) which contradicts the APSP Hypothesis by Corollary 5.9 (applied with parameters \(\epsilon'=\epsilon/2,\kappa=\epsilon/4\) and \(\alpha_1=1,\alpha_2=1/2,\alpha_3=1\)).

Let _n_ be a square number, let _A,B_ be the given matrices of sizes \(n\times\sqrt{n}\) and \(\sqrt{n}\times n\), respectively, and let \(X\subseteq\mathbb{Z}\) denote the set of entries that appear in _A_ and _B_. We assume that \(|X|\le\sqrt{n}\) and \(|X+X|\le K|X|\) for some \(K\le n^{\epsilon/4}\). First compute _Z=X-X_ (e.g., by brute-force), and recall that by the Plünnecke-Ruzsa inequality (Lemma 2.16) we have \(|X-X|\le K^2|X|\le n^{1/2+\epsilon/2}\).

Construct the augmented matrices \(A',B'\) indexed by \([n]\times([\sqrt{n}]\times Z)\) and \(([\sqrt{n}]\times Z)\times[n]\), respectively, defined by

\(A'[i,(k,z)]=2A[i,k]-z,\)<br>
\(B'[(k,z),j]=2B[k,j]+z.\)

We compute their min-equality product _C_ and claim that _C=A∗B_ is exactly the desired min-plus product. On the one hand, we have that \(A'[i,(k,z)]=B'[(k,z),j]\) if and only if _z=A_\[_i,k_\]-_B_\[_k,j_\]. In this case we have \(A'[i,(k,z)]=2A[i,k]-z=A[i,k]+B[k,j]\), and thus \(C\ge A*B\). On the other hand, focus on any witness (_A∗B_)\[_i,j_\]=_A_\[_i,k_\]+_B_\[_k,j_\]. Then clearly \(z=A[i,k]-B[k,j]\in X-X=Z\), and thus by construction \(C[i,j]\le A[i,k]+B[k,j]\), and therefore \(C\le A*B\). The claim follows.

Finally, consider the running time. The matrices \(A',B'\) have size \(n\times n^{1+\epsilon/2}\) and \(n^{1+\epsilon/2}\times n\), respectively. We can partition the inner dimension into \(O(n^{\epsilon/2})\) blocks of size _n_ and thereby compute the rectangular min-equality product of \(A'\) and \(B'\) by \(n^{\epsilon/2}\) square computations, each running in time \(O(n^{2.5-\epsilon})\). The total time is \(O(n^{2.5-\epsilon/2})\) as claimed.

## 6.5 Bounded-Difference and Monotone Min-Plus Product

Next, we consider the restriction of the Min-Plus Product problem to _bounded-difference_ or, more generally, _monotone_ matrices defined as follows.

**Definition 6.8** (Bounded Difference)**.** _A matrix_ \(A\in\mathbb{Z}^{n\times n}\) _is_ row-bounded-difference _if_ \(|A[i,j]-A[i,j+1]|\le O(1)\) _for all i,j. Similarly, A is_ column-bounded-difference _if_ \(|A[i,j]-A[i+1,j]|\le O(1)\) _for all i,j. A is_ bounded-difference _if it is both row- and column-bounded-difference._

**Definition 6.9** (Monotone)**.** _A matrix_ \(A\in\mathbb{Z}^{n\times n}\) _is_ row-monotone _if_ \(0\le A[i,1]\le\cdots\le A[i,n]\le O(n)\) _for all rows i. Similarly, A is_ column-monotone _if_ \(0\le A[n,j]\le\cdots\le A[1,j]\le O(n)\) _for all columns j. A is_ monotone _if it is both row- and column-monotone._

Bringmann, Grandoni, Saha, and Vassilevska W. \[25\] designed the first subcubic-time algorithm for bounded-difference Min-Plus Product, which they used to derive subcubic-time algorithms for various string problems like language edit distance and RNA-folding. Mao \[78\] later similarly applied their algorithm to unweighted tree edit distance. Motivated by these applications, a line of research \[99, 61, 43, 44\] sought to optimize the running time of bounded-difference and monotone Min-Plus Product. This line culminated only recently in an \(\tilde{O}(n^{(3+\omega)/2})\)-time algorithm due to Chi, Duan, Xie, and Zhang \[44\]. Specifically, they design two different algorithms--one to compute the min-plus product of a _row-monotone_ matrix _A_ and an unconstrained matrix _B_, and another one for a _column-monotone_ matrix _A_ and an unconstrained matrix _B_.

