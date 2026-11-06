<tbc>for why this causes positive entropy production). Thus, it is necessary to determine the induced marginal probability distribution over the bit being erased conditioned on the values stored on all other wires to obtain zero circuit entropy production.

First we explain how to compute the mapping \((b,V)\mapsto(b,s,W)\) reversibly. In the sorting network _C_, replace each comparator gate between wires _i_ and _j_ with a reversible comparator between records that also outputs (for reversibility) whether a swap occurred:

\(\begin{array}{ c c c c }
 & ((b_i,V_{i:}), & (b_j,V_{j:}), & 0 \\
 & ((b'_i,V'_{i:}), & (b'_j,V'_{j:}), & g
\end{array}),\)

where the primed values are the identity if \(b_i\le b_j\) and swapped otherwise, with _g_=1 if a swap occurred and 0 otherwise. To implement this record comparator using constant-size gates, we reversibly distribute _g_ to _m_ clean ancilla wires using a balanced tree of copy gates of depth _O_(log_m_), use those copies to swap all _m_ pairs of payload bits in parallel, and then reverse the copy tree. Thus each comparator of _C_ becomes _O(m_) gates of depth _O_(log_m_). All record comparators belonging to one layer of _C_ act on disjoint records, so their copy trees and bit swaps can be performed in parallel. The resulting reversible sorting computation has gate complexity _O(t(n)m_) and depth _O(d(n_)log_m_). Running this modified sorting network _C_ on the records (_b,V_) results in the sorted output (_s,W_) described above, along with "garbage" data _G_ indicating which swaps occurred, reversibly computing the mapping<tbc>

\(\begin{array}{ c c c c }
 & (b,V, & \vec{0} & ) \\
 & (s,W, & G & ).
\end{array}\)

<tbc>We now reversibly copy _s_:<tbc>

\(\begin{array}{ c c c c c }
 & (s,W, & G, & \vec{0} & ) \\
 & (s,W, & G, & s
\end{array}).\)

<tbc>Now, "uncompute" _C_ via the mirror-image reverse of the first sorting step, but using swap gates that _only_ swap the keys, leaving the sorted payloads in place:

\(\begin{array}{ c c c c c }
 & (s,W, & G, & s & ) \\
 & (b,W, & \vec{0}, & s
\end{array}).\)

This completes the mapping \((b,V)\mapsto(b,s,W)\), using _O(t(n)m_) gates and _O(d(n_)log_m_) depth.

At this point we _almost_ have the clean output _y_=(_s,W_), but it remains to erase the unsorted key bits _b_.

Write \(b_{\le i}\) to denote the _i_’th prefix _b_<sub>1_..i_</sub> of _b_ (similarly \(b_{<i}=b_{1..i-1}\), \(b_{\ge i}=b_{i..n}\), and _b<sub>>>\>i</sub>=b_<sub>_i_+1_..n_</sub>). Let _h_=|_b_|<sub>1</sub>=|_s_|<sub>1</sub>. We erase the bits one at a time starting with the first, successively producing \(b\mapsto 0b_{\ge 2}\mapsto 00b_{\ge 3}\mapsto\dots\mapsto 0^{n-2}b_{n-1}b_n\mapsto 0^{n-1}b_n\mapsto 0^n\). Suppose we currently have \(0^{i-1}b_{\ge i}\) and now need to erase _b<sub>i</sub>_; call this _stage i_. The correct distribution to assume when erasing _b<sub>i</sub>_ when we apply Lemma 3.1 is such that the probability of a one is \(|b_{\le i}|_1/i\); we justify this at the end of the proof. The denominator _i_ is a fixed constant in stage _i_ of this circuit, so the key is to make the numerator \(z_i=|b_{\le i}|_1\) reversibly available in a binary register _Z_, which will then be used to route _b<sub>i</sub>_ to a "controlled erasure" gate with an optimal heat function for this probability.<sup>37</sup> We explain below how to maintain _Z_ incrementally as we iterate through the bits of _b_.

<sup>37</sup>A controlled erasure gate takes two input bits: _c_ and _b_. If the control bit _c_=0, then it leaves _b_ alone (and releases 0 heat), otherwise it erases _b_. We need these because there will be a "bank" of several that might be used, but only one will actually be used to erase _b<sub>i</sub>_, i.e., will have its _c_=1; the other gates will have _c_=0.

