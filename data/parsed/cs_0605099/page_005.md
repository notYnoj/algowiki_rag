**Procedure for Finding a Near-Optimal **

1. Start with an optimal or near-optimal nonalphabetic code with length vector **_l_**<sup>non</sup>, either the Shannon-like **_l_**<sup>s</sup> or the Huffman-like **_l_**<sup>h</sup>.<tbc>

2. Find the set of all _minimal points: i_ such that 1_\<i\<n_, _l_<sup>non</sup>(_i)\<l_<sup>non</sup>(_i_-1), and _l_<sup>non</sup>(_i)\<l_<sup>non</sup>(_i_+1); or \(i\in[j,j+k]\) minimizing _w(i_) for _l_<sup>non</sup>(_j_-1)_\>l_<sup>non</sup>(_j_)=_l_<sup>non</sup>(_j_+1)=\(\cdots=l^\mathrm{non}(j+k)<l^\mathrm{non}(j+k+1)\).<tbc>

3. Assign a preliminary alphabetic code with lengths _l_<sup>pre</sup>(_i_)=_l_<sup>non</sup>(_i_)+1 for all minimal points and _l_<sup>pre</sup>(_i_)=_l_<sup>non</sup>(_i_) for all other items. The first codeword is _l_<sup>pre</sup>(1) zeros, and each additional codeword _c(i_) is obtained by either truncating _c(i_-1) to _l_<sup>pre</sup>(_i_) bits and adding 1 to the integer that the binary codeword represents (if \(l^\mathrm{pre}(i)\le l^\mathrm{pre}(i-1)\)) or by adding 1 to the integer/codeword _c(i_-1) and appending _l_<sup>pre</sup>(_i_)-_l_<sup>pre</sup>(_i_-1) zeros (if _l_<sup>pre</sup>(_i)\>l_<sup>pre</sup>(_i_-1)), defining the binary tree.<tbc>

4. Go through the code tree (with, e.g., a depth-first search), and remove any redundant nodes. Any node with only one child can replace the child by its grandchild or grandchildren. At the end of this process, an alphabetic code with \(\sum_{i=1}^n2^{-l(i)}=1\) is obtained.

<tbc>code tree for the Huffman-like problem.

Every step after the first takes linear time with linear space, thus the overall complexity of the algorithms. Step 3 is the method by which Nakatsu showed that any nonalphabetic code can be made into an alphabetic code with similar lengths \[9\]. (The use of weights as a tie breaker and the nonlinearity of the problem do not change the validity of the algorithm.) Step 4 is the method by which Yeung showed that any alphabetic code can be made into another alphabetic code with \(\sum_{i=1}^n2^{-l(i)}=1\) without lengthening any codewords \[11\]. Thus this is a hybrid and extension of these two approaches.

For _w_=(8/26,1/26,9/26,6/26,2/26) with _a_=0.6, applying the Shannon- like version of this algorithm, we find that **_l_**<sup>s</sup>=(2,13,1,4,10), preliminary codeword lengths are \(l_\mathrm{s}^\mathrm{pre}=(2,13,2,4,10)\), and the preliminary code tree is as follows:

\(C=(00,0100000000000,10,1100,1101000000)\)

The italicized bits are redundant, and therefore so are the corresponding nodes in the code tree. They are thus removed in Step 4, which means the final tree has lengths (2,2,2,3,3). The probability of success is _a_<sup>_L<sub>a</sub>(w,l_)</sup>≈0.316 (_L<sub>a</sub>(w,l_)≈0.851), close to the optimal probability of about 0.334 (_L<sub>a</sub>(w,l_<sup>∗</sup>)≈0.843). Using the Huffman-like approximation algorithm yields **_l_**<sup>h</sup>=(2,4,1,3,4), a preliminary tree of lengths \(l_\mathrm{h}^\mathrm{pre}=(2,4,2,3,4)\), and an output tree with lengths (2,2,2,3,3), which are identical to the above. The same probability mass function with _a_=0.7 yields an optimal tree in the Huffman- like version. For \(a\in(0.5,1)\), coding bounds follow from these approaches:<tbc>

