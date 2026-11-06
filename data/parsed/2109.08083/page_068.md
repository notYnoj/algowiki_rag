<tbc>If \(E_{v,S}^+(i)\ge-b^{1/3}|E_\mathcal{T}(v,S)|\) then \(\mathbb{E}'(\Delta E_{v,S}^+(i))\le 0\). If \(V_S^+(i)\ge-b^{1/3}|S|\) then \(\mathbb{E}'(\Delta V_S^+(i))\le 0\). If \(Z_\mathcal{A}^+(i)\ge-b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|\) then \(\mathbb{E}'(\Delta Z_\mathcal{A}^+(i))\le 0\). _Submartingale conditions:_ If \(Q^-(i)\le bn^2\) then \(\mathbb{E}'(\Delta Q^-(i))\ge 0\). If \(d_v^-(i)\le b^{2/3}n\) then \(\mathbb{E}'(\Delta d_v^-(i))\ge 0\). If \(E_{v,S}^-(i)\le b^{1/3}|E_\mathcal{T}(v,S)|\) then \(\mathbb{E}'(\Delta E_{v,S}^-(i))\ge 0\). If \(V_S^-(i)\le b^{1/3}|S|\) then \(\mathbb{E}'(\Delta V_S^-(i))\ge 0\). If \(Z_\mathcal{A}^-(i)\le b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|\) then \(\mathbb{E}'(\Delta Z_\mathcal{A}^-(i))\ge 0\).

**Boundedness hypotheses:**<br>
_Supermartingale conditions:_<br>
\(\Delta Q^+(i)^2np\mathrm{log}^2(n)<(bn^2)^2\).<br>
\(-\Theta_d<\Delta d_v^+(i)<\theta_d\) with \(\theta_d<\Theta_d/10\) and \(\theta_d\Theta_dn\mathrm{log}^2(n)<(b^{2/3}n)^2\).<br>
\(-\Theta_E<\Delta E_{v,S}^+(i)<\theta_E\) with \(\theta_E<\Theta_E/10\) and \(\theta_E\Theta_Enpl\mathrm{log}^2(n)<(b^{1/3}|E_\mathcal{T}(v,S)|)^2\).<br>
\(-\Theta_V<\Delta V_S^+(i)<\theta_V\) with \(\theta_V<\Theta_V/10\) and \(\theta_V\Theta_Vnp\mathrm{log}^2(n)<(b^{1/3}|S|)^2\).<br>
\(-\Theta_Z<\Delta Z_\mathcal{A}^+(i)<\theta_Z\) with \(\theta_Z<\Theta_Z/10\) and \(\theta_Z\Theta_Znp\mathrm{log}^2(n)<(b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|)^2\).<br>
_Submartingale conditions:_<br>
\(\Delta Q^-(i)^2np\mathrm{log}^2(n)<(bn^2)^2\).<br>
\(-\Theta_d<\Delta d_v^-(i)<\theta_d\) with \(\theta_d<\Theta_d/2\) and \(\theta_d\Theta_dn\mathrm{log}^2(n)<(b^{2/3}n)^2\).<br>
\(-\Theta_E<\Delta E_{v,S}^-(i)<\theta_E\) with \(\theta_E<\Theta_E/2\) and \(\theta_E\Theta_Enpl\mathrm{log}^2(n)<(b^{1/3}|E_\mathcal{T}(v,S)|)^2\).<br>
\(-\Theta_V<\Delta V_S^-(i)<\theta_V\) with \(\theta_V<\Theta/2_V\) and \(\theta_V\Theta_Vnp\mathrm{log}^2(n)<(b^{1/3}|S|)^2\).<br>
\(-\Theta_Z<\Delta Z_\mathcal{A}^-(i)<\theta_Z\) with \(\theta_Z<\Theta_Z/2\) and \(\theta_Z\Theta_Znp\mathrm{log}^2(n)<(b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|)^2\).

For the boundedness hypotheses, informally we want, for example, that

\(\Delta Q^-(i)^2np=o(f_q^2),\)

where we require the ‘little-o’ term sufficiently small for union bounding the polynomially many variables to be considered. The log<sup>2</sup>(_n_) factor suffices for this.

In order to verify the trend hypotheses we make use of Taylor’s Theorem.

Theorem 5.5 (Taylor’s Theorem). _Let_ \(f:\mathbb{R}\rightarrow\mathbb{R}\) _be twice differentiable on_ \[_a,b_\]_. Then there exists_ \(\tau\in[a,b]\) _such that_

\(f(b)-f(a)=f'(a)(b-a)+\frac{f''(\tau)}{2}(b-a)^2.\)

We use this with _a=t(i_) and _b=t(i_+1) so that \(b-a=\frac{1}{|V(0)|}\) and \((b-a)^2=\frac{1}{|V(0)|^2}\). In particular, considering \(\mathbb{E}'(\Delta d_v^-(i))\), by linearity of expectation we get that \(\mathbb{E}'(\Delta d_v^-(i))=\mathbb{E}'(\Delta d_v(i))-\mathbb{E}'(\Delta np(i)^3)+\mathbb{E}'(\Delta e_d(i))=\mathbb{E}'(\Delta d_v(i))-n(p(i+\)

