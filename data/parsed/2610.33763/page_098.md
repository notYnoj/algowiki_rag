**Theorem 7.1** _\[66\] There exist continuous_ \(2\pi\)_-periodic functions_ \(g_{\eta_1}\) _and_ \(g_{\eta_2}\) _such that_

\(\{B_{n_1}^x\}_{n_1}\sim_{\mathrm{GLT},\sigma} g_{\eta_1}(\theta_1),\theta_1\in[-\pi,\pi],\)<br>
\(\{B_{n_2}^y\}_{n_2}\sim_{\mathrm{GLT},\sigma} g_{\eta_2}(\theta_2),\theta_2\in[-\pi,\pi].\)

_Moreover,_

\(\{B_{n_1}^x\}_{n_1}\sim_\lambda\delta_0,\)<br>
\(\{B_{n_2}^y\}_{n_2}\sim_\lambda\sigma_0.\)

**Theorem 7.2** _\[66\] There exists a continuous_ \(2\pi\)_-periodic function_ \(h_\xi\) _such that_

\(\{U_m\}_m\sim_{\mathrm{GLT},\sigma} h_\xi(\theta),\theta\in[-\pi,\pi].\)

_Moreover,_

\(\{U_m\}_m\sim_\lambda\gamma_0.\)

**Corollary 7.1** _If_ \(a:[0,1]^2\rightarrow\mathbb{R}\) _is continuous a.e. and if_

\(\frac{\alpha_m}{\beta_{n_1}}\rightarrow\nu_1,\frac{\alpha_m}{\beta_{n_2}}\rightarrow\nu_2,\text{\textit{as}}m,n_1,n_2\rightarrow\infty,\)

_with_ \(\nu_1\neq 0\) _or_ \(\nu_2\neq 0\)_. Then, we have_

\(\{G_\mathbf{n}\}_\mathbf{n}\sim_{\mathrm{GLT},\sigma} a(x,y)\left(\nu_1g_{\eta_1}(\theta_1)+\nu_2g_{\eta_2}(\theta_2)\right),(x,y)\in[0,1]^2,(\theta_1,\theta_2)\in[-\pi,\pi]^2,\)

_with_ \(g_{\eta_1}\) _and_ \(g_{\eta_2}\) _as in Theorem 7.1. Moreover,_

\(\{G_\mathbf{n}\}_\mathbf{n}\sim_\lambda a(x,y)\left(\delta_0+\sigma_0\right),(x,y)\in[0,1]^2.\)

**Proof:** From the definition in (7.17), we have<tbc>

\(G_\mathbf{n}:=D_\mathbf{n}(a)\left(B_\mathbf{n}^x+B_\mathbf{n}^y\right).\)

<tbc>Thus, by GLT 2, we deduce that<tbc>

\(\{D_\mathbf{n}(a)\}_\mathbf{n}\sim_\mathrm{GLT}a(x,y),(x,y)\in[0,1]^2.\)

<tbc>Then, using (7.14) and assuming \(\frac{\alpha_m}{\beta_{n_1}}\rightarrow\nu_1\), by GLT 2, and GLT 7, we obtain<tbc>

\(\{B_\mathbf{n}^x\}_\mathbf{n}=\left\{I_{n_2}\otimes\frac{\alpha_m}{\beta_{n_1}}B_{n_1}^x\right\}_\mathbf{n}=\left\{T_{n_2}(1)\otimes\frac{\alpha_m}{\beta_{n_1}}T_{n_1(g_{\eta_1})}\right\}_\mathbf{n}\sim_\mathrm{GLT}\nu_1g_{\eta_1}(\theta_1).\)

<tbc>Similarly, using (7.15) and assuming \(\frac{\alpha_m}{\beta_{n_2}}\rightarrow\nu_2\), by GLT 2, and GLT 7, we obtain<tbc>

\(\{B_\mathbf{n}^y\}_\mathbf{n}=\left\{\frac{\alpha_m}{\beta_{n_2}}B_{n_2}^y\otimes I_{n_1}\right\}_\mathbf{n}=\left\{\frac{\alpha_m}{\beta_{n_2}}T_{n_2(g_{\eta_2})}\otimes T_{n_1}(1)\right\}_\mathbf{n}\sim_\mathrm{GLT}\nu_2g_{\eta_2}(\theta_2).\)

<tbc>Invoking the ∗-algebra properties detailed in GLT 3, we obtain that<tbc>

\(\{B_\mathbf{n}^x+B_\mathbf{n}^y\}_\mathbf{n}\sim_\mathrm{GLT}\nu_1g_{\eta_1}(\theta_1)+\nu_2g_{\eta_2}(\theta_2),(\theta_1,\theta_2)\in[-\pi,\pi]^2.\)

