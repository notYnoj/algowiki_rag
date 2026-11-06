## 3 Sorting and Batched Predecessor in External Memory with Size-Priced Information

The input to the two-sized sorting and batched predecessor problems are _S_={_s_<sub>∗</sub>} (the small records) and \(L=\{\ell_*\}\) (the large records, each of size \(1<w\le M/2\)). A set of large elements forms a _stripe_ if for each pair of large elements \(\ell_i\) and \(\ell_j\) in the stripe, there does not exist a small element between \(\ell_i\) and \(\ell_j\) in the final sorted order. Let _k_ be the number of large-element stripes, and let the large-element stripes be L<sub>1</sub>,L<sub>2</sub>_,...,_L_<sub>k</sub>_, as they are encountered in the ascending sorted order. The parameters in the complexity analysis of sorting and batched predecessor are thus _S_, _L_, _w_, _k_, and \(\{L_i\}_{i=1}^k\).

**Definition 2** (_Two-Sized Sorting_ Sort(_S,L_))**.** _The input is an (unsorted) set of elements_ \(N=S\cup L\)_. Set S consists of S unit-size elements, and L consists of L/w elements, each of size w, where_<sup>3</sup> \(B\le w\le M/2\)_. The output comprises the elements in N, sorted and stored contiguously in external memory._

**Definition 3** (PLE_-Placement of Large Elements:_)**.** _The input is the_ sorted _set of small elements_ S={_s_<sub>1</sub>_,s_<sub>2</sub>_,...,s<sub>S</sub>}, and the_ unsorted _set of large elements_ \(\mathcal{L}=\{\ell_1,\ell_2,\dots,\ell_{L/w}\}\)_. In the output, elements in_ S _are sorted, and elements in L are sorted according to which stripe they belong to, but arbitrarily ordered within their stripe._

The following theorem relates the complexities of the sorting and the batched predecessor problem.

**Theorem 4** (**Sorting complexity**)**.** _Denote by_ PLE(_S,L_) _the complexity of the_ PLE _problem. Then the I/O complexity of Two-Sized Sorting_ Sort(_S,L_) _is_

\(\Theta\left(\frac{S}{B}log_{M/B}\frac{S}{B}+\text{PLE}\left(S,L\right)+\left(\sum_{i=1}^k\left(\frac{L_i}{B}log_{M/w}\frac{L_i}{w}\right)+\frac{L}{B}\right)\right).\)

We will use this section to prove the first and the third term of the Theorem 4. It is easy to see that PLE(_S,L_) is an instance of Sort(_S,L_) that starts with more information (sorted small elements), and requires less (just the contents of the stripes, unsorted).

<sup>3</sup>We overload notation for convenience of presentation. We assume \(w\ge B\) also for the convenience of presentation. Our bounds hold for any \(1<w\le M/2\); we extend our results to this entire range in Appendix 5.3.

