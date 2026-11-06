## 1.3 Our Contribution

In this paper, we show that the random-order model substantially improves the performance in online coloring: _k_-colorable graphs can be colored online with a _polylogarithmic_ number of colors for any constant _k_. Formally, we prove the following main theorem.

**Theorem 1.** _In the random-order model, when both n and k are known in advance, there exists a randomized online algorithm that colors any k-colorable n-vertex graph using O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>4</sup>_n_) _colors in expectation._

This result significantly improves upon the previous \(\widetilde{O}(n^{1-\frac{1}{k-1}})\)-color bound [Vis92]. In addition, for all fixed \(k\ge 6\), our random-order result is better than the known lower bound of \(\Omega(log^{k-1}n)\) colors for adversarial arrivals [Vis92]. Therefore, we establish the _asymptotic separation_ between the random-order model and the adversarial-order model.

Moreover, assuming the result of the recent preprint [LL26], which claims that First-Fit uses expected \(\Omega(n^{1/2000})\) colors for some bipartite graphs under random arrivals (and hence, for every \(k\ge 2\), some _k_-colorable graphs), our algorithm asymptotically outperforms First-Fit for all \(k\ge 2\).

Furthermore, we obtain a competitive ratio of \(\widetilde{O}(n^{2/3})\), as stated in the following theorem.

**Theorem 2.** _In the random-order model, when n is known in advance, there exists a randomized online algorithm that attains a competitive ratio of_ \(\widetilde{O}(n^{2/3})\).

Given the known lower bound of \(\Omega(\frac{n}{log^2n})\) on the competitive ratio for adversarial arrivals [HS94], this also establishes the _asymptotic separation_ between the random-order model and the adversarial-order model in terms of the competitive ratio. Note that our result assumes that _n_ is known in advance. This is a standard assumption in the random-order model; several previous studies [AJ21; AKL21; Lin61; SSZ25] also make the same assumption.

## 1.4 Online Algorithms vs. Approximation Algorithms

A broader question in theoretical computer science concerns the relationship between the _competitive ratio_ in online algorithms and the _approximation ratio_ in polynomial-time approximation algorithms. This topic is discussed in various studies [KKL07; MAS14]. In general, if an online algorithm achieves a performance guarantee beyond the hardness barrier for polynomial-time approximation algorithms, then it must run in super-polynomial time.

As a matter of fact, online algorithms can achieve better performance guarantees than approximation algorithms for some problems, although we did not find any references that explicitly mention this observation. The work of Rubinstein (2016) [Rub16] presents an _O_(log_n_)-competitive algorithm for the (maximum cardinality) secretary problem on a downward-closed set system. This immediately yields an _O_(log_n_)-competitive algorithm for "online maximum independent set" with random arrivals. In contrast, approximating (offline) maximum independent set within a factor of \(n^{1-\varepsilon}\) is NP-hard for every fixed \(\varepsilon>0\), as shown by Zuckerman (2006) [Zuc06].

This paper gives an exponential-time \(\widetilde{O}(n^{2/3})\)-competitive algorithm for online coloring with random arrival order (Theorem 2), whereas approximating (offline) graph coloring within a factor of \(n^{1-\varepsilon}\) is NP-hard for every fixed \(\varepsilon>0\) [Zuc06]. Therefore, we establish the _asymptotic separation_ between online and (deterministic or randomized) approximation algorithms in graph coloring,<tbc>

