**Lemma 6.3** (Min Product)**.** _Min Product cannot be solved in time_ \(O(n^{2.5-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the APSP Hypothesis fails._

**Proof.** Suppose that Min Product can be solved in time \(O(n^{2.5-\epsilon})\) for some \(\epsilon>0\); we show that in this case \(\mathrm{MinPlus}(n,\sqrt{n},n|D\le\sqrt{n})=O(n^{2.5-\epsilon})\) which contradicts the APSP Hypothesis by Corollary 5.10.

Let _A,B_ denote the two given matrices of sizes \(n\times\sqrt{n}\) and \(\sqrt{n}\times n\) (assuming that _n_ is a square number at the cost of doubling _n_ in the worst case), and let \(X\subseteq\mathbb{Z}\) be the set of entries appearing in _A_ and _B_; we assume that \(|X|\le\sqrt{n}\). Our goal is to compute the min-plus product _A∗B_. Construct the matrices \(n\times n\) matrices \(A',B'\) as follows, where we index the inner dimension by pairs \([\sqrt{n}]\times X\):

\(A'[i,(k,x)]=A[i,k]+x,\)<br>
\(B'[(k,x),j]=\left\{\begin{array}{ c c }
1 & \text{if}B[k,j]=x, \\
0 & \text{otherwise.}
\end{array}\right.\)

Note that the min product \(C'\) of \(A'\) and \(B'\) satisfies that

\(C'[i,j]=\mathrm{min}_{(k,x)\in[\sqrt{n}]\times XB^\prime[(k,x),j]=1}A'[i,(k,x)]=\mathrm{min}_{(k,x)\in[\sqrt{n}]\times XB[k,j]=x}(A[i,k]+x)=\mathrm{min}_{k\in[\sqrt{n}]}(A[i,k]+B[k,j]),\)

and thus \(C'=A*B\) is the desired min-plus product. The matrices \(A'\) and \(B'\) can be constructed in time \(\tilde{O}(n^2)\), so the total time is dominated by the Min Product computation in time \(O(n^{2.5-\epsilon})\) as claimed.

## 6.3 Min-Max Product

Next, we consider the Min-Max Product problem which was studied in the context of All-Pairs Bottleneck Paths and All-Pairs Nondecreasing Paths. We show that Duan and Pettie’s \(\tilde{O}(n^{(3+\omega)/2})\)-time algorithm \[49\] is best-possible (if \(\omega=2\)), conditioned on the APSP Hypothesis.

**Definition 6.4** (Min-Max Product)**.** _The_ min-max product _of two matrices_ \(A,B\in\mathbb{Z}^{n\times n}\) _is the matrix_ \(C\in\mathbb{Z}^{n\times n}\) _defined by_

\(C[i,j]=\mathrm{min}_{k\in[n]}\mathrm{max}\{A[i,k],B[k,j]\}.\)

_The_ Min-Max Product _problem is to compute the min-max product of two given matrices A,B._

**Lemma 6.5** (Min-Max Product)**.** _Min-Max Product cannot be solved in time_ \(O(n^{2.5-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the APSP Hypothesis fails._

**Proof.** The proof is almost immediate by Lemma 6.3: The min product of two matrices _A_ and _B_ can be expressed as the min-max product of the matrices _A_ and \(B'\), where \(B'\) is obtained from _B_ by replacing 1 with \(-\infty\) and 0 by \(\infty\).

This lower bound entails various other lower bounds. By the known equivalence \[95\] we conclude our lower bound for All-Pairs Bottleneck Paths (Theorem 1.15). Moreover, from known reductions \[96\] it follows that also the Min-\(\le\) Product and the All-Pairs Nondecreasing Paths problems cannot be solved in time \(O(n^{2.5-\epsilon})\) unless the APSP Hypothesis fails, matching their respective upper bounds if \(\omega=2\) \[96, 47, 48\]. Lemma 6.5 also implies a matching lower bound for the All-Edges Monochromatic Equality Triangle problem studied in \[98\].

## 6.4 Min-Equality Product

Min-Equality Product is yet another matrix problem with intermediate complexity \(\tilde{O}(n^{(3+\omega)/2})\), first introduced by Vassilevska W. and Xu in \[98\]. An interesting aspect of the problem is that it naturally generalizes the Equality Product problem which is one of the few intermediate problems for which we currently cannot prove conditional lower bounds.

