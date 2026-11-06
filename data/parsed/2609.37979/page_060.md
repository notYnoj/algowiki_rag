## Step 2: Gap correctness (black-box).

We argue informally, following Feige.

_YES case._ If \(OPT(\Phi)=1\), then by Lemma 9.26 there is a prover strategy that causes the verifier to _strongly_ accept on every random string. Fix that strategy and choose the \(k'\) sets that correspond to the provers’ answers on all possible questions (one answer per question per prover, hence _k<sup>Q</sup>_ choices total). For each _r_, strong acceptance implies that the induced strings \(p_r(\cdot)\) are consistent across provers, and therefore the chosen sets cover, inside the block \(\{r\}\times B_r\), all _m_ points (because the _k_ parts of P_<sub>r,p</sub>_ partition _B<sub>r</sub>_). Hence the chosen \(k'\) sets cover all of \(U(\Phi)\), so \(OPT(R(\Phi))=1\).

_NO case._ If \(OPT(\Phi)\le 1-\varepsilon\), then by Lemma 9.26 the verifier weakly accepts with probability at most \(\delta\), where \(\delta\) can be made exponentially small in \(\ell\). Feige’s analysis of the reduction (using the partition-system lemma) shows that any family of \(k'\) sets corresponds to a (possibly inconsistent) prover strategy, and that the fraction of universe elements covered is at most \(1-1/e+O(\delta)+O(1/d)\) (cf. \[Fei98, Sec. 4-5\]). Choosing \(\ell\) and _d_ large enough as functions of \(\varepsilon\) makes the additive terms \(O(\delta)+O(1/d)\) arbitrarily small; in particular, we can choose parameters so that the covered fraction is at most \(1-1/e+\varepsilon'\). Therefore \(OPT(R(\Phi))\le 1-1/e+\varepsilon'\) in the NO case.

Altogether, \(\Phi\in\mathsf{Gap}\mathsf{Max}\mathsf{3}\mathsf{SAT}_{1,1-\varepsilon^\prime}\) implies \(R(\Phi)\in\mathsf{Gap}\mathsf{Max}\mathsf{3}\mathsf{Coverage}_{1,1-1/e+\varepsilon^\prime}\).

## Step 3: Isomorphism preservation.

Let \(\alpha:\Phi\rightarrow\Phi'\) be an isomorphism of 3CNF instances (renaming variables and permuting clauses, preserving literal signs). We build an isomorphism between \(R(\Phi)=(U,\mathcal{S},k')\) and \(R(\Phi')=(U',\mathcal{S}',k')\).

The verifier’s random string \(r\in\mathcal{R}\) specifies a pattern of queries (which clause indices are chosen, which variables are distinguished, etc.). Under \(\alpha\), clause/variable identifiers are renamed, and hence each question _q_ and answer _a_ is renamed canonically to \(\alpha(q)\) and \(\alpha(a)\). Define a bijection \(\beta_U:U\rightarrow U'\) by<tbc>

\(\beta_U(r,x):=(r,x)\text{for}x\in B_r,\)

<tbc>i.e. we keep the partition-system point and randomness index, but interpret the clause/variable identifiers inside the indexing data via \(\alpha\) (equivalently: we identify R across \(\Phi\) and \(\Phi'\) by the same randomness and query pattern, differing only by renamed identifiers). Define a bijection \(\beta_\mathcal{S}:\mathcal{S}\rightarrow\mathcal{S}'\) by<tbc>

\(\beta_\mathcal{S}\big(S(q,a,i)\big):=S(\alpha(q),\alpha(a),i).\)

<tbc>By construction, for every universe element (_r,x_) and every set _S(q,a,i_), we have

\((r,x)\in S(q,a,i)\Longleftrightarrow(r,x)\in S(\alpha(q),\alpha(a),i),\)

because membership is defined solely by (i) whether _q<sub>i</sub>(r_)=_q_ and (ii) which part _B(r,p<sub>r</sub>(a),i_) is selected, and both are invariant under renaming clause/variable identifiers. Hence \((\beta_U,\beta_\mathcal{S})\) preserves incidence, so it is an isomorphism of set systems. Therefore \(R(\Phi)\cong R(\Phi')\).

## Conclusion.

The mapping \(\Phi\mapsto R(\Phi)\) is polynomial-time, isomorphism-preserving, and maps YES-instances of \(\mathsf{Gap}\mathsf{Max}\mathsf{3}\mathsf{SAT}_{1,1-\varepsilon}\) to YES-instances of \(\mathsf{Gap}\mathsf{Max}\mathsf{3}\mathsf{Coverage}_{1,1-1/e+\varepsilon^\prime}\) and NO- instances to NO-instances of \(\mathsf{Gap}\mathsf{Max}\mathsf{3}\mathsf{Coverage}_{1,1-1/e+\varepsilon^\prime}\). This proves the lemma.

We use this isomorphism-preserving reduction to conclude the proofs of Theorems 9.5 and 9.6.

_Proof of Theorems 9.5 and 9.6._ We show the contraposition. Assume there is an \(\varepsilon>0\) such that \(\mathsf{Gap}\mathsf{Max}\mathsf{3}\mathsf{Coverage}_{1,1-1/e+\varepsilon}\) can be solved in the Isomorphic-Priors model with preprocessing and query time polynomial in _n_ even when _k_=1 prior instance is given.

Then for every \(\varepsilon'>0\), \(\mathsf{Gap}\mathsf{Max}\mathsf{3}\mathsf{SAT}_{1,1-\varepsilon^\prime}\) can be solved in the Isomorphic-Priors model with preprocessing and query time polynomial in _n_ even when _k_=1 prior instance is given.

