<tbc>where a motif refers to a kind of graph pattern (e.g., a triangle). Consequently, in these real-world scenarios, we require DPSS algorithms to identify high-quality local clusters efficiently.

## B Proofs for Section 2 (Preliminaries)

FACT 2.1. _In the d-bit Word RAM model, consider the integer universe U_={0,1_,...,d_-1}_, and a set_ \(I\subseteq U\) _of n integers; there exists a data structure that maintains all the integers in I in a sorted linked list and supports each of the following operations in O_(1) _worst-case time:_

\(\bullet\) _each update (either an insertion of a new integer or a deletion of an existing integer) to I;_<tbc>

\(\bullet\) _finding the predecessor or successor for any integer_ \(q\in U\) _in I._

_Such a data structure consumes O(n_) _space at all times, where n is the current cardinality of I._

PROOF. We provide an implementation to proof Fact 2.1.

**The Data Structure.** The input is a set _I_ of _n_ integers from the universe _U_={0,1_,...,d_-1}. We can construct the following data structure, which includes the following four parts: a bitmap M, a pointer array P, a menu array Q and a sorted linked list L.

\(\bullet\) <u>_The bitmap_</u>M. The bitmap M is a 1 word integer which contains _d_ bits and the _i_-th bit indicates whether the integer _i_ is in _I_.<tbc>

\(\bullet\) <u>The sorted linked list L</u>. A sorted list that contains the integers in _I_.<tbc>

\(\bullet\) <u>The pointer array P.P</u> is a dynamic array with _n_ elements and each element stores the _pointer_ to an integer in L.<tbc>

\(\bullet\) <u>The menu array Q.Q</u> contains _d_ integers and each of the integers is in the range of \[1_,n_\]. For each integer \(i\in I\), the _i_-th element of Q is denoted as Q\[_i_\]. We make sure the Q\[_i_\]-th element of P, i.e. P\[Q\[_i_\]\], stores the pointer to _i_.

**The Construction of the Data Structure.** The above data structure can be constructed in _O(n_) worst case time and in _O(n_) space with the following four steps.

\(\bullet\) <u>_Step 1_</u>. Construct the bitmap M.<tbc>

\(\bullet\) <u>_Step 2_</u>. Initialize Q with all 0 elements. Observe that each integer in Q occupies at most _O_(log_n_) bits of storage and in total Q takes _O_(log_n_) words and can be initialized in _O_(log_n_) time.<tbc>

\(\bullet\) <u>_Step 3_</u>. For each integer, _i_ in _I_ generate a node of the sorted linked list and push back its pointer to P. At the same time, _update_ the menu array Q by setting Q\[_i_\] as the index of _i_-th pointer in P.<tbc>

\(\bullet\) <u>_Step 4_</u>. Link the nodes in order to construct L. Given an integer \(q\in U\), we find its successor, denoted as \(q'\), in _I_ with the following steps:<tbc>

– \(u\leftarrow\mathcal{M}>>q\), which shifts all the lower _q_ bits out;<tbc>

– If _u_=0, report that the successor of _q_ does not exist in _I_;<tbc>

– Otherwise, compute \(q'=q+log_2(u\&\neg(u-1))\);<tbc>

– \(q'\) is the successor of _q_ in _I_. Thus \(\mathcal{P}[\mathcal{Q}[q']]\) stores the pointer of its successor node.

Clearly, the construction algorithm above only takes _O(n_) worst case running time and takes _O(n_) space.

**Maintain the Data Structure with Updates.** Now we consider how to maintain this data structure when an insertion of a new integer or a deletion of an existing integer happens. We first suppose the insertion and deletion does not change the value of \(\lceil log_2n\rceil\), thus we do not need to rebuild Q and P.

<u>_Insertion_</u>. When a new integer _q_ is inserted to _I_, the corresponding bit in M is set as 1. Then build a linked sorted list node of _q_, tail insert its pointer to P and set the the _q_-th element of Q as the index. Then we find the pointer of _q_’s predecessor or successor and insert the node of _q_ to the correct location in the linked list to maintain it to be sorted.

<u>_Deletion_</u>. To delete an existing integer _p_, the pointer of its corresponding linked list node can be found with P\[Q\[_p_\]\] and it can be removed from the sorted linked list. Then the bitmap M can be maintained by setting the corresponding bit as 0. To maintain P and Q, locate the index of the associated element in P, swap it with the element at the end, and then pop out the last pointer from P. When we do the swapping, the pointer that was swapped also needs to have its reference in Q updated. All of the above operations can be done in _O_(1) time.

