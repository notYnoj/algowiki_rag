## Step 3: Verifying the Sparse Certificate

Given Lemma 3.4, we present our algorithm for (min,+)- Witness Equality. In this final step, we search all candidate block witnesses and check if they are true block witnesses. As discussed, we begin by sampling random primes and generating all candidate block witnesses for every pair (_i,j_).

Correctness of the above procedure follows by the correctness of Lemma 3.4 and the definition of candidate block witnesses. The time required over all _O(N/B_) blocks _K_ and _O_(log_S_) primes _p_ is

\(\tilde{O}\left(\frac{N^3}{B}+N^2P^2+\frac{N^3P^{1-\gamma}}{B^{1+\gamma}}+\frac{N^3(BP)^{\kappa-\gamma}}{B}\right).\)

For a pair (_i,j_), let _K(i,j_) denote the set of candidate block witnesses. In the second phase, we test whether a candidate block witness is a block witness. We use the following algorithm for every pair (_i,j_).

Correctness of the algorithm follows from the fact that Claim 3.3 implies that every block witness is a candidate block witness. Thus, if (_i,j_) is accurate, we will eventually iterate over a block witness in _K(i,j_) and enumerate the witness _k_ such that _A_\[_i,k_\]+_B_\[_k,j_\]=_C_\[_i,j_\]. On the other hand, if (_i,j_) is not accurate, no check will succeed.

To bound the running time, we separately bound the time required to process block witnesses and false candidates (i.e. candidate block witnesses that are not block witnesses). Since we terminate after any successful check, we process at most 1 block witness for every pair (_i,j_), resulting in total time _O(N_<sup>2</sup>_B_) to process all block witnesses. To bound the time required to process false candidates, we bound the total number of false candidates. From Claim 3.3, a block _K_ that is not a block witness is a candidate block witness with probability at most \(2^{-\lceil logS\rceil}\le S^{-1}\). Since there are _N_<sup>2</sup> (_i,j_) pairs and _O(N/B_) blocks per pair, the total number of false candidates is in expectation at most _O(N_<sup>3</sup>/(_BS_)), resulting in _O(N_<sup>3</sup>_/S_) expected time to process all false candidates. Overall, the expected runtime of our algorithm is

\(\tilde{O}\left(\frac{N^3}{B}+N^2P^2+\frac{N^3P^{1-\gamma}}{B^{1+\gamma}}+\frac{N^3(BP)^{\kappa-\gamma}}{B}+N^2B+N^3/S\right).\)

Recall that we require \(P\gg BlogU\), so that minimizing _P_ subject to this constraint, the running time is

\(\tilde{O}\left(\frac{N^3}{B}+N^2B^2log^2U+N^3B^{-2\gamma} logU+N^3B^{2\kappa-2\gamma-1}logU+N^2B+N^3/S\right).\)

Setting _S=N_ and simplifying (e.g. recalling \(\kappa\ge\gamma\)), we obtain the running time

\(\tilde{O}\left(\frac{N^3B^{2(\kappa-\gamma)}}{B}logU+N^2B^2log^2U+N^3B^{-2\gamma} logU\right).\)

\begin{tabular}{cc}
\multicolumn{2}{c}{**Generate Candidate Block Witnesses.**} \\
1. & Sample \(\lceil logS\rceil\) random primes independently in the range \[_P,_2_P_\]. \\
2. & Using Lemma 3.4, verify for every pair (_i,j_) and block _K_, whether _K_ is a candidate block witness with respect to all sampled primes. Return _K_ is a candidate block witness if and only if yes. \\
\end{tabular}

\begin{tabular}{cc}
\multicolumn{2}{c}{**Verify Block Witnesses.**} \\
1. & For each candidate block witness \(K\in K(i,j)\) enumerate \(k\in K\) and check _A_\[_i,k_\]+_B_\[_k,j_\]=_C_\[_i,j_\]. \\
2. & If any check succeeds, return (_i,j_) is accurate and terminate. \\
3. & If no check succeeds, return (_i,j_) is inaccurate. \\
\end{tabular}

