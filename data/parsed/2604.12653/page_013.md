(7) All leaders in _L_<sub>0</sub> have a height in \[0,4\], and for \(i\ge 1\), all leaders in _L<sub>i</sub>_ have a height in \([2^i,4\cdot 2^i]\). (Recall that the height of a leader is its height in _M_, not in _L<sub>i</sub>_.)<tbc>

(8) The leaders in _L<sub>i</sub>_ of height \((2\cdot 2^i,4\cdot 2^i]\) in _L<sub>i</sub>_ are called _unpromoted_. Among every maximal sequence \(u_\ell,\dots,u_r\) of consecutive leaders in _M_ that all are in _L<sub>i</sub>_ and are all unpromoted, we require there be at least one leader of height \(2\cdot 2^i+1\) or \(2\cdot 2^i+2\). We call such a sequence \(u_\ell,\dots,u_r\) an _unpromoted block_.

Invariant (8) might seem artificial at first, but it will allow us to move many leaders from _L<sub>i</sub>_ to _L_<sub>_i_+1</sub> at once. Indeed, whenever there is a leader of height \(4\cdot 2^i\) in _L<sub>i</sub>_, the unpromoted block in invariant (8) contains \(\Omega(2^i)\) consecutive unpromoted leaders in _M_. By promoting a whole block from _L<sub>i</sub>_ to _L_<sub>_i_+1</sub>, we will save a bunch of time updating subtree minima. Invariants (6) and (7) allow us to bound the height of the index trees:

**Lemma 15.** _Let u be a leader that is stored in some index tree L<sub>i</sub>. Then_ \(\text{height}(L_i)\in O(\text{height}(u))\).

_Proof._ By Invariant (7), we have \(\text{height}(u)\ge 2^i\) or _i_=0. By Invariant (6) and (7), we have \(|L_i|\le 23\cdot 4^{2^{i+2}}\). Thus, \(\text{height}(L_i)\le 2^{i+2}log(4)+log(23)\in O(2^i)\).

## 5.3 Storing the data structure

We use a "level-linked" representation of the main tree: every node stores pointers to its parent and its children, plus pointers to the left and right neighbor of the same height. Every internal node stores a Boolean indicating whether it is active or not. Every leaf _i_ stores its index _i_, its item, and its last access time _s(i_). Each active internal node moreover stores the maximum access time in its subtree, and a pointer to the minimum item in its subtree. In combination with invariant (3), this level-linked representation allows us to go from a leader to the next or previous leader by following _O_(1) pointers and checking whether _O_(1) nodes are active or not.

For the index trees, we use any balanced binary tree that allows us to insert or delete _k_ (presorted) consecutive items in _O(k_+log_S_) time where _S_ is the size of the balanced binary tree. We call this a _bulk insertion / deletion_. If a balanced binary tree _T_ of size _S_ can be built in _O(S_) time and supports split and join operations in _O_(log_S_), then we can do a bulk insertion by splitting _T_ into _T_<sub>1</sub>_,T_<sub>2</sub> at the insertion location, building a tree \(T'\) on the _k_ presorted elements, and joining \(T_1,T',T_2\). Similarly, we can perform a bulk deletion by splitting _T_ into \(T_1,T',T_2\) and joining _T_<sub>1</sub>_,T_<sub>2</sub>. One example of a balanced binary tree with these properties is a red-black tree \[27\].

Every node in an index tree stores its subtree minimum, and the size of its subtree. We can update these values during a split or join operation in _O_(log_S_) time. In particular, while maintaining these values, we can still do bulk insertions and bulk deletion in _O(k_+log_S_) time. For every leader, we store pointers between its node in the main tree and its node in the index trees.

## 5.4 Amortized Analysis Potential

We use the accounting method \[6\]: creating a coin or bill takes _O_(1) amortized time, you can spend a coin to do _O_(1) work for free, and spend a bill to gain _O_(1) coins. We have the following money:

• two coins per leader node,<tbc>

• one additional coin per unpromoted leader node, and<tbc>

• one bill per pair of consecutive leaders with height difference 2.

We think it is easier to keep track of money locally. But, for readers that prefer working with potential functions, you may think of the potential function

\(\Phi=(\text{total number of coins})+10^9\cdot(\text{total number of bills}).\)

