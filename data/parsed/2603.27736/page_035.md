**Lemma 5.2** (Listing-to-Decision Reduction for Exact Triangle)**.** _Let_ (_A,B,C_) _be an Exact Triangle instance, and assume that there is an algorithm solving_ \((A',B',C')\) _for any restrictions_ \(A'\) _of A,_ \(B'\) _of B, and_ \(C'\) _of C in time T. Then, for any parameter_ \(t\ge 1\)_, we can compute lists of up to t witnesses for all outputs A_\[_i,k_\]_,B_\[_k,j_\]_,C_\[_i,j_\] _in randomized time_ \(\widetilde{O}(Tt)\).

## 5.2 Small-Universe Reduction

We start with the reduction from small universes {0_,...,n_} to even smaller universes \(\{0,\dots,n^\alpha\}\) (for any constant \(\alpha\le 1\)). The proof of this universe reduction can be split into two parts: dealing with the _unpopular_ and _popular_ outputs. The first part is as in \[35\] without modifications. The innovation is to solve the second part with "low-rank APSP" instead of "Fredman’s trick meets dominance product".

**Lemma 5.3** (Small-Universe Reduction)**.** _For all parameters_ \(n_1,n_2,n'_2,n_3,u,t\) _with_ \(n'_2\le n_2\)_, it holds that_<tbc>

\(\mathrm{MinPlus}(n_1,n_2,n_3|u)=\tilde{O}\big(\mathrm{MinPlus}(n_1,n'_2,n_3|u\le n'_2)\cdot\frac{n_2t}{n'_2}+\mathrm{ExactTri}(n_1,n_2,n_3|r\le u/t)\big).\)

<tbc>**Proof.** Let _A,B_ be the two given matrices. The first step is to apply a scaling trick to obtain an additive approximation \(\tilde{C}\) of the output matrix _A∗B_. To this end, let \(A'\) be the matrix obtained from _A_ by dropping the least significant bits of all entries (i.e., \(A'[i,j]=\lfloor A[i,j]/2\rfloor\)), and similarly obtain \(B'\) from _B_. We _recursively_ compute the min-plus product \(C'=A'*B'\) and pick \(\tilde{C}=2C'\). It is easy to verify that for all pairs (_i,j_):

\(\tilde{C}[i,j]\le(A*B)[i,j]\le\tilde{C}[i,j]+2.\)

Let \(p=\lceil n'_2\rceil\) and \(q=\lceil u/n'_2\rceil\). Without loss of generality, we can assume that _A_\[_i,k_\]mod_q\<q/_2 and _B_\[_k,j_\]mod_q\<q/_2 by the following simple trick. Partition _A_ into two submatrices, one containing the entries with _A_\[_i,k_\]mod_q\<q/_2 and the other containing all remaining entries. Subtract \(\lceil q/2\rceil\) from all entries of the second matrix; then both submatrices are as claimed. Similarly partition _B_ into two parts. It remains to compute four min-plus products from which we can easily recover the original product _A∗B_ (by appropriately adding 0, \(\lceil q/2\rceil\), or \(2\lceil q/2\rceil\) to the respective output matrices).

Now view the matrices _A_ and _B_ in their "base-(_p,q_)" representation, i.e., we rewrite the matrices as

\(A=A_1\cdot q+A_0,\)<br>
\(B=B_1\cdot q+B_0,\)

where _A_<sub>0</sub>_,B_<sub>0</sub> have nonnegative entries less than _q/_2 and where _A_<sub>1</sub>_,B_<sub>1</sub> have nonnegative entries less than _p_. We call _k_ a _witness_ of (_i,j_) if _A_\[_i,k_\]+_B_\[_k,j_\]=(_A∗B_)\[_i,j_\], and we call _k_ a _pseudo-witness_ of (_i,j_) if _A_<sub>1</sub>\[_i,k_\]+_B_<sub>1</sub>\[_k,j_\]=(_A_<sub>1</sub>∗_B_<sub>1</sub>)\[_i,j_\]. Importantly, note that each witness is also a pseudo-witness (as we have that \(\lfloor(A[i,k]+B[i,k])/q\rfloor=\lfloor A[i,k]/q\rfloor+\lfloor B[i,k]/q\rfloor\), using that _A_<sub>0</sub>_,B_<sub>0</sub> have entries less than _q/_2).

We call (_i,j_) _popular_ if it has at least \(tn_2/n'_2\) pseudo-witnesses, and _unpopular_ otherwise. In the following two cases we separately deal with the unpopular and popular pairs (_i,j_). Initially, let _C_ be the all-\(\perp\) matrix.

1. _(Unpopular Pairs)_ To deal with the unpopular pairs (_i,j_), we will list _all_ pseudo-witnesses _k_ of (_i,j_). To this end, repeat the following steps \(O(tn_2/n'_2\cdot\mathrm{log}(n_1n_3))\) times:<tbc>

1.1. Sample a uniformly random subset \(\mathcal{K}\subseteq[n_2]\) with rate \(\rho=n'_2/(2tn_2)\). The resulting set has size \(|\mathcal{K}|\le O(n'_2/t)\le O(n'_2)\) with high probability.<tbc>

1.2. Restrict _A_<sub>1</sub> to the columns in K, restrict _B_<sub>1</sub> to the rows in K, and compute the min-plus product of the resulting matrices. Additionally, report a witness _k_ for each output pair (_i,j_) by Lemma 5.1. (Note that a witness for _A_<sub>1</sub>∗_B_<sub>1</sub> is a pseudo-witness in our language.) We update \(C[i,j]\leftarrow\mathrm{min}\{C[i,j],A[i,k]+B[k,j]\}\) for each triple (_i,k,j_) reported in this way.<tbc>

