of the same key and delete arbitrary elements. Also, we avoid defining current/internal keys explicitly.

In the following, let U denotes a universe of values that can only be accessed via comparisons; these are the _keys_. For technical reasons, the soft heap does not contain keys themselves, instead, it contains _elements_. Elements can be arbitrary objects given by the user. The only condition is that every element _x_ is associated with a fixed key key(_x_), and that the soft heap implementation may associate additional data to _x_. For now, this additional data will be a single corruption bit _x._`corr`.

**Definition 11.** A _soft heap_ stores a set _X_ of distinct elements. Each element \(x\in X\) is associated with a fixed key key(_x_). The soft heap additionally uses a bit _x._`corr` indicating that _x_ is _uncorrupted_ (_x._`corr`=0) or _corrupted_ (_x._`corr`=1). It supports the following operations:

• `insert`(_x_) inserts an element _x_ into _X_, and sets _x._`corr`=0.<tbc>

• \(\mathtt{find-min}()\rightarrow x\) returns some element _x_ such that \(\mathtt{key}(x)\le\mathtt{key}(y)\) for each uncorrupted element \(y\in X\).<tbc>

• \(\mathtt{delete}(x)\rightarrow C\). Removes the element _x_. Then, the implementation chooses some set \(C\subseteq X\) of _uncorrupted_ elements, corrupts them, and returns _C_.

The soft heap is initialized with an _error parameter_ \(\varepsilon\), and always satisfies the following invariant: The number of corrupted elements currently in the soft heap is at most \(\varepsilon\cdot m\), where _m_ is the number of `insert` operations performed so far.

Observe that the usual `extract-min`() function can be simulated with `delete`(`find-min`()). Soft heaps usually also implement a `meld` function to merge two soft heaps, which we do not need here.

**Lemma 12** (\[Cha00, KTZ13, KKZZ18\])**.** _Soft heaps can be implemented with amortized running time_ \(\mathcal{O}(log\frac{1}{\varepsilon})\) _for_ `delete`_, and_ O(1) _for all other operations._

_Proof._ The implementation of Kaplan, Tarjan, and Zwick \[KTZ13\] is suitable for our specification, although a clarification is needed. Their implementation defines corruption as increasing the key of an element arbitrarily, and `find-min` returns an element _x_ with smallest _current_ key. The original key of _x_ is no larger than the current key of _x_ by definition, and the current key of _x_ is no larger than the original key of every other uncorrupted element in the soft heap. Thus, our specification is satisfied.

We now define the novel _weighted soft heap_ data structure. As mentioned in the introduction, the idea is to give the user more control over which elements are corrupted, by assigning a _weight_ \(x.\mathtt{weight}\in\mathbb{N}_+\) to each element _x_. Elements with higher weight are, in a certain sense, less likely to become corrupted. In the following, if _Y_ is a set of elements, we write \(W(Y)=\sum_{y\in Y}w(y)\) for brevity.

