The total running time then follows straightforwardly from the following claim.

**Claim 3.2.** _When S is a_ \(\pi\)_-avoiding permutation sequence, Algorithm 1 terminates in_ \(m'\le\frac{n}{d\cdot\mathrm{log}n}\) _rounds._

_Proof._ Observe that the presorted sequences \(S'_1,\dots S'_{m^\prime}\) partition _S_ into consecutive intervals with respect to the left-to-right order, while the individual rounds partition _S_ into consecutive intervals of elements with respect to their values. Together, they form a gridding of sorts that we aim to use in conjunction with the Marcus-Tardos theorem. Let _R_ denote the total number of rounds and let us define an \(m'\times R\) matrix _M_ as follows<tbc>

\(M(i,j)=\left\{\begin{array}{ c c }
1 & \text{if the sequence}S'_i\text{was touched in the}j\text{th round} \\
0 & \text{otherwise.}
\end{array}\right.\)

<tbc>Assume for a contradiction that \(R>m'\). Since the algorithm touches exactly _d_ sequences in each round except for possibly the last one, each row in _M_ except for possibly the last one contains exactly _d_1-entries. In total, that makes the number of 1-entries in _M_ is strictly larger than

\((R-1)\cdot d\ge(R-1)\cdot 2c_\pi\ge R\cdot c_\pi\)

where the last inequality holds since \(R\ge 2\). Now Lemma 2.1 implies that _M_ contains an occurrence of \(\pi\) because by our assumptions \(\mathrm{max}(m',R)=R\). Therefore, there are indices \(i_1<\cdots<i_{|\pi|}\) and \(j_1,\dots,j_{|\pi|}\) such that \(M(i_1,j_1),\dots,M(i_k,j_{|\pi|})\) are all 1-entries and \(j_1,\dots,j_{|\pi|}\) is order-isomorphic to \(\pi\). For \(p\in[|\pi|]\), let _x<sub>p</sub>_ be an arbitrary element of the sequence \(S'_{i_p}\) that was outputted in the _j<sub>p</sub>_th round. It follows that \(x_1,\dots,x_{|\pi|}\) form a subsequence of _S_ that is order-isomorphic to \(\pi\) and we reach a contradiction.

## 3.2 Without prior knowledge of \(\pi\)

Now, we consider the more general case where \(\pi\) (and \(c_\pi\) in particular) is not known to the algorithm. However, we still restrict inputs to permutation sequences. The basic idea is to guess \(c_\pi\) by starting with a constant, trying the previous approach for a bounded number of rounds and doubling.

### Description of the algorithm.

Initially, we set _d_=1 and the algorithm proceeds in _phases_ until all the elements are written on output. At the beginning of each phase, the algorithm doubles the main parameter by setting \(d\leftarrow 2d\), and halves the number of input sequences by merging them in pairs. If the number of sequences at the start of the phase was odd, we perform one additional merge to ensure that we always decrease the number of sequences by at least half. Let us denote by _d<sub>i</sub>_ the value of _d_ in the _i_th phase. It follows that in the _i_th phase, we work with \(m_i\le\frac{m}{2^i}\) sequences and _d<sub>i</sub>_ is equal to 2_<sup>i</sup>_. In particular, we have \(m_i\le\frac{n}{d_i\mathrm{log}n}\) in the _i_th phase.

Afterwards, the algorithm follows the case where \(c_\pi\) was known, i.e. it proceeds in rounds where in each round, it takes the _d_-tuple of sequences with the smallest initial elements and performs a _d_-way merge until the value of the (_d_+1)-th smallest initial element is reached. A standard binary heap is again used for efficiently retrieving these _d_ sequences. The only change is that now the upper bound on the number of rounds is explicitly enforced rather than implicitly observed. Specifically, the _i_th phase is terminated after _m<sub>i</sub>_ rounds and the algorithm enters next phase. This continues until all sequences are exhausted. See Algorithm 2.

It is important that whenever a new phase begins, the algorithm does not reset to the very beginning as there is no reason to do so. The output to this point is a valid prefix of the sorted sequence. Thus, the next phase continues with only the remaining elements in each sequence.

