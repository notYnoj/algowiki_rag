Lemma 4 for completeness. That is, we describe a family of simple algorithms parameterized by \(k\le logn\) that gives a matching upper bound of

\(O\big(\big(\mathsf{Alt}(X)+m\cdot\frac{logn}{k}\big)\cdot(logk+1)\big).\)

In this algorithm, the fixed cost is \(\beta(n)=\Theta\big(\frac{lognlogk}{k}\big)\) and multiplicative factor \(\alpha(n)=\Theta(logk)\). We just proved that any algorithm with fixed cost \(\beta(n)\) must have

\(\alpha(n)\ge\Omega\big(log\big(\frac{logn}{\beta(n)}\big)\big)=\Omega\big(log\big(\frac{k}{logk}\big)\big)=\Omega(logk),\)

so our trade-off is optimal for any sufficiently large \(k\le logn\).

_Note:_ The trade-off above suggests that there is some leeway in the other direction, i.e. we could have an algorithm with the same multiplicative factor of _O_(log_k_) but a reduced fixed cost of \(\frac{logn}{(logk)^C}\) for any _C\>_1 we choose. And this is indeed the case: we simply need to change variables

\(k':=k^{1/C}\Longrightarrow O\big((logk)\overline{\mathsf{Alt}}(X)+\frac{lognlogk}{k}\big)\le O\big((logk')\overline{\mathsf{Alt}}(X)+\frac{logn}{(k')^{C-o(1)}}\big).\)

\(\blacktriangleright\) **Theorem 27** (Restatement and full version of Theorem 5)**.** _Let_ \(\alpha:\mathbb{N}\times\mathbb{R}_{\ge 1}\rightarrow\mathbb{R}_{\ge 1}\) _be any function and let A be some BST algorithm. Denote the amortized cost of A on an access sequence X as <o>A</o>(X). Suppose that for all access sequences X over n keys, we have_

\(\overline{A}(X)\le\alpha\big(n,\overline{\mathsf{OPT}}(X)\big)\cdot\big(\overline{\mathsf{Alt}}(X)+1\big).\)

_Then_ \(\alpha(n,s)\ge\Omega\big(log\big(\frac{logn}{s}\big)\big)\) _for infinitely many values of n, and (for each such n) for a set of values for s that ranges from O_(1) _to_ \(\Omega(logn)\) _and are spaced by at most a constant factor._

**Proof.** Again, we will show that the result holds under the weaker assumption that the theorem holds for the _optimal_ amortized cost:

\(\overline{\mathsf{OPT}}(X)\le\alpha\big(n,\overline{\mathsf{OPT}}(X)\big)\cdot\big(\overline{\mathsf{Alt}}(X)+1\big).\)

The above inequality must in particular hold for the access sequence \(Y_n^{\circ R}\) from Theorem 2, for any power-of-two _R_. This gives us

\(\left\{\begin{array}{ c } \overline{\mathsf{OPT}}\big(Y_n^{\circ R}\big)\le\alpha\big(n,\overline{\mathsf{OPT}}(Y_n^{\circ R})\big)\cdot\big(\overline{\mathsf{Alt}}(Y_n^{\circ R})+1\big)\le O\big(R\alpha\big(n,\overline{\mathsf{OPT}}(Y_n^{\circ R})\big)\big) \\ \overline{\mathsf{OPT}}\big(Y_n^{\circ R}\big)\ge\Omega\big(\mathsf{Funnel}\big(Y_n^{\circ R}\big)\big)\ge\Omega\big(Rlog\big(\frac{logn}{R}\big)\big). \end{array}\right.\)

Combining these inequalities, we obtain

\(\alpha\big(n,\overline{\mathsf{OPT}}(Y_n^{\circ R})\big)\ge\Omega\big(log\big(\frac{logn}{R}\big)\big)\ge\Omega\big(log\big(\frac{logn}{\overline{\mathsf{Alt}}(Y_n^{\circ R})}\big)\big)\ge\Omega\big(log\big(\frac{logn}{\overline{\mathsf{OPT}}(Y_n^{\circ R})}\big)\big).\)

It is easy to verify that \(\overline{\mathsf{OPT}}(Y_n^{\circ R})\) can range from _O_(1) to \(\Omega(logn)\) and that the available values spaced by at most a constant factor. \(\blacktriangleleft\)

