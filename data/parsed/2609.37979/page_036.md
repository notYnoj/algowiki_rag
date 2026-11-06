We note that, in Theorems 7.2 and 7.4, we can also reconstruct an optimal solution of a query graphs if we are given optimal solutions for all priors. While it does not seem possible to obtain such a statement in the general setting of Theorems 8.3 and 8.4, we note that all our arguments for specific problems do imply that optimal solutions can indeed be reconstructed (see Appendix A for further examples).

In the following, we use an alternative way to characterize when an optimization problem is \(\ell\)-WL invariant. We limit ourself to minimization problems. However, our approach can easily be extended to maximization problems. Remember that G is the set of valid attributed input graphs.

**Definition 8.5.** Let \(\Pi\) be an minimization problem. We call a triple \((W,\text{check}:\mathcal{G}\times W\rightarrow\mathbb{R}_{\ge 0},\text{cost}:W\rightarrow\mathbb{R})\) a _witness function of_ \(OPT_\Pi\) if:

• For all _G_ and \(X\in W\): if check(_G,X)\>_0 then \(OPT_\Pi(G)\le\text{cost}(X)\).<tbc>

• If \(OPT_\Pi(G)<\infty\) then there is a \(X\in W\) with \(OPT_\Pi(G)=\text{cost}(X)\) and check(_G,X)\>_0.

The intuition behind \((W,\text{check}:\mathcal{G}\times W\rightarrow\mathbb{R}_{\ge 0},\text{cost}:W\rightarrow\mathbb{R})\) is that it characterizes the witnesses of the minimization problem \(\Pi\). The function "check" checks for an element _X_ if there exist a feasible solution (which is the case if check(_G,X)\>_0) with cost at most cost(_X_). Further, if _G_ has a feasible solution (i.e. \(OPT_\Pi(G)<\infty\)) then there is a _witness_ \(X\in G\) that attains the optimal value (i.e. \(OPT_\Pi(G)=\text{cost}(X)\) and check(_G,X)\>_0).

In the following, we show that we can a witness function to show that \(OPT_\Pi\) is \(\ell\)-WL. To this end, we show that the witness function itself is \(\ell\)-WL invariant.

**Definition 8.6.** Let \(\text{check}:\mathcal{G}\times W\rightarrow\mathbb{R}_{\ge 0}\) be a function. We say that check is \(\ell\)_-WL invariant on_ G if: for all graphs \(G,H\in\mathcal{G}\) with \(G\equiv_{\ell\text{-WL}}H\) and all \(X\in W\) we obtain that check(_G,X)\>_0 if and only if check(_H,X)\>_0.

**Lemma 8.7.** _Let_ \(\Pi\) _be an minimization problem and_ \((W,\text{check}:\mathcal{G}\times W\rightarrow\mathbb{R}_{\ge 0},\text{cost}:W\rightarrow\mathbb{R})\) _be a witness function of_ \(OPT_\Pi\)_. If_ check _is_ \(\ell\)_-WL invariant on_ G _then_ \(\Pi\) _is_ \(\ell\)_-WL invariant._

_Proof._ Let \(G,H\in\mathcal{G}\) be two graphs with \(G\equiv_{\ell\text{-WL}}H\). Without loss of generality, we assume \(OPT_\Pi(G)\le OPT_\Pi(H)\) (otherwise we change to role of _G_ and _H_). We have to show that \(OPT_\Pi(H)\le OPT_\Pi(G)\). If \(OPT_\Pi(G)=\infty\) then we are already done. Otherwise, \(OPT_\Pi(G)<\infty\). Thus, there exist a \(X\in W\) with \(OPT_\Pi(G)=\text{cost}(X)\) and check(_G,X)\>_0. Now, since check is \(\ell\)-WL invariant, we obtain that check(_H,X)\>_0. Hence, \(OPT_\Pi(H)\le\text{cost}(X)=OPT_\Pi(G)\).

## 8.3 CSP is 1-WL Invariant

We first demonstrate the above approach on the Constrained Shortest Path (CSP) problem and present an alternative proof for Theorem 7.2 using a characterization of 1-WL via homomorphism counts \[Dvo10, DGR18\]. Write _OPT_ for the optimal value function of CSP and G for the set of valid input graphs of CSP. We show that _OPT_ is 1-WL invariant for all values.<sup>26</sup> This together with Theorem 8.4 immediately yields that CSP is in the Isomorphic-Priors model.

**Theorem 8.8.** _The Problem_ CSP _is 1-WL invariant._

To prove Theorem 8.8 we define a witness for _OPT_ and show that this witness is 1-WL invariant. To this end, we start by defining graph homomorphisms.

<sup>26</sup>There is the small technical detail that an input graph _G_ has a length constraint _B_ that is part of the input. Consistent with previous sections, we say that two input graphs _G_ and _H_ are 1-WL equivalent if _G_ and _H_ have the same length constraint _B_ and \(G\equiv_{1\text{-WL}}H\) for the underlying attributed graphs.

