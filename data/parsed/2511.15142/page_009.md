learning/classification and optimization settings should be interesting more generally. The algorithm is also surprisingly simple:

1.1 while |P| _is more than O(k_) do<br>
   Independently include each point of P in a subset Y with probability 2k/N<br>
   \(\sigma\leftarrow\) result of sorting Y using O(klogk) expected comparisons<br>
  \(y\leftarrow\) first (smallest) element of \(\sigma\)<br>
   Eliminate all points \(x\in\mathcal{P}\backslash\{y\}\) such that \(x-y\in\text{env}(\sigma)\)<br>
   Sort P using a brute-force algorithm.

The proof of the algorithm uses from the next lemma, which shows that each iteration reduces the number of points in P by half in expectation. We defer the proof to Section A.1.2.

**Lemma 2.3** (Sieving Lemma)**.** _The expected number of points that are eliminated from_ P _at step 1.4 is at least_ |P|/2.

Since Boolean point sets have small conic dimension \[KLMZ17\] (see Section A.2 for a proof), we get our main query complexity theorem for Boolean optimization:

**Theorem 1.1** (Boolean Linear Optimization)**.** _For any family_ \(\mathcal{F}\subseteq 2^U\) _and unknown weight function_ \(w^*:U\rightarrow\mathbb{R}\)_, we can solve_ \(argmin_{S\in\mathcal{F}}\sum_{e\in S}w_e^*\) _using_ \(O(nlog^2n\cdot log|\mathcal{F}|)=\widetilde{O}(n^2)\) _comparison queries, where n_=|_U|._

As mentioned in Section 1.1, this result is very surprising to us: it shows that a small number of very structured comparison queries suffice to find the optimal solution, even for NP-hard optimization problems for which the computational complexity is exponential (assuming the ETH).

Can we hope to implement Algorithm 1 efficiently for "nice" Boolean problems? E.g., can we do this for problems which admit an optimization oracle, and also a sampling oracle, so that we can implement step 1.1 efficiently? Matroids are one such class of problems to keep in mind. Note that the above algorithm restricts to some subset of the points in step 1.4; it remains unclear how to efficiently sample from these restrictions. To sidestep this difficulty, we give a different algorithm in the next section, and show that which we can indeed implement for several "nice" problems.

## 3 Optimization from Certification: Dual Ellipsoid Algorithm

In this section, we present an alternative to Algorithm 1 for the General Linear Optimization problem. Crucially, this framework establishes an efficient reduction from optimization to certification. The algorithm iteratively either acquires more information regarding the unknown objective vector _w_<sup>∗</sup>, or certifies that a candidate point \(x\in\mathcal{P}\) is optimal.

This approach leverages the classic ellipsoid method using the concept of _conic certificates_ to determine if the candidate solution \(x_t=argmin_{x\in\mathcal{P}}\langle w_{t-1},x\rangle\) (which is optimal with respect to the current ellipsoid center _w_<sub>_t_-1</sub>) is also optimal with respect to the hidden vector _w_<sup>∗</sup> using only comparisons between feasible sets. The procedure is detailed in Algorithm 4; we build up the necessary machinery for it in the next two sections.

### 3.1 The Conic-Certification Oracle

The Dual Ellipsoid algorithm relies on having access to a specific oracle, which we call the _Conic- Certification Oracle_ (CCO). To describe it, define the following notation: for any point \(y\in\mathbb{R}^d\), let<tbc>

**Algorithm 1:** Iterative Sieving Algorithm

