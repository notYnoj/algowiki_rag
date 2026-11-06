## Appendix A: Proofs for §3

_Proof of Lemma 1(i)_ Fix any realized \(\theta\in\mathbb{R}^I\) and any \(q\in\mathbb{R}\). Then

\(\text{OC}(S_k(\mu(t)),\theta)=\sum_{i\in S_k(\theta)}\theta_i-\sum_{i\in S_k(\mu(t))}\theta_i\)<br>
\(=^{(a)}\sum_{i\in S_k(\theta)\backslash S_k(\mu(t))}\theta_i-\sum_{i\in S_k(\mu(t))\backslash S_k(\theta)}\theta_i\)<br>
\(=^{(b)}\sum_{i\in S_k(\theta)\backslash S_k(\mu(t))}(\theta_i-q)+\sum_{i\in S_k(\mu(t))\backslash S_k(\theta)}(q-\theta_i)\)<br>
\(\le\sum_{i\notin S_k(\mu(t))}(\theta_i-q)^++\sum_{i\in S_k(\mu(t))}(q-\theta_i)^+,\)

where (a) holds because indices in \(S_k(\mu(t))\cap S_k(\theta)\) cancel, and (b) holds because \(|S_k(\mu(t))\backslash S_k(\theta)|=|S_k(\theta)\backslash S_k(\mu(t))|\). Taking posterior expectation proves the claim. \(\square\)

_Proof of Lemma 1(ii)_ Define<tbc>

\(G_t(q):=\mathbb{E}_t\left[\sum_{i\in S_k(\mu(t))}(q-\theta_i)^++\sum_{i\notin S_k(\mu(t))}(\theta_i-q)^+\right].\)

<tbc>By Assumption 1 each posterior CDF _F<sub>i,t</sub>_ is continuous on J, so differentiating under the expectation gives<tbc>

\(\frac{d}{dq}\mathbb{E}_t[(q-\theta_i)^+]=F_{i,t}(q),\frac{d}{dq}\mathbb{E}_t[(\theta_i-q)^+]=F_{i,t}(q)-1.\)

<tbc>Hence

\(G'_t(q)=\sum_{i\in S_k(\mu(t))}F_{i,t}(q)+\sum_{i\notin S_k(\mu(t))}(F_{i,t}(q)-1)=\sum_{i=1}^IF_{i,t}(q)-(I-k).\)

Additionally, by Assumption 1 each posterior density is positive on J, so each _F<sub>i,t</sub>_ is strictly increasing on J. Thus \(G'_t\) is continuous and strictly increasing on J, which gives convexity of _G<sub>t</sub>_. Taking limits, \(F_{i,t}(q)\rightarrow 0\) as \(q\rightarrow-\infty\) and \(F_{i,t}(q)\rightarrow 1\) as \(q\rightarrow+\infty\), so \(G'_t(q)\rightarrow-(I-k)<0\) as \(q\rightarrow-\infty\) and \(G'_t(q)\rightarrow k>0\) as \(q\rightarrow+\infty\). By the intermediate value theorem, \(G'_t\) has a unique zero \(q^*(t)\in\mathcal{J}\), characterized by \(\sum_iF_{i,t}(q^*(t))=I-k\), equivalently (2), and _q_<sup>∗</sup>(_t_) is the unique minimizer of _G<sub>t</sub>_. \(\square\)

_Proof of Proposition 1_ Starting with _r_=0, set _V_<sub>0</sub>(0)=0 and \(V_0(b)=+\infty\) for _b_=1_,...,B<sub>t</sub>_. For the inductive step, suppose \(V_{r-1}(\cdot)\) is already known and consider the (_r,b_) subproblem. Because the objective in (8) is separable across items, fixing item _r_’s allocation at some \(\delta\in\{0,\dots,b\}\) splits the subproblem into two pieces: the cost \(\ell_{r,t}(\delta)\) incurred by item _r_, plus the cost of optimally allocating exactly the residual \(b-\delta\) samples among items 1_,...,r_-1, which is \(V_{r-1}(b-\delta)\). Therefore, for each \((r,b)\in\{(x,y):1\le x\le I,0\le y\le B_t\}\) the optimal value function is given by

\(V_r(b)=min_{\delta\in\{0,\dots,b\}}\{V_{r-1}(b-\delta)+\ell_{r,t}(\delta)\},\Delta_r^*(b)\in argmin_{\delta\in\{0,\dots,b\}}\{V_{r-1}(b-\delta)+\ell_{r,t}(\delta)\}.\)

