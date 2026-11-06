<tbc>These bounds together show that the uniform capacity decays polynomially but faster than linearly in 1-_p_ as \(p\rightarrow 1\).

We note that \(f_\mathrm{null}^\mathrm{ann}(\alpha)\) trivially admits an exact analytic formula. Indeed, we have

\(f_\mathrm{null}^\mathrm{ann}(\alpha)=\mathrm{lim}_{N\rightarrow\infty}\frac{1}{N}\mathrm{log}\mathbb{E}[Z_{X^\prime,Y}]\)<br>
\(=\mathrm{lim}_{N\rightarrow\infty}\frac{1}{N}\mathrm{log}\left(|\Sigma_{N,M}|2^{-M}\right)=\mathrm{lim}_{N\rightarrow\infty}\frac{1}{N}\mathrm{log}\left(\genfrac(){pt}{2}{N}{M}2^{-M}\right)=h(\alpha)-\alpha\mathrm{log}2.\)

The situation is significantly more involved for the annealed free energy of the planted model

\(f_\mathrm{pl}^\mathrm{ann}(\alpha)=\mathrm{lim}_{N\rightarrow\infty}\frac{1}{N}\mathrm{log}\mathbb{E}[Z_{X,Y}].\)

However, our next result gives an exact analytic formula for this quantity as well.

**Theorem 1.3** (Annealed free energy of the planted model)**.** _For every_ \(\alpha\in(0,1)\)_, define_<tbc>

\(\Delta(\alpha)=\sqrt{9\alpha^2-4\alpha+4};x_\alpha=\frac{\Delta(\alpha)-3\alpha}{2};y_\alpha=\frac{(3\alpha+2-\Delta(\alpha))^2}{2(\Delta(\alpha)-3\alpha)(2+\Delta(\alpha)-3\alpha)}.\)

<tbc>_Then_ \((x_\alpha,y_\alpha)\in(0,\infty)^2\) _and_

\(f_\mathrm{pl}^\mathrm{ann}(\alpha)=-h(\alpha)-\alpha\mathrm{log}2-\mathrm{log}x_\alpha-\alpha\mathrm{log}y_\alpha.\)

Note that, by Jensen’s inequality, \(f_\mathrm{pl}^\mathrm{ann}(\alpha)\) is an upper bound on \(f_\mathrm{pl}(\alpha)\). Combining this with (1.3) yields an upper bound on the uniform capacity of the deletion channel for all deletion probabilities. We note that this is one of the very few known analytic bounds for the deletion channel [DG01; Che19], and is numerically far closer than any other upper bounds of which we are aware, albeit bounding the uniform capacity rather than the full capacity. We view this as further evidence that the uniform capacity is a fruitful stepping stone towards better understanding the full capacity problem. Finally, we note that [PIW24] previously gave an efficient _algorithm_ to compute the annealed free energy in the planted model to any desired precision. Our result significantly improves on theirs by being exact and analytic.

We conclude this section by returning to the connection with directed polymers. As we mentioned in Section 1.1, the Random Subsequence Model can be understood as a directed polymer model in a random "rank-one" environment. In the directed polymer literature, only models with special algebraic structure have been found to admit exact solutions. Since this kind of structure does not seem to be present in the Random Subsequence Model, the experience of the directed polymer literature suggests that it may be intractable to obtain exact analytic formulas for _f_<sub>pl</sub> or _f_<sub>null</sub> with existing mathematical techniques, and results of the kind proved in Theorem 1.1 and Theorem 1.3 may be the best we can hope for. However, we think that a promising direction is to study variants of the Random Subsequence Model which do admit such exact solutions. There is a long tradition of doing this in the literature on spin glasses. For example, the Sherrington-Kirkpatrick model, which led to tremendous progress, was first proposed as a simplified, mean-field version of the earlier Edwards-Anderson model [EA75; SK75]. In our case, the natural solvable analogue is the Strict-Weak Polymer Model, introduced and solved in [CSS15]. After a trivial mapping, this corresponds to exactly the same recurrence as (1.5), but where we take _B_ to have i.i.d. Gamma(_a,b_) entries. The exact solution in this case is (see [CSS15, Theorem 1.3])

(1.9) \(\mathrm{lim}_{N,M\rightarrow\infty M/N=\alpha}\frac{1}{N}\mathbb{E}\left[\mathrm{log}Z_{N,M}\right]=\mathrm{inf}_{\lambda>0}\left\{-(1-\alpha)\Psi(\lambda)+\Psi(a+\lambda)+\alpha\mathrm{log}b\right\},\)

where \(\Psi\) is the digamma function

\(\Psi(x)=\frac{d}{dx}\mathrm{log}\Gamma(x)=\frac{\Gamma'(x)}{\Gamma(x)}.\)

