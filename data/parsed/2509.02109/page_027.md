## A.2 Postponed Proofs

**Proof of Proposition 3.1.** Consider the cost matrices \(C,\hat{C}\in\mathbb{R}_+^{K_0\times K_1}\) defined by their entries at \((k_0,k_1)\in\unknown 1,K_0\unknown\times\unknown 1,K_1\unknown\):<tbc>

\(C_{k_0,k_1}:=\|m_{k_0}^{(0)}-m_{k_1}^{(1)}\|_2^2+d_\mathrm{BW}^2(\Sigma_{k_0}^{(0)},\Sigma_{k_1}^{(1)}),\hat{C}_{k_0,k_1}:=\|\hat{m}_{k_0}^{(0)}-\hat{m}_{k_1}^{(1)}\|_2^2+d_\mathrm{BW}^2(\hat{\Sigma}_{k_0}^{(0)},\hat{\Sigma}_{k_1}^{(1)}),\)

<tbc>and apply \[TFD24, Lemma 2.1\] with weights \((w_i,\overline{w_i}):=(w_i,\hat{w}_i)\) for \(i\in\{0,1\}\), and cost matrices \((M,\overline{M}):=(C,\hat{C})\): we obtain:<tbc>

\(\left|\mathrm{MW}_2^2(\hat{\mu}_1,\hat{\mu}_2)-\mathrm{MW}_2^2(\mu_1,\mu_2)\right|\le\|C-\hat{C}\|_\infty+\|C\|_\infty\left(\|w_0-\hat{w}_0\|_1+\|w_1-\hat{w}_1\|_1\right).\)

<tbc>First, noticing that \(\forall\Sigma\in S_d^+(\mathbb{R})\), \(d_\mathrm{BW}(0,\Sigma)=\sqrt{\mathrm{Tr}(\Sigma)}\), we apply the triangle inequality on \(\|\cdot\|_2\) and _d_<sub>BW</sub> to obtain \(\|C\|_\infty\le 4(R_m^2+R_\Sigma^2)\). We now turn to upper-bounding \(\|C-\hat{C}\|_\infty\). We will use the inequality \(\forall(s,t)\in\mathbb{R}^2\), \(|s^2-t^2|\le 2\mathrm{max}(|s|,|t|)|s-t|\). First, for \(x,\hat{x},y,\hat{y}\in B_{\mathbb{R}^d}(0,R_m)\), we have by the triangle inequality:<tbc>

\(\left|\|x-y\|_2^2+\|\hat{x}-\hat{y}\|_2^2\right|\le 2\mathrm{max}(\|x-y\|_2,\|\hat{x}-\hat{y}\|_2)\|(x-y)-(\hat{x}-\hat{y})\|_2\le 4R_m\left(\|x-\hat{x}\|_2+\|y-\hat{y}\|_2\right).\)

<tbc>Similarly, for \(A,\hat{A},B,\hat{B}\in\{S\in S_d^+(\mathbb{R}):\sqrt{\mathrm{Tr}(S)}\le R_\sigma\}\), we compute:

\(\left|d_\mathrm{BW}(A,B)-d_\mathrm{BW}(\hat{A},\hat{B})\right|\le 4R_\Sigma\left(d_\mathrm{BW}(A,\hat{A})+d_\mathrm{BW}(B,\hat{B})\right).\)

Applying our two inequalities to the entries of \(C-\hat{C}\) and combining with the inequality on \(\mathrm{MW}_2^2\) gives Eq. (18) in expectation.

**Proof of Proposition 3.2.** For notational simplicity, introduce \(g_k:=\mathcal{N}(m_k,\Sigma_k)\) and \(\hat{g}_k:=\mathcal{N}(m_k,\hat{\Sigma}_k)\). Let \(\eta_k:=\mathrm{min}(\hat{w}_k,w_k)\) and the diagonal matrix \(D:=\mathrm{diag}(\eta)\). Our objective is to complete the non-negative matrix _D_ into a coupling \(P\in\Pi(\hat{w},w)\). First, if \(\sum_k\eta_k=1\), then \(w=\hat{w}\) and already \(D\in\Pi(\hat{w},w)\), so we can set _P_:=_D_. If \(\sum_k\eta_k\neq 1\), we introduce \(Q\in\mathbb{R}_+^{K\times K}\) such that \(Q_{k,\ell}=(\hat{w}_k-\eta_k)(w_\ell-\eta_\ell)/(1-\sum_p\eta_p)\) for all \((k,\ell)\). The matrix _Q_ is the independent coupling between the non-negative vectors \(\hat{w}-\eta\) and \(w-\eta\). We set _P_:=_D+Q_, straightforward computation shows that \(P\in\Pi(\hat{w},w)\). We denote the pairwise cost matrix \(C:=(\mathrm{W}_2^2(\hat{g}_k,g_\ell))_{k,\ell}\) and use _P_ as a candidate coupling in the definition of \(\mathrm{MW}_2^2(\hat{\mu},\mu)\):<tbc>

\(\mathrm{MW}_2^2(\hat{\mu},\mu)\le\langle P,C\rangle=\langle D,C\rangle+\langle Q,C\rangle\le\mathrm{max}_k\mathrm{W}_2^2(\hat{g}_k,g_k)(\sum_\ell\eta_\ell)+\|C\|_\infty\|Q\|_1.\)

<tbc>(Note that in the case \(\sum_k\eta_k=1\), the second term vanishes.) Then since \(\eta\le w\) entry-wise, \(\sum\eta_k\le 1\), and we compute \(\|Q\|_1=1-\sum_k\eta_k\), and further re-write:<tbc>

\(\sum_{k=1}^K\eta_k=\sum_{k=1}^K\mathrm{min}(\hat{w}_k,w_k)=\frac{1}{2}\sum_{k=1}^K(\hat{w}_k+w_k-|\hat{w}_k-w_k|)=1-\frac{\|\hat{w}-w\|_1}{2},\)

<tbc>which finally yields:

\(\mathrm{MW}_2^2(\hat{\mu},\mu)\le\mathrm{max}_k\mathrm{W}_2^2(\hat{g}_k,g_k)+\frac{\|\hat{w}-w\|_1}{2}\mathrm{max}_{k,\ell}\mathrm{W}_2^2(\hat{g}_k,g_\ell).\)

Taking expectations and using the assumptions on the parameter estimators concludes the proof.

## A.3 Specific GMMs Used in Section 3.2 and Section 4.5

In Section 3.2, we use two fixed mixtures \(\mu\) and \(\nu\) with _K_=3 components in _d_=2, shown in Fig. 13. Separation is controlled by the covariance scaling parameter \(\sigma\): "low" uses \(\sigma=10\), "medium" \(\sigma=0.5\), and "high" \(\sigma=0.1\). Larger values create strong overlap between components, while smaller values yield well-separated mixtures. The same pairs \((\mu,\nu)\) are used across all repetitions.

