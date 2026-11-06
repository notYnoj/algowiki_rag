It has remained open if these algorithms are best-possible. In this section we show that the first algorithm is conditionally optimal (if \(\omega=2\)); it remains an interesting open question if the second algorithm is similarly optimal.

**Theorem 1.16** (Row-Bounded-Difference Row-Monotone Min-Plus Product)**.** _The min-plus product of a row-bounded-difference, row-monotone matrix_ \(A\in\mathbb{Z}^{n\times n}\) _and a column-bounded-difference, column-monotone matrix_ \(B\in\mathbb{Z}^{n\times n}\) _cannot be computed in time_ \(O(n^{2.5-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the APSP Hypothesis fails._

The conceptual idea behind Theorem 1.16 is simple. For a reduction based on the Directed Unweighted APSP Hypothesis, i.e., starting from Min-Plus Product of size \(n\times\sqrt{n}\times n\) with entries bounded by \(\sqrt{n}\), one can readjust the matrix entries \(A[i,k]\leftarrow A[i,k]+k\cdot\sqrt{n}\) and \(B[k,j]\leftarrow B[k,j]-k\cdot\sqrt{n}\), which leaves _A∗B_ unchanged, and ensures that _A_ is row-monotone and _B_ is column-monotone. This insight was independently communicated to us by Łukasiewicz \[106\]. To make _A_ row-bounded-difference one can additionally blow up the inner dimension from \(\sqrt{n}\) to _n_, by adding \(\sqrt{n}\) new columns between any pair of consecutive columns in _A_ to appropriately interpolate between the previous entries.

The major technical complication is that we aim to base the reduction on the APSP Hypothesis instead. We thus cannot assume that the entries in the given matrices are bounded by \(\sqrt{n}\), but only that there are \(\sqrt{n}\) distinct entries that form a low-doubling set (by Corollary 5.9). We show that after an appropriate transformation we can substitute numbers by their rank (i.e., position in the sorted order), and thereby still reduce to matrices with entries in the range roughly \(\{0,\dots,\sqrt{n}\}\). We give the details in the following technical lemma. In this first step we only care to make _A_ row-monotone; later we comment how to achieve the other properties without loss of generality.

**Lemma 6.10.** _The min-plus product of a row-bounded-difference_ \(A\in[\sqrt{n}]^{n\times n}\) _with a matrix_ \(B\in\{0,\perp\}^{n\times n}\) _containing at most n_<sup>1.5</sup> _non-_\(\perp\) _entries cannot be computed in time_ \(O(n^{2.5-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the APSP Hypothesis fails._

**Proof.** Assume that there is an \(O(n^{2.5-\epsilon})\)-time algorithm for the problem described in the lemma statement. We design an algorithm for the uniform regular low-doubling Min-Plus Product problem of size \(n\times\sqrt{n}\times n\), proving \(\mathrm{MinPlus}(n,\sqrt{n},n|D\le\sqrt{n};\rho\le 1/D;K\le n^{\epsilon/6})\le O(n^{2.5-\epsilon/6})\). This contradicts the APSP Hypothesis by Corollary 5.9.

Let _n_ be a square number, and let _A_ and _B_ be the given \(n\times\sqrt{n}\) and \(\sqrt{n}\times n\) matrices with integer entries in _X_. That is, we can assume that \(D=|X|\le\sqrt{n}\) and \(|X+X|\le K|X|\) where \(K\le n^{\epsilon/6}\). We compute _X+X_ (by brute-force, say). Then we sort _X_ and _X+X_. We say that \(y\in X\) is the _successor_ of \(x\in X\) if it is the next-larger element in _X_. We also define two functions

\(\text{select}:[|X+X|]\rightarrow X+X,\)<br>
\(\text{rank}:X\times X\rightarrow[|X+X|],\)

where select maps each index _i_ to the _i_-th smallest element in the sumset _X+X_, and rank(_x,y_) is exactly the index _i_ such that _x+y_ is the _i_-th smallest element in the sumset _X+X_. In particular, we have that select(rank(_x,y_))=_x+y_.

We now define another function \(f:X\times X\rightarrow[|X+X|]\). Let _L\>_0 be a parameter to be determined later. Initially, set \(f(x,y)\leftarrow\text{rank}(x,y)\). Now enumerate all pairs \((x,y)\in X^2\) in lexicographically descending order. If _y_ has a successor \(y'\) and if \(f(x,y)<f(x,y')-L\), then we update \(f(x,y)\leftarrow f(x,y')-L\). The resulting function _f_ satisfies the following three properties by construction:

(i) For each fixed \(x\in X\) the function \(f(x,\cdot)\) is increasing and _L_-bounded-difference, i.e., for any successive \(y,y'\in X\) we have that \(f(x,y')-f(x,y)\le L\).<tbc>

(ii) \(f(x,y)\ge\text{rank}(x,y)\) for all \(x,y\in X\).<tbc>

