To bound the height of the recursion trees, observe that Corollary 2.5 in \[AKT20a\], especially its adapted Corollary 3.5 mentioned above, is robust enough to accommodate the terminals, an aspect previously leveraged in those algorithms to handle the arbitrary node subsets resulting from the recursion. Thus, the same argument from the Monte Carlo algorithm on the height of the recursion trees being at most log<sub>4/3</sub>_n_ follows here as well. This concludes the correctness proof.

## Running time

A successful choice of a pivot _p_ in step 4 means that both (4a) \(|V_{small}|\ge n'/4\), and (4b) _p_ is not an overused pivot. The first case (4a) is handled similarly to the Monte Carlo algorithm; the probability of 8log_n_ consecutive failures in a single instance is bounded by (1/2)<sup>8log_n_</sup>=1_/n_<sup>8</sup>, and by applying the union bound over the at most \(\tilde{O}(n^2)\) instances in all repetitions, with probability at most 1_/n_<sup>6</sup> at least one instance takes more than 8log_n_ attempts until a successful choice of _p_. The second case (4b) was handled in the correctness proof in Lemma 3.6. Again, by the union bound over the two cases, with high probability no instance takes more than 8log_n_ times to select a pivot, and no pivots are overused. To bound the total number of Max-Flow calls, consider the total number of terminal pairs in all repetitions (counting multiplicities) for which we could potentially directly call Max-Flow.

• for case (i), this number is at most \(\tilde{O}((\alpha(V)/k)/k\cdot k^2\cdot k)\le\tilde{O}(\alpha(V)k)\). This is explained by having \((\alpha(V)/k)\) terminals in the \[_k,_2_k_) stage, considering only final (small) \(\le\tilde{O}(k)\) sized instances in this case, the at most \(\tilde{O}(k^2)\) pairs of terminals within a small instance, and the \(\tilde{O}(k)\) repetitions.<tbc>

• for case (ii), this number is simply bounded by \(\tilde{O}(\sum_{u\in V}\alpha(u)\cdot k)=\tilde{O}(\alpha(V)k)\).

Since we only call Max-Flow directly for a node pair if it is required by at least _k_ repetitions of a certain type (either (i), or (ii)), the total number of queries in both cases is bounded by \(\tilde{O}(\alpha(V))\). The basic recursion takes \(\tilde{O}(k\cdot(\alpha(V)/k))\le\tilde{O}(\alpha(V))\) calls to Max-Flow, concluding the running time proof.

## Space usage

We aim to bound the total space used by the data structure, starting with item 1 of Theorem 3.1.

• For cuts in step 2, an initial bound for the occupied space is at most<tbc>

<tbc>\(\tilde{O}\left(max_k\left\{k\cdot(min\{\alpha(V)/k,n\}\cdot 2k)\right\}\right)\le\tilde{O}(\alpha(V)n),\)<tbc>

<tbc>taking into account that for a cut \(\left(S_{p,f(u)},C_{p,f(u)},S_{f(u),p}\right)\) in this step and in a \[_k,_2_k_) stage, we only store the separator _C<sub>p,f(u_)</sub> if its size is smaller than 2_k_, and the set {_f_<sup>-1</sup>_f(u_)} (i.e., the nodes assigned to the side opposite of _p_). However, this can be further improved as all node pairs \(u,v\in V_{\ge k}\) are anyway queried directly for \(k\ge\sqrt{\alpha(V)/(60log^3n)}\) in step 6a due to the halting condition in step 5. Consequently, we may perform those queries directly in a preprocessing step, performing the recursion only for stages where \(k\le\tilde{O}\left(\sqrt{\alpha(V)}\right)\), and so the space occupied in step 2 becomes \(\tilde{O}\left(\alpha(V)^{3/2}\right)\), as required.<tbc>

• For cuts in step 6, recall that any query we make in this step is required by at least _k_ repetitions. Using the bound from the Monte Carlo algorithm, the occupied space here is at most<tbc>

<tbc>\(\tilde{O}\left(k\cdot\alpha(V)^{3/2}/k\right)\le\tilde{O}\left(\alpha(V)^{3/2}\right).\)<tbc>

