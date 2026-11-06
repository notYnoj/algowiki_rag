Let \(\mathbf{E}\in\unknown_q^m\) denote the random variable representing the full error vector obtained by drawing _m_ independent errors from \(\nu_p\). Let \(P_\mathrm{W}^\mathrm{ML}(G,p,\theta)\) be the minimum whole-word error probability in recovering **E** from _B<sup>T</sup>_**E**, and put \(P_\mathrm{S}^\mathrm{ML}=1-P_\mathrm{W}^\mathrm{ML}\). Thus

\(P_\mathrm{S}^\mathrm{ML}(G,p,\theta)=\sum_{\mathbf{s}\in\unknown_q^V}\mathrm{max}_{\mathbf{e}\in\unknown_q^E}\prod_{j=1}^m\nu_p(e_j).\) (59)

This is also ML codeword success for a uniformly distributed transmitted codeword, and it is independent of the choice among equal-likelihood maximizers. For uniform \(\theta\), we retain the notation \(P_\mathrm{W}^\mathrm{ML}(G,p)\). For _p\<_1-_q_<sup>-1</sup>, the likelihood of an error decreases with Hamming weight, so ML syndrome decoding is minimum-weight decoding. Its worst-case hardness for _q\>_2 does not preclude efficient recovery at lower noise levels, as the LP guarantees below demonstrate.

From the Moore bound \[Big93\], the girth for _D_-regular graphs can be at most logarithmic in terms of the number of vertices, as given by

\(g(G)\le 2\mathrm{log}_{D-1}(n)+O(1).\) (60)

However, many graphs such as random regular graphs contain short cycles whose distribution is Poissonian \[MWW04\]. The presence of these short cycles hurts the decoding performance, leading to a word error rate bounded away from zero.

**Theorem 3** (Error floor from short cycles)**.** _Fix_ \(D\ge 3\)_, a finite field_ \(\unknown_q\)_, an even replacement distribution_ \(\theta\)_, and_ 0_\<p\<_1/2_. If G<sub>n</sub> is uniform among simple D-regular graphs on n labeled vertices, then_

\(\mathrm{liminf}_{n\rightarrow\infty}\unknown_{G_n}P_\mathrm{W}^\mathrm{ML}(G_n,p,\theta)\ge(p\theta_\mathrm{max})^3\left(1-\mathrm{exp}\left[-\frac{(D-1)^3}{6}\right]\right)>0,\) (61)

_where_ \(\theta_\mathrm{max}:=\mathrm{max}_a\theta(a)\)_. The limit is through n\>D with Dn even. The same statement holds after conditioning on connectedness._

_Proof._ Whenever _G<sub>n</sub>_ contains a triangle, select one deterministically and orient its unit circulation **f**. Choose \(a\neq 0\) with \(\theta(a)=\theta_\mathrm{max}\). With probability \((p\theta_\mathrm{max})^3\), the error equals _a_**f** on the triangle, because \(\theta\) is even. Subtracting this circulation leaves the syndrome and all other coordinates unchanged, while replacing three entries of probability \(p\theta_\mathrm{max}\) by zero entries of probability \(1-p>p\theta_\mathrm{max}\). Thus the resulting error is strictly more likely, and every ML decoder fails on the original error. Therefore

\(P_\mathrm{W}^\mathrm{ML}(G_n,p,\theta)\ge(p\theta_\mathrm{max})^3\mathbf{1}_{\{G_n\text{contains a triangle}\}}.\) (62)

The triangle count converges to a Poisson random variable with mean (_D_-1)<sup>3</sup>/6 \[MWW04; Joh15\]. Averaging the preceding inequality and taking the lower limit proves (61). The probability of connectedness tends to one \[Bol01\], so conditioning on connectedness leaves the same limit.

Excluding cycles only up to any fixed length still leaves a positive error floor, by the joint Poisson limit for the remaining fixed cycle lengths \[MWW04; Joh15\]. We therefore employ an ensemble with girth growing logarithmically.

