<tbc>These basis transformations, which were constructed by hand, transform the sixth term of (2.3) to

\(\left(\begin{array}{ c c }
0 & 0 \\
0 & \varepsilon
\end{array}\right)\otimes\left(\begin{array}{ c c }
-\varepsilon & 0 \\
0 & 0
\end{array}-1\right)\otimes\left(\begin{array}{ c c }
0 & \varepsilon \\
0 & 0 \\
0 & 0
\end{array}\right).\) (2.8)

While in this case the entries of _R_<sup>-1</sup>_U_<sub>6</sub>_S_, _S_<sup>-1</sup>_V_<sub>6</sub>_T_, and _T_<sup>-1</sup>_W_<sub>6</sub>_R_ do _not_ all belong to \(\varepsilon\mathbb{C}[\varepsilon]\), their tensor product is still \(O(\varepsilon)\). In this way, Theorem 2.1 and Theorem 2.4 guarantee more than is necessary to remove one (or more) terms from an exact algorithm. We leave determining what constitutes an "optimal" choice for these basis transformations to future work.

## 2.2 Implementation Details and Results

We can use the results from the previous section to determine when an APA algorithm can be derived from an exact one. Nevertheless, the conditions suggested by Theorem 2.1 and Theorem 2.4 are more rare than we might expect. Indeed, an initial search of the repository of Sedoglavic<sup>8</sup> turned up no exact algorithms whose corresponding tensor decompositions contain a nilpotent term. Luckily we can generate more candidates by running a _flip graph_ search, which we describe below.

**Remark 2.5.** There are many other search algorithms for exact matrix multiplication that could be used here in place of the flip graph - e.g., algorithms that apply some version of least squares to the tensor decomposition problem \[3, 35, 56\] or use reinforcement/machine learning \[28, 47\]. We choose the flip-graph approach since it is particularly easy to use and requires minimal computing resources.

### 2.2.1 Flip Graph Search for Exact Decompositions

The flip graph is a recent tool for discovering (exact) matrix multiplication algorithms introduced by Kauers and Moosbauer \[39\]. For given _m_, _k_, and _n_, the vertices of the \(\langle m,k,n\rangle\) flip graph are \(\langle m,k,n\rangle\) matrix multiplication algorithms, represented by their corresponding tensor decompositions. Edges in the graph connect schemes that can be obtained from one another via the _flip_ operation. In the simplest case, a flip replaces two rank-one factors \(A\otimes B\otimes C\) and \(A\otimes B'\otimes C'\) in a matrix-multiplication decomposition with \(A\otimes(B+B')\otimes C\) and \(A\otimes B'\otimes(C'-C)\). Since this leaves the sum of the terms unchanged, each flip results in a new decomposition and corresponding algorithm (of the same rank). Note that this only works because the terms \(A\otimes B\otimes C\) and \(A\otimes B'\otimes C'\) share the common factor _A_; to perform a flip in general, we need at least one factor to be shared between the rank-one terms, though it need not be the first.

The key insight for Kauers and Moosbauer is that, under the right circumstances, an algorithm found in the flip graph can be _reduced_, meaning two rank-one terms can be replaced by a single one, thereby producing a new algorithm of lower rank. Accordingly, they propose a search algorithm that runs a "flip- graph walk," in which successive, random flips are applied to an initial decomposition, at each step checking for the conditions that make a reduction possible. In \[39\], they use this algorithm to improve the best-known ranks for several sizes \(\langle m,k,n\rangle\). Subsequent work accelerated the original flip graph algorithm by leveraging symmetry and/or traversing multiple sizes in one search \[1, 40, 46\].

In this work, we are interested in using a flip graph walk to generate many exact algorithms rather than improve the rank of exact matrix multiplication. In this way, the flip graph gives a simple search algorithm for our application: run a flip-graph walk, checking not for possible reductions but instead for decompositions that satisfy the conditions of Theorem 2.1 and/or Theorem 2.4. With this, we can now state our full algorithm for generating new APA schemes, which is shown here (in high-level pseudocode) as Algorithm 1. Like Theorem 2.2, this pseudocode assumes that the terms that can be removed from an exact decomposition are leading. This is done to simplify the notation (and since we can always reorder the terms in a decomposition however we like).

For better efficiency we use an implementation of Perminov \[50\] to execute the flip-graph search in line 1 of Algorithm 1. As is typical for flip-graph algorithms, this search is conducted over a finite field (usually F<sub>2</sub> or F<sub>3</sub>) with nilpotence checked by repeatedly multiplying each _U<sub>j</sub>V<sub>j</sub>W<sub>j</sub>_. Resulting decompositions are then converted to characteristic zero via Hensel lifting \[60\], which we modify to ensure that nilpotence is<tbc>

<sup>8</sup>https://fmm.univ-lille.fr/

