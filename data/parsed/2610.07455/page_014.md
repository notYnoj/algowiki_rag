\(\varepsilon)\text{unsatval}_I(\alpha)\text{for every assignment}\alpha\text{. As we show in Corollary 6.2, running the sparsifier with a slightly smaller error and minimizing these inequalities gives a}(1+\varepsilon)\text{-approximation to OPT}_\mathrm{min}(I)\text{.}\)

In the streaming model, the constraints arrive one at a time in an arbitrary order, and the algorithm makes one pass over this insertion-only stream. The domain and relation are fixed and are not part of the stream. We use _n_ for the number of variables and _m_ for the stream length. There is no restriction on the update time or on the time used after the stream. We measure only the number of stored bits.

Unless stated otherwise, a randomized algorithm must be correct with probability at least 2/3 on every input. We write SPACE(\(\Pi\)) for the minimum worst-case space of such a one-pass algorithm for a problem \(\Pi\). Upper bounds described as deterministic use no randomness, while all lower bounds also apply to randomized bounded-error algorithms.

## 3.3 Non-redundancy

Non-redundancy measures how many constraints can be independently necessary for satisfiability. Let _I_ be an unweighted _R_-instance and let \(C\in I\). We call _C redundant in I_ if every assignment satisfying all constraints obtained by removing this occurrence of _C_ also satisfies _C_. Otherwise, there is an assignment that violates _C_ and satisfies every other constraint of _I_. We call such an assignment a _witness for C_. The instance _I_ is _nonredundant_ if every one of its constraints has a witness.

We define NRD_<sub>n</sub>(R_) to be the maximum number of constraints in a nonredundant _R_-instance on at most _n_ variables.

**Example 3.2.** For the relation CUT, every forest gives a nonredundant instance. Fix an edge and remove it. The two endpoints are now in different components. We can properly 2-color each component and choose the colors so that these endpoints receive the same value. This assignment violates the removed edge and satisfies every other edge, so it is a witness for that edge.

We will use the following elementary lower bound to account for the space needed to store an assignment.

**Observation 3.3.** _If_ \(R\unknown D^k\) _is nonempty, then_ \(\mathsf{NRD}_n(R)=\Omega_R(n)\).

_Proof._ Choose a tuple \(r\in R\) and a tuple \(u\in D^k\backslash R\). Partition \(k\lfloor n/k\rfloor\) variables into disjoint ordered scopes of size _k_, and put one _R_-constraint on each scope. To witness one chosen constraint, assign the tuple _u_ to its scope and the tuple _r_ to every other scope. The chosen constraint is violated and all other constraints are satisfied. The resulting instance is nonredundant and has \(\lfloor n/k\rfloor=\Omega_R(n)\) constraints.

By definition, a non-trivial relation is nonempty and is not equal to _D<sup>k</sup>_. Thus the observation shows that non-redundancy is at least linear for every non-trivial fixed relation, although it may be much larger. Our satisfiability and minimization results depend on its value for the core of _R_, which we define next.

## 3.4 Cores, automorphisms, and hard pinnings

We now define the core of a relation. A map \(\sigma:D\rightarrow D\) is an _endomorphism_ of _R_ if applying \(\sigma\) to every coordinate of a tuple in _R_ always gives another tuple in _R_. Equivalently, \(\sigma(R)\subseteq R\). An endomorphism is an _automorphism_ if it is a bijection. In this case \(\sigma(R)=R\). We write Aut(_R_) for the set of automorphisms of _R_.

