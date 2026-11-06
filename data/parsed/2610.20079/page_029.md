**Lemma C.1** (Interchange for arbitrary field widths and prefix counts)**.** Keep the fixed parameters of Lemma 6.3. For arbitrary positive integers \(P,G,\ell,e\), consider the lexicographically stored bit array with addresses<tbc>

\((p,H,g,D,z)\in[P]\times[q^e]\times[G]\times[q^e]\times[\ell].\)

<tbc>The permutation \((p,H,g,D,z)\mapsto(p,D,g,H,z)\) on its \(V=PG\ell q^{2e}\) bits can be performed in

\(Q(e,V)=O\big(1+\frac{V}{Bw}[1+(e/t_0)^\gamma]\big)\) (21)

block transfers. The padding required by recursion less than doubles the volume of each call, and the memory and polynomial disk-space guarantees are preserved.

_Proof._ Calls fitting in memory or having width \(e\le t\) are still handled directly. For other calls, put _x=e/t_<sub>0</sub> and \(k=\lceil log_mx\rceil\). The required depth is at most _k_, so we want the prefix count to be a multiple of _W<sup>k</sup>_. Taking \(\rho\) high-order digits from each field gives \(q^{2\rho}\) prefixes. Choose the smallest integer making \(q^{2\rho}\ge W^k\), namely \(\rho=\lceil klogW/(2logq)\rceil\).

First handle fields too short to supply these digits. If \(\rho\ge e\), then \(x\le e\le\rho=O(1+logx)\), forcing _x_ to be bounded by a fixed constant. Split the fields into _O_(1) pairs of width at most _t_<sub>0</sub> and apply base interchanges, without adding prefixes.

If \(\rho<e\), write _H_=(_H_<sub>+</sub>_,H_<sub>-</sub>) and _D_=(_D_<sub>+</sub>_,D_<sub>-</sub>), with both high-order parts of width \(\rho\) and both low-order parts of width \(h=e-\rho\). The exact address layouts, including the unchanged outer prefix, intervening coordinate, and suffix, are

\((p,H_+,H_-,g,D_+,D_-,z)\mapsto^E(p,D_+,H_+,H_-,g,D_-,z)\mapsto^L(p,D_+,H_+,D_-,g,H_-,z)\mapsto^F(p,D_+,D_-,g,H_+,H_-,z).\) (22)

Here _E_ extracts _D_<sub>+</sub> to just after _p_, _L_ exchanges the two low fields while fixing (_p,D_<sub>+</sub>_,H_<sub>+</sub>), and _F_ moves _H_<sub>+</sub> to just before _H_<sub>-</sub>. Thus _FLE_ is precisely the required interchange; _g_ and _z_ retain their values and final positions. Figure 5 suppresses _p,z_ in these four layouts.

## Extracting and restoring the high digits.

Moving a single base-_q_ digit across any intervening coordinates costs _O_(1+_V/(Bw_)) transfers. Distribute bits into _q_ streams according to that digit, preserving the order of all remaining coordinates. Enumerate the target addresses and read from<tbc>

Original
H+
H-
g
D+
D-
Extract high
D+
H+
H-
g
D-
q2p segments
Swap low
D+
H+
D-
g
H-
Restore high
D+
D-
g
H+
H-

Figure 5: The two high-order parts form the segment index (dashed box). The middle interchange fixes that index and swaps only the low-order parts. \(g\in[G]\) is the original intervening coordinate.

