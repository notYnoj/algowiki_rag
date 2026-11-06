<tbc>Solving this we get<tbc>

\(\mathbb{E}[r']\le\frac{r}{1-\frac{m}{k}}.\)

<tbc>Also,

\(\mathbb{E}[(r')^2]\le r^2+\mathbb{P}[\text{restart}]\mathbb{E}[(r+r')^2]\)<br>
\(\le r^2+\frac{m}{k}(r^2+2r\mathbb{E}[r']+\mathbb{E}[(r')^2])\)<br>
\(\le r^2+\frac{m}{k}\cdot r^2+\frac{m}{k}\cdot\frac{2r^2}{1-\frac{m}{k}}+\frac{m}{k}\cdot\mathbb{E}[(r')^2].\)

Solving this we get<tbc>

\(\mathbb{E}[(r')^2]\le(1-\frac{m}{k})^{-1}(r^2+\frac{m}{k}\cdot r^2+\frac{m}{k}\cdot\frac{2r^2}{1-\frac{m}{k}}).\)

<tbc>Choosing _k=m_log_m_, we have 1/(1-_m/k_)=1+_o<sub>m</sub>_(1), so we get

\(P_e(\mathcal{B})\le(1+o_m(1))\delta,\)<br>
\(\mathbb{E}[\rho]\le(1+o_m(1))m,\)<br>
\(\mathbb{E}[\rho^2]\le O(m^2\mathrm{log}^2m)=O(m^3),\)<br>
\(\mathbb{E}[r']\le(1+o_m(1))r,\)<br>
\(\mathbb{E}[(r')^2]\le O(r^2).\)

Using Lemma 18, we are able to construct "safe" (i.e., with guaranteed tail behavior) versions of algorithms introduced before.

**Corollary 19** (Safe Algorithms)**.**

1. _Given_ \(\delta\in(0,1)\)_, there exists a randomized algorithm_ SafeBinarySearch _for_ NoisyBinarySearch(_n), with error probability_ \(\le\delta\)_, with the number of queries_ \(\tau\) _satisfying_<tbc>

<tbc>\(\mathbb{E}[\tau]=(1+o(1))\left(\frac{\mathrm{log}n+O(\mathrm{log}\frac{1}{\delta})}{I(p)}\right),\mathrm{Var}[\tau]=O(\mathrm{log}^3n+\mathrm{log}^3\frac{1}{\delta}).\)<tbc>

<tbc>_and with the number of used random bits r satisfying_<tbc>

<tbc>\(\mathbb{E}[r]=O(\mathrm{log}n),\mathrm{Var}[r]=O(\mathrm{log}^2n).\)<tbc>

_2._ _Given_ \(\delta\in(0,1)\)_, there exists a deterministic algorithm_ SafeLessThan _which compares two elements with error probability_ \(\le\delta\)_, with the number of queries_ \(\tau\) _satisfying_<tbc>

<tbc>\(\mathbb{E}[\tau]=(1+o_{1/\delta}(1))\frac{\mathrm{log}\frac{1}{\delta}}{(1-2p)\mathrm{log}\frac{1-p}{p}},\mathrm{Var}[\tau]=O(\mathrm{log}^3\frac{1}{\delta}).\)<tbc>

