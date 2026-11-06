## 1 Introduction

Polynomial Local Search (PLS) is the complexity class of problems that require us to find a local optimum. Formally, a PLS problem is defined by a set I of instances, a set S of solutions, a function Feasible \(:\mathcal{I}\times\mathcal{S}\rightarrow\{\text{\texttt{true}},\text{\texttt{false}}\}\) telling us whether _s_ is at all a feasible solution to instance _x_, and a function StartSolution \(:\mathcal{I}\rightarrow\mathcal{S}\) where StartSolution(_x_) is always a feasible solution for _s_; further, functions Value \(:\mathcal{I}\times\mathcal{S}\rightarrow\mathbb{N}\), where Value(_x,v_) computes how good the solution _v_ is for the instance _x_; and a _successor function_ Succs \(:\mathcal{I}\times\mathcal{S}\rightarrow\mathcal{S}^*\), where Succs(_x,v_)=(_w_<sub>1</sub>_,...,w<sub>k</sub>_) means that _w_<sub>1</sub>_,...,w<sub>k</sub>_ are the neighboring solutions to solution _v_. We require that all feasible solutions to _x_ have the same length, and that all functions are polynomially computable. In particular, this means that each solution _v_ has at most polynomially many successors _w<sub>i</sub>_. A feasible solution _v_ is _locally optimal_ if none of its successors _w<sub>i</sub>_ is _better_, i.e., \(\text{Value}(x,v)\ge max_i\text{Value}(x,w_i)\) (for maximization problems) or \(\text{Value}(x,v)\le min_i\text{Value}(x,w_i)\) (for minimization problems). The goal is to find a locally optimal feasible solution.

The study of this class was initiated by Johnson, Papadimitriou and Yannakakis in [13]. In their work they showed that Flip is PLS-complete:

\(\blacktriangleright\) **Search Problem 1** (Flip)**.** _Given a circuit C with n input and m output bits; find an input_ \(x\in\{0,1\}^n\) _such that_ \(C(x)\unknown_\text{lex}C(x\oplus\text{\texttt{e}}_i)\) _for all i_=1_,...,n. Here,_ \(\unknown_\text{lex}\) _is the lexicographical order on_ {0,1}_<sup>m</sup>, i.e., we interpret the outputs as binary numbers and compare them accordingly._

The instances of Flip are circuits; feasible solutions are bit vectors of the appropriate length; the function Value is given by the output of the circuit and the neighborhood of a bit vector are all bit vectors with a Hamming distance of 1.

In the realm of search problems, the notion of a _reduction from A to B_ requires a function _f_ mapping _A_-instances to _B_-instances and a function _g_ mapping _B_-solutions to _A_-solutions. Several search problems are known to be PLS-complete under these reductions:

**1.** LocalMax-_k_-SAT for \(k\ge 2\). Given a _k_-CNF formula \(F=C_0\wedge\cdots\wedge C_{m-1}\) with _n_ variables and clause weights _w_<sub>1</sub>_,...,w<sub>m</sub>_, find an assignment \(\alpha\) such that the weight of satisfied clauses cannot be improved by flipping a single variable (Krentel [16], Schäffer and Yannakakis [19]).

**2.** LocalMaxCut. Given a graph _G_=(_V,E_) and edge weights \(w:E\rightarrow\mathbb{R}\), find a cut \(V=S\unknown T\) such that its weight (the sum of weights of all edges crossing the cut) cannot be improved by moving a vertex from one side to the other (Schäffer and Yannakakis [19]).

**3.** Permutation Orbit Local Minimum (Polm): Given a string \(s\in\{0,1\}^n\) and permutations \(\pi_1,\dots,\pi_k\in S_n\), find \(\pi\in\langle\pi_1,\dots,\pi_k\rangle\) such that \(s\circ\pi\) is lexicographically locally minimal, i.e, \(s\circ\pi\unknown_\text{lex}s\circ\pi\circ\pi_i\) for all \(1\le i\le k\) (Scheder and Tantow [20]).

**4.** Finding pure Nash equilibria in congestion games, described in more detail in Section 2 below (Fabrikant, Papadimitriou and Talwar [7], Ackermann, Röglin and Vöcking[1]).

The first two are obviously in PLS. Polm is because membership \(\pi\in\langle\pi_1,\dots,\pi_k\rangle\) can be decided efficiently (Furst, Hopcroft and Luks [9]). For congestion games, the existence of pure Nash equilibria can be shown using an appropriate potential function that decreases whenever a player decreases their cost by changing their strategy (Rosenthal [18]), which then also shows membership in PLS.

As described by Giannakopoulos, Grosz, and Melisourgos [10], the function Value can be described as a function mapping a solution _s_ to some solution vector \(s'\) and the result is then

