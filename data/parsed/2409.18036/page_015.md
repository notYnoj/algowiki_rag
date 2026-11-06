<tbc>construct a suitable static subset sampling instance from a final-level PSS instance, where the latter is dynamic and parameterized on the fly by \((\alpha,\beta)\). The second challenge is how to "encode" the configuration of static subset sampling instance such that it can be evaluated and located in the lookup table in _O_(1) time. Third, the overall space consumption of both the lookup table and the "encoder" must be bounded by _O(n_). Next, we introduce the remaining two components in our HALT structure, i.e., the _adapters_ and the _lookup table_, to address these technical challenges.

## 4.3 The Lookup  in HALT

In order to set up the context of the goal which the adapters aim to achieve, we first introduce the lookup table in our HALT structure.

Define _n_<sub>0</sub> be the size of the item set _S_ when the HALT structure is constructed. Our lookup table aims to solve a _special static subset sampling_ (4S) problem in the following form:

\(\bullet\) the input item set _V_ contains _exactly K_ items {_v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>K</sub>_}, where \(K=2\cdot log_2log_2log_2n_0\);

\(\bullet\) the sampling probability of the _i_<sup>th</sup> item _v<sub>i</sub>_ in _V_ is in the form of \(p_i=min\{1,\frac{2^{i+1}\cdot c_i}{m^2}\}\), where _c<sub>i</sub>_ is an integer in the range of \[0_,m_\] and _m_ is an integer bounded by _O_(loglog_n_<sub>0</sub>); as a result, the probability of each item must be an integer multiple of \(\frac{1}{m^2}\).

Therefore, every possible input to the above 4S problem can be uniquely specified by a _K_-dimensional vector \(\vec{c}=(c_1,c_2,\dots,c_K)\), where each _c<sub>i</sub>_ is an integer in \[0_,m_\]. Each \(\vec{c}\) is called an _input configuration_ of the 4S problem. The total number of possible input configurations is (_m_+1)_<sup>K</sup>_.

Consider a fixed input configuration \(\vec{c}\). Every possible subset sampling result can be encoded by a _K_-bit string _r_, where the _i_<sup>th</sup> bit _r_\[_i_\]=1 indicates the item _v<sub>i</sub>_ is in the sampling result and _r_\[_i_\]=0 means _v<sub>i</sub>_ is not. Thus, the probability of obtaining a subset sampling result _r_ can be calculated as:

\(Pr(r)=\prod_{i=1}^K\left(r[i]\cdot p_i+(1-r[i])\cdot(1-p_i)\right).\)

Since _p<sub>i</sub>_ is an integer multiple of \(\frac{1}{m^2}\), Pr(_r_) is an integer multiple of \(\frac{1}{(m^2)^K}\). Furthermore, observe that there are exactly 2_<sup>K</sup>_ possible subset sampling results, _r_. Summing Pr(_r_) over all _r_’s, we must have \(\sum_{r\in\{0,1\}^K}Pr(r)=1\).

Therefore, all the possible subset sampling results for a fixed input configuration, \(\vec{c}\), can be encoded in an array \(A(\vec{c})\) of (_m_<sup>2</sup>)_<sup>K</sup>_ cells and each cell is an _K_-bit string. Specifically, each subset sampling result _r_ is stored in exactly \(Pr(r)\cdot(m^2)^K\) cells in the array \(A(\vec{c})\). As a result, given an input configuration \(\vec{c}\) to the 4S problem, a subset sampling result for \(\vec{c}\) can be obtained by picking a cell in \(A(\vec{c})\) uniformly at random and returning the _K_-bit string _r_ as the subset sampling result. Clearly, each subset sampling result _r_ will be returned with probability exactly Pr(_r_) independently.

Figure 2 shows the detailed structure of the lookup table.

**The Lookup  and Query Algorithm.** Our lookup table T contains (_m_+1)_<sup>K</sup>_ rows, where each row is an array \(A(\vec{c})\) corresponding to an input configuration \(\vec{c}\). Given an input configuration \(\vec{c}\), the query algorithm works as follows:

\(\bullet\) locate the corresponding row \(A(\vec{c})\) in T of \(\vec{c}\);

\(\bullet\) uniformly at random select an index in \(A(\vec{c})\) and return the _K_-bit string in the cell at the index as the subset sampling result.

LEMMA 4.12. _Each input configuration_ \(\vec{c}\) _can be represented in O_(1) _words._

PROOF. Since each _c<sub>i</sub>_ is an integer in \[0_,m_\], it can be encoded in \(\lceil log_2(m+1)\rceil\) bits. Thus, \(\vec{c}\) can be encoded in \(K\cdot\lceil log_2(m+1)\rceil\in O(logn_0)\subseteq O(d)\) bits, equivalently, _O_(1) words, where \(K\in O(logloglogn_0)\) and \(m\in O(loglogn_0)\). \(\sqcap\sqcup\)

