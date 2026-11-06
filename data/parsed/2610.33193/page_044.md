do not actually exist due to the constraint \(2^{k_\ell}\le i<n-2^{k_\ell}\) on the starting point of gates. After all this, the number of gates in layer \(\ell\) is at least \(n/8-2^{k_\ell}\ge n/9\) for sufficiently large _n_. The number of considered layers is \((\mathrm{log}n)-(\lceil(1/2)\mathrm{log}n\rceil+1)\ge(\mathrm{log}n)/4\). Thus the number of relevant gates in the non recursive step is at least (_n_log(_n_))/36 or \(\Theta(n\mathrm{log}n)\) with the asymptotic upper bound coming from the total number of gates in the non-recursive step. Considering in the recursive step, we have:

\(C(n)=2C(n/2)+\Theta(n\mathrm{log}n)\)

Which is \(\Theta(n\mathrm{log}^2n)\) by the Master theorem.

By Lemma 5.12, each of these gates must release \(\Omega(1)\) heat in expectation. Thus the total heat dissipation of the circuit is \(\Omega(n\mathrm{log}^2n)\). To see that this bound is asymptotically tight, observe that the heat function _Q(x_<sub>1</sub>_,x_<sub>2</sub>)=1 is valid. Since there are _O(n_log<sup>2</sup>_n_) total gates in Batcher’s odd even mergesort, this choice for _Q_ gives a total of _O(n_log<sup>2</sup>_n_) expected heat released.

**Corollary 5.14.** _Let D be an ordered set and_ D _be the distribution resulting from picking n elements of D without replacement uniformly at random. Batcher’s odd-even mergesort has_ \(\Omega(n\mathrm{log}^2n)\) _circuit entropy production on input distribution_ D.

_Proof._ By Theorem 5.13 we know this circuit releases \(\Omega(n\mathrm{log}^2n)\) expected heat. The drop in entropy by sorting an input is at most log(_n_!) which is only _O(n_log_n_). Thus the released heat dominates the drop in entropy term for this circuit.

We have thus shown that Batcher’s odd even mergesort network is thermodynamically inefficient.

## 5.3 A more thermodynamically efficient sorting network

In Section 5.2.2 we showed that Batcher’s odd even mergesort is a poor choice if one is interested in optimizing the thermodynamic costs of sorting more than just bits, as the minimal expected heat released is asymptotically larger than the drop in entropy. If one is only interested in asymptotic bounds, then there is a trivial way to get a sorting network with _O(n_log_n_) expected heat release by using the AKS sorting network which has only _O(n_log_n_) gates \[AKS83\]. However, this construction has such a large constant hidden in the _O_ notation that it is unsuitable for actual implementation.

### A network sorting almost all inputs

In \[LP98\] the authors present a comparator network that sorts almost every permutation of \[_n_\] using only (3.72+_o_(1))_n_log_n_ comparator gates. We will show how this construction can be leveraged to give a sorting network that releases only _O(n_log_n_) expected heat. To start, we cite the relevant result from their paper.

**Proposition 5.15** (\[LP98\])**.** _Let n_=2_<sup>d</sup>. For every_ \(\varepsilon(d)=2^{-2^{o(\sqrt{d})}}\) _there is a deterministic (non- uniform) network of depth_ \((7.44+o(1))\cdot d\) _that sorts a uniformly random permutation of_ \[_n_\] _with probability at least_ \(1-\varepsilon(d)\).

**Remark 5.16.** _In \[LP98\] the authors actually prove a bound that works for every_ \(\varepsilon(d)=2^{-2^{o(d)}}\) _however, this stronger error bound requires invoking AKS on small subproblems. Thus the enormous constant associated with AKS would still be present in the o_(1) _term in the depth bound. Instead, we use a weaker version of their result that they explicitly mention at the end of section 6 where AKS is replaced by bitonic sort. This slightly weakens the error bounds but avoids the large constant factor in the overall cost._

