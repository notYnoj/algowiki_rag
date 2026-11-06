## A Detailed Procedures and Proofs for Representatives Structure

Recall that there are _r<sub>#</sub>_ segment representatives out of which _s<sub>#</sub>_ are active, distributed among \(s'_\#\) gaps \(L_1\dots L_{s^\prime_\#}\), each a contiguous block of 8 representatives. Additionally, we also have the rebuild buffer _D_ that is large enough to hold all active representatives. Our objective is to support _R_.search(_x_) and _R_.insert(_x_) efficiently.

### A.1 Search

The operation _R_.search(_x_) finds the active representative \(R'_z\) such that \(f'_z\le x<f'_{z+1}\), and is implemented as two binary searches:

**1.** By an outer binary search in \(L_1\dots L_{s^\prime_\#}\), locate the last gap _Li_ whose first active representative \(\ell_1\) satisfies \(\ell_1\le x\).

**2.** By an inner binary search over \(Li_i=\ell_1\dots\ell_8\), find the first representative _l<sub>j</sub>_ that is either an active representative _\>x_ or a buffer representative (if no such active representative exists). The gap invariant guarantees such a segment representative exists (as a buffer representative must exist in the gap).

**3.** If _i_=1 and _j_=1, then _x\<f_<sub>1</sub>, thus _x_ belongs in _S_<sub>0</sub>; return 0. Otherwise, the correct active representative is \(\ell_{j-1}\), or _R<sub>y</sub>_ where _y_=8(_i_-1)+(_j_-1) in the global sequence _R_; return _y_.

Let the resulting active representative from _R_.search(_x_) be \(R'_z\). We show that \(f'_z\le x<f'_{z+1}\). By the outer binary search, _x_ lies between the first active representatives of _Li_ and _Li_+1. By the inner binary search, \(\ell_j\) is either the first active representative _\>x_ or the first buffer representative in _Li_. Therefore, \(\ell_{j-1}\) is the last active representative \(\le x\). The next active representative is either \(\ell_j\) which is _\>x_ by the inner binary search or the first representative of _Li_+1 which is also _\>x_ by the outer binary search. Thus, the inequality \(f'_z\le x<f'_{z+1}\) holds.

The outer binary search requires \(lgs'_\#\) comparisons exactly as \(s'_\#\) is a power of 2. The inner binary search requires exactly lg8=3 iterations as 8 is a power of 2. Naively, for each iteration, 2 comparisons are required to first determine if \(\ell_j\) is a buffer representative, then optionally an additional comparison against _x_ for active representatives. However, as buffer elements are greater than all active elements (see Section 3), a single comparison \(\ell_j>x\) suffices. Lastly, the edge case check and position calculation requires _O_(1) arithmetic operations.

\(\blacktriangleright\) **Lemma A.1.** _R.search(x_) _requires_ \(lgs'_\#+3=\lfloor lgs_\#\rfloor+3\) _comparisons._

### A.2 Insertion

The procedure for _R_.insert(_x_) is as follows:

**1.** Run _y=R_.search(_x_) to find the representative \(\ell_j\) from _Li_ (\(i=\lceil y/8\rceil\), _j=y_-8(_i_-1)), then increment _j_ giving position where _x_ should be inserted.

**2.** By a binary search in _Li_ find the last active representative _a<sub>k</sub>_ to determine the value of _k_, i.e. the number of active representatives in _Li_.

**3.** Iterating through \(j'=k\dots j\) (descending order), we swap every \(\ell_{j^\prime}\) with \(\ell_{j^\prime+1}\). This shifts the active representatives initially at \(\ell_j\dots\ell_k\) one unit rightwards into the positions \(\ell_{j+1}\dots\ell_{k+1}\), and \(\ell_j\) now contains the representative initially at \(\ell_{k+1}\), which is a buffer representative (as \(\ell_k\) is defined as the last active representative).

**4.** Construct the new active representative in \(\ell_j\), promoting _x_ to the frame.

