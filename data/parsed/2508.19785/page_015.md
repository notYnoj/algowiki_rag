<tbc>and _s_<sub>_R(u_)+_i_</sub> reports _x_ as the smaller element). Let \(X=\sum_{i=0}^{k-1}X_i\) and \(Y=\sum_{i=0}^{k-1}Y_i\) and notice that for a test to fail at least one of \(X>\frac{k}{2}\) and \(Y>\frac{k}{2}\) must hold.

Consider the comparison between _x_ and _s_<sub>_L(u_)-_i_</sub> for some _i_=0_,...,k_-1. Since \(i^*\in I(u)\) and the pointer _L(u_) only gets decremented, we have \(L(u)-i\le L(u)\le\mathrm{min}I(u)-d-1\le i^*-d-1\). This, combined with the fact that _S_ has dislocation at most _d_, implies \(\mathrm{rank}(s_{L(u)-i},S)\le L(u)-i+d\le i^*-1\) and hence _s_<sub>_L(v_)-_i_</sub>_\<x_.

We conclude that the probability to observe _S_<sub>_L(v_)-_i_</sub>_\<x_ is at least 1-_p_, and _X_ stochastically dominates a binomial random variable \(X'\) of parameters _k_ and 1-_p_. Thus, we can use a Chernoff bound to write:

\(\mathrm{Pr}\left(X\le\frac{k}{2}\right)\le\mathrm{Pr}\left(X'\le\left(1-\frac{1-2p}{2-2p}\right)\cdot\mathbb{E}[X']\right)\le\mathrm{exp}\left(-\frac{1}{2}\cdot\left(\frac{1-2p}{2-2p}\right)^2\cdot k(1-p)\right)\)<br>
\(\le e^{-4}<\frac{1}{50}.\)

A similar argument shows that \(\mathrm{Pr}(Y\le\frac{k}{2})<\frac{1}{50}\) once we observe that \(R(u)+i\ge\mathrm{max}I(u)+d\ge i^*+d\), which implies \(\mathrm{rank}(s_{R(u)+i},S)\ge i^*\) and hence _s_<sub>_R(u_)+_i_</sub>_\>x_. The claim follows by using the union bound on the events \(X\le\frac{k}{2}\) and \(Y\le\frac{k}{2}\). □

Lemma 4.4. _Consider a test performed on a bad vertex u. The probability that u passes the test is at most_ \(\frac{1}{50}\).

Proof. Since _u_ is a bad vertex, either _i_<sup>∗</sup>_\<_min_I(u_)-_cd_ or _i_<sup>∗</sup>_\>_max_I(u_)-_cd_. We consider the first case, as the second one is symmetric.

Let _X<sub>i</sub>_ be an indicator random variable that is 1 iff the comparison between _x_ and _s_<sub>_L(u_)-_i_</sub> reports _x_ as the smaller element and define \(X=\sum_{i=0}^{k-i}X_i\). A necessary condition for the test to succeed is \(X\le\frac{k}{2}\).

Focus on the comparison between _x_ and _s_<sub>_L(u_)-_i_</sub> for some _i_=0_,...,k_-1 and notice that, before the considered test is performed, the pointer _L(u_) must have been decremented (by _k_) at most \(\rho-1\) times. Using \(k\rho=120k\lceil\mathrm{ln}m\rceil<(c-2)\lceil\mathrm{ln}m\rceil\le(c-2)d\), we can write:

\(L(u)-i\ge\mathrm{min}I(u)-d-1-k(\rho-1)-i\ge\mathrm{min}I(u)-d-k\rho>i^*+cd-d-(c-2)d=i^*+d.\)

Since _S_ has dislocation at most _d_, this implies \(\mathrm{rank}(s_{L(u)-i},S)\ge L(u)-i-d>i^*\). Therefore, _s_<sub>_L(u_)-_i_</sub>_\>x_ and _s_<sub>_L(u_)</sub>_\>x_ is observed with probability at least 1-_p_. Hence, _X_ stochastically dominates a binomial random variable \(X'\) of parameters _k_ and 1-_p_, and we can use a Chernoff bound to write:

\(\mathrm{Pr}\left(X\le\frac{k}{2}\right)\le\mathrm{Pr}\left(X\le\left(1-\frac{1-2p}{2-2p}\right)\mathbb{E}[X']\right)\le\mathrm{exp}\left(-\frac{1}{2}\cdot\left(\frac{1-2p}{2-2p}\right)^2\cdot kp\right)\le e^{-4}<\frac{1}{50}.\) □

_Definition 4.5._ A step on _T<sub>j</sub>_ from vertex _v_ to vertex _u_ is called _improving_ if either of the following two conditions holds:

\(\bullet\) _u_ is a good vertex and _h(u)\>h(v_), implying that _v_ is also good; or<tbc>

\(\bullet\) _v_ is a bad vertex and _h(u)\<h(v_).

Intuitively, each improving step is making progress towards identifying the interval containing the true rank _i_<sup>∗</sup> of _x_, while each non-improving step undoes the progress of at most one improving step.

Lemma 4.6. _Each step performed during the walk on T_<sup>∗</sup> _is improving with probability at least_ \(\frac{9}{10}\).

