**Proof.** Let us assume that we are given a low-rank decomposition of _C_; the statements for _A_ and _B_ follow by first rotating the given instance. By Lemma 3.6 we may further assume that the given rank-_r_ decomposition of _C_ is _R_-row-regular for some _R=O_(log(_n_<sub>1</sub>_n_<sub>3</sub>)). Formally, we apply the lemma to partition _C_ into \(C_\mathrm{row}\sqcup C_\mathrm{col}\sqcup C_\mathrm{sm}\), where _C_<sub>row</sub> has an _R_-row-regular rank-_r_ decomposition, _C_<sub>col</sub> has an _R_-column-regular rank-_r_ decomposition, and _C_<sub>sm</sub> has a rank-_r/_2 decomposition. It then remains to solve the Exact Triangle instances (_A,B,C_<sub>row</sub>), (_A,B,C_<sub>col</sub>) and (_A,B,C_<sub>sm</sub>). We will describe how to solve (_A,B,C_<sub>row</sub>) in the following. The instance (_A,B,C_<sub>col</sub>) can be equivalently viewed as \((B^T,A^T,C_\mathrm{col}^T)\); in this case, too, we have access to a _R_-row-regular rank-_r_ decomposition of \(C_\mathrm{col}^T\), so we can solve the instance also as described in the following. Finally, we solve (_A,B,C_<sub>sm</sub>) recursively--since the rank _r_ halves with every recursive call this only leads to a logarithmic overhead.

Let (_U,V,S_) denote the _R_-row-regular rank-_r_ decomposition of _C_. Let \(\mathcal{T}\leftarrow\emptyset\) be a set of exceptional triples, and let \(\mathcal{I}\leftarrow\emptyset\) be a set of _r_-slice-uniform potential adjustments of (_A,B,C_). Consider the following algorithm. In an outer loop, we enumerate \(\ell\leftarrow 1,\dots,r\). We maintain the invariant that after the \(\ell\)-th iteration each exact triangle (_i,k,j_) with \(S[i,j]=\ell\) has been inserted into T or is present in one of the instances in I.

1. _(Heavy/Light Setup)_ Define the matrices \(A_\ell\) and \(B_\ell\) of sizes \(n_1\times n_2\) and \(n_2\times n_3\), respectively, by<tbc>

\(A_\ell[i,k]=A[i,k]-U[i,\ell],\)<br>
\(B_\ell[k,j]=-(B[k,j]-V[\ell,j]).\)

Note that for all pairs (_i,j_) with \(S[i,j]=\ell\) the conditions \(A[i,k]+B[k,j]=C[i,j]\) and \(A_\ell[i,k]=B_\ell[k,j]\) are equivalent. We now classify the non-\(\perp\) entries (_i,k_) in \(A_\ell\) as follows: We say that (_i,k_) is _light_ if<tbc>

\(|\{i'\in[n_1]:A_\ell[i,k]=A_\ell[i',k]\}|\le\frac{n_1}{rt},\)

and _heavy_ otherwise. In the following two steps we separately deal with the exact triangles (_i,k,j_) involving light and heavy edges (_i,k_), respectively.

_Running Time: O_((_n_<sub>1</sub>_n_<sub>2</sub>+_n_<sub>2</sub>_n_<sub>3</sub>+_n_<sub>1</sub>_n_<sub>3</sub>)_r_) over all iterations.

2. _(Light Edges)_ We enumerate all triples (_i,k,j_) with \(A_\ell[i,k]=B_\ell[k,j]\) for which (_i,k_) is light as follows. Enumerate all pairs \((k,j)\in[n_2]\times[n_3]\). Only if there is a light edge \((i',k)\) do we enumerate the at most _n_<sub>1</sub>/(_rt_) rows _i_ with \(A_\ell[i,k]=B_\ell[k,j]\). We insert each triple (_i,k,j_) with _A_\[_i,k_\]+_B_\[_k,j_\]=_C_\[_i,j_\] into the set T . This correctly maintains the invariant for all exact triangles involving light edges.

_Running Time: O_(_n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>/(_rt_)) per iteration, and thus _O_(_n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>_/t_) across all iterations.

3. _(Heavy Edges)_ We distinguish two cases depending on the number of heavy edges:

3.1. _(Few Heavy Edges)_ If there are at most _n_<sub>1</sub>_n_<sub>2</sub>_/t_ heavy edges, then we apply brute-force as follows. Enumerate all heavy pairs (_i,k_), and enumerate all columns _j_ with \(S[i,j]=\ell\). Each triple (_i,k,j_) enumerated in this way that satisfies _A_\[_i,k_\]+_B_\[_k,j_\]=_C_\[_i,j_\] is inserted into T . This again clearly maintains the invariant for all exact triangles involving a heavy edge.

_Running Time:_ For each row _i_ there are at most \(R\cdot(n_3/r)\) columns _j_ with \(S[i,j]=\ell\) as the given rank decomposition is assumed to be _R_-row-regular. Hence the running time is \(O(n_1n_2/t\cdot R\cdot(n_3/r))=\tilde{O}(n_1n_2n_3/(rt))\) per iteration, and thus \(\tilde{O}(n_1n_2n_3/t)\) across all iterations.

