## Layer 2

There are _n/_4 comparator gates in layer 2; we number them by the index of their upper wire, from _n/_4 to _n/_2-1. The _i_’th gate has input wires _i_ and _i+n/_4. We partition the gates into three regions: a narrow band of gates at the top, a large middle region, and a narrow band at the bottom.

• Top narrow band: \(i\in[n/4,(n+n^{(1+\alpha)/2})/4]\). Using the heat function \(\tilde{Q}^\mathrm{unif}\), the expected heat dissipation for each gate is at most 2.<tbc>

• Middle region: \(i\in[(n+n^{(1+\alpha)/2})/4,(n-n^{(1+\alpha)/2})/2]\). It follows from Proposition 2.14 that \(\mathrm{Pr}[w_i(1)=1]=\mathrm{Pr}[\mathrm{min}\{w_i(0),w_{n/2+i}(0)\}=1]=\mathrm{Pr}[w_i(0)=1]\mathrm{Pr}[w_i(0)=1]\ge 1-2\mathrm{exp}(-n^\alpha/4)\), and \(\mathrm{Pr}[w_{i+n/4}(1)=0]=\mathrm{Pr}[\mathrm{max}\{w_{i-n/4}(0),w_{i+n/4}(0)\}=0]\ge\mathrm{Pr}[w_{i-n/4}(0)=0]\mathrm{Pr}[w_{i+n/4}(0)=0]\ge 1-2\mathrm{exp}(-n^\alpha/4)\). So each comparator gate in this range has input (1,0) with probability at least \(1-4\mathrm{exp}(-n^\alpha/4)\). Using the heat function \(\tilde{Q}^{(0,1)}(4\mathrm{exp}(-n^\alpha/4))\), the expected heat release of each gate is \(O(n^\alpha\mathrm{exp}(-n^\alpha/4))=O(\mathrm{exp}(-n^\alpha/5))\).<tbc>

• Bottom narrow band: \(i\in[(n-n^{(1+\alpha)/2})/2,n/2-1]\). Using the heat function \(\tilde{Q}^\mathrm{unif}\), the the expected heat dissipation for each gate is at most 2.

Therefore, the total expected heat dissipation for layer 2 is dominated by the narrow bands, and is \(O(n^{(1+\alpha)/2})\), using two different types of heat functions.

## Layers 3 and beyond

We will reuse Claim 5.3 from the proof of Theorem 5.2 which shows that with high probability, the number of 1-valued wires in the range \[0_,n/_2-1\], and the number of 0-valued wires in the range \[_n/_2_,n_-1\], is small.

**Claim 5.3.** _Let_ \(\alpha\in(0,1)\)_. Except with probability_ \(3ne^{-n^\alpha/4}/2\)_, the following hold for every_ \(\ell\ge 2\):

1. _The number of i such that i\<n/_2 _and_ \(w_i(\ell)=1\) _is at most_ \(n^{(1+\alpha)/2}/2\).<tbc>

_2._ _The number of i such that_ \(i\ge n/2\) _and_ \(w_i(\ell)=0\) _is at most_ \(n^{(1+\alpha)/2}/2\).

We partition gates of each layer \(\ell,3\le\ell\le\mathrm{log}_2n\), into three groups: upper gates, lower gates, and crossover gates, defined in the cases below. In Figure 2, where _n_=16, when _l_=3 there are two upper gates, two lower gates, and two crossover gates.

• Upper gates: Both inputs are from wires in the range \[0_,...,n/_2-1\]. We assign them the heat function \(\tilde{Q}^{(0,0)}(2\mathrm{exp}(-n^\alpha/4))\). On input (0,0), such gates have expected heat dissipation \(O(\mathrm{exp}(-n^\alpha/4))\), and otherwise they have expected heat dissipation \(O(n^\alpha\mathrm{log}_2(1/\mathrm{exp}(-n^\alpha/4)))=O(n^{2\alpha})\). It follows from Claim 5.3 that with probability \(1-O(\mathrm{exp}(-n^\alpha/5))\), the number of upper gates that don’t have input (0,0) is \(O(n^{(1+\alpha)/2})\). In this scenario, the total (conditional) expected heat dissipation of the upper gates of layer 3 is<tbc>

<tbc>\(O(n\mathrm{exp}(-n^\alpha/4))+O(n^{(1+\alpha)/2}n^{2\alpha})=O(n^{(1+5\alpha)/2}).\)<tbc>

<tbc>With the remaining probability \(O(\mathrm{exp}(-n^\alpha/5))\), there may be more gates that don’t have input (0,0); in the worst case none of the _n/_8 gates has input (0,0). In this alternative scenario the conditional expected heat dissipation is \(O(n^{1+2\alpha})\). Taking the expectation over the two scenarios, the total heat dissipation for the upper gates of layer 3 is<tbc>

<tbc>\((1-O(\mathrm{exp}(-n^\alpha/5)))O(n^{(1+5\alpha)/2})+O(\mathrm{exp}(-n^\alpha/5)n^{1+2\alpha})=O(n^{(1+5\alpha)/2}).\)<tbc>

