<tbc>storing the prefix-sums. Inside a single frame we use a lookup table to compute the prefix sum. More exactly, _P<sub>i</sub>[j_] stores the prefix-sum over all self-delimiting numbers in \(S'\) up to the _j_th frame in _A<sub>i</sub>_. Fig. 2 sketches an example. We so obtain the next theorem where we again require the position _p<sub>x</sub>_ in _S_ of all _x\>N_ as the input to our competitive rank query.

\(\blacktriangleright\) **Theorem 6.** _Given an N-bit sequence S of k self-delimiting numbers, a parameter_ \(\tau\) _with_ \(logN\le\tau\le w\) _we can compute a data structure realizing competitive rank. The data structure can be constructed in_ \(O(k+N/\tau)+o(2^\tau)=O(k+N/logN)+o(2^\tau)\) _time and uses_ \(O(N)+o(2^\tau)\) _bits._

**Proof.** We make use of a table `PREFIXSUM` that stores for all binary sequences of length \(\lceil\tau/2\rceil\) the answer to all prefix-sum queries. The table can easily be computed in time \(o(2^\tau)\) and stored with \(o(2^\tau)\) bits.

We can handle numbers in the range of [_N,_2_<sup>N</sup>_) the same way we did in Theorem 5, that is, storing the competitive rank of a number _x_ in an extra _O(N_)-bit sequence _I_ starting at bit _p<sub>x</sub>_, where _p<sub>x</sub>_ is the position of _x_ in _S_. Thus, it suffices to consider the case that the given self-delimiting numbers are all in the range [0_,N_).

We start to describe our storage schema. Partition [0_,N_) into \(\lceil N/\tau\rceil\) regions where each region \(\mathcal{R}_i=[i\lceil\tau/2\rceil,(i+1)\lceil\tau/2\rceil)\) (with \(i=0,\dots,2\lceil N/\lceil\tau/2\rceil]-1\)) consists of \(\lceil\tau/2\rceil\) different numbers. Create an array _B_ of \(\lceil N/\lceil\tau/2\rceil\rceil\) fields, each of \(\lceil\tau/2\rceil\) bits. For each region R_<sub>i</sub>_ with \(\mathcal{R}_i\cap S=\emptyset\), _B[i_] contains a `null` pointer. Otherwise, _B[i_] points to a data structure _Q<sub>i</sub>_ that contains all information to determine the competitive rank of each number of \(\mathcal{R}_i\cap S\).

The data structure _Q<sub>i</sub>_ consists of two auxiliary structures _A<sub>i</sub>_ and _P<sub>i</sub>_ defined in the next paragraphs. Let _A<sub>i</sub>_ be a sequence of self-delimiting numbers consisting of the number of occurrences of each number \(x\in\mathcal{R}_i\) in _S_, stored via static space allocation (Section 2). Note that, if a number \(x\in\mathcal{R}_i\) does not appear in _S_, we store 0 as the number of its occurrences in _S_. Partition _A<sub>i</sub>_ into frames of \(\lceil\tau/2\rceil\) bits each.

A frame can contain multiple self-delimiting numbers. If this is the case, we want to access the prefix sum over the self-delimiting numbers inside the frame, up to a desired number, quickly. To do so we use the precomputed lookup table `PREFIXSUM`. However, to simplify the process we want no self-delimiting number to be divided between two frames. Therefore, we store each self-delimiting number in _A<sub>i</sub>_ so that it either fits into the current not full frame, or it uses the next one. Of course it is not possible to store a large number (of more than \(\lceil\tau/2\rceil\) bits) into a single frame. In this case a frame contains only one number and we can read it directly without using table lookup. If the number is too large to fit into a single frame, we use the next three frames to store the number in a standard binary representation.

R1
R8
R10
S'
1
8
10
F
A1
A8
A10
P1
0
9
P8
14
P10
18

**Figure 2** A sketch of our storage schema to realize competitive rank. For each region R_<sub>i</sub>_, that contains numbers out of \(S'\), a pointer _F[i_] points to a data structure storing the amount of occurrences for each of the numbers. In addition, _P<sub>i</sub>_ stores the prefix-sum over the frames up to _A<sub>i</sub>_. For numbers _x_ of size _\>N_ the position _p<sub>x</sub>_ of _x_ in _S_ is required as the input.

