the stream selected by the target digit. Within each selected stream, the remaining coordinates occur in the same lexicographic order before and after the move; every stream is therefore read sequentially. The operation needs _q_ stream buffers and one output buffer, and its partial-block overhead is _O(q_)=_O_(1). It applies even when the crossed coordinate has arbitrary cardinality _G_. Applying it one digit at a time implements both _E_ and _F_ in \(O(\rho)\) scans, preserving the order within _D_<sub>+</sub> and _H_<sub>+</sub>. These are digit moves, so no unproved unequal-width interchange is being used.

## Padding the extracted prefix.

After _E_, encode the adjacent high fields by<tbc>

\(s=q^\rho D_++H_+\in[R],R=q^{2\rho}\ge W^k.\)

<tbc>The layout is now (_p,s,H_<sub>-</sub>_,g,D_<sub>-</sub>_,z_). For every _p_, append zero segments with \(s\in[R,R')\), where

\(R'=W^k\lceil R/W^k\rceil<2R.\)

Each segment has exactly \(q^{2h}G\ell\) bits. This defines a rectangular padded array of volume \(V'=(R'/R)V<2V\) , whose prefix coordinate (_p,s_) has \(PR'\) values. Inserting all the padding together requires one scan of this array; it does not incur a separate block-transfer startup cost for every _p_.

It remains to fit the width to the recursive scales. Divide it by the base width _t_<sub>0</sub> and expand the quotient in radix _m_:<tbc>

\(e-\rho=t_0\nu+r,0\le r<t_0,\nu=\sum_{j=0}^ka_jm^j,0\le a_j<m.\)

<tbc>Use this expansion to partition both low fields into corresponding contiguous chunks with identical widths: _a<sub>j</sub>_ chunks of width _t_<sub>0</sub>_m<sup>j</sup>_ for each _j_, followed by a residual chunk of width _r_ if _r\>_0. Write these chunks as _H_<sub>-</sub>=(_A_<sub>1</sub>_,...,A<sub>d</sub>_) and _D_<sub>-</sub>=(_B_<sub>1</sub>_,...,B<sub>d</sub>_). The interchange of _A<sub>i</sub>_ and _B<sub>i</sub>_ is an allowed equal-width interchange: its intervening coordinate consists of the remaining _A_-chunks, _g_, and the preceding _B_-chunks. If _b<sub>i</sub>_ is the total width of the _A_-chunks preceding _A<sub>i</sub>_, its prefix-segment count is exactly<tbc>

\(PR'q^{b_i}.\)

<tbc>This is divisible by _W<sup>j</sup>_ whenever the selected chunk has width _t_<sub>0</sub>_m<sup>j</sup>_. Earlier swaps do not change any coordinate cardinality, so the condition holds for every call. Each swap fixes all other coordinate positions, including (_p,s_). Each swap acts on a different pair of coordinate positions; their composition maps<tbc>

\((p,s,A_1,\dots,A_d,g,B_1,\dots,B_d,z)\)<br>
\(\longmapsto(p,s,B_1,\dots,B_d,g,A_1,\dots,A_d,z).\)

<tbc>Consequently they implement _L_ exactly, for every \(P,G,\ell\), rather than only for adjacent fields or a particular gap shape. Lemma 6.3, applied to the entire padded array in each call, gives total scan factor

\(O\left(1+\sum_{j=0}^ka_jm^{j\tau}\right)=O(m^{k\tau})=O(x^\tau).\)

The residual pair requires at most one base interchange. Here _x\>_1, \(m^{k\tau}\le m^\tau x^\tau\), and \(\tau>0\); hence the \(O(\rho)=O(1+\mathrm{log}x)\) scans for _E,F_ are absorbed by \(O(1+x^\tau)\). We are outside the in-memory case, so _V/(Bw_) is bounded below by a positive constant and also absorbs each call’s additive startup cost.

