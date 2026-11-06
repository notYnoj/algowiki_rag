overall merge. In particular, at every step of the high-level merge, we will run the single-word merge on the leftover word from _L<sub>b</sub>_ with the next full word from \(L_\overline{b}\).

\(\blacktriangleright\) **Lemma 13.** _Let w be the word size. Given compressed sorted lists L_<sub>0</sub> _and L_<sub>1</sub> _where both lists are stored in a single word, the merge step of L_<sub>0</sub> _and L_<sub>1</sub> _can be implemented in constant time with_ AC0 _word operations. We assume list elements are in the universe_ [2_<sup>u</sup>_] _for_ \(u\le w\).

**Proof of Lemma 13.** Since _L_<sub>0</sub> and _L_<sub>1</sub> are stored in a single word, we may assume there are at most \(k=\lfloor w/u\rfloor\) elements in each. If the lists have fewer than _k_ elements, we expect the entries to appear packed consecutively in the upper bits of the word, and the remainder of the word to be padded with _u_-bit \(\pm\) entries which are treated as "infinity", larger than all other entries.

To sort \(L_0\cup L_1\), observe that it suffices to determine, for every element _x_ in _L_<sub>0</sub>, the number of elements in _L_<sub>1</sub> that precede _x_ in sorted order, and for every element \(x'\) in _L_<sub>1</sub>, the number of elements in _L_<sub>0</sub> that precede \(x'\) in sorted order. Using an AC0 circuit, exploiting the fact that _L_<sub>0</sub> and _L_<sub>1</sub> are already sorted, we can check all possible values for these numbers in parallel. We will perform comparisons as if all entries in _L_<sub>0</sub> have a trailing 0 appended to them, and all entries in _L_<sub>1</sub> have a trailing 1. This means that there does not exist any element that appears in both _L_<sub>0</sub> and _L_<sub>1</sub>, which has the effect of breaking ties in favor of _L_<sub>0</sub>.

To compute the _k_th value of the merged output, we check the following. For every \(i\in[|L_0|]\), compute _j=k-i_. Then, check the following conditions:

(1) _L_<sub>0</sub>[_i]\>L_<sub>1</sub>[_j_] and

(2) either _L_<sub>0</sub>[_i]\<L_<sub>1</sub>[_j_+1] or \(L_1[j]=\pm\).

If the AND of (1) and (2) holds, we output _L_<sub>0</sub>[_i_], else output 0. We then OR together all of these gadgets for all \(i\in[|L_0|]\), and also OR these results with the analogous computation taking \(i\in[|L_1|]\). If the condition is satisfied (say for \(i\in[|L_0|]\)), this means that there are _j_+1 elements in _L_<sub>1</sub> that are strictly smaller than _L_<sub>0</sub>[_i_], and the rest of the elements are strictly larger. Since elements in _L_<sub>0</sub> cannot be equal to those in _L_<sub>1</sub>, there is only one such value of _j_ per element. Additionally, since we enforce that our merge step is stable, the (unique) correct location in the merged list for this element is _i+j_, as desired.

As mentioned in Section 2, the addition and comparisons can be done in AC0. By construction, at most one comparison gadget fires a nonzero index, so we can simply OR them all. Thus, we can run these checks for all |_L_<sub>0</sub>|+|_L_<sub>1</sub>| list elements in parallel, constructing our merged list index by index.

All that remains is to determine which list will be left empty following the merge step. To do this, let _i_ and _j_ be the last elements of _L_<sub>0</sub> and _L_<sub>1</sub>. If _i\<j_, then _L_<sub>0</sub> is the newly emptied list (_b_=0), otherwise _L_<sub>1</sub> is emptied (_b_=1). Let _m_ be the minimum of _i_ and _j_. We place all elements whose sorted rank is in [_m_] into at most two words, which is the merged portion. We can pad the second word with \(\pm\). We place the remaining non-\(\pm\) elements (all from list \(L_\overline{b}\)) into another word (again padding with \(\pm\)), and return _b_, completing the merge step.

As mentioned above, each of these gadgets is constant-depth, and we compose them in parallel. For every element, we perform at most max(|_L_<sub>0</sub>|,|_L_<sub>1</sub>|) comparisons, so the circuit size is at most quadratic in the input size, and thus the entire construction is in AC0.

\(\triangleright\) Claim 14. Given compressed sorted lists _L_<sub>0</sub> and _L_<sub>1</sub> with _u_-bit entries and at most _k_ elements each, a merge of _L_<sub>0</sub> and _L_<sub>1</sub> can be implemented in _O(ku/w_) time with AC0 word operations.

**Proof of Claim 14.** We will use Lemma 13 as a subroutine. We know that _L_<sub>0</sub> and _L_<sub>1</sub> are word-packed, so we can merge them one word at a time. In particular, start by merging the

