<tbc>gate receives a marginal induced input distribution where the probability of input (0,1) is at most \(\varepsilon\le 1/2\), then the expected heat released by this gate is at most \(2\varepsilon log(1/\varepsilon)\). In each layer \(\ell\), we split gates up into one of three regions depending on the value _i_ for the gate \((i,i+2^{k_\ell})\) and use the same heat function for every gate in the region. We use closed intervals on regions to cleanly handle non-integer values; this has the side-effect of counting some wires as belonging to multiple regions and thus using different heat functions. We will analyze such wires as being a part of both regions and account for costs associated with both heat functions. This only increases our upper bound and significantly simplifies the analysis. Let \(\alpha\) be some value in (0,1) that we pick later and for now assume that \(n\ge 32\).

## Layer 1

In this layer, we have that \(2^{k_\ell}=n/2\). The _upper region_ contains all gates with \(i\in\left[0,(n-n^{(1+\alpha)/2})/4\right]\) and uses the heat function _Q_<sup>unif</sup>. Since we know that \(w_0(0)\le\dots\le w_{n/2-1}(0)\) and \(w_{n/2}(0)\le\dots\le w_{n-1}(0)\) and the input was distributed uniformly at random, Proposition 2.14 gives us that the probability that _w<sub>i</sub>_(0)=1 as well as the probability that _w_<sub>_i+n/_2</sub>(0)=1 are each at most \(e^{-n^\alpha/4}\). Thus by a union bound, the probability that gate (_i,i+n/_2) receives input (0,0) is at least \(1-2\cdot e^{-n^\alpha/4}\) and so the expected released heat by every such gate is at most \(2e^{-n^\alpha/4}\).

The _middle narrow band_ contains all gates with \(i\in\left[(n-n^{(1+\alpha)/2})/4,(n+n^{(1+\alpha)/2})/4\right]\) and uses the heat function _Q_<sup>unif</sup>. There are a total of \(n^{(1+\alpha)/2}/2+1\) gates in this band that each release at most 1 expected heat.

The _lower region_ contains all gates with \(i\in\left[(n+n^{(1+\alpha)/2})/4,n/2-1\right]\) and uses the heat function _Q_<sup>unif</sup>. Using a symmetrical argument to the upper region case, Proposition 2.14 gives us that the expected released heat of every gate in this region is at most \(2e^{-n^\alpha/4}\).

Putting all of this together, the heat released in the first layer is at most \(n^{(1+\alpha)/2}/2+2ne^{-n^\alpha/4}+1\).

## Layer 2

In this layer, we have that \(2^{k_\ell}=n/4\). The _upper narrow band_ contains all gates with \(i\in\left[n/4,(n+n^{(1+\alpha)/2})/4\right]\) and uses the heat function _Q_<sup>unif</sup>. There are at most \(n^{(1+\alpha)/2}/4+1\) gates in this band that each only release at most 1 expected heat.

The _middle region_ contains all gates with \(i\in\left[(n+n^{(1+\alpha)/2})/4,(n-n^{(1+\alpha)/2})/2\right]\) and uses the heat function \(Q_\varepsilon^{(1,0)}\) for some \(\varepsilon\le 1/2\) specified later. By the construction of Batcher’s odd-even mergesort, we know that _w_<sub>_i+n/_4</sub>(1)=max(_w_<sub>_i+n/_4</sub>(0)_,w_<sub>_i-n/_4</sub>(0)). Thus, by Proposition 2.14, the probability that _w_<sub>_i+n/_4</sub>(1)=1 is at most the probability that _w_<sub>_i+n/_4</sub>(0)=1 or _w_<sub>_i-n/_4</sub>(0)=1 which is at most \(2e^{-n^\alpha/4}\). Thus the probability each gate in this region receives the input (0,1) is also at most \(2e^{-n^\alpha/4}\). Picking \(\varepsilon=2e^{-n^\alpha/4}\) and \(\alpha=1/2\) gives us that \(\varepsilon\le 1/2\) and thus the expected heat released by any gate in this region is at most \(log(e)e^{-n^\alpha/4}n^\alpha\).

The _bottom narrow band_ contains all gates with \(i\in[(n-n^{(1+\alpha)/2})/2,n/2-1]\) and uses the heat function _Q_<sup>unif</sup>. There are only \(n^{(1+\alpha)/2}/2\) gates in this band that each only release at most 1 expected heat.

Putting all of this together, the heat released in the second layer is at most \(n^{(1+\alpha)/2}/2+log(e)e^{-n^\alpha/4}n^{1+\alpha}+1\).

## Layer 3 and beyond

The following claim gives us that, after layer 2, most 0’s are already in the top half of wires and most 1’s are already in the bottom half of wires.

**Claim 5.3.** _Let_ \(\alpha\in(0,1)\)_. Except with probability_ \(3ne^{-n^\alpha/4}/2\)_, the following hold for every_ \(\ell\ge 2\):<tbc>

