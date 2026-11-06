We observe, however, that for a sequence to be maximally uneven on a particular scale _s_, the density of 1’s has to be maximally different (i.e., close to either 0 or 1) at each block of width _M_<sup>_s_-1</sup>, and, intuitively, such density requirement makes it more difficult for the sequence to be maximally uneven on the remaining smaller scales. For the simplest example, suppose _n_=4 and _M_=2. We have two scales corresponding to blocks of size 2 and 4. The largest total deviation on the larger scale is achieved by _A_={0,0,1,1} or _A_={1,1,0,0}, but for both sequences the total deviations on the smaller scale become zero. We prove that this is not a coincidence:

(Ideal and informal version of Lemma 4.1) For all sequences with each entry being _O_(1) in absolute value, the overall total unevenness is roughly bounded by \(n\sqrt{\mathrm{log}_Mn}\), i.e., roughly \(\sqrt{\mathrm{log}_Mn}\) smaller than the naïve _O(n_log_<sub>M</sub>n_) upper bound. Moreover, if the total sum of the sequence is \(\varepsilon n\) and \(\varepsilon\) is at least 2<sup>-polylog(_n_)</sup>, then the total unevenness is roughly bounded by \(\varepsilon n\sqrt{\mathrm{log}_Mn}\).

## Proof Sketch

We now give a sketch of the proof for _M_=2, which contains all the techniques we need for proving the more general case but is much less tedious. The key idea is to decompose the total tree deviation into the contribution of each element, and then bound the contribution from an average element using a probabilistic argument.

Towards the goal of decomposing the total tree deviation to individual elements’ contributions, we first transform the sequence into another sequence with the same total tree deviation. Suppose we have a sequence _A_ with each entry being _O_(1) with total sum \(\varepsilon n\). Let _S_:=log<sub>2</sub>_n_ be the number of scales. For each scale \(s\in[S]\), we go through all _n/_2<sup>_S-s_+1</sup> intervals (_l,r_\] of form \(\left(2^{S-s+1}\cdot k,2^{S-s+1}\cdot(k+1)\right]\). Fix a scale _s_. For every interval (_l,r_\] on scale _s_, we divide it into two halves (_l,(l+r)/_2\] and ((_l+r)/_2_,r_\]. We let \(\sigma_L:=\sum_{l<x\le(l+r)/2}a_x\) be the sum on the left half, and \(\sigma_R:=\sum_{(l+r)/2<x\le r}a_x\) be the sum on the right half. In the case where _M_=2, we can see that the contribution from the interval to the tree total deviation is

\(|\sigma_L-(\sigma_L+\sigma_R)/2|+|\sigma_R-(\sigma_L+\sigma_R)/2|=|\sigma_L-\sigma_R|.\)

In other words, the local unevenness is simply the difference between the sums of the two halves. Notice that if we swap the two halves to obtain a new sequence, the total tree deviation does not change:

(_l,r_\] is the only interval where sums of the two halves are swapped (which does not change their difference) -- for other intervals, the sums of the two halves remain identical.

We can apply this swap to every applicable interval. Therefore, without loss of generality, we can assume that \(\sigma_L<\sigma_R\), and the contribution from the interval to the tree total deviation is

\(\sigma_R-\sigma_L=\left(\sum_{l<x\le(l+r)/2}-a_x\right)+\left(\sum_{(l+r)/2<x\le r}+a_x\right).\)

Thus, for every \(x\in(l,r]\), it contributes -_a<sub>x</sub>_ if _x_ is in the first half, and +_a<sub>x</sub>_ if _x_ is in the second half. Since (_l,r_\] is a scale-_s_ interval, the sign of _x_’s contribution depends only on the _s_-bit binary representation of (_x_-1): on scale-_s_, _x_ contributes -_a<sub>x</sub>_ if (_x_-1)’s _s_-th bit is 0, and +_a<sub>x</sub>_ if (_x_-1)’s _s_-th bit is 1. Summing up the total contribution from each index _x_ for each scale _s_, we have

\(\text{tree total deviation}=\sum_{1\le x\le n}a_x\left(\text{number of 1’s in}(x-1)\text{in binary) - (number of 0’s in}(x-1)\text{in binary)).\)

