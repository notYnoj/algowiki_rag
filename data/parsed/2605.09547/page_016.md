**Algorithm 1** Interior Point Method, Algorithm 1 in \[BLL<sup>+</sup>21\]

procedure IPM(A, x<sup>(init)</sup>, s<sup>(init)</sup>, \(\tau^{(\mathrm{init})}\), l, u, \(\mu\), \(\mu^{(\mathrm{final})}\))<br>
   Fix \(\tau(x):=w(\phi''(x)^{-\frac{1}{2}})\), as defined in Definition 4.3.<br>
   Define \(\alpha=\frac{1}{4\mathrm{log}(4m/n)}\), \(\epsilon=\frac{\alpha}{C}\), \(\lambda=\frac{C\mathrm{log}(Cm/\epsilon^2)}{\epsilon}\) , \(\gamma=\frac{\epsilon}{C\lambda}\), \(r=\frac{\epsilon\gamma(1-p)}{C\sqrt{n}}=\frac{\epsilon^2\gamma}{\sqrt{n}}\).<br>
   \(t\leftarrow 1\), \(x^t\leftarrow x^{(\mathrm{init})}\), \(s^t\leftarrow s^{(\mathrm{init})}\), \(\tau^t\leftarrow\tau^{(\mathrm{init})}\), \(\mu^t\leftarrow\mu\)<br>
   while \(\mu^t>\mu^{(\mathrm{final})}\) do<br>
   \(\mu^{t+1}\leftarrow(1-r)\mu^t\)<br>
   \((x^{t+1},s^{t+1},\tau^{t+1})\leftarrow\mathrm{ShortStep}(x^t,s^t,\tau^t,\mu^t,\mu^{t+1})\)<br>
   \(t\leftarrow t+1\)<br>
   end while<br>
   return (x<sup>t</sup>,s<sup>t</sup>)<br>
end procedure<br>
procedure ShortStep(x, s, \(\tau\), \(\mu\), \(\mu^{(\mathrm{new})}\))<br>
   Find \(\overline{\tau}\) such that \(\overline{\tau}\approx_\epsilon\tau(x)\)<br>
   Let \(v=\frac{s+\mu\tau(x)\phi^\prime(x)}{\mu\tau(x)\sqrt{\phi^{\prime\prime}(x)}}\) and let \(\|\overline{v}-v\|_\infty\le\gamma/20\).<br>
   Let \(g=-\gamma\nabla\Psi(\overline{v})^{\unknown(\overline{\tau})}\) where<br>
\(\nabla\Psi(\overline{v})^{\unknown(\overline{\tau})}:=\mathrm{argmax}_{\|h\|_{\tau+\infty}=1}h^\top\nabla\Psi(\overline{v})\)<br>
where \(\Psi(\overline{v})=\sum_{i=1}^m\mathrm{cosh}(\lambda\overline{v})\)<br>
   Let \(\mathbf{H}^t\approx_\gamma=\mathbf{A}^\top\overline{\mathbf{T}^{-1}}\Phi''(x)^{-1}\mathbf{A}\)<br>
   Let \(\delta_y^t:=\mathbf{H}^{-1}\mathbf{A}^\top\Phi''(x)^{-\frac{1}{2}}g\), \(\delta_c^t:=\mathbf{H}^{-1}(\mathbf{A}^\top x-b)\)<br>
   \(\delta_x^t\leftarrow\Phi''(x)^{-\frac{1}{2}}g-\overline{\mathbf{T}^{-1}}\Phi''(x)^{-1}\mathbf{A}(\delta_y^{t+1}+\delta_c^{t+1})\)<br>
   \(\delta_s^t\leftarrow\mu\mathbf{A}\delta_y^{t+1}\)<br>
   \(x^t\leftarrow x+\delta_x^t\) and \(s^t\leftarrow s+\delta_s^t\).<br>
   return \((x^t,s^t,\tau^t)\).<br>
end procedure

**Definition 4.4** (\(\epsilon\)-centered point)**.** _We say that_ \((x,s,\mu)\in\mathbb{R}^m\times\mathbb{R}^m\times\mathbb{R}_{>0}^m\) _is_ \(\epsilon\)_-centered for_ \(\epsilon\in(0,1/80]\) _if the following properties hold, where C_<sub>norm</sub>=_C_(1_/p_) _for a constant_ \(C\ge 100\).

1. _(Approximate centrality)_ \(\left\|\frac{s+\mu\tau(x)\phi^\prime(x)}{\mu\tau(x)\sqrt{\phi^{\prime\prime}(x)}}\right\|_\infty\le\epsilon\).<tbc>

2. _(Dual Feasibility) There exists a vector_ \(z\in\mathbb{R}^n\) _with_ **A**_z+s=c._<tbc>

_3. (Approximate Feasibility)_ \(\|\mathbf{A}^\top x-b\|_{\mathbf{A}^\top(\mathbf{T}(x)\Phi^{\prime\prime}(x))^{-1}}\le\epsilon\gamma/C_\mathrm{norm}\).

The following potential is used to guarantee \(\epsilon\)-centrality. The interior point method essentially performs a gradient descent w.r.t. this potential.

**Definition 4.5** (Centrality Potential)**.** _We track the following centrality potential._

\(\Psi(x,s,\mu):=\sum_{i=1}^m\psi\left(\frac{s_e+\mu\tau(x)_e\phi'_e(x_e)}{\mu\tau(x)_e\sqrt{\phi''_e(x_e)}}\right)\)

_for_ \(\psi(x):=\mathrm{cosh}(\lambda x)\)_, where_ \(\lambda=\Theta(\mathrm{log}(m)/\epsilon)\) _(see Algorithm 1 for exact definition of_ \(\lambda\)_)._

The interior point method sometimes measures the length of vectors in a mixed norm, defines as

**Definition 4.6** (\[BLL<sup>+</sup>21, Definition 4.9\])**.** _For a vector_ \(v\in\mathbb{R}^m,\tau\in\mathbb{R}_{\ge 0}^m\)_, we define_

\(\|v\|_{\tau+\infty}:=\|v\|_\infty+C\mathrm{log}(4m/n)\cdot\|v\|_\tau\)

_where_ \(\|v\|_\tau=\sqrt{\sum_i\tau_i\cdot v_i^2}\) _and C is some large constant._

