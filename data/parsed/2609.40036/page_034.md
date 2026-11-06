_Proof._ On the graph event A_<sub>n</sub>_, apply (126) to the enumerator. For \(w\le a_*n\), summing over all excesses costs at most _e<sup>L<sub>w</sub></sup>_, giving

\(\sum_t\unknown[\mathbf{1}_{\mathcal{A}_n}A_{w,t}]B_\Theta(p)^w\le\frac{qD}{D-1}\mathrm{exp}\{w[\mathrm{log}R+\Psi(a_*)+\xi_n]\}.\) (143)

All nonzero flows have weight at least \(g\rightarrow\infty\), so the sum of these bounds tends to zero.

For the remaining weights allowed by (128), put _a=w/n_ and _y=qa_. Since \(a\le 2u<1/4\), we have \(L_w\le 2w\sqrt{y}\). Set _T_<sub>0</sub>=⌈2_u_<sup>2</sup>_n_⌋ and _h=K/y_<sup>3/2</sup>. For \(a\ge a_*\), \(h\le 1/8\), and

\(\sum_{t=0}^{T_0}\frac{L_w^{2t}}{(2t)!}\le h^{-2T_0}e^{hL_w},\) (144)

\(\frac{1}{w}\mathrm{log}(h^{-2T_0}e^{hL_w})\le\frac{2K}{y}\left(1+\mathrm{log}\frac{y^{3/2}}{K}\right)\le b_0K^{1/3}.\) (145)

The last function is decreasing for \(y\ge 4K^{2/3}\), and its value at that endpoint is _b_<sub>0</sub>_K_<sup>1/3</sup>. Thus each remaining weight contributes at most

\(\frac{qD}{D-1}\mathrm{exp}\{w[\mathrm{log}R+8u+b_0K^{1/3}+\xi_n]\}.\) (146)

Summing from \(w\ge a_*n\) gives an exponentially small bound. If that range is empty, nothing is required there.

Finally add \(\mathrm{Pr}(\mathcal{A}_n^c)=o(1)\) and the channel-budget probability (127), and divide by Pr(E_<sub>n</sub>_)=1-_o_(1). No independence between the budget and favorability has been assumed: the budget was used only to restrict the indices of a union bound.

**Lemma 6** (Recovery after one-coordinate changes)**.** _Under (142), with probability tending to one over the Linial-Simkin graph and the errors, every word at Hamming distance at most one from E is the unique minimum-weight representative of its syndrome. In particular, a fixed lexicographic minimum-weight syndrome decoder corrects all these words._

_Proof._ For a connected nonzero flow _f_, write _Q<sub>f</sub>(E_)=|_E_|-|_E-f_|. Changing one error coordinate changes _Q<sub>f</sub>_ by at most two. If a word at distance at most one from _E_ is not uniquely minimum- weight, a connected component of a competing flow therefore satisfies \(Q_f(E)\ge-2\). The common tilt in (130) gives

\(\mathrm{Pr}\{Q_f(E)\ge-2\}\le e^{2t_\Theta} B_\Theta(p)^w.\) (147)

For such a flow, \(|E-f|\le|E|+2\). The deterministic comparisons in Lemma 4 now give

\(w\le 2|E|+2,t\le\mathcal{D}(E)+2.\) (148)

Outside the same exceptional event of probability \(\eta_n\), the budget is therefore \(w\le 2un+2\), \(t\le 2u^2n+2\). Repeat the union bound in Proposition 1. The factor \(e^{2t_\Theta}\) is fixed, and the additive changes to the budget contribute _o_(1) to the exponent per edge. The two strict exponent inequalities in (142) still make the sum tend to zero. Since _u\<_1/8, the enlarged weight range lies below _n/_4 for all sufficiently large _n_.

