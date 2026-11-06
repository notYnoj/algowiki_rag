# Lexicographic PLS-complete problems: Max-_k_-SAT, Abelian Permutation Orbit Minimization, and approximate pure Nash equilibria

**Dominik Scheder**<br> TU Chemnitz, Germany

**Johannes Tantow**<br> TU Chemnitz, Germany

**Abstract**

How hard is it to find a local optimum? If we are given a graph and want to find a locally maximal cut-meaning that the number of edges in the cut cannot be improved by moving a single vertex from one side to the other-then just iterating improving steps finds a local maximum since the size of the cut can increase at most |_E_| times. If, on the other hand, the edges are weighted, this problem becomes hard for the class PLS (Polynomial Local Search) [19].

We are interested in optimization problems with _lexicographic costs_. For Max-Cut this would mean that the edges _e_<sub>1</sub>_,...,e<sub>m</sub>_ have costs _c(e<sub>i</sub>_)=2_<sup>i</sup>_. For such a cost function, it is easy to see that finding a _global_ Max-Cut is easy. In contrast, we show that it is PLS-complete to find an assignment for a 4-CNF formula that is locally maximal (when the clauses have lexicographic weights); and also for a 3-CNF when we relax the notion of "local" by allowing to switch two variables at a time.

This result is interesting for two different reasons. Firstly, it offers another starting point for reductions to problems that are lexicographic by definition. We use these results to answer a question in Scheder and Tantow [20], who showed that finding a lexicographic local minimum of a string \(s\in\{0,1\}^n\) under the action of a list of given permutations \(\pi_1,\dots,\pi_k\in S_n\) is PLS-complete. They ask whether the problem stays PLS-complete when the \(\pi_1,\dots,\pi_k\) commute, i.e., generate an Abelian subgroup _G_ of _S<sub>n</sub>_. We show that it does, and in fact stays PLS-complete even (1) when every element in _G_ has order two and also (2) when _G_ is cyclic, i.e., all \(\pi_1,\dots,\pi_k\) are powers of a single permutation \(\pi\).

Secondly, we use it to further investigate the complexity of computing pure \(\alpha\)-Nash equilibria in congestion games. Using lexicographic 4-SAT, we obtain a simple proof of the PLS-completeness originally shown by Skopalik and Vöcking[21]. The simple structure allows us to also show hardness for exponential and polynomial delay functions with positive coefficients. Additionally, every resource is used by a constant amount of players and every player has a constant number of strategies. However, the degree of the polynomials is not bounded by a constant but grows linearly with the number of clauses and logarithmically with the approximation ratio \(\alpha\).

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Problems, reductions and completeness; Theory of computation \(\rightarrow\) Exact and approximate computation of equilibria

**Keywords and phrases** PLS, local search, total search problems, permutations, congestion games

\(\includegraphics{}\)

