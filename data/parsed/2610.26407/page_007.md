<tbc>the resulting per-round objective differs from those in prior work in §3.2 and give efficient algorithms for finding the batch that minimizes it in §3.3. §3.4 presents the sequential sampling procedure, and §3.5 gives explicit expressions of the sampling rule for the ESCP. We begin with the EOC upper bound, which is based on comparing each item’s \(\theta_i\) to a threshold.

LEMMA 1 (Threshold upper bound on EOC).

(i) _For every threshold_ \(q\in\mathbb{R}\),<tbc>

<tbc>\(\mathrm{EOC}(\mathcal{H}_t)\le\mathbb{E}_t\left[\sum_{i\in S_k(\mu(t))}(q-\theta_i)^++\sum_{i\notin S_k(\mu(t))}(\theta_i-q)^+\right].\)<tbc>

<tbc>(ii) _The right-hand side of_ (i) _is convex in q and has a unique minimizer q_<sup>∗</sup>(_t_) _characterized by_

\(\mathbb{E}_t\left[|\{i:\theta_i\ge q^*(t)\}|\right]=\sum_{i=1}^I\{1-F_{i,t}(q^*(t))\}=k.\) (2)

_Proof_ All proofs are provided in the Appendix.

Part (i) gives a family of upper bounds on EOC, each separable across items. For an item in the current top-_k_ set, its corresponding term in the bound is the expected shortfall of its true mean below threshold _q_. For an item outside this set, its corresponding term is the expected amount its true mean exceeds the threshold. Part (ii) states that the tightest bound in this family is given by _q_<sup>∗</sup>(_t_), the threshold such that, in expectation, exactly _k_ item means are larger than it. This makes _q_<sup>∗</sup>(_t_) a natural threshold choice when constructing the surrogate objective. We also consider another top-_k_ threshold motivated by the theoretical analysis in §4. Write \(d_i(x,y):=\mathrm{KL}(P_i(\cdot|x)\|P_i(\cdot|y))\) for the Kullback–Leibler (KL) divergence between the sampling distributions of item _i_ at means _x_ and _y_, and let \(\mu_{[1]}(t)\ge\cdots\ge\mu_{[I]}(t)\) denote the ordered posterior means. We define the threshold

\(q^\dagger(t):=\left\{\begin{array}{ c c }
\mathrm{argmin}_{\mu_{[k+1]}(t)<q<\mu_{[k]}(t)}\sum_{i=1}^I\frac{1}{d_i(\mu_i(t),q)}, & \mu_{[k]}(t)>\mu_{[k+1]}(t), \\
\mu_{[k]}(t), & \mu_{[k]}(t)=\mu_{[k+1]}(t).
\end{array}\right.\) (3)

§4 explains why this choice of top-_k_ threshold is "good". In what follows, let _q(t_) denote the top-_k_ threshold used in round _t_, which can be either _q_<sup>∗</sup>(_t_) or _q_<sup>†</sup>(_t_).

## 3.1. Forward-looking objective

Given _q(t_), the threshold bound at state H_<sub>t</sub>_ is

\(\mathbb{E}_t\left[\sum_{i\in S_k(\mu(t))}(q(t)-\theta_i)^++\sum_{i\notin S_k(\mu(t))}(\theta_i-q(t))^+\right].\) (4)

To make this a function of a proposed round-_t_ allocation \(\unknown=(\Delta_1,\dots,\Delta_I)\), we take the expectation with respect to an approximation of the random posterior of \(\theta_i\) _after_ allocating \(\unknown\) and observing its outcomes. This approximation preserves the shape of \(\Pi_{i,t}\) and has mean and variance equal to the expected posterior mean and variance. We say two distributions have the same _shape_ if they are equivalent after centering by their<tbc>

