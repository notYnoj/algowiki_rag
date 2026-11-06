**Algorithm 1** Search Algorithm for APA Matrix Multiplication

**Input:** An exact decomposition \(\mathcal{M}_{\langle m,k,n\rangle}=\sum_{j=1}^RU_j\otimes V_j\otimes W_j\).

**Output:** A decomposition corresponding to an APA \(\langle m,k,n\rangle\) algorithm with rank \(r'=r-l\) for \(l\ge 1\).

1: Run a flip-graph search (over F<sub>2</sub> or F<sub>3</sub>, starting from the input decomposition) until a decomposition \(\sum_{j=1}^RU'_j\otimes V'_j\otimes W'_j\) satisfying the conditions of Theorem 2.1 or Theorem 2.4 is found.

2: Lift the decomposition to characteristic zero.

3: **if** lifting fails **then**

4: Return to line 1 and continue the search.

5: **else**

6: Construct symbolic basis transformations \(R\in\mathbb{C}(\varepsilon)^{m\times m}\), \(S\in\mathbb{C}(\varepsilon)^{k\times k}\), and \(T\in\mathbb{C}(\varepsilon)^{n\times n}\) such that \(R^{-1}U'_pS\otimes S^{-1}V'_TT\otimes T^{-1}W'_JR\) has entries in \(\varepsilon\mathbb{C}[\varepsilon]\) for \(1\le j\le l\).

7: **end if**

8: **return** \(\sum_{j=l+1}^rR^{-1}U'_pS\otimes S^{-1}V'_TT\otimes T^{-1}W'_JR\)

preserved.<sup>9</sup> Of course, it is sometimes not possible to lift a decomposition with one (or more) nilpotent terms to characteristic zero, in which case we simply continue the search.

### 2.2.2 Additional Results

In practice, the initial decompositions used to start the search are particularly important. Perminov’s implementation allows many flip graph walks to run in parallel, possibly with decompositions of different dimensions for each walk. Periodically, decompositions are combined or modified by meta-moves, as described in the meta-flip-graph paper \[40\]. With human intervention, we also chose the most promising decompositions seen so far as seeds for a restarted search. Most new border rank decompositions were found over the course of a week using a 23 thread search. We ran the search on a Ryzen 9 9900X CPU.

Our best result came in the case of \(\langle 2,4,5\rangle\), where we found the first rank 31 APA algorithm and therefore lowered the border rank upper bound for this size to 31. Encoding matrices for this algorithm are given in Section B.1. For the other schemes found in our search (including those listed in s 1 and 2), see https://github.com/nliskij/border-rank.

### 2.3 Generalization via Null Cone Membership Testing

Our approach to searching for suitable exact algorithms is not the most general possible. It may be the case that individual rank one terms cannot be made \(O(\varepsilon)\) but their sum can. In the representation theory literature, the sum of such terms would be called an element of the null cone of the De-Groote group. This may be promising for future work since recent papers have addressed algorithms for testing null cone membership \[14, 15\]. While such an approach can produce decompositions more general than described here, in practice we were not able to obtain any further border-rank improvements.

## 3 Alternative Basis APA Matrix Multiplication

In this section, we demonstrate that APA matrix multiplication algorithms can be accelerated by reducing their additive complexity, accomplished by applying fast, symbolic basis transformations to reduce the number of nonzero entries in the encoding matrices \(U(\varepsilon)\), \(V(\varepsilon)\) and \(W(\varepsilon)\) (recall Figure 2). This has the effect of lowering the leading coefficient in an APA algorithm’s arithmetic _and_ IO complexities.<sup>10</sup> In particular, generalizing \[32\], we present a greedy algorithm for constructing these basis transformations, which depend on an evaluation parameter \(\varepsilon\).

<sup>9</sup>This can be done since nilpotence of a product is simply a polynomial constraint in the entries of the corresponding matrices, which only requires adding additional rows to the Jacobian in the lifting step. <sup>10</sup>While not the focus of this paper, IO complexity refers to the amount of data movement or communication performed by an algorithm.

