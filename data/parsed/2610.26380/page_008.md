<tbc>§6 considers the batch setting. §7 reports the results of the numerical experiments, and §8 gives concluding remarks.

## 2. Model and objective

This section defines the generative data model for pairwise comparisons and ratings, introduces the sequential evaluation process and formulates the optimization problem as a dynamic program. We then demonstrate that the KG policy is not well-suited for our setting, which motivates the surrogate objective of §3.

### 2.1. Generative model

We consider **_I_** items with latent utilities \(\theta=(\theta_1,\dots,\theta_I)\in\mathbb{R}^I\), which represent the values of selecting each item. We adopt a Bayesian framework and place a Gaussian prior on the utility vector, \(\theta\sim N(\mu_0,\Sigma_0)\) where \(\Sigma_0\) is positive definite. When preliminary information distinguishes the items, \(\mu_0\) and \(\Sigma_0\) can reflect it. When no such information is available, or when items are people and a prior that discriminates raises ethical or legal concerns, an exchangeable prior (\(\mu_0=\mathbf{0}\), \(\Sigma_0=s\mathrm{Id}_I\)) treats all items symmetrically.

Evaluators can provide two types of feedback, _pairwise comparisons_ and _ratings_. A _pairwise comparison_ of items _i_ and _j_ produces a binary outcome: one item is preferred to the other. The event that an evaluator prefers _i_ to _j_ is denoted by \(i\succ j\), and its probability is determined by \(\theta_i-\theta_j+\epsilon_1\), where \(\epsilon_1\sim N(0,\sigma_1^2)\). Thus, the evaluator’s ability to distinguish between the two items depends on the difference in their utilities and on \(\epsilon_1\), which captures imperfections in pairwise evaluations. The subscript 1 is used because item _i_ is compared to 1 other item. A _rating_ of item _i_ produces a binary ‘thumbs-up’ or ‘thumbs-down’ outcome, where item _i_ is implicitly compared to some utility threshold \(\theta_0\). Note that \(\theta_0\) is not a part of \(\theta\)--we use this notation to facilitate unified expressions for pairwise comparisons and ratings. Similar to the pairwise comparison model, the event that an evaluator ranks _i_ above the threshold is denoted by \(i\succ 0\) and its probability is determined by \(\theta_i-\theta_0+\epsilon_0\), where \(\epsilon_0\sim N(0,\sigma_0^2)\). Here \(\epsilon_0\) captures two sources of noise: the evaluator’s ability to estimate item _i_’s utility and the uncertainty about where the latent threshold \(\theta_0\) lies. The subscript 0 is used because item _i_ is compared to 0 items.

The set of possible evaluations is given by \(\mathcal{I}:=\left\{(i,j):0\le j<i\le I\right\}.\) Define _j_=min(_j,_1), which is 0(1) when an evaluation is a rating (comparison). For an evaluation \((i,j)\in\mathcal{I}\), let _X<sub>ij</sub>_ denote the outcome where<tbc>

\(X_{ij}=\left\{\begin{array}{ c c }
1 & \text{if}i\succ j \\
-1 & \text{if}i\prec j,
\end{array}\right.\)

<tbc>and, conditioned on the evaluator-noise term \(\epsilon_J\), \(\mathbb{P}(X_{ij}=1|\theta,\epsilon_J)=g(\theta_i-\theta_j+\epsilon_J)\), where \(g:\mathbb{R}\rightarrow(0,1)\) is some link function. For the remainder of the paper, unless specified otherwise, we consider the probit link function, commonly used to model human ordinal rating data (Liddell and Kruschke 2018), i.e., \(g=\Phi\), where \(\Phi\) is the standard normal CDF and \(\phi\) its density. Thus,

\(\mathbb{P}(X_{ij}=1|\theta)=\mathbb{E}_{\epsilon_J}\left[\Phi\left(\theta_i-\theta_j+\epsilon_J\right)\right]=\Phi\left(\frac{1}{\sqrt{1+\sigma_J^2}}(\theta_i-\theta_j)\right)=\Phi\left(\beta_J(\theta_i-\theta_j)\right),\)

