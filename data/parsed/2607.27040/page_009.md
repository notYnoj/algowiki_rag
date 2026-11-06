**i.** Select the median element _a_med of _S<sub>z</sub>_ by the linear-time stable, in-place selection algorithm of [6] then stably ternary partition _S<sub>z</sub>_ around pivot _a_med [7], logically dividing the block =_a_med at the midpoint of _S<sub>z</sub>_. This leaves the elements of _S<sub>z</sub>_ in the configuration \(a_1\dots a_{\lfloor s/2\rfloor} a_\text{med}a'_1\dots a'_{\lfloor s/2\rfloor}\) where \(a_i\le a_\text{med}\le a'_i\) for all \(1\le i\le\lfloor s/2\rfloor\).

**ii.** Allocate the new segment _S_<sub>_z_+1</sub>, which returns a pointer to its start.

**iii.** Swap the block \(a'_1\dots a'_{\lfloor s/2\rfloor}\) to the front of _S_<sub>_z_+1</sub>.

**iv.** Create the active representative for _S_<sub>_z_+1</sub> by _R_.insert(_a_med). This may invalidate the location returned by _R_.search in step 1 (see Section 2.2). However, as the insertion terminates immediately after without accessing representatives, correctness is unaffected.

After splitting, the ordering invariants are maintained by construction. Since all original elements \(x\in S_z\) satisfied \(f'_z\le x\le f'_{z+1}\), the elements \(\le a_\text{med}\) remaining in _S<sub>z</sub>_ satisfy \(f'_z\le x\le a_\text{med}\) while those moved to _S_<sub>_z_+1</sub> are from the other block \(\ge a_\text{med}\) and satisfy \(a_\text{med}\le x\le f'_{z+1}\). After _a_med is promoted as the new \(f'_{z+1}\), the invariants \(f'_z\le a_i\le f'_{z+1}\) and \(f'_{z+1}\le a'_i\le f'_{z+2}\) hold true. Similarly, the segment invariant is respected: _S_<sub>_z_+1</sub> receives \(\lfloor s/2\rfloor\) elements and \(s-\lfloor s/2\rfloor-1=\lfloor s/2\rfloor\) elements (see (1)) remain in _S<sub>z</sub>_.

In the case where the _R_.search(_x_)=0 in step 1 directing us to _S_<sub>0</sub>, we conduct the following:

1. Swap _x_ with the element at position _l_<sub>0</sub>, then increment _l_<sub>0</sub>.

2. If _l_<sub>0</sub>_\>r_<sub>0</sub>, _S_<sub>0</sub> is full and split using the procedure above, then update \(l_0:=l_0-\lceil s/2\rceil\) so _l_<sub>0</sub> points to the next available buffer space in _S_<sub>0</sub> after the split.

\(\blacktriangleright\) **Lemma 2.4.** _Inserting all m active elements into the structure requires no more than_ \(m\mathrm{lg}\lfloor m/s\rfloor+O(m)\) _comparisons, O(m_) _moves, m cache inserts and_ \(\lfloor m/g\rfloor\) _cache flushes._

**Proof.** We now analyze the cost of inserting all _m_ elements into the structure step-by-step.

1. _R_.search(_x_) requires \(\lfloor\mathrm{lg}s_\#\rfloor+3\le\mathrm{lg}\lfloor m/s\rfloor+4\) comparisons by Lemma 2.1 and (2).

2. Inserting _x_ into the cache line requires a single cache insert. Over \(m-\lfloor s/2\rfloor\le m\) insertions the first 2 steps cost \(m\mathrm{lg}\lfloor m/s\rfloor+4m\) comparisons and _m_ cache inserts.

3. Cache lines are flushed only after _g_ insertions into the same cache line, so cache flushes occur at most \(\lfloor m/g\rfloor\) times, each costing _O_(lg_m_) comparisons and a single cache flush, totaling _O(m_) comparisons and \(\lfloor m/g\rfloor\) cache flushes.

4. Splitting is triggered when a segment has become full after the cache flush. Every split requires: 1 comparison to check fullness, _O_(1) arithmetic operations to allocate a new segment, _O(s_) comparisons and _O(s_) moves for stable selection and partitioning by the median [6, 7], \(3\lfloor s/2\rfloor\) moves to transport \(a'_1\dots a'_{\lfloor s/2\rfloor}\) to the new segment, and _O_(lg<sup>3</sup>_m_)=_o(s_) comparisons and _O_(lg<sup>3</sup>_m_)=_o(s_) moves for _R_.insert(_a_med) by Lemma 2.2 and (1). In total, a split costs _O(s_) comparisons and _O(s_) moves. Since each split creates a new segment, and there are _s_# additional segments, there have been _s_# splits, costing \(s_\#O(s)\le O(m)\) comparisons and \(s_\#O(s)\le O(m)\) moves.

S z+1 <
med amed > amed > amed S Z



**Figure 2** Movement of active elements during splitting a full segment _S<sub>z</sub>_.

