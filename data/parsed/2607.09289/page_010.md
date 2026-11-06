<tbc>_and_

\(\sigma_\text{rrb}(\ell',k')=\left\{\begin{array}{ c c }
\ell'-k' & \text{\textit{if}}\ell'-k'>1/2, \\
1-\text{phi}(\ell'-k') & \text{\textit{otherwise.}}
\end{array}\right.\)

_Proof._ Let \(x=\ell'-k'\). As in Lemma 3.4, set \(p_\text{max}=2^{n-(\ell-k)}=\Theta^*(2^{(1-x)n})\) if _x\>_1/2, and \(p_\text{max}=\genfrac(){pt}{2}{n-(\ell-k)}{\lfloor(\ell-k-1)/2\rfloor}=\Theta^*(2^{\text{phi}(x)n})\) otherwise. The latter equality follows from \(\left|\frac{\lfloor(\ell-k-1)/2\rfloor}{n-(\ell-k)}-\frac{x}{2(1-x)}\right|\le O(1/n)\), together with Fact 2.2. Here, we use the assumptions on \(\ell\) and \(k'\), which imply \(\ell-k=\Theta(n)\) and \(n-(\ell-k)=\Theta(n)\).

By Lemma 3.7, one trial of Algorithm 2 runs in _O_<sup>∗</sup>(max{2_<sup>xn</sup>,_2<sup>_n/_2</sup>})=_O_<sup>∗</sup>(2_<sup>xn</sup>_) time and uses _O_<sup>∗</sup>(max{2_<sup>xn</sup>,_2<sup>_n/_4</sup>})=_O_<sup>∗</sup>(2_<sup>xn</sup>_) space when _x\>_1/2. In the remaining case, one trial runs in _O_<sup>∗</sup>(max{2<sup>(1-phi(_x_))_n_</sup>,2<sup>_n/_2</sup>}) time and uses _O_<sup>∗</sup>(max{2<sup>(1-phi(_x_))_n_</sup>,2<sup>_n/_4</sup>})=_O_<sup>∗</sup>(2<sup>(1-phi(_x_))_n_</sup>) space. By Lemma 3.4, one trial succeeds with probability at least \(\Omega^*\left(\genfrac(){pt}{2}{\ell}{2k}/\genfrac(){pt}{2}{n}{2k}\right)\). Hence, repeating the algo rithm \(O^*(\genfrac(){pt}{2}{n}{2k}/\genfrac(){pt}{2}{\ell}{2k})=O^*(2^{\text{repl}(\ell^\prime,k^\prime)n})\) times amplifies the success probability to a constant, where the bound follows from \(|2k/n-2k'|\le O(1/n)\) and \(|2k/\ell-2k'/\ell'|\le O(1/\ell)\), together with Fact 2.2.

Therefore, when _x\>_1/2, the total running time is \(O^*(2^{(x+\text{repl}(\ell^\prime,k^\prime))n})\), and the space usage is _O_<sup>∗</sup>(2_<sup>xn</sup>_). When \(x\le 1/2\), the total running time is \(O^*\left(2^{(\text{max}\{1-\text{phi}(x),1/2\}+\text{repl}(\ell^\prime,k^\prime))n}\right)\), and the space usage is \(O^*(2^{(1-\text{phi}(x))n})\). Since \(x=\ell'-k'\), these bounds are exactly \(O^*(2^{\tau_\text{rrb}(\ell^\prime,k^\prime)n})\) time and \(O^*(2^{\sigma_\text{rrb}(\ell^\prime,k^\prime)n})\) space, as claimed.

In the remainder of this section, we mainly focus on the case \(\ell'-k'>1/2\). The case \(\ell'-k'\le 1/2\) will be used later when deriving the time-space tradeoff in Section 5. The authors of \[25\] presented the _UnbalancedEqualSubsetSum_ algorithm, which is particularly useful when \(\ell'\) is close to 0 or 1.

**Lemma 3.9** (\[25, Theorem 3.3\])**.** _Let_ \(\ell'=\ell/n\) _be the minimum solution size ratio. There is a Monte Carlo algorithm for ESS that runs in_ \(O^*(2^{\frac{n}{2}(H(\ell^\prime)+\ell^\prime)})\) _time and uses_ \(O^*(2^{\frac{n}{4}(H(\ell^\prime)+\ell^\prime)})\) _space._

The authors of \[25\] actually give an algorithm using \(O^*(2^{\frac{n}{2}(H(\ell^\prime)+\ell^\prime)})\) space. This space usage can be reduced to \(O^*(2^{\frac{n}{4}(H(\ell^\prime)+\ell^\prime)})\) by applying the technique of Schroeppel and Shamir \[29\]; we provide the details in Appendix B.3. We now restate and prove Theorem 1.3.

**Theorem 1.3.** _There exists a Monte Carlo algorithm for ESS that runs in O_<sup>∗</sup>(1.6994_<sup>n</sup>_) _time and uses O_<sup>∗</sup>(1.5664_<sup>n</sup>_) _space._

_Proof._ Let \(\gamma_1\) be the value of \(\ell'\) in the interval \((1/\sqrt{2},1-\epsilon]\) satisfying

\(\frac{H(\ell')+\ell'}{2}=\tau_\text{rrb}\left(\ell',\frac{\sqrt{2}\ell'-1}{2(\sqrt{2}-1)}\right).\) (6)

We define \(\alpha_1\) by

\(\alpha_1=\gamma_1-\frac{\sqrt{2}\gamma_1-1}{2(\sqrt{2}-1)}.\) (7)

Numerically, these values satisfy \(0.79158<\gamma_1<0.79159\) and \(0.64737<\alpha_1<0.64738\).

For \(\ell'\in(0,1/2]\cup(\gamma_1,1]\), we apply Lemma 3.9. For \(\ell'\in(1/2,\gamma_1]\), we apply Theorem 3.8 with \(k'=\text{max}\{0,\ell'-\alpha_1\}\) for each value of \(\ell'\). Then the worst-case time exponent, namely the constant _c_ such that the running time is _O_<sup>∗</sup>(2_<sup>cn</sup>_), can be expressed as

\(\text{max}\left\{\text{max}_{\ell^\prime\in(0,1/2]\cup(\gamma_1,1]}\frac{H(\ell')+\ell'}{2},\text{max}_{\ell^\prime\in(1/2,\gamma_1]}\tau_\text{rrb}\left(\ell',\text{max}\{0,\ell'-\alpha_1\}\right)\right\},\)

