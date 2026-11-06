## 6 Near-Optimal In-Place Sorting

**The rebuild buffer** _D_ is a contiguous block of fixed size \(\lfloor 2m/s\rfloor\) representatives. Typically, _D_ consists only of buffer representatives, but active representatives are temporarily stored in _D_ during rebalancing. By (2), |_D|\>s_<sub>#</sub>, so _D_ can hold every active representative.

This gives the total number of representatives

\(r_\#=|L|+|D|\le 8\lfloor 2m/s\rfloor+\lfloor 2m/s\rfloor=9\lfloor 2m/s\rfloor\) (5)

It follows that the required size of the frame memory, cache memory, and bit vector are respectively

\(|F|=r_\#\le 9\lfloor 2m/s\rfloor\le 9m/lg^4m,\) (6)

\(|G|=r_\#2g\approx 18m/lg^3m,\) (7)

\(|V|=r_\#\left(\lfloor lg\lfloor 2m/s\rfloor\rfloor+\lfloor lgg\rfloor+2\right)\approx 9m/lg^3m\le m/lg^2m,\) (8)

for sufficiently large _m_. From (3), (6), (7), the required size of the buffer memory is then

\(|B|=|F|+|G|+|S|\le 3m-1\) (9)

**The operation** _R._search(_x_) is implemented by two binary searches to locate the final active representative \(R_y\le x\). The outer search locates the last gap _L<sub>i</sub>_ among \(L_1\dots L_{s_\#^\prime}\) whose first representative \(\ell_1\le x\), leveraging the existence of an active representative at the front of every gap by the gap invariant to guarantee a contiguous, monotonic search space. The second binary search then locates the exact last representative \(\ell_j\le x\) within the isolated gap, returning its position. Because \(R'_z=R_y\) is the last active representative \(\le x\), the next active representative \(R'_{z+1}>x\). Thus, it obeys the ordering invariant \(f'_z\le x<f'_{z+1}\).

\(\blacktriangleright\) **Lemma 2.1.** _R.search(x_) _requires_ \(lgs'_\#+3=\lfloor lgs_\#\rfloor+3\) _comparisons._

**Proof.** The outer binary search costs \(lgs'_\#\) comparisons exactly since \(s'_\#\) is a power of 2. The inner search then requires lg8=3 comparisons. Summing gives \(\lfloor lgs_\#\rfloor+3\) comparisons. \(\blacktriangleleft\)

**The operation** _R._insert(_x_) is implemented by first locating the position where _x_ belongs by _R._search(_x_). Then, by a standard array-based linear shift within the gap implemented with exchanges, we shift a buffer representative from the back of the gap _x_ belongs in to the desired location, making room for _x_ to be constructed in its sorted position, maintaining the sorted order of active frame elements. To ensure that a buffer representative is always present at the end of the gap for future insertions, we verify if the gap invariant still holds, executing dynamic rebalancing to restore the invariant if it was violated by the insertion. Occasionally when \(s_\#=2s'_\#\) a resize exchanges all active representatives into _D_ and rebuilds the library structure with _s_<sub>#</sub> gaps each containing one active representative, updating \(s'_\#:=s_\#=2s'_\#\).

**Dynamic rebalancing** uses an imaginary segment tree over the gaps \(L_1\dots L_{s_\#^\prime}\) with nodes \(n_1\dots n_{2s_\#^\prime-1}\), where _n_<sub>1</sub> is the root node _covering_ all gaps, and leaves \(n_{s_\#^\prime}\dots n_{2s_\#^\prime-1}\) correspond with individual gaps. The nodes are indexed like a binary tree. For each node _n<sub>k</sub>_ covering the range _L<sub>l</sub>...L<sub>r</sub>_, let size(_n<sub>k</sub>_) denote the number of active representatives in the range, and let span(_n<sub>k</sub>_)=_r-l_+1, i.e. the size of the range. The rebalancing strategy is inspired by lazy weight balancing in scapegoat trees from [3]. When we encounter a full gap _L<sub>i</sub>_, we traverse towards the root from its corresponding leaf node _n<sub>j</sub>_ where \(j=i+s'_\#-1\) (with size(_n<sub>j</sub>_)=8). At every step of the traversal, a linear scan counts \(size\left(n_{j\oplus 1}\right)\) (i.e. the sibling’s size), then we compute \(size\left(n_{\lfloor j/2\rfloor}\right)=size\left(n_j\right)+size\left(n_{j\oplus 1}\right)\), and set \(j:=\lfloor j/2\rfloor\), moving to the parent. This process repeats until we encounter a _scapegoat node n<sub>j</sub>_ that satisfies

\(|size\left(n_{2j}\right)-size\left(n_{2j+1}\right)|>max\left(1,size\left(n_j\right)/lgs'_\#\right)\) (10)

