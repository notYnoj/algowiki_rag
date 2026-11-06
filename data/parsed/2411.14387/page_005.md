Note that the sequence _Y_ is _easy_ w.r.t. the Alteration bound since \(\overline{\text{Alt}}(Y)\le O(1)\). We use the sequence _Y_ as a base-case and apply Theorem 1 to construct _hard_ sequence w.r.t. the funnel bound while maintaining the separation as in the following theorem <sup>3</sup>.

\(\blacktriangleright\) **Theorem 2** (Hardness Amplification)**.** _There is a constant K\>_0 _such that for any n of the form_ 2<sup>2_r_</sup> _and any power-of-two_ \(R\le\frac{logn}{K}\) _, there is a sequence_ \(Y_n^{\circ R}\in[n]m^{\prime\prime}\) _with_ \(m'\le poly(n)\) _such that_

\(\overline{\text{Alt}}\big(Y_n^{\circ R}\big)\le O(R)\overline{\text{Funnel}}\big(Y_n^{\circ R}\big)\ge\Omega\big(Rlog\big(\frac{logn}{R}\big)\big).\)

**Remark 1.** We emphasize that the approximate subadditivity of the Alteration bound (Equation (2)) is not sufficient for such hardness amplification. On the other hand, one could also use the superadditivity of the optimal cost (Equation (1)) instead of the Funnel bound to prove hardness amplification.

**Tightness of the Separation.** As a corollary of Theorem 2, we can derive the following trade-offs between the multiplicative and additive factors for the Alteration bound.

\(\blacktriangleright\) **Theorem 3.** _Let_ \(\alpha,\beta:\mathbb{N}\rightarrow\mathbb{R}_{\ge 1}\) _be any functions such that some BST algorithm achieves an amortized cost of_ \(\alpha(n)\overline{\text{Alt}}(X)+\beta(n)\) _for all access sequences X over n keys. Then_ \(\alpha(n)\ge\Omega\big(log\big(\frac{logn}{\beta(n)}\big)\big)\).

As we discuss below, the trade-offs are tight with the matching upper bounds from Tango Trees (which can be derived directly from Tango trees). For convenience, we present self-contained BST algorithms with the matching upper bounds.

\(\blacktriangleright\) **Lemma 4.** _There is a BST algorithm that takes an integer_ \(k\le logn\) _as a parameter and serve the sequence_ \(X=(X_1,\cdots,X_m)\) _with the total access time of_

\(O\big(\big(\text{Alt}(X)+m\cdot\frac{logn}{k}\big)\cdot(logk+1)\big).\)

We prove Lemma 4 in Appendix A.

In this algorithm, the additive cost is \(\Theta\big(\frac{lognlogk}{k}\big)\) and multiplicative cost \(\Theta(logk)\). By Theorem 3, if \(\beta(n)=\Theta\big(\frac{lognlogk}{k}\big)\), then we have

\(\alpha(n)\ge\Omega\big(log\big(\frac{logn}{\beta(n)}\big)\big)=\Omega\big(log\big(\frac{k}{logk}\big)\big)=\Omega(logk),\)

so our trade-off is optimal for any sufficiently large \(k\le logn\).

**Optimality of Tango Trees.** As another corollary of Theorem 2, we prove the optimality of Tango Trees among any algorithm charging its cost to Wilber’s Alteration bound for all values of the <o>Alt</o>(_X_). Note that \(\overline{\text{Alt}}(X)\le O(logn)\). Previously, the optimality of Tango trees is known only when <o>Alt</o>(_X_)=_O_(1) [27].

The basic idea of Tango Trees is to "mimic" Wilber’s alternation bound via a BST, by dynamically maintaining a partition of the reference tree T into _disjoint paths_, formed by designating, for each node \(x\in\mathcal{T}\) , the unique "preferred" descendant in T (left or right) which

<sup>3</sup> This can be viewed as hardness amplification because the new sequence becomes harder from the optimum’s point of view without losing the gap too much.

