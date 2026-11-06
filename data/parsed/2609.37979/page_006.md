Next, we consider **problems in** P. Beyond Negative Triangle, Replacement Path is another fundamental problem in P that requires _n_<sup>3-_o_(1)</sup> time in the worst case under standard fine-grained hypotheses \[VW10, Vas18\]. In this problem, given a shortest _s-t_ path _P_ in a graph _G_, the goal is to compute, for every edge \(e\in P\), the length of the shortest _s-t_ path in _G-e_. Our Isomorphic- Priors model allows us to bypass this classical cubic barrier, achieving near-linear query time for Replacement Path and truly subcubic query time for Negative Triangle:

**Theorem 1.2** (Algorithms for Problems in P)**.** _There exists a deterministic isomorphic-priors algorithm that solves_ Replacement Path _using_ \(\widetilde{O}(km)\) _preprocessing time and_ \(\widetilde{O}(m)\) _query time. For_ Negative Triangle_, there exists a randomized_<sup>6</sup> _isomorphic-priors algorithm requiring_ \(\widetilde{O}(kn^\omega)\) _preprocessing time and_ \(\widetilde{O}(n^\omega)\) _query time._

Interestingly, while Negative Triangle and Replacement Path are subcubic equivalent in the classical setting \[VW10, AGV15\], their current complexities diverge in the Isomorphic-Priors model.

Additionally, we can solve Maximum Flow with near-linear preprocessing and query times, which is slightly faster than the current worst-case complexity \[CKL<sup>+</sup>22, vdBCP<sup>+</sup>23, vdBLL<sup>+</sup>21, vdBLN<sup>+</sup>20\].

Our third class of problems concerns the **frontier between** P **and** NP, namely **infinite- duration games** played on graphs, including Parity Game, Mean Payoff Game, Energy Game, and Simple Stochastic Game. In these games, two players take turns moving a token along the edges of a directed graph to form an infinite path. For example, in an Energy Game (played on a bipartite graph with integer edge weights), the token starts at vertex _s_ with initial energy _e_<sub>0</sub>. Traversing an edge adds its weight to the running total. Player A wins if they can keep the energy non-negative indefinitely; otherwise, Player B wins. We defer formal definitions to Section 7.

Originating from automata theory, reactive systems synthesis, and model checking \[EJ91, Tho97\], these games lie in \(\mathsf{NP}\cap\mathsf{coNP}\) (and often \(\mathsf{UP}\cap\mathsf{coUP}\) \[Jur98, Con92\]), making NP-hardness highly unlikely. While a major breakthrough (S 2017 best paper) showed Parity Game are solvable in quasipolynomial time \[CJK<sup>+</sup>17\], harder variants (Mean Payoff Game, Energy Game, and Simple Stochastic Game) still rely on randomized subexponential simplex-like methods \[Hal07, BV07\]. Determining whether any of these games admit polynomial-time algorithms remains a prominent open question.

In our setting, however, all these problems can be easily solved in near-linear time.

**Theorem 1.3** (Algorithms for Infinite-Duration Games)**.** _There exist deterministic Isomorphic-Priors algorithms that solve_ Parity Game, Mean Payoff Game, Energy Game_, and_ Simple Stochastic Game _using_ \(\widetilde{O}(km)\) _preprocessing time and_ \(\widetilde{O}(m)\) _query time._

More broadly, a similar result holds for every infinite-duration game with a well-defined value (value-determined game; see Definition A.1)

In all the results above, we compute only the optimal _values_. If the corresponding optimal _solutions_ are provided with the priors, then our algorithms can also compute an optimal solution for the query graph.

## Conditional Lower Bounds.

We observe that many known reductions can be naturally adapted to our framework to establish conditional lower bounds, which hold even when the database contains only a single prior graph (_k_=1). Specifically, we show that for many NP-hard problems, achieving both polynomial preprocessing and query times would imply the major algorithmic breakthrough of \(\mathsf{GI}\in\mathsf{P}\). Moreover, barring a breakthrough proving \(\mathsf{GI}\in\mathsf{coMA}\), these lower bounds hold even in a stronger model allowing unbounded preprocessing time.

