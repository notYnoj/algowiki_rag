Our positive results for the MaxST guarantee suggest that Maximum Acyclic Subgraph above the Poljak-Turzík guarantee could also admit efficient algorithms. We re-formulate the corresponding open question, which was already posed in \[EM18\] for integral weights and for a broader class of problems.

**Open Question 3.** _Can we find an acyclic subgraph of weight at least_

\(\mathbf{w}(G)/2+\mathbf{w}(\mathrm{MinST}(G,\mathbf{w}))/4+k\)

_in a directed graph G with positive integer edge weights_ \(\mathbf{w}:E(G)\rightarrow\mathbb{Z}_{\ge 1}\) _in_ FPT_-time?_

We note that for the Maximum Cut problem, the Poljak-Turzík guarantee also applies, and in \[LPW24\] Lill, Petrova and Weber have shown that a cut of weight at least **w**(_E(G_))/2+**w**(MinST(_G,_**w**))/4+_k_ can be found in \(2^{\mathcal{O}(k)}\cdot|G|\) time, if _G_ has integer edge weights. Similarly, the weight of the maximum spanning tree is also a viable lower bound for the maximum cut weight in _G_. This gives rise to the following natural open problem.

**Open Question 4.** _Can we find a cut of weight at least_ **w**(MaxST(_G,_**w**))+_k in an undirected graph G with positive integer edge weights_ \(\mathbf{w}:E(G)\rightarrow\mathbb{Z}_{\ge 1}\) _in_ FPT_-time?_

For the last two open questions, the weights could as well be replaced with rationals not less than one.

One can also study the existence of efficient kernelization algorithms. The main result of \[EM18\] demonstrates that many problems parameterized above the Poljak-Turzík bound admit linear kernels, in the unweighted (oriented graph) case. In \[LPW24\], the authors show that Maximum Cut parameterized above Poljak-Turzík is in FPT in the case of integral weights. Can we improve this result and prove that it admits polynomial kernels? Can we do the same for Theorem 1 and show that \(\mathrm{MAS}/\mathrm{MaxST}(\mathbb{Z}_{\ge 1})\) admits polynomial kernels? We summarize this direction in the following question.

**Open Question 5.** _Do polynomial kernels exist for any relevant weighted problem parameterized above the Poljak-Turzík or the maximum spanning tree guarantees?_

Obtaining a negative answer to this question for some weighted parameterized problem, that, on the other hand, admits an FPT-algorithm, would also be very interesting.

## References

