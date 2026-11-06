## B.3 Probability of a bad path

_Proof of Theorem 6._ If _h\<g<sub>G</sub>_, every nonbacktracking walk of _h_ edges is a simple path: a first repeated vertex would yield a cycle of length at most _h_. There are at most 2_m(D_-1)<sup>_h_-1</sup> oriented such paths, because the first edge has 2_m_ orientations and each subsequent step has at most _D_-1 choices.

For a fixed path, let _X_ count its erroneous positions. Under independent symbol errors, _X_ has the Bin(_h,p_) distribution. For _p\<_1/2, Markov’s inequality with _s_=(1-_p)/p\>_1 yields

\(Pr\{X\ge h/2\}\le s^{-h/2}(1-p+ps)^h=\left[2\sqrt{p(1-p)}\right]^h.\) (215)

Lemma 12 and a union bound prove (83). This argument bounds an event depending only on the support, so it permits arbitrary nonzero values at corrupted positions.

For the fixed-weight assertion, put \(\rho=t/m\). If _t_=0 the LP has the zero word as its unique optimal marginal vector. Otherwise, for a uniformly chosen _t_-subset of edges and \(s\ge 1\), expansion of _s<sup>X</sup>_ gives

\(\unknown s^X=\sum_{j=0}^h\genfrac(){pt}{2}{h}{j}(s-1)^j\frac{(t)_j}{(m)_j}\le(1-\rho+\rho s)^h.\) (216)

Here \((a)_j=a(a-1)\cdots(a-j+1)\), with (_t)<sub>j</sub>_=0 for _j\>t_, and \((t)_j/(m)_j\le(t/m)^j\). Applying (215) with \(\rho\) in place of _p_ proves the same bound because \(\rho\le p<1/2\) and \(2\sqrt{p(1-p)}\) is increasing on \[0,1/2\].

For independent noise at any fixed positive rate in Corollary 2, the error weight is _pm+o(m_) with probability tending to one. The fixed-weight version proves the linear-error statement without using this concentration step. Neither version gives correction of all adversarial supports of linear size.

### Recovery after a one-coordinate change.

Changing one coordinate can increase the number of corrupted positions on a simple path by at most one. Hence, if every simple path of _h\<g<sub>G</sub>_ edges contains fewer than _h/_2-1 corrupted positions, then every word at Hamming distance at most one from the error satisfies the hypotheses of Lemma 12. Each such word is therefore uniquely LP-recoverable from its own syndrome. With _s_=(1-_p)/p_, the tail estimate (215) becomes

\(Pr\{X\ge h/2-1\}\le s^{1-h/2}(1-p+ps)^h=\frac{1-p}{p}\left[2\sqrt{p(1-p)}\right]^h.\) (217)

For a uniformly chosen support of size \(t\le pm\), use (216) with the same _s_ and \(t/m\le p\). A union bound proves (84) in both cases. The bound is uniform over all nonzero values, including replacements introduced by the one-coordinate change.

## B.4 An equivalent LP with polynomial dependence on the degree

The recovery proof is complete. We now establish the stronger size bound stated in §3.3. A check involving \(d_v\ge 1\) symbols has exactly _q_<sup>_d<sub>v</sub>_-1</sup> satisfying assignments: the first _d<sub>v</sub>_-1 symbol values can be chosen freely, and the check uniquely determines the last value because its coefficient is nonzero. After omitting empty checks, the direct LP therefore has

\(mq+\sum_{v:d_v>0}q^{d_v-1}\le mq+nq^{D-1}\) (218)

