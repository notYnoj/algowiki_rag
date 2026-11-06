**Theorem 27** (Comparison Complexity of Simple Adaptive Mergesort)**.** _An array of size n containing r_<sub>#</sub> _non-decreasing runs of lengths r_<sub>1</sub>_,r_<sub>2</sub>_,...,r_<sub>_r_<sub>#</sub></sub> _is sorted by Simple Adaptive Mergesort using at most nH_+4_n comparisons, where_ \(H=\sum_{i=1}^{r_\#}(r_i/n)lg(n/r_i)\).

_Proof._ Combining upper and lower level comparison charges for a run of length _r_ yields:<tbc>

\(r(t+1)+2(n/2^t)\)

<tbc>Letting \(\gamma=\lceil lg(n/r)\rceil-lg(n/r)\in[0,1)\), we rewrite this bound as:<tbc>

\(r\left(lg(n/r)+\gamma+1\right)+2\left(r/2^\gamma\right)=rlg(n/r)+r\left(1+\gamma+2\left(2^{-\gamma}\right)\right)\)

<tbc>Applying the secant line bound to the convex expression \(2^{-\gamma}\) for \(\gamma\in[0,1]\):

\(2^{-\gamma}\le 1-(1/2)\gamma\)<br>
\(2(2^{-\gamma})\le 2-\gamma\)<br>
\(2(2^{-\gamma})+\gamma\le 2\)

Thus, the total comparison charge per run is at most _r_lg(_n/r_)+3_r_. Summing across all _r_<sub>#</sub> runs:

\(\sum_{i=1}^{r_\#}\left(r_ilg(n/r_i)+3r_i\right)=nH+3n\)

Finally, reintroducing the _n_-1 skip check comparisons gives:

\(nH+3n+(n-1)\le nH+4n\)

## B.2 Data Movement Complexity

**Corollary 28** (Move Complexity of Simple Adaptive Mergesort)**.** _An array of size n containing r_<sub>#</sub> _non-decreasing runs of lengths r_<sub>1</sub>_,r_<sub>2</sub>_,...,r_<sub>_r_<sub>#</sub></sub> _is sorted by Simple Adaptive Mergesort using at most_ 1.5_nH_+5_n moves, where_ \(H=\sum_{i=1}^{r_\#}(r_i/n)lg(n/r_i)\).

_Proof._ As Theorem 11 already utilizes an amortized accounting scheme that charges a flat 1.5 moves per element oblivious to potential localized directional merging savings, the bound established in Theorem 11 holds for the simplified version.

