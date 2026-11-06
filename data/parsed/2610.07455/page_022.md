<tbc>then sends the _S(n_)-bit memory state to Bob. Bob resumes the algorithm from this state and appends the hard-pinning instance _P<sub>s<sub>i</sub></sub>_ from Lemma 4.4. The final instance uses at most _n_<sub>0</sub>+_c<sub>R</sub>=n_ variables.

We claim that the final instance is satisfiable if and only if _x<sub>i</sub>_=0. Suppose first that _x<sub>i</sub>_=0. The assignment _s<sub>i</sub>_ satisfies every constraint streamed by Alice, and it extends to a satisfying assignment of _P<sub>s<sub>i</sub></sub>_ by using the identity automorphism in Lemma 4.4. Hence the final instance is satisfiable.

Now suppose that _x<sub>i</sub>_=1. Any assignment satisfying _P<sub>s<sub>i</sub></sub>_ restricts on the original variables to \(\sigma\circ s_i\) for some \(\sigma\in\mathrm{Aut}(R)\). The assignment _s<sub>i</sub>_ violates _C<sub>i</sub>_, so Observation 4.1 implies that \(\sigma\circ s_i\) also violates _C<sub>i</sub>_. Since Alice streamed _C<sub>i</sub>_, no assignment can satisfy the final instance. This proves the claim.

Alice and Bob use the random tape of the streaming algorithm as public randomness. Bob outputs the complement of the algorithm’s answer, which recovers _x<sub>i</sub>_ with the same constant error probability. We have therefore obtained a public-coin one-way protocol for INDEX_<sub>M</sub>_ with _S(n_) bits of communication. By Lemma 3.7, \(S(n)=\Omega(M)=\Omega(\mathsf{NRD}_{n_0}(R))\).

Finally, we need to prove that removing a constant number of variables changes non-redundancy by at most a constant factor depending only on _R_. We start with a maximum nonredundant instance on at most _n_ variables and add unused variables so that its variable set has size exactly _n_. Choose a uniformly random set of _n_<sub>0</sub>=_n-c<sub>R</sub>_ variables. A constraint uses at most _k_ distinct variables, so for all sufficiently large _n_ the probability that all variables in its scope are chosen is bounded below by a positive constant dependent only on _R_. Some choice therefore keeps \(\Omega_R(\mathsf{NRD}_n(R))\) constraints. These constraints remain nonredundant because their original witnesses can be restricted to the chosen variables. Thus \(\mathsf{NRD}_{n_0}(R)=\Omega_R(\mathsf{NRD}_n(R))\), and consequently \(S(n)=\Omega_R(\mathsf{NRD}_n(R))\).

We now combine the core reduction with the two core relation bounds to conclude the proof of Theorem 5.1.

_Proof of Theorem 5.1._ By Lemma 4.2, deciding SAT(_R_) has the same streaming space complexity as deciding SAT(_R<sup>⋆</sup>_). Apply Lemma 5.2 to _R<sup>⋆</sup>_ for the deterministic upper bound and Theorem 5.3 to _R<sup>⋆</sup>_ for the randomized lower bound. This gives both parts of the theorem and the claimed characterization.

Thus the streaming complexity of satisfiability is governed, up to the logarithmic factor in the upper bound, by the non-redundancy of the core relation.

## 6 Sparsification and Min-CSP

We first state our sparsification result for CSPs that are revealed in streams.

**Theorem 6.1** (Sparsification)**.** _Let_ \(R\subseteq D^k\) _be a fixed non-trivial relation and let_ \(\varepsilon>0\)_. There is a deterministic one-pass streaming algorithm which, given an unweighted stream of constraints defining an R-instance I on n variables and with stream length m, stores a weighted subinstance_ \(H\subseteq I\) _such that for every assignment_ \(\alpha\), \(\mathrm{unsatval}_H(\alpha)\in(1\pm\varepsilon)\mathrm{unsatval}_I(\alpha)\)_. The space used is_ \(O_{R,\varepsilon}(\mathsf{NRD}_n(R)\cdot\mathrm{polylog}(n,m,1/\varepsilon))\).

As an immediate corollary, we obtain the following.

**Corollary 6.2** (Min-CSP)**.** _Let_ \(R\subseteq D^k\) _be a fixed non-trivial relation, let R<sup>⋆</sup>_=core(_R), and let_ \(\varepsilon>0\).

