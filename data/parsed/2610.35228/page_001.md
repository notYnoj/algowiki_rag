# Improved Quasi-Polynomial-Time Approximation for Maximum Independent Set

Zhao Song<sup>∗</sup>

October 25, 2026

**Abstract**

We give a deterministic quasi-polynomial-time algorithm for the maximum independent set problem. If an _N_-vertex graph contains an independent set of size 2<sup>-_t_</sup>_N_, where _t_ is an integer with \(1\le t\le\sqrt{logN}/12\), then our algorithm finds an independent set of size 2_<sup>t</sup>_ in time _N_<sup>_O(t_)</sup>. This gives an approximation ratio of \(N/2^{\Omega(\sqrt{logN})}\) in time \(N^{O(\sqrt{logN})}\), improving on the approximation ratio \(N/2^{\Omega((logN)^{1/3})}\) obtained by Lovett [Lov26].

A limitation of this form of analysis follows from the integrality gaps of Tulsiani [Tul09]. These gaps imply that a universal guarantee of the form \(\mathrm{Las}_{R(t)}(G)\ge 2^{-t}N\Longrightarrow\alpha(G)\ge 2^t\), at \(2^{o(\sqrt{logNloglogN})}\) levels, cannot hold over a range extending beyond \(t=O(\sqrt{logNloglogN})\). Thus, the exponent 1/2 is the limit of this form of analysis, up to a factor of \(\sqrt{loglogN}\).

<sup>∗</sup>`magic.linuxkde@gmail.com`.

