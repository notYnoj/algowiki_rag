Unlike for the other cases, for locally stable matching we cannot guarantee consistent generation rules if we increase the number of matching edges. The same holds for lookahead _\>_2. In both cases the accessibility of an edge might depend on more than one matching edge. There are exponential lower bounds in [16,19] for those extensions which proves that it is impossible to find an embedding with consistent rules even with the help of auxiliary constructions.

## 2.2 Reaching a Given Matching

In this section we consider the problem of deciding reachability of a _given_ stable matching from a given initial state. We first show that for correlated coalition formation games with constraints and consistent rules, this problem is in NP. If we can reach it and there exists a sequence, then there always exists a polynomial- size certificate due to the following result.

**Theorem 2.** _In a correlated coalition formation game with constraints and consistent generation and domination rules, for every coalition structure_ \(\unknown\) _that is reachable from an initial state_ \(\unknown_0\) _through a sequence of improvement steps, there is also a sequence of polynomially many improvement steps from_ \(\unknown_0\) _to_ \(\unknown\)_._

For the proof we analyze an arbitrary sequence of improvement steps from \(\unknown_0\) to \(\unknown\) and show that, if the sequence is too long, there are unnecessary steps, that is, coalitions are created and deleted without making a difference for the final outcome. By identifying and removing those superfluous steps we can reduce every sequence to one of polynomial length. The detailed proof can be found in the appendix.

For locally stable matching, the problem of reaching a given locally stable matching from a given initial matching is known to be NP-complete [19]. Here we provide a generic reduction that shows NP-completeness for socially, locally, considerate, and friendship matching, even in the two-sided case. Surprisingly, it also applies to ordinary two-sided stable matching games that have either correlated preferences with ties, or non-correlated strict preferences. Observe that the problem is trivially solvable for ordinary stable matching and correlated preferences without ties, as in this case there is a unique stable matching that can always be reached using the greedy construction algorithm [2].

**Theorem 3.** _It is_ NP_-complete to decide if for a given matching game, initial matching_ \(\unknown_0\) _and stable matching_ \(\unknown\)_, there is a sequence of improvement steps leading form_ \(\unknown_0\) _to_ \(\unknown\)_. This holds even for bipartite games with strict correlated preferences in the case of_

1. _socially stable matching and locally stable matching,_<tbc>

2. _considerate matching, and_<tbc>

3. _friendship matching for symmetric_ \(\alpha\)_-values in_ [0,1]._

_In addition, it holds for ordinary bipartite stable matching in the case of_

4. _correlated preferences with ties,_<tbc>

5. _strict preferences._<tbc>

