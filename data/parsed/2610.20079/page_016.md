## 6.1 The interchange operation

Write each bit position as \((p,t,g,d,z)\in[P]\times[2^u]\times[G]\times[2^u]\times[\ell]\), stored in lexicographic order, with _z_ varying fastest. Here _p_ is the prefix before the two fields, _g_ is the coordinate between them, and _z_ is the suffix; all three remain unchanged. An _address-field interchange_ moves the bit at (_p,t,g,d,z_) to (_p,d,g,t,z_) and leaves the other coordinates unchanged. If _z_ contains all bits of a record, the record moves as a whole. Fixing _p_ selects one contiguous prefix segment containing all values of (_t,g,d,z_). A stream below means an ordered sequence of bits stored on disk. The permutation is independent of key values. Intermediate steps may use coding, but the final result must preserve every bit’s value. Figure 4 illustrates _u_=2.

Let _a_=log(_M/B_) and \(\tau=1-\varepsilon\), where \(\varepsilon=1.5\times 10^{-5}\). The denominator _a_ corresponds to the field width that memory buffers can handle directly.

**Lemma 6.1** (Block transfers for address-field interchange)**.** There is a fixed constant _C_<sub>abs</sub> such that, for \(M\ge max\{2B,C_\mathrm{abs}\}\), the interchange above on \(V=PG\ell 2^{2u}\) bits, with \(u\ge 1\), takes

\(O\left(1+\frac{V}{Bw}\left[1+\left(\frac{u}{a}\right)^\tau\right]\right)\) (14)

block transfers and at most _M_ words of memory. The algorithm is deterministic, with a schedule determined by the array dimensions. If all array dimensions are polynomial in _N_, its workspace is also polynomial, and dimension parameters and workspace addresses occupy a constant number of machine words of the original width _w_.

The block simulation in Appendix A lets us first assume \(M/B\ge R_0\) for a sufficiently large fixed constant _R_<sub>0</sub>, reserving a fixed number of block buffers. The constant _C_<sub>abs</sub> accommodates the fixed circuit’s control information. We follow the recursive construction of OpenAI \[Ope26, Proposition 11 and Lemma 12\]: the circuit reduces interchanges of long fields to interchanges of short fields, stopping when memory can handle them directly.

## 6.2 The Coding Recursion

Corollary 5.4 gives fixed parameters _m,W,S_, with _m_=512, such that

\(\lambda:=S/W<m^\tau.\) (15)

We turn this rank saving into a smaller recursive cost: an edge of rank _r_ requires only _r_ short-field interchanges, each acting on one stream of _V/W_ bits. Summing over edges gives _S_ child calls with total data volume (_S/W)V_ .

Address
Record value
p
01
g
10
z
37
p
10
g
01
z
37

Figure 4: Interchanging two address fields preserves the record value. The fields are 01 and 10; the other coordinates _p,g,z_ remain unchanged.

