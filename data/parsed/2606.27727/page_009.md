predicate evaluated on the associated entry in another word. We now show, inspired by bit tricks from [25], that we can produce a mask that indicates the all-zeros entries in _O_(1) time.

\(\triangleright\) Claim 16. Let _z_ be a word in a compressed list. There is a constant-time algorithm to produce an indicator mask whose ones indicate that the associated entries in _z_ are all-zeros.

**Proof of Claim 16.** The high-level idea is as follows: we will produce a mask _IL_ that indicates whether the leading entry is a zero, a second mask _IR_ that indicates whether the remaining \(\ell-1\) are all-zeros, and return \(IL\wedge IR\).

The first mask is easy to construct. Let _I_ be the indicator mask whose indicator bits are all ones. Let \(IL:=I\wedge(\neg z)\). This sets all indicator bits to 1 if and only if the leading bits in their associated entries were 0. We then use a bitmask to zero out non-leading bits in _IL_.

Constructing _IR_ requires a bit more work. First, we need to zero out the leading bits of every entry while leaving the remaining bits untouched. To do this, we compute \(R:=z\wedge(\neg I)\). Now, consider _D_:=_I-R_. For each entry, since the leading bit of _I_ is a 1 while that of _R_ is a 0, there is no borrowing across entries. If the value in _R_ is nonzero, then the subtraction requires borrowing from the leading 1 in the corresponding entry in _I_. Thus the entry has the form 0∗. If the value in _R_ is all-zeros, the entry is 100_..._ as before. Thus, \(IR:=D\wedge I\) is an indicator mask for the entries whose non-leading bits were all-zeros in _z_, as desired. We return \(IL\wedge IR\). Because the computation required a constant number of word operations, we get a runtime of _O_(1). \(\blacktriangleleft\)

Our next task is to compute an indicator mask for set intersection.

\(\triangleright\) Claim 17. Given two sorted compressed lists _L_<sub>0</sub> and _L_<sub>1</sub> with _k_ elements of length \(\ell\) bits, which correspond to _k_-element sets _S_<sub>0</sub> and _S_<sub>1</sub>, we can compute a mask that indicates elements in \(S_0\cap S_1\) in \(O(k\ell/w)\) time.

**Proof of Claim 17.** Since _L_<sub>0</sub> and _L_<sub>1</sub> correspond to sets, we assume they do not contain duplicates. We begin by merging _L_<sub>0</sub> and _L_<sub>1</sub> to produce a new compressed list _L_. By Claim 14, this can be done in \(O(k\ell/w)\) time. We then make a copy of _L_ and shift it to the left \(\ell\) bits. We XOR _L_ with the shifted copy. This causes any adjacent duplicates (which correspond to items in \(S_0\cap S_1\)) to have all-zeroes entries of length \(\ell\) in locations corresponding to indices in _L_<sub>0</sub>. We can then use Claim 16 to produce an indicator mask with ones in these locations in constant time. The runtime is thus dominated by the merge step. \(\blacktriangleleft\)

The purpose of computing these indicator masks is to efficiently indicate "special" list entries that are of interest to our algorithms. However, these compressed lists are created as a result of hashing, and our algorithms generally need to filter out false positives by looking up the associated entries in the preimages. To that end, we need to be able to extract indices of the ones in our masks. We will use the following AC0 circuit to do this:

\(\triangleright\) Claim 18. In the AC0-RAM model, there is a constant-time algorithm that returns the index of the most significant set bit of a word.

**Proof of Claim 18.** Our goal is to produce a length-log_w_ index indicating the most significant set bit. There are _w_ possibilities, and we can construct a depth-one circuit that checks each one. In particular, to check if the _i_th bit is the leftmost set bit, we AND _i_ with the negation of each of the _i_-1 bits to its left.

We now need to reconstruct the index. To do this, we add an additional layer of OR gates _G<sub>j</sub>_ for every \(j\in[logw]\). We would like for the concatenation of all the _G<sub>j</sub>_’s in order to produce the index. Fix one of the circuits above, and let _i_ be the input bit that it is

