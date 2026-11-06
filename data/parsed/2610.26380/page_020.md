**Algorithm 3** Knowledge gradient (KG)

**Input:** \(\unknown_{t-1}\), \(\Sigma_{t-1}\), \(R_t\ge\mathrm{min}(r_0,r_1)\)

1: Compute \(\psi_{t,ij}^\mathrm{KG}\) for all \((i,j)\in\mathcal{I}\) with \(r_j\le R_t\)

2: \((i,j)\leftarrow\mathrm{argmax}_{(i,j)\in\mathcal{I}:r_j\le R_t}\psi_{t,ij}^\mathrm{KG}\)

3: **if** \(\psi_{t,ij}^\mathrm{KG}=0\)

4: Choose an affordable (_i,j_) using the fallback rule

5: **return** (_i,j_)

### 5.2. Endgame when?

Up to this point, Algorithm 2 provides the general sequential procedure, and we have given two algorithms for its EVALUATIONRULE: SA (Algorithm 1) and KG (Algorithm 3). What remains is a rule for when to use which. SA was designed for the bulk of the evaluation process and KG for the endgame, so we consider the following class of policies: run SA until a predetermined share \(\nu\) of the budget has been spent, then switch to KG.<sup>2</sup> We refer to \(\nu\) as the switching point. Within this class, we choose the switching point via Monte Carlo simulation. For \(\nu\in[0,1]\), let \(\pi_\nu\) denote the policy obtained from Algorithm 2 using EVALUATIONRULE<sup>_R<sub>t</sub>_</sup>= SA while \(R-R_t<\nu R\) and EVALUATIONRULE<sup>_R<sub>t</sub>_</sup>= KG once \(R-R_t\ge\nu R\), so that \(\pi_1\) is SA throughout and \(\pi_0\) is KG throughout. Given a problem specification \((I,k,R,r_0,r_1,p_0,\beta_0,\beta_1,\theta_0)\), let

\(\mathrm{EOC}\left(S_k^*(\unknown_T);\pi_\nu\right):=\mathbb{E}\left[\sum_{i\in S_k^*(\theta)}\theta_i-\sum_{i\in S_k^*(\unknown_T)}\theta_i\right|\pi_\nu\right],\)

where the expectation is over \(\theta\) with prior distribution _p_<sub>0</sub> and over the outcomes _X_<sub>1</sub>_,...,X<sub>T</sub>_ drawn from the likelihood under policy \(\pi_\nu\).

We choose the switching point by a marginal analysis over a fixed set of candidate switching points \(0\le\nu_1<\nu_2<\cdots<\nu_J\le 1\). Let \(\widehat{\mathrm{EOC}}\left(S_k^*(\unknown_T);\pi_\nu\right)\) denote the Monte Carlo estimate of \(\mathrm{EOC}\left(S_k^*(\unknown_T);\pi_\nu\right)\), obtained by averaging the realized opportunity cost \(\sum_{i\in S_k^*(\theta)}\theta_i-\sum_{i\in S_k^*(\unknown_T)}\theta_i\) over _M_ independent simulated runs of \(\pi_\nu\), each drawing \(\theta\sim p_0\) and the outcomes from the specified likelihood. Starting from \(\nu_J\) (\(\nu_J=1\) meaning SA all the way through), we move the switching point back one candidate at a time, from \(\nu_h\) to \(\nu_{h-1}\) (peeling back the last stretch of SA into KG), as long as the marginal reduction \(\widehat{\mathrm{EOC}}\left(S_k^*(\unknown_T);\pi_{\nu_h}\right)-\widehat{\mathrm{EOC}}\left(S_k^*(\unknown_T);\pi_{\nu_{h-1}}\right)\) remains positive. We stop at the first \(\nu^*\) at which peeling back further fails to reduce \(\widehat{\mathrm{EOC}}\), and deploy the policy \(\pi_{\nu^*}\). We will refer to this as the switching procedure, and to our method, the policy \(\pi_{\nu^*}\), as SE (Surrogate to Endgame).

## 6. Batching extension

To conclude the analysis, we consider settings where evaluations are assigned in batches whose outcomes are observed at once before the next batch is chosen. While we have presented the problem sequentially, the model and analysis for the surrogate were developed with batching in mind, and extend naturally.

<sup>2</sup> In practice, the switching point can also be chosen state-dependently, that is, during the run as a function of _p_<sub>_t_-1</sub> rather than fixed in advance. We restrict attention to a predetermined switching point for simplicity.

