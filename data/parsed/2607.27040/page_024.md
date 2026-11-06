**1. Construct a selection tree on pointers** _a_<sub>1</sub>_...a<sub>k</sub>_ to the first elements of the _k_ runs _A_<sub>_k(j_-1)+1</sub>_...A<sub>kj</sub>_ to select the minimum (rank of pointers dependent on elements they point to). Alongside each pointer to the first elements of the runs, we also store a pointer to the position right after end of each run, denoted by \(a'_1\dots a'_k\). Lastly, we have a pointer _b_ initialized to point to the beginning of the run _B<sub>j</sub>_.

**2. Use the selection tree to select the minimum** _a<sub>x</sub>_ from the current front of all runs (_a_<sub>1</sub>_...a<sub>k</sub>_).

**3. Swap** _a<sub>x</sub>_ with _b_, then increment _a<sub>x</sub>_ and _b_ so they point to the next active element in _A_<sub>(_j_-1)_k+x_</sub> and the next available space in _B<sub>j</sub>_ respectively.

**4. Repair the selection tree to select the next merged element. For runs where** \(a_x=a'_x\), the run is exhausted of active elements, and we treat them as \(\infty\) sentinels.

**5. Repeat steps 2-5 until the root becomes an** \(\infty\) **entinel.**

This process merges the group of runs _A_<sub>_k(j_-1)+1</sub>_...A<sub>kj</sub>_ into one contiguous sorted run stored in _B<sub>j</sub>_, and _A_<sub>_k(j_-1)+1</sub>_...A<sub>kj</sub>_ now hold only buffer elements. For the last potentially short group, we use additional logic to calculate the number of runs, then use the same merge procedure.

After processing all groups, logically swap roles of \(A'\) and \(B'\), as all active elements have been swapped over to the other run. Now, if \(r_i\ge m'\), which is the case when \(i\ge k_\#\), all \(m'\) active elements have been merged into a sorted run. Otherwise, continue to next pass of merging. When the procedure terminates, the logical active region containing all active elements is guaranteed to be the original active region due to the parity handling in the initial run sorting step. This is because there are _k_<sub>#</sub> merge passes, and every merge pass swaps all active elements to the opposite region. If _k_<sub>#</sub> was even, all active elements would end up in the region they started, which is the original \(A'\) as we would have used the cycle method that kept active elements in \(A'\). And if _k_<sub>#</sub> was odd, all active elements would end up in the opposite region, which is the original \(A'\) as we would have exchanged them to \(B'\) in the initial run sorting phase.

We now analyze the cost of a single pass of merging. The first initialization step of merging a group of runs constructs a selection tree over _k_ pointers, requiring _O(k_) comparisons and _O(k_) arithmetic operations, then uses _O_(1) arithmetic operations to initialize _b_, which costs _o(m_) over all groups. Every pointer to an element from a range of \(m'\) elements requires \(O(lgm')=O(lglgm)\) bits by (B.1). As the selection tree on \(\le k\) entries has _O(k_) nodes, the required number of bits for the selection tree is 2_O(k)O_(lglg_m_)=_O(w_) by (B.2), which fits in _O_(1) words.

Subsequently, every merged element is selected from the selection tree using exactly lg_k_ comparisons as _k_ is a power of 2 by (B.2) and exchanged into the next available position in \(B'\) using 3 moves. The arithmetic operations made in assigning and dereferencing pointers are _O_(lg_k_). For the last short group, the selection tree may contain less than _k_ entries, but in any case, the number of comparisons to select each element do not exceed lg_k_.

Thus, the total cost of a merge pass is \(m'lgk+O(m')\) comparisons and \(3m'\) moves, with \(O(m'lgk)\) arithmetic operations. A naive bound for the total cost of the entire algorithm, using the above bound for every pass would give \(m'lgk-m'+k_\#(m'lgk+O(m'))=m'lgm'+O(m'lggm')\) comparisons and \(3(k_\#+1)m'\) moves by (B.2) and (B.3). However, we can obtain a tighter bound by carefully accounting for the comparisons made in the final merge pass.

When we conduct the final merging pass, \(A'\) is made up of runs of size _r_<sub>_k_<sub>#</sub>-1</sub> from the previous merging passes, with the last run being potentially short. Thus, there are at most \(k'=\left\lceil m'/r_{k_\#-1}\right\rceil=\left\lceil m'/k_{k_\#}\right\rceil\) runs. Selecting each element from a selection tree of \(k'\) entries

