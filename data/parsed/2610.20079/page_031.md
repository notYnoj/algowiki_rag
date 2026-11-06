### Removing padding before restoration.

After all complete chunk swaps, scan the layout (_p,s,D_<sub>-</sub>_,g,H_<sub>-</sub>_,z_) and discard exactly those segments with \(s\ge R\). Every complete chunk swap fixes (_p,s_) and is a bit-value-preserving permutation, so no valid bit enters a discarded segment; those segments remain zero. Intermediate coded states need not satisfy this property, which is why removal occurs only after the complete swaps. Concatenate the retained segments, decode _s_ as (_D_<sub>+</sub>_,H_<sub>+</sub>), and then apply _F_ in (22). Removal costs \(O(1+V'/(Bw))=O(1+V/(Bw))\) and restores the original volume before _F_.

The widths, padding tests, and chunk descriptions depend only on the dimensions and are generated using a fixed number of counters, each occupying a constant number of machine words of width _w_. All scans share their stream buffers across prefixes; recursive calls and chunk swaps run sequentially and reuse workspace. Thus the stated memory bound is preserved, and constant-factor padding preserves the polynomial disk-space bound. This proves (21).

## D Formal Verification

We use Lean 4 and Mathlib [dUU21,The20] to formally verify the correctness and complexity bounds of the external-memory integer sorting algorithm in Theorem 3.1, with \(\varepsilon=3/200000=1.5\times 10^{-5}\). The verification covers the full parameter range \(2B\le M\le N\): for every input, the algorithm terminates, outputs the integers in nondecreasing order with their multiplicities preserved, uses at most _M_ words of memory and polynomial disk space, and satisfies the stated I/O bound. These guarantees include the input/output format conversions.

The formalization uses the external-memory model of Section 3. One I/O reads or writes a block of _B_ words. Computation uses only data already read into memory, and data buffers and mutable workspace count toward the _M_-word limit. The program is fixed from the size parameters before the input is given, and in-memory computation is not charged as I/O. Storage of program code and the predetermined execution-step index follows the conventions in that section.

The Lean source code is maintained at https://github.com/rtyu-1/coded-sorting-lean. The proofs have been checked by the Lean kernel, without unfinished proofs or additional mathematical axioms. Readers can follow the repository instructions to build the project and inspect the assumptions and conclusions of the formal statements.

## References

