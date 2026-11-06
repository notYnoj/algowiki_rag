<tbc>Consider adding an evaluation (_i,j_) to _n_. If the outcomes of _n_ were observed, the resulting posterior _p<sub>t</sub>_ would give expected covariance \(\overline{\Sigma_t}((i,j),p_t)\) after the additional evaluation. Averaging over the outcomes of _n_ gives

\(\overline{\Sigma_t}(n+F^{ij},p_{t-1})=\mathbb{E}\big[\overline{\Sigma_t}((i,j),p_t)\big|n,p_{t-1}\big].\)

Here \(\overline{\Sigma_t}((i,j),p_t)\) averages over the two outcomes of (_i,j_) given _p<sub>t</sub>_, while the outer expectation averages over the outcomes of the already committed batch _n_.

We approximate this expectation by fixing the covariance after _n_ at \(\Sigma'_t(n)\). We then compute the expected covariance after adding (_i,j_) by averaging over its two possible outcomes under \(N(\mu_{t-1},\Sigma'_t(n))\), giving

\(\overline{\Sigma_t}(n+F^{ij},p_{t-1})\approx\overline{\Sigma_t}\big((i,j),N(\mu_{t-1},\Sigma'_t(n))\big)=\Sigma'_t(n+F^{ij}),\)

where the equality follows from Lemma 2 and gives (12). The first update is exact because _n_=0 and \(\Sigma'_t(0)=\Sigma_{t-1}\). Note that for the same batch matrix _n_, the approximation \(\Sigma'_t(n)\) can differ depending on the order in which evaluations are committed.

## A.2. The batched endgame

In this subsection, it is convenient to use an alternative notation for a batch. Above, a batch was represented by its count matrix _n(t_), which records how many times each evaluation (_i,j_) is conducted in round _t_. Here it will be useful to distinguish between repeats of the same evaluation, so we fix an ordering of the evaluations, writing a batch of _U_ evaluations as (_i_<sub>1</sub>_,j_<sub>1</sub>),(_i_<sub>2</sub>_,j_<sub>2</sub>)_,...,(i<sub>U</sub>,j<sub>U</sub>_), where each \((i_u,j_u)\in\mathcal{I}\) and _j<sub>u</sub>_:=min(_j<sub>u</sub>,_1). The associated count matrix is \(n_{ij}(t)=\sum_{u=1}^U\unknown\{(i_u,j_u)=(i,j)\}\) for each \((i,j)\in\mathcal{I}\).

Consider a candidate feasible batch (_i_<sub>1</sub>_,j_<sub>1</sub>)_,...,(i<sub>U</sub>,j<sub>U</sub>_) with count matrix _n_. Let \(X_u\in\{-1,1\}\) denote the outcome of the _u_th evaluation and define \(X:=(X_1,\dots,X_U)^\top\). For an outcome vector **_x_**, write \(\mu_t(x|n,p_{t-1})=\mathbb{E}[\theta|X=x,n,p_{t-1}]\).

### A.2.1. The myopic value of a batch

We begin by writing the myopic value function of §2.3 using the notation introduced above. The myopic value function which the KG policy maximizes each round (reformulated from §2.3) is

\(V_\mathrm{myopic}(n|p_{t-1})=\sum_{x\in\{-1,1\}^U}\mathbb{P}(X=x|n,p_{t-1})\sum_{i\in S_k^*(\mu_t(x|n,p_{t-1}))}\mu_{t,i}(x|n,p_{t-1})-\sum_{i\in S_k^*(\mu_{t-1})}\mu_{t-1,i},\) (A.2)

with _V_<sub>myopic</sub>(0|_p_<sub>_t_-1</sub>)=0. Proposition A.1, which applies the results of Mullahy (2017), gives explicit expressions for the outcome-dependent quantities P(**_X_**=**_x_**|_n,p_<sub>_t_-1</sub>) and \(\mu_t(x|n,p_{t-1})\).

PROPOSITION A.1. _Define_ \(C\in\mathbb{R}^{U\times U}\) _by_

\(C_{uu^\prime}=\beta_{j_u}\beta_{j_{u^\prime}}(e_{i_u}-e_{j_u})^\top\Sigma_{t-1}(e_{i_{u^\prime}}-e_{j_{u^\prime}})+\unknown\{u=u'\},u,u'=1,\dots,U.\)

_For any_ \(x\in\{-1,1\}^U\)_, let_ \(D:=\mathrm{diag}\big(\sqrt{C_{11}},\dots,\sqrt{C_{UU}}\big)\), \(D_x:=\mathrm{diag}(x_1,\dots,x_U)\), \(\widetilde{C}_x:=D_xD^{-1}CD^{-1}D_x\)_, and_ \(\alpha(x):=(\alpha_1(x),\dots,\alpha_U(x))^\top\) _where_ \(\alpha_u(x)=\frac{x_u\beta_{j_u}(\mu_{t-1,i_u}-\mu_{t-1,j_u})}{\sqrt{C_{uu}}}\) _for each u. Let_ \(\Phi_U(\cdot;\widetilde{C}_x)\) _denote the CDF_

