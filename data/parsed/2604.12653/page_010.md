then we also have the sorted order of _X-P_ since \(X-P\subseteq Y\) . Thus, by Lemma 7 we can sort _X_ in _O_(log_e(G_)) time.

Using Theorem 11, we show that Theorem 4 implies Theorem 5.

_Proof._ We first check whether _m\<n/_3. If so, then we ignore _G_ and sort _X_ from scratch with merge sort. Thus, we may now assume that \(m\in\Omega(n)\). Given the DAG _G_ on _X_, we apply Theorem 11 to obtain a DAG _H_ on a subset \(Y\subseteq X\). We run `UniTopSort`(_Y,H_) to obtain the sorted order on _Y_ . Finally, we use the sorting phase of Theorem 11 to get the sorted order on _X_.

We first check that this is a correct algorithm: Let _L_ be a linear order compatible with _G_. By Theorem 11, the restriction of _L_ to _Y_ is compatible with _H_. Thus, (_Y,H_) is a valid input for `UniTopSort` and we sort _Y_ correctly. Then, Theorem 11 computes the sorted order of _X_.

Next, we analyze the running time: If _m\<n/_3, there are at least _n/_3 items not incident to any edges in _G_, so \(loge(G)\in\Theta(nlogn)\). We spend _O(m_) preprocessing time and _O(n_log_n_)=_O_(log_e(G_)) sorting time in this case. Assume now that \(m\in\Omega(n)\) and let \(n',m'\) denote the number of vertices and edges of _H_. During preprocessing, Theorem 11 spends _O(n+m_)=_O(m_) time and `UniTopSort` spends \(O(n'+m')=O(m)\) time. During sorting, `UniTopSort` spends \(O(n'+loge(H))=O(loge(G))\) time, and Theorem 11 spends _O_(log_e(G_)) time. Thus, we obtain an algorithm with _O(m_) preprocessing and _O_(log_e(G_)) sorting time. This shows Theorem 5.

## 5 Heaps with the Unified Bound

In this section, we show Theorem 2 and design a heap with the unified bound (Definition 1). We achieve this by maintaining a tree where each leaf stores an item, every node stores its subtree minimum (a pointer to the smallest item in its subtree), and where the depth of each leaf is bounded by a function that looks like the unified bound. To this end, consider _n_ leaves numbered 1_,...,n_ and let _t_ be a time counter that starts at 0. Every leaf _i_ has a last access time _s(i)\<t_. We define \(d(i):=1+min_{1\le j\le n}(log(1+|i-j|)+log(1+t-s(j)))\). In this section, we show:

**Theorem 12.** _There is a data structure that maintains a rooted binary tree on top of n leaves numbered_ 1_,...,n that each store an item, such that each node in the tree stores its subtree minimum and every leaf i has depth O(d(i_))_. The data structure supports the operations:_

• addLeaf(_x): In amortized O_(1) _time, increment n and add a new leaf with index n, value x, and_ \(s(n)=-\infty\).<tbc>

• access(_i): In amortized O(d(i_)) _time (computed before the operation), set s(i_)=_t and then increment t. For the very first access operation, d(i_) _is ill-defined, so we require a bound of amortized O_(1) _time instead._<tbc>

• changeKey(_i,x): In O(d(i_)) _time, replace the item stored at leaf i with x._

_The data structure may remodel the internal tree nodes arbitrarily (within the allowed time bounds). The leaves do_ not _need to be stored in order._

But first, we show how Theorem 12 yields a heap with the unified bound (in the sense of Definition 1): Suppose that Theorem 12 is true and let _T_ be the data structure that maintains a rooted tree. For every insert(_x_) operation, we call T.addLeaf(_x_). For every extractMin() operation, we look at the subtree minimum of the root of _T_ to determine the leaf _i_ that contains the current minimum item _x_. We call T.access(_i_) and then T.changeKey\((i,\infty)\) where \(\infty\) is a dummy<tbc>

