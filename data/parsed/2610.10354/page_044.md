## 6.1 Min-Max Convolution

**Theorem 1.9** (Min-Max Convolution)**.** _Min-Max Convolution cannot be solved in time_ \(O(n^{3/2-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong Min-Plus Convolution Hypothesis fails._

**Proof.** Suppose Min-Max Convolution can be solved in \(O(n^{3/2-\epsilon})\) time for some \(\epsilon>0\) by an algorithm A. In order to show this contradicts the Strong Min-Plus Convolution Hypothesis, by Corollary 5.2 with \(\gamma=\frac{1}{2}\), it suffices to give a truly sub-quadratic time algorithm for Min-Plus Convolution instances (_A,B_) where the elements are from \([\sqrt{n}]\) while we need to list up to \(\sqrt{n}\) witnesses per output.

Because the universe is \([\sqrt{n}]\), _C=A∗B_ can be computed in \(\widetilde{O}(n^{1.5})\) time. By Lemma 6.1, we can further assume every non-\(\perp\) value in _B_ appears at most \(n^{1/2+\epsilon/3}\) times.

For every \(b\in[\sqrt{n}]\), we define a Min-Max Convolution instance (_A<sub>b</sub>,B<sub>b</sub>_), where _A<sub>b</sub>_\[_i_\]=_A_\[_i_\] for every \(i\in[0,n]\), and \(B_b[j]=-\infty\) if _B_\[_j_\]=_b_ and \(B_b[j]=\infty\) otherwise. Let _C<sub>b</sub>_=Min-Max(_A<sub>b</sub>,B<sub>b</sub>_). It is not difficult to see that, (_i,j_) is a witness for _C_\[_k_\] (i.e., _A_\[_i_\]+_B_\[_j_\]=_C_\[_k_\] and _i+j=k_), if and only if for some _b_, _C<sub>b</sub>_\[_k_\]=_C_\[_k_\]-_b_ and (_i,j_) is a witness for _C<sub>b</sub>_\[_k_\] in the Min-Max Convolution instance defined for _b_.

Consider the following algorithm. We enumerate \(b\in[\sqrt{n}]\), create _A<sub>b</sub>_ and _B<sub>b</sub>_, and compute _C<sub>b</sub>_=Min-Max(_A<sub>b</sub>,B<sub>b</sub>_) using A in \(O(n^{1.5-\epsilon})\) time per _b_. By standard sampling-based approaches (Lemma 2.14), we can further list \(n^{2\epsilon/3}\) witnesses for every _C<sub>b</sub>_\[_k_\] in \(\widetilde{O}(n^{1.5-\epsilon/3})\) time using A as a black-box. This step takes \(\widetilde{O}(\sqrt{n}\cdot n^{1.5-\epsilon/3})=\widetilde{O}(n^{2-\epsilon/3})\) time over all \(b\in[\sqrt{n}]\).

What remains to consider are those _C<sub>b</sub>_\[_k_\] that have more than \(n^{2\epsilon/3}\) witnesses and _C<sub>b</sub>_\[_k_\]=_C_\[_k_\]-_b_. We call such a pair (_b,k_) heavy. For a heavy pair, we enumerate all elements in \(S_b:=\{j\in[n]:B[j]=b\}\) (this can be done in _O_(|_S<sub>b</sub>_|) time by computing these sets in preprocessing), and check whether each \(j\in S_b\) forms a witness for _C<sub>b</sub>_\[_k_\]. Recall each value in _B_ appears at most \(n^{1/2+\epsilon/3}\) time, so the cost for each heavy pair is \(O(n^{1/2+\epsilon/3})\). Since we only need to list up to _n_<sup>1/2</sup> witness per _C_\[_k_\], we only need to resolve \(n^{1/2-2\epsilon/3}\) heavy pairs for a particular value of _k_ before we find enough witnesses for _C_\[_k_\]. Hence, we only need to handle \(O(n^{3/2-2\epsilon/3})\) heavy pairs in total, and thus the overall running time for this case is \(O(n^{2-\epsilon/3})\).

## 6.2 Min-Equality Convolution

**Theorem 1.10** (Min-Equality Convolution)**.** _Min-Equality Convolution cannot be solved in time_ \(O(n^{3/2-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong Min-Plus Convolution Hypothesis fails._

**Proof.** Suppose Min-Equality Convolution can be solved in \(O(n^{3/2-\epsilon})\) time for some \(\epsilon>0\) by an algorithm A. Similar as before, it suffices to give a truly sub-quadratic time algorithm for Min-Plus Convolution Listing instances (_A,B_) where the elements are from \([\sqrt{n}]\) while we need to list up to \(\sqrt{n}\) witnesses per output.

We can compute _C=A∗B_ in \(\widetilde{O}(n^{1.5})\) time and we can further assume every non-\(\perp\) value in _B_ appears at most \(n^{1/2+\epsilon/3}\) time by Lemma 6.1.

For every \(\Delta\in\{-\sqrt{n},\dots,\sqrt{n}\}\), we define a Min-Equality Convolution instance \((A_\Delta,B_\Delta)\), where \(A_\Delta[i]=A[i]+\Delta\) for every \(i\in[0,n]\) and \(B_\Delta=B\). Intuitively, we aim to use \(\Delta\) to represent _B_\[_j_\]-_A_\[_i_\]. Let \(C_\Delta=\text{Min-Equal}(A_\Delta,B_\Delta)\). The following claim shows how the witnesses in the Min-Equality Convolution instance \((A_\Delta,B_\Delta)\) are related to the witnesses in the Min-Plus Convolution instance (_A,B_).

