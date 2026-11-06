approximation, and we already know that _x_<sup>∗</sup> is a constant right approximation, it follows that in the end we return a constant approximation. The case where the number of elements that compare less is \(\ge i\) is handled symmetrically.

## 3 Preliminaries

In this section, we give some basic definitions and results in the adversarial comparison setting which will serve as the basis for many of our algorithms.

**Definition 3.1.** _Element x<sub>j</sub> in the set X_={_x_<sub>1</sub>_,...,x<sub>n</sub>_} _is of k-order i if there exists a partition S_<sub>1</sub>_,S_<sub>2</sub> _of X_\\{_x<sub>j</sub>_} _such that_ |_S_<sub>1</sub>|=_i_-1_, and_ \(S_2\cup\{x_j\}\ge_kS_1\cup\{x_j\}\).

This the notion of approximate selection that was originally introduced in \[AFHN15\]. We show that this is equivalent to the intuitive notion we previously described, and then show that it is equivalent to something that is easier to work with.

**Lemma 3.2.** _An item x<sub>j</sub> in X is of k-order i if and only if x<sub>j</sub> is a k-approximate i-selection._

_Proof._ Assume _S_<sub>1</sub>_,S_<sub>2</sub> exist as in the definition of _x<sub>j</sub>_ being _k_-order _i_. Then, since \(S_2\cup\{x_j\}\ge_kS_1\cup\{x_j\}\), the concatenation of the sorted order of _S_<sub>1</sub>, _x<sub>j</sub>_, and the sorted order of _S_<sub>2</sub> in that order is a _k_-approximate sorting by definition. Thus, _x<sub>j</sub>_ is a _k_-approximate _i_-selection as desired.

Similarly, assume there exists a _k_-approximate sorting _Y_ of _X_ where _y<sub>i</sub>=x<sub>j</sub>_. Then, taking _S_<sub>1</sub> to be the first _i_-1 elements of _Y_ , and _S_<sub>2</sub> to be the final _n-i_ elements, it follows by definition that \(S_2\cup\{x_j\}\ge_kS_1\cup\{x_j\}\). Thus, _x<sub>j</sub>_ is of _k_-order _i_ as desired.

**Lemma 3.3.** _An item x<sub>j</sub> in X is a k-approximate i-selection if and only if_ \(|x_j-x_i|\le k\) _where x<sub>i</sub> is the actual i-th smallest element of X._

_Proof._ Consider some _k_-approximate sorting _Y_ of _X_ where _y<sub>i</sub>=x<sub>j</sub>_. Without loss of generality, assume \(x_j\le x_i\). Since _x<sub>i</sub>_ is the _i_th smallest element of _X_, there must be at least _n-i_+1 elements of _X_ that are \(\ge x_i\). Thus, there must exist some element \(x_\ell\ge x_i\) that is to the left of _x<sub>j</sub>_ in _Y_ since there are only _n-i_ places to the right that they can be. It follows that \(x_j\ge_kx_\ell\), which implies \(x_j\ge_kx_i\) since \(x_\ell\ge x_i\). Thus, \(x_i\ge x_j\ge x_i-k\), so \(|x_j-x_i|\le k\).

Consider some element _x<sub>j</sub>_ in _X_ such that \(|x_j-x_i|\le k\). Let _Y_ be the sorted order of _X_, but with _x<sub>j</sub>_ and _x<sub>i</sub>_ swapped. All pairs that do not contain _x<sub>i</sub>_ or _x<sub>j</sub>_ must still be in the right order. Pairs \((x_i,x_\ell)\) that are in the wrong order must have \(x_\ell\) between _x<sub>i</sub>_ and _x<sub>j</sub>_ (or equal to _x<sub>j</sub>_), so \(x_\ell\) and _x<sub>i</sub>_ must differ by at most _k_. An identical argument applies to pairs \((x_j,x_\ell)\), so it follows that _Y_ is a _k_-approximate sorting as desired.

**Corollary 3.4.** _If Y is a k-approximate sorting of X, and S is the actual sorting of X,_ \(|y_i-s_i|\le k\) _for all i._

We define the notion of a _gap-preserving_ algorithm, where elements must be correctly sorted with respect to a gap of size 1. This will be useful in proving the correctness of our later algorithms.

**Definition 3.5.** _We say a sorting algorithm is_ gap-preserving _if, given there exists a gap of length_ 1 _in the input, the sorting algorithm returns all elements before the gap before all elements after the gap. Formally, given input X such that there exists a gap_ \([y,y+1)\) _where_ \(X\cap[y,y+1)=\emptyset\)_, the sorting algorithm must return all elements of X less than y before all elements of X greater than y._

