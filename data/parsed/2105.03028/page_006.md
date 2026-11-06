## 23:6 Improved Approximation for Longest Common Subsequence over Small Alphabets

\(\blacktriangleright\) **Lemma 10** (Balanced Inputs, adapted from Lemma 3.2 of [21])**.** _For all sufficiently small_ \(\rho>0\)_, if either A or B is_ \(\rho\)_-balanced, we can_ \((1/s+\gamma)\)_-approximate_ LCS(_A,B_) _in truly subquadratic time, where_ \(\gamma\) _is some positive constant depending on_ \(\rho\).

**Proof.** We reduce the problem to approximating the edit distance between _A_ and _B_.

Without loss of generality assume _A_ is \(\rho\)-balanced. This means that all of its character frequencies are at least \((1/s-\rho)n\). So there exists a unary common subsequence of _A_ and _B_ of at least this length. If this is a \((1/s+\gamma)\) approximation we are done. Otherwise the LCS must be quite large:

\(LCS(A,B)>s(1/s-\rho)n-s\gamma n=(1-s(\rho+\gamma))n.\)

Recall from Lemma 6 that

\(ED(A,B)+2\cdot LCS(A,B)=2n,\)

where ED(_A,B_) denotes the (no substitutions) edit distance of _A_ and _B_. Using the ED approximation of [5] with some approximation ratio _c\>_3 we recover an LCS approximation of length at least

\(n-c(n-LCS(A,B))>n(1-cs(\rho+\gamma))\)

so as long as we have \(1-cs(\rho+\gamma)\ge 1/s+\gamma\), this approximation is strong enough. This inequality holds when

\(\gamma\le\frac{s-1-cs^2\rho}{s(1+cs)}.\)

We can ensure it does by picking \(\rho\) small enough that the numerator of the right hand side above is positive and then taking \(\gamma\) smaller than the right hand side. Note that smaller values of \(\rho\) correspond to larger values of \(\gamma\). \(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 11** (Balanced LCS)**.** _If the LCS of A and B is not_ \(\rho\)_-balanced, then in linear time we can_ \((1/s+\rho/(s-1))\)_-approximate_ LCS(_A,B)._

**Proof.** Returning the longest common unary subsequence gives the desired approximation. To see this, let \(\sigma_\mathrm{max}\) and \(\sigma_\mathrm{min}\) be the most frequent and least frequent characters in the LCS respectively. Since the LCS is not balanced, either \(\sigma_\mathrm{max}\) makes up more than a \((1/s+\rho)\) fraction of all symbols in the LCS, or \(\sigma_\mathrm{min}\) makes up fewer than a \((1/s-\rho)\) fraction of the symbols in the LCS.

In the latter case, the _s_-1 members of the alphabet besides \(\sigma_\mathrm{min}\) must account for at least an \(((s-1)/s+\rho)\) fraction of characters in the LCS. Among these, \(\sigma_\mathrm{max}\) appears the most often, which means by averaging that \(\sigma_\mathrm{max}\) accounts for at least a

\(\frac{1}{s}+\frac{\rho}{s-1}\)

fraction of all symbols in the LCS.

In either case, \(\sigma_\mathrm{max}\) makes up at least a \((1/s+\rho/(s-1))\) fraction of the symbols in the LCS. Then the string consisting of \(\sigma_\mathrm{max}\) repeated \(min(\sigma_\mathrm{max}(A),\sigma_\mathrm{max}(B))\) times is a common subsequence of _A_ and _B_ which has at least as many instances of \(\sigma_\mathrm{max}\) as the LCS does, and thus yields the desired approximation. \(\blacktriangleleft\)

