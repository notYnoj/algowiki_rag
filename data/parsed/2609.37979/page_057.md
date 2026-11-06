### GI preprocessing (one prior instance).

Given a single prior GI-instance _I_=(_G_<sub>1</sub>_,G_<sub>2</sub>) together with _L_=GI(_I_),<sup>38</sup> compute the corresponding \(\Pi\)-instance _X_:=_R(I_). Since _R_ is a many-one reduction, we have \(\Pi(X)=\mathsf{GI}(I)=L\),<sup>39</sup> so we can use the same value _L_ for _X_. Run \(\Pi\)-preprocessing on the singleton database {(_X,L_)} to obtain a data structure _D_.

### GI query.

Given a query GI-instance _J_, compute the \(\Pi\)-instance _Y_:=_R(J_) and query the \(\Pi\)-algorithm to get

\(z:=\mathsf{Query}_\Pi(D,Y)\in\{0,1,\perp\}.\)

Output _z_.

### Correctness.

If \(J\cong I\), then by isomorphism preservation \(Y\cong X\), hence the query is matching and the \(\Pi\)-algorithm must output \(z=\Pi(Y)=\mathsf{GI}(J)\), so we output the correct answer. If \(J\unknown\cong I\), then either the \(\Pi\)-algorithm outputs \(\Pi(Y)\) or \(\perp\); in either case, the above rule outputs the correct value for GI(_J_) or \(\perp\), both are correct outputs for _J_ in the Isomorphic-Priors model.

Thus we obtain a GI solver in the Isomorphic-Priors model with a polynomial-size data structure, contradicting Lemma 9.7 unless \(\mathsf{GI}\in\mathsf{coMA}\).

_Proof of Theorem 9.3._ Fix \(\Pi\in\mathcal{H}\) and assume for contradiction that \(\Pi\) can be solved in the Isomorphic-Priors model with preprocessing time polynomial in _k_ and _n_ and query time polynomial in _n_, even for _k_=1.

By Theorem 9.14, the promise problem Iso-\(\Pi\) is GI-hard. Applying Lemma Lemma 9.24, we conclude that \(\mathsf{GI}\in\mathsf{P}\).

Taking the contrapositive, unless \(\mathsf{GI}\in\mathsf{P}\) no such Isomorphic-Priors model algorithm for \(\Pi\) exists (even for _k_=1). Since \(\Pi\) was arbitrary in the set H, the claim follows for all three problems.

_Proof of Theorem 9.4._ Fix \(\Pi\in\mathcal{H}\) and assume for contradiction that \(\Pi\) can be solved in the Isomorphic-Priors model with a data structure of size poly(_k,n_).

By Lemma 9.25, it suffices to show that \(\mathsf{GI}\le_p^\cong\Pi\). For \(\Pi=\mathsf{IS}\) this holds by Lemma 9.15, and for \(\Pi=\mathsf{SAT}\) it holds by Lemma 9.16. For \(\Pi=\mathsf{MaxCut}\), we have \(\mathsf{GI}\le_p^\cong\mathsf{IS}\) by Lemma 9.15 and \(\mathsf{IS}\le_p^\cong\mathsf{MaxCut}\) by Lemma 9.17; by composition of isomorphism-preserving reductions, \(\mathsf{GI}\le_p^\cong\mathsf{MaxCut}\).

Hence in all three cases \(\mathsf{GI}\le_p^\cong\Pi\), and Lemma 9.25 implies \(\mathsf{GI}\in\mathsf{coMA}\), contradicting the assumption. Therefore, unless \(\mathsf{GI}\in\mathsf{coMA}\), no such polynomial-size data structure algorithm for \(\Pi\) exists (even for _k_=1).

## 9.6 Proof of Hardness for Gap-Max-_k_-Coverage

In this section, we show that Max-_k_-Coverage cannot be approximated better than (1-1_/e_) in our model, unless Max 3-SAT can be approximated arbitrarily well in our model. We achieve this by first observing that Feige’s _k_-prover system works for general Max 3-SAT and is not limited to bounded-occurrences. This is necessary because bounded occurrences would imply that the underlying isomorphism problem can be solved fast. We then go on and show that this implies a isomorphism-preserving reduction.

**Lemma 9.26** (Feige’s _k_-prover system for general Max 3-SAT)**.** _Consider the k-prover proof system of Section 2.3 in \[Fei98\] applied to an arbitrary 3CNF formula_ \(\phi\) _(no bounded-occurrence assumption). Let_ \(\varepsilon\in(0,1)\).

<sup>38</sup>That is, _L_=1 if \(G_1\cong G_2\) and zero, otherwise. <sup>39</sup>Here, \(\Pi(x)=1\) if \(x\in\Pi\) and zero otherwise.

