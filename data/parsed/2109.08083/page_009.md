<tbc>(both for the standard and toroidal problems) for some values of _n_. Luria went on to give a stronger conjecture than that of Rivin, Vardi and Zimmerman in the toroidal case, that when \(n\equiv 1,5mod6\) we have \(T(n)=((1+o(1))\frac{n}{e^3})^n\). In fact, our main result is precisely that this conjecture is true.

Theorem 1.2. _Let_ \(n\equiv 1,5mod6\)_. Then_

\(T(n)=\left((1+o(1))\frac{n}{e^3}\right)^n.\)

Theorem 1.2 both settles the conjectures of Rivin, Vardi and Zimmerman, and of Luria concerning the toroidal problem, as well as answering the original question of Pólya asymptotically in the exponent. As far we are aware, there are no other known bounds for the toroidal problem for general \(n\equiv 1,5mod6\) or for any infinite subsequence. In particular, until now, there was no non-trivial lower bound on the number of solutions to the toroidal _n_-queens problem that held for all \(n\equiv 1,5mod6\) (i.e. all _n_ for which at least one solution exists), and due to Luria’s upper bound, our work here on the lower bound asymptotically settles the problem completely.

We also prove that the bound on _T(n_) given above when \(n\equiv 1,5mod6\) yields a lower bound for all _n_ in the classical case.

Theorem 1.3. _For_ \(n\in\mathbb{N}\) _sufficiently large we have that_

\(Q(n)\ge\left((1+o(1))\frac{n}{e^3}\right)^n.\)

_Furthermore, this lower bound only considers configurations with at most six pairs of queens that attack toroidally._

This result, along with Theorem 1.2 and the upper bound of Luria settles Conjecture 1.1 completely (both the classical and toroidal cases). Independently, very recently, Luria and Simkin [**40**] also released a preprint obtaining the same lower bound on _Q(n_), thereby also settling the conjecture in the classical case. Following on from this, Simkin [**54**] subsequently released a preprint improving both the lower and upper bounds for the classical problem, with the main result as follows:

Theorem 1.4 ([**54**]). _There exists a constant_ 1.94_\<c\<_1.9449 _such that_

\(Q(n)=\left((1+o(1))\frac{n}{e^c}\right)^n.\)

This result gets significantly closer to the ‘truth’ for the classical problem and is a big breakthrough concerning the classical case. However neither of these recent results yields headway on the toroidal problem for any _n_ and nor do the methods shed any new light on how to solve the toroidal problem. We defer mention of the methods used for these recent lower bounds to discuss alongside the methods we use to prove Theorem 1.2.

The _n_-queens problem (both the classical and toroidal versions) are not only of recreational interest, but their importance goes well beyond this. As well as the algebraic formulation discussed above, there are various combinatorial reformulations that we discuss in the next section that demonstrate its abstract mathematical importance. Beyond this, the problem is useful in the discussion of mathematical optimisation and in design and analysis of algorithms, as well as having various

