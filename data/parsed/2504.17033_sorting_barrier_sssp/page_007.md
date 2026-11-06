**Batch Prepend** _Insert L key/value pairs such that each value in L is smaller than any value currently in the data structure, in amortized_ \(O(L\cdot\mathrm{max}\{1,\mathrm{log}(L/M)\})\) _time. If there are multiple pairs with the same key, keep the one with the smallest value._

**Pull** _Return a subset_ \(S'\) _of keys where_ \(|S'|\le M\) _associated with the smallest_ \(|S'|\) _values and an upper bound x that separates_ \(S'\) _from the remaining values in the data structure, in amortized_ \(O(|S'|)\) _time. Specifically, if there are no remaining values, x should be B. Otherwise, x should satisfy_ \(\mathrm{max}(S')<x\le\mathrm{min}(D)\) _where D is the set of elements in the data structure after the pull operation._

_Proof._ We introduce a block-based linked list data structure to support the required operations efficiently.

Specifically, the data is organized into two sequences of blocks, D<sub>0</sub> and D<sub>1</sub>. D<sub>0</sub> only maintains elements from batch prepends while D<sub>1</sub> maintains elements from insert operations, so every single inserted element is always inserted to D<sub>1</sub>. Each block is a linked list containing at most _M_ key/value pairs. The number of blocks in D<sub>1</sub> is bounded by _O_(max{1_,N/M_}), while D<sub>0</sub> does not have such a requirement. Blocks are maintained in the sorted order according to their values, that is, for any two key/value pairs \(\langle a_1,b_1\rangle\in B_i\) and \(\langle a_2,b_2\rangle\in B_j\) , where _B<sub>i</sub>_ and _B<sub>j</sub>_ are the _i_-th and _j_-th blocks from a block sequence, respectively, and _i\<j_, we have \(b_1\le b_2\). For each block in D<sub>1</sub>, we maintain an upper bound for its elements, so that the upper bound for a block is no more than any value in the next block. We adopt a self-balancing binary search tree (e.g. Red-Black Tree \[GS78\]) to dynamically maintain these upper bounds, with _O_(max{1,log(_N/M_)}) search/update time.

For cases where multiple pairs with the same key are added, we record the status of each key and the associated value. If the new pair has a smaller value, we first delete the old pair then insert the new one, ensuring that only the most advantageous pair is retained for each key.

For the operations required in Lemma 3.3:

Initialize(_M,B_) Initialize D<sub>0</sub> with an empty sequence and D<sub>1</sub> with a single empty block with upper bound _B_. Set the parameter _M_.

Delete(_a,b_) To delete the key/value pair \(\langle a,b\rangle\), we remove it directly from the linked list, which can be done in _O_(1) time. Note that it’s unnecessary to update the upper bounds of blocks after a deletion. However, if a block in D<sub>1</sub> becomes empty after deletion, we need to remove its upper bound in the binary search tree in _O_(max{1,log(_N/M_)}) time. Since Insert takes _O_(max{1,log(_N/M_)}) time for D<sub>1</sub>, deletion time will be amortized to insertion time with no extra cost.

Insert(_a,b_) To insert a key/value pair \(\langle a,b\rangle\), we first check the existence of its key _a_. If _a_ already exists, we delete original pair \(\langle a,b'\rangle\) and insert new pair \(\langle a,b\rangle\) only when \(b<b'\).

Then we insert \(\langle a,b\rangle\) to D<sub>1</sub>. We first locate the appropriate block for it, which is the block with the smallest upper bound greater than or equal to _b_, using binary search (via the binary search tree) on the block sequence. \(\langle a,b\rangle\) is then added to the corresponding linked list in _O_(1) time. Given that the number of blocks in D<sub>1</sub> is _O_(max{1_,N/M_}), as we will establish later, the total time complexity for a single insertion is _O_(max{1,log(_N/M_)}).

After an insertion, the size of the block may increase, and if it exceeds the size limit _M_, a split operation will be triggered.

Split When a block in D<sub>1</sub> exceeds _M_ elements, we perform a split. First, we identify the median element within the block in _O(M_) time \[BFP<sup>+</sup>73\], partitioning the elements into two new blocks each with at most \(\lceil M/2\rceil\) elements -- elements smaller than the median are placed in the first block, while the rest are placed in the second. This split ensures that each new block retains about \(\lceil M/2\rceil\) elements while preserving inter-block ordering, so the number of blocks in D<sub>1</sub> is bounded by _O(N/M_). (Every block<tbc>

