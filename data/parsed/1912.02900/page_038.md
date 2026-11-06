around. The _second Wilber bound_ is:

\(\mathsf{WB}^{(2)}(X)=m+\sum_{p\in X}\mathrm{alt}(X,p).\)

The goal of this section is to prove the following:

**Theorem 4.16** _For every integer_ \(n'\)_, there is an integer_ \(n\ge n'\) _and a point set X that is a permutation with_ |_X_|=_n, such that_ \(\mathsf{WB}^{(2)}(X)\ge\Omega(n\mathrm{loglog}n)\) _but_ \(\mathsf{WB}(X)\le O(n\mathrm{logloglog}n)\).

As it is known that \(\mathsf{OPT}(X)\ge\mathsf{WB}^{(2)}(X)\) for any point set _X_ \[Wil89\], Theorem 4.16 is a stronger statement than Theorem 1.1. To prove Theorem 4.16, we use exactly the same permutation sequence _X_<sup>∗</sup> of size _N_<sup>∗</sup> that is constructed in Section 4.4. Since we already showed that \(\mathsf{WB}(X^*)\le O(N^*\mathrm{logloglog}N^*)\), it remains to show that \(\mathsf{WB}^{(2)}(X^*)\ge\Omega(N^*\mathrm{loglog}N^*)\).

We use the following claim of Wilber \[Wil89\]. bitwise reversal sequences:

**Claim 4.17 (\[Wil89\])** \(\mathsf{WB}^{(2)}(\mathsf{BRS}(n))=\Omega(n\mathrm{log}n)\) _for any n._

We extend this bound to the cyclically shifted BRS in the following lemma.

**Lemma 4.18** _For integers n\>_0_,s with_ \(0\le s<n\)_, let X be the sequence obtained by performing a cyclic shift to_ BRS(_n_) _by s units. Then_ \(\mathsf{WB}^{(2)}(X)=\Omega(n\mathrm{log}n)\).

**Proof:** Observe that, for any choice of _s_, there must exists a subsequence \(X'\) of _X_ such that \(X'\) is a copy of BRS(_n_-1) ( see Figure 4). It is shown in Lemma 6.2 of \[LT19\] that for any pair of sequences \(Z,Z'\) with \(Z'\subseteq Z\), \(\mathsf{WB}^{(2)}(Z')\le\mathsf{WB}^{(2)}(Z)\) holds. Therefore, we conclude that

\(\mathsf{WB}^{(2)}(Y)\ge\mathsf{WB}^{(2)}(\mathsf{BRS}(n-1))\ge\Omega(n\mathrm{log}n).\) \(\square\)

Now, we are ready to bound WB<sup>(2)</sup>(_X_<sup>∗</sup>).

**Lemma 4.19** \(\mathsf{WB}^{(2)}(X^*)=\Omega(N^*\mathrm{loglog}N^*)\).

**Proof:** Recall that \(\hat{X}\) is the union of the sets _X_<sup>0</sup>_,X_<sup>1</sup>_,...,X_<sup>_N_-1</sup> of points, where for all \(0\le s\le N-1\), set _X<sup>s</sup>_ is an exponentially-spaced BRS instance that is shifted by _s_ units. From the definition of WB<sup>(2)</sup>, it is easy to see that \(\mathsf{WB}^{(2)}(\hat{X})\ge\sum_{s=0}^{N-1}\mathsf{WB}^{(2)}(X^s)\). This is since, for all \(0\le s\le N-1\), for ever point \(p\in X^s\), \(\mathrm{funnel}(X^s,p)\subseteq\mathrm{funnel}(\hat{X},p)\), and moreover \(\mathrm{alt}(\hat{X},p)\ge\mathrm{alt}(X^s,p)\). From Lemma 4.18, we get that \(\mathsf{WB}^{(2)}(X^s)=\Omega(n\mathrm{log}n)\), where _n_=|_X<sup>s</sup>_|=log_N_. Therefore,

\(\mathsf{WB}^{(2)}(\hat{X})\ge N\cdot\Omega(n\mathrm{log}n)=\Omega(N^*\mathrm{loglog}N^*).\)

Finally, recall that the sequence _X_<sup>∗</sup> is obtained from \(\hat{X}\) by replacing each column \(C\hat{X}\) with a block B(_C_) of columns, and placing all points of \(\hat{X}\) lying in _C_ on the columns of B(_C_) so that they form a monotonically increasing sequence of length _n_. It is not hard to see that \(\mathsf{WB}^{(2)}(X^*)\ge\mathsf{WB}^{(2)}(\hat{X})\) which concludes the proof. \(\square\)

