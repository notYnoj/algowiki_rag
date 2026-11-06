**Proposition 31.** _Let T be a binary tree,_ \(\rho\) _a ranking of the leaves of T,_ \(\tau\) _an adjacent-rank transposition,_ \(\ell_\mathrm{lo}\) _and_ \(\ell_\mathrm{hi}\) _the two leaves affected by_ \(\tau\) _under_ \(\rho\) _such that_ \(\rho\) _ranks_ \(\ell_\mathrm{lo}\) _before_ \(\ell_\mathrm{hi}\)_. Referring to the notation in Figure 9, we have that_

\(\mathrm{MinInv}(T,\rho)=\mathrm{MinInv}(T,\tau\rho)\Leftrightarrow\mathrm{DInv}_\rho(L_\mathrm{lo},L_\mathrm{hi})=\mathrm{DInv}_\rho(\{\ell_\mathrm{lo}\},\{\ell_\mathrm{hi}\})\) (8)

\(\Leftrightarrow\mathrm{DInv}_\rho(A,B)=|A_<|-|A_>|+|B_>|-|B_<|.\) (9)

## 5.2 Root sensitivity

Given a ranking \(\rho\) and an adjacent-rank transposition \(\tau\), we know by Proposition 27 that at most one of the terms in the decomposition (5) of \(\mathrm{MinInv}(T,\rho)\) is affected by the transposition, namely \(\mathrm{MinRInv}(T_v,\rho)\) where _v_ is the lowest common ancestor of the affected leaves \(\ell_\mathrm{lo}\) and \(\ell_\mathrm{hi}\). It follows that we can write the average sensitivity of \(\Pi_T\doteq\mathrm{MinInv}(T,\cdot)\) as the following convex combination:

\(s(\Pi_T)=(n-1)\cdot\mathbb{P}[\mathrm{MinInv}(T,\rho)\neq\mathrm{MinInv}(T,\tau\rho)]\)<br>
\(=(n-1)\sum_v\mathbb{P}[v=\mathrm{LCA}(\ell_\mathrm{lo},\ell_\mathrm{hi})]\cdot\mathbb{P}[\mathrm{MinRInv}(T_v,\rho)\neq\mathrm{MinRInv}(T_v,\tau\rho)|v=\mathrm{LCA}(\ell_\mathrm{lo},\ell_\mathrm{hi})],\) (10)

where the probability is over a uniformly random choice of the ranking \(\rho\) and the adjacent-rank transposition \(\tau\), and \(\ell_\mathrm{lo}\) and \(\ell_\mathrm{hi}\) denote the affected leaves. The conditional probability on the right-hand side of (10) only depends on the subtree _T<sub>v</sub>_. The ranking \(\rho\) of all leaves induces a ranking \(\rho'\) of the leaves of _T<sub>v</sub>_ that is uniform under the conditioning. Similarly, the adjacent-rank transposition \(\tau\) for \(\rho\) induces an adjacent-rank transposition \(\tau'\) for \(\rho'\); the distribution of \(\tau'\) under the conditioning is independent of \(\rho'\) and uniform among all adjacent-rank transpositions such that the affected leaves live in subtrees of different children of _v_. Thus, the probability on the right-hand side of (10) coincides with the following notion for the subtree _T<sub>v</sub>_.

**Definition 32 (root sensitivity).** _Let T be a tree. The_ root sensitivity _of T is the probability that_ \(\mathrm{MinRInv}(T_v,\rho)\neq\mathrm{MinRInv}(T_v,\tau\rho)\) _when_ \(\rho\) _is a uniform random ranking of_ L(_T), and_ \(\tau\) _a uniform random adjacent transposition with the condition that the affected leaves are in subtrees of different children of the root of T._

Note that the only nodes _v_ that need to be considered in the sum on the right-hand side of (10) are those that can appear as the lowest common ancestor of two leaves, and such that _T<sub>v</sub>_ is not freely arrangeable. In the case of binary trees, this means that we only need to consider nodes _v_ of degree 2 such that _T<sub>v</sub>_ contains more than 2 leaves. In this section we prove a strong lower bound on the root sensitivity of such trees _T<sub>v</sub>_.

Consider the binary tree _T_ with root _v_ in Figure 9. The distribution underlying Definition 32 can be generated as follows: Pick a leaf on each side of the root _v_ uniformly at random, and let \(\rho\) be a ranking of the leaves of _T_ that is uniformly random on the condition that the selected leaves receive adjacent ranks; \(\tau\) then is the adjacent-rank transposition that swaps the two selected leaves. The root sensitivity of _T_ is the complement of the probability that the right-hand side of (9) holds under this distribution. Let us analyze the left-hand side of (9) further. As \(A=A_<\sqcup A_>\) and \(B=B_<\sqcup B_>\), we have that<tbc>

\(\mathrm{DInv}_\rho(A,B)=\mathrm{DInv}_\rho(A_<,B_<)+\mathrm{DInv}_\rho(A_<,B_>)+\mathrm{DInv}_\rho(A_>,B_<)+\mathrm{DInv}_\rho(A_>,B_>).\)

