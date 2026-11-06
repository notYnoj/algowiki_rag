\(=log\left((Pr_\mathcal{D}[(x_1,x_2)]+Pr_\mathcal{D}[(x_2,x_1)])/Pr_\mathcal{D}[(x_1,x_2)]\right)\)<br>
\(=log(1+Pr_\mathcal{D}[(x_2,x_1)]/Pr_\mathcal{D}[(x_1,x_2)]).\) (5)

This means that to prove a \(\Omega(nlog^2n)\) lower bound on the expected heat release, it is sufficient to show that there are \(\Omega(nlog^2n)\) comparator gates where, on their induced marginal input distribution D, for every pair \((x_1,x_2)\in supp(\mathcal{D})\) we have that there are universal constants _a,b\>_0 such that \(a\le\frac{Pr_\mathcal{D}[(x_1,x_2)]}{Pr_\mathcal{D}[(x_2,x_1)]}\le b\). In particular, the gates that we show have this property will be ones that are centrally located and in the later layers. An empirical plot of the expected heat released per gate in Batcher’s odd-even mergesort when _n_=256 is shown in Fig. 4.

## Notation and network properties

In order to show that these gates have similar probabilities for inputs (_x_<sub>1</sub>_,x_<sub>2</sub>) and (_x_<sub>2</sub>_,x_<sub>1</sub>), we need some properties about the Batcher’s odd-even mergesort network. Some of the stated properties below are already established (see, e.g., \[Bat68, Knu98\]), but the key technical lemma that we require (i.e., Lemma 5.11) appears to be new.

**Fact 5.6.** _For every_ \(0\le r<2^{k_\ell}\)_, we have that_

\(\{w_j(0)|j\equiv rmod2^{k_\ell}\}=\{w_j(\ell)|j\equiv rmod2^{k_\ell}\}.\)

_Proof._ For every \(\ell'\le\ell\) we know that every \((i,j)\in G_{\ell^\prime}\) has \(2^{k_\ell}|(j-i)\). Thus, comparator gates up to level \(\ell\) can only shift the index of elements within these congruency classes.

The following basic fact about Batcher’s odd-even sorting network follows directly from the original proof sketch of the network’s correctness by Batcher \[Bat68\]. Hinze and Martin \[HM18\] give a proof of this result similar to the one we include here.

**Proposition 5.7.** _After layer_ \(\ell\) _of Batcher’s odd-even mergesort, the values stored on wires whose indices are congruent mod_ \(2^{k_\ell}\) _are in their relative sorted order._



Figure 4: A plot of empirically calculated expected released heat per gate for sorting randomly permuted integers 0_,...,n_-1. The algorithm in Lemma 4.8 is used to find approximate heat functions for each gate and then a fresh source of randomness is used to compute the empirical expected heat release. Teal indicates low heat release and orange high heat release. While it appears that there are many orange gates at the beginning of each recursive step, in the later layers this number is only _O(n_). Thus we use the centrally located orange gates in the later layers of each recursive step to obtain our bound.

