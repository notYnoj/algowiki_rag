## A ADDITIONAL DETAILS FOR PARALLEL OPTIMAL ALPHABETIC TREES (OAT)

This section supplements additional details for the parallel OAT algorithm in Sec. 5.1.

### A.1 Sequential Algorithms for OAT

Hu-Tucker algorithm [53] was the first _O(n_log_n_) algorithm for OAT, and a simplified version Garsia-Wachs algorithm [46] was proposed later. Both algorithms have two phases. In the first phase, a certain tree called the _l_-tree (short for level-tree) is constructed from the input sequence. Hu-Tucker algorithm and Garsia-Wachs algorithm differ in the manner to find the _l_-tree, but the final _l_-tree is the same. In the second phase, the OAT can be constructed from the _l_-tree, and each item in the OAT is at the same level as in the _l_-tree.

The key problem is how to compute the _l_-tree. Here we describe the first phase of Garsia-Wachs, as it is easier to understand than Hu-Tucker and the idea is used in the parallel algorithm by Larmore et al. [72]. Let the input weight sequence be _a_<sub>1_...n_</sub>. We denote _a<sub>i</sub>+a_<sub>_i_+1</sub> be the _i_’th 2-sum, for \(1\le i<n\). A pair of consecutive elements (_a<sub>i</sub>,a_<sub>_i_+1</sub>) is said to be locally minimal if the _i_’th 2-sum is a local minimum in the sequence of 2-sums. The Garsia-Wachs algorithm repeatedly performs the following steps until there is only one element in the sequence:

(1) Find the left-most locally minimal pair (_a<sub>i</sub>,a_<sub>_i_+1</sub>).<tbc>

(2) Combine _a<sub>i</sub>_ and _a_<sub>_i_+1</sub>. Make a new node _x_ to be the parent of _a<sub>i</sub>_ and _a_<sub>_i_+1</sub> in the _l_-tree, and the weight of _x_ is _a<sub>i</sub>+a_<sub>_i_+1</sub>.<tbc>

(3) Remove _a<sub>i</sub>_ and _a_<sub>_i_+1</sub> from the sequence. Insert _x_ before the first element _a<sub>j</sub>_ where _j\>i_ and \(a_j\ge x\). If such _a<sub>j</sub>_ does not exist, insert _x_ at the end of the sequence.

Note that each newly generated node represents a tree, with both children as the two trees corresponding to the two nodes it merges in step (2). At the end, there will be only one element in the sequence, which is the final output of the _l_-tree. An _l_-tree can be easily converted to an OAT in parallel with _O(n_) work and _O_(log_n_) span, and we refer the audience to [72] for more details.

