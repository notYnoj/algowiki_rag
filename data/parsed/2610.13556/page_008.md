<tbc>_Proof._ At equal chromatic numbers the palette correction is zero, and the maximum defining _T<sub>k</sub>_ already contains the zero transfer. Thus _T<sub>k</sub>_=0 is equivalent to (4.6). The sufficient condition follows from (4.4). For unequal chromatic numbers, subtract the two intrinsic weak-villainy values from (4.3). □

These criteria use local profile radii and remain valid for every graph pair. The correction \(\Gamma_k(G,H)\) is kept signed; the argument does not require an assumption about how the feasible- source maximum changes when additional colors are made available.

## 4.2. Repeated copies and the fixing number.

The unrestricted maximum _F<sub>k</sub>(G_) may be attained by a word whose profile is not feasible. Taking several copies of the graph permits such a word to be balanced across the palette. This gives an exact relation between weak villainy and the fixing number.

**Theorem 4.5.** _Fix an integer_ \(k\ge max\{1,\chi(G)\}\)_, and write m=qk+r, where_ \(q\ge 0\) _and_ \(0\le r<k\)_. Then_<tbc>

\(0\le mF_k(G)-\beta_k(mG)\le r\big(F_k(G)-\beta_k(G)\big).\) (4.8)

<tbc>_In particular,_<tbc>

\(\beta_k(mG)=mF_k(G)\text{\textit{whenever}}k|m,\) (4.9)

<tbc>_and_

\(lim_{m\rightarrow\infty}\frac{\beta_k(mG)}{m}=F_k(G).\) (4.10)

_Proof._ Every source on _mG_ can be weakly repaired one copy at a time, each at cost at most _F<sub>k</sub>(G_). This proves the upper bound \(\beta_k(mG)\le mF_k(G)\).

Let _w_ be a word on _G_ at distance _F<sub>k</sub>(G_) from P_<sub>k</sub>(G_), and let \(\pi\) be a cyclic permutation of all _k_ color labels. On _k_ copies of _G_, use the sources

\(w,\pi\circ w,\dots,\pi^{k-1}\circ w.\)

If _G_ has _n_ vertices, their total profile is (_n,...,n_): the _k_ copies of every vertex receive every label once. This profile is feasible. Indeed, starting with any proper [_k_]-coloring _y_ of _G_, its _k_ cyclic relabelings give a proper coloring of _kG_ with the same total profile. Relabeling preserves distances to the proper-coloring set, so each of the _k_ sources still requires _F<sub>k</sub>(G_) changes in a weak repair. The repairs on distinct copies are independent. Thus this admitted source on _kG_ requires exactly _kF<sub>k</sub>(G_) changes.

Repeating the construction gives _qk_ copies with cost _qkF<sub>k</sub>(G_). On each of the remaining _r_ copies, use a feasible source attaining \(\beta_k(G)\). The resulting total profile is feasible, since every block and each remaining copy has a feasible profile. Its weak repair cost is

\(qkF_k(G)+r\beta_k(G).\)

Combining this lower bound with the upper bound proves (4.8). The exact formula when _r_=0 follows immediately, and the error in (4.8) is bounded independently of _m_, proving (4.10). □

When \(k=\chi(G)\), the common-palette quantities in this theorem are the intrinsic weak-villainy values.

The error in equation (4.8) eventually repeats. The following result gives an explicit stabilization bound and identifies its least period from the repetitions attaining the fixing- number bound.

**Theorem 4.6** (Effective weak repetition)**.** _Let G have n vertices and let_ \(k\ge max\{2,\chi(G)\}\)_. Put_<tbc>

\(F=F_k(G),\varepsilon=F-\beta_k(G),M=\big(2(k-1)n+1\big)^{k-1},N=(k-1)M.\)

<tbc>_Define_<tbc>

\(h=gcd\{\ell\ge 1:\beta_k(\ell G)=\ell F\}.\)

<tbc>_Then h|k, and there are integers c_<sub>0</sub>_,...,c_<sub>_h_-1</sub> _such that_

\(c_0=0,1\le c_r\le r\varepsilon(1\le r<h),\beta_k(mG)=mF-c_{modh}(m\ge N).\)

