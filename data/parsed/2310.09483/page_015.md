Let \(C=\#\{x_i\in Z|x_i>x_L+1\}\). Clearly, \(x_i>x_L+1\Longrightarrow x_i\unknown\in U\), so \(C\le A=\sum_iA_i\). We have:

\(Pr[C\ge 6B]\le Pr[A\ge 6B]\)<br>
\(\le e^{-7B\big(2\big(\frac{6}{7}-\frac{3}{4}\big)^2\big)}\)<br>
\(=e^{-\frac{9B}{56}}\)<br>
\(=e^{-logN\frac{9c_3}{14}}\)<br>
\(=N^{-\frac{9c_3}{14}}\)

Thus, choosing \(c_3\ge\frac{14(r+1)}{9}\)<tbc>

\(\le\frac{1}{N^{r+1}}\)

<tbc>By a union bound:

\(Pr[C\ge 5B\text{on some iteration}]\le\frac{n}{B}\frac{1}{N^{r+1}}\)<br>
\(<\frac{1}{N^r}.\)

Here we use the generalized Chernoff bound from Theorem 1.1 of \[IK10\].

Since we initially have |_Y|\<|<o>Y</o>_|, elements are only added in this case, so if we had \(min(X\backslash Y)\ge x_L-1\) before this phase, this must still be the case. If this happens, and the conclusion of Lemma 4.7 holds, then after this phase, \(max(Y)\le x_L+2\) and \(min(X\backslash Y)\ge x_L-1\), so \(\overline{Y}\ge_4Y\) . Furthermore, after this phase, both _Y_ and <o>_Y_</o> must have size at least \(\frac{n}{8}\), as otherwise we would have added elements to the smaller one in this phase. Thus, if these conditions hold, then we get the desired result.

## 4.4 Tying it together

We conclude the probability bounds for the algorithm and describe the comparison and round complexity.

**Lemma 4.8.** _For any constant r\>_0_, we can choose c_<sub>1</sub>_,c_<sub>2</sub>_,c_<sub>3</sub> _sufficiently large such that the probability that we split X into sets Y,<o>Y</o> such that_ \(\overline{Y}\ge_4Y\) _is_ \(>1-\frac{1}{N^r}\).

_Proof._ As described in the previous sections, there are 6 failure points at which something may go wrong and we may end up with \(\overline{Y}\unknown\ge_4Y\) . By a union bound, it follows that the probability that \(\overline{Y}\ge_4Y\) is at least \(1-\frac{6}{N^{r+1}}>1-\frac{1}{N^r}\) for sufficiently large _c_<sub>1</sub>_,c_<sub>2</sub>_,c_<sub>3</sub> as desired.

**Theorem 4.9.** _For any constant r\>_0_, we can choose c_<sub>1</sub>_,c_<sub>2</sub>_,c_<sub>3</sub> _sufficiently large such that `RSort` returns a_ 4_-approximate sorting with probability_ \(>1-\frac{1}{N^r}\).

_Proof._ Recall that it is sufficient for every recursive call to satisfy \(\overline{Y}\ge_4Y\) . Since we reduce the size of the input by a constant factor in each recursive call, there must be _O(N_) total recursive calls. Thus, by a union bound, we return a 4-approximate sorting with probability at least \(1-O(N)\frac{1}{N^{r+2}}>1-\frac{1}{N^r}\) as desired.

**Theorem 4.10. _RSort uses O(N_log<sup>2</sup>_N_) _comparisons._

_Proof._ It is clear that any recursive call takes _O(n_log_N_) comparisons. It follows by a well known recurrence that _O(N_log<sup>2</sup>_N_) comparisons are thus required in total.

