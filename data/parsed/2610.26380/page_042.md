<tbc>Our goal is to express _P<sub>P</sub>_ as a function of \(\beta_1\). Under the prior, the utility difference \(\Delta:=\theta_i-\theta_j\) satisfies \(\Delta\sim N(0,2s)\). Writing _E∼N_(0,1) independently and \(Z:=\beta_1\Delta+E\), the comparison outcome is determined by the sign of _Z_, while the true ordering is determined by the sign of \(\Delta\). Hence<tbc>

\(P_P=\mathbb{P}\big(\mathrm{sign}(Z)=\mathrm{sign}(\Delta)\big).\)

<tbc>We first compute the correlation of \((\Delta,Z)\).<tbc>

\(\mathbb{V}(\Delta)=2s,\mathbb{V}(Z)=\beta_1^2\mathbb{V}(\Delta)+\mathbb{V}(E)=1+2s\beta_1^2,\mathrm{Cov}(\Delta,Z)=\mathrm{Cov}(\Delta,\beta_1\Delta+E)=2s\beta_1,\)

<tbc>thus their correlation is<tbc>

\(\rho_P=\frac{\mathrm{Cov}(\Delta,Z)}{\sqrt{\mathbb{V}(\Delta)\mathbb{V}(Z)}}=\frac{\beta_1\sqrt{2s}}{\sqrt{1+2s\beta_1^2}}.\)

<tbc>For a mean-zero bivariate normal pair with correlation \(\rho_P\), the probability that the two variables have the same sign is \(\frac{1}{2}+\frac{1}{\pi}\mathrm{arcsin}(\rho_P)\). Therefore,

\(P_P=\frac{1}{2}+\frac{1}{\pi}\mathrm{arcsin}\left(\frac{\beta_1\sqrt{2s}}{\sqrt{1+2s\beta_1^2}}\right),\)

which gives the calibration equation for \(\beta_1\).

_Calibrating the rating accuracy factor_ \(\beta_0\) _and the threshold_ \(\theta_0\). We calibrate \(\beta_0\) and \(\theta_0\) jointly from the probability that a rating is correct and the expected thumbs-up rate under the prior. Let

\(P_R:=\mathbb{P}(\mathrm{a rating of a randomly chosen item is correct}),\overline{P}:=\mathbb{P}(X_{i0}=1).\)

_Step a: Calibrate the thumbs-up rate._ Writing _E∼N_(0,1) independently, a thumbs-up occurs when \(\beta_0(\theta_i-\theta_0)+E>0\). Since \(\theta_i\sim N(0,s)\), we have \(\beta_0\theta_i+E\sim N(0,1+s\beta_0^2)\), and therefore<tbc>

\(\overline{P}=\mathbb{P}(\beta_0\theta_i+E>\beta_0\theta_0)=\Phi\left(-\frac{\beta_0\theta_0}{\sqrt{1+s\beta_0^2}}\right).\)

<tbc>_Step b: Calibrate the probability that a rating is correct._ Let \(\Delta_i:=\theta_i-\theta_0\) and \(Z:=\beta_0\Delta_i+E\). The true rating of item _i_ is determined by the sign of \(\Delta_i\), while the estimated rating is determined by the sign of _Z_. Hence<tbc>

\(P_R=\mathbb{P}(\Delta_i>0,Z>0)+\mathbb{P}(\Delta_i<0,Z<0).\)

<tbc>To compute these probabilities, note that \((\Delta_i,Z)\) is bivariate normal with<tbc>

\(\Delta_i\sim N(-\theta_0,s),Z\sim N(-\beta_0\theta_0,1+s\beta_0^2),\mathrm{Cov}(\Delta_i,Z)=\beta_0s,\)

<tbc>so their correlation is<tbc>

\(\rho_0=\frac{\beta_0s}{\sqrt{s(1+s\beta_0^2)}}=\frac{\beta_0\sqrt{s}}{\sqrt{1+s\beta_0^2}}.\)

