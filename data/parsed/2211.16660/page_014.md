We call a pair _bad_ if it is not good.

Obviously, we cannot determine in almost-linear time if an input is good or bad, since that involves computing LCS(_x,y_). However, our analysis of the performance of FullLCSAAlgorithm(_x,y_) differs depending on whether the input is good or bad. In Section 5.4, we prove (3) when the input is bad, and in Section 5.5, we prove (3) when the input is good.

In both the easy direction (2) and the hard direction (3), we use the following characterization of the output of the dynamic programming in Algorithm 2. Recall a collection of rectangles is called an _ordered_ collection if every pair (_I,J_) and \((I',J')\) is comparable (i.e. either \(I<I'\) and \(J<J'\) or \(I>I'\) and \(J>J'\)).

**Lemma 5.2.** _The output of_ FullLCSAAlgorithm _is the maximum, over all ordered collections of certified rectangles_ \((I_1\times J_1,\kappa_1),\dots,(I_\ell\times J_\ell,\kappa_\ell)\)_, of_ \(\kappa_1+\kappa_2+\cdots+\kappa_\ell\).

_Proof._ By induction, it follows that DP\[_i_\]\[_j_\] is the maximum, over all ordered collections of certified rectangles \((I_1\times J_1,\kappa_1),\dots,(I_\ell\times J_\ell,\kappa_\ell)\) contained in \([0,\gamma wi]\times[0,\theta wj]\), of \(\kappa_1+\kappa_2+\cdots+\kappa_\ell\). Here, we use that, for all rectangles \(I\times J\) in R, interval _I_ is \(\gamma w\)-aligned and interval _J_ is \(\theta w\)-aligned.

The next lemma asserts that certified rectangles are indeed "certified."

**Lemma 5.3.** _Every certified rectangle_ \((I\times J,\kappa)\) _in_ CoveringAlgorithm _satisfies_ \(\mathsf{LCS}(I,J)\ge\kappa\).

_Proof._ This is true of all rectangles certified by Trivial and EqLCS by definition. The algorithmic structure lemma rectangles \((I'\times J,\kappa)\) for \(\kappa=\frac{|I'|}{2}+\alpha w\) satisfy \(\mathsf{LCS}(I',J)\ge\kappa\) by Lemma 4.1.

The easy direction (2) follows easily from Lemma 5.2 and Lemma 5.3.

**Corollary 5.4.** FullLCSAAlgorithm\((x,y)\le\mathsf{LCS}(x,y)\)

_Proof._ By Lemma 5.2, the output of FullLCSAAlgorithm(_x,y_) equals \(\kappa_1+\cdots+\kappa_\ell\) for some ordered collection of certified rectangles \((I_1\times J_1,\kappa_1),\dots,(I_\ell\times J_\ell,\kappa_\ell)\). Then, by Lemma 5.3, we have

\(\mathsf{FullLCSAAlgorithm}(x,y)=\sum_{i=1}^\ell\kappa_i\le\sum_{i=1}^\ell\mathsf{LCS}(I_i,J_i)\le\mathsf{LCS}(x,y),\)

as desired.

## 5.4 Proof of (3) for bad inputs

We show that (3) holds in the bad case by conditioning on which case of Definition 5.1 is violated.

**Subcase 1: Trivial.** In the first subcase, we suppose \(\mathsf{LCS}(x,y)\le(1-\delta)|x|\).

**Lemma 5.5.** _If_ \(\mathsf{LCS}(x,y)\le(1-\delta)|x|\)_, then_ (3) _holds._

_Proof._ We always have \(\mathsf{Trivial}([0,|x|],[0,|y|])\ge\frac{|x|}{2}\) as \(\frac{|x|}{2}=1(x)=0(x)\le min(1(y),0(y))\). Hence, we have \(\mathsf{FullLCSAAlgorithm}(x,y)\ge\frac{|x|}{2}\ge\frac{1+\delta}{2}\mathsf{LCS}(x,y)\).

**Subcase 2: Locally imbalanced.** In the next subcase, we assume \(\mathsf{LCS}(x,y)\ge(1-\delta)|x|\) and that a nontrivial fraction of intervals are imbalanced. Since _x_ and _y_ have such a long LCS, we know that most intervals in _x_ appear nearly unmodified in _y_:

**Lemma 5.6.** _If_ \(w'\) _is a positive integer that divides_ |_x_| _and_ \(\mathsf{LCS}(x,y)\ge(1-\delta)|x|\)_, then at most_ \(\sqrt{\delta}\frac{|x|}{w^\prime}\) _intervals_ \(I_i\in\mathcal{I}_{w^\prime}\) _satisfy_ \(\mathsf{LCS}(I_i,J_{I_i}^\tau)>(1-\sqrt{\delta})|I_i|\).

