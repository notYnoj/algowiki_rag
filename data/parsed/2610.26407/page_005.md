<tbc>half the best achievable rate. This establishes the type of general-_k_ guarantee conjectured by Russo (2020), but for our sampling rule.

In a range of simulations, we demonstrate that our method is competitive with and often improves on the current state-of-the-art approaches, including those specialized to _k_=1 as well as those for general _k\>_1, those specialized to Gaussian as well as other distributions, and both at small and large budgets. These comparisons are conducted in the non-batched setting to include as many existing methods as possible. In the batched setting, we show that our method significantly outperforms existing batch algorithms and its performance degrades less as the batch size grows.

We believe this method can be valuable to both researchers and practitioners. It is flexible across a wide range of practical settings, is competitive with the best algorithms in each of these settings, and extends naturally to richer settings, such as those with varying sample forms and sampling costs.

The rest of the paper is organized as follows: §2 formulates the model and objective, §3 derives the surrogate objective and the batch allocation algorithm, §4 establishes the theoretical guarantees, §5 presents the numerical experiments, and §6 concludes.

**2. Model and objective**

We consider _I_ items, indexed _i_=1_,...,I_, each with an unknown mean \(\theta_i\in\mathcal{J}\) , where \(\mathcal{J}\subseteq\mathbb{R}\) is an open interval. The goal is to select the _k\<I_ items with the largest means. Each item _i_ has a prior distribution \(\Pi_{i,0}\) on \(\theta_i\) with density \(\pi_{i,0}\). For item _i_, let Y_<sub>i</sub>_ be the outcome space, and let \(\{P_i(\cdot|\theta):\theta\in\mathcal{J}\}\) be a known mean-parametrized family of distributions on Y_<sub>i</sub>_ with density or mass function \(p_i(\cdot|\theta)\). Conditional on \(\theta_i\), the _n_th observation _Y<sub>i,n</sub>_ from item _i_ is drawn i.i.d. from \(P_i(\cdot|\theta_i)\), with \(\mathbb{E}[Y_{i,n}|\theta_i]=\theta_i\). We make the following regularity assumption.

ASSUMPTION 1 **(Regular one-parameter Bayesian model)**. _For each i_=1_,...,I, the prior_ \(\Pi_{i,0}\) _and sampling family_ \(\{P_i(\cdot|\theta):\theta\in\mathcal{J}\}\) _are such that for every_ \(n\ge 0\) _and every_ \((y_1,\dots,y_n)\in\mathcal{Y}_i^n\) _the posterior of_ \(\theta_i\) _conditioned on_ {_Y_<sub>_i,_1</sub>=_y_<sub>1</sub>_,...,Y<sub>i,n</sub>=y<sub>n</sub>_} _has continuous positive density on_ J _and finite second moment, and the corresponding posterior predictive distribution of Y_<sub>_i,n_+1</sub> _has finite second moment. In addition, the priors and observations are independent across items._

Remark 1 gives examples of standard conjugate pairs (ESCP) satisfying Assumption 1 that we will refer to throughout the paper.

REMARK 1 (ESCP). _ESCP covered by Assumption 1:_

- _Gaussian:_ \(Y_{i,n}|\theta_i\sim N(\theta_i,\sigma_i^2)\) _with_ \(\sigma_i^2\) _known, prior_ \(\theta_i\sim N(m_i(0),s_i^2(0)),\mathcal{J}=\mathbb{R}\).<tbc>

**-** _Bernoulli:_ \(Y_{i,n}|\theta_i\sim\text{Bern}(\theta_i),\text{\textit{prior}}\theta_i\sim\text{Beta}(a_i(0),b_i(0)),\mathcal{J}=(0,1)\).<tbc>

**-** _Poisson:_ \(Y_{i,n}|\theta_i\sim\text{Pois}(\theta_i),\text{\textit{prior}}\theta_i\sim\text{Gamma}(a_i(0),b_i(0))\) _with rate_ \(b_i(0),\mathcal{J}=(0,\infty)\).<tbc>

