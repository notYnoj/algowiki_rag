## 5 Conclusion and open problems

We added two members to the club of PLS-complete problems with lexicographic costs: LocalLexMax-4-SAT and Abelian Polm. We believe that as a point for further reductions, LocalLexMax-4-SAT is better than Flip due to its simple structure while preserving the lexicographical costs. We demonstrated this by showing that finding approximate Nash equilibria is PLS-complete, and the simple structure of lexicographic costs allowed us to use nice continuous delay functions. Additionally, all reductions in this work are tight (see Section D).

Multiple open problems remain: While LocalLexMax-_k_-SAT is PLS-complete for _k_=4 and in P for _k_=2, the case _k_=3 is open. Our reduction cannot easily be changed to produce 3-clauses: we already need 3-clauses to model the correct evaluation of a circuit (2-clauses don’t suffice because 2-SAT is in NL and circuit evaluation is P-complete); and then we need an additional variable _f_ to temporarily de-activate one copy of the circuit. It is also open whether LocalMax-4-SAT stays PLS-complete if every variable appears a bounded number of times.

Secondly, in our reduction and the reduction in [20] for Polm the number of permutations grows with the input size. What happens if we only have a fixed number of permutations _k_? For _k_=1 this is in P [14, 20] but even for _k_=2 it is open.

Thirdly, what happens if the delay functions in the congestion game are polynomials of bounded degree _d_ (and perhaps weighted)? While upper bounds are known, there are no lower bounds known for those \(\alpha\) where the problem is in PLS[4, 5, 11]. In [5] it is shown that for \(\alpha\in\mathcal{O}(\frac{d}{lnd})\) deciding the existence of an approximate Nash-equilibrium is NP-hard if the game is weighted. LocalLexMax-4-SAT might be a helpful intermediate problem to reach this target.

Lastly, another interesting PLS problem with lexicographic costs might be the traveling salesman problem as here it is also not feasible to check if there exists a solution using a set of edges. Known reductions[12, 19] start however from Max-Cut and are therefore not adaptable for lexicographic costs.

## References

1 Heiner Ackermann, Heiko Röglin, and Berthold Vöcking. On the impact of combinatorial structure on congestion games. In _47th Annual IEEE Symposium on Foundations of Computer Science, FOCS 2006, Berkeley, California, USA, October 21-24, 2006, Proceedings_, pages 613–622. IEEE Computer Society, 2006. `doi:10.1109/FOCS.2006.55`.

2 Christoph Buchheim and Michael Jünger. Linear optimization over permutation groups. _Discret. Optim._, 2(4):308–319, 2005. URL: `https://doi.org/10.1016/j.disopt.2005.08.005`, `doi: 10.1016/J.DISOPT.2005.08.005`.

3 Ioannis Caragiannis, Angelo Fanelli, Nick Gravin, and Alexander Skopalik. Efficient computation of approximate pure nash equilibria in congestion games. In Rafail Ostrovsky, editor, _IEEE 52nd Annual Symposium on Foundations of Computer Science, FOCS 2011, Palm Springs, CA, USA, October 22-25, 2011_, pages 532–541. IEEE Computer Society, 2011. `doi:10.1109/FOCS.2011.50`.

4 Ioannis Caragiannis, Angelo Fanelli, Nick Gravin, and Alexander Skopalik. Approximate pure nash equilibria in weighted congestion games: Existence, efficient computation, and structure. _ACM Trans. Economics and Comput._, 3(1):2:1–2:32, 2015. `doi:10.1145/2614687`.

5 George Christodoulou, Martin Gairing, Yiannis Giannakopoulos, Diogo Poças, and Clara Waldmann. Existence and complexity of approximate equilibria in weighted congestion games.

