where the last step holds as long as _C<sub>O</sub>_ is large enough. For Funnel, by Theorem 20 we have

\(\overline{\text{Funnel}}\big(Y_\sqrt{n}^{\circ R}\big)\ge\overline{\text{Funnel}}\big(Y_\sqrt{n}^{\circ R}\big)+\frac{\sqrt{n}\cdot\overline{\text{Funnel}}\big(Y_\sqrt{n}^{\circ R}\big)}{\sqrt{n}}-O(1)\ge C_\Omega(R+1)log\big(\frac{log\sqrt{n}}{R}\big)-O(1)=C_\Omega\frac{2R+1}{2}log\big(\frac{logn}{2R}\big)+\frac{C_\Omega}{2}log\big(\frac{logn}{2R}\big)-O(1)\ge C_\Omega\frac{2R+1}{2}log\big(\frac{logn}{2R}\big)+\frac{C_\Omega}{2}log\big(\frac{K}{2}\big)-O(1)\ge C_\Omega\frac{2R+1}{2}log\big(\frac{logn}{2R}\big),\)

where the penultimate step holds because \(R\le\frac{logn}{K}\) , and the last step holds as long as _K_ is large enough. \(\blacktriangleleft\)

## 4.2 Optimality of Tango Trees

We are ready to prove Theorem 3. \(\blacktriangleright\) **Theorem 26** (Restatement of Theorem 3)**.** _Let_ \(\alpha,\beta:\mathbb{N}\rightarrow\mathbb{R}_{\ge 1}\) _be any functions and let A be some BST algorithm. Denote the amortized cost of A on an access sequence X as <o>A</o>(X). Suppose that for all access sequences X over n keys, we have_

\(\overline{A}(X)\le\alpha(n)\overline{\text{Alt}}(X)+\beta(n).\)

_Then_ \(\alpha(n)\ge\Omega\big(log\big(\frac{logn}{\beta(n)}\big)\big)\) _for infinitely many values of n._ **Proof.** In fact we will show that the result holds under the weaker assumption that the theorem holds for the _optimal_ amortized cost: \(\overline{\text{OPT}}(X)\le\alpha(n)\overline{\text{Alt}}(X)+\beta(n).\) The above inequality must in particular hold for the access sequence \(Y_n^{\circ R}\) from Theorem 2, where we let _R_ be the largest power of two such that \(R\le\beta(n)\). This gives us

\(\left\{\begin{array}{ c } \overline{\text{OPT}}\big(Y_n^{\circ R}\big)\le\alpha(n)\overline{\text{Alt}}(X)+\beta(n)\le O(R(\alpha(n)+1)) \\ \overline{\text{OPT}}\big(Y_n^{\circ R}\big)\ge\Omega\big(\overline{\text{Funnel}}\big(Y_n^{\circ R}\big)\big)\ge\Omega\big(Rlog\big(\frac{logn}{R}\big)\big). \end{array}\right.\)

Combining these inequalities, we obtain

\(R(\alpha(n)+1)\ge\Omega\big(Rlog\big(\frac{logn}{R}\big)\big)\Longrightarrow\alpha(n)\ge\Omega\big(log\big(\frac{logn}{R}\big)\big)\ge\Omega\big(log\big(\frac{logn}{\beta(n)}\big)\big)\) (where the implication uses the fact that \(\alpha(n)\ge 1\)). \(\blacktriangleleft\)

### Optimal Trade-off

The matching trade-offs for \(\alpha(n)\) and \(\beta(n)\) follows from Tango trees [16] as discussed in the introduction. We provide an alternate proof by designing an algorithm parameterized by _k_ in

