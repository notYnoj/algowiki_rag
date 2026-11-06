<tbc>width into recursive scales. This keeps the additional padding within the original data volume and proves the general bound \(Q(e,V)=O(1+\frac{V}{Bw}[1+(e/t_0)^\tau])\).

Finally, return to binary addresses. Choose the smallest _e_ with \(q^e\ge 2^u\), and pad both field ranges from \[2_<sup>u</sup>_\] to \[_q<sup>e</sup>_\], increasing the volume by less than the fixed factor _q_<sup>2</sup>. Adding and removing padding require only scans, and the complete interchange preserves the set of valid positions whose two coordinates are both below 2_<sup>u</sup>_. The bound follows from _e=O(u_), \(t_0=\Theta(a)\), and (21). Lemma A.2 extends it to all \(M\ge max\{2B,C_\text{abs}\}\). The matrices are fixed, and the schedule is generated from dimension parameters independently of the data. Streams, padding, and the stack of descriptions all have polynomial size. The buffering and suspension rules above ensure the claimed memory and disk-space bounds.

## 7 Local Sorting

Address-field interchange rearranges records, but sorting also needs value comparisons. We use classical Columnsort, alternating column sorts with fixed rearrangements that bring records from different columns together for comparison \[Lei85, CC03\]. We first prove Columnsort correct and reduce its rearrangements to address-field interchange, then bound the recursive cost.

A record occupies _O(w_) bits and may be an integer or a constant number of integer fields compared lexicographically. The word size \(w=\Theta(logN)\) is always determined by the global input size _N_. Keep _a_=log(_M/B_) and \(\tau=1-\varepsilon\), and set \(H=\lfloor M/C\rfloor\). Choose the fixed constant _C_ large enough that 512_H_ records, including the two-bit tags used below to distinguish ordinary records from padding, fit in reserved memory, leaving space for buffers and control information. We first assume sufficiently large _M_ and _M/B_; Corollary A.3 transfers the bounds to all \(2B\le M\).

### 7.1 The Columnsort Reduction

Columnsort requires columns long enough to contain the disorder left by its rearrangements. We use _s_ columns of _r=s_<sup>3</sup> records: this shape satisfies the Columnsort conditions and makes column length the 3/4 power of the total size _rs_, allowing recursion to shrink the problem. Taking _s_=2_<sup>t</sup>_ also expresses each record address as four equal-width fields, so the intercolumn rearrangement becomes a rotation of those fields. The next proposition reduces the required movement to six interchanges.

**Proposition 7.1** (The Columnsort reduction)**.** Let _s_=2_<sup>t</sup>_ and _r=s_<sup>3</sup>, where \(t\ge 3\). An array stored as _s_ contiguous columns of _r_ records each can be sorted using four rounds of column sorting, six address-field interchanges of width _t_, and sequential scans. The procedure is correct whenever all column sorts are correct.

_Proof._ Step 2 distributes records from each original column among the new columns for joint sorting; step 4 restores the original column layout. A final half-column shift brings remaining inversions across old boundaries into one column. The eight steps are:

1. Sort each column.<tbc>

2. Move the record at position _j_ to \(\pi(j)=(jmods)r+\lfloor j/s\rfloor\).<tbc>

3. Sort each rearranged column.<tbc>

4. Apply the inverse permutation \(\pi^{-1}\).<tbc>

