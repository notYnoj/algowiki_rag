<tbc>Altogether, we have that, letting _X_ play the role of \(X'\) above when invoking (3.35) and (3.36) and recalling that \(\mathbb{P}(Y=y|X)=Z_{X,y}/\genfrac(){pt}{2}{N}{M}\) for each \(y\in\{0,1\}^M\),

\(\mathbb{P}\left(\frac{1}{N}logZ_{X,Y}>f_\mathrm{null}^\mathrm{ann}(\alpha)+\frac{\Omega(1)}{4}\right)\)<br>
\(\ge\mathbb{P}\left(X\text{hoarded}\right)\cdot\left[1-\mathbb{P}\left(\frac{1}{N}logZ_{X,Y}\le f_\mathrm{null}^\mathrm{ann}(\alpha)+\frac{\Omega(1)}{4}\big|X\text{hoarded}\right)\right]\)<br>
\(\ge^\text{(3.36)}\left(1-e^{-\Omega(N)/2}\right)\cdot\left[1-\mathbb{P}\left(Z_{X,Y}\le e^{N\left(f_\mathrm{null}^\mathrm{ann}(\alpha)+\Omega(1)/4\right)},Y\notin\mathcal{H}(X)\big|X\text{hoarded}\right)\right.\)<br>
\(\left.-\mathbb{P}\left(Z_{X,Y}\le e^{N\left(f_\mathrm{null}^\mathrm{ann}(\alpha)+\Omega(1)/4\right)},Y\in\mathcal{H}(X)\big|X\text{hoarded}\right)\right]\) (3.37)

\(\ge^\text{(3.35)}\left(1-e^{-\Omega(N)/2}\right)\cdot\left(1-\underbrace{2^M\cdot e^{N\left(f_\mathrm{null}^\mathrm{ann}(\alpha)-\Omega(1)\right)}\frac{1}{\genfrac(){pt}{2}{N}{M}}}_\text{bound on}-\underbrace{2^Me^{-\Omega(N)/2}\cdot e^{N\left(f_\mathrm{null}^\mathrm{ann}(\alpha)+\Omega(1)/4\right)}\frac{1}{\genfrac(){pt}{2}{N}{M}}}_\text{bound on}Y\in\mathcal{H}(X)\text{term}\right)\)<br>
\(=\left(1-e^{-\Omega(N)}\right)\cdot\left(1-e^{-\Omega(N)}e^{Nf_\mathrm{null}^\mathrm{ann}(\alpha)}\frac{2^M}{\genfrac(){pt}{2}{N}{M}}-e^{-\Omega(N)/4}e^{Nf_\mathrm{null}^\mathrm{ann}(\alpha)}\frac{2^M}{\genfrac(){pt}{2}{N}{M}}\right)\) (3.38)

\(=\left(1-e^{-\Omega(N)}\right)\cdot\left(1-e^{-\Omega(N)+o(N)}-e^{-\Omega(N)/4+o(N)}\right)\rightarrow 1.\)

We note that (3.37) specifically follows by, in each case, bounding the number of length-_M_ subsequences of _X_ that satisfy the conditions of the corresponding event and then multiplying by the probability \(\genfrac(){pt}{2}{N}{M}^{-1}\) of _Y_ being any particular such length-_M_ subsequence. We conclude in conjunction with the weak limit of (1.6) that \(f_\mathrm{pl}(\alpha)>f_\mathrm{null}^\mathrm{ann}(\alpha)\). This completes the proof of Theorem 1.1.

## 3.5. Consequences of Theorem 1.1.

We now turn to the consequences of Theorem 1.1 for uniformly random codes over the deletion channel.

### 3.5.1. _Positive rate for uniform codes under the deletion channel._

With Theorem 1.1 in hand, we now prove Corollary 1.2, settling \[PIW24, Conjecture 3\].

_Proof of Corollary 1.2._ The _p_=0 case follows directly from (1.2), so we are free to fix \(p\in(0,1)\). We set \(\alpha=1-p\). In particular, we recall from (1.2) that the largest rate achievable via uniform random codebooks admits the representation

(3.39) \(C_\mathrm{unif}(p)=\mathrm{lim}_{N\rightarrow\infty}\frac{1}{N}I\left(X;\mathsf{BDC}_p(X)\right)=^\text{(1.3)}\alpha log2-h(\alpha)+f_\mathrm{pl}(\alpha),\)

where the last equality follows since the normalized log-partition function \(\frac{1}{N}logZ_{X,Y}\) is uniformly bounded. Thus, for fixed \(\alpha\in(0,1)\), it holds that

(3.40) \(0<^\text{(1.6)}f_\mathrm{pl}(\alpha)-f_\mathrm{null}^\mathrm{ann}(\alpha)=f_\mathrm{pl}(\alpha)-\left(h(\alpha)-\alpha log2\right)=^\text{(3.39)}C_\mathrm{unif}(1-\alpha).\)

We conclude that \(d_\mathrm{unif}^*=1\), as desired. □

