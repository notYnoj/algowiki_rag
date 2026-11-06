(ii) _Suppose that at round t, for every item i there exists_ \(\lambda_i(t)>0\) _such that_

\(c_i(t,d)^2=\frac{1}{1+\lambda_i(t)d}\text{\textit{for every}}d\in\mathbb{Z}_{\ge 0}.\) \(\text{(10)}\)

_Then_ (9) _holds, and GBB returns a global optimizer of_ (8).

(iii) _Suppose that for every item i, the sampling family is a regular one-parameter natural exponential family, meaning it has an open natural parameter space_ E_<sub>i</sub> and density or mass function_ \(p_i(y|\eta_i)=h_i(y)exp\{\eta_iy-A_i(\eta_i)\}\)_, where_ \(\theta_i=A'_i(\eta_i)\)_. Suppose also that the prior on_ \(\eta_i\) _induced by_ \(\Pi_{i,0}\) _has density proportional to_ \(exp\{a_i\eta_i-b_iA_i(\eta_i)\}\) _on_ E_<sub>i</sub> for some_ \(a_i\in\mathbb{R}\) _and b<sub>i</sub>\>_0_. Then_ (10) _holds at every round, and GBB returns a global optimizer of_ (8).

Part (i) says that GBB finds an optimal allocation whenever the gain from each additional sample is nonincreasing. However, checking this condition requires computing all marginal decreases in every round. Part (ii) avoids that computation by giving a sufficient condition for (9) based on how the expected posterior variance decreases with additional samples, and part (iii) establishes that the condition holds for regular natural exponential families with conjugate priors.

REMARK 2 (SAMPLING COSTS). _In some settings, items may differ in their sampling costs. Let_ \(w_i\in\mathbb{Z}_{>0}\) _denote the cost of one sample of item i. The constraint in_ (8) _becomes_ \(\sum_{i=1}^Iw_i\Delta_i\le B_t\) _and the same dynamic programming approach finds the optimal batch by accounting for these costs in the remaining budget._

## 3.4. Sequential algorithm

Algorithm 3 gives the full sampling procedure. In each round, we update the threshold from the current prior and allocate samples by solving (8) using one of the batch builders above.

**Algorithm 3** Threshold-EOC allocation for top-_k_ selection (TEAk)

1: **Input:** priors \((\Pi_{i,0})_{i=1}^I\), sampling distributions \((P_i(\cdot|\theta_i))_{i=1}^I\), warm-up _n_<sub>0</sub>, batch sizes \((B_t)_{t=1}^T\)

2: **Initialize:** _N<sub>i</sub>_(0)=0 for all _i_

3: **Warm-up:** for each _i_, allocate _n_<sub>0</sub> samples, observe outcomes, and update _N<sub>i</sub>_(1)=_n_<sub>0</sub> and \(\Pi_{i,1}\)

4: **for** _t_=1_,...,T_

5: Compute _q(t_) using (2) or (3)

6: Run DPBB to obtain \(\Delta^t\), or GBB when (9) holds for every item

7: For each _i_, allocate \(\Delta'_i\) samples and observe outcomes

8: Update \(N_i(t+1)=N_i(t)+\Delta'_i\) and \(\Pi_{i,t+1}\)

9: **Return** \(S_k(\mu(T+1))\)

## 3.5. ESCP explicit expressions for Algorithm 3

This section instantiates Algorithm 3 for the five ESCP in Remark 1. Recall from (7) that

\(\ell_{i,t}(\Delta_i)=c_i(t,\Delta_i)\mathbb{E}_t\left[(z_i(t,\Delta_i)-\theta_i)^+\right],z_i(t,\Delta_i):=\mu_i(t)+\frac{q(t)-\mu_i(t)}{c_i(t,\Delta_i)}.\)

Computing the round _t_ allocation thus requires explicit formulas for \(c_i(t,\Delta_i)\) as well as \(\mathbb{E}_t\left[(z-\theta_i)^+\right]\) for each family, which are given in Proposition 3.

