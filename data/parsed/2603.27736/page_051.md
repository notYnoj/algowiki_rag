\(\text{\textit{Running Time:}}O(|R|\cdot\sqrt{n}\cdot\rho n\cdot\rho n)=O(KD^2/L\cdot\sqrt{n}\cdot n/D\cdot n/D)=O(n^{2.5}K/L)\text{, recalling that each integer appears in at most a}\rho\le 1/D\text{-fraction of all rows and columns in}A\text{and}B\text{.}O(|R|\cdot\sqrt{n}\cdot\rho n\cdot\rho n)=O(KD^2/L\cdot\sqrt{n}\cdot n/D\cdot n/D)=O(n^{2.5}K/L)\)

The correctness is clear from before. The total running time is \(O((K^5+L^{2.5})n^{2.5-\epsilon}+n^{2.5}K/L)\). Recall that \(K\le n^{\epsilon/6}\) and choose the parameter \(L=n^{\epsilon/3}\). The total time becomes \(O(n^{2.5-\epsilon/6})\) as claimed.

To conclude Theorem 1.16 from Lemma 6.10 we additionally need to argue that _A_ is row-monotone, and that _B_ is column-bounded-difference and column-monotone. It turns out that these three extra constraints are without loss of generality, based on a sequence of observations mostly from previous work; see \[61\] and \[44, Section 2\].

**Lemma 6.11** (\[61, 44\])**.** _The computation of an_ \(n\times n\times n\) _min-plus product A∗B where A is row-bounded- difference can be reduced in time O(n_<sup>2</sup>) _to the computation of an_ \(n\times n\times n\) _min-plus product_ \(A'*B'\) _where_ \(A'\) _is row-bounded-difference and row-monotone and_ \(B'\) _is column-bounded-difference and column-monotone._

**Proof.** Let _A,B_ be the given matrices, where _A_ is row-bounded-difference, i.e., \(|A[i,k]-A[i,k+1]|\le c\) for some constant _c_. The reduction is to apply the following four simple transformations step-by-step.

• _(Make A Small-Universe)_ When _A_ is row-bounded-difference, by definition each row in _A_ only takes integer values in some interval {_a,...,a+O(n_)}. By subtracting _a_ from the entire row we can make sure that _A_ only takes values in {0_,...,u=O(n_)}. We can recover the original min-plus product _A∗B_ from this transformation by adding back the respective offset _a_ to each row.<tbc>

• _(Make B Small-Universe)_ Next, we also restrict the range of entries in _B_. Focus on any column in _B_, and let _b_ denote its minimum entry. All entries larger than _b_+2_u_ and all \(\perp\) entries cannot matter in the min-plus product _A∗B_, so we simply replace these entries by _b_+2_u_. Afterwards we can remove _b_ from the entire column; the resulting matrix has integer entries in {0_,...,_2_u=O(n_)}. We can recover the original min-plus product _A∗B_ from this transformation by adding back the respective offset _b_ to each column.<tbc>

• _(Make B Column-Bounded-Difference)_ Next, to ensure that _B_ is column-bounded-difference we replace each entry _B_\[_k,j_\] by \(B'[k,j]=min_{k^\prime}(B[k',j]+|k'-k|\cdot c)\). We first claim that this transformation leaves the min-plus product unchanged, i.e., \(A*B=A*B'\). The "\(\ge\)" direction is clear, so focus on the "\(\le\)" direction. Suppose that \((A*B')[i,j]=A[i,k]+B'[k,j]\) and that \(B'[k,j]=B[k',j]+|k'-k|\cdot c\). As _A_ is row-bounded-difference (with constant _c_), it follows that indeed

\((A*B)[i,j]\le A[i,k']+B[k',j]\)<br>
\(\le A[i,k]+|k-k'|\cdot c+B[k',j]\)<br>
\(=A[i,k]+B'[k,j]\)<br>
\(=(A*B')[i,j].\)

Moreover, the augmented matrix \(B'\) is indeed column-bounded-difference as \(|B'[k,j]-B'[k+1,j]|\le c\), and still consists of integer entries in the range {0_,...,O(n_)}.

Finally, we remark that \(B'\) can be computed in quadratic time from _B_. We will separately compute \(B_L[k,j]=min_{k^\prime\le k}(B[k',j]+(k-k')\cdot c)\) and \(B_R[k,j]=min_{k^\prime\ge k}(B[k',j]+(k'-k)\cdot c)\), and then take their entry-wise minimum. But each column in _B<sub>L</sub>_ can be computed in linear time by a dynamic program evaluating \(B_L[k,j]=min\{B'[k,j],B_L[k-1,j]+c\}\), and similarly for _B<sub>R</sub>_.

In the following we will continue to write _B_ for the augmented matrix \(B'\).

• _(Make A Row-Monotone and B Column-Monotone)_ We finally turn _A_ into a row-monotone matrix and _B_ into a column-monotone matrix based on the following observation due to \[61\]. Replace each entry _A_\[_i,k_\] by _A_\[_i,k_\]+_kc_, and each entry _B_\[_k,j_\] by _B_\[_k,j_\]+(_n-k)c_. The resulting matrices<tbc>

