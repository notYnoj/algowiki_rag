<tbc>By comparing to the expectation of (B.1), this observation readily yields that \(f_\mathrm{null}(\alpha)=f_\mathrm{null}^\mathrm{ann}(\alpha)\). Thus, it is necessarily the case that either

\(\bullet\) there exists some critical value \(\alpha_*\le 1/2\) for which<tbc>

<tbc>\(\left\{\begin{array}{ c c }
f_\mathrm{null}(\alpha)<f_\mathrm{null}^\mathrm{ann}(\alpha) & \alpha>\alpha_*, \\
f_\mathrm{null}(\alpha)=f_\mathrm{null}^\mathrm{ann}(\alpha) & \alpha<\alpha_*;
\end{array}\right.\)<tbc>

\(\bullet\) it holds that \(f_\mathrm{null}(\alpha)<f_\mathrm{null}^\mathrm{ann}(\alpha)\) for all \(\alpha<1/2\).

In this sense, Theorem 1.1 exactly characterizes the relative asymptotic behavior of \(f_\mathrm{null}(\alpha)\) and \(f_\mathrm{null}^\mathrm{ann}(\alpha)\). In particular, it shows that there is no double phase transition past \(\alpha<1/2\), i.e., that the expectation always exhibits an exponential gap with the typical partition function which can be readily shown (via comparing the upper and lower bounds of Theorem 1.1) to diminish as \(\alpha\rightarrow 0\). We note that this is in contrast to other combinatorial properties of the null variant of the Random Subsequence Model which emerge for smaller values of \(\alpha\). For example, via a simple adaptation of the greedy algorithm, it is easy to show that \(\alpha=1/3\) is the threshold for \(X'\) to typically contain every string in {0,1}_<sup>M</sup>_ as a subsequence.

## Appendix C. Proof of Proposition 3.8

_Proof._ We fix a typical string \(x\in\{0,1\}^N\). Towards establishing (3.13), we define<tbc>

\(Z=\left(Z^{(1)},\dots,Z^{(B)}\right)\)

<tbc>to denote a random string resulting from independently including each bit of _x_ with probability \(\alpha\) (i.e., \(Z=\text{BDC}_{1-\alpha}(x)\)), with _Z_<sup>(_i_)</sup> the part of _Z_ which corresponds to the block _x_<sup>(_i_)</sup> for each \(i\in[B]\). It is clear that this random string _Z_ has law P_<sub>x</sub>_. It holds from the multiplicative Chernoff bound that

(C.1) \(q_\mathrm{len}:=\mathbb{P}\left(\left||Z^{(1)}|-\alpha b\right|>\delta\alpha b\right)^{\le^{(\text{Chernoff})}}2\mathrm{exp}\left(-\frac{\delta^2\alpha b}{3}\right)=2\mathrm{exp}\left(-\frac{\alpha b^{2\epsilon}}{3}\right)^{\le^{(b\mathrm{large})}}b^{-\epsilon}=\gamma.\)

It thus follows from the additive Chernoff bound that

\(\mathbb{P}\left(\left(Z^{(1)},\dots,Z^{(B)}\right)\notin\mathcal{N}\mathcal{E}_\mathrm{ind}(Z)\right)\le\mathbb{P}\left(\sum_{i=1}^B\unknown\left\{\left||Z^{(i)}|-\alpha b\right|>\delta\alpha b\right\}>\gamma B\right)\)<br>
\(\le^{(\text{Chernoff})}\mathrm{exp}\left(-B\cdot D_\mathrm{KL}\left(\gamma\|q_\mathrm{len}\right)\right)=\mathrm{exp}\left(-\frac{N}{b}\left[\gamma\mathrm{log}\left(\frac{\gamma}{q_\mathrm{len}}\right)+(1-\gamma)\mathrm{log}\left(\frac{1-\gamma}{1-q_\mathrm{len}}\right)\right]\right)\)<br>
\(\le^{(\text{C.1})}\mathrm{exp}\left(-\frac{N}{b}\left[\gamma\left(\mathrm{log}\gamma-\mathrm{log}2+\frac{\alpha b^{2\epsilon}}{3}\right)+(1-\gamma)\mathrm{log}\left(\frac{1-\gamma}{1-q_\mathrm{len}}\right)\right]\right)\)<br>
\(=\mathrm{exp}\left(-\frac{N}{b}\left[b^{-\epsilon}\left(-\epsilon\mathrm{log}b-\mathrm{log}2+\frac{\alpha b^{2\epsilon}}{3}\right)+(1-b^{-\epsilon})\mathrm{log}\left(\frac{1-b^{-\epsilon}}{1-o_b(1)}\right)\right]\right)\)<br>
\(\le^{(b\mathrm{large})}\mathrm{exp}\left(-\frac{N}{b}\cdot\frac{\alpha b^\epsilon}{6}\right)=e^{-\Omega(N)}.\) (C.2)

Next, we define the (deterministic) collection of indices

(C.3) \(\mathcal{I}_x:=\left\{i\in[B]:\Delta\big(x^{(i)}\big)\ge\sqrt{b}\right\}^{\Rightarrow^{(x\text{typical})}}|\mathcal{I}_x|\ge B/10.\)

