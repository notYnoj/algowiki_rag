Then a CSP with literals over _R_ is exactly a positive CSP over \(\Gamma_R^\mathrm{lit}\). We write \(\mathsf{NRD}_n^+(\Gamma)\) for the largest number of constraints in a nonredundant positive \(\Gamma\)-instance on _n_ variables. Similarly, \(\mathsf{NRD}_n^\mathrm{lit}(R)\) denotes non-redundancy in the literal model over _R_.

For a constraint language \(\Gamma\), let \(\mathsf{SAT}(\Gamma)\) denote satisfiability for positive \(\Gamma\)-instances. The following corollary records the language version of our satisfiability characterization.

**Corollary A.1** (Satisfiability for constraint languages)**.** _For every fixed finite constraint language_ \(\Gamma\),

\(\Omega_\Gamma\big(\mathsf{NRD}_n^+(\mathrm{core}(\Gamma))\big)\le\mathsf{SPACE}(\mathsf{SAT}(\Gamma))\le O_\Gamma\big((\mathsf{NRD}_n^+(\mathrm{core}(\Gamma))+1)\mathrm{log}(n+1)\big).\)

_The upper bound is deterministic, and the lower bound holds for randomized bounded-error one-pass algorithms._

_Proof._ The core reduction replaces each relation in \(\Gamma\) by its restriction to the core domain and preserves satisfiability and streaming space exactly, as in Lemma 4.2. For a core language, the upper bound maintains a nonredundant subinstance with the same satisfying assignments, exactly as in Lemma 5.2. If the language contains a nonempty proper relation, disjoint constraints from this relation show that its non-redundancy is \(\Omega_\Gamma(n)\), so the space needed to try assignments is within the stated bound. Otherwise every relation is empty or full, and satisfiability can be decided by checking whether an empty-relation constraint appears. For the lower bound, the hard-pinning construction and the INDEX reduction in Theorem 5.3 work with constraints from any relation in the core language. This proves the two bounds.

The following lemma shows that passing to the core does not change non-redundancy for any shift-closed language.

**Lemma A.2.** _Let_ \(\Gamma\) _be a finite constraint language over D_=Z_<sub>q</sub> that is closed under coordinatewise shifts. Then_ \(\mathsf{NRD}_n^+(\Gamma)=\mathsf{NRD}_n^+(\mathrm{core}(\Gamma))\).

_Proof._ First, we may assume that every relation in \(\Gamma\) is nonempty. Empty relations are fixed by every shift and every endomorphism. Moreover, if a nonredundant instance contains an empty-relation constraint, then it can contain no other constraint. Empty relations therefore give the same trivial size-one instances before and after passing to the core, so we may discard them. If no relations remain, the statement is immediate.

For a relation _S_ and a coordinate _i_, let _S+de<sub>i</sub>_ denote the relation obtained by adding _d_ to coordinate _i_, where _e<sub>i</sub>_ is the _i_th unit vector. Define

\(H:=\{d\in D:S+de_i=S\text{for every}S\in\Gamma\text{and every coordinate}i\}.\)

Thus _H_ is the subgroup of shifts that are invisible to every relation.

Choose one representative from each coset of _H_, let \(C\subseteq D\) be the set of representatives, and let \(\rho:D\rightarrow C\) map every element to the representative of its coset. Since \(\rho(a)-a\in H\), for every \(S\in\Gamma\) and every tuple _x_,

\(x\in S\Longleftrightarrow\rho(x)\in S.\) (A.3)

In particular, \(\rho\) is an endomorphism.

We claim that \(\rho\) is a core endomorphism. Let \(h:D\rightarrow D\) be any endomorphism and write \(\delta(a):=h(a)-a\). We show that

\(\delta(a)-\delta(b)\in H\text{for all}a,b\in D.\) (A.4)

