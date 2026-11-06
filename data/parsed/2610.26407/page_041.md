<tbc>The numerator is covered by Lemma 9. For the denominator, let \(M_i:=\int_\mathcal{J}\mathbb{E}_x[Y^2]\Pi_{i,0}(dx)<\infty\), by Assumption 1. Equation (18) gives<tbc>

\(\mathbb{V}_t(Y)\le\mathbb{E}_t[Y^2]\le M_ie^{n\varepsilon_{i,n}}.\)

<tbc>Since \(\mathbb{V}_t(Y)\ge v_i(t)\ge\bar{v}_i(t,B-1)\),

\(0\le-\frac{1}{n}log\frac{\bar{v}_i(t,B-1)}{2\mathbb{V}_t(Y)}\le-\frac{1}{n}log\bar{v}_i(t,B-1)+\varepsilon_{i,n}+\frac{log(2M_i)}{n}\longrightarrow 0.\)

Combining this with (24) in (22) proves (21).

We now use these rates and batch optimality to show that<tbc>

\(\frac{d_i(\theta_i^0,q_0)N_i(t)-min_jd_j(\theta_j^0,q_0)N_j(t)}{\sum_jN_j(t)}\longrightarrow 0\text{for every}i.\)

<tbc>We first compare the sample counts for items sampled in the current round. Write<tbc>

\(\varepsilon_t:=max_{i,0\le d<B}\frac{|-logD_{i,t}(d)-d_i(\theta_i^0,q_0)N_i(t)|}{\sum_jN_j(t)}.\)

<tbc>By (21), \(\varepsilon_t\rightarrow 0\). If \(\Delta_i^t>0\) and \(j\neq i\), transferring one sample from _i_ to _j_ is feasible. Optimality of \(\Delta^t\) gives<tbc>

\(0\le\ell_{i,t}(\Delta_i^t-1)+\ell_{j,t}(\Delta_j^t+1)-\ell_{i,t}(\Delta_i^t)-\ell_{j,t}(\Delta_j^t)=D_{i,t}(\Delta_i^t-1)-D_{j,t}(\Delta_j^t).\)

<tbc>Since \(0\le\Delta_i^t-1\le B-1\) and \(0\le\Delta_j^t\le B-1\),

\(d_i(\theta_i^0,q_0)N_i(t)\le-logD_{i,t}(\Delta_i^t-1)+\varepsilon_t\sum_\ell N_\ell(t)\)<br>
\(\le-logD_{j,t}(\Delta_j^t)+\varepsilon_t\sum_\ell N_\ell(t)\)<br>
\(\le d_j(\theta_j^0,q_0)N_j(t)+2\varepsilon_t\sum_\ell N_\ell(t).\)

Taking the minimum over _j_ gives

\(\Delta_i^t>0\Longrightarrow d_i(\theta_i^0,q_0)N_i(t)\le min_jd_j(\theta_j^0,q_0)N_j(t)+2\varepsilon_t\sum_jN_j(t).\) (25)

To extend this analysis to every item, we apply it at the last round in which that item was sampled. Let \(\tau_i(t)<t\) be that round. Since \(N_i(t)\rightarrow\infty\), we have \(\tau_i(t)\rightarrow\infty\), and boundedness of the batches gives<tbc>

\(N_i(t)=N_i(\tau_i(t))+\Delta_i^{\tau_i(t)}\le N_i(\tau_i(t))+B.\)

<tbc>Also, \(min_jd_j(\theta_j^0,q_0)N_j(t)\) is nondecreasing. Applying (25) at \(\tau_i(t)\) therefore gives

\(0\le\frac{d_i(\theta_i^0,q_0)N_i(t)-min_jd_j(\theta_j^0,q_0)N_j(t)}{\sum_jN_j(t)}\)<br>
\(\le\frac{Bd_i(\theta_i^0,q_0)}{\sum_jN_j(t)}+2\varepsilon_{\tau_i(t)}\frac{\sum_jN_j(\tau_i(t))}{\sum_jN_j(t)}\)

