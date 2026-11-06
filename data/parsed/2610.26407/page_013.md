<tbc>Throughout this section, we fix a true mean vector \(\theta^0\in\mathcal{J}^I\). We write \(\mathbb{P}_{\theta^0}\) and \(\mathbb{E}_{\theta^0}\) for probability and expectation over observations generated from \(P_i(\cdot|\theta_i^0)\). All convergence statements hold \(\mathbb{P}_{\theta^0}\)-almost surely. Although the true means are fixed, EOC(H_<sub>t</sub>_) remains the Bayesian posterior expectation in (1). Our rate guarantees also hold for the posterior error probability \(\mathbb{P}_t(S_k(\theta)\neq S_k(\theta^0))\), the quantity studied in the _k_=1 analyses of Russo (2020), Qin et al. (2017), and Shang et al. (2020).

These posterior guarantees should not be confused with guarantees for the frequentist EOC \(\mathbb{E}_{\theta^0}[\mathrm{OC}(S_k(\mu(t)),\theta^0)]\) and the frequentist probability of incorrect selection \(\mathbb{P}_{\theta^0}(S_k(\mu(t))\neq S_k(\theta^0))\). The posterior quantities measure the EOC and posterior error probability _conditional_ on an observed history, while the frequentist quantities average over observation histories. This distinction matters for exponential-rate guarantees: a sampling rule that achieves the optimal posterior convergence rate need not achieve the corresponding frequentist rate. In fact, no single sampling rule can generally guarantee a constant fraction of the best exponential decay rate of the frequentist probability of incorrect selection (likewise frequentist expected opportunity cost) uniformly across problem instances (Goldberger 2026, Degenne 2023).

**4.1. Consistency**

PROPOSITION 4 (**Consistency**). _Run TEAk for infinitely many rounds with threshold q_<sup>∗</sup>(_t_) _or q_<sup>†</sup>(_t). For q_<sup>†</sup>(_t), assume that the minimum in_ (3) _is attained whenever_ \(\mu_{[k]}(t)>\mu_{[k+1]}(t)\)_. There is a set_ \(\Theta^*\subseteq\mathcal{J}^I\) _with prior probability one such that for every_ \(\theta^0\in\Theta^*\)_, the following hold as_ \(t\rightarrow\infty\):

(i) \(N_i(t)\rightarrow\infty\), \(\mu_i(t)\rightarrow\theta_i^0\)_, and_ \(v_i(t)\rightarrow 0\) _for every i._<tbc>

(ii) \(\mathrm{EOC}(\mathcal{H}_t)\rightarrow 0\).<tbc>

(iii) _If_ \(\theta_{[k]}^0>\theta_{[k+1]}^0\)_, then_ \(S_k(\mu(t))=S_k(\theta^0)\) _for all sufficiently large t._

Part (i) says that every item is sampled infinitely often, and consequently its posterior mean converges to the true mean, and its posterior variance to 0. Parts (ii) and (iii) then follow: the posterior EOC converges to 0 and, when the true top-_k_ gap is positive, there is a finite time after which \(S_k(\mu(t))=S_k(\theta^0)\).

**4.2. The optimal exponential rate**

For the remainder of this section, assume \(1\le B_t\le B\) for every _t_ where _B_ is a fixed positive integer, and assume \(\theta_1^0\ge\cdots\ge\theta_k^0>\theta_{k+1}^0\ge\cdots\ge\theta_I^0\). We next establish an upper bound on the posterior convergence rate that any sequential sampling rule can achieve, and characterize the sample allocation that attains this bound. This gives the benchmark against which we will evaluate TEAk. We rely on the general posterior large-deviation analysis of Russo (2020), which we then apply to our top-_k_ EOC objective. Accordingly, we follow the distributional assumptions of Russo (2020).

