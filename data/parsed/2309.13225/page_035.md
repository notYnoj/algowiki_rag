giving the desired result. The proof of correctness follows exactly as in \[CDXZ22\].

**Lemma 5.5.** _The expected number of segments in_ \(T_b^{(l)}\) _is_ \(\tilde{O}(n^{(a+b+\mu)-\alpha})\)

_Proof._ Suppose first \(2^l>\frac{p}{100}\). Then, _B_<sup>(_l_)</sup>, _C_<sup>(_l_)</sup> have at most \(O\left(\frac{n^\mu}{2^l}\right)=O\left(\frac{n^\mu}{p}\right)=O\left(n^{\mu-\alpha}\right)\) intervals in a given row. The overall number of intervals is therefore bounded by \(O\left(n^{(a+b+\mu)-\alpha}\right)\)

Consider a segment (_i,k,(j_<sub>0</sub>_,j_<sub>1</sub>)) and arbitrarily pick \(j\in[j_0,j_1]\) where _A<sub>ik</sub>_ finite and \(A_{ik}^*+B_{kj}^*\neq C_{ij}^*\). Then, by Assumption 5.2, we have \(|A_{ik}+B_{kj}-C_{ij}|\ge\frac{p}{3}\). We now bound the probability that \((i,k,(j_0,j_1))\in T_b^{(l)}\). By definition, this implies that,<tbc>

\(\left\lfloor\frac{A_{ik}modp}{2^l}\right\rfloor+\left\lfloor\frac{B_{kj}modp}{2^l}\right\rfloor=C_{ij}^{(l)}+b\)

<tbc>Since \(\left\lfloor\frac{(C_{ij}modp)-2(2^l-1)}{2^l}\right\rfloor\le C_{ij}^{(l)}\le\left\lfloor\frac{(C_{ij}modp)+2(2^l-1)}{2^l}\right\rfloor\)<br>
\(-4\le\frac{A_{ik}modp}{2^l}+\frac{B_{kj}modp}{2^l}-\frac{C_{ij}modp}{2^l}-b\le 4\)

Let _C<sub>ij</sub>=A<sub>iq</sub>+B<sub>qj</sub>_, so that,

\(-4\cdot 2^l\le(A_{ik}+B_{kj}-A_{iq}-B_{qj})modp-b\cdot 2^l\le 4\cdot 2^l\)

so that (_A<sub>ik</sub>+B<sub>kj</sub>-A<sub>iq</sub>-B<sub>qj</sub>_)mod_p_ takes one of _O_(2_<sup>l</sup>_) values _r_ in the range \[2_<sup>l</sup>(b_-4),2_<sup>l</sup>(b_+4)\]. Since \(|b|\le 10\), the largest such value is bounded by \(|r|\le 14\cdot 2^l<\frac{p}{6}\le\frac{1}{2}|A_{ik}+B_{kj}-A_{iq}-B_{qj}|\) where we used \(2^l<\frac{p}{100}\).

Then, if _B<sub>kj</sub>,B<sub>qj</sub>_ are from _B_ in Lemma 5.3, then,

\(|(A_{ik}+B_{kj}-A_{iq}-B_{qj})-r|=O(n^\mu)\)

The number of primes larger than \(40n^\alpha\) that divide this quantity is therefore at most \(\frac{\mu}{\alpha}=O(1)\). In particular, such a _p_ is chosen with probability \(n^{-\alpha}\).

On the other hand, if _B<sub>kj</sub>,B<sub>qj</sub>_ may have been set artificially to some number congruent to \(0,\lceil p/3\rceil,\lceil 2p/3\rceil\) in Lemma 5.3. We can still bound the probability that _p_ divides \(|(A_{ik}+B_{kj}-A_{iq}-B_{qj})-r|\), as in \[CDXZ22\].

Finally, we have _O_(2_<sup>l</sup>_) such remainders _r_, and in total \(O\left(\frac{n^{a+b+\mu}}{2^l}\right)\) segments, so that in expec tation we can upper bound \(|T_b^{(l)}|=\tilde{O}(n^{(a+b+\mu)-\alpha})\).

## 5.2 Framework for Additive Approximations via Monotone (min,+) Product

We now give an improvement on the generalized algorithm of Dor et al. \[DHZ00\], using fast matrix multiplication to give a better trade-off between additive approximation error and running time. This extends the work of Deng et al. \[DKR<sup>+</sup>22\] to additive error beyond +2.

**Theorem 5.6.** _Let_ \(\beta\ge 4\) _be an even integer. Let G be an undirected, unweighted graph with n vertices. Algorithm 6 computes_ \(\hat{\delta}\) _such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+\beta\) _for all_ \(u,v\in V\) _in time,_ \(\tilde{O}\left(n^{2+\frac{2x}{\beta+2}}\right)\) _where x is the solution to,_ \(\omega\left(1-\frac{\beta-2}{\beta+2}x,1-x,1-\frac{\beta-4}{\beta+2}x\right)=1+\frac{4+2\beta}{\beta+2}x\).<sup>2</sup>

<sup>2</sup>\(\omega(a,b,c)\) is the minimum value such that the product of a \(\lceil n^a\rceil\times\lceil n^b\rceil\) matrix by a \(\lceil n^b\rceil\times\lceil n^c\rceil\) matrix can be computed in \(O(n^{\omega(a,b,c)+\varepsilon})\) arithmetic operations for any constant \(\varepsilon>0\). Note \(\omega=\omega(1,1,1)\).

