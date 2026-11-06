## 5 Complexity of the Batched Predecessor problem: Lower Bounds

In this section, we prove the lower bounds for the PLE(_S,L_) problem in the following theorem:

**Theorem 8** (**PLE Lower Bound**)**.**

\(\mathrm{PLE}\left(S,L\right)=\Omega\left(\mathrm{min}\left\{\frac{kw}{B}\mathrm{log}_MS+\frac{L}{B}\mathrm{log}_Mk,\frac{k}{B}\mathrm{log}S+\frac{L}{wB}\mathrm{log}k+\frac{L}{B}\right\}\right).\)

In order to prove Theorem 8, first divide the PLE(_S,L_) problem further into three subproblems. Doing this helps us develop a more intricate adversarial analysis that gives us tight lower bounds. We then develop matching upper bounds on the PLE(_S,L_) problem. We consider the following three subproblems of PLE, whose complexities lower bound the complexity of PLE, and hence Sort(_S,L_):

1. _S-k_: An instance with only _one large element_ in each large-element stripe.<tbc>

• Input: Set _S_ of unit-sized elements _s_<sub>1</sub>_,...,s<sub>S</sub> (sorted)_, where \(s_1=-\infty\) and \(s_S=\infty\), and large elements \(\ell_1,\dots,\ell_k\) (volume _kw_) _unsorted_.<tbc>

• Output: For each \(\ell_i\) output _s<sub>j</sub>_ such that \(s_j\le\ell_i\le s_{j+1}\). It is guaranteed that no other \(\ell_k\) satisfies \(s_j\le\ell_k\le s_{j+1}\) (one large element per stripe).<tbc>

2. _k-_\(\tilde{k}\): An instance with only _one small element_ in each small-element stripe.<tbc>

• Input: Unit-sized elements _s_<sub>1</sub>_,...,s_<sub>_k_+1</sub> _sorted_, where \(s_1=-\infty\) and \(s_{k+1}=\infty\), and large elements \(\ell_1,\dots,\ell_\tilde{k}\) (volume \(\tilde{kw}\)) _un sorted_.<tbc>

• Output: For each \(\ell_i\), output its predecessor and successor in _S_.<tbc>

3. _k-k_: An instance with only _one element in each stripe_, large or small.<tbc>

• Input: Unit-sized elements _s_<sub>1</sub>_,...,s_<sub>_k_+1</sub> _sorted_, where \(s_1=-\infty\) and \(s_{k+1}=\infty\), and large elements \(\ell_1,\dots,\ell_k\) (volume _kw_) _un sorted_.<tbc>

• Output: The entire set in the sorted order.

The format of lower bounds for _S-k_, _k-_\(\tilde{k}\) and _k-k_ is as follows: let _X_ be the logarithm of the total number of permutations that an algorithm needs to achieve in order to solve the problem. As is easily observed, the values of _X_ for these three subproblems are _k_log(_S/k_), \(\tilde{k}\mathrm{log}k\), and _k_log_k_, respectively. Lemma 9 below is the most technical part of this paper, and<tbc>

