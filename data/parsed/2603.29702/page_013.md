For LCS, a minimization problem, we can simply let our back-up estimate be 0 when the sub-paths differ a lot in lengths, since this is always sound. For ED, we can use an off-the-shelf constant-factor approximation (e.g., \[CDG<sup>+</sup>20, GRS20, AN20\]) to obtain a sound back-up estimate with a multiplicative error of _O_(1).

### Putting it all together

If we never misestimate by more than a multiplicative factor of \(\left(1+\frac{\varepsilon'}{|\widetilde{S}|}\right)\) for each interval (_l,r_\] on an active scale for some \(\varepsilon'=o(1)\), the total error over \(\widetilde{S}\) active layers is bounded by:

\(\left(1+\frac{\varepsilon'}{|\widetilde{S}|}\right)^{|\widetilde{S}|}\approx(1+\varepsilon'),\)

which gives us a (1+_o_(1))-approximation. In our final algorithms, for an interval (_l,r_\] on an active scale, we use a simple concentration inequality to show that, for any specific path _p_ and interval (_l,r_\], the probability of mestimating the answer by more than \(\left(1+\frac{\varepsilon'}{|\widetilde{S}|}\right)\) due to sub-sampling is roughly \(2^{-M\frac{(\varepsilon')^2}{|\widetilde{S}|^2}}\) . Suppose that

\(M\gg log^{\Omega(1)}(n)/(\varepsilon')^2.\)

Then the probability of a large misestimation is \(2^{-log^{\Omega(1)}(n)}\). Even when we largely misestimate, the estimate inside an interval (_l,r_\] should never exceed its width _r-l_. Thus intuitively, the total additive error is expected to be bounded by \(n/2^{-log^{\Omega(1)}(n)}\) (we will formally show this using an observation on a special type of layered graphs (Claim 6.13)), which suffices since we assume the answer is _n/_2log<sup>_O_(1)</sup>(_n_).

## 3 Preliminaries

### 3.1 Notations

For \(i\in\mathbb{N}\), let \[_i_\] denote the set {1,2_,...,i_}.

For \(r\in\mathbb{R}\), let \(sign(r):=\left\{\begin{array}{ c c }
-1, & \text{if}r\le 0 \\
+1, & \text{if}r>0
\end{array}\right.\) be the sign of _r_.

For a sequence _A_=(_a<sub>i</sub>_) of length _n_, we write \(\sum A\) to denote its sum \(\sum_{i=1}^na_i\).

### 3.2 Concentration Bound

As an ingredient for our analysis, we will use Hoeffding’s Inequality \[Hoe63\]:

**Lemma 3.1.** _Let X_=(_x_<sub>1</sub>_,...,x<sub>N</sub>_) _be N independent random variables in_ \[-_c,c_\]_. Then, for all_ \(\delta>0\),

\(\mathbf{Pr}\left(\left|\sum_{i=1}^Nx_i-\mu\right|\ge\delta\right)\le 2exp\left(-\frac{\delta^2}{2Nc^2}\right),\)

_where_ \(\mu=\mathbf{E}\left[\sum_{i=1}^Nx_i\right]\).

