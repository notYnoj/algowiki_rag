## 9.5 Hardness in the Isomorphism-Priors Model

We show that the Gl-hardness of Iso-\(\Pi\) implies that \(\Pi\) cannot be solved in our model with fast preprocessing, unless \(\mathsf{Gl}\in\mathsf{P}\).

**Lemma 9.24.** _Let_ \(\Pi\) _be a decision problem such that_ Iso-\(\Pi\) _is_ Gl_-hard. Unless_ \(\mathsf{Gl}\in\mathsf{P}\), \(\Pi\) _cannot be solved inside the Isomorphic-Priors model with k prior instances each of size at most n with preprocessing and query time polynomial in n, even when k_=1 _prior instance is given._

_Proof._ Assume that there exists an algorithm for \(\Pi\) in the Isomorphic-Priors model with preprocessing time poly_<sub>k</sub>(n_) and query time poly_<sub>k</sub>(n_), and that it is correct on all valid queries. In particular, consider the case _k_=1.

We show that this implies Iso-\(\Pi\in\mathsf{P}\). Given an input (_G,H_) to Iso-\(\Pi\), run the model’s preprocessing phase on the single prior instance _G_ together with \(L=\Pi(G)\) (i.e., _L_=1 if any only if _G_ is a YES-instances), obtaining a data structure _D_. Then query the model on _H_ and obtain an output

\(z:=\mathsf{Query}(D,H)\in\{0,1,\perp\}.\)

We decide Iso-\(\Pi\) by outputting YES iff _z_=1, and NO otherwise (in particular, treat \(z=\perp\) as NO). Correctness holds under the promise defining Iso-\(\Pi\):

• If \((G,H)\in\text{Iso-}\Pi_\mathrm{YES}\), then \(G\in\Pi\) and \(H\cong G\). Since \(\Pi\) is invariant under isomorphism, \(\Pi(H)=\Pi(G)=1\), so the model must output \(z=\Pi(H)=1\), and we accept.<tbc>

• If \((G,H)\in\text{Iso-}\Pi_\mathrm{NO}\), then \(G\in\Pi\) and \(H\notin\Pi\), i.e. \(\Pi(H)=0\). By correctness of the model algorithm on non-matching queries, on input _H_ it outputs either \(z=\Pi(H)=0\) or the special symbol \(\perp\). In both cases we reject.

The running time is polynomial, since preprocessing on one instance and one query are polynomial in _n_.

Thus Iso-\(\Pi\in\mathsf{P}\). Since by assumption Iso-\(\Pi\) is Gl-hard, this implies \(\mathsf{Gl}\in\mathsf{P}\). Therefore, unless \(\mathsf{Gl}\in\mathsf{P}\), no such algorithm exists for \(\Pi\) in the Isomorphic-Priors model (even for _k_=1).

We show that a problem, that can be reduced to Gl with an isomorphism-preserving reduction, cannot be solved in our model with a small data structure, unless \(\mathsf{Gl}\in\mathsf{coMA}\).

**Lemma 9.25.** _Let_ \(\Pi\) _be a decision problem such that_ \(\mathsf{Gl}\le_p^\cong\Pi\)_. Assume_ \(\mathsf{Gl}\notin\mathsf{coMA}\)_. Then_ \(\Pi\) _cannot be solved inside the Isomorphic-Priors model with k prior instances each of size at most n with a data structure of size polynomial in n and query time polynomial in n, even when k_=1 _prior instance is given._

_Proof._ Assume for contradiction that \(\Pi\) can be solved in the Isomorphic-Priors model with preprocessing and query time polynomial and with a data structure of size poly_<sub>k</sub>(n_).

Since \(\mathsf{Gl}\le_p^\cong\Pi\), there exists an isomorphism-preserving many-one reduction _R_ from Gl-instances to \(\Pi\)-instances such that for every Gl-instance _I_,

\(I\in\mathsf{Gl}\Longleftrightarrow R(I)\in\Pi.\)

We build an algorithm that solves Gl in the Isomorphic-Priors model with a polynomial-size data structure (already for _k_=1), contradicting Lemma 9.7 unless \(\mathsf{Gl}\in\mathsf{coMA}\).

