**Theorem 5.1** (Satisfiability)**.** _Let_ \(R\subseteq D^k\) _be a fixed non-trivial relation and let R<sup>⋆</sup>_=core(_R). The following statements hold._

(_i)_ _there is a deterministic one-pass streaming algorithm for_ SAT(_R_) _using O<sub>R</sub>_(NRD_<sub>n</sub>(R<sup>⋆</sup>_)log_n_) _bits of space._<tbc>

_(ii)_ _every randomized bounded-error one-pass streaming algorithm for_ SAT(_R_) _uses_ \(\Omega_R(\mathsf{NRD}_n(R^\star))\) _bits of space._

_Consequently,_

\(\Omega_R(\mathsf{NRD}_n(\mathsf{core}(R)))\le\mathsf{SPACE}(\mathsf{SAT}(R))\le O_R(\mathsf{NRD}_n(\mathsf{core}(R))\mathrm{log}n).\)

We prove the two bounds for a core relation and then use Lemma 4.2 to obtain the theorem for an arbitrary relation.

The upper bound is the following known consequence of non-redundancy \[SV26a, Theorem 1(a)\].

**Lemma 5.2** (Satisfiability upper bound)**.** _\[SV26a, Theorem 1(a)\] If R is a core relation, then_ SAT(_R_) _has a deterministic one-pass streaming algorithm using O<sub>R</sub>_(NRD_<sub>n</sub>(R_)log_n_) _bits of space._

The algorithm maintains a nonredundant subinstance with exactly the same satisfying assignments as the current prefix of the stream. When a constraint arrives, the algorithm adds it and repeatedly removes any constraint whose deletion does not change the set of satisfying assignments. The stored instance therefore has at most NRD_<sub>n</sub>(R_) constraints. Since _R_ is fixed, each constraint is specified by its scope using _O<sub>R</sub>_(log_n_) bits. There is no update-time restriction, so redundancy and final satisfiability can be checked by trying all assignments using _O<sub>R</sub>(n_) additional bits. For a non-trivial relation, \(\mathsf{NRD}_n(R)=\Omega_R(n)\), so this is within the stated space bound. For a trivial relation, satisfiability is immediate.

It remains to prove the matching lower bound. The reduction uses the witnesses of a nonredundant instance in the way suggested by the definition of non-redundancy.

## 5.1 Lower bound for a core relation

In this subsection, we prove the following main theorem.

**Theorem 5.3** (Satisfiability lower bound)**.** _Let_ \(R\subseteq D^k\) _be a core relation. Every randomized bounded-error one-pass streaming algorithm for_ SAT(_R_) _uses_ \(\Omega_R(\mathsf{NRD}_n(R))\) _bits of space._

_Proof._ The idea is simple. Alice streams a subinstance of a maximum nonredundant instance. Bob takes the witness for his queried constraint, meaning an assignment that violates this constraint and satisfies every other constraint in the nonredundant instance, and uses Lemma 4.4 to force that witness up to one automorphism. Since automorphisms preserve which constraints are satisfied, the resulting instance tells Bob whether Alice streamed the queried constraint.

Let _c<sub>R</sub>_ be a constant such that the hard-pinning instance in Lemma 4.4 always uses at most _c<sub>R</sub>_ additional variables. Fix a sufficiently large number _n_, put _n_<sub>0</sub>=_n-c<sub>R</sub>_, and let _F_={_C_<sub>1</sub>_,...,C<sub>M</sub>_} be a nonredundant _R_-instance on _n_<sub>0</sub> variables with _M_=NRD<sub>_n_<sub>0</sub></sub>(_R_). If _M_=0, the claimed lower bound is empty, so assume \(M\ge 1\). For every \(i\in[M]\), choose a witness assignment _s<sub>i</sub>_ that violates _C<sub>i</sub>_ and satisfies every _C<sub>j</sub>_ with \(j\neq i\).

Suppose that a randomized one-pass streaming algorithm decides SAT(_R_) on _n_ variables using _S(n_) bits of space. We use it to solve INDEX_<sub>M</sub>_. Alice receives a string \(x\in\{0,1\}^M\), and Bob receives an index \(i\in[M]\). Alice starts the streaming algorithm and streams _C<sub>j</sub>_ exactly when _x<sub>j</sub>_=1. She<tbc>

