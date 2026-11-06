- _Gamma with known shape:_ \(Y_{i,n}|\theta_i\sim\mathrm{Gamma}(\kappa_i,\theta_i/\kappa_i)\) _with scale_ \(\theta_i/\kappa_i\) _and_ \(\kappa_i\) _known (_\(\kappa_i=1\) _gives the exponential distribution), prior_ \(\theta_i\sim\mathrm{InvGamma}(a_i(0),b_i(0))\) _with a<sub>i</sub>_(0)_\>_2, \(b_i(0)>0,\mathcal{J}=(0,\infty)\).<tbc>

**-** _Lognormal with known log-variance:_ \(Y_{i,n}|\theta_i\sim\mathrm{Lognormal}(\mathrm{log}\theta_i-\sigma_i^2/2\), \(\sigma_i^2)\) _with_ \(\sigma_i^2\) _known, prior_ \(\mathrm{log}\theta_i\sim N(m_i(0),s_i^2(0)),\mathcal{J}=(0,\infty)\).

Sampling proceeds in _T_+1 rounds, an optional warm-up round indexed _t_=0 followed by _T_ adaptive rounds. In the warm-up round, each item is sampled \(n_0\in\mathbb{Z}_{\ge 0}\) times. In rounds _t_=1_,...,T_, we choose a batch of \(B_t\in\mathbb{Z}_+\) samples, where the per-round batch sizes \(\{B_t\}_{t=1}^T\) are pre-specified. The choice of samples in round _t_ is denoted by the vector \(\Delta^t=(\Delta_1^t,\dots,\Delta_I^t)\), where \(\Delta_i^t\in\mathbb{Z}_{\ge 0}\) is the number of samples assigned to item _i_. Let _N<sub>i</sub>(t_) denote the total samples allocated to item _i_ up to but not including round _t_, so that _N<sub>i</sub>_(0)=0, _N<sub>i</sub>_(1)=_n_<sub>0</sub>, and

\(N_i(t+1)=N_i(t)+\Delta_i^t,t=1,\dots,T.\)

Let H_<sub>t</sub>_ denote the history at time _t_, which is the collection of priors \(\{\Pi_{i,0}\}_{i=1}^I\) and observations \(\{Y_{i,n}:1\le i\le I\), \(1\le n\le N_i(t)\}\). We write \(\mathbb{E}_t[\cdot]\) and \(\mathbb{P}_t(\cdot)\) for conditional expectation and probability given H_<sub>t</sub>_. Let \(\Pi_{i,t}\) denote the posterior distribution of \(\theta_i\) given H_<sub>t</sub>_ and define \(\mu_i(t):=\mathbb{E}_t[\theta_i],v_i(t):=\mathbb{V}_t(\theta_i),F_{i,t}(x):=\mathbb{P}_t(\theta_i\le x)\). In round _t_, we refer to \(\Pi_{i,t}\) as the current prior.

In any round _t_, if we were to select items based on the current prior, we would pick the _k_ items with the largest posterior means. Thus, it is convenient to define the following: for any vector \(\mathbf{x}\in\mathbb{R}^I\), let _S<sub>k</sub>_(**x**) denote the set of indices of the _k_ largest elements of **x**. Write \(\mu(t)=(\mu_1(t),\dots,\mu_I(t))\) and \(\theta=(\theta_1,\dots,\theta_I)\). For any \(\theta\in\mathbb{R}^I\), the opportunity cost of the current selection \(S_k(\mu(t))\) is<tbc>

\(\mathrm{OC}(S_k(\mu(t)),\theta):=\sum_{i\in S_k(\theta)}\theta_i-\sum_{i\in S_k(\mu(t))}\theta_i.\)

<tbc>Thus the Bayesian expected opportunity cost given H_<sub>t</sub>_ is

\(\mathrm{EOC}(\mathcal{H}_t)=\mathbb{E}_{\theta|\mathcal{H}_t}\big[\mathrm{OC}(S_k(\mu(t)),\theta)\big].\) (1)

The decision maker’s problem is to sequentially choose the sample batches \(\{\Delta^t\}_{t=1}^T\) that minimize the terminal expected opportunity cost EOC(H<sub>_T_+1</sub>). This can be formulated as a dynamic program, but it is intractable to solve, as discussed in the introduction. We next formulate a _static_ surrogate objective that guides the choice of batch in each round.

## 3. Surrogate objective via EOC bound

EOC(H_<sub>t</sub>_) does not generally admit an expression amenable to analysis, so (1) is not immediately useful for choosing which batch of samples to collect. Thus, we construct the per-round surrogate objective in two steps. First, Lemma 1 gives an upper bound on EOC(H_<sub>t</sub>_) that is amenable to analysis. Second, in §3.1, we make this bound a function of the round-_t_ allocation to guide the choice of future samples. We then discuss how<tbc>

