**Definition 13.** A _weighted soft heap (WSH)_ stores a set _X_ of elements. Like in a soft heap, each element \(x\in X\) is associated with a fixed key key(_x_), provided by the user. The WSH additionally maintains a bit _x._`wsh-corr` indicating whether _x_ is corrupted, and a positive integer _x._`weight` for each \(x\in X\). The following operations are supported

• `insert`(_x,w_) inserts the element _x_, and sets _x._`wsh-corr`=0 and _x._`weight`=_w_.<tbc>

• `find-min` and `delete` are identical to their classical soft heap counterparts. None of these operation change the weight of any element.<tbc>

• `increase-weight`(_x,w_) increases _x._`weight` by a positive integer _w_. If _x_ was corrupted before, it becomes _uncorrupted_ again.

The WSH is again initialized with an _error parameter_ \(\varepsilon\). The corruption invariant is as follows. Let _m_ be the number of `insert` operations so far, let _W_<sub>corrupted</sub> be the sum of weights of corrupted elements currently in the soft heap, and let _W_<sub>deleted</sub> be the sum of weights of deleted elements at the time of their deletion. Then we always have

\(W_\mathrm{corrupted}\le\varepsilon(m+W_\mathrm{deleted}).\)

**Theorem 14.** _Weighted soft heaps can be implemented with amortized time_ \(\mathcal{O}(w\cdot\mathrm{log}\frac{1}{\varepsilon})\) _for_ `delete`_, where w is the weight of the deleted element, and_ O(1) _amortized time for all other operations. The amortized number of comparisons performed by_ `increase-weight` _is zero._

Before proving theorem 14, observe that it strictly generalizes lemma 12. Indeed, if all weights are one, then the running times are as for classical soft heaps, and the invariant simplifies to \(|C|\le\varepsilon(m+|D|)\), where _C_ is the set of currently corrupted and _D_ is the set of deleted elements. Since each deleted element must have been inserted at some point, this implies \(|C|\le 2\varepsilon m\). By halving \(\varepsilon\), we recover the classical soft heap guarantee without changing asymptotic running times.

We now proceed with the proof of theorem 14. The WSH internally uses a classical soft heap _H_ with error parameter \(\varepsilon'=\frac{\varepsilon}{1+\varepsilon}\). This heap will contain every element currently in the WSH, but additionally some _copies_ of elements. Each copy _x_ of an element _y_ stores a pointer _x._`orig`=_y_. For the WSH element _y_, we say _y._`orig`=_y_. We also store the number of copies for every WSH element _y_ as _y._`copies` (_y_ itself is included in the count).

Note that a WSH element may be marked as corrupted within _H_, but that does not necessarily mean the WSH considers it corrupted. To avoid confusion, the internal soft heap _H_ uses the field _x._`corr` to manage corruption, and the WSH uses the field _x._`wsh-corr`.

An operation `insert`(_x,w_) calls \(x\leftarrow H.\text{\texttt{insert}}(x)\), and then sets \(x.\text{\texttt{weight}}\leftarrow w\), and moreover \(x.\text{\texttt{wsh-corr}}\leftarrow 0\), \(x.\text{\texttt{orig}}\leftarrow x\), and \(x.\text{\texttt{copies}}\leftarrow 1\). For `find-min`, we first call \(x\leftarrow H.\text{\texttt{find-min}}()\), and then return _x._`orig`.

The main interesting operation is `delete`(_x_). It calls _H._`delete`(_y_) for each element _y_ in _H_ with _y._`orig`=_x_. Note that this includes _x_ itself. Each of these `delete` calls returns a set of newly corrupted elements. Let _C_ be the union of these sets. We now determine which WSH elements should be actually marked and reported as corrupted. Do the following for<tbc>

