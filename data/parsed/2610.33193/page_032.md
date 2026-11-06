**Proposition 5.1** (\[Knu98\])**.** _A sorting network on n inputs from any ordered set is correct iff it correctly sorts all inputs in_ {0,1}_<sup>n</sup>._

The binary input restriction allows for comparator gates to be implemented in a more thermodynamically efficient way. This is because the inputs (0,0) and (1,1) are the unique pre-images of outputs (0,0) and (1,1) respectively, meaning that we can set _Q_(0,0)=_Q_(1,1)=0 and we only need to optimize the values of _Q_(0,1) versus _Q_(1,0) which both map to output (0,1).

**Theorem 5.2.** _When given the uniform distribution over input x in_ {0,1}_<sup>n</sup>, there is an assignment of heat function to every gate that results in the circuit releasing only O(n_) _expected heat across all gates. Moreover, the construction need only use_ 2log(_n_)+1 _distinct heat functions._

_Proof._ We start by bounding the expected heat released in each layer of the non-recursive merge step. We will use three different types of heat functions in this construction. _Q_<sup>unif</sup> is defined such that _Q_<sup>unif</sup>(_x<sub>i</sub>,x<sub>j</sub>_)=0 when _x<sub>i</sub>=x<sub>j</sub>_ and _Q_<sup>unif</sup>(_x<sub>i</sub>,x<sub>j</sub>_)=1 when \(x_i\neq x_j\). This is an unbiased heat function that we will use either when inputs (0,0) and (1,1) are overwhelmingly common or when the number of gates in a group is sufficiently small. This heat function has the advantage that neither input (0,1) or input (1,0) releases too much heat in expectation. We also define \(Q_\varepsilon^{(0,1)}\) parameterized by \(\varepsilon\le 1/2\) such that \(Q_\varepsilon^{(0,1)}(0,0)=Q_\varepsilon^{(0,1)}(1,1)=0\), \(Q_\varepsilon^{(0,1)}(0,1)=log(1/(1-\varepsilon))\), and \(Q_\varepsilon^{(0,1)}(1,0)=log(1/\varepsilon)\). Intuitively, these functions are used to reduce the expected heat released by gates where the first input is heavily biased towards input 0 while the second input is heavily biased towards input 1. In particular, if a gate receives a marginal induced input distribution where the probability of input (1,0) is at most \(\varepsilon\le 1/2\), then the expected heat released by this gate is at most \((1-\varepsilon)log(1/(1-\varepsilon))+\varepsilon log(1/\varepsilon)\le 2\varepsilon log(1/\varepsilon)\). Likewise we define \(Q_\varepsilon^{(1,0)}\) such that \(Q_\varepsilon^{(1,0)}(a,b)=Q_\varepsilon^{(0,1)}(b,a)\) for \(\varepsilon\le 1/2\). These gates are used when the first input is heavily biased towards 1 while the second input is heavily biased towards 0. By the same reasoning as \(Q_\varepsilon^{(0,1)}\), if a<tbc>

Layer O
Layer 1
Layer2
layer3
Layer log n (=4)
1
N/2
i
N/2
n/2
n-1
(=15)

Figure 2: Recursive case of Batcher’s odd-even mergesort network for 16 inputs. The base case is _n_=4 is shown in Figure 3.

