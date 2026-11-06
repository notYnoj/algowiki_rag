## 4. The number of unitaries

In this section, we show that piecewise-monotone families have piecewise-constant truncations and count their factors (Lemma 3.4 and Theorem 3.11). Changes occur only when an entry’s real or imaginary part reaches or crosses a multiple of 2<sup>-_k_</sup>, so counting these crossings bounds the number of pieces.

**Definition 4.1.** The _coordinates_ of a \(d\times d\) Hermitian matrix are the real and imaginary parts of its entries on and above the diagonal, _d_<sup>2</sup> of them once the vanishing imaginary parts on the diagonal are dropped. A coordinate _h_ of _H_ is a real function of _t_, and 2_<sup>k</sup>_\[_h(t_)\]_<sub>k</sub>_ is its _grid level_. A family is _piecewise monotone_ if its coordinates are monotone on each interval of a finite partition.

**Proposition 4.2.** _Let_ \(k\ge 0\) _be an integer and_ \(0=\xi_0<\xi_1<\cdots<\xi_N=T\) _be times such that every coordinate of H is monotone on each interval_ \([\xi_r,\xi_{r+1}]\)_. Then H_<sup>(_k_)</sup> _is piecewise constant, with at most_

\(\sum_{r=0}^{N-1}\big(1+\sum_h\big\lceil 2^k\left|h(\xi_{r+1})-h(\xi_r)\right|\big\rceil\big)\)

_pieces, the inner sum running over the coordinates of H._

_Proof._ Fix \([a,b]=[\xi_r,\xi_{r+1}]\). By Hermiticity, the grid levels _v<sub>h</sub>(t_)=2_<sup>k</sup>_\[_h(t_)\]_<sub>k</sub>_ determine _H_<sup>(_k_)</sup>(_t_). Since truncation preserves monotonicity, each _v<sub>h</sub>_ is monotone, so \(c(t)=\sum_h\left|v_h(t)-v_h(a)\right|\) is nondecreasing and increases whenever any _v<sub>h</sub>_ changes. Thus, _H_<sup>(_k_)</sup> is constant on each level set of _c_, an interval since _c_ is nondecreasing, and _c_ takes values in {0_,...,c(b_)}. Discard singleton level sets, since values at piece endpoints do not matter (Section 2). The remaining intervals are adjacent, since finitely many singletons cannot cover a positive-length gap, and their interiors give the pieces, at most one per value of _c_.

Truncation satisfies \(2^k([y]_k-[x]_k)\le\left\lceil 2^k(y-x)\right\rceil\) whenever \(x\le y\). For \(0\le x\le y\), this is the floor-difference inequality \(\left\lfloor 2^ky\right\rfloor-\left\lfloor 2^kx\right\rfloor\le\left\lceil 2^k(y-x)\right\rceil\). For \(x\le y\le 0\), it follows from the nonnegative case for \(-y\le-x\) by oddness, and for opposite signs, \(2^k([y]_k-[x]_k)=\left\lfloor 2^ky\right\rfloor+\left\lfloor 2^k\left|x\right|\right\rfloor\le 2^k(y-x)\). Applying this to each monotone _h_ gives

\(\#\{\text{pieces on}[a,b]\}\le\#\{\text{values of}c\}\le 1+c(b)\)<br>
\(=1+\sum_h\left|v_h(b)-v_h(a)\right|\le 1+\sum_h\big\lceil 2^k\left|h(b)-h(a)\right|\big\rceil.\)

Summing over the intervals gives the bound. □

The count is especially simple for interpolation _H(t_)=_H_(0)+_f(t_)(_H(T_)-_H_(0)) with _f_ nondecreasing from 0 to 1. Each coordinate is \(h(0)+f(t)\Delta h\), with \(\Delta h\) the corresponding coordinate of _H(T_)-_H_(0), so Proposition 4.2 with _N_=1 gives at most

(4.1) \(1+\sum_h\big\lceil 2^k\left|\Delta h\right|\big\rceil\)

pieces at fixed precision _k_, independently of _T_ and _f_.

### 4.1. Comparison with time sampling.

To compare truncation with uniform time steps at equal accuracy, take a \(\sigma\)-sparse, piecewise-monotone, and _L_-Lipschitz family with _L\>_0. As in Lemma 3.8, choose \(0<\varepsilon\le\sqrt{2}\sigma T\), and let _k_ be the least nonnegative integer with \(2^k\ge\sqrt{2}\sigma T/\varepsilon\). The induced product (Lemma 3.4), with _k_-bit generators, and the midpoint product with uniform steps \[28\], with (_k_+1)-bit generators (Lemma 3.8(3)), both approximate _U(T_) within \(\varepsilon\). Proposition 4.2 bounds the induced product’s factor count by the number of intervals plus coordinate changes in units of 2<sup>-_k_</sup>, independently of _L_, whereas uniform steps use \(n\le 1+4LT^2/\varepsilon\) unitaries (Lemma 3.8(3)).

For interpolation at fixed _T_ and target accuracy \(\varepsilon\), (4.1) is independent of _f_, whereas the uniform-step bound depends, through _L_, on the fastest change of _f_. Neither bound dominates, since brief bursts of fast change can favor truncation over uniform steps, while many simultaneously varying coordinates can favor the dimension-independent uniform-step bound.

