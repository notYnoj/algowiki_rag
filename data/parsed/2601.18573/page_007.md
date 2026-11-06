We will also study the maximum-cardinality matching analogue, which we define formally below.

In search of more computational tractability, we will also consider the above problem in the bipartite smi restriction, where we are given an smi instance _I_ instead, and a subset \(D\subseteq A\). We will refer to this problem as Deviator-Max-smi. Of course, all three problems are NP-hard in general, because the NP-hard problems MinBP-AlmostStable-sri and MinBP-AlmostStable-Max-smi appear as special cases when _D=A_. However, we will investigate natural restrictions and algorithms for the case when _D_ is small, and we will also show that, contrary to their non-deviator analogues, these problems turn out to be intractable even when the optimal value is 0, i.e., when merely aiming to decide whether a deviator-stable matching exists! This contrasts known complexity results as follows: deciding whether the optimal value is 0 is efficiently solvable using the Gale-Shapley or Irving’s algorithm when _D=A_, and MinBP-AlmostStable-sri is in XP with respect to the optimal parameter value, i.e., efficiently solvable for any fixed optimal parameter value \[1\].

We will first examine maximum-cardinality matchings with these properties in bipartite acceptability graphs (i.e., the Deviator-Max-smi problem) in Section 3.1, before extending our techniques to the general case in Section 3.2.

## 3.1 Deviator-Stable Maximum Matchings in Bipartite Graphs

We start by defining the following restriction of Deviator-Max-smi.

We will denote the problem of deciding whether there exists a solution to the above problem in the special case when maximum-cardinality matchings are perfect by _k_-Deviator-Perfect- smi-Dec.

Notice that whenever _D=A_ and _k_=0, then (_I,D_) is a yes-instance to 0-Deviator-Max- smi if and only if there exists a stable maximum-cardinality matching of _I_. This can be decided in polynomial time by computing a stable matching _M_ of _I_ using the Gale-Shapley algorithm \[21\] and checking whether _M_ is a maximum-cardinality matching. If it is not, then no solution exists, as every stable matching is of equal size \[43\].

Somewhat surprisingly, when \(D\subset A\), then even 0-Deviator-Perfect-smi-Dec becomes intractable, i.e., even when we merely ask whether a perfect matching exists such that no agent in _D_ is in a blocking pair.

**Theorem 3.1.** 0-Deviator-Perfect-smi-Dec _is_ NP-complete_, even if all preference lists are of length at most 3 and all deviators are on one side of the bipartition._

_Proof._ Membership in NP follows from the fact that, given a matching _M_, we can efficiently check whether _M_ is a perfect matching and whether any agent in the deviator subset is contained in any blocking pair by iterating through the preference lists.

Deviator-sri
Input: sri instance I = (A, ) and a subset D A.
Output: A matching M M such that | (aiin D bpaa i M) = minM'in M | (aiin D bpaa i M')|.

Deviator-Max-sri
Input: sri instance I = (A, ) and a subset D A.
Output: A matching M M such that | (aiin D bpaa i M) = minM'in M | (aiin D bpaa i M')|.

k-Deviator-Max-smi
Input: smi instance I = (A, ) and a subset D A.
Output: A matching M M such that | (aiin D bpaa i M) | k, if one exists.

