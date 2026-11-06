## 2.1 A tail-integral identity

The starting point is an identity that rewrites a clipped value in terms of tail events. For _L\>_0, define

\([w]_L:=\left\{\begin{array}{ c c }
-L, & w<-L, \\
w, & -L\le w\le L, \\
L, & w>L.
\end{array}\right.\)

The point of clipping is that it separates the estimation problem into two parts: a bounded quantity, which can be estimated reliably, and a bias term, which we will control using the variance bound.

**Lemma 2** (Tail-integral identity)**.** _For every_ \(w\in\mathbb{R}\) _and every L\>_0,

\([w]_L=\int_0^L\left(\mathbf{1}\{w\ge t\}-\mathbf{1}\{w\le-t\}\right)dt.\)

_Consequently,_ \(\mathbb{E}[[W]_L]=\int_0^L\left(Pr(W\ge t)-Pr(W\le-t)\right)dt\).

This identity is the bridge between mean estimation and 1-bit queries. It says that the clipped-variable mean can be written as an integral of differences between upper-tail and lower-tail probabilities. Since each of those probabilities can be accessed through a threshold comparison, the identity suggests that we should estimate the integral by randomizing the threshold _t_ and asking only a single yes/no question per sample. The proof is given in Appendix B.1.

## 2.2 A 1-bit randomized estimator

To turn the tail-integral identity into an estimator, we need a distribution over _t_. For \(L\ge\sigma\), define

\(\alpha_L:=1+log\frac{L}{\sigma},g_L(t):=\frac{1}{\alpha_Lmax\{\sigma,t\}},t\in[0,L].\)

Then _g<sub>L</sub>_ is a density on \[0_,L_\], since \(\int_0^Lg_L(t)dt=\alpha_L^{-1}\left(\int_0^\sigma dt/\sigma+\int_\sigma^Ldt/t\right)=1\).

The shape of _g<sub>L</sub>_ is important. It places relatively more mass on small thresholds _t_, where the query is informative, while still assigning enough mass to larger thresholds to represent the integral up to _L_.

### Randomized query and estimator.

Draw \(S\in\{+1,-1\}\) uniformly, independently of everything else, and draw _T∼g<sub>L</sub>_. Given a fresh reward sample _X_, issue the 1-bit query<tbc>

\(Y=\mathbf{1}\{S(X-c)\ge T\}.\)

<tbc>Equivalently, when _S_=+1 we ask whether \(X\ge c+T\), and when _S_=-1 we ask whether \(X\le c-T\). We then define

\(Z:=\frac{2S}{g_L(T)}Y.\)

The next lemma summarizes why this construction works.

**Lemma 3** (Unbiasedness, variance, and range)**.** _For every_ \(L\ge\sigma\):

_(i)_ \(\mathbb{E}[Z]=\mathbb{E}[[W]_L]\), _(ii)_ \(Var(Z)\le 3\alpha_L\sigma^2\)_, (iii)_ \(|Z|\le 2\alpha_LL\) _almost surely._

Each part of the lemma has a different role. The first part shows that _Z_ is exactly unbiased for the clipped-variable mean. The second part gives a variance bound of the correct scale, up to the logarithmic factor \(\alpha_L\). The third part provides an almost-sure range bound. Together, the second and third parts are precisely what is needed to apply Bernstein’s inequality; the proof is given in Appendix B.2.

Of course, _Z_ is unbiased only for the clipped-variable mean E\[\[_W_\]_<sub>L</sub>_\], not for E\[_W_\] itself. The next lemma quantifies the price paid for clipping.

**Lemma 4** (Clipping bias)**.** _For every_ \(L\ge\sigma\),

\(\left|\mathbb{E}[W]-\mathbb{E}[[W]_L]\right|\le\frac{\sigma^2}{2L}.\)

This bound has the expected form: increasing the clipping level _L_ reduces the bias, but making _L_ too large will worsen the variance bound \(3\alpha_L\sigma^2\) as well as the range bound \(2\alpha_LL\). The estimator therefore has a standard bias-variance tradeoff, and the choice of _L_ needs to balance the two effects. The bias proof is given in Appendix B.3.

