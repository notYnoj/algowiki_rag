### Limit theorems.

By the strong law of large numbers for U-statistics, \(U_n\rightarrow\theta\) almost surely when \(\mathbb{E}|h|<\infty\) (Serfling, 1980, Chapter 5). By the central limit theorem, \(\sqrt{n}(U_n-\theta)\rightarrow^dN(0,m^2\mathrm{Var}\{h_1(Z_1)\})\); the multivariate version holds jointly for finitely many U-statistics, with asymptotic covariance _ms_Cov{_h_<sub>1</sub>(_Z_<sub>1</sub>)_,g_<sub>1</sub>(_Z_<sub>1</sub>)} between kernels of orders _m_ and _s_ (Serfling, 1980, Chapter 5). These results, combined with the delta method (van der Vaart, 1998), give the limits of smooth functions such as ratios.

### Leave-one-out identity.

Let \(\widehat{h}_1(Z_i)=\genfrac(){pt}{2}{n-1}{m-1}^{-1}\sum_{I\unknown i,|I|=m}h(Z_I)\) be the average of the kernel over the subsets containing observation _i_, and let \(U_{n-1}^{(-i)}\) be the U-statistic computed from the sample without observation _i_. Then

\(\widehat{h}_1(Z_i)=\frac{\genfrac(){pt}{2}{n}{m}U_n-\genfrac(){pt}{2}{n-1}{m}U_{n-1}^{(-i)}}{\genfrac(){pt}{2}{n-1}{m-1}},i=1,\dots,n,\) (A.3)

because the subsets containing _i_ are those not contained in the sample without _i_.

### Disjoint-subset principle.

If _I_ and _J_ are disjoint, _h(Z<sub>I</sub>_) and _g(Z<sub>J</sub>_) are independent, so E{_h(Z<sub>I</sub>)g(Z<sub>J</sub>_)}=E(_h_)E(_g_). Averaging such products over all disjoint pairs (_I,J_) therefore gives an unbiased estimator of the product of means, and subtracting it from _U<sub>n</sub>V<sub>n</sub>_ gives an unbiased estimator of Cov(_U<sub>n</sub>,V<sub>n</sub>_) (Hoeffding, 1948).

### Inclusion-exclusion.

For finite index sets _I_ and _J_, \(\mathbf{1}\{I\cap J=\varnothing\}=\sum_{K\subseteq I\cap J}(-1)^{|K|}\). This identity converts sums over disjoint subsets into sums over overlapping ones, as used in Proposition 5.1.

## B Concomitant coefficients, conditional kernels, and calculations under independence

### B.1 Concomitant representation and means of the kernels

Put _U=F<sub>Y</sub>(Y_). Since _Y_ is continuous, the pair (_X<sub>j</sub>,Y<sub>j</sub>_) has the _r_th smallest _Y_ value among _k_ pairs with conditional probability \(\genfrac(){pt}{2}{k-1}{r-1}U_j^{r-1}(1-U_j)^{k-r}\) given (_X<sub>j</sub>,Y<sub>j</sub>_). Hence

\(\mathbb{E}\big(X_{[r:k]}\big)=k\genfrac(){pt}{2}{k-1}{r-1}\mathbb{E}\big\{XU^{r-1}(1-U)^{k-r}\big\}\) (B.1)

(Serfling and Xiao, 2007, Section 3.2). Substituting (B.1) into the right-hand sides of (2.4) gives, inside \(\mathbb{E}\{X\cdot\}\),

\(U-(1-U)=2U-1=P_1(U),\)<br>
\(U^2-4U(1-U)+(1-U)^2=6U^2-6U+1=P_2(U),\)<br>
\(U^3-9U^2(1-U)+9U(1-U)^2-(1-U)^3=20U^3-30U^2+12U-1=P_3(U),\)

