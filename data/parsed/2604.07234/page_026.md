\(=\mathbb{E}\left[\unknown\left\{X'\text{is typical}\right\}\left(\sum_{S\in\genfrac(){pt}{2}{[N]}{M}:X^\prime|_S\notin\mathcal{G}(X^\prime)}\unknown\left\{X'|_S=Y\right\}\right)\unknown\left\{Y\notin\mathcal{G}(X')\right\}\right]\)<br>
\(=^{(\text{Fubini})}\mathbb{E}_{X^\prime}\left[\unknown\left\{X'\text{is typical}\right\}\cdot\mathbb{E}_Y\left[\sum_{S\in\genfrac(){pt}{2}{[N]}{M}:X^\prime|_S\notin\mathcal{G}(X^\prime)}\unknown\left\{X'|_S=Y\right\}\right]\right]\)<br>
\(=\mathbb{E}_{X^\prime}\left[\unknown\left\{X'\text{is typical}\right\}\cdot 2^{-M}\cdot\left|\left\{S\in\genfrac(){pt}{2}{[N]}{M}:X'|_S\notin\mathcal{G}(X')\right\}\right|\right]\)<br>
\(\le^{(\text{Proposition 3.8})}\mathbb{E}_{X^\prime}\left[\unknown\left\{X'\text{is typical}\right\}\cdot 2^{-M}\cdot\genfrac(){pt}{2}{N}{M}\cdot e^{-\Omega(N)}\right]\)<br>
\(\le\genfrac(){pt}{2}{N}{M}e^{-\Omega(N)}\cdot 2^{-M}=e^{N\left(f_\text{null}^\text{ann}(\alpha)-\Omega(1)\right)}.\)(3.33)

Markov’s inequality thus implies that (with a weaker universal constant implicit in the \(\Omega(\cdot)\) term than in the corresponding \(\Omega(\cdot)\) term in the final expression of (3.33))<tbc>

\(\mathbb{P}\left(Z_{X^\prime,Y}\cdot\unknown\{E_N\}<e^{N\left(f_\text{null}^\text{ann}(\alpha)-\Omega(1)\right)}\right)\ge 1-e^{-\Omega(N)}.\)

<tbc>The discussion after Definition 3.6 and (3.31) together imply \(\mathbb{P}(E_N)\ge 1-e^{-\Omega(N)}\), so we conclude that

(3.34) \(\mathbb{P}\left(Z_{X^\prime,Y}<e^{N\left(f_\text{null}^\text{ann}(\alpha)-\Omega(1)\right)}\right)\ge 1-e^{-\Omega(N)},\)

from which the weak law proves the strict inequality in (1.8). Furthermore, after shrinking implicit constants if necessary, we may take both \(\Omega(\cdot)\) terms in (3.34) to be governed by the same positive constant.

We complete the proof of Theorem 1.1 via proving the strict inequality of (1.6). In the rest of Section 3.4, we let all \(\Omega(\cdot)\) terms specifically denote the corresponding implicit constant as guaranteed in (3.34). We say that \(x\in\{0,1\}^N\) is _hoarded_ if

(3.35) \(\left|\mathcal{H}(x)\right|:=\left|\left\{y\in\{0,1\}^M:Z_{x,y}\ge e^{N\left(f_\text{null}^\text{ann}(\alpha)-\Omega(1)\right)}\right\}\right|\le 2^Me^{-\Omega(N)/2}.\)

It then follows that

\(e^{-\Omega(N)}\ge^{(\text{3.34})}\mathbb{P}\left(Z_{X^\prime,Y}\ge e^{N\left(f_\text{null}^\text{ann}(\alpha)-\Omega(1)\right)}\right)\)<br>
\(=\mathbb{P}\left(Z_{X^\prime,Y}\ge e^{N\left(f_\text{null}^\text{ann}(\alpha)-\Omega(1)\right)}|X'\text{hoarded}\right)\cdot\mathbb{P}\left(X'\text{hoarded}\right)\)<br>
\(+\mathbb{P}\left(Z_{X^\prime,Y}\ge e^{N\left(f_\text{null}^\text{ann}(\alpha)-\Omega(1)\right)}|X'\text{not hoarded}\right)\cdot\mathbb{P}\left(X'\text{not hoarded}\right)\)<br>
\(\ge^{(\text{3.35})}2^{-M}\cdot 2^Me^{-\Omega(N)/2}\cdot\mathbb{P}\left(X'\text{not hoarded}\right)=e^{-\Omega(N)/2}\cdot\mathbb{P}\left(X'\text{not hoarded}\right)\)

from which we conclude that

(3.36) \(\mathbb{P}\left(X'\text{not hoarded}\right)\le e^{-\Omega(N)/2}.\)

