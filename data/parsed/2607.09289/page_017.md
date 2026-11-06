Combining (9) and (10), we obtain

\(\mathbb{P}[\mathcal{G}\cap\mathcal{H}]=\mathbb{P}[\mathcal{H}]-\mathbb{P}[\mathcal{G}^c\cap\mathcal{H}]\ge\Omega(1/n^2)-1/n^d=\Omega(1/n^2),\)

since _d\>_2. This completes the proof of Lemma 5.5.

We now turn to the time and space complexity analysis of Algorithm 3.

**Theorem 5.9.** _Assume that the minimum solution ratio satisfies_ \(\ell'\in[\epsilon,1-\epsilon]\) _for some constant_ \(\epsilon>0\)_. For every constant_ \(\alpha\in(0,1/2]\)_, there is a Monte Carlo algorithm for ESS that uses_ \(O^*(2^{\alpha n})\) _space and runs in_ \(O^*(2^{\tau_\mathrm{sbb}(\ell^\prime,\alpha)n})\) _time. Here,_ phi _is defined in_ (4)_, and_ \(\tau_\mathrm{sbb}(\ell',\alpha)\) _is defined as follows:_

\(\tau_\mathrm{sbb}(\ell',\alpha)=\left\{\begin{array}{ c c }
\frac{3}{2}(1-\mathrm{min}\{\alpha,1-\ell'\})-\frac{\alpha}{2} & \text{\textit{if}}\ell'>\frac{1}{2}, \\
\frac{3}{2}(1-\mathrm{min}\{\alpha,\mathrm{phi}(\ell')\})-\frac{\alpha}{2} & \text{\textit{otherwise}}.
\end{array}\right.\) (11)

_Proof._ We show that Algorithm 3 satisfies these complexity bounds. Line 2 of Algorithm 3 takes _O(np_)=_O_<sup>∗</sup>(_p_<sub>max</sub>) time and space. Since \(p_\mathrm{max}\le 2^{\alpha n}\) by the definition of _p_<sub>max</sub>, the space usage of Line 2 is bounded by \(O^*(2^{\alpha n})\). Moreover, the space usage of Line 3 is bounded by \(O^*(\mathrm{min}\{|C|,2^{\alpha n}\})\le O^*(2^{\alpha n})\). Therefore, the overall space complexity is bounded by \(O^*(2^{\alpha n})\).

Let _L_ be the list considered in Line 3. Since \(|L|=|C|\le O^*(2^n/p_\mathrm{max})\), we have polylog(|_L_|)=poly(_n_). Thus, the polylog(|_L_|) factor can be absorbed into the \(O^*(\cdot)\) notation.

By Lemma 5.3, Line 3 takes

\(O^*\left(\frac{|C|^{3/2}}{(\mathrm{min}\{|C|,2^{\alpha n}\})^{1/2}}\right)\le O^*\left(\frac{(2^n/p_\mathrm{max})^{3/2}}{2^{\alpha n/2}}\right)\)

time. Here, the inequality follows from \(|C|\le O^*(2^n/p_\mathrm{max})\) and \(2^{\alpha n}\le 2^n/p_\mathrm{max}\), where the latter holds because \(p_\mathrm{max}\le 2^{\alpha n}\) and \(\alpha\le 1/2\). Moreover, since \(p_\mathrm{max}\le 2^n/p_\mathrm{max}\le\frac{(2^n/p_\mathrm{max})^{3/2}}{2^{\alpha n/2}}\) , the running time of Line 2 is dominated by that of Line 3. By Lemma 5.5, repeating the algorithm poly(_n_) times amplifies the success probability to a constant, and this repetition does not affect the time complexity in \(O^*(\cdot)\) notation. Thus, the overall time complexity is \(O^*\left(\frac{(2^n/p_\mathrm{max})^{3/2}}{2^{\alpha n/2}}\right)\).

By the definition of _p_<sub>max</sub>, we have

\(p_\mathrm{max}=\left\{\begin{array}{ c c }
\Theta^*(2^{\mathrm{min}\{\alpha,1-\ell^\prime\}n}) & \text{if}\ell'>1/2, \\
\Theta^*(2^{\mathrm{min}\{\alpha,\mathrm{phi}(\ell^\prime)\}n}) & \text{otherwise}.
\end{array}\right.\)

Here, we used \(\left(\begin{array}{ c }
n-\ell \\
\lfloor(\ell-1)/2\rfloor
\end{array}\right)=\Theta^*(2^{\mathrm{phi}(\ell^\prime)n})\), which follows from \(\left|\frac{\lfloor(\ell-1)/2\rfloor}{n-\ell}-\frac{\ell'}{2(1-\ell^\prime)}\right|\le O(1/n)\) and Fact 2.2, using the assumption \(\ell'\in[\epsilon,1-\epsilon]\), which implies \(\ell=\Theta(n)\) and \(n-\ell=\Theta(n)\). Therefore, we obtain \(O^*\left(\frac{(2^n/p_\mathrm{max})^{3/2}}{2^{\alpha n/2}}\right)=O^*(2^{\tau_\mathrm{sbb}(\ell^\prime,\alpha)n})\), which completes the proof.

## 5.4 Space Bounded Modification of the Unbalanced ESS Algorithm

We introduce Algorithm 4, a space-bounded variant of the algorithm used in Lemma 3.9. This algorithm uses Lemma 5.10 as a subroutine. The _Target Equal-Subset-Sum Problem_ is a slightly generalized version of ESS. As stated in Lemma 5.10, it can be solved within the same time and space bounds as those in Lemma 3.9 \[25, Appendix E of the full version\]. We provide the details in Appendix C.

