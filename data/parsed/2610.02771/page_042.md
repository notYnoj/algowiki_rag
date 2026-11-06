If \(t>\tau\), the process has stopped, and \(Z_t=(1,\emptyset,\perp)\) is deterministic under both instances. The conditional KL divergence is exactly 0.

If \(t\le\tau\), the arm _K<sub>t</sub>_ and query set _A<sub>t</sub>_ are deterministic functions of F<sub>_t_-1</sub>. The only randomness lies in the Bernoulli observation _Y<sub>t</sub>_. If \(K_t\neq i\), its distribution is unchanged between \(\nu^{(0)}\) and \(\nu^{(i)}\), so the conditional divergence is 0. If _K<sub>t</sub>=i_, then _Y<sub>t</sub>_∼Ber(_P_<sub>-</sub>(_A<sub>t</sub>_)) under \(\nu^{(0)}\) and _Y<sub>t</sub>_∼Ber(_P_<sub>+</sub>(_A<sub>t</sub>_)) under \(\nu^{(i)}\). By Lemma 36, the conditional divergence is bounded by \(4C_0\Delta^2/(J\sigma^2)\). Thus:

\(\mathrm{KL}(\mathrm{Pr}_0^{(T)},\mathrm{Pr}_i^{(T)})\le\sum_{t=1}^T\mathbb{E}_0\left[\mathbf{1}\{t\le\tau,K_t=i\}4C_0\frac{\Delta^2}{J\sigma^2}\right]=4C_0\frac{\Delta^2}{J\sigma^2}\mathbb{E}_0[N_i(T\wedge\tau)].\)

Because F_<sub>T</sub>_ forms an increasing filtration generating the full transcript, \(\mathrm{KL}(\mathrm{Pr}_0,\mathrm{Pr}_i)=\mathrm{lim}_{T\rightarrow\infty}\mathrm{KL}(\mathrm{Pr}_0^{(T)},\mathrm{Pr}_i^{(T)})\). Applying the monotone convergence theorem to \(N_i(T\wedge\tau)\) yields the final bound.

_Proof of Theorem 12._ Assuming \(\mathbb{E}_0[\tau]<\infty\) (otherwise the lower bound holds trivially), we link the information complexity from Lemma 38 to the statistical requirement from Lemma 37, for each _i_=2_,...,K_:<tbc>

\(4C_0\frac{\Delta^2}{J\sigma^2}\mathbb{E}_0[N_i(\tau)]\ge c_1\mathrm{log}\left(\frac{1}{\delta}\right).\)

<tbc>Rearranging this inequality for the expected sample complexity yields:<tbc>

\(\mathbb{E}_0[N_i(\tau)]\ge\frac{c_1}{4C_0}\frac{\sigma^2J}{\Delta^2}\mathrm{log}\left(\frac{1}{\delta}\right).\)

<tbc>All these inequalities hold under the same base instance. Summing over its _K_-1 suboptimal arms gives<tbc>

\(\mathbb{E}_0[\tau]\ge\sum_{i=2}^K\mathbb{E}_0[N_i(\tau)]\ge\frac{c_1}{4C_0}(K-1)\frac{\sigma^2J}{\Delta^2}\mathrm{log}\left(\frac{1}{\delta}\right).\)

<tbc>Recalling our construction choice that \(J=\lfloor\mathrm{log}_2(\frac{\sigma}{\Delta})\rfloor\), it holds that \(J\ge c_2\mathrm{log}(\frac{\sigma}{\Delta})\) for some constant _c_<sub>2</sub>_\>_0 given the restriction \(\Delta\le\sigma/4\). Substituting this structural scale count gives:

\(\mathbb{E}_0[\tau]\ge c(K-1)\frac{\sigma^2}{\Delta^2}\mathrm{log}\left(\frac{\sigma}{\Delta}\right)\mathrm{log}\left(\frac{1}{\delta}\right),\)

where \(c=\frac{c_1c_2}{4C_0}>0\) is an absolute constant, completing the proof.

