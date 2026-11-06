This _k_-prover systems can be used for an isomorphism-preserving reduction.

**Lemma 9.27.** _For every_ \(\varepsilon,\varepsilon'\in(0,1/3)\)_, there is an isomorphism-preserving reduction_

\(\mathsf{Gap}\text{-Max-3-SAT}_{1,1-\varepsilon}\le_p^\cong\mathsf{Gap}\text{-Max-}k\text{-Coverage}_{1,1-1/e+\varepsilon^\prime}.\)

_Proof._ Fix \(\varepsilon\in(0,1/3)\). We construct an isomorphism-preserving mapping from 3CNF formulas to Max-_k_-Coverage instances, following Feige \[Fei98\], and use Lemma 9.26 (Feige’s Lemma 2.3.1 without bounded-occurrence) as the only nontrivial black box about the underlying _k_-prover system.

## No regularization.

We do _not_ apply any bounded-occurrence / regularization preprocessing: such steps typically require non-canonical choices (e.g., ordering occurrences), and are therefore not isomorphism-preserving in general.

## Step 1: The reduction \(\Phi\mapsto(U(\Phi),\mathcal{S}(\Phi),k')\).

Let \(\Phi\) be a 3CNF instance. Consider the _k_-prover verifier from \[Fei98, Sec. 2.3\] with repetition parameter \(\ell\) (to be chosen later as a function of \(\varepsilon\)). Let R be the set of random strings of the verifier; write _R_:=|R|. For each \(r\in\mathcal{R}\), the verifier determines (for each prover \(i\in[k]\)) a question _q<sub>i</sub>(r_) (a tuple of clause/variable identifiers as in \[Fei98, Sec. 2.3\]). Let _Q_ be the number of possible questions a prover can receive (as in Feige).

_Partition systems._ Fix parameters (_m,L,k,d_) as in Feige’s partition-system lemma (Lemma 3.2 in \[Fei98\]), with \(L=2^\ell\). For each \(r\in\mathcal{R}\), create an independent copy of the partition system<tbc>

\(B_r:=B(m,L,k,d)\)

<tbc>on a ground set of size _m_, equipped with _L_ partitions indexed by strings \(p\in\{0,1\}^\ell\). Each such partition consists of _k_ disjoint parts, which we denote<tbc>

\(\mathcal{P}_{r,p}=\big\{B(r,p,1),\dots,B(r,p,k)\big\},\bigcup_{i=1}^kB(r,p,i)=B_r.\)

<tbc>_Universe._ Define the universe as the disjoint union of all these ground sets:

\(U(\Phi):=\unknown_{r\in\mathcal{R}}\big(\{r\}\times B_r\big),\)

so \(|U(\Phi)|=mR\).

_Sets._ For each prover \(i\in[k]\), each question _q_ that prover _i_ may receive, and each possible answer _a_ to that question, define a set \(S(q,a,i)\subseteq U(\Phi)\) by<tbc>

\(S(q,a,i):=\bigcup_{r\in\mathcal{R}:q_i(r)=q}\big(\{r\}\times B(r,p_r(a),i)\big),\)

<tbc>where \(p_r(a)\in\{0,1\}^\ell\) is the induced assignment to the \(\ell\) distinguished variables selected under randomness _r_ (exactly as in Feige’s reduction). Let<tbc>

\(\mathcal{S}(\Phi):=\big\{S(q,a,i):i\in[k],q\in\mathcal{Q}_i,a\in\mathcal{A}_{i,q}\big\}.\)

<tbc>_Budget._ Set

\(k':=k^Q,\)

corresponding to choosing, for each prover, one answer for each of its _Q_ possible questions (as in Feige’s Max-_k_-Cover hardness, Section 5 of \[Fei98\]).

We output the Max-_k_-Coverage instance<tbc>

\(R(\Phi):=\big(U(\Phi),\mathcal{S}(\Phi),k'\big).\)

