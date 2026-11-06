The idea is that if no \(k\in A\) encloses \(\ell\) for some _t_, then the endpoints of each _k_-interval form a fraction of denominator _k_ contained strictly within the \(\ell\)-interval of _t_. As a result, we have a contiguous interval _I_ containing a fraction of denominator _k_, and _I_ is contained strictly within the \(\ell\)-interval of _t_. As such, _I_ cannot contain a fraction of denominator \(\ell\). This is illustrated in Fig. 16. The formal proof also considers the edge cases involving the endpoints of the intervals.

For Claim 70, we prove the following proposition.

**Proposition 71.** _The following statements are equivalent for any half-open interval_ [_c,d_) _and positive integer k:_

(_1)_ [_c,d_) _is contained within a k-interval._<tbc>

(_2)_ (_c,d_) _is contained within a k-interval._<tbc>

_(3)_ (_c,d_) _contains no fraction of denominator k._

_Proof._ \((1)\Longrightarrow(2)\). This follows as (_c,d_) is a subset of [_c,d_).

(2) \(\Longrightarrow(3)\). Suppose (_c,d_) is contained in the _k_-interval [_n/k,(n_+1)_/k_). The interval (_c,d_) cannot contain a fraction of denominator _k_, otherwise said fraction would be strictly between _n/k_ and (_n_+1)_/k_.

(3) \(\Longrightarrow(1)\). Let _n/k_ be the largest fraction of denominator _k_ less than or equal to _c_. It must be true that \((n+1)/k\ge d\), since (_n_+1)_/k_ cannot be contained in (_c,d_). Therefore, [_c,d_) is contained in the _k_-interval [_n/k,(n_+1)_/k_).

From this, we can prove Claim 70.

k = 2
k = 3
l = 5

t
k-intervals for k E A
l-interval
I

Figure 15: Example 69

Figure 16: _I_ contains a fraction of denominator _k_ for all _k_, but no fraction of denominator \(\ell\).

