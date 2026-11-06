_Proof._ The standard reduction from kSUM to 2SUM is efficiently computable, in the sense that a given bit of the kSUM instance can be computed in log(_n_) space and polylog(_n_) time given read access to the 2SUM instance \[Eri95\]. So, it suffices to give an _n_<sup>1+_o_(1)</sup>-time, _O_(log_n_) clean space, catalytic algorithm for 2SUM. This follows from the standard reduction from 2SUM to sorting, which can be implemented catalytically.

That is, take one of the lists, negate all of the elements in it, add some small \(\varepsilon\) to all of them, and merge it with the other list. Then, use the _n_<sup>1+_o_(1)</sup>-time CL algorithm for sorting. Finally, observe that there is a near-linear-size TC<sup>0</sup> circuit which returns whether any adjacent elements of a list differ by exactly \(\varepsilon\) -- this yields a near-linear-time CL algorithm by Theorem 1.1, which reads its input via XORing into the catalytic tape a constant number of times, and hence can be composed with the previous algorithm. The composition of these algorithms will decide 2SUM.

We note that a similar idea<sup>11</sup> will also allow computing #kSUM in \(n^{\lceil k/2\rceil+o(1)}\)-time CL. A modification of this #2SUM construction, instead taking the _k_th power of the element count in equal-value blocks, gives:

**Corollary 3.4.** Let _A_ be a list of _n_<sup>_o_(1)</sup>-bit integers. Let _n_=|_A_| and let _k\>_1 be a constant. There exists a catalytic algorithm computing the _k_th frequency moment

\(F_k=\sum_{i\in\mathbb{Z}}(f_i)^k,\)

where _f<sub>i</sub>_ is the frequency of value _i_ in _A_. This algorithm takes _n_<sup>1+_o_(1)</sup> time, _n_<sup>1+_o_(1)</sup> catalytic space, and _O_(log_n_) clean space.

We note that while \[BCCPV26; KKK26\] show there exist \(\widetilde{O}(n)\) time catalytic algorithms computing frequency moments, their algorithms would use catalytic space proportional to the size of the universe (i.e. they would only get a bound of 2<sup>_n_<sup>_o_(1)</sup></sup> catalytic space).

## 4 Evaluating Low-Degree Arithmetic Circuits

In this section, we observe that with some modifications the original \[BCKLS14\] approach for circuit evaluation will actually allow fast evaluation of even high-depth arithmetic circuits, so long as most layers consist only of linear operations. This allows us to obtain fast catalytic algorithms for Fourier transforms, matrix multiplication, and applications thereof.

### 4.1 Fast Low-Multiplicative-Depth Circuit Evaluation

**Definition 4.1.** For a ring K, an #NC(K) circuit has the following gateset:

i) fan-in 2 addition gates,<tbc>

ii) fan-in 2 product gates, and<tbc>

iii) fan-in 1 "\(\times x\)" and "+_x_" gates for each constant \(x\in\mathcal{K}\).

We say that such a circuit has **_multiplicative depth_** _d_ if its gates are presented grouped into layers such that gates in each layer depend only on gates in previous layers, and such that at most _d_ of those layers involve (fan-in 2) product gates.

We show that we can evaluate succinctly uniform #NC(K) circuits in near-linear time so long as they have sublogarithmic multiplicative depth, and so long as the ring operations are efficiently computable.

<sup>11</sup>One can similarly reduce to #2SUM, and begin by sorting, but now in order to construct a near-linear-size, _o_(log(_n_))- depth threshold circuit which performs the relevant counting step, one needs to be somewhat more careful. One can get this construction e.g. by breaking up into blocks of size _n_<sup>1/loglog(_n_)</sup>, spending _n_<sup>2/loglog(_n_)</sup> time counting in each block, and recurring loglog(_n_) times, as Allender and Koucký do for hardness magnification \[AK10\].

