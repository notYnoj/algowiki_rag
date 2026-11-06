operations, we need

\(10^L\le 2^{-m/9}NN_0.\) (6)

This also holds: \(10^{19}\cdot 2^{1/9}/3^{18}<4^{18}\), so \(10^L\cdot 2^{m/9}/N_0\le D^{18}\le N\).

_The algorithm._ We compute the encodings of all row bands and column bands (Section 2.4.1). Each wanted position \((I,J)\in W\) lies in one tile _T_ and is indexed by one output string of _T_, the string whose inner set is the subset _Q_ of the block product containing (_I,J_) and whose row and column are those of (_I,J_) within that block product (Sections 2.3.3 and 2.3.4). For each tile _T_, let _W<sub>T</sub>_ be the set of the output strings of the wanted positions in _T_. Then, for each tile _T_ with \(W_T\neq\emptyset\), we run Pruned(_W<sub>T</sub>_), and report, for each \((I,J)\in W\), the value at its output string. This is correct by Lemmas 9 and 10.

_The cost._ By (6), the encodings cost \((2N/K_0N_0)\cdot O(10^L)=O(2^{-m/9}N^2)\) operations. Each position of _W_ lands in one set _W<sub>T</sub>_, so \(\sum_T|W_T|\le|W|\le N^2/\sqrt{D}=2^{-m}N^2\), and there are at most 4_N_<sup>2</sup>_/M_ tiles, so \(\sum_TM\le 4N^2\). A call of Pruned with a set _S_ takes _O(L|S_|) operations, since each of its steps handles each string of _S_ a constant number of times and a string has length _L_ (we store the sets as sorted lists, so that a slice is a segment and a union of slices is a merge). By Lemma 10, the total number of operations per leaf of Leaves(_W<sub>T</sub>_) is thus _O(L_<sup>2</sup>)=_O_(log<sup>2</sup>_D_). Thus, by Lemma 11 summed over the tiles, the pruned recursions use

\(O\big(L^2\sum_T|\text{Leaves}(W_T)|\big)\le O\big(L^22^{-m/9}\big(2^m|W|+2\sum_TM\big)\big)=O(L^22^{-m/9}N^2)\)

operations, no matter how _W_ is distributed among the tiles. The remaining minutiae, which list the \(K_0^2\) subsets, locate the output strings, and sort the sets _W<sub>T</sub>_, take _O(L_) operations per subset, per tile, and per position of _W_, which is _O(L_2<sup>-_m/_9</sup>_N_<sup>2</sup>) in all (as \(K\le N\), there are at most 4_N_<sup>2</sup>_/N_<sub>0</sub> tiles, \(|W|\le 2^{-m}N^2\), and \(N,N_0\ge 2^{m/9}\)). Finally, since _L_=19log<sub>4</sub>_D_ and 2<sup>-_m/_9</sup>=_D_<sup>-1/18</sup>, the total operation count is _O(N_<sup>2</sup>log<sup>2</sup>_D/D_<sup>1/18</sup>), as desired.

_Word size._ Every number the algorithm handles is an integer of magnitude _N_<sup>_O_(1)</sup>. The input entries are of this size, by assumption. Every number in an encoding, or formed on the way to one, is a \(\pm 1\) combination of at most 7_<sup>L</sup>_ input entries, as step (2) only adds and subtracts slices, and every value computed by Pruned is a sum of at most 10_<sup>L</sup>_ products of two encoded numbers (Lemma 7), where \(7^L\le 10^L\le N^2\) by (6). Indices and list positions are at most the number of words in use, also _N_<sup>_O_(1)</sup>. Hence every integer has _O_(log_N_) bits, as desired.

_Remark_ 12 (comparison with related techniques). Prior work on matrix multiplication typically counts only multiplications, since they are usually a dominant cost for the algorithm, whereas in our algorithm, the additions need to be dealt with carefully. Our encodings (Section 2.4.1) are Yates’ algorithm for Kronecker powers [Yat37, Goo58], as is standard in recursive matrix multiplication algorithms. The pruned recursion of Section 2.4.2 is an analog of FFT pruning [Mar71, SB93], of trimmed Möbius inversion [BHKK10], and, transposed, of sparse evaluation of Kronecker-power circuits [AL25], which builds on [Wil24]. The new part along these lines in this paper is the count of Section 2.4.3, which shows that the pruned recursion visits few leaves.

## 3 Exact Triangle reduces to computing certain entries of a thin matrix product

This section derives the faster deterministic algorithms for Exact Triangle (given a tripartite graph with integer weights on its edges, is there a triangle whose three weights sum to zero?),<tbc>

