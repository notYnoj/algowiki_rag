## J.1 Compute-only model

Given that our core focus is on estimating doubling times in effective compute, one natural parameterization is to directly consider total training compute _C_, in particular,

\(L=\gamma'+\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{compute}(\mathrm{log}C-\mathrm{log}C_0)].\) (33)

Here \(\gamma'\) is defined similarly to the "primed" constants above, i.e. \(\gamma'=\gamma+\gamma_\mathrm{PTB}x_\mathrm{PTB}+\gamma_\mathrm{WT2}x_\mathrm{WT2}\), and we have the approximate relation that _C_≈6_ND_ (Hoffmann et al. 2022). However, this model has a tendency to yield implausible results, in particular with a very small scale exponent \(\alpha_\mathrm{compute}\) and a very short effective compute doubling time (on the order of 1-5 months).

We omit this model because we believe there are two reasons to expect this model to be strongly misspecified. The first reason is that the model scaling does not accurately reflect complementarities between scaling parameter and data. For illustration, compare the following two equations:

\(L=E+\frac{A}{N^\alpha}+\frac{B}{D^\beta}\) (34)

\(L=E+\frac{A}{C^\alpha}=E+\frac{A}{(6ND)^\alpha}\) (35)

where _E_ is the irreducible loss, and \(A,B,\alpha,\beta\) are constants. In equation 34, reductions to the loss are bottlenecked by a lack of sufficient data _D_. This bottleneck does not exist in the case of 35, where scaling _N_ arbitrarily would bring you to the irreducible loss _E_. This model thus unrealistically suggests equivalent performance between a 1-parameter model trained on 10<sup>24</sup> tokens, and a 10<sup>12</sup> parameter model trained on 10<sup>12</sup> tokens. Of course, such extreme choices of parameters _N_ and dataset size _D_ are implausible in practice, but nevertheless we do see clear variation in how these values are chosen in practice. For instance, Figure 12 shows a plot log<sub>10</sub>(_N/D_) for models across different years, spanning over five orders of magnitude over this time period. This is in spite of the estimate by Hoffmann et al. 2022 that _N/D_ should be _O_(1) for compute-optimal training.

A second way in which equation 33 is misspecified is due to its unrealistic scaling behavior. To see why this is the case, we compare the difference between the reducible loss terms in equations 34 and 35, by writing them as a single fraction with the same denominator \((ND)^\alpha\). For illustration purposes, we also assume that \(\alpha=\beta\) and _A=B_, which simplify our argument without changing the core conclusion. If we then factor out the coefficient _A_, we then have that

\(L_H\propto\frac{1}{N^\alpha}+\frac{1}{D^\alpha}=\frac{N^\alpha+D^\alpha}{(ND)^\alpha}\) (36)

\(L_C\propto\frac{1}{(6ND)^\alpha}=\frac{6^{-\alpha}}{(ND)^\alpha},\) (37)

where _L<sub>H</sub>_ is the loss predicted from the scaling law in Hoffmann et al. 2022, and _L<sub>C</sub>_ is the loss from only considering compute. Here we observe that in the case of Chinchilla-scaling (equation 36), as _N_ or _D_ is increased the value of<tbc>

Tokens per parameter D/N
102
Chinchilla
101
GPT-3
100
10-1
10-2
10-3
2012
2014
2016
2018
2020
2022
2024
Publication date

Figure 12: Ratio of parameters _N_ to dataset size _D_ for models in our dataset. We emphasize the ratios corresponding to GPT-3 (T. B. Brown et al. 2020) and Chinchilla models (Hoffmann et al. 2022), which are of historical importance in determining how to choose this ratio when scaling language models.

