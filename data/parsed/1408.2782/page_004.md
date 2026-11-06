**Remark 2.2.** Again, we reiterate that there is no consensus in the literature on the precise definition of almost stability. For example, the authors of \[3\] compare the number of blocking pairs to |_M_|, the size of the matching rather than |_E_|, as we do. Since in \[3\], they only consider bounded preference lists, their notion of almost stability agrees with Definition 2.1 up to a constant factor.

**Definition 2.3** (Kipnis and Patt-Shamir \[9\])**.** Given \(\varepsilon\ge 0\), preferences P, and a matching _M_ we call an edge \((m,w)\in E\varepsilon\)**_-blocking_** if _m_ and _w_ appear an \(\varepsilon\)-fraction higher on each other’s preferences than their assigned partners. Specifically, (_m,w_) is \(\varepsilon\)-blocking if

\(P^m(p(m))-P^m(w)\ge\varepsilon degm\text{and}P^w(p(w))-P^w(m)\ge\varepsilon degw.\)

We say that _M_ is \(\varepsilon\)**_-blocking-stable_** if it contains no \(\varepsilon\)-blocking pairs.

**Remark 2.4.** Kipnis and Patt-Shamir \[9\] prove an \(\Omega(\sqrt{n}/logn)\) round lower bound for finding an \(\varepsilon\)-blocking-stable matching. That we are able to achieve a polylogarithmic round algorithm for the almost stable matching problem using Definition 2.1 bolsters the use of Definition 2.1 for almost stability, at least for practical applications. Further, **ASM** produces a matching which is nearly \(\varepsilon\)-blocking-stable in the sense that after the removal of an arbitrarily small fraction of "bad" men, the resulting matching is \(\varepsilon\)-blocking stable with respect to the remaining players.

## 2.2 Computational model

We describe **ASM** in terms of the CONGEST model formalized by Peleg \[11\]. In this distributed computational model, each player \(v\in X\cup Y\) represents a processor. Given preferences P, the communication links between the players are given by the set of edges _E_ in the communication graph _G_. Communication is performed in synchronous rounds. Each communication round occurs in three stages: first, each processor receives messages (if any) sent from its neighbors in _G_ during the previous round. Next, each processor performs local calculations based on its internal state and any received messages. We make no restrictions on the complexity of local computations. Finally, each processor sends short (_O_(log_n_) bit) messages to its neighbors in _G_--the processor may send distinct messages to distinct neighbors. In the CONGEST model, complexity is measured by the number of communication rounds needed to solve a problem.

**Remark 2.5.** Although the CONGEST model allows for unbounded local computation during each round, the computations required by **ASM** can be implemented in linear or near-linear time in each processor’s input.

## 2.3 Maximal matchings

As a subroutine, **ASM** requires a method for computing maximal matchings in a graph.

**Definition 2.6.** A matching _M_ is a **_maximal matching_** if it is not properly contained in any larger matching. Equivalently, _M_ is maximal if and only if every \(v\in V\) satisfies precisely one of the following conditions:

1. there exists a unique \(u\in V\) with \((v,u)\in M\);<tbc>

2. for all \(u\in N(v)\) there exists \(v'\in V\) with \(v'\neq v\) such that \((v',u)\in M\).

For the deterministic version of our algorithm, we invoke the work of Hanń ́ckowiak, Karo ́nski, and Panconesi \[6\] who give a deterministic distributed algorithm which finds a maximal matching in a polylogarithmic number of rounds.

**Theorem 2.7** (Han ́ckowiak, Karo ́nski, and Panconesi \[6\])**.** There exists a deterministic distributed algorithm, **MaximalMatching**, which finds a maximal matching in a communication graph _G_=(_V,E_) in log<sup>4</sup>(_n_) rounds, where _n_=|_V_|.

