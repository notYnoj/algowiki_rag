<tbc>_Applications of DPSS._ In Appendix A, we provide two detailed case studies on applications of DPSS in<br>
Influence Maximization \[15, 16\] and Local Clustering \[29\]. These two applications further illustrate<br>
that current algorithms (such as DSS algorithms) cannot address these cases since the sampling<br>
probabilities of items may change simultaneously after just one update.

**Main Result 1: An Optimal DPSS Algorithm.** Our first contribution is an optimal algorithm for<br>
solving the DPSS problem in the Word RAM model. The main result is summarized as follows:

Theorem 1.1. _Consider a set S of n items; there exists a data structure for solving the Dynamic Parameterized Subset Sampling (DPSS) problem, which achieves:_

\(\bullet\) _Pre-processing time: O(n_) _worst-case time to construct the data structure on S;_<tbc>

\(\bullet\) _Query time:_ \(O(1+\mu_S(\alpha,\beta))\) _expected time to return a sample for each Parameterized Subset Sampling (PSS) query on S with parameters_ \((\alpha,\beta)\)_, where_ \(\mu_S(\alpha,\beta)\) _is the expected size of the sample;_<tbc>

\(\bullet\) _Update time: O_(1) _worst-case time for each item insertion or deletion._

_At all times, the worst-case space consumption of such a data structure is bounded by O(n), where n denotes the current cardinality of S._

_An Overview of Our Algorithm._ Given a pair of Parameterized Subset Sampling (PSS) query parameters, \((\alpha,\beta)\), the crucial idea of our algorithm is to convert the PSS query on _S_ into a _O_(1) number of PSS query instances (with possibly different query parameters on possibly different item sets), of which the PSS results can be converted back into a feasible PSS result on _S_ by _rejection sampling_. And each of these _O_(1) query instances can be solved optimally in \(O(1+\mu)\) expected time, where \(\mu\) is its expected sample size. To achieve such a conversion, and to solve those converted PSS query instances optimally, we propose a novel data structure, called _Hierarchy + Adapter + Lookup  _ (HALT). As its name suggests, it consists of three main components: (i) a three-level sampling hierarchy, (ii) a set of dynamic adapters, and (iii) a static lookup table.

Specifically, the sampling hierarchy converts the PSS query on _S_ into _O_(1) PSS query instances on other item sets, while the lookup table can answer PSS queries on a special family of item sets. Last, but not least, as the lookup table is static, while the PSS queries are parameterized on the fly, our dynamic adapters play a crucial role to bridge the hierarchy and the lookup table. Specifically, the adapters, dynamically translate the PSS query instances, during query time, into a form for which our lookup table is applicable.

**Main Result 2: A Hardness Result on DPSS with Float Item Weights.** While our HALT algorithm is optimal for DPSS with integer item weights, interestingly, if the item weights are floating-point numbers, each represented by a _O_(1)-word exponent and a _O_(1)-word mantissa, the DPSS problem suddenly becomes a lot more difficult. In fact, this difficulty arises even in the _deletion-only_ setting where the updates are deletions only. We demonstrate this by showing that DPSS can be used to obtain an algorithm for Integer Sorting:

Theorem 1.2. _Suppose there exists an algorithm for deletion-only DPSS on a set of N items with float weights that has pre-processing time t<sub>p</sub>(N), expected query time_ \((1+\mu)\cdot t_q(N)\)_, and deletion time t<sub>del</sub>(N). Then the Integer Sorting problem for N integers can be solved in_ \(t_p(N)+O(N\cdot(t_q(N)+t_{del}(N)))\) _expected time on the d-bit Word RAM model with_ \(d\in\Omega(logN)\).

In particular, this implies that if there is an optimal algorithm for deletion-only DPSS--i.e., one with \(t_p(N)\in O(N)\), and \(t_q(N),t_{del}(N)\in O(1)\)--then sorting _N_ integers (each represented with _O_(1) words) can be achieved in _O(N_) expected running time on the _d_-bit Word RAM model with \(d\in\Omega(logN)\). However, solving the Integer Sorting problem in _O(N_) expected time for every word-length \(d\in\Omega(logN)\) remains an open problem \[3\]. Moreover, an algorithm for deletion-only DPSS (with float item weights) with \(t_p(N)\in o(N\cdot\sqrt{loglogN})\), and \(t_q(N),t_{del}(N)\in o(\sqrt{loglogN})\)<tbc>

