### Soundness.

Assume \(G_0\cong G_1\). Then the distributions of \(\pi(G_0)\) and \(\pi(G_1)\) are identical, hence the random bit _b_ is independent of the pair (_D,J_), and therefore also independent of \(\widehat{b}\) (which is a function of (_D,J_) and the internal randomness of Query). Consequently, in each round we have \(\mathrm{Pr}[\widehat{b}=b]\le\frac{1}{2}\), and Arthur accepts with probability at most 1/4_\<_2/3.

Therefore \(\overline{\mathsf{Gl}}\in\mathsf{MA}\), which implies \(\mathsf{Gl}\in\mathsf{coMA}\).

By contrapositive, unless \(\mathsf{Gl}\in\mathsf{coMA}\), no such polynomial-size data structure algorithm for Gl exists in the Isomorphic-Priors model (even for _k_=1).

## 9.2 Iso-Problems and Gl-Completeness

We introduce the promise problem Iso-\(\Pi\) and show properties that will be used in later sections to show hardness results in our model.

**Definition 9.8.** For a decision problem \(\Pi\), define the promise problem Iso-\(\Pi=(\mathsf{Iso}-\Pi_\mathrm{YES},\mathsf{Iso}-\Pi_\mathrm{NO})\) over pairs of instances (_I,J_) by

\(\mathrm{Iso}-\Pi_\mathrm{YES}:=\{(I,J)|I\in\Pi\wedge J\cong I\},\mathrm{Iso}-\Pi_\mathrm{NO}:=\{(I,J)|I\in\Pi\wedge J\notin\Pi\}.\)

The input is promised to lie in Iso-\(\Pi_\mathrm{YES}\cup\mathsf{Iso}-\Pi_\mathrm{NO}\).

We recall the definition of polynomial-time many-one reductions.

**Definition 9.9.** We say that there is a _polynomial-time many-one reduction_ from \(\Pi\) to \(\Pi'\) if there exist a polynomial-time computable function _f_ such that \(X\in\Pi\) if and only if \(f(X)\in\Pi\).

We say that \(\Pi\) is Gl-hard if there is a polynomial-time many-one reduction from Gl to \(\Pi\). We say that \(\Pi\) is Gl-complete if there \(\Pi\) is Gl-hard and there is a polynomial-time many-one reduction from \(\Pi\) to Gl.

We show that for \(\Pi=\mathsf{Gl}\), Iso-\(\Pi\) is just a reformulation of Gl.

**Lemma 9.10.** Iso-Gl _is_ Gl_-complete._

_Proof._ Recall that Iso-Gl is the promise problem on pairs (_I,J_) of Gl-instances such that \(I\in\mathsf{Gl}\) and either \(J\cong I\) (YES) or \(J\notin\mathsf{Gl}\) (NO).

### (1) Iso-\(\mathsf{Gl}\in\mathsf{Gl}\).

Given an input (_I,J_), where _I_=(_G_<sub>0</sub>_,G_<sub>1</sub>) and _J_=(_H_<sub>0</sub>_,H_<sub>1</sub>), run a Gl-test to decide whether \(I\cong J\), i.e. whether \(G_0\cong H_0\) and \(G_1\cong H_1\). If \(I\cong J\) output YES, otherwise output NO. This is correct under the promise: in a YES-instance we have \(J\cong I\), while in a promised instance with \(J\unknown\cong I\) we cannot be in Iso-Gl<sub>YES</sub>, hence must be in Iso-Gl<sub>NO</sub>.

### (2) Gl-hardness.

We give a polynomial-time many-one reduction from Gl to Iso-Gl. Given a Gl-instance _I_=(_G,H_), output the pair

\(f(G,H):=\big((G,G),(G,H)\big).\)

Note that \((G,G)\in\mathsf{Gl}\) always. If \(G\cong H\), then \((G,H)\cong(G,G)\), so \(f(G,H)\in\mathsf{Iso}-\mathsf{Gl}_\mathrm{YES}\). If \(G\unknown\cong H\), then \((G,H)\notin\mathsf{Gl}\), so \(f(G,H)\in\mathsf{Iso}-\mathsf{Gl}_\mathrm{NO}\). Hence _f_ is a valid reduction and \(\mathsf{Gl}\le_m\) Iso-Gl.

