_Proof._ As previously established (in the proof of Lemma 6), at levels \(h\ge t+1>t\), Case 1 and Case 4 nodes execute no moves (relevant to the run), and Case 3 nodes cannot exist. Thus, the moves at lower levels are purely from at most two Case 2 boundary nodes at each level.

By Fact 2, the maximum size of any node at level _h_ is \(\lceil n/2^h\rceil\). Consequently, the maximum number of run elements contained in a boundary node at level _h_ is at most \(\lceil n/2^h\rceil-1\le n/2^h\). Across both boundary nodes at level _h_, the total number of run elements charged is at most 2(_n/_2_<sup>h</sup>_). Applying the uniform accounting charge of 1.5 moves per element, the total charge at level _h_ is bounded by 3(_n/_2_<sup>h</sup>_). Summing this geometric series for all lower levels:

\(\sum_{h=t+1}^{lgn}3(n/2^h)\le 3\left(\frac{n/2^{t+1}}{1-1/2}\right)=6(n/2^{t+1})=3(n/2^t)\)

**Theorem 11** (Total Move Complexity)**.** _An array of size n containing r_<sub>#</sub> _pre-existing sorted runs is sorted in at most_ 1.5_nH_+5_n moves, where_ \(H=\sum_{i=1}^{r_\#}(r_i/n)lg\left(n/r_i\right)\) _is the run-based entropy._

_Proof._ Using the threshold \(t+1=\lceil lg(n/r)\rceil+1=lg(n/r)+\gamma+1\), we combine the upper (Lemma 9) and lower (Lemma 10) level costs for a single run of length _r_:

\(1.5r(t+1)+3(n/2^t)=1.5rlg(n/r)+r\left(1.5+1.5\gamma+3\left(2^{-\gamma}\right)\right)\) (2)

Rearranging the secant line bound on \(2^{-\gamma}\) for \(\gamma\in[0,1]\):

\(2^{-\gamma}\le 1-(1/2)\gamma\)<br>
\(3(2^{-\gamma})\le 3-1.5\gamma\)<br>
\(3(2^{-\gamma})+1.5\gamma\le 3\)

Substituting into (2), the moves made to process a run of length _r_ is given by:

\(1.5rlg(n/r)+r\left(1.5+1.5\gamma+3\left(2^{-\gamma}\right)\right)\le 1.5rlg(n/r)+4.5r\)

Summing this bound across all _r_<sub>#</sub> sorted runs (with lengths _r_<sub>1</sub>_,r_<sub>2</sub>_,...,r_<sub>_r_<sub>#</sub></sub> where \(\sum r_i=n\)):

\(\sum_{i=1}^{r_\#}\left(1.5r_ilg(n/r_i)+4.5r_i\right)=1.5n\left(\sum_{i=1}^{r_\#}(r_i/n)lg(n/r_i)\right)+4.5n=1.5nH+4.5n\)

Lastly, we reintegrate the (_n_-1)/2 overhead moves isolated from the initial merge cost:

\(1.5nH+4.5n+(n-1)/2\le 1.5nH+5n\)

## 3.3 Summary

**Corollary 12** (Overall Complexity)**.** _Directional mergesort sorts an array of size n with run-based entropy H using no more than nH_+3_n comparisons and_ 1.5_nH_+5_n element moves. Excluding the merge buffer of size_ \(\lceil n/2\rceil\)_, the algorithm uses O_(lg_n_) _auxiliary words._

_Proof._ Comparison and move bounds follow immediately from Theorem 8 and Theorem 11. The _O_(lg_n_) auxiliary words accounts for the recursive call stack, which is bounded by the merging tree’s height of \(\lceil lgn\rceil\) due to the balanced binary splitting logic of the algorithm.

**Remark 13** (Scope of Run Entropy)**.** The run-based entropy \(H=\sum(r_i/n)lg(n/r_i)\) in Corollary 12 is defined exclusively over non-decreasing pre-existing runs. If the input contains strictly decreasing runs, they are treated as individual runs of length 1.

