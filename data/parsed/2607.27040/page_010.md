Inserting an element into _S_<sub>0</sub> is equivalent to a standard insertion without the overhead of cache operations (steps 2, 3) by leveraging the auxiliary pointers. Thus, the cost lies within the general bound. Adding the per-step bounds yields the bounds stated in the lemma. \(\blacktriangleleft\)

## 2.5 Extracting in Sorted Order

The extraction phase transports all active elements back to _A_ in sorted order. After insertion completes, every active element lies either in the frame, cache or segments, whilst _A_ contains only buffer elements.

By a linear scan through the _L_, for every active representative \(R'_i\), \(G'_i\) is emptied into _Si_ by the same method as step 3 of insertion. In total, _o(m_) comparisons and _s_# cache flushes are required to empty all cache lines. This leaves active elements either as active frame elements \(f'_1\dots f'_{s_\#}\) in sorted order or in segments _S_<sub>0</sub>_...S<sub>s<sub>#</sub></sub>_, where for any \(a_i\in S_i\), the ordering invariant \(f'_i\le a_i\le f'_{i+1}\) holds. It follows that, the sequence \(S'_0f'_1S'_1f'_2\dots f'_{s_\#}S'_{s_\#}\) is the sorted sequence of all _m_ active elements, where \(S'_i\) denotes the sorted sequence of all active elements in _Si_. We now construct this sequence in _A_.

First, we transport \(S'_0\) to the front of _A_. We sort the active elements in _S_<sub>0</sub> (from _l_<sub>0</sub> to _r_<sub>0</sub>) with the small sort using _A_ as the merge buffer, then move the sorted block to the front of _A_.

Next, we linearly scan through _L_ from left to right. for each active representative \(R'_i\) we encounter, we conduct the following:

**1.** Swap the element \(f'_i\) with the next available buffer space in _A_.

**2.** Read the corresponding active segment pointer \(p:=P'_i\) to locate the physical position of _Si_.

**3.** Perform a binary search over _Si_ to find the number of active elements in _Si_, denoted by _si_. Let the active elements in _Si_ be _a_<sub>1</sub>_...a<sub>si</sub>_.

**4.** Using _S_<sub>0</sub> (already emptied) as the merge buffer, sort _a_<sub>1</sub>_...a<sub>si</sub>_ with the small sort.

**5.** Move _a_<sub>1</sub>_...a<sub>si</sub>_ into the next _si_ buffer positions in _A_.

Every iteration adds the sequence of active elements \(f'_iS'_i\) to the end of the growing sorted sequence in _A_. Since active representatives appear in sorted order in _L_, the resulting sequence in _A_ is exactly \(S'_0f'_1S'_1f'_2\dots f'_{s_\#}S'_{s_\#}\), the global sorted sequence of all _m_ active elements.

Finally, to fulfill the Section 2 termination requirements, we verify the ending states of _B_ and _V_ . Throughout, the algorithm writes elements only by swapping (via hole :=_a_, _a_:=_b_, _b_:= hole), which exclusively permutes elements. Since the final sorted permutation of all active elements is in _A_, then the remaining elements in _B_ are already a permutation of the original buffer elements. However, the bit vector remains modified, requiring a linear scan to reset it to all `false`, using |_V_|=_o(m_) comparisons and at most 3|_V_|=_o(m_) moves (see (8)). Subsequently the algorithm terminates safely.

\(\blacktriangleright\) **Lemma 2.5.** _Extracting all m active elements from the structure in sorted order requires no more than m_lg_s+O(m_) _comparisons, O(m_) _moves and s_# _cache flushes._

**Proof.** The linear scan in _L_ requires \(|L|=8s'_\#\) comparisons. Each segment is processed using _si_lg_s<sub>i</sub>+O(s<sub>i</sub>_) comparisons and _O(s<sub>i</sub>_) moves (handling _S_<sub>0</sub> is a simplified case that lies within the same bounds):

**1.** Swapping \(f'_i\) into _A_ costs 3 moves.

**2.** reading \(P'_i\) requires \(\lfloor lgm/s\rfloor+2\) comparisons.

**3.** The binary search for _si_ takes \(\lfloor lgs\rfloor+1\) comparisons.

**4.** Sorting the segment requires _si_lg_s<sub>i</sub>+o(s<sub>i</sub>_) comparisons and _O(s<sub>i</sub>_) moves by Lemma 2.3.

**5.** Swapping _si_ elements into _A_ costs 3_si_ moves.

