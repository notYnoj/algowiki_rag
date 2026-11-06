<tbc>As a consequence of Theorem 1.1 and the trivial bound \(\mathcal{Q}(n)\le n!\), we conclude that

\(lim_{n\rightarrow\infty}\frac{log\mathcal{Q}(n)}{nlogn}=1.\)

This proves, in a strong form, a conjecture of Rivin, Vardi, and Zimmerman \[12, Conjecture 1\] who conjectured that the limit above is positive.

It is interesting to note that the previous lower bounds on Q(_n_) are actually due to algebraic constructions of solutions to the toroidal _n_-queens puzzle. In contrast, our construction relies purely on probabilistic and combinatorial methods: random greedy algorithms and absorption. The former has proved to be a powerful tool when constructing constrained combinatorial objects such as regular graphs \[13\], triangle Ramsey graphs \[2\], and high-girth approximate Steiner triple systems \[5, 3\]. Combined with absorbers, they also played important roles in the recent constructions of combinatorial designs \[6, 4\]. In the latter example, a random greedy algorithm was the key to obtaining lower bounds on the count of the associated objects \[7\].

We prove Theorem 1.1 by describing a probabilistic algorithm to construct solutions to the _n_-queens puzzle. We formally describe the algorithm in Section 2, and we give a brief overview here. The algorithm has two phases. The first is a random greedy algorithm that constructs an approximate toroidal _n_-queens configuration. Beginning with an empty board, we repeatedly place queens uniformly at random subject to the constraint that they may not share a row, column, or toroidal diagonal. We show that with high probability this algorithm succeeds in placing (1-_o_(1))_n_ queens on the board. This phase of the algorithm, which is analyzed in Section 3, also gives the enumeration used to prove Theorem 1.1. In the second phase of the algorithm we use absorbers to perform a small number of modifications and obtain a complete solution. The absorbing phase is analyzed in Section 4.

In the random greedy phase of the algorithm it would be natural to choose each queen uniformly at random subject to the constraint that it may not share a row, column, or (non-toroidal) diagonal with a previously placed queen. However, we have found this algorithm challenging to analyze. The difficulty is due to the fact that the lengths of the diagonals vary, leading to a non-uniform distribution of the queens. In contrast, toroidal diagonals all have the same length. This simplifies the analysis of the random greedy algorithm.

## 1.1. Notation and terminology.

We adopt the standard notation \[_n_\]:={1_,...,n_}. Also, we write \(a=b\pm c\) as a shorthand for \(b-|c|\le a\le b+|c|\).

Throughout, all asymptotics are with \(n\rightarrow\infty\). Since we are concerned only with asymptotic statements we assume that _n_ is sufficiently large for relevant inequalities to hold. For example, we may write _n_<sup>2</sup>-_n\>n_ without explicitly requiring _n\>_2.

We say that a sequence of events occurs **with high probability** (**w.h.p.**) if the probabilities of their occurrence tend to 1. Typically, we will abuse terminology and say that a _specific_ event occurs w.h.p. while leaving the sequential statement to be inferred from context.

To formally define the classical and toroidal _n_ queens problems, we identify the \(n\times n\) chessboard with \[_n_\]<sup>2</sup>. In the classical problem, a queen at (_x,y_) attacks all squares \((x',y')\) such that either \(x'=x\), \(y'=y\), \(x'+y'=x+y\), or \(x'-y'=x-y\). In the<tbc>

