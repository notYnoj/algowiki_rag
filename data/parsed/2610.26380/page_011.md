<tbc>components of any vector \(\vartheta\in\mathbb{R}^I\). After _T_ rounds of evaluations, the decision-maker selects a set of items \(S_k\subset\{1,\dots,I\}\) with |_S<sub>k</sub>|=k_ and the EOC is

\(\text{EOC}(S_k;p_T):=\mathbb{E}_\unknown\left[\sum_{i\in S_k^*(\vartheta)}\theta_i-\sum_{i\in S_k}\theta_i\left|p_T\right]=\mathbb{E}_\unknown\left[\sum_{i\in S_k^*(\vartheta)}\theta_i\left|p_T\right]-\sum_{i\in S_k}\mu_{T,i}.\) (1)

Throughout the paper, conditioning on _p<sub>t</sub>_ means that the expectation (or probability) is taken with respect to \(\theta\sim p_t\). The first term in (1) does not depend on the choice of _S<sub>k</sub>_, so minimizing EOC is equivalent to maximizing the sum of the selected set’s posterior means (the second term). It follows that the optimal set to select given \(\mu_T\) is the set of _k_ items with the largest posterior means \(S_k^*(\mu_T)\).

With the terminal objective established, we next formulate the sequential problem of minimizing it as a dynamic program. At any round _t_ the state is described by (_p_<sub>_t_-1</sub>_,R<sub>t</sub>_). First consider a state where \(min(r_0,r_1)\le R_t<2min(r_0,r_1)\), which is a sufficient condition for _t=T_. The decision-maker chooses an evaluation \((i,j)\in\mathcal{I}\) with \(r_j\le R_t\), an outcome _X<sub>t</sub>=x_ is observed, and the posterior EOC is

\(\mathbb{E}_\unknown\left[\sum_{\ell\in S_k^*(\theta)}\theta_\ell\left|X_t=x,(i,j),p_{t-1}\right]-\sum_{\ell\in S_k^*(\mu_t(x|(i,j)))}\mu_{t,\ell}(x|(i,j)),\) (2)

where \(\mu_t(x|(i,j))=\mathbb{E}[\theta|X_t=x,(i,j),p_{t-1}]\). Therefore, the problem is to choose the evaluation (_i,j_) that minimizes the expectation of (2) over its outcome _X<sub>t</sub>_. By the law of total expectation, the expectation of the first term equals \(\mathbb{E}_\unknown[\sum_{\ell\in S_k^*(\theta)}\theta_\ell|p_{t-1}]\), which does not depend on the choice of (_i,j_). Thus, the optimal evaluation is

\((i_t,j_t)\in argmax_{(i,j)\in\mathcal{I}:r_j\le R_t}\sum_{x\in\{-1,1\}}\mathbb{P}(X_{ij}=x|p_{t-1})\sum_{\ell\in S_k^*(\mu_t(x|(i,j)))}\mu_{t,\ell}(x|(i,j)).\)

To consider the full sequential process, let _V_<sup>∗</sup>(_p_<sub>_t_-1</sub>_,R<sub>t</sub>_) denote the largest expected sum of terminal selected posterior means from state (_p_<sub>_t_-1</sub>_,R<sub>t</sub>_). If no evaluation is affordable, the decision-maker selects \(S_k^*(\mu_{t-1})\) now, giving

\(V^*(p_{t-1},R_t)=\sum_{\ell\in S_k^*(\mu_{t-1})}\mu_{t-1,\ell},R_t<min(r_0,r_1).\)

Otherwise, the optimal value function satisfies the Bellman equation

\(V^*(p_{t-1},R_t)=max_{(i,j)\in\mathcal{I}:r_j\le R_t}\sum_{x\in\{-1,1\}}\mathbb{P}\big(X_{ij}=x\big|p_{t-1}\big)\times V^*\big(p_t(\cdot|x,(i,j)),R_t-r_j\big),\) (3)

where \(p_t(\cdot|x,(i,j))\) denotes the posterior obtained after starting from prior _p_<sub>_t_-1</sub>, choosing evaluation (_i,j_), and observing outcome _x_.

## 2.3. Shortcomings of the knowledge gradient policy

Addressing the curse of dimensionality of the dynamic program in (3), the KG policy adopts the myopic version of it, given by

\(V_\text{myopic}\big(\big((i,j)|p_{t-1}\big):=\sum_{x\in\{-1,1\}}\mathbb{P}\big(X_{ij}=x\big|p_{t-1}\big)\left(\sum_{\ell\in S_k^*(\mu_t(x|(i,j)))}\mu_{t,\ell}(x|(i,j))-\sum_{\ell\in S_k^*(\mu_{t-1})}\mu_{t-1,\ell}\right).\) (4)

