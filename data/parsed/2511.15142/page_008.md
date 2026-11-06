## 2 Linear Optimization for General Set Systems

We begin our investigation with the question of query complexity for linear optimization in a very general setting: in the _general linear optimization_ (GLO) problem, we are given a set of _N_ points \(\mathcal{P}=\{x_1,\dots,x_N\}\subseteq\mathbb{R}^d\), and an unknown weight vector \(w^*\in\mathbb{R}^d\). We are only allowed comparison queries: given \(x,y\in\mathcal{P}\), the comparison oracle responds with \(\mathrm{sign}\left(\langle w^*,x-y\rangle\right)\), i.e., the relative ordering of _x_ and _y_ in the ordering on P induced by _w_<sup>∗</sup>. The goal is to identify \(x^*:=\mathrm{arg}\mathrm{min}_{x\in\mathcal{P}}\langle w^*,x\rangle\) using as few queries as possible. The combinatorial optimization setting is obtained when we restrict to some point set in {0,1}_<sup>d</sup>_.

Our main result for general linear optimization depends on the complexity of these point sets, via the notion of the _conic dimension_, which we define next.

### 2.1 Envelopes and the conic dimension of Point Sets

We begin by defining the _envelope_ and _conic dimension_ of a point set. Recall that a cone of a point set is the collection of all positive linear combinations of these points. The idea behind the envelope is simple: if \(\sigma\) is the total order induced by _w_<sup>∗</sup> on the points {_y_<sub>1</sub>_,...,y<sub>n</sub>_} (i.e., if \(\langle w^*,y_i-y_j\rangle\ge 0\) for _i\<j_, then taking the envelope of \(\sigma\) gives us all the "implications" of this ordering, and allows us to derive implications without performing any further calculations.

**Definition 2.1.** For a sequence of points \(\sigma=(y_1,\dots,y_k)\in(\mathbb{R}^d)^k\):

1. The _envelope_ of \(\sigma\) is<tbc>

<tbc>\(\mathrm{env}(\sigma):=\mathrm{cone}(\{y_j-y_i\}_{1\le i<j\le k})=\mathrm{cone}(\{y_{i+1}-y_i\}_{1\le i<k}).\)<tbc>

2. The points are _conically independent_ if, for each \(t\in\{2,\dots,k\}\),<tbc>

<tbc>\(y_t-y_1\notin\mathrm{env}(\sigma^{1:t-1}),\)<tbc>

<tbc>where \(\sigma^{1:t}\) denotes the prefix consisting of the first _t_ elements of \(\sigma\).

**Definition 2.2.** The _conic dimension_ of a set \(\mathcal{Y}\subseteq\mathbb{R}^d\), denoted ConicDim(Y), is the largest integer _k_ for which there exists a length-_k_ conically independent sequence \(\sigma=(y_1,\dots,y_k)\in\mathcal{Y}^k\).

In other words, the conic dimension is the largest number of comparisons \(\langle w^*,y_t\rangle\) vs. \(\langle w^*,y_1\rangle\) such that each one cannot be inferred from the complete sorted ordering of the preceding points.

### 2.2 An Algorithm for Finding a Minimizer

Given these definitions, it is possible to show that if a point set P has conic dimension _k_, then for the optimal point \(y^*\in\mathcal{P}\) there exists proofs/certificates of optimality of size at most _k_-1 (see Section A.1). Since we are interested in the query complexity and not the certificate complexity of optimization, we show the following:

**Theorem 1.2** (General Linear Optimization)**.** _There is an algorithm that, for any point set_ \(\mathcal{P}\subseteq\mathbb{R}^d\) _with conic dimension k and unknown weights_ \(w^*\in\mathbb{R}^d\)_, returns the minimizer_ \(x^*=\mathrm{arg}\mathrm{min}_{x\in\mathcal{P}}\langle w^*,x\rangle\) _using at most O(k_log_k_log|P|) _comparisons._

The proof of this remarkable result relies on adapting the powerful active classification framework of \[KLMZ17\] to the optimization setting; we believe that this connection between the active<tbc>

