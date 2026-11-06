**Lemma 5.** \(\text{Sort}\left(S,L\right)=\Omega\left(\frac{S}{B}log_{M/B}\frac{S}{B}\right)\).

_Proof._ We denote by _p_ the total number of permutations that any algorithm for Two-Sized Atomic-Key Sorting must distinguish between in order to sort. We bound _p_ in terms of the number of large-element stripes _k_:

\(p\ge\frac{S!}{(B!)^{S/B}}\genfrac(){pt}{2}{S-1}{k}\left(\frac{L}{w!}\right)\genfrac(){pt}{2}{L/w-1}{k-1}.\)

The four factors that comprise the right side include (1) sorting _S_ (after sorting within the small blocks, the total number of permutations goes down by a factor of (_B_!)<sup>_S/B_</sup>), (2) choosing the _k_ locations for stripes within _S_, (3) sorting _L_ and (4) forming _k_ large-element stripes by choosing _k_-1 delimiters in the sorted _L_.

We can assume that the elements in memory are sorted at all times, because maintaining this order requires no additional I/Os. The number of remaining permutations goes down by at most \(\genfrac(){pt}{2}{M}{B}\) after one memory transfer, thus a lower bound on the number of I/Os to sort is \(\text{sort-lower}(N)=\Omega\left(logp/log\genfrac(){pt}{2}{M}{B}\right)\). Using that \(p\ge\frac{S!}{(B!)^{S/B}}\), and that \(log\genfrac(){pt}{2}{M}{B}=\Theta(Blog(M/B))\), we get

\(\text{sort-lower}(N)=\Omega\left(\frac{SlogS-SlogB}{Blog(M/B)}\right)=\Omega\left(\frac{S}{B}log_{M/B}\frac{S}{B}\right),\)

concluding the proof.

The third term concerns sorting the stripes _L<sub>i</sub>_ of large elements. Although this is same-size sorting, we need a slight generalization of the classical Aggarwal and Vitter \[1\] result for records of size _w\>_1.

**Lemma 6** (Aggarwal and Vitter)**.** _Consider an external-memory algorithm A that sorts the total volume V of V/w elements, each of size w._

1. _If_ \(1\le w<B\)_, A requires_ \(\Omega\left(\frac{V}{B}log_{M/B}\frac{V}{B}\right)\) _block transfers._<tbc>

_2._ _If_ \(w\ge B\)_, A requires_ \(\Omega\left(\frac{V}{B}log_{M/w}\frac{V}{w}\right)\) _block transfers._

**Remark:** The third term in the bound in Theorem 4 is derived by substituting _V=L<sub>i</sub>_ in the above lemma, and adding all the lower bounds (since sorting stripe _i_ is independent of sorting stripe _j_).

