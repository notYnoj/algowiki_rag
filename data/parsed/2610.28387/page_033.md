## Declarations

**Competing interests.** The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

**Funding.** The research of P.S. was supported by Khon Kaen University, Thailand.

**Author contributions.** Palakorn Seenoi: conceptualization, formal analysis, software, numerical experiments, and drafting. Jeong-Soo Park: conceptualization, methodology, supervision, mathematical verification, and writing-review and editing.

**Data availability.** No external observational data were used. All numerical results are based on simulated bivariate observations described in the paper.

** availability.** R code for the numerical experiments and covariance computation is available at `https://github.com/palakorn-seenoi/sample\_Lcomom`.

**Declaration of generative AI use.** ChatGPT (OpenAI) and Claude (Anthropic) were used for language editing, technical discussion, and mathematical derivations. The authors are responsible for reviewing and verifying all derivations, results, citations, and the final manuscript.

**ORCID.** Palakorn Seenoi: 0000-0001-9374-070X; Jeong-Soo Park: 0000-0002-8460-4869.

## Appendix

## A Preliminaries on U-statistics and L-comoments

We collect standard facts used repeatedly in the paper, without proofs.

### Results of Serfling and Xiao (2007).

For (_X,Y_) with finite mean and continuous margins, the _k_th L-comoment of _X_ with respect to _Y_ is \(\lambda_k^{[XY]}=\mathrm{Cov}[X,P_{k-1}\{F_Y(Y)\}]\), \(k\ge 2\), which equals (2.3) because E\[_P_<sub>_k_-1</sub>{_F<sub>Y</sub>(Y_)}\]=0. The following facts are used in this paper.

(i) _Invariance_ (their equation (11)). \(\lambda_k^{[XY]}\) is translation invariant and scale equivariant in _X_, and translation and scale invariant in _Y_ .<tbc>

(ii) _Special cases._ If _Y=X_, \(\lambda_k^{[XY]}\) is the univariate L-moment \(\lambda_k(X)\). If _X_ and _Y_ are independent, \(\lambda_k^{[XY]}=0\) for all \(k\ge 2\).<tbc>

(iii) _Concomitant representation_ (their Proposition 6).<tbc>

<tbc>\(\lambda_k^{[XY]}=k^{-1}\sum_{j=0}^{k-1}(-1)^j\genfrac(){pt}{2}{k-1}{j}\mathbb{E}\big(X_{[k-j:k]}\big);\)<tbc>

<tbc>the cases _k_=2,3,4 are (2.4).<tbc>

(iv) _Unbiased estimation_ (their Proposition 7 and equation (26)). The sample L-comoment, a weighted sum of the sample concomitants with the weights of univariate sample L- moments, is an unbiased estimator of \(\lambda_k^{[XY]}\) and is also a U-statistic; for _k_=2,3 this is (2.8).<tbc>

