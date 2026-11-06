## Techniques.

We obtain our results by developing two new query lower bound techniques for generic problems \(\Pi\) in the comparison-query model, and then instantiating them to the problem \(\Pi_T\) of inversion minimization on a fixed tree _T_. Although some of our techniques extend to relations, we restrict attention to computational problems \(\Pi\) that are functions, just like the problem \(\Pi_T\) that we focus on.

**Definition 10 (computational problem and algorithm in the comparison-query model).** _A computational problem in the comparison-query model is a total function on the rankings of a set X. An algorithm in the comparison-query model can access an input ranking_ \(\rho:X\rightarrow[n]\) _using comparison queries: For given_ \(x_1,x_2\in X\)_, test if_ \(\rho(x_1)<\rho(x_2)\).

Both of our techniques follow the common pattern of lower bounding the number of distinct execution traces that any algorithm for \(\Pi\) needs to have.

**Definition 11 (execution trace, complexity measures** \(\mathrm{D}(\cdot)\) **and** \(\mathrm{Q}(\cdot)\)**).** _Consider an algorithm A for a problem_ \(\Pi\) _in the comparison-query model. An execution trace of A is the sequence of comparisons that A makes on some input_ \(\rho\)_, as well as the outcomes of the comparisons. The complexity_ \(\mathrm{D}(\Pi)\) _is the minimum over all possible algorithms for_ \(\Pi\) _of the number of distinct traces the algorithm has over the set of all inputs_ \(\rho\)_. The complexity_ \(\mathrm{Q}(\Pi)\) _is the minimum, over all possible algorithms for_ \(\Pi\) _of the maximum number of comparisons that the algorithm makes over the set of all inputs_ \(\rho\).

The complexity measure Q is what we refer to as query complexity. Since the maximum number of queries that an algorithm _A_ makes is at least the base-2 logarithm of the number of execution traces, we have that \(\mathrm{Q}(\Pi)\ge\mathrm{log}_2(\mathrm{D}(\Pi))\). Note that, in order to avoid confusion with the tree _T_ specifying an instance of inversion minimization, we refrain from the common terminology of decision trees in the context of the complexity measure D. In those terms, we lower bound the number of leaves of any decision tree for \(\Pi\), and use the fact that the depth of this binary decision tree is at least the base-2 logarithm of the number of leaves.

Both techniques proceed by considering the effect on the output of perturbations to the input ranking \(\rho\) that are hard for queries to observe. More specifically, we consider the following perturbations:

**Definition 12 (adjacent-rank transposition, affected items).** _An_ adjacent-rank transposition _is a permutation_ \(\tau\) _of_ \[_n_\] _of the form_ \(\tau=(r,r+1)\)_, where_ \(r\in[n-1]\) _and n denotes the number of items. Given_ \(\tau\) _and a ranking_ \(\rho:X\rightarrow[n]\)_, the_ affected items _are the two elements_ \(x\in X\) _for which_ \(\tau(\rho(x))\neq\rho(x)\)_, i.e., the items with ranks r and r_+1 _under_ \(\rho\).

As with any permutation of the set of ranks, the effect of \(\tau\) on a ranking \(\rho\) is the ranking \(\tau\rho\). Adjacent-rank transpositions are the least noticeable perturbations one can apply to a ranking in the following sense: If two rankings differ by an adjacent-rank transposition, then the only query that distinguishes them is the query that compares the affected items.

## Sensitivity.

Our first technique turns this observation around to obtain a lower bound on query complexity. We adopt the terminology of sensitivity from Boolean query complexity.

**Definition 13 (sensitivity, average sensitivity,** \(s(\cdot)\)**).** _Let_ \(\Pi\) _be a computational problem in the comparison-query model on a set X of items. For a fixed ranking_ \(\rho\) _and adjacent-rank transposition_<tbc>

