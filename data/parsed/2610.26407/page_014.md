<tbc>ASSUMPTION 2 (Bounded exponential-family model). _In addition to Assumption 1,_ J=(_L,U_) _with_ \(-\infty<L<U<\infty\)_. For every item i, the likelihood has the form_<tbc>

\(p_i(y|x)=h_i(y)exp\{\eta_i(x)T_i(y)-A_i(\eta_i(x))\},x\in\mathcal{J},\)

<tbc>_where T<sub>i</sub> is strictly increasing and A<sub>i</sub> is twice differentiable. Write_ \(\mathcal{E}_i:=\eta_i(\mathcal{J})=(\underline{\eta_i},\overline{\eta_i})\)_, with_ \(-\infty<\underline{\eta_i}<\overline{\eta_i}<\infty\)_, and let_ \(\widetilde{\pi}_{i,0}\) _denote the prior density of_ \(\eta_i(\theta_i)\)_. We assume_

\(sup_{\eta\in\mathcal{E}_i}|A'_i(\eta)|<\infty,0<inf_{\eta\in\mathcal{E}_i}\widetilde{\pi}_{i,0}(\eta)\le sup_{\eta\in\mathcal{E}_i}\widetilde{\pi}_{i,0}(\eta)<\infty.\)

The boundedness assumptions are used in the posterior convergence analysis primarily to facilitate generality across this broad range of families. As Russo (2020, p. 1635) notes, "Analogous results are easily established for certain unbounded conjugate priors." All five ESCP in Remark 1 satisfy Assumption 2 when their priors are restricted and normalized to a bounded interval whose closure is contained in J.

The next result shows that the exponential decay rate of a posterior probability is determined by the empirical sampling proportions. Let \(\Delta_I:=\{w\in\mathbb{R}^I:w_i\ge 0,\sum_iw_i=1\}\), and define the empirical sampling proportions by \(\widehat{w}_i(t):=N_i(t)/\sum_jN_j(t)\) for \(t\ge 2\).

LEMMA 2 (Russo (2020, Proposition 5)). _Under any sequential sampling rule, for every nonempty open set_ \(O\subseteq\mathcal{J}^I\),<tbc>

\(-\frac{log\mathbb{P}_t(\theta\in O)}{\sum_iN_i(t)}-inf_{x\in O}\sum_{i=1}^I\widehat{w}_i(t)d_i(\theta_i^0,x_i)\longrightarrow 0.\) (11)

<tbc>To interpret the first term in (11), \(\{\theta\in O\}\) is the "bad" event whose probability we want to control. For top-_k_ selection, _O_ is the set of _alternative_ parameters: parameters whose top-_k_ set is different from \(S_k(\theta^0)\). Ignoring ties which have a posterior probability of zero, these are the parameters where some pair of items (_i,j_) satisfies \(i\le k<j\), and yet \(\theta_j>\theta_i\). Accordingly, define the alternative space

\(Alt(\theta^0):=\bigcup_{i\le k<j}\{x\in\mathcal{J}^I:x_j>x_i\}\)

so that \(\mathbb{P}_t(\theta\in Alt(\theta^0))=\mathbb{P}_t(S_k(\theta)\neq S_k(\theta^0))\). We will apply Lemma 2 with \(O=Alt(\theta^0)\). In the second term, for fixed sampling proportions **_w_**, the quantity \(\sum_iw_id_i(\theta_i^0,x_i)\) is the expected log-likelihood ratio per observation between the true parameter \(\theta^0\) and an alternative **_x_**. The infimum over _O_ therefore identifies the alternative parameter that this allocation provides the least evidence to distinguish from the true parameter. For \(w\in\Delta_I\), denote this infimum at \(O=Alt(\theta^0)\) by \(\Gamma(w;\theta^0)\). Lemma 3 characterizes its structure.

LEMMA 3 (Pairwise representation of \(\Gamma\)). _For every_ \(w\in\Delta_I\),

\(\Gamma(w;\theta^0):=inf_{x\in Alt(\theta^0)}\sum_{\ell=1}^Iw_\ell d_\ell(\theta_\ell^0,x_\ell)=min_{i\le k<j}min_{x\in[\theta_j^0,\theta_i^0]}\{w_id_i(\theta_i^0,x)+w_jd_j(\theta_j^0,x)\}.\) (12)

