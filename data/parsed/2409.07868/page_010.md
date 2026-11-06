We would like to bound the number of light rounds in a similar fashion to the proof of Claim 3.2. However, two elements processed in consecutive light rounds might have the same value, and thus, the gridding induced by sequences and rounds would be ill-formed. In particular, an occurrence of \(\pi\) in this gridding would not necessarily imply an occurrence of \(\pi\) in the input sequence. On the other hand, notice that two light rounds separated by another light round must involve elements of completely disjoint values. Therefore, the solution is to consider only every other light round.

Let _L_ denote the number of full light rounds. We claim that \(L\le\frac{m_i}{2}\) . Assume for a contradiction that \(L>\frac{m_i}{2}\) and let \(\ell_1,\dots,\ell_{\lceil L/2\rceil}\) be the indices of odd full light rounds. We construct an \(m_i\times\lceil\frac{L}{2}\rceil\) matrix _M_ as follows<tbc>

\(M(j,k)=\left\{\begin{array}{ c c }
1 & \text{if the sequence}S'_j\text{was touched in the}(\ell_k)\text{th round} \\
0 & \text{otherwise.}
\end{array}\right.\)

<tbc>Each full round touches exactly _d<sub>i</sub>_ sequences, and thus the number of 1-entries in _M_ is

\(\left\lceil\frac{L}{2}\right\rceil\cdot d_i>\frac{m_i}{4}\cdot 4c_\pi=m_i\cdot c_\pi.\)

Again, it follows that _M_ contains an occurrence of \(\pi\) due to Lemma 2.1. We argue that it induces an occurrence of \(\pi\) in the original input sequence _S_. We recover a subsequence \(x_1,\dots,x_{|\pi|}\) of _S_ from the occurrence of \(\pi\) in _M_ exactly as in the proof of Claim 3.2. In this general case, we must also verify that all the elements are distinct in value. But crucially, this follows by our consideration of only every other light round and hence, \(x_1,\dots,x_{|\pi|}\) is order-isomorphic to \(\pi\) and we reach a contradiction. Thus, we have \(L\le\frac{m_i}{2}\) .

Putting it all together, the _i_th phase consisted of at most \(\frac{3}{4}m_i\) full rounds, and accounting for the one additional final round makes the total number of rounds at most \(\frac{3}{4}m_i+1\). Furthermore, the number of rounds must be an integer and thus we know that at most \(\lfloor\frac{3}{4}m_i\rfloor+1\) rounds occurred. But it is easily verified that \(\lfloor\frac{3}{4}m_i\rfloor+1\le m_i\) for every integer \(m_i\ge 1\) and it follows that Algorithm 2 should have terminated in the _i_th phase.

## 4 Sorting many short sequences

In this section, we show how to use decision trees to efficiently sort a large set of short sequences. Step by step, we will construct an algorithm summarized by the following theorem.

**Theorem 4.1.** _Let S_<sub>1</sub>_,...,S<sub>n/k</sub> be_ \(\pi\)_-avoiding sequences, each of length k. Then there is an algorithm that sorts all S<sub>i</sub>’s in time_ \(O((\mathrm{log}c_\pi+1)\cdot n)+2^{2^{O(k\mathrm{log}k)}}\) _even if_ \(\pi\) _is a priori unknown._

### 4.1 Decision trees

A _decision tree T_ for sorting a sequence of length _k_ is formally a full binary tree with each internal node labeled by a pair \((i,j)\in[k]^2\) and each leaf labeled by a permutation of length _k_. For a sequence _S_=(_s_<sub>1</sub>_,...,s<sub>k</sub>_) of length _k_, the _run of T on S_ is the root-to-leaf path in _T_ such that in an internal node _v_ labeled with (_i,j_), the path continues to the left subtree of _v_ if and only if \(s_i\le s_j\). For a sequence _S_ of length _k_, the _result of a run of T on S_ is the label of the leaf reached by the run of _T_ on _S_. We say that a decision tree _T sorts_ a sequence _S=s_<sub>1</sub>_,...,s<sub>k</sub>_ if the result of the run of _T_ on _S_ is a permutation \(\sigma\) such that \(s_{\sigma_1}\le\cdots\le s_{\sigma_k}\). See Figure 2. Observe that for a permutation \(\sigma\), a decision tree _T_ sorts \(\sigma\) precisely if the result of applying _T_ on \(\sigma\) is its inverse \(\sigma^{-1}\).

