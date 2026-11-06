reverse order, from its bottom-right corner. Then column _k_ becomes column _c_=2_b+a-k_, and row _k-i_+1 becomes row 2_b+a_-(_k-i_+1)=_i+c_-1. So the middle block has a 1 in row _i+c_-1 and column _c_ for every \(c\in[b]\), and zeros elsewhere: it is the _i_th slice of \((23)\cdot\mathsf{P}_{a,b}\). In block form, where each block stands for the tensor whose slices are the corresponding blocks of the slices, we have shown

\(\mathsf{P}_{a,3b+a-1}=\left(\begin{array}{ c c c }
\mathsf{P}_{a,b} & 0 & 0 \\
* & (23)\cdot\mathsf{P}_{a,b} & * \\
0 & 0 & \mathsf{P}_{a,b}
\end{array}\right),\)

where ∗ marks the two blocks that need not be zero. An application of Lemma 2.4 makes the ∗ blocks zero and proves the lemma.

**Remark 3.12.** The proof of Lemma 3.11 naturally extends to multiple blocks of different sizes. Let \(s,r,n\ge 1\) and \(a,b_i,c_j\ge 1\) be integers. Then<tbc>

\(\mathsf{P}_{a,b_1}\oplus_1\cdots\oplus_1\mathsf{P}_{a,b_r}\oplus_1\left((23)\cdot\mathsf{P}_{a,c_1}\right)\oplus_1\cdots\oplus_1\left((23)\cdot\mathsf{P}_{a,c_s}\right)\le_1\mathsf{P}_{a,n}\)

<tbc>if and only if \(n\ge N:=\sum_ib_i+\sum_jc_j+(a-1)max(s,r-1)\). The proof interleaves the tensors P<sub>_a,b<sub>i</sub>_</sub> and \((23)\cdot\mathsf{P}_{a,c_j}\) as the diagonal blocks of P<sub>_a,n_</sub>, and degenerates the off-diagonal blocks using Lemma 2.6, as in the proof of Lemma 3.11. In block form, this looks as follows:

