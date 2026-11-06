will be the leaves. The root, we label level 1, of the binary tree will get the most significant bit, namely _g_<sub>_f_(log_n_)</sub>. The nodes in level _k_ will get _g_<sub>_f_(log_n_-(_k_-1))</sub>. The distribution of this bit starts with the least significant bit first and end with the most significant bit to the root. This process does not proceed in parallel but in a sequential process using token passing. This requires _g_<sub>_f_(log_n_)</sub>_,g_<sub>_f_(log_n_-1)</sub>_,...,g_<sub>_f_(2)</sub> to receive a bit to start the seeding of the next level. This ensures that the first bit received by the nodes of the tree is the control bit. Once the root gets its control bit, it follows the binary search process described in proof of Theorem 5.1. Only one leaf will receive a bit and it declares the correct count based on its position in the tree. □

## 5.3 Solving Sorting and Searching with Constant Local Complexity

The ability to count 1 bits in the input with constant local complexity enables the solution of other natural problems with this same low complexity. We highlight two such problems here:

**Sorting:** The first problem is _sorting_. In the context of binary inputs distributed among _n_ nodes, _P_<sub>1</sub>_,P_<sub>2</sub>_,...,P<sub>n</sub>_, sorting reduces to gathering all the 1 bits together. Formally, if #<sub>1</sub>(_a_<sub>1</sub>_...a<sub>n</sub>)=k_, then to solve sorting for input _a_<sub>1</sub>_...a<sub>n</sub>_, the nodes in {_P_<sub>1</sub>_,...,P<sub>k</sub>_} should output 1, and the nodes in {_P_<sub>_k_+1</sub>_,...,P<sub>n</sub>_} should output 0.

The counting solution described in analyzed in Theorem 5.1 has the nice property that not only does a node output _k_, but the unique node that does so is _P<sub>k</sub>_. To extend this solution to sorting, therefore, it is sufficient for _P<sub>k</sub>_ to disseminate a bit down the line from _P_<sub>_k_-1</sub> to _P_<sub>1</sub>, letting these preceding nodes know that they should also output 1. This increases the local complexity by a single bit from 11 to 12. Formally:

**Theorem 5.4.** _The sorting of 1-bit inputs can be solved with local complexity_ 12.

**Searching:** Another natural problem is _searching_. In particular, for a given binary input assignment _a_<sub>1</sub>_...a<sub>n</sub>_, we say that _P<sub>i</sub>_ has the _k_th "1", if: (1) _a<sub>i</sub>=_1, and (2) #<sub>1</sub>(_a_<sub>1</sub>_...a<sub>i</sub>)=k_. We can therefore define a search problem, parameterized with _k_, such that the goal is to output the id of the node with the _k_th one. Building on our counting strategy, we can also solve this problem with constant local complexity:

**Theorem 5.5.** _For every network size n=_2_<sup>i</sup> and search location_ \(k\le n\)_, searching for the kth_ 1 _can be solved with constant local complexity._

_Proof._ First, run the protocol for counting the number of ones in the input where the result is in the binary form. This is the first tree of the Theorem 5.1.

Now store _k_ in binary in log_n_+1 locations. If _k=n_ then check the count is equal to _n_ and report the outcome.

From now on we assume that _k\<n_ and if there is _k_ ones it will be between 0 through _n_-1. This occupies log_n_ bits in binary form. Let the count of 1s to be _c_(1_,n_). Compare _k_ with _c_(1_,n_). This comparison can be done in _O_(1) local communication complexity by starting with comparing most significant bit first and find out if _k\>c_(1_,n_). If _k\>c_(1_,n_) then there is no such _k_ exists. Store _k_ in exactly the same place where _c_(1_,n_) is stored. Recall that we have the counts _c_(1_,n/_2) and _c(n/_2+1_,n_) whose sum led to _c_(1_,n_) still stored in appropriate places. We compare _k_ with _c_(1_,n/_2) in _O_(1) local communication complexity to find out if _k\>c_(1_,n/_2).

If the answer is yes, then perform subtraction _k-c_(1_,n/_2). The subtraction is very similar to the addition we performed in the Theorem 5.1. Store the result in exactly the same place where the bits of count _c(n/_2+1_,n_) are stored. Now you can compare this new _k_ with _c(n/_2+1,3_n/_4).

But if the answer is no, then copy _k_ into where bits of _c_(1_,n/_2) are stored and compare this with the count _c_(1_,n/_4).

This process continues until we hit a final group of 16 bits. One can then easily find the original _k_th one in constant local communication complexity. □

