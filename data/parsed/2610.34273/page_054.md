vertex. Enumerate the _R_ labelings and, on each leg, map the basis vector belonging to the _h_-th labeling to \(e_h^{(R)}\) for \(0\le h\le R-1\), while sending unused coordinates to zero. These local maps send _T<sub>g</sub>_ to l_<sub>k</sub>(R_). We have proved the degeneration \(\mathsf{l}_k(R)\triangle\mathsf{GT}_q(G)\).

For clarity, we finish by converting this degeneration into a bound on ordinary asymptotic subrank. Fix _q_ and the preceding degeneration. The interpolation argument in Lemma 2.17 supplies a nonnegative integer _b_, independent of _N_, such that<tbc>

\(\mathsf{l}_k(R^N)\unknown\mathsf{GT}_q(G)^{\otimes_KN}\otimes_K\mathsf{l}_k(bN+1)(N\ge 1).\)

<tbc>Let \(t_N=\lceil log_q(bN+1)\rceil\). Lemma B.3, applied to _t<sub>N</sub>_ copies and followed by coordinate projection, gives

\(\mathsf{l}_k(bN+1)\unknown\mathsf{l}_k(q^{t_N})\unknown\mathsf{GT}_q(G)^{\otimes_KT_N}.\)

The same statement holds for _t<sub>N</sub>_=0 by the conventions for zeroth powers. Combining the two restrictions gives \(\mathsf{Q}(\mathsf{GT}_q(G)^{\otimes_K(N+t_N)})\ge R^N\).

Now choose _q_=2_<sup>s</sup>_ for a positive integer _s_. By Lemma 2.21, GT_<sub>q</sub>(G_) is isomorphic to \(\mathsf{GT}_2(G)^{\otimes_Ks}\). Since _t<sub>N</sub>=O_(log_N_) for fixed _q_, taking _s(N+t<sub>N</sub>_)-th roots in the preceding inequality and letting \(N\rightarrow\infty\) gives \(\widetilde{\mathsf{Q}}(\mathsf{GT}_2(G))\ge R^{1/s}\ge 2^\ell C^{-1/s}\). Finally, _C_ does not depend on _s_. Letting \(s\rightarrow\infty\) proves \(\widetilde{\mathsf{Q}}(\mathsf{GT}_2(G))\ge 2^\ell\), which matches the upper bound.

