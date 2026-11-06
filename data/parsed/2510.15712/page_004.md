Skopalik and Vöcking have shown that finding an \(\alpha\)-equilibrium in congestion games with step functions is PLS-complete[21]. Using Theorem 3, we can give a very short and simple proof of this fact. In the appendix of the work of Caragiannis, Fanelli, Gravin and Skopalik [3] this was also shown for polynomials with positive coefficients. Nonetheless, the question of the complexity of finding approximate Nash equilibria with positive coefficient polynomials was raised in [8, 22, 23].

Using LocalLexMax-4-SAT we get an extremely simple reduction for both cases that is also very regular and easy to analyze. In the light of this hardness result it is natural to ask whether there are useful parameters of the game that allow us to solve the problem efficiently when these parameters are small.

In all reductions the maximum number of players per resource is bounded (3 in [21], 2 in [3] and 4 in our work). Another interesting parameter is the maximum number of strategies per player. In [3, 21] this grows linearly with the input due to the \(\check{\mathrm{ck}}_{i,b}^j\) strategies of the _Y<sub>j</sub>_ players. Our reduction shows that the problem is hard even when each player has only two strategies.<sup>1</sup> We will prove Theorem 5 in Section 2.

All reductions in this work are tight, i.e. the standard algorithm that starts from a solution and moves to a better neighbor takes for any problem in the worst-case exponentially many steps and deciding if a solution is the result of the standard algorithm is PSPACE-complete. (see Section D).

## 2 Computing approximate Nash equilibria in congestion games - proof of Theorem 5

In a congestion game, there is a set _N_={1_,...,n_} of players and a set _E_ of resources. Each player \(i\in N\) has a set of \(strategiesS_i\subseteq 2^E\). Each resource \(e\in E\) has a \(delayde:\mathbb{N}\rightarrow\mathbb{N}\). A _strategy profile_ is a vector **s**=(_s_<sub>1</sub>_,s_<sub>2</sub>_,...,s<sub>n</sub>_) with \(si_i\in S_i\). The _load_ of a resource _e_ under profile **s** is the number of players using it: \(l(e,\mathbf{s}):=|\{i\in N|e\in si_i\}|\). This load causes a delay of _de(l(e,_**s**)). The cost of such a strategy profile **s** for a player _i_ is the sum of the delays of each resource they use, i.e. \(C_i(\mathbf{s})=\sum_{e\in s_i}d_e(l(e,\mathbf{s}))\). Players act selfishly and switch their strategy if it reduces the cost. A pure Nash equilibrium is a strategy profile **s**=(_s_<sub>1</sub>_,...,s<sub>n</sub>_) where no player has an incentive to unilaterally change their strategy, i.e., if

\(\forall i\in N\forall s'_i\in S_i:C_i(\mathbf{s})\le C_i(s_1,\dots,s_{i-1},s'_i,s_{i+1},\dots,s_n).\)

For such games, a pure Nash equilibrium always exists, as shown by Rosenthal [18]. Fabrikant, Papadimitriou, Talwar [7] show that finding a pure Nash equilibrium is PLS-complete by giving a simple reduction from local NAE-3-SAT. When we assume that the players are lazy and only change their strategy if their cost decreases by a significant amount, we get the concept of an _approximate_ pure Nash equilibrium. More formally, for a real \(\alpha\ge 1\), an \(\alpha\)-equilibrium is a strategy profile **s**=(_s_<sub>1</sub>_,...,s<sub>n</sub>_) such that

\(\forall i\in N\forall s'\in S_i:C_i(\mathbf{s})\le\alpha\cdot C_i(s_1,\dots,s_{i-1},s'_i,s_{i+1},\dots,s_n).\)

Skopalik and Vöcking [21] show that this is PLS-complete for any computable \(\alpha>1\) using an involved reduction from Flip and even more extended in [3] for polynomials with positive coefficients.

<sup>1</sup> Players with one strategy can be removed by changing the payoff functions, so this is the minimum number of strategies players can have in any (non-trivial) game.

