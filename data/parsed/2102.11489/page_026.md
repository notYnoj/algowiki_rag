**Comparator.** A _k_-bit comparator takes two values each of _k_ bits, and outputs an answer from a constant-sized result set such as {_\>,\<,_=}, or \(\{\ge,<\}\), or \(\{\le,>\}\). Note that the outcome can be expressed as 1 to 2 bits.

**Fact 6.2.** _A k-bit comparator can be implemented with a circuit with O(k_) _generalized boolean gates and O_(log_k_) _depth._

**Delayed-carry representation and shallow addition.** Adding two \(\ell\)-bit numbers in binary representation takes \(O(log\ell)\) depth. We will later need adders that are constant in depth. To do this, we can use a Wallace-tree-like trick and adopt a delayed-carry representation of numbers.

We represent an \(\ell\)-bit number _v_ as the addition of two \(\ell\)-bit numbers, i.e., _v_:=_x+y_. Here, it must be that the sum \(x+y\le 2^\ell-1\) can still be presented as \(\ell\)-bits; moreover, the delayed-carry representation of _v_ is not unique. Given two \(\ell\)-bit numbers _v_<sub>1</sub>:=_x_<sub>1</sub>+_y_<sub>1</sub> and _v_<sub>2</sub>:=_x_<sub>2</sub>+_y_<sub>2</sub> in this delayed-carry representation, we can compute the \((\ell+1)\)-bit number _v_<sub>1</sub>+_v_<sub>2</sub> as follows where the answer is also in delayed-carry representation:

1. Compute a delayed-carry representation of _x_<sub>1</sub>+_y_<sub>1</sub>+_x_<sub>2</sub>, and let the result be \(x'+y'\). This can be done by summing up the _i_-th bit of _x_<sub>1</sub>, _y_<sub>1</sub>, and _x_<sub>2</sub> respectively, for each \(i\in[\ell]\). For each \(i\in[\ell]\), the sum of the three bits can be expressed as a 2-bit number, where the first bit becomes the _i_-th bit of \(x'\) and the other bit becomes the (_i_+1)-st bit of \(y'\).<tbc>

2. Now, using the same method, compute and output a delayed-carry representation of \(x'+y'+y_2\).

The above can be accomplished with \(O(\ell)\) generalized boolean gates and in _O_(1) depth. Henceforth this is called a _shallow addition_.

**Counting.** We will need a simple circuit gadget that counts the number of 1s in an input array containing _n_ bits.

**Fact 6.3.** _Given an input array containing n bits, counting the number of 1s in the input array can be realized with a circuit of size O(n_) _and depth O_(log_n_).

_Proof._ We can use the algorithm in Fact 4.3 of Asharov et al. [ALS21], but use the delayed-carry representation of numbers, and replace all adders with shallow adders. Essentially, the numbers are added over a binary tree, where in the leaf level (also called the last level), every number is promised to be at most 1-bit long; in the second to last level, every number is promised to be at most 2-bit long; and so on. In this way, the total circuit size for the entire tree of adders is _O(n_). At the end of the algorithm, we perform a final addition to convert the delayed-carry representation of the answer to a binary representation.

**All prefix sums.** We consider an all-prefix-sum circuit gadget, which upon receiving an input _A_ containing _n_ non-negative integers, outputs the sums of all _n_ prefixes, that is, _A_\[:1\]_,A_\[:2\]_,A_\[:3\]_,...,A_\[:_n_\]. It is promised that the sum of the entire array _A_ can be stored in \(\ell\) bits.

**Fact 6.4.** _For any_ \(\ell\le n\)_, there is a circuit composed of at most_ \(O(n\ell)\) _generalized boolean gates and of depth O_(log_n_) _that solves the aforementioned all-prefix-sum problem._

_Proof._ We can use the standard prefix sum algorithm, but represent all numbers using the delayed- carry representation, and use shallow addition which can be computed in constant depth.

