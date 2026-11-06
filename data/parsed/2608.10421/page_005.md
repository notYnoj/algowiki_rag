Hence, we assume no savings occur. Each of the _r_ elements in the run is charged 1 comparison per level, incurring a collective charge of at most _r_ comparisons at each level. Summing across the _t_ upper levels _h_=0_,...,t_-1, the total merge cost charged to the run is bounded by _rt_.

**Lemma 6** (Comparisons at Lower Levels)**.** _For a non-decreasing run of length r, the total number of comparisons charged to its elements at levels_ \(h\ge t\) _is bounded by_ 2(_n/_2_<sup>t</sup>)._

_Proof._ For levels \(h\ge t\) we have that \(h\ge\lceil lg(n/r)\rceil\ge lg(n/r)\) which gives \(n/2^h\le r\). However, _r_ is an integer so \(\lceil n/2^h\rceil\le r\), bounding the node sizes on these levels at _r_ elements. Thus, Case 3 (Encapsulating) nodes, which require at least _r_+2 elements, cannot exist on these levels. Therefore, any node relative to the run must either be fully contained within it (Case 1), fall completely outside of it (Case 4), or intersect exactly one of the run’s edges (Case 2). The only such nodes with costs relevant to the run are Case 2 (Boundary) nodes. Because the run spans a contiguous interval, there are at most two Case 2 nodes at any level: one containing the left boundary of the run, and one containing the right boundary.

## Left Boundary Analysis:

Let _v<sub>i</sub>_ be the Case 2 node on the left boundary at level \(i\ge t\), with size _n<sub>i</sub>_=|_v<sub>i</sub>_|. Because _v<sub>i</sub>_ contains the left boundary of the run, the run forms a suffix of _v<sub>i</sub>_. Node _v<sub>i</sub>_ splits into children _L_ and _R_ where \(|L|=\lfloor n_i/2\rfloor\) and \(|R|=\lceil n_i/2\rceil\). We trace the path of left boundary nodes down the tree:

1. **Subcase A (Boundary falls in _R_):** The left child _L_ lies entirely outside the run, and the run elements in _v<sub>i</sub>_ fall within _R_. We explicitly define the next boundary node in our path as _v_<sub>_i_+1</sub>=_R_. The maximum comparisons charged is 1 for each of the _s<sub>i</sub>_ run elements in _v<sub>i</sub>_. Since the run boundary falls inside _R_, \(s_i\le|R|-1\). Given \(|R|=\lceil n_i/2\rceil\), it follows that:<tbc>

<tbc>\(s_i\le\lceil n_i/2\rceil-1\le\lfloor n_i/2\rfloor=|L|=n_i-|R|=n_i-n_{i+1}\)<tbc>

2. **Subcase B (Boundary falls in _L_):** The right child _R_ is entirely contained within the run, making _R_ a pure sub-run. We explicitly define the next boundary node in our path as _v_<sub>_i_+1</sub>=_L_. Because _R_ is pure, its recursive sort returns `true`, setting \(b\leftarrow\text{\texttt{true}}\). Furthermore, because _L_ contains a boundary between two runs, it is not pure, and its recursive sort returns `false`, setting \(a\leftarrow\text{\texttt{false}}\). The directional mergesort thus selects mergeBw, which compares elements from largest to smallest (selecting from _R_ upon ties). Because all elements in _R_ and \(L\cap\text{Run}\) belong to the same sorted run, every element in _R_ is \(\ge\) all run elements in _L_. Consequently, the algorithm exhausts _R_ inside the main comparison loop (costing |_R_| comparisons) before selecting any elements from \(L\cap\text{Run}\). The remaining run elements in _L_ are merged direct using 0 comparisons. Thus, the charged cost is exactly |_R_|. Since _n<sub>i</sub>_=|_L_|+|_R_| and _v_<sub>_i_+1</sub>=_L_, the cost is:<tbc>

<tbc>\(|R|=n_i-|L|=n_i-n_{i+1}\)<tbc>

3. **Subcase C (Boundary aligns perfectly):** If the boundary aligns perfectly with the partition between _L_ and _R_ at some level _k_, _R_ is a pure sub-run (Case 1) and _L_ contains zero run elements (Case 4). Node _v<sub>k</sub>_ is therefore the final Case 2 node in the boundary path. As in Subcase B, _R_ is pure, triggering mergeBw which exhausts the elements in _R_ at a cost of |_R_| comparisons (using worst-case charge of 1 comparison per element). To cleanly terminate the telescoping sum, we define the final term _n_<sub>_k_+1</sub>=|_L_|. The cost at this terminal level _k_ is:<tbc>

<tbc>\(|R|=n_k-|L|=n_k-n_{k+1}\)<tbc>

