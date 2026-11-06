Combining the two lemmas gives the desired result.

**Proof of Theorem 2.** Set \(\Delta=2^{0.75n}\) so that the two time bounds in Lemma 11 and Lemma 13 are balanced to _O_<sup>∗</sup>(2<sup>0.75_n_</sup>). Given an instance of Pigeonhole Equal Sums (with unknown _d_), we run both algorithms in parallel, and return the answer of whichever terminates first. \(\blacktriangleleft\)

## 5 Open problems

Allcock et al. [1] proposed a modular variant of the Pigeonhole Equal Sums problem: given integers _w_<sub>1</sub>_,...,w<sub>n</sub>_ and a modulus \(m\le 2^n-1\), find two distinct subsets \(A,B\subseteq[n]\) such that \(\sum_{i\in A}w_i\equiv\sum_{i\in B}w_i(modm)\). They obtained a _O_<sup>∗</sup>(2<sup>_n/_2</sup>)-time algorithm for this problem. Can this result be improved as well?

Can we obtain faster algorithms for other problems in PPP (e.g., [5, 21])?

## References

