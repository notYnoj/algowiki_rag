By using the union bound, we have that all the required conditions for iteration _i_ to be good occur with probability at least 1-_O(n_<sup>-2</sup>)-_O(n_<sup>-3</sup>)-_O(n_<sup>-1.5</sup>)=1-_O(n_<sup>-1.5</sup>).

Since there are _k=O_(log_n_) iterations, yet another application of the union bound, implies that all iterations are good with a probability of at least \(1-O\left(\frac{logn}{n\sqrt{n}}\right)\). The claim follows from the fact that the _k_-th iteration is good with the above probability. □

To conclude, Lemma 3.1 and Lemma 3.4 directly lead to the main result of this section.

Theorem 3.5. _Consider a set of n elements subject to random persistent comparison faults with probability at least q and most p, for some constants p, q with_ \(0\le q\le p<\frac{9q+1}{8q+11}\)_. Let S be a sequence of these elements (possibly chosen as a function of the errors)._ RiffleSort _is a randomized algorithm that approximately sorts S in O(n_log_n_) _worst-case time. The maximum dislocation and the total dislocation of the returned sequence are at most O_(log_n_) _and at most O(n), respectively, with probability at least_ \(1-O\left(\frac{logn}{n\sqrt{n}}\right)\).

## 4 Noisy Binary Search

In this section we tackle the problem of efficiently compute an approximate rank of an "external" element with respect to an approximately sorted sequence in presence of persistent random comparison faults. More precisely, given a sequence \(S=\langle s_1,\dots,s_m\rangle\) of _m_ elements, an integer _d_ that satisfies \(d\ge max\{disl(S),lnm\}\), and an element \(x\notin S\), we want to compute, in time _O_(log_m_), a value \(\tau_x\) such that \(|\tau_x-rank(x,S\cup\{x\})|=O(d)\) with high probability.

Recall from Section 2 that only comparisons between _x_ and the elements in _S_ are allowed, that errors happen independently with probability at most _p_, and that the order of the elements in _S_ does not depend on the comparison errors.

### 4.1 High-level ideas

As mentioned in the introduction, the seminal paper of Feige et al. [15] presented a noisy binary search tree for _non-persistent_ random comparison faults that allows to compute \(rank(x,S\cup\{x\})\) w.h.p. in time _O_(log_n_). However, this approach does not readily generalize to our model due to two main difficulties:

\(\bullet\) Feige et al.’s algorithm heavily relies on the fact that comparing the same pair of elements multiple times yields independent outcomes.<tbc>

\(\bullet\) The input sequence _S_ of [15] is perfectly sorted while, in our case, _S_ is only _approximately sorted_. This is motivated by the fact that, when comparison faults are persistent, it is impossible to compute a correctly sorted sequence, as we discuss in Section 6.

To circumvent the first difficulty, we ensure that _x_ is never compared twice with any element _y_ in _S_. Rather, any further comparison between _x_ and _y_ is replaced by a comparison (or multiple comparisons) between _x_ and some nearby proxy element(s) for _y_.

To tackle the second difficulty, we use the upper bound _d_ on the maximum dislocation which implies that an element in a generic position _i_ is larger than any element in a position preceding _i-d_ and smaller than any element in a position following _i+d_. Then, if we group the elements into blocks of size at least _d_, all elements in _i_-th group will be guaranteed to be larger (resp. smaller) than all the elements in the (_i_-2)-th (resp. (_i_+2)-th) group. We can then perform two parallel noisy binary searches: one involving only even-numbered groups and one involving one odd-numbered groups.

The next subsection describes the details of our construction.

