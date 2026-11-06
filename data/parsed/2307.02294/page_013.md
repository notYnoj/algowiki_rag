<tbc>suppose \(i\ge 2\), \(t\ge 4\).

\(2\mu_{i,t-1}+2C_k\mu_{i,t-2}+2\mu_{i-1,t}+C'_k\)<br>
\(\le 2(2C+3i)^{t-3}(2^i-1)+2C(2C+3i)^{t-4}(2^i-1)+2(2C+3(i-1))^{t-2}(2^{i-1}-1)+C\)<br>
\(\le(2C+3i)^{t-2}(2^i-1)\left(\frac{2}{2C+3i}+\frac{2C}{(2C+3i)^2}+1-\frac{3}{2C+3i}\right)\)<br>
\(\le(2C+3i)^{t-2}(2^i-1)\left(\frac{2}{2C+3i}+\frac{1}{2C+3i}+1-\frac{3}{2C+3i}\right)\)<br>
\(\le(2C+3i)^{t-2}(2^i-1)=\mu_{i,t}.\)

The first inequality is from the inductive hypothesis and \(C_k\le C'_k\le C\). The second inequality follows from \((2C+3(i-1))^{t-2}\le(2C+3i)^{t-2}-3(2C+3i)^{t-3}\). This completes the induction.

_Proof of Theorem 1.3._ Let _A_ be a _Q_-free \(n\times m\) matrix and _t=c_=3_k_. Take _i_ to be minimal such that for \(j=max\{3,\lceil n/m\rceil^{1/t}\}\), \(m\le(a_{i,j})^c\). It is tedious, but straightforward, to show that \(i=\alpha(n,m)\pm O(1)\). Lemma 3.4 bounds the number of 1s in _A_ by

\(\mu_{i,t}(n+(cj)^{t-3}(2k-1)m)=\mu_{i,t}\left(n+2^{O(klogk)}n\right)(cj)^{t-3}<2^{O(klogk)}(n/m)\)<br>
\(=n\cdot 2^{O(klogk)}\cdot(2C+3i)^{t-2}2^i\)<br>
\(=n\cdot\left(2^{O(k^2)}+O(i)^{3k-2}\right)2^iC=2^{O(k)};\text{see Theorem 2.1}\)<br>
\(=n\cdot 2^{O(k^2)+(1+o(1))\alpha(n,m)}.\)

## 4 Lower Bounds on 0-1 Matrices via Sequences

### Blocked Sequences and 0-1 Matrices.

If _S_ is a sequence, let |_S_| be its length and ∥_S_∥ the size of its alphabet \(|\Sigma(S)|\). A _block_ is a contiguous sequence of distinct symbols. If _S_ is understood to be partitioned into blocks, \(\unknown S\unknown\) is the number of blocks. Regardless of \(\Sigma(S)\), we can always write _S_ in _canonical form_ over the alphabet {1_,...,_∥_S_∥}, where the symbols are sorted according to their first appearance in _S_. If _S_ is in canonical form, its canonical matrix _A<sub>S</sub>_ is the \(\unknown S\unknown\times\unknown S\unknown\) symbol-block incidence matrix, i.e., _A<sub>S</sub>(i,j_)=1 if symbol _i_ appears in block _j_, and 0 otherwise. One cannot quite recover _S_ from _A<sub>S</sub>_ since _A<sub>S</sub>_ does not encode the order of symbols within a block. Nonetheless, the transformation is _useful_ inasmuch as subsequences avoided by _S_ often become 0-1 patterns avoided by _A<sub>S</sub>_.

### Composition and Shuffling.

We consider sequences _S_ partitioned into _live_ and _dead_ blocks satisfying extra constraints:

• All live blocks have the same length. Dead blocks have variable lengths, and the number of dead blocks between consecutive live blocks is also variable.<tbc>

• The first occurrence of every symbol appears in a dead block, and dead blocks contain only first occurrences. Let \((\unknown S\unknown)\) be the number of live blocks in _S_.<tbc>

