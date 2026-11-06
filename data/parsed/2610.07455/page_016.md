where _b_ chooses one nonzero value _b<sub>i</sub>_ for every \(i\in T\). These products form a basis for all real-valued functions on _D<sup>k</sup>_. This follows by evaluating the function on points that are 0 outside _T_ and using inclusion-exclusion. In particular, when _f_ is integer-valued, all the coefficients \(\widehat{f}(T,b)\) are integers. We define deg_<sub>D</sub>(f_) to be the largest |_T_| for which \(\widehat{f}(T,b)\neq 0\), with constant functions having degree 0. Changing the basepoint changes the coefficients but not the degree. Indeed, the indicator of the old basepoint is one minus the sum of the indicators of all other values. Thus either set of indicators can be written using the other without increasing degree.

For a relation \(R\subseteq D^k\), we write **1**_<sub>R</sub>_ for its indicator function and use deg_<sub>D</sub>_(**1**_<sub>R</sub>_) as the degree of _R_.

**Example 3.6.** For CUT, let _Z<sub>i</sub>(z_)=**1**\[_z<sub>i</sub>_=1\]. Then

\(\mathbf{1}_\mathsf{CUT}(z_1,z_2)=Z_1(z)+Z_2(z)-2Z_1(z)Z_2(z),\)

so deg<sub>{0,1}</sub>(**1**<sub>CUT</sub>)=2.

As another example, let \(R_\mathsf{NAE}\subseteq\{0,1\}^3\) contain the tuples that are not constant. With _Z<sub>i</sub>(z_)=**1**\[_z<sub>i</sub>_=1\], we have

\(\mathbf{1}_{R_\mathsf{NAE}}(z)=Z_1(z)+Z_2(z)+Z_3(z)-Z_1(z)Z_2(z)-Z_1(z)Z_3(z)-Z_2(z)Z_3(z).\)

Thus deg<sub>{0,1}</sub>(**1**_<sub>R<sub>NAE</sub></sub>_)=2, even though _R_<sub>NAE</sub> has arity 3.

The upper and lower bounds for Exact-CSP will both use this degree after reducing the relation to its core.

### 3.6 Communication complexity

Our streaming lower bounds use the one-way communication problem INDEX_<sub>M</sub>_. Alice receives a string \(b\in\{0,1\}^M\), Bob receives an index \(i\in[M]\), and Bob must output _b<sub>i</sub>_. In a public-coin one-way protocol, Alice and Bob share a random string, Alice sends one message to Bob, and Bob produces the answer from this message, his index, and the shared randomness.

The connection to streaming is standard. Alice creates the first part of a stream from her input, runs the streaming algorithm on it, and sends the memory state to Bob. Bob resumes the algorithm from this state and appends constraints determined by his index. The memory state is the only message, so an _s_-space streaming algorithm gives a one-way protocol with _s_ bits of communication. The random tape of the streaming algorithm can be treated as the public random string.

We use the following standard lower bound.

**Lemma 3.7** (One-way complexity of INDEX, \[Abl96; KNR99\])**.** _Every randomized public-coin one-way protocol for_ INDEX_<sub>M</sub> with constant error uses_ \(\Omega(M)\) _bits of communication._

In each of our lower bounds, Alice’s part of the stream encodes her string, while Bob appends constraints that reveal the bit at his index. The rest of each reduction is devoted to constructing those constraints.

## 4 Properties of Cores

In this section, we prove the facts about cores that we will use throughout the paper. We first show that reducing to the core does not change any of our three objectives. We then give two ways to force an assignment using only constraints from a core relation. The first forces the assignment up<tbc>

