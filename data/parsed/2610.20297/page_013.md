The inner dimension is \(D=B^{(\ell)}p\); smaller blocks are padded with zero coordinates in both matrices. For a query \((i,j,K^{(\ell)},p)\), set _r=C_\[_i,j_\]mod_p_. As in Lemma 3.4 we have

\((XY_r)[i,j]=C(i,j,K^{(\ell)},p).\)

Apply Theorem 3.11 to preprocess each input matrix pair. There are \(O(NP/B^{(\ell)})\) products, since _t_ is constant. Constructing all input matrices takes _O(N_<sup>2</sup>_P_<sup>2</sup>) time, and their preprocessing and query costs give the claimed bounds.

We now use these data structures to search the candidate blocks in depth-first order. For each output pair (_i,j_), process all level-0 blocks in order. At each visited block \(K^{(\ell)}\), use the following algorithm.

1. Query \(C(i,j,K^{(\ell)},p)\) for each \(p\in\mathcal{P}^{(\ell)}\). If any \(C(i,j,K^{(\ell)},p)=0\), discard and proceed to the next block.<tbc>

2. If \(\ell=h\), test \(\Delta_{ikj}=0\) for all \(k\in K^{(h)}\) until a witness is found. If \(\Delta_{ikj}=0\) is found, return (_i,j_) is accurate and proceed to the next (_i,j_) output pair. If no \(\Delta_{ikj}=0\) is found, discard and proceed to the next block.<tbc>

3. If \(\ell<h\), recurse on the first child \((i,j,K^{(\ell+1)})\) and then recurse on the second child (in depth-first search order).

If the full search finishes without finding a witness \(\Delta_{ikj}=0\), return that (_i,j_) is inaccurate.

**Lemma 3.13.** _Let_ \(P=\Theta(BlogU)\)_, where the implied constant is sufficiently large, and let_ \(0\le h\le logB\)_. Suppose the parameters in Lemma 3.12 are valid for every_ \(0\le\ell\le h\)_. Then the above algorithm solves_ (min,+)_-Witness Equality deterministically in time_

\(\tilde{O}_{log^{t+1}(U)}\left(N^\omega B^{t-1}P^{t+1}+N^2P^2+\frac{N^2B}{2^h}+\frac{N^3}{2^{ht}}+\sum_{\ell=0}^h\left(\frac{N^3P}{B^{(\ell)}(B^{(\ell)}P)^{g_\ell}}+\left(N^2+\frac{N^3}{B2^{\ell(t-1)}}\right)(B^{(\ell)}P)^{q_\ell}\right)\right)\)

_Proof of Lemma 3.13._ Correctness follows from Claim 3.5 as we return that (_i,j_) is accurate only after finding an exact witness, and a search will not terminate until either an exact witness is found or all candidate blocks are explored.

To bound the number of queries, fix (_i,j_). At each level, the depth-first search visits at most one block witness. Indeed, once it enters a block containing an exact witness, it finds such a witness before returning from that block, and then stops. Over all output pairs, at most _N_<sup>2</sup> visited blocks at any level are block witnesses. The number of false candidates at level \(\ell\) is at most \(\Phi^{(\ell)}\) by Claim 3.6.

There are _O(N_<sup>3</sup>_/B_) tests at level 0. At level \(\ell\ge 1\), every tested block is a child of a visited level-\((\ell-1)\) candidate. Thus the number of queries at level \(\ell\), over the constant number _t_ of primes in \(\mathcal{P}^{(\ell)}\), is<tbc>

\(O(N^2+\Phi^{(\ell-1)})=O\left(N^2+\frac{N^3}{B2^{\ell(t-1)}}\right).\)

<tbc>The same bound holds at level 0. Multiplying by the query time in Lemma 3.12 gives the query term in the statement. The final scans at level _h_ cost<tbc>

\(O\left(N^2B^{(h)}+\Phi^{(h)}B^{(h)}\right)=O\left(\frac{N^2B}{2^h}+\frac{N^3}{2^{ht}}\right).\)

<tbc>It remains to include preprocessing and Lemma 3.7. Summing Lemma 3.12 over the _O_(log_N_) levels gives the preprocessing terms. Furthermore, we have

\(\mathsf{T}_\mathsf{MUL}\left(N,N(B^{(\ell)})^{t-1},N\right)=O\left(N^\omega(B^{(\ell)})^{t-1}\right).\)

Lemma 3.7, summed over all levels, therefore contributes \(\tilde{O}(N^\omega B^{t-1}P^{t+1}log^{t+1}U)\). Combining the bounds proves the lemma.

