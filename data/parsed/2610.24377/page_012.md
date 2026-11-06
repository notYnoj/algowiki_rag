**Corollary 3.2.** There exists a catalytic algorithm using _O_(log(_n_)) clean space and _n_<sup>1+_o_(1)</sup> time which takes as input a pair of _n_-bit integers and computes their product.

_Proof._ The classic Schönhage-Strassen algorithm for integer multiplication gives a (succinctly uniform) NC<sup>1</sup> circuit of size _O(n_log(_n_)loglog(_n_)) \[SS71; Weg87\]. Applying Lemma 3.1 to this circuit yields the result. \(\blacksquare\)

Recall that Schönhage-Strassen works by computing a discrete Fourier transform over Z/(2_<sup>m</sup>_+1)Z -- the same argument as above shows that such DFTs can be performed in near-linear time catalytically. As we observe in Section 4, in fact there exists an algorithm with the even faster runtime \(\widetilde{O}(n)\), over any ring with efficiently-computable operations, which in turn also gives \(\widetilde{O}(n)\)-time polynomial multiplication.

## 3.3 Application: Sorting

We do not know small NC<sup>1</sup> circuits for sorting lists of integers, but fortunately, if we are somewhat more careful, we can nonetheless also apply Theorem 1.1 here:

**Corollary 3.3.** There exists a catalytic algorithm using _O_(log(_n+b_)) clean space and _n_<sup>1+_o_(1)</sup>_b_ time which takes as input a length-_n_ list of _b_-bit numbers, and computes the sorted list.

_Proof._ Recall that there exists an _O_(log(_n_))-depth _sorting network_ \[AKS83\]. A sorting network operates over _n_ wires, and consists of "comparators" which swap the values of two wires if they are out of sorted order.

If this network was converted into a fan-in 2 Boolean circuit, each comparator would require depth log(_b_), so the overall circuit would have depth _O_(log(_n_)log(_b_)), which is much too high to apply Lemma 3.1. However, we can nonetheless produce a _o_(log(_n_))-depth, _n_<sup>1+_o_(1)</sup>_b_-size SYM circuit, by a similar approach to the proof of that lemma. That is, we show how to evaluate loglog(_n)/_100 layers of a sorting network using a constant- depth SYM circuit with _O(bn_<sup>1+1/loglog(_n_)</sup>) wires.

Suppose we have written down the values on all of the wires prior to this sequence of layers, and want to compute the value of one of the wires after the sequence of layers. This wire’s output depends on at most 2<sup>loglog(_n)/_100</sup>=log<sup>1/100</sup>(_n_) of the initial values. Observe that there are only \(log^{1/100}(n)!\le 2^{log^{1/50}(n)}\) possible orderings of those log<sup>1/100</sup>(_n_) many values, and that the ordering of those values is sufficient to determine which of them should be written to the output wire. Now, for a given candidate ordering, there exists a _O(b_2<sup>log<sup>1/50</sup>(_n_)</sup>)-wire AC<sup>0</sup> circuit which evaluates whether the values are thus ordered: we can check whether a given pair of values is in the correct order in _O(b_) size and depth _O_(1) \[CSV84\], so we simply do all of these checks in parallel and take their AND. So, to compute the _i_th bit on output value of the wire, we can simply compute in parallel for each initial value ordering whether that ordering is correct, and then take the OR over all orderings of "this initial value ordering is correct AND the _i_th bit of the value which would get output under this initial value ordering is a 1".

This overall gives a SYM circuit for sorting with depth _O_(log(_n)/_loglog(_n_)) and size \(O(nlog(n)\cdot b2^{log^{1/50}(n)})=O(bn^{1+o(1)})\). Since the AKS sorting network is DLOGTIME uniform, and the identity of a gate or wire in the above constructed circuit can be computed in logarithmic space and _n_<sup>_o_(1)</sup> time given the original sorting network, we can apply Theorem 1.1 to evaluate it in time _bn_<sup>1+_o_(1)</sup>. \(\blacksquare\)

We observe that by composing catalytic algorithms one can use these results to get fast algorithms for decision (and counting) problems:

**Corollary 1.6** (kSUM)**.** Let \(A_1,A_2,\cdots,A_k\) be lists of _n_<sup>_o_(1)</sup>-bit integers. Let _n_=max_<sub>i</sub>_{|_A<sub>i</sub>_|}. There exists a catalytic algorithm which, using \(n^{\lceil k/2\rceil+o(1)}\) time, \(n^{\lceil k/2\rceil+o(1)}\) catalytic space, and _O_(log_n_) clean space, decides whether there exists a _k_-tuple \((a_1,\cdots,a_k)\in A_1\times\cdots\times A_k\) such that \(a_1+\cdots+a_k=0\) .

