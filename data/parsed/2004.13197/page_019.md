<tbc>_k-k_ algorithm runs in _T_ I/Os, then the node capacity of _v_ at a level _h_ of T is designated by _c<sup>T</sup>(v_)=_k/_2_<sup>h</sup>_.

**Definition 16** (_type one_ and _type two bits_)**.** _A bit gained by a large element_ \(\ell\) _is an_ type one _bit if, when_ \(\ell\) _moves from v to one of v’s children, at most c<sup>T</sup>(v)/_4-1 _other large elements have already passed through v. The remainder of the bits are_ type two _bits._

Because a small-block input gives _O(B_) bits and a large-element input gives _O_(log_M_) bits, and we need to achieve all type one bits to solve the problem (there are (_k_log_k)/_4 of them), we obtain the following lower bound:

**Lemma 17.** \(k-k=\Omega\left(min\left(\frac{kw}{B}log_Mk,\frac{k}{B}logk+\frac{kw}{B}\right)\right)\).

Now we combine everything to get the proof of our PLE and sorting lower bounds.

**Proof of Theorem 8**

The lower bounds for _k-k_, _k-_\(\tilde{k}\) and _S-k_ are each a minimum of two terms; it is safe to add the respective terms as the transition between which term dominates occurs at exactly the same value of _w_ for each of the subproblems. Adding the terms for the lower bounds of _k-k_ and _S-k_ provides the \(\frac{k}{B}logS\) and \(\frac{kw}{B}log_MS\) terms in Theorem 8. Adding the terms for the lower bounds of _k-k_ and _k-_\(\tilde{k}\), and using that \(k+\tilde{k}=L/w\) provides the \(\frac{L}{wB}logS\) and \(\frac{L}{B}log_MS\) terms in Theorem 8.

## 5.3 Generalization of lower bounds to the case when _w_<sub>1</sub>_\<w_<sub>2</sub>_\<B_

So far, our assumptions on the record sizes accommodate one set of records of unit size, and the other set contains items larger than a block. But what if we have two record sizes, where both can be relatively large but still smaller than a block? In this section, we generalize the lower bound results to this case.

The number of bits required by an algorithm remains unchanged as that is an information-theoretic lower bound. It remains to see how the invariant maintained by the adversary limits the information achieved by any algorithm.

The input of a small block contains _B/w_<sub>1</sub> elements now. Since the large elements in memory have disjoint search spaces, the maximum number of bits achievable by this I/O is _B/w_<sub>1</sub>, which is the case when each of these small elements is a pivot for a unique large element. Thus we get _O(B/w_<sub>1</sub>) bits per I/O.

