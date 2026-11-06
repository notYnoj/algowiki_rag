• _Let_ \(r'\) _be the number of random bits algorithm_ B _uses. Then_

\(\mathbb{E}[r']\le(1+o_m(1))r,\)<br>
\(\mathbb{E}[(r')^2]=O(r^2).\)

_Proof._ Let _k_ be a parameter to be chosen later. Consider the following algorithm B:

1. Run algorithm A until it halts, or it is about to use the (_k_+1)-th query.<tbc>

2. If A halts, then we return the return value of A; otherwise, we restart the whole algorithm.

Let us compute the probability of a restart. By Markov’s inequality,<tbc>

<tbc>\(\mathbb{P}[\text{restart}]=\mathbb{E}[\tau>k]\le\frac{m}{k}.\)<tbc>

<tbc>Algorithm B’s error probability _P<sub>e</sub>_(B) is<tbc>

<tbc>\(P_e(\mathcal{B})=\mathbb{P}[\mathcal{A}\text{errs}|\tau\le k]\le\frac{\mathbb{P}[\mathcal{A}\text{errs}]}{\mathbb{P}[\tau\le k]}\le\frac{\delta}{1-\frac{m}{k}}.\)<tbc>

<tbc>The expected number of queries \(\rho\) used by Algorithm _B_ satisfies

\(\mathbb{E}[\rho]=\mathbb{E}[\tau\wedge k]+\mathbb{P}[\text{restart}]\mathbb{E}[\rho]\)<br>
\(\le m+\frac{m}{k}\mathbb{E}[\rho].\)

Solving this, we get<tbc>

<tbc>\(\mathbb{E}[\rho]\le\frac{m}{1-\frac{m}{k}}.\)<tbc>

<tbc>The second moment satisfies

\(\mathbb{E}[\rho^2]\le\mathbb{E}[(\tau\wedge k)^2]+\mathbb{P}[\text{restart}]\mathbb{E}[(k+\rho)^2]\)<br>
\(\le k^2+\frac{m}{k}\cdot(\mathbb{E}[\rho^2]+2k\mathbb{E}[\rho]+k^2)\)<br>
\(\le k^2+mk+\frac{2m^2}{1-\frac{m}{k}}+\frac{m}{k}\cdot\mathbb{E}[\rho^2].\)

Solving this, we get<tbc>

<tbc>\(\mathbb{E}[\rho^2]\le\left(1-\frac{m}{k}\right)^{-1}\left(k^2+mk+\frac{2m^2}{1-\frac{m}{k}}\right).\)<tbc>

<tbc>Similar to \(\rho\), we have

\(\mathbb{E}[r']\le r+\mathbb{P}[\text{restart}]\mathbb{E}[r']\)<br>
\(\le r+\frac{m}{k}\cdot\mathbb{E}[r'].\)

