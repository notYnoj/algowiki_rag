**Theorem 5.3** (**FindDominant** algorithm)**.** _Suppose that n\>_2<sup>_k_+7</sup> _and moreover n is a power of_ 2_. Let A be an array containing n elements each with a k-bit key, and suppose that A is_ (1-2<sup>-8_k_</sup>)_- uniform. There is a deterministic, oblivious algorithm that can correctly identify the dominant key given any such A; and moreover, the algorithm requires O(n_) _total work and O(k_+log_n_) _depth._

_Proof._ Let _K_:=2_<sup>k</sup>_. We can call **FindDominant**(_A,K,n_) which is defined below -- since _n\>_2<sup>_k_+7</sup> and _n_ is a power of 2, one can verify that every recursive call to **FindDominant**(_B,K,n_) will have an input _B_ whose size is a multiple of 8.

Henceforth, any element whose key differs from the dominant key is said to be a minority element. In the above algorithm, for each column, if we want to make sure that both median elements are minority, we must consume at least 5 minority elements. If we want to make sure that one of the two median elements is minority, we must consume at least 4 minority elements.

Suppose that _B_ is \((1-\mu)\)-uniform. In the array \(\{(a_i,b_i)\}_{i\in[||B|/8]}\), the number of elements that are minority is upper bounded by \(\frac{2\mu\cdot|B|}{5}\) ; the fraction of elements that are minority is upper bounded by<tbc>

\(\frac{2\mu\cdot|B|/5}{|B|/4}=8\mu/5\)

<tbc>After \(D:=\lceil log_4K\rceil\) recursive calls, the algorithm will encounter the base case, invoke **SlowSort** and output the median. At this moment, the fraction of minority elements is upper bounded by

\(2^{-8k}\cdot\left(\frac{8}{5}\right)^D\le 1/2\)

Therefore, outputting the median at this moment will give the correct result.

## 5.3 Sorting a Nearly Orderly Array

Recall that using a nearly ordered segmenter (see Section 3) to partially sort the input array, such that the result is \((\eta,p)\)-nearly ordered. We will show that there is an efficient oblivious algorithm that can correct the remaining errors and fully sort the array.

**Theorem 5.4.** _Suppose that n\>_2<sup>4_k_+7</sup>_. There is a deterministic, oblivious algorithm that fully sorts an_ (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)_-orderly array in O(n_) _total work and O_(log_n_) _depth._

**Proof of Theorem 5.4:** We consider the following algorithm.

