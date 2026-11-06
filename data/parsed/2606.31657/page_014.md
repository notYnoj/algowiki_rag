We can also combine the two kinds of permutations. For any \(\pi\in\mathrm{perm}([k])\) and \(\tau\in\mathrm{perm}(\Sigma)^k\), we define \(\{\nu_m^{\pi,\tau}\}\) by<tbc>

\(\nu_m^{\pi,\tau}(m'):=\nu_{\tau(\pi(m))}(\tau(\pi(m'))).\)

<tbc>Since both \(\pi\) and \(\tau\) are bijections that preserve the Hamming distance, we have<tbc>

\(L\left(\{\nu_m^{\pi,\tau}\}\right)=L\left(\{\nu_m\}\right).\)

<tbc>We define \(\{\nu_m^*\}\) as the mixture of all \(\{\nu_m^{\pi,\tau}\}\):<tbc>

\(\nu_m^*(m'):=\frac{1}{(|\Sigma|!)^kk!}\sum_{\tau\in\mathrm{perm}(\Sigma)^k}\sum_{\pi\in\mathrm{perm}([k])}\nu_m^{\pi,\tau}(m').\)

<tbc>The mixture \(\{\nu_m^*\}\) is in \(\mathcal{D}_\varepsilon\) by Lemma 3.5. Note that _L_ is convex since \(\mathsf{TV}(\cdot,\cdot)\) is convex. Thus we have<tbc>

\(L\left(\{\nu_m^*\}\right)\le\frac{1}{(|\Sigma|!)^kk!}\sum_{\tau\in\mathrm{perm}(\Sigma)^k}\sum_{\pi\in\mathrm{perm}([k])}L\left(\{\nu_m^{\pi,\tau}\}\right)=L\left(\{\nu_m\}\right).\)

<tbc>So \(\{\nu_m^*\}\) is also a minimizer of _L_. We may fix two different characters \(a_0,a_1\in\Sigma\), and define \(\bar{m}=(a_0,\dots,a_0)\). For any \(m,m'\in\Sigma^k\), we can choose \(\pi^*\in\mathrm{perm}([k])\) such that \(\pi^*(m)\) and \(\pi^*(m')\) are different at exactly the first \(d_\mathrm{H}(m,m')\) coordinates, and \(\tau^*\in\mathrm{perm}(\Sigma)^k\) such that<tbc>

\(\forall 1\le i\le k:\tau_i^*(\pi^*(m)_i)=a_0,\tau_i^*(\pi^*(m')_i)=\left\{\begin{array}{ c c }
a_1, & 1\le i\le d_\mathrm{H}(m,m') \\
a_0, & d_\mathrm{H}(m,m')<i\le k
\end{array}\right..\)

<tbc>Then we have

\(\nu_m^*(m')=\frac{1}{(|\Sigma|!)^kk!}\sum_{\tau\in\mathrm{perm}(\Sigma)^k}\sum_{\pi\in\mathrm{perm}([k])}\nu_m^{\pi,\tau}(m')\)<br>
\(=\frac{1}{(|\Sigma|!)^kk!}\sum_{\tau\in\mathrm{perm}(\Sigma)^k}\sum_{\pi\in\mathrm{perm}([k])}\nu_{\tau^*(\pi^*(m))}^{\pi,\tau}(\tau^*(\pi^*(m')))\)<br>
\(=\nu_{\tau^*(\pi^*(m))}^*(\tau^*(\pi^*(m')))\)<br>
\(=\nu_\bar{m}^*\left(\underbrace{(a_1,\dots,a_1,}_{d_\mathrm{H}(m,m^\prime)},\underbrace{a_0,\dots,a_0}_{k-d_\mathrm{H}(m,m^\prime)}\right).\)

Thus \(\nu_m^*\) is symmetric in the sense that for any \(m,m'\in\Sigma^k\), \(\nu_m^*(m')\) only depends on \(\delta_\mathrm{H}(m,m')\). That is, there is a function \(g:\{0,1,\dots,k\}\rightarrow[0,1]\) such that<tbc>

\(\nu_m^*(m')=g\left(d_\mathrm{H}(m,m')\right).\)

<tbc>Now we can lower bound \(L\left(\{\nu_m^*\}\right)\). Since \(\{\nu_m^*\}\) is the distribution constructed from the output of a \((1-\varepsilon)\)-approximation algorithm A by definition, we have

\(\mathbb{E}\left[\delta_\mathrm{H}(\sigma(\tilde{\mathcal{A}}(\mathcal{I}_C(m))),m)\right]\le\frac{\varepsilon}{\kappa}\)

by Lemma 3.4.

