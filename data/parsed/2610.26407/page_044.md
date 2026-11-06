<tbc>Let **_w_**<sup>∗</sup> maximize \(\Gamma\). By the proof of Proposition 5, \(w_i^*>0\) for every _i_. The functions (of _q_)

\(min_{i\le k}w_i^*d_i(\theta_i^0,q),min_{j>k}w_j^*d_j(\theta_j^0,q)\)

are continuous on \([\theta_{k+1}^0,\theta_k^0]\). The first is positive at \(\theta_{k+1}^0\) and zero at \(\theta_k^0\), while the second is zero at \(\theta_{k+1}^0\) and positive at \(\theta_k^0\). Thus they are equal at some \(\bar{q}\in(\theta_{k+1}^0,\theta_k^0)\). Write

\(r:=min_{i\le k}w_i^*d_i(\theta_i^0,\bar{q})=min_{j>k}w_j^*d_j(\theta_j^0,\bar{q})>0.\)

Choose \(i\le k<j\) attaining the two minima. Evaluating (12) at this pair and \(x=\bar{q}\) gives

\(\Gamma^*(\theta^0)\le w_i^*d_i(\theta_i^0,\bar{q})+w_j^*d_j(\theta_j^0,\bar{q})=2r.\)

Since \(w_i^*d_i(\theta_i^0,\bar{q})\ge r\) for every _i_,

\(rH(\bar{q})=\sum_i\frac{r}{d_i(\theta_i^0,\bar{q})}\le\sum_iw_i^*=1.\)

Since _q_<sup>†</sup> minimizes _H_,

\(\frac{1}{2}\Gamma^*(\theta^0)\le r\le\frac{1}{H(\bar{q})}\le\frac{1}{H(q^\dagger)}\le\Gamma(w(q^\dagger);\theta^0).\)

The corresponding result for the posterior error follows from Lemma 8. \(\square\)

## Appendix D: Additional simulation results

This section presents the remaining plots of the experiments in §5. §D.1 gives the EOC plots for the Bernoulli, exponential, and lognormal families and the PCS counterparts of all the EOC plots, which use the middle column in  1 for distributions of the true means. §D.2 and §D.3 give the EOC and PCS plots for the right and left columns, respectively.  1 is repeated below for reference.

## D.1. Middle column

\begin{tabular}{cccc}
Likelihood \(Y_{i,n}|\theta_i\) & \multicolumn{3}{c}{Distribution of true means \(\theta_i\)} \\
\(N(\theta_i,1)\) & Unif(-2,2) & Unif(-1,1) & Unif(-0.5,0.5) \\
\(Exp(1/\theta_i)\) & Unif(1,9) & Unif(1,5) & Unif(1,3) \\
\(Bern(\theta_i)\) & Unif(0.05,0.95) & Unif(0.2,0.8) & Unif(0.35,0.65) \\
\(\text{Lognormal}(log\theta_i-1/2,1)\) & Unif(1,9) & Unif(1,5) & Unif(1,3) \\
\end{tabular}

