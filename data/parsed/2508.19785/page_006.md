We say that the elements in _S_ are subject to persistent random comparison faults (or errors) with probability at most _p_ (resp. at least _q_) if \(p_{\{x,y\}}\le p\) (resp. \(p_{\{x,y\}}\ge q\)) for all pairs {_x,y_}. Throughout the paper, _q_ and _p_ will be some constants with \(0\le q\le p<\frac{1}{2}\), and we might impose further constraints on the range of allowed values.

An algorithm that approximately sorts _S_ takes as input a sequence of the elements in _S_ and outputs an "approximately sorted" sequence \(S'\), i.e., permutation of the input sequence, while only performing noisy comparisons. Each comparison requires constant time, and the goal is that of _quickly_ computing a sequence _S_ with small dislocation. Notice that, in general, the order in which the elements appear in the input permutation of _S_ might depend on the comparison errors, i.e., one can imagine the following process: all the comparison errors between distinct pairs of elements are randomly decided a-priori (independently and according to the probabilities described above), then an adversary is given access to the elements in _S_, to their true order, and to all the noisy outcomes of the comparisons, and chooses the input sequence to be used by the algorithm.

_Our error model for approximate noisy binary searching._ As discussed in the introduction, we also consider the problem of estimating the rank rank(_x,S_) of an element _x_ in an input sequence _S_ that satisfies \(\text{disl}(S)\le d\), where _d_ is an integer input parameter.

In this problem, only comparisons between _x_ and the elements in _S_ are allowed, and these comparisons are noisy: errors occur with probability at most _p_ for some constant \(p\in[0,\frac{1}{2})\), errors are independent, and the comparison outcomes are persistent. Here, the order of the elements in the sequence _S_ cannot depend on the comparison errors between _x_ and the elements in _S_.

## 3 Our Sorting Algorithm

In this section, we design an algorithm that approximately sorts an input sequence _S_ of _n_ elements subject to persistent random comparison faults with probability at least _q_ and at most _p_ with \(p\le\frac{9q+1}{8q+11}\). The algorithm uses _O(n_log_n_) worst-case time, which is asymptotically optimal, and returns a permutation of _S_ having maximum dislocation _O_(log_n_) and total dislocation _O(n_), with high probability. For the case _q=_0, i.e., when no lower bound on the error probability is known, the above condition becomes \(p<\frac{1}{11}\), while for the case _p=q_, which is the one that has been considered in [10, 19, 23], the algorithm can handle any constant \(p<\frac{1}{4}\).

To some extent, the flavor of our algorithm is a mixture of _Insertion Sort_ and _Merge Sort_. On the one hand, our algorithm extends a partially sorted sequence by finding the (approximate) ranks of new elements and inserting them in the computed positions; on the other hand, our algorithm inserts such elements in batches so that the size of the intermediate sequences doubles at each iteration. Due to the persistent comparison faults, it is not possible to guarantee that these intermediate sequences will be correctly sorted. Instead, our algorithm ensures that such sequences are kept approximately sorted w.h.p. More precisely, since inserting a batch of elements causes the dislocation of the sequence to increase multiplicatively, we counteract this effect by post-processing the resulting sequence.

In order to implement our algorithm, we answer the following three key questions:

(1) How do we quickly find an approximate rank of a new element to be inserted in an approximately sorted sequence?<tbc>

(2) How do we bound the increase in dislocation resulting from simultaneously inserting a batch of elements in an approximately sorted sequence?<tbc>

(3) How can the sequence resulting from inserting a batch of elements be post-processed to counteract the increase in dislocation?<tbc>

