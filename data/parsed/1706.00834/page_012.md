<tbc>We now prove that Property (1) of Definition 8 (i.e. product form) is also true since for all \(\unknown\in\mathcal{P}_s\):

\(\prod_{m\in M}(w_m^\text{new})^{\pi_m}=\prod_{v\in V-\mathcal{T}}\prod_{m\in M_v^{(\text{out})}}(w_m^\text{new})^{\pi_m}\)<br>
\(=\prod_{v\in V-\mathcal{T}}\prod_{m\in M_v^{(\text{out})}}\left(\widehat{w}_m\frac{\prod_{u:(v,u)\in m}Z_u}{Z_v}\right)^{\pi_m}\)<br>
\(=\left[\prod_{v\in V-\mathcal{T}}\prod_{m\in M_v^{(\text{out})}}(\widehat{w}_m)^{\pi_m}\right]\left[\prod_{v\in V-\mathcal{T}}\prod_{m\in M_v^{(\text{out})}}\left(\frac{\prod_{u:(v,u)\in m}Z_u}{Z_v}\right)^{\pi_m}\right].\)

Notice that \(\prod_{v\in V-\mathcal{T}}\prod_{m\in M_v^{(\text{out})}}\left(\frac{\prod_{u:(v,u)\in m}Z_u}{Z_v}\right)^{\pi_m}\) telescopes along the multiedges in the multipath \(\unknown\). After telescoping, since _Z<sub>v</sub>_=1 for all \(v\in\mathcal{T}\) , the only remaining term will be \(\frac{1}{Z_s}\) where _s_ is the souce node. Therefore we obtain:

\(\prod_{m\in M}(w_m^\text{new})^{\pi_m}=\left[\prod_{v\in V-\mathcal{T}}\prod_{m\in M_v^{(\text{out})}}(\widehat{w}_m)^{\pi_m}\right]\left[\prod_{v\in V-\mathcal{T}}\prod_{m\in M_v}\left(\frac{\prod_{u:(v,u)\in m}Z_u}{Z_v}\right)^{\pi_m}\right]\)<br>
\(=\left[\prod_{m\in M}(\widehat{w}_m)^{\pi_m}\right]\left[\frac{1}{Z_s}\right]\)<br>
\(=\frac{1}{Z_s}\prod_{m\in M}(\widehat{w}_m)^{\pi_m}=W^\text{new}(\unknown).\)

Regarding the time complexity, we first focus on the the recurrence relation \(Z_v=\sum_{m\in M_v}\widehat{w}_m\prod_{u:(v,u)\in m}Z_u\). Note that for each \(v\in V\) , _Z<sub>v</sub>_ can be computed in \(\mathcal{O}(c|M_v^{(\text{out})}|)\). Thus the computation of all _Z<sub>v</sub>_’s takes O(_c|M_|) time. Now observe that \(w_m^\text{new}\) for each multiedge \(m=(v,U)\in M\) can be found in O(_c_) time using \(w_m^\text{new}=\widehat{w}_m\frac{\prod_{u\in U}Z_u}{Z_v}\) . Hence the computation of \(w_m^\text{new}\) for all multiedges \(m\in M\) takes O(_c|M_|) time. Therefore the generalized weight pushing algorithm runs in O(_c|M_|) time.

## Regret Bound.

In order to apply the regret bound of EH we have to initialize the distribution _W_ on multipaths to the uniform distribution. This is achieved by setting all the weights \(\widehat{w}_m\)’s to 1 followed by an application of generalized weight pushing. Note that Theorem 1 is a special case of the theorem below when |_U_|=1 for all multiedge \((v,U)\in M\) and |T|=1.

**Theorem 10** _Given a multi-DAG_ H=(_V,M_) _with designated source node_ \(s\in V\) _and sink nodes_ \(\mathcal{T}\subset V\)_, assume_ N _is the number of multipaths in_ H _from s to_ T _, L_<sup>∗</sup> _is the total loss of best multipath, and D is an upper-bound on the_ 1_-norm of the count vectors of the multipaths (i.e._ \(\|\unknown\|_1\le D\) _for all multipaths_ \(\unknown\)_). Then with proper tuning of the learning rate_ \(\eta\) _over the trials, EH guarantees the following regret bound:_<tbc>

\(\mathcal{R}_{EH}\le\sqrt{2L^*Dlog\mathcal{N}}+Dlog\mathcal{N}.\)

