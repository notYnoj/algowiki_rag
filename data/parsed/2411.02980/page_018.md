\(\bullet\) Since \(\varepsilon_1=\Theta(1/k)\) and \(p_1=\Theta(k^7)\), for _k_ sufficiently large it holds<tbc>

\(\left(1-\mathrm{e}q^{-(1-\varepsilon_1)k}\right)^{-2kp_1\alpha}=\mathrm{exp}\left(\Theta\left(\mathrm{e}q^{-(1-\varepsilon_1)k}\cdot 2kp_1\alpha\right)\right)\)<br>
\(=\mathrm{exp}\left(\Theta\left(q^{-k+O(1)}k^8\alpha\right)\right)\)<br>
\(=O(1),\)

assuming \(\alpha\le\frac{q^k}{(qk)^c}\) for a sufficiently large universal constant \(c\ge 8\).

Combining everything above, we conclude with

\(\mathbf{Pr}\left[d_\mathrm{Ham}(X,Y)\ge k\cdot M\right]\le\left(8\mathrm{e}k^2\alpha\cdot q^{-k+O(1)}\cdot O(1)\right)^M\le 2^{-M},\)

where we assume \(\alpha\le\frac{q^k}{(qk)^c}\) for some sufficiently large universal constant _c\>_0. □

## 4.4. Proofs of replica symmetry and non-reconstruction.

In this subsection, we leverage the coupling analysis from previous sections to explore the correlation decay properties for random CSP formulas. Specifically, we will establish the properties of replica symmetry (Theorem 1.9) and non- reconstruction (Theorem 1.11) for random CSPs at the considered densities. Additionally, we will examine a connectivity property of the solution space, known as the _looseness_ property (which will be formally defined later in Definition 4.12).

It is important to note that while these theorems are stated in the context of random _k_-SAT, our proofs are applicable to a broader class of random CSPs, including random hypergraph colorings.

_Proof of Theorems 1.9 and 1.11._ Recall the decay of correlation property established in Theorem 4.1, which implies both replica symmetry and non-reconstruction.

We apply the procedure \(\mathrm{Couple}(\mathcal{E},\mathcal{F},\sigma,\tau)\) described in Algorithm 2 to construct a coupling between two instances obtained from the same set of constraints C, differing only in the pinning on one variable. Specifically, we consider the coupling procedure \(\mathrm{Couple}(\mathcal{E},\mathcal{F},\sigma,\tau)\) with the following initial states:

\(\bullet\) The initial set of constraints are E=F=C;<tbc>

\(\bullet\) The initial assignments \(\sigma,\tau\) are both specified on just _v_, with \(\sigma(v)=x_1\) and \(\tau(v)=x_2\).

The key proofs for the coupling procedure in Section 4 apply to this setting. In particular, the correctness follows directly from the proof of Proposition 4.2. Thus, \(\mathrm{Couple}(\mathcal{E},\mathcal{F},\sigma,\tau)\) returns (_X,Y_) such that \(X\sim\mu_\mathcal{C}^\sigma\) and \(Y\sim\mu_\mathcal{C}^\tau\). Since all pinned constraints in the initial discrepancy set \(\mathcal{E}^\sigma\triangleup\mathcal{F}^\tau\) must include _v_, they are connected in \(G_\Phi\). Hence, the proof for Proposition 4.5 holds in this case as well. As a result, following the same reasoning as in Theorem 4.1, we can establish that for the pair (_X,Y_) returned by this \(\mathrm{Couple}(\mathcal{E},\mathcal{F},\sigma,\tau)\), we have

(8) \(\mathbf{Pr}\left[d_\mathrm{Ham}(X,Y)\ge k\cdot M\right]\le d\cdot 2^{-M}.\)

The extra factor of _d_ in the probability bound comes from the need to bound the number of witness trees rooted at a constraint containing _v_, rather than at a single constraint _c_<sub>0</sub>. While Condition 3.1 technically holds with width _k_-1 after pinning one variable, the proof of Theorem 4.1 is robust enough to proceed with this slightly weakened Condition 3.1, thereby implying (8).

Finally, we conclude the proof:

\(\bullet\) Theorem 1.9 follows from the exponential decay of correlation established in (8);<tbc>

\(\bullet\) Theorem 1.11 also follows from (8), as with high probability, the discrepancy at _v_ does not affect the assignment on \(\bar{B}_H(v,r)\) when _r_ is large enough. □

Recent work has focused on exploring the solution space of random _k_-SAT through various notions of connectivity. One way to characterize connectivity of the solution space is looseness considered in \[AC08, CGG<sup>+</sup>24\], basically saying one can obtain another solution with some variable flipped without overall flipping too many variables.

**Definition 4.12** (looseness)**.** Let \(\Phi=(V,C)\) be a SAT formula with |_V_|=_n_. A variable \(v\in V\) is said to be _M-loose_ with respect to a satisfying assignment \(\sigma\in\Omega_\Phi\) if there exists another satisfying assignment \(\tau\in\Omega_\Phi\) such that \(\tau(v)\neq\sigma(v)\) and \(d_\mathrm{Ham}(\sigma,\tau)\le M\).

