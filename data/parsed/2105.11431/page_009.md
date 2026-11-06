<tbc>**Claim 4.6.** _Let_ \(R\subseteq[n]^2\) _be a random binomial subset where each position is present with probability_ \(p\in[0,1]\)_, independently of other positions. Let_ \((r,c),(x,y)\in[n]^2\) _be two positions that do not share a line. Then:_

\(\mathbb{P}[(x,y)\in\mathcal{S}_R(r,c)]\ge|\ell_1^{far}(r,y)||\ell_2^{far}(r,y)||\ell_1^{far}(x,c)||\ell_2^{far}(x,c)|p^5(1-p)^{20n}-O\left(\frac{1}{n^2}\right).\)

_Proof._ Instead of asking for the probability that \((x,y)\in\mathcal{S}_R(r,c)\), we will instead estimate the probabilities of the following events.

• Let _A_ be the event that \((x,y)\in R\) and no other position sharing a line with (_x,y_) is in _R_. Then<tbc>

<tbc>\(\mathbb{P}[A]=p(1-p)^{4n-1}\ge p(1-p)^{4n}.\)<tbc>

• Let _B_ be the event that there exist distinct positions \(a_1\in\ell_1^{far}(r,y),a_2\in\ell_2^{far}(r,y),b_1\in\ell_1^{far}(x,c),b_2\in\ell_2^{far}(x,c)\) such that \(a_1,a_2,b_1,b_4\in R\), and no line incident to any of these positions contains more than one element of _R_. Since every pair of lines intersects in at most one position, there are at least<tbc>

\(\left(|\ell_1^{far}(r,y)|-O(1)\right)\left(|\ell_2^{far}(r,y)|-O(1)\right)\left(|\ell_1^{far}(x,c)|-O(1)\right)\left(|\ell_2^{far}(x,c)|-O(1)\right)\)<br>
\(=|\ell_1^{far}(r,y)||\ell_2^{far}(r,y)||\ell_1^{far}(x,c)||\ell_2^{far}(x,c)|-O(n^3)\)

8
7
6
5
4
3
2
1
1
2
3
4
5
6
7
8

Figure 1. In the above partial 8-queens configuration, the black queen at (8,8) is a safe absorber for the square (5,4). The four white queens occupy the toroidal diagonals incident to (5,8) and (8,4), while the (non-toroidal) diagonals incident to those squares are unoccupied.

