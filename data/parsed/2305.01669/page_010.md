2. _Preaccumulation terminates._

_Proof._

1. Equation (4.1) is invariant under preaccumulation.<tbc>

2. The cumulative sum of all paths connecting sources with sinks decreases monotonically under preaccumulation. Hence, full preaccumulation yields the bipartite DAG that represents \(F'\).

Definition 4.7 (Bipartite DAG Splitting). _A_ bipartite DAG _G representing a local Jacobian_ \(F'_j\in\mathbb{R}^{m\times n}\) _is_ split _by replacing it with a layered tripartite DAG representing the matrix products_ \(F'\cdot I_n\)_, if_ \(n\le m\)_, or_ \(I_m\cdot F'\)_, otherwise._

The condition \(n\le m\) could be omitted if numerical correctness was our sole objective. However, aiming for maximum sparsity we keep the number of newly generated edges as low as possible. Further implications of the two choices are the subject of ongoing research.

Lemma 4.8. _Let a DAG G induce an invertible Jacobian_ \(F'\in\mathbb{R}^{n\times n}\) _under the chain rule of differentiation as in Lemma 4.1._

1. _The Jacobian is invariant under bipartite DAG splitting as in Definition 4.7._<tbc>

2. _If repeated bipartite DAG splitting yields a uniformly layered DAG as in Definition 2.4, then the local Jacobians of each layer are invertible._

_Proof._

1. Equation (4.1) is invariant under bipartite DAG splitting.<tbc>

2. Let the uniformly layered DAG have depth _q_. Equation (4.1) yields \(F'=F'_q\cdot\dots\cdot F'_1\) and hence \((F')^{-1}=(F'_1)^{-1}\cdot\dots\cdot(F'_q)^{-1}\) implying invertibility of all \(F'_j\), _j_=1_,...,q_.

**4.3. Combinatorics.** The combinatorial Matrix-Free Newton Step problem to be formulated in its decision version next turns out to be computationally intractable.

Problem 1 (Matrix-Free Newton Step).<br>
instance: _An invertible DAG and an integer_ \(K\ge 0\).<br>
question: _Can the corresponding Newton step be evaluated with at most K flops_4?

Theorem 4.9. Matrix-Free Newton Step _is NP-complete._

_Proof._ The proof of NP-completeness of the Adjoint Computation problem presented in [16] reduces Ensemble Computation [5] to uniformly layered DAGs representing matrix chain products over diagonal Jacobians \(\in\mathbb{R}^{n\times n}\) as<tbc>

\(F'=F'_q\cdot\dots\cdot F'_1\in\mathbb{R}^{n\times n}.\)

<tbc>A corresponding Newton step becomes equal to

\((F')^{-1}\cdot y=(F'_q\cdot\dots\cdot F'_1)^{-1}\cdot y=(F'_1)^{-1}\cdot\dots\cdot(F'_q)^{-1}\cdot y.\)

The "accumulate first, then factorize" method turns out to be superior as \(F'\) remains a diagonal matrix. Its inversion adds a constant offset of _n_ (reciprocals) to the flop count of any given instance of Adjoint Computation. A solution for Matrix-Free

4floating-point operations

