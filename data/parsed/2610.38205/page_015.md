## 3.2 \(\alpha\)-Navigable Graphs in Batches

Having established that PartialVoteCover covers at least half of the elements in _U_ when given a valid parameter opt, we now describe how we use it to build a full \(\alpha\)-navigable graph. It is easy to see that if we can cover a constant fraction of _U_, then we can do so again to cover another constant fraction of the remainder, and that we will eventually cover all of _U_ after at most log<sub>2</sub>(|_U_|) calls to PartialVoteCover. Our full algorithm follows this general strategy.

**Algorithm 3.2** BatchedVoteCover \((P,\alpha,\varepsilon,C,c,\gamma)\)

**Input:** A set _P_ of _n_ points and constants \(\alpha\ge 1\), \(\varepsilon,C,c>0\), and integer \(\gamma\ge 0\).

**Output:** A graph _G_.

1: \(G,U\leftarrow\) an array of _n_ sets

2: \(Q\leftarrow P\)

3: **for** \(\mathsf{opt}\in\{2^1,2^2,2^3,\dots\}\) **do**

4: **for** \(p_i\in Q\) **do**

5: \(G[i]\leftarrow\) a set of optln_n_ elements sampled from _P_

6: \(U[i]\leftarrow P\backslash\{p_i\}\backslash\bigcup_{p_j\in G[i]}S_j\)

7: **for** \(t\in[\mathrm{log}_2n+\gamma]\) **do**

8: **for** \(p_i\in Q\) **do**

9: \(G[i]\leftarrow G[i]\cup\mathsf{PartialVoteCover}(\{S_{i\rightarrow j}^{\alpha(1+\varepsilon)}:j\in[n]\},U[i],\mathsf{opt},C,c)\)

10: \(\mathcal{N}\leftarrow\mathsf{VerifyNav}(G,\alpha,\varepsilon)\)

11: **for** \(p_i\in Q\) **do**

12: \(U[i]\leftarrow\{t:(i,t)\in\mathcal{N}\}\)

13: **if** \(U[i]=\emptyset\) **then** \(Q\leftarrow Q\backslash\{p_i\}\)

14: **if** \(Q=\emptyset\) **then**

15: **return** _G_

However, it is not so simple. If we wish to run PartialVoteCover on the remaining uncovered elements, we need to identify which elements of _U_ are still uncovered. This is difficult because, whereas we have efficient access to the sets containing a given element, we do not have efficient access to the elements contained in a given set. The naive approach of iterating over _U_ and removing any elements covered by some set in C takes too long (\(\Omega(n\cdot|\mathcal{C}|)\) time).

This is where we employ the VerifyNav procedure described in Section 2.5. Recall that given a graph, VerifyNav takes \(O(n^\omega\cdot\mathrm{log}(\Delta)/\varepsilon)\) time to return a list N of pairs (_s,t_) that includes any pair whose \(\alpha\) constraint is not satisfied and excludes any pair whose \(\alpha(1+\varepsilon)\) constraint is satisfied.

Thus, we can use VerifyNav to identify all _U_ that remain uncovered for a given set cover instance. Upon obtaining a partial set cover C for the set cover instance corresponding to point _p<sub>i</sub>_, we add to _G_ the edges (_p<sub>i</sub>,p<sub>j</sub>_) for all \(S_{i\rightarrow j}\in\mathcal{C}\). Then, we run VerifyNav on _G_ to obtain N, and the remaining uncovered points are all those _t_ where \((p_i,t)\in\mathcal{N}\). But note that using VerifyNav in this way to materialize the remainder of _U_ for only a single set cover instance is wasteful. Instead, we run a single VerifyNav to materialize the uncovered points for all set cover instances simultaneously.

That is, we execute PartialVoteCover on each set cover instance, obtaining a partial cover for each. We add the edges corresponding to those covers to an accumulated graph. Then, we run VerifyNav on the graph to list all remaining unsatisfied constraints. We run PartialVoteCover again on these remaining constraints. This process repeats roughly _O_(log_n_) times, which we know to be sufficient because each round covers a constant fraction of constraints. An important caveat<tbc>

