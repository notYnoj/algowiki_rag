## 1 Introduction

Subset-Sum is a fundamental NP-hard problem, which can be formulated as follows.

**Problem 1.1** (Subset-Sum)**.** Given a multiset _S_ of _n_ integers and a target integer _t_, output a subset \(A\subseteq S\) such that \(t=\sum_{a\in A}a\), if such a subset exists.

Subset-Sum admits a simple meet-in-the-middle algorithm, due to Horowitz and Sahni \[19\], that runs in _O_<sup>∗</sup>(2<sup>_n/_2</sup>) time <sup>1</sup>. This remains the standard running-time bound for exact algorithms for Subset-Sum, and the fastest known algorithm \[13\] improves over the _O_(2<sup>_n/_2</sup>) bound only by a polynomial factor. Whether there exists an algorithm for Subset-Sum that runs in \(O^*(2^{(0.5-\delta)n})\) time for some constant \(\delta>0\) remains a long-standing open question.

Closely related to this open problem, Howgrave-Graham and Joux \[20\] broke this meet-in-the- middle barrier in the _average-case_ setting by giving an _O_<sup>∗</sup>(2<sup>0.337_n_</sup>)-time algorithm, which was later improved to _O_<sup>∗</sup>(2<sup>0.283_n_</sup>) by \[8, 9\]. The algorithm of Howgrave-Graham and Joux introduced the representation technique, which was later also used for Equal-Subset-Sum (ESS), an important variant of Subset-Sum that can be formulated as follows.

**Problem 1.2** (Equal-Subset-Sum (ESS) \[31\])**.** Given a set _S_ of _n_ integers, output two distinct subsets \(A,B\subseteq S\) such that \(\sum_{a\in A}a=\sum_{b\in B}b\), if such subsets exist.

ESS admits a simple meet-in-the-middle algorithm that runs in _O_<sup>∗</sup>(3<sup>_n/_2</sup>) time. Surprisingly, the authors of \[25\] broke this meet-in-the-middle barrier for ESS in the _worst-case_ setting by exploiting the representation technique, giving an algorithm that runs in _O_<sup>∗</sup>(1.7088_<sup>n</sup>_) time and space. In the _average-case_ setting, the authors of \[12\] gave an \(O^*(3^{0.387n})\le O^*(1.5299^n)\)-time algorithm for ESS. The open question of whether the running time for ESS in the worst-case setting can be improved beyond _O_<sup>∗</sup>(1.7088_<sup>n</sup>_) \[21, Section 5, Question 1\] was answered affirmatively very recently by Randolph and Węgrzycki \[28\], who gave an algorithm that runs in _O_<sup>∗</sup>(1.7067_<sup>n</sup>_) time and space.

### 1.1 Our Results

In this work, we focus on exact algorithms for ESS in the worst-case setting. All our algorithms are Monte Carlo algorithms that never return false positives, and their error probabilities can be reduced to \(2^{-\Omega(n)}\) by repetition. Our first result establishes a new state-of-the-art algorithm for ESS by further improving the result of \[28\]. While the running-time improvement is our primary contribution, the algorithm also reduces the space usage by a much larger exponential factor.

**Theorem 1.3.** _There exists a Monte Carlo algorithm for ESS that runs in O_<sup>∗</sup>(1.6994_<sup>n</sup>_) _time and uses O_<sup>∗</sup>(1.5664_<sup>n</sup>_) _space._

Our second result improves the polynomial-space running time for ESS. We improve upon the _O_<sup>∗</sup>(2.6817_<sup>n</sup>_)-time algorithm of \[25\] by analyzing two approaches suited to different parameter regimes: one based on recent improvements for low-space Element Distinctness \[11\], and the other using the fast polynomial-space Subset-Sum algorithm of \[5\] as a subroutine.

**Theorem 1.4.** _There exists a Monte Carlo algorithm for ESS that runs in O_<sup>∗</sup>(2.5430_<sup>n</sup>_) _time and uses polynomial space._

For Subset-Sum, Schroeppel and Shamir \[29\] gave a time-space tradeoff _T=O_<sup>∗</sup>(2_<sup>n</sup>/S_<sup>2</sup>) for any space bound \(S\le O^*(2^{n/4})\). This tradeoff was later improved for almost all choices of the tradeoff parameter by \[3\]. In contrast, for ESS, the analogous Schroeppel–Shamir-type tradeoff,<tbc>

<sup>1</sup>The \(O^*(\cdot)\) notation suppresses poly(_n_) factors.

