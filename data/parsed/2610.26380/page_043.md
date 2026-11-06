<tbc>Standardizing with<tbc>

\(U:=\frac{\Delta_i+\theta_0}{\sqrt{s}},V:=\frac{Z+\beta_0\theta_0}{\sqrt{1+s\beta_0^2}},\)

<tbc>gives a mean-zero bivariate normal pair (_U,V_) with correlation \(\rho_0\), and<tbc>

\(\Delta_i>0\Longleftrightarrow U>\frac{\theta_0}{\sqrt{s}},Z>0\Longleftrightarrow V>\frac{\beta_0\theta_0}{\sqrt{1+s\beta_0^2}}.\)

<tbc>Writing \(\Phi_2(\cdot,\cdot;\rho)\) for the standard bivariate normal CDF with correlation \(\rho\), we therefore obtain

\(P_R=\mathbb{P}\big(U>\frac{\theta_0}{\sqrt{s}},V>\frac{\beta_0\theta_0}{\sqrt{1+s\beta_0^2}}\big)+\mathbb{P}\big(U<\frac{\theta_0}{\sqrt{s}},V<\frac{\beta_0\theta_0}{\sqrt{1+s\beta_0^2}}\big)\)<br>
\(=1-\Phi\big(\frac{\theta_0}{\sqrt{s}}\big)-\Phi\big(\frac{\beta_0\theta_0}{\sqrt{1+s\beta_0^2}}\big)+2\Phi_2\big(\frac{\theta_0}{\sqrt{s}},\frac{\beta_0\theta_0}{\sqrt{1+s\beta_0^2}};\rho_0\big).\)

Together, the equations for <o>_P_</o> and _P<sub>R</sub>_ give the calibration equations for \((\beta_0,\theta_0)\).

## Appendix C: Proofs of results in §3

_Proof of Lemma 1._ First consider a fixed utility vector \(\vartheta\in\mathbb{R}^I\), and let \(S_k^*(\vartheta)\) denote the set of indices of the _k_ largest elements of \(\vartheta\). Define the opportunity cost \(O(\vartheta;S_k):=\sum_{i\in S_k^*(\vartheta)}\vartheta_i-\sum_{i\in S_k}\vartheta_i\), and recall the mismatch loss \(\mathcal{M}(\vartheta;S_k,a)\) from (6) evaluated at \(\vartheta\). Since \(|S_k|=|S_k^*(\vartheta)|=k\), the sets \(S_k\backslash S_k^*(\vartheta)\) and \(S_k^*(\vartheta)\backslash S_k\) have the same cardinality. Then

\(\mathcal{M}(\vartheta;S_k,a)=\sum_{i\in S_k}\big(a(\vartheta)-\vartheta_i\big)^++\sum_{i\notin S_k}\big(\vartheta_i-a(\vartheta)\big)^+\)<br>
\(\ge\sum_{i\in S_k\backslash S_k^*(\vartheta)}\big(a(\vartheta)-\vartheta_i\big)^++\sum_{i\in S_k^*(\vartheta)\backslash S_k}\big(\vartheta_i-a(\vartheta)\big)^+\)<br>
\(\ge\sum_{i\in S_k\backslash S_k^*(\vartheta)}\big(a(\vartheta)-\vartheta_i\big)+\sum_{i\in S_k^*(\vartheta)\backslash S_k}\big(\vartheta_i-a(\vartheta)\big)\)<br>
\(=\sum_{i\in S_k^*(\vartheta)\backslash S_k}\vartheta_i-\sum_{i\in S_k\backslash S_k^*(\vartheta)}\vartheta_i=O(\vartheta;S_k).\)

The first inequality drops the nonnegative terms indexed by \(i\in S_k\cap S_k^*(\vartheta)\) and \(i\notin S_k\cup S_k^*(\vartheta)\), the second uses \(x^+\ge x\), and the third line’s _a_ terms cancel because the two index sets have equal cardinality. This is the upper bound. When \(a(\vartheta)\in[\vartheta^{(k+1)},\vartheta^{(k)}]\) we have \(\vartheta_i\ge a(\vartheta)\) for \(i\in S_k^*(\vartheta)\) and \(\vartheta_i\le a(\vartheta)\) for \(i\notin S_k^*(\vartheta)\), so the dropped terms in the first inequality are zero, and each _x_<sup>+</sup>=_x_ in the second inequality. Hence both inequalities are then equalities, giving \(O(\vartheta;S_k)=\mathcal{M}(\vartheta;S_k,a)\).

Applying this pointwise with \(\vartheta=\theta\) and taking expectations over \(\theta|p_{t-1}\sim N(\mu_{t-1},\Sigma_{t-1})\) gives

\(\mathrm{EOC}(S_k;p_{t-1})=\mathbb{E}\big[O(\theta;S_k)\big|p_{t-1}\big]\le\mathbb{E}\big[\mathcal{M}(\theta;S_k,a)\big|p_{t-1}\big],\)

with equality whenever \(a(\theta)\in[\theta^{(k+1)},\theta^{(k)}]\) almost surely. \(\square\)

