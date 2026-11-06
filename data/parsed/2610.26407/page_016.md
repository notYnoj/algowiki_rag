<tbc>rate is then obtained by plugging these proportions into \(\Gamma\). Part (iii) gives a lower bound on TEAk’s rate, and we establish the one-half guarantee by comparing this lower bound, rather than \(\Gamma(w(q_0);\theta^0)\) itself, with the optimal rate \(\Gamma^*(\theta^0)\). This lower bound motivates choosing the threshold that makes it tightest,

\(q^\dagger\in argmin_{\theta_{k+1}^0<q<\theta_k^0}\sum_{i=1}^I\frac{1}{d_i(\theta_i^0,q)}.\)

Replacing the true means with the posterior means results in our choice of threshold _q_<sup>†</sup>(_t_) in (3). This parallels our earlier choice of _q_<sup>∗</sup>(_t_): there we minimize an upper bound on the current EOC, whereas here we maximize a lower bound on its exponential decay rate.

It remains to show that \(q^\dagger(t)\rightarrow q^\dagger\). To establish this convergence, we assume the minimizer is unique.

ASSUMPTION 3 (**Unique threshold**). _For every_ \(x\in\mathcal{J}^I\) _with x_<sub>\[_k_\]</sub>_\>x_<sub>\[_k_+1\]</sub>_, the function_ \(q\mapsto\sum_{i=1}^I1/d_i(x_i,q)\) _has a unique minimizer on_ (_x_<sub>\[_k_+1\]</sub>_,x_<sub>\[_k_\]</sub>).

REMARK 3. _Each likelihood family in Remark 1 satisfies Assumption 3._

LEMMA 4 (**Convergence of** _q_<sup>†</sup>(_t_)**)**.** _Run Algorithm 3 with threshold q_<sup>†</sup>(_t). Then_ \(q^\dagger(t)\rightarrow q^\dagger\).

By Lemma 4, Theorem 1 applies with _q_<sub>0</sub>=_q_<sup>†</sup>. We further show that \(\left(\sum_{i=1}^I1/d_i(\theta_i^0,q^\dagger)\right)^{-1}\ge\Gamma^*(\theta^0)/2\), which yields our main theoretical result.

THEOREM 2 (**Exponential rate of TEAk**). _Run Algorithm 3 with threshold q_<sup>†</sup>(_t). Then_

\(lim_{t\rightarrow\infty}-\frac{logEOC(\mathcal{H}_t)}{\sum_iN_i(t)}\ge\frac{1}{2}\Gamma^*(\theta^0).\)

Thus, the posterior convergence rate of TEAk is at least half the optimal posterior convergence rate. The conclusions in Proposition 5 and in Theorems 1 and 2 also hold when EOC(H_<sub>t</sub>_) is replaced by the posterior error probability \(\mathbb{P}_t(S_k(\theta)\neq S_k(\theta^0))\).

## 4.4. Numerical illustration

We illustrate Theorems 1 and 2 on a Gaussian instance with _I_=20, _k_=5, likelihood variance of 1, and true means \(\theta_i^0=-(i-1)/2\) so that the gap between consecutive means is 0.5. On this instance \(\Gamma^*(\theta^0)=0.0243\) and _q_<sup>†</sup>=-2.25, the midpoint between \(\theta_k^0\) and \(\theta_{k+1}^0\). The rate of the threshold allocation is \(\Gamma(w(q^\dagger);\theta^0)=0.57\Gamma^*(\theta^0)\) and the lower bound on it in Theorem 1(iii) is \(0.53\Gamma^*(\theta^0)\).

We run TEAk with _q_<sup>†</sup>(_t_) on this instance with _B<sub>t</sub>_=1, a sampling budget of 20,000, and a _N_(0,10<sup>2</sup>) prior over 50 replications. We also run two fixed allocations: the oracle **_w_**<sup>∗</sup> that maximizes (13) using the true means, and equal allocation. Figure 3 shows the results.

The left panel shows the average sampling proportions at the end of the run. TEAk’s proportions coincide with **_w_**(_q_<sup>†</sup>), as guaranteed by Theorem 1(i), and are a bit off from **_w_**<sup>∗</sup>: TEAk puts 83% of the budget on the _k_th<tbc>

