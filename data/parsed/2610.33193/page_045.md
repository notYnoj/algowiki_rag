In addition to a depth bound that is linear in _d_, Proposition 5.15 has only a linear number of gates per layer. Thus the overall gate count is only _O(n_log_n_). We will only need to instantiate this with \(\varepsilon(d)=2^{-log(d)-loglog(d)}=1/(log(n)loglog(n))\). The following corollary suffices for our use case.

**Corollary 5.17.** _Let n be a power of two, D be an arbitrary ordered set and_ D _be the distribution over inputs given by sampling n elements of D uniformly at random without replacement. Then there exists a deterministic (non-uniform) network with O(n_log_n_) _gates that correctly sorts inputs x_<sub>1</sub>_,...,x<sub>n</sub>_∼D _except with probability at most_ 1/(log(_n_)loglog(_n_)).

## A sorting network with low expected released heat

Now we show that the network in Corollary 5.17 can be used as a subroutine in a thermodynamically efficient sorting network. Intuitively, this network sorts most inputs using only a small number of gates. This allows it to be followed by a larger sorting network which uses a heat function that takes advantage of the fact that its input is often already in sorted order.

**Theorem 5.18.** _Let D be an arbitrary ordered set and_ D _be the distribution over inputs given by sampling n elements of D uniformly at random without replacement. There is a thermodynamic sorting network_ C _with O(n_log<sup>2</sup>_n_) _gates that are each augmented with one of two heat functions Q_<sub>0</sub>_,Q_<sub>1</sub> _such that, on input distribution_ D_, the expected heat dissipation of_ C _is O(n_log_n)._

_Proof._ We fix C to be the concatenation of the sorting network in Corollary 5.17 on all _n_ wires (call this C<sub>0</sub>) followed by Batcher’s odd even mergesort on the same _n_ wires (call this C<sub>1</sub>). Since Batcher’s odd even mergesort is a sorting network, we know that C is also a sorting network. We augment every gate in C<sub>0</sub> with the heat function _Q_<sub>0</sub>(_x_<sub>1</sub>_,x_<sub>2</sub>)=1. Since C<sub>0</sub> has _O(n_log_n_) gates, the expected heat dissipation of this component is also _O(n_log_n_). Importantly, after running C<sub>0</sub>, the input is already sorted except with probability at most 1/(log(_n_)loglog(_n_)).

We augment every gate in C<sub>1</sub> with the heat function:<tbc>

\(Q_1(x_1,x_2)=\left\{\begin{array}{ c c }
1/log(n) & x_1\le x_2 \\
log\left(\frac{1}{1-2^{-1/log(n)}}\right) & x_1>x_2
\end{array}\right.\)

<tbc>The validity of _Q_<sub>1</sub> follows from Lemma 2.22. When C<sub>1</sub> receives an already sorted input from C<sub>0</sub>, this choice of _Q_<sub>1</sub> implies that every gate will dissipate only 1/log(_n_) heat. Since C<sub>1</sub> has _O(n_log<sup>2</sup>_n_) total gates, the expected released heat conditioned on C<sub>0</sub> sorting its input is only _O(n_log_n_). Conditioned on C<sub>0</sub> failing to sort its input, some gates in the network might release up to

\(-log(1-2^{-1/logn})=-log(1-e^{-\frac{ln2}{logn}})\)<br>
\(=-log\left(\frac{ln2}{logn}\right)-log\left(\frac{1-e^{-\frac{ln2}{logn}}}{\frac{ln2}{logn}}\right)\)<br>
\(=loglog(n)-log(ln(2))-log\left(\frac{1-e^{-\frac{ln2}{logn}}}{\frac{ln2}{logn}}\right)\)<br>
\(=loglog(n)-log(ln(2))+o(1)\text{since}lim_{x\rightarrow 0}\frac{1-e^{-x}}{x}=1\)<br>
\(=O(loglogn)\)

