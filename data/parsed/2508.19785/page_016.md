<tbc>Proof. Consider a generic step performed during the walk on _T_<sup>∗</sup> from a vertex _v_. If _v_ is a good vertex, then exactly one child _u_ of _v_ in _T_<sup>∗</sup> is good (notice that _v_ cannot be a leaf). By Lemma 4.3, the test on _u_ succeeds with probability at least \(\frac{48}{50}\). Moreover, there can be at most one other child \(w\neq u\) of _v_ in _T_<sup>∗</sup>. If _w_ exists, then it must be bad and, by Lemma 4.4, the test on _w_ fails with probability at least \(\frac{49}{50}\). By using the union bound on the complementary probabilities, we have that process walks from _v_ to _u_ with probability at least \(\frac{47}{50}\).

If _v_ is a bad vertex, then all of its children are also bad. Since _v_ has at most 2 children and, by Lemma 4.4, a test on a bad vertex fails with probability at least \(\frac{49}{50}\), we have that all the tests fail with probability at least \(\frac{48}{50}\). In this case, the process walks from _v_ to the parent of _v_ (notice that, since _v_ is bad, it cannot be the root of _T_<sup>∗</sup>). □

As a consequence of our choice for the group size, no two tests will ever compare _x_ with the same element from _S_, as the following lemma shows.

Lemma 4.7. _During the random walk on T<sub>j</sub>, element x is compared to each element in S at most once._

Proof. During the random walk, each pointer moves from its initial position by at most \(k\rho\) positions (since each of the at most \(\rho\) steps of the random walk either does not affect the pointer or it increases/decreases the pointer by _k_). However, the initial distance between any two distinct pointers is more than \(2k\rho\), indeed:

\(cd-2d-1\ge(c-3)d=(250k-3)d>240kd=2k\cdot 120d\ge 2k\cdot 120\lceil lnm\rceil=2k\rho,\)

where we used the fact that _d_ is an integer with \(d\ge lnm\), which implies \(d\ge\lceil lnm\rceil\). The claim follows by observing that _x_ is only compared to the elements in _S_ via test operations. □

The following lemmas show that the walk on _T_<sup>∗</sup> is likely to return a good vertex, while the walk on \(T'\neq T^*\) is likely to either timeout or to return a non-bad (good or neutral) vertex, i.e., a vertex whose corresponding interval contains positions that are close to the true rank of _x_ in _S_.

Lemma 4.8. _The walk on T_<sup>∗</sup> _timeouts with probability at most m_<sup>-6</sup>.

Proof. For \(t=1,\dots,\rho\), let _X<sub>t</sub>_ be an indicator random variable that is equal to 1 iff the _t_-th step of the walk on _T_<sup>∗</sup> is improving. If the _t_-th step is not performed then let _X<sub>t</sub>_=1.

Notice that if, at any time \(t'\) during the walk, the number \(X^{(t^\prime)}=\sum_{t=1}^{t^\prime} X_t\) of improving steps exceeds the number of non-improving steps by at least \(h+\eta\), then the success condition is met. This means that a necessary condition for the walk to timeout is \(X^{(\rho)}-(\rho-X^{(\rho)})<h+\eta\), which is equivalent to \(X^{(\rho)}<\frac{h+\eta+\rho}{2}\) .

By Lemma 4.7 and by Lemma 4.6, we know that each _X<sub>t</sub>_s corresponding to a performed step satisfies \(P(X_t=1)\ge\frac{9}{10}\), regardless of whether the other steps are improving. We can therefore consider the following experiment: at every time step \(t=1,\dots,\rho\), we flip a coin that lands on heads with probability \(q=\frac{9}{10}\), we let _Y<sub>t</sub>_=1 if this happens, and _Y<sub>t</sub>_=0 otherwise. Defining \(Y^{(\rho)}=\sum_{t=1}^\rho Y_t\), we have that the probability of having \(X^{(\rho)}<\frac{h+\eta+\rho}{2}\) is at most the probability of having \(Y^{(\rho)}<\frac{h+\eta+\rho}{2}\) . Since \(h<logm<2lnm\), we have \(h+\eta<2+4\lceil log_7m\rceil+2lnm\le 8\lceil lnm\rceil<\frac{\rho}{10}\),<tbc>

