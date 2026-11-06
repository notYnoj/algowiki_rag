<tbc>compute a \(\widetilde{O}(1)\)-approximation it suffices to compute an LCS of length 1, which is just a matching pair and can be found in time _O(n_) (assuming that the alphabet is \[_O(n_)\]).

This yields an algorithm that computes a value \(\widetilde{L}\le L\) such that w.h.p. \(\widetilde{L}\ge\widetilde{\Omega}(LT^{0.4}/n^{0.8})\). The algorithm runs in time _O(T_), and this running time bound holds deterministically, i.e., with probability 1. Hence, we proved Theorem 1.

It remains to prove Theorem 9. Our algorithm is a combination of four methods that work well in different regimes of the problem, see Sections 5.1, 5.3, 5.4, and 5.5. We will combine these methods in Section 5.6.

## 5.1 Algorithm 1: Small _L_

Algorithm 1 works well if the LCS is short. It yields the following result.

**Theorem 10** (Algorithm 1)**.** _We can compute in expected time_ \(\widetilde{O}(T)\) _an estimate_ \(\widetilde{L}\le L\) _that w.h.p. satisfies_ \(\widetilde{L}\ge min\{L,\sqrt{LT/n}\}\).

_Proof._ Our Algorithm 1 works as follows.

1. Run Lemma 7 on _x_ and _y_.<tbc>

2. Run Lemma 4 on _x_ and _y_ with \(\beta:=max\{1,\frac{M}{2T}\}\).<tbc>

3. Output the larger of the two common subsequence lengths computed in Steps 1 and 2.

**Running Time:** Step 1 runs in time \(\widetilde{O}(n)=\widetilde{O}(T)\). Step 2 runs in expected time \(\widetilde{O}(n+M/\beta)\). Since \(\beta\ge\frac{M}{2T}\) we have \(M/\beta\le 2T\), so the expected running time is \(\widetilde{O}(n+T)=\widetilde{O}(T)\).

**Upper Bound:** Steps 1 and 2 compute common subsequences, so the computed estimate \(\widetilde{L}\) satisfies \(\widetilde{L}\le L\).

**Approximation Guarantee:** Note that Step 1 guarantees \(\widetilde{L}\ge\frac{M}{2n}\) and Step 2 guarantees w.h.p. \(\widetilde{L}\ge L/\beta\). If \(M\le 2T\) then \(\beta=1\) and \(\widetilde{L}=L\), so we solved the problem exactly. Otherwise we have _M\>_2_T_ and \(\beta=\frac{M}{2T}\), so Step 2 guarantees w.h.p. \(\widetilde{L}\ge 2LT/M\). By multiplying the two guarantees on \(\widetilde{L}\) and taking square roots, we obtain w.h.p.

\(\widetilde{L}\ge\sqrt{\frac{M}{2n}\cdot\frac{2LT}{M}}=\sqrt{\frac{LT}{n}}.\)

It follows that w.h.p. \(\widetilde{L}\ge min\{L,\sqrt{LT/n}\}\).

## 5.2 Block Sequences and Parameter Guessing

This section introduces some general notation and structure for the remaining algorithms.

**Block Sequences:** We split _x_ into substrings _x_<sub>1</sub>_,...,x<sub>n/m</sub>_ of length \(m=n/\sqrt{T}\). Similarly, we split _y_ into _y_<sub>1</sub>_,...,y<sub>n/m</sub>_. A pair \((i,j)\in[n/m]^2\), corresponding to the substrings _x<sub>i</sub>,y<sub>j</sub>_, is called a _block_. For any block we write _M<sub>ij</sub>=M(x<sub>i</sub>,y<sub>j</sub>_) and _L<sub>ij</sub>=L(x<sub>i</sub>,y<sub>j</sub>_). Moreover, we write \((i,j)<(i',j')\) if and only if \(i<i'\) and \(j<j'\). A _block sequence_ is a set S={(_i_<sub>1</sub>_,j_<sub>1</sub>)_,...,(i<sub>k</sub>,j<sub>k</sub>_)} with \(\mathcal{S}\subseteq[n/m]^2\) satisfying the monotonicity property (_i_<sub>1</sub>_,j_<sub>1</sub>)_\<...\<(i<sub>k</sub>,j<sub>k</sub>_). In what follows, every algorithm will compute estimates \(0\le\widetilde{L}_{ij}\le L_{ij}\) and then choose a block sequence S to produce an overall estimate \(\widetilde{L}=\sum_{(i,j)\in\mathcal{S}}\widetilde{L}_{ij}\). Note that this guarantees \(\widetilde{L}\le L\), as the sum \(\sum_{(i,j)\in\mathcal{S}}\widetilde{L}_{ij}\) corresponds to some (block-aligned) common subsequence of _x_ and _y_. In order to get bounds in the other direction, we need to show that there always exists a block sequence of large LCS sum, i.e., a long "block-aligned common subsequence". This is shown by the following lemma.

