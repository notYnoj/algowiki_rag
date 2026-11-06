<tbc>to the oracle, so in total this takes time:

\(\mathrm{poly}(n)\cdot M^{\varepsilon/\mathrm{log}n}\le\mathrm{poly}(n)\cdot 2^{(2\kappa n\mathrm{log}n)\cdot\varepsilon/\mathrm{log}n}\)<br>
\(\le\mathrm{poly}(n)\cdot 2^{\delta_H\cdot n/2}\)<br>
\(\le\mathcal{O}(2^{\delta_H\cdot n}).\)

So in total, the reduction works in \(\mathcal{O}(2^{\delta_H\cdot n})\) time. Finally, recall that Algorithm 2 returns a non-zero vector \(\mathbf{v}\in\mathcal{L}\) such that \(\|\mathbf{v}\|\le N^5\cdot\lambda_n(\mathcal{L})=n^{10}\lambda_n(\mathcal{L})\). This contradicts the initial assumption that no algorithm finds such a vector **v** in time \(\mathcal{O}(2^{\delta_H\cdot n})\).

We conclude the proof of Theorem 1.2 by showing that a different tradeoff yields a \(2^{\Omega(n/\mathrm{log}n)}\) lower bound.

**Lemma 5.2.2.** _Under Hypothesis 1, there exists_ \(\varepsilon>0\) _such that there does not exist an algorithm that is given a set_ \(S\subseteq\{1,\dots,2^{N-1}\}\) _of size N, with probability \>_3/4 _finds two different_ \(A,B\subseteq S\) _and runs in time_ \(\mathcal{O}(2^{\varepsilon N/\mathrm{log}N})\).

_Proof._ Set _c_=6 and similarly, to the proof of Lemma 5.2.1, this gives us parameters \(\delta_H,\kappa\). Based on that, we select \(N=4\kappa n\mathrm{log}n\) and similarly we select _B,W_ and _M_. As before, we know that \(M\le 2^{2\kappa n\mathrm{log}n}<2^{N-1}\) so the pigeonhole condition holds.

Analogously to the proof of Lemma 5.2.1 the running time of Algorithm 2 is \(\mathcal{O}(2^{\delta_Hn/2})\), except for all the calls to the PESS oracle, which if we set \(\varepsilon:=\delta_H/(4\kappa)\) take in total time:

\(\mathrm{poly}(n)\cdot 2^{\varepsilon N/\mathrm{log}N}\le\mathrm{poly}(n)\cdot 2^{\varepsilon\cdot 4\kappa n\mathrm{log}n/(\mathrm{log}(4\kappa n\mathrm{log}n))}\)<br>
\(\le\mathrm{poly}(n)\cdot 2^{\varepsilon\cdot 4\kappa n\mathrm{log}n/(2\mathrm{log}n)}\)<br>
\(\le\mathrm{poly}(n)\cdot 2^{2\varepsilon\kappa n}\)<br>
\(\le\mathrm{poly}(n)\cdot 2^{\delta_H\cdot n/2}\)<br>
\(\le 2^{\delta_H\cdot n}.\)

So in total, the reduction works in \(\mathcal{O}(2^{\delta_H\cdot n})\) time. Finally, recall that Algorithm 2 returns a non-zero vector \(\mathbf{v}\in\mathcal{L}\) such that \(\|\mathbf{v}\|\le N^5\cdot\lambda_n(\mathcal{L})=\mathcal{O}(n\mathrm{log}n)^5\lambda_n(\mathcal{L})\le n^6\cdot\lambda_n(\mathcal{L})\) because _n_ is large enough. This contradicts the initial assumption that no algorithm can find such a vector **v** in time \(\mathcal{O}(2^{\delta_H\cdot n})\).

## 6 Modular average-case: Proof of Theorem 1.4

### Notations.

For an _n_ dimension vector **v** where _n_ is even, **v**<sup>(_L_)</sup> and **v**<sup>(_R_)</sup> denote the first _n/_2 and the last _n/_2 elements of the vector. Z_<sub>M</sub>_ denotes the ring of integers modulo _M_.

In this section, we conclude the proof of Theorem 1.4. Firstly, recall the definition of the **ACM- RESS** problem.

### Average-Case Modular Restricted Equal Subset Sum (ACM-RESS).

Given a modulus _M_ and an integer _n_ divisible by 4 as input, such that _M_ has the following structure

1. _M=pqr_, where _p_, _q_, and _r_ are pairwise co-prime integers,<tbc>

2. \(M=\Theta(2^n)\), and \(p,q\in\Theta(M^{1/4})\). <sup>14</sup><tbc>

<sup>14</sup>As mentioned in the introduction, the average-case algorithms work even for \(M\le\mathrm{poly}(n)\cdot 2^n\), the trade-off is the success probability of the algorithm. We need to optimize the integers _p_ and _q_ for an optimal success probability. But for simplicity of the presentation, we present an algorithm for \(M=\Theta(2^n)\).

