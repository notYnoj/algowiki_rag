_Proof._ The number of bits given due to comparisons with small elements already in memory is _O_(log_M_). In each of the three cases an additional _O_(log(_M/w_)) bits are given. Thus, the total number of bits given by the adversary during the I/O of a large element is _O_(log_M_).

## 5.2 Putting It All Together: getting lower bounds for _S-k_, _k_-\(\tilde{k}\) and _k-k_

### 1) _S-k_ Lower Bound.

The proof rests on the following action of the adversary: in the very beginning, the adversary gives the algorithm the extra information that the _i_th largest large element lies somewhere between \(s_{(i-1)\alpha}\) and \(s_{i\alpha}\), where \(\alpha=S/k\). In other words, the adversary tells the algorithm that the large elements are equally distributed across S, one in each chunk of size _S/k_ in S.

This deems the invariant of large elements in main memory having disjoint search intervals automatically satisfied.

Because any algorithm that solves _S-k_ must achieve \(\Omega(klog(S/k))\) bits of information, we have that

**Lemma 14.** \(S-k=\Omega\left(min\left(\frac{kw}{B}log_M\frac{S}{k},\frac{k}{B}log\frac{S}{k}+\frac{kw}{B}\right)\right).\)

### 2) _k_-\(\tilde{k}\) Lower Bound.

To solve _k_-\(\tilde{k}\), an algorithm needs to learn \(klog\tilde{k}\) bits of information. Using the adversary strategy we described, we obtain the following lower bound:

**Lemma 15.** _k_-\(\tilde{k}\) = \(\Omega\left(min\left(\frac{\tilde{kw}}{B}log_Mk,\frac{\tilde{k}}{B}logk+\frac{\tilde{kw}}{B}\right)\right).\)

### 3) _k-k_ Lower Bound.

To solve _k-k_, an algorithm needs to learn _k_log_k_ bits of information. In the _k-k_ problem, we expect to produce the perfect interleaving of the small and large elements in the final sorted order. That is, _each element lands in its own leaf of_ T .

Therefore, the adversary does not posses the freedom to route elements down the tree at all times using the strategy we described. Instead, the strategy is used for a fraction of total bits the algorithm learns, and the remaining fraction is used to make up for the potential imbalance created by sending more elements to the left or to the right. We call these _type one_ and _type two_ bits, respectively. Late bits are effectively given away for free by the adversary.

More formally, we define the _node capacity (c<sup>T</sup>(v))_ as the number of large elements that pass through _v_ during the execution of an algorithm. If the<tbc>

