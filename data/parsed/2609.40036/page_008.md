The decoder acts on syndromes of \(C^\perp=\mathrm{ker}B^T\). We assume that \(D:\mathrm{im}B^T\rightarrow\mathbb{F}_q^m\) is deterministic and syndrome-consistent:<tbc>

\(B^TD(\mathbf{s})=\mathbf{s}\text{for all}\mathbf{s}\in\mathrm{im}B^T.\) (14)

<tbc>Computing the syndrome produces

\(\sum_\mathbf{y}\phi_\mathbf{C}(\mathbf{y})|\mathbf{y}\rangle|B^T\mathbf{y}\rangle.\) (15)

A reversible implementation of _D_ then subtracts _D(B<sup>T</sup>_**y**) from the error register. Postselecting this register on \(|\mathbf{0}\rangle\) retains exactly the decoder’s success set

\(\mathcal{S}:=\{\mathbf{y}:D(B^T\mathbf{y})=\mathbf{y}\},\mathcal{F}:=\mathbb{F}_q^m\backslash\mathcal{S}.\) (16)

Because _B<sup>T</sup>_ is injective on S, the resulting normalized syndrome state is

\(|\widetilde{P}_\mathcal{S}\rangle\propto\sum_{\mathbf{y}\in\mathcal{S}}\phi_\mathbf{C}(\mathbf{y})|B^T\mathbf{y}\rangle.\) (17)

The algorithm applies \((\mathsf{F}_q^\dagger)^{\otimes n}\) and measures in the computational basis to obtain an assignment **X**. All expected satisfaction fractions below are conditioned on successful postselection. The analysis applies to any implementation of the state preparation and reversible decoder described above.

For each target _C<sub>i</sub>_, put

\(\theta_i(a):=|\widetilde{g}_i(a)|^2=\frac{\left|\sum_{t\in C_i}\chi_q(at)\right|^2}{r(q-r)}.\) (18)

These probabilities satisfy \(\theta_i(a)=\theta_i(-a)\). Let _P<sub>k</sub>_ be the error distribution obtained by choosing _k_ coordinates uniformly and drawing their nonzero values independently from the corresponding \(\theta_i\). This is the DQI error distribution conditioned on weight _k_.

**Theorem 1** (Semicircle law for fixed targets)**.** _Let_ \(\ell\le m\) _be a positive integer, and let_ \(\varepsilon\in[0,1)\)_. Suppose that, for every_ \(0\le k\le\ell\),

\(\mathrm{Pr}_{\mathbf{Y}\sim P_k}\left[D(B^T\mathbf{Y}')=\mathbf{Y}'\text{\textit{for every}}\mathbf{Y}'\text{\textit{with}}|\mathbf{Y}-\mathbf{Y}'|\le 1\right]\ge 1-\varepsilon.\) (19)

_Let_ \(f_\ell^*\) _be the largest value of_ E\[_s_(**X**)_/m_| _successful postselection_\] _over all normalized shell-amplitude vectors_ **w**=(_w_<sub>0</sub>_,...,w<sub>m</sub>)<sup>T</sup> satisfying w<sub>k</sub>_=0 _for_ \(k>\ell\)_. Put_ \(\rho:=r/q\) _and_ \(p_\ell:=\mathrm{min}\{\ell/m,1-\rho\}\)_, and define_

\(F_\rho(p):=\left(\sqrt{\rho(1-p)}+\sqrt{(1-\rho)p}\right)^2.\) (20)

_Then_

\(f_\ell^*\ge(1-\varepsilon)\left(F_\rho(p_\ell)-\frac{1}{\sqrt{m}}\right)-\frac{\sqrt{(q-1)\rho(1-\rho)}\varepsilon}{1-\varepsilon},f_\ell^*\le(1-\varepsilon)F_\rho(p_\ell)+\varepsilon+\frac{\sqrt{(q-1)\rho(1-\rho)}\varepsilon}{1-\varepsilon}.\text{(21)}\)

_Every such normalized shell-amplitude vector has postselection probability at least_ \(1-\varepsilon\).

