<tbc>in Theorem 5 then follows from the Sensitivity Lemma. In Section 4.3 we prove that the average sensitivity measure is Lipschitz continuous. For the analysis, we make use of the decomposition of the objective of inversion minimization on trees mentioned earlier. We describe the decomposition in more detail in Section 4.2; it will be helpful in later parts of this paper, as well.

## 4.1 Subtree-induced sensitivity

We first introduce a sensitivity bound for inversion minimization based on the size of a subtree.

**Lemma 21 (subtree-induced sensitivity).** _Consider a tree T with_ \(n\doteq|\mathrm{L}(T)|\) _leaves, and some node v in T with_ \(\ell\doteq|\mathrm{L}(T_v)|\) _leaves. We have_

\(s(\Pi_T)\ge\frac{\ell(n-\ell)}{n}-1.\)

Note that _v_ is not necessarily a direct child of the root, as shown in Fig. 6.

We now prove Lemma 21. Let \(\rho\) be a ranking of the leaves of _T_, and let \(\sigma_\mathrm{min}\) be a tree ordering that minimizes the number of inversions with respect to \(\rho\).

**Claim 22.** \(\rho\) _is sensitive to the transposition_ \(\tau=(r,r+1)\) _if_ \(\sigma_\mathrm{min}(\rho^{-1}(r))>\sigma_\mathrm{min}(\rho^{-1}(r+1))\).

_Proof._ If \(\sigma_\mathrm{min}(\rho^{-1}(r))>\sigma_\mathrm{min}(\rho^{-1}(r+1))\), then \(\mathrm{Inv}_{\tau\rho}(\sigma_\mathrm{min})=\mathrm{Inv}_\rho(\sigma_\mathrm{min})-1\). Since \(\mathrm{Inv}_\rho(\sigma_\mathrm{min})=\mathrm{MinInv}(T,\rho)\), this means that \(\mathrm{MinInv}(T,\tau\rho)<\mathrm{MinInv}(T,\rho)\), or that \(\rho\) is sensitive to \(\tau\).

In the case of general trees, a tree ordering \(\sigma\) that minimizes the number of inversions with respect to \(\rho\) is difficult to find (see the discussion on NP-hardness in Section 10). Our strategy is to find a lower bound on the number of _r_ for which \(\sigma(\rho^{-1}(r))>\sigma(\rho^{-1}(r+1))\) that applies regardless of \(\sigma\).

**Claim 23.** _For any ordering_ \(\sigma\)_, the number of r such that_ \(\sigma(\rho^{-1}(r))>\sigma(\rho^{-1}(r+1))\) _is at least one less than the number of s such that_ \(\rho^{-1}(s)\in\mathrm{L}(T_v)\) _and_ \(\rho^{-1}(s+1)\unknown\in\mathrm{L}(T_v)\).

_Proof._ For all except at most one value of _s_ (the maximum _s_ for which \(\rho^{-1}(s)\in\mathrm{L}(T_v)\)), there exists a minimal \(s'>s\) such that \(\rho^{-1}(s')\in\mathrm{L}(T_v)\). We claim that at least one value of \(r=s,\dots,s'-1\) satisfies \(\sigma(\rho^{-1}(r))>\sigma(\rho^{-1}(r+1))\). If not, then \(\sigma\) would rank \(\rho^{-1}(s),\rho^{-1}(s+1),\dots,\rho^{-1}(s')\) in increasing order. Because \(\sigma\) is a tree ordering, the leaves of L(_T<sub>v</sub>_) must be mapped into a contiguous range by \(\sigma\), as shown in Fig. 7. However, we have \(\rho^{-1}(s),\rho^{-1}(s')\in\mathrm{L}(T_v)\) but \(\rho^{-1}(s+1)\unknown\in\mathrm{L}(T_v)\), which violates this property since \(\sigma\) ranks a leaf outside L(_T<sub>v</sub>_) between two leaves inside L(_T<sub>v</sub>_).

Because each value of _r_ is found between consecutive pairs of values in L(_T<sub>v</sub>_), the values of _r_ are distinct.

**Claim 24.** _Over a uniformly random_ \(\rho\)_, the expected number of s such that_ \(\rho^{-1}(s)\in\mathrm{L}(T_v)\) _and_ \(\rho^{-1}(s+1)\unknown\in\mathrm{L}(T_v)\) _is_ \(\frac{\ell(n-\ell)}{n}\) .

v
L(T)
L(T)

Figure 6: Subtree rooted at _v_

