_Proof._ We show the contra-positive. Let _M_ be a perfect matching of the reduced instance with at most _L_-1 blocking pairs. Define \(K=\{v_i|M(\hat{u}_i)=t_z\text{for some}z\in[h]\}\) and \(E'=\{e|M(y_e)\in\hat{s}_z\text{for some}z\in[\genfrac(){pt}{2}{h}{2}]\}\). We aim to show that \(E'\) induces a size-_h_ clique.

Clearly |_K_|=_h_ and \(|E'|=\genfrac(){pt}{2}{h}{2}\) since _M_ is a perfect matching.

Consider an arbitrary edge \(e\in E'\) and let _e_={_v<sub>i</sub>,v<sub>j</sub>_}. We claim that both _v<sub>i</sub>_ and _v<sub>j</sub>_ must be in _K_.

Towards a contradiction, suppose that one of the endpoints of _e_ is not in _K_, say \(v_i\notin K\). Then, by definition and by the preferences of _u<sub>i</sub>_ we infer \(M(\hat{u}_i)=\hat{w}_i\). By the acceptability graph over _u<sub>i</sub>_, we infer that either _M(u<sub>i</sub>_)=_w<sub>i</sub>_ or \(M(u_i)\in\Theta(v_i)\).

If _M(u<sub>i</sub>_)=_w<sub>i</sub>_, then for each \(z\in[L]\), either \(\{u_i,\pi_e^{u_i}[z]\}\) or \(\{y_e,\theta_e^{u_i}[z]\}\) is blocking, inducing at least _L_ blocking pairs, a contradiction.

If \(M(u_i)=\theta_{e^\prime}^{u_i}[r]\) for some \(e'\in E\) with \(v_i\in e'\) and \(r\in[L]\), then by the preferences of \(\hat{\pi}_{e^\prime}^{u_i}\) we infer that \(M(\hat{\pi}_{e^\prime}^{u_i})=\hat{\theta}_{e^\prime}^{u_i}\). Since both \(\theta_{e^\prime}^{u_i}\) and \(\hat{\theta}_{e^\prime}^{u_i}\) are not available, we infer that \(M(\hat{\pi}_{e^\prime}^{u_i})=y_{e^\prime}\), a contradiction to Claim 2.

We have just shown that for each edge \(e\in E'\) both endpoints must be in _K_. Since \(|E'|=\genfrac(){pt}{2}{h}{2}\), we infer that \(|K|\ge h\). Since |_K_|=_h_, we immediately obtain that _K_ induces a clique of size _h_. (end of Claim 3) \(\diamond\)

Since Clique is W\[1\]-hard, the theorem follows directly from Claims 1 and 3.

We proceed with the roommates setting. We show that the same inapproximability result from the marriage setting holds for roommates setting even if we do not set any bound of the size of the target matching. The idea is to adapt the reduction from Theorem 1 by adding a very large but _even_ number of agents for every original agent with preferences so that each original agent must be matched as desired in that reduction in order to avoid too many blocking pairs. Note that such adaption has become a standard technique for many reduction; see for instance the work by Abraham et al. \[1, Lemma 2\] and Chen et al. \[6, Construction 2\].

**Corollary 1.** _Let_ \(F:\mathbb{N}\rightarrow\mathbb{N}\) _be an arbitrary computable function. Given an instance_ \((\mathcal{P},k,\beta)\) _of_ Min-BP- SRI-dec _it is_ W\[1\]_-hard to distinguish between the following two cases:_

(_i)_ P _admits a k matching with at most_ \(\beta\) _blocking pairs._<tbc>

_(ii)_ _Every matching of_ P _has at least_ \(F(\beta)\cdot\beta\) _blocking pairs._

_Proof._ As mentioned above, we will modify the reduction from Theorem 1. Let (_G,h_) be an instance of Clique, and let (_I,k_) be the instance of Min-BP-SMI constructed in Theorem 1. Let \(\hat{V}\) be the set of agents in _I_. Note that the reduction in Theorem 1 does not work for Min-BP-SRI, because Min-BP-SRI does not require every agent to be matched. To fix this, we add a large set _S<sub>u</sub>_ of even number of agents for each original agent _u_ in \(\hat{V}\) and append _S<sub>u</sub>_ to the end of the preferences of _u_ to ensure that _u_ is matched in the same way as in the proof for Theorem 1. Let \(\hat{I}\) be the modified instance for Min-BP-SRI. Then,

(i) if _M_ is a matching of _I_ in which every agent in \(\hat{V}\) is matched to another agent in \(\hat{V}\), then there is a matching \(M'\) of \(\hat{I}\) that admits the same number of blocking pairs as _M_, and<tbc>

(ii) if \(M'\) is a matching of \(I'\) in which some agent in \(\hat{V}\) is not matched to another agent in \(\hat{V}\), then \(M'\) admits more than _F(h_) blocking pairs.

Thus, the corollary follows.

## 4 FPT-approximability of Max-SMTI

In this section, we complement the result by Marx and Schlotter \[24\] and show that Max-SMTI admits an FPT-AS with respect to the number \(\tau\) of agents with preferences containing ties. More precisely, we provide an FPT-algorithm (with respect to \(\tau\)) that for every approximation ratio \(\varepsilon\in[\frac{2}{3},1)\) outputs a stable matching with size at least \(\varepsilon\cdot\text{OPT}(I)\) where OPT(_I_) denotes the size of an maximum-size stable matching in _I_. Note that we do not need to consider approximation factor between 0 and \(\frac{2}{3}\) since there is a factor-\(\frac{2}{3}\) polynomial-time algorithm by Király \[19\] and McDermid \[25\]. The idea of our algorithm is to show that for each approximation ratio \(\varepsilon\), either the size of a largest matching is upper-bounded by a function in \((\tau,\varepsilon)\) or the approximated result by Király \[19\] and McDermid \[25\] is good enough. In the former case, we apply the kernelization algorithm by Adil et al. \[2\] to obtain an FPT-algorithm for our parameter \((\tau,\varepsilon)\).

