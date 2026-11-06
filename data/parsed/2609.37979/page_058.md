1. _If_ \(\phi\) _is satisfiable, then there is a prover strategy that causes the verifier to always_ strongly _accept._<tbc>

_2._ _If_ \(OPT(\phi)\le 1-\varepsilon\) _(i.e., no assignment satisfies more than a_ \((1-\varepsilon)\)_-fraction of clauses), then the verifier_ weakly _accepts with probability at most_ \(k^2\cdot 2^{-c\ell}\)_, where c\>_0 _depends only on_ \(\varepsilon\) _(and on the constant answer length), and_ \(\ell\) _is the repetition parameter of the verifier._

_Proof._ The verifier samples \(\ell\) clauses uniformly and independently and chooses one distinguished variable per clause, exactly as in \[Fei98, Sec. 2.3\]. The weak predicate is "some pair of provers is consistent" (on the induced assignment to the \(\ell\) distinguished-variable positions), and the strong predicate is "every pair is consistent" \[Fei98, Sec. 2.3\].

## Completeness.

If \(\phi\) is satisfiable, fix any satisfying assignment and let every prover answer consistently with it. Then the induced assignments to the distinguished-variable positions are identical for all provers, so the verifier always strongly accepts (identical to Feige’s argument) \[Fei98, Lem. 2.3.1\].

## Soundness: reducing to two provers and parallel repetition.

Assume \(OPT(\phi)\le 1-\varepsilon\) and suppose the verifier weakly accepts with probability at least \(\delta\). Then there exist two provers whose answers are consistent with probability at least \(\delta/k^2\) (by averaging over the \(\genfrac(){pt}{2}{k}{2}\) pairs), exactly as in Feige \[Fei98, Lem. 2.3.1\]. By the Hamming-distance property of the code used to distribute queries, there are at least \(\ell/6\) coordinates in which one of these provers receives a clause and the other receives the distinguished variable from that clause (again exactly as in Feige) \[Fei98, Lem. 2.3.1\]. Fix the questions on the remaining \(5\ell/6\) coordinates to maximize acceptance; the acceptance probability remains at least \(\delta/k^2\). Now ignore those fixed coordinates. This yields a strategy for a two-prover system that succeeds with probability at least \(\delta/k^2\) on \(\ell/6\) independent coordinates, i.e., on \(\ell/6\) parallel repetitions of the underlying two-prover test.

## Base two-prover error does not need bounded occurrence.

Feige’s Proposition 2.2.1 (stated for 3CNF-5) bounds the optimal acceptance probability of the base two-prover test by \(1-\varepsilon/3\) when at most a \((1-\varepsilon)\)-fraction of clauses are simultaneously satisfiable \[Fei98, Prop. 2.2.1\]. Its proof uses only: (i) the second prover’s strategy induces a global assignment _x_, (ii) a random clause is unsatisfied by _x_ with probability at least \(\varepsilon\), and (iii) conditioned on such a clause, if the first prover makes it satisfied by changing at least one literal, then a uniformly random distinguished variable from that clause disagrees with probability at least 1/3. This argument does not depend on how many times a variable appears in the formula (variables may occur unboundedly often).

Hence the base two-prover system has constant error at most \(1-\varepsilon/3\), independent of _n_ and of occurrence bounds.

## Parallel repetition.

By Raz’s parallel repetition theorem (Feige’s Theorem 2.2.2), repeating a one-round two-prover system _t_ times independently in parallel reduces the acceptance probability to at most 2<sup>-_ct_</sup> for some constant _c\>_0 that depends only on the base error and the constant answer length \[Fei98, Thm. 2.2.2\]. Taking \(t=\ell/6\), we obtain

\(\delta/k^2\le 2^{-c\ell},\)

after renaming constants, and thus \(\delta\le k^2\cdot 2^{-c\ell}\).

This proves the claimed soundness bound for arbitrary 3CNF formulas, without any bounded- occurrence assumption.

