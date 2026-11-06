where the last step uses \(\mathbb{E}[(mp_\ell-K)_+]=\frac{1}{2}\mathbb{E}|K-mp_\ell|\) and Cauchy-Schwarz. Consequently,

\((F_\rho(p_\ell)-\rho)(1-R_\ell)\le\frac{(1-2\rho)\sqrt{p_\ell(1-p_\ell)}+2\sqrt{\rho(1-\rho)}(1-p_\ell)}{\sqrt{m}}\)<br>
\(\le m^{-1/2},\) (51)

again by Cauchy-Schwarz and \((1-2\rho)^2+4\rho(1-\rho)=1\). This proves (46); substituting it into (45) proves the theorem.

The lower bound uses the top eigenvector of \(T_{\rho,\ell}\); the upper bound holds for every choice of amplitudes with the stated cutoff.

**Corollary 1** (Independently random target sets)**.** _Fix a constraint matrix with m rows and a deterministic, syndrome-consistent decoder that returns zero on the zero syndrome. Choose the target sets independently and uniformly among the r-element subsets of_ F_<sub>q</sub>, where_ 0_\<r\<q, independently of the decoder. Run DQI with the binomial amplitudes of (47) at_ 0_\<p\<_1_. Let_ \(\varepsilon_p\) _be the decoder’s word-error probability when each coordinate is independently unchanged with probability_ 1-_p and otherwise uniformly distributed over the nonzero field elements. Writing_ \(\rho=r/q\) _and averaging over both the targets and the success-conditioned DQI measurement, the expected satisfaction fraction f satisfies_

\((1-\varepsilon_p)F_\rho(p)-v\le f\le(1-\varepsilon_p)F_\rho(p)+\varepsilon_p+v,\)<br>
\(v=2\sqrt{\frac{F_\rho(p)(1-F_\rho(p))\varepsilon_p(1-\varepsilon_p)}{m}}.\) (52)

_In particular,_ \(v\le 1/(2\sqrt{m})\).

_Proof._ The binomial amplitudes give the product state

\(|\Gamma^{(p)}\rangle=\otimes_{i=1}^m\left(\sqrt{1-p}|0\rangle+\sqrt{p}\sum_{a\neq 0}\widetilde{g}_i(a)|a\rangle\right).\) (53)

Its expectation and variance under \(\widetilde{\mathsf{S}}_\mathrm{err}\) are

\(\mathbb{E}_{\Gamma^{(p)}}\widetilde{\mathsf{S}}_\mathrm{err}=mF_\rho(p),\mathrm{Var}_{\Gamma^{(p)}}(\widetilde{\mathsf{S}}_\mathrm{err})=mF_\rho(p)(1-F_\rho(p)).\) (54)

Indeed, each local term is a projector with expectation \(F_\rho(p)\) by (26), and the covariances vanish.

For a fixed target tuple, abbreviate _Z=Z_**<sub>C</sub>**. The assumption on the zero syndrome and the nonzero amplitude at the zero error ensure _Z\>_0. Write

\(|\Gamma_\mathcal{S}^{(p)}\rangle=\sqrt{Z}|\Gamma^{(p)}\rangle+\sqrt{1-Z}|\eta\rangle,\langle\eta|\Gamma^{(p)}\rangle=0,\|\eta\|=1.\) (55)

The expectation on \(|\eta\rangle\) lies in \[0_,m_\]. Subtracting \(mF_\rho(p)I\) in the cross term and applying Cauchy- Schwarz therefore gives

\(ZF_\rho(p)-2\sqrt{\frac{Z(1-Z)F_\rho(p)(1-F_\rho(p))}{m}}\le\frac{1}{m}\left\langle\widetilde{\mathsf{S}}_\mathrm{err}\right\rangle_{\Gamma_\mathcal{S}^{(p)}}\le ZF_\rho(p)+1-Z+2\sqrt{\frac{Z(1-Z)F_\rho(p)(1-F_\rho(p))}{m}}.\) (56)

