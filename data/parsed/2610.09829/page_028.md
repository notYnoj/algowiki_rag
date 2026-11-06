**Starting with the dynamic programming states.** We now define the states of our dynamic programming table, for a fixed _d_-diverse \(\mathcal{P}\subseteq\mathcal{Q}\) set of longitudinal paths.

**Definition 5.6** (States)**.** Consider a set of longitudinal paths \(\mathcal{P}\subseteq\mathcal{Q}\), where P is _d_-diverse. Recall that \(w(\mathcal{C}\cup\mathcal{P})=\sum_{e\in E_{\mathcal{C}\cup\mathcal{P}}}w(e)\), where \(E_{\mathcal{C}\cup\mathcal{P}}=\bigcup_{X\in\mathcal{C}\cup\mathcal{P}}E(X)\). For an integer _h_, where \(1\le h\le k\), and a node \(\alpha\) of T , we define \(\Pi_\mathcal{P}(\alpha,h)\) to be the maximum over \(w(\mathcal{C}\cup\mathcal{P})\), where C is a set of _d_- diverse tree cycles of _G_ satisfying the following conditions:

1. |C|=_h_ and \(\alpha\in\mathcal{C}\).<tbc>

2. For each \(\beta\in\mathcal{C}\), \(\beta\) is a descendant of \(\alpha\) in T .<sup>4</sup><tbc>

3. Every tree cycle in C is _d-diverse_ from every path in P, i.e., for each \(C\in\mathcal{C}\) and \(P\in\mathcal{P}\), we have \(w(C\cap P)\le d\).

In the above, any C satisfying the above three conditions is a _solution_ for \(\Pi_\mathcal{P}(\alpha,h)\). Moreover, it is an _optimal solution_ if we have \(w(\mathcal{C}\cup\mathcal{P})=\Pi_\mathcal{P}(\alpha,h)\).

In Section 5.3 we prove the following lemma, and for the remainder of this section we show how we can compute the optimal solution for \((G,w,k,d,\ell)\) using this lemma.

**Lemma 5.5** (Section 5.3)**.** _Given_ \((G,w,k,d,\ell)\), T _and a d-diverse_ \(\mathcal{P}\subseteq\mathcal{Q}\)_, in (total) time bounded by_ \(2^{\mathcal{O}(k)}\cdot n^{\mathcal{O}(1)}\)_, for each_ \(\alpha\in V(\mathcal{T})\) _and integer_ \(h\in[k]\)_, we can compute the entry_ \(\Pi_\mathcal{P}(\alpha,h)\).

We are ready to prove the main result of this section.

_Proof of Theorem 1.2._ Consider an instance \((G,w,k,d,\ell)\) of Planar DSC. As discussed earlier, we assume that \((G,w,k,d,\ell)\) satisfies the conditions stated in the beginning of the section, and we have computed T (using Item 4), rooted at _C<sub>r</sub>_. If the number of leaves in T is more than 4_k_, we can resolve the instance in polynomial time as discussed earlier, so we assume that T has at most 4_k_ leaves.

Now for each _d_-diverse \(\mathcal{P}\subseteq\mathcal{Q}\), we compute \(\Pi_\mathcal{P}(\alpha,h)\), for each node \(\alpha\) of T and an integer \(h\in[k]\). As the number of leaves in T is bounded by 4_k_, from Lemmas 5.4 and 5.5 and Lemma 5.1 (Item (ii)), it follows that we can execute the above stated step in (total) time bounded by \(2^{\mathcal{O}(k)}\cdot n^{\mathcal{O}(1)}\). Furthermore, within the same running time we can compute the following number:<sup>5</sup>

\(z=\mathrm{max}_{d\text{-diverse}\mathcal{P}\subseteq\mathcal{Q}h\in[k]:(k-h)\text{is}\mathcal{P}\text{-valid}}\Pi_\mathcal{P}(C_r,h)\)

Finally, we return that \((G,w,k,d,\ell)\) is a yes-instance if and only if \(z\ge\ell\).

The desired runtime bound follows from above discussions. Thus, to conclude the proof it is enough to argue that the weight of an optimal solution for \((G,w,k,d,\ell)\) is exactly _z_. (In the above if an optimal solution does not exist, by the weight of its optimal solution we mean \(-\infty\).) To this end, consider an optimal solution C for \((G,w,k,d,\ell)\), where \(C_r\in\mathcal{C}\).

We will first show that \(z\ge w(\mathcal{C})\). We assume that right hand side is not \(-\infty\), else the inequality is trivially satisfied. Let C_<sub>T</sub>_ and C_<sub>N</sub>_ denote the sets of tree cycles and non-tree cycles in C, respectively. Let _h_<sup>∗</sup>=|C_<sub>T</sub>_|, and let P<sup>∗</sup> be the set of longitudinal paths covered by the _k-h_<sup>∗</sup> cycles in C_<sub>N</sub>_.

<sup>4</sup>For a rooted tree, we use the convention that each node is also a descendant of itself. <sup>5</sup>We use the convention that empty maximum is \(-\infty\), which is a number smaller than any fixed integer.

