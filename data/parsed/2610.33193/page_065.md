• Lower gates: Both inputs are from wires in the range \[_n/_2_,...,n_-1\]. The reasoning is similar to that for the upper gates, with heat function \(\tilde{Q}^{(1,1)}(2\mathrm{exp}(-n^\alpha/4))\) and expected heat dissipation \(O(n^{(1+5\alpha)/2})\).<tbc>

• Crossover gates: One input wire is in the range \[0_,...,n/_2-1\] and the other is in the range \[_n/_2_,...,n_-1\]. The reasoning is similar to the previous two cases, with heat function \(\tilde{Q}^{(0,1)}(2\mathrm{exp}(-n^\alpha/4))\) and expected heat dissipation \(O(n^{(1+5\alpha)/2})\).

Summing up over upper, lower and crossover gates, the total heat dissipation per layer in the range 3 to log<sub>2</sub>_n_ is \(O(n^{(1+5\alpha)/2})\), and three different heat functions are used.

**Theorem B.1.** _With respect to the overwriting circuit model, when given the uniform distribution over inputs in_ {0,1}_<sup>n</sup>, there exist valid heat functions for each gate in Batcher’s odd-even mergesort such that the expected total heat release across all gates is O(n)._

_Proof._ Adding up the expected heat dissipation for layers 1 through log<sub>2</sub>_n_, we see that the total expected heat dissipation is<tbc>

\(O(n^{(1+\alpha)/2})+O(n^{(1+5\alpha)/2}\mathrm{log}_2n),\)

<tbc>where the first term accounts for layers 1 and 2, and the second term accounts for gates in layers 3 to log<sub>2</sub>_n_. The total heat dissipation for the whole circuit is therefore given by the recurrence

\(\mathsf{Q}(n)=2\mathsf{Q}(n/2)+O(n^{(1+5\alpha)/2}\mathrm{log}_2n)\)

and so is _O(n_) when \(\alpha<1/5\). The number of different heat functions used is _O_(1) per layer, and so is _O_(log_n_) in total for the network.

## C Re-deriving mismatch costs

In \[WK20, YCW26, YYW26\] the authors use the language of _mismatch costs_ to lower bound the entropy production of implementing gates in a Boolean circuit. Instead of explicitly defining heat functions, they start with the assumption that some distribution over inputs D<sup>∗</sup> minimizes the entropy production of the desired computation. Their main observation is that entropy production can be decomposed as the sum of a term characterizing how far the actual input distribution is from D<sup>∗</sup> and a term characterizing the inefficiencies even when using D<sup>∗</sup> as the input distribution. We start by characterizing how D<sup>∗</sup> can be derived from a given heat function.

**Lemma C.1.** _Let f be an arbitrary function with domain D and_ \(Q:D\rightarrow\mathbb{R}_{\ge 0}\cup\{\infty\}\) _be a valid heat function for computing f. Then any conditional input distribution_ \(\mathcal{D}_{|f^{-1}(y)}^*\) _that minimizes the entropy production of applying a gate g computing f with heat function Q must satisfy_

\(\mathcal{D}_{|f^{-1}(y)}^*=(\mathcal{G}_Q)_{|f^{-1}(y)}\)

_on all y where_ (G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub> _is defined. If_ (G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub> _is undefined, then all conditional input distributions have infinite entropy flow._

_Proof._ By the definition of entropy production, we have that for every _y_:<tbc>

\(\mathsf{EP}_g(\mathcal{D}_{|f^{-1}(y)})=-\mathcal{S}(\mathcal{D}_{|f^{-1}(y)})+\mathbb{E}_{x\sim\mathcal{D}_{|f^{-1}(y)}}[Q(x)].\)

