<tbc>If _A(s_) is analytic in a disk centered at zero with radius _R\>_1, then choose 1_\<r\<R_ and by using Cauchy’s integral formula, we have

\(\|A_j\|_2=\big\|\frac{1}{2\pi i}\oint_{|\zeta|=r}\frac{A(\zeta)}{\zeta^{j+1}}\mathrm{d}\zeta\big\|_2\le\mathrm{max}_{|\zeta|=r}\|A(\zeta)\|_2r^{-j},\)

which implies \(C_\infty<\infty\). \(\sqcap\sqcup\)

_Remark_ 5.3. Notice that when we apply infGMRES to solve _A(s)x(s_)=_z_ for |_s|\>_1, _A(s_) is always assumed a priori to be analytic in the disk centered at zero with radius |_s_|, so \(C_\infty<\infty\) and the lower bound is strictly positive.

_Effect of scaling._ Appropriate parameter scaling can significantly improve the convergence of infGMRES \[6,16\]. The residual lower bound above helps explain this effect. For an expansion center _s_<sub>0</sub> with _A(s_<sub>0</sub>) nonsingular, choose a scaling factor _w\>_0, set<tbc>

\(\widehat{A}(\sigma)=A(s_0+w\sigma),\sigma=\frac{s-s_0}{w}.\)

<tbc>The scaled Taylor coefficients of \(\widehat{A}(\sigma)\) at \(\sigma=0\) are \(\widehat{A}_j=w^jA^{(j)}(s_0)/j!\). Under such scaling, set<tbc>

\(t=|\sigma|,C=\widehat{C}_m(w):=\|[\widehat{A}_0,\dots,\widehat{A}_{m-1}]\|_2,\)

<tbc>then Theorem 5.2 shows that infGMRES applied to solve \(\widehat{A}(\sigma)x(\sigma)=z\) has the lower bound \(\|z\|_2F(t,C)\), where

\(F(t,C)=\frac{t-1}{\sqrt{(t-1)^2+C^2}},t>1,C>0.\)

_F(t,C_) is strictly increasing in _t_ and strictly decreasing in _C_. For a fixed target _s_, increasing |_w_| decreases _t_ and makes \(\widehat{C}_m(w)\) non-decreasing, as the latter is because \(\sum_{j=0}^{m-1}\widehat{A}_j\widehat{A}_j^*\) increases in the positive semi-definite order. Thus, both changes weaken the residual lower bound while _t\>_1. This explains why using a large weight can significantly improve the accuracy of infGMRES, especially when the Taylor coefficients are small.

## 6. Numerical experiments.

We set _p=q_ in every experiment, so _p_ is both the Taylor degree and the Arnoldi length. All experiments were run in MATLAB R2023b using eight computational threads on an exclusively allocated Linux node with two AMD EPYC 9754 processors.

We call Dynamic TiGMRES with \(\tau=0\) fully refreshed TiGMRES and use it as a baseline because it has completely identical arithmetic and storage complexities with TOAR infGMRES, as discussed in Section 3.4. Dynamic TiGMRES uses \(\tau=100\), because we want to trigger refreshing when the indicator suggests a potential loss of approximately two decimal digits.

For the parameterized systems, we use the relative residual

\(r_k(s)=\frac{\|A(s)\widetilde{x}_k(s)-z\|_2}{\|z\|_2}\)

to measure the convergence.

The reported runtime in each experiment is the median of seven runs. We first make one untimed run, then rotate the method order across the timed runs.

