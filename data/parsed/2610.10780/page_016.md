## 5.1 Algorithm description

We describe a general _i_-th phase. Before the phase starts, we are given an interval _I_ satisfying \(|S\cap I|=O(n^{4/3}(log^{(i-1)}n)^4)\) and containing \(\delta^*\). The goal of the phase is to produce a subinterval \(I'\subseteq I\) such that \(|S\cap I'|=O(n^{4/3}(log^{(i)}n)^4)\) and \(\delta^*\in I'\).

The phase proceeds in iterations. At the beginning of the _j_-th iteration, we are given an interval _I_<sub>_j_-1</sub> containing \(\delta^*\). Initially, _I_<sub>0</sub>=_I_. Each iteration either:

1. produces a smaller interval \(I_j\subseteq I_{j-1}\) satisfying \(\delta^*\in I_j\) and \(|S\cap I_j|\le\rho|S\cap I_{j-1}|\) for some constant \(\rho<1\); or<tbc>

2. certifies that \(|S\cap I_{j-1}|=O(n^{4/3}(log^{(i)}n)^4)\), in which case the phase terminates and returns _I_<sub>_j_-1</sub> as \(I'\).

Since the phase starts with \(|S\cap I|=O(n^{4/3}(log^{(i-1)}n)^4)\), the first outcome can occur only _O_(log<sup>(_i_)</sup>_n_) times. Hence, the phase terminates after _O_(log<sup>(_i_)</sup>_n_) iterations.

In the following, we describe a general _j_-th iteration. For simplicity, we assume \(i\ge 3\). The cases _i_=1,2 are identical except for the running-time bounds. We will show that each iteration requires _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>) time.

We begin by applying Theorem 3 to the interval _I_<sub>_j_-1</sub> with parameter _i_. This produces a collection of bicliques \(\Gamma=\{A_t\times B_t\}\) in _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>) time. Let \(N(\Gamma)=\sum_{A_t\times B_t\in\Gamma}|A_t||B_t|\), i.e., the number of distances recorded in \(\Gamma\). Since \(\sum_t(|A_t|+|B_t|)=O(n^{4/3}/(log^{(i)}n)^2)\) by Theorem 3, the value \(N(\Gamma)\) can be computed within the same asymptotic running time.

In the remainder of the section, let _c_<sub>1</sub> denote the constant from Theorem 3.

**Lemma 6.** _If_ \(N(\Gamma)\le c_1n^{4/3}(log^{(i)}n)^4\)_, then_ \(|S\cap I_{j-1}|=O(n^{4/3}(log^{(i)}n)^4)\).

_Proof._ If \(|S\cap I_{j-1}|<c_1n^{4/3}(log^{(i)}n)^4\), the conclusion is immediate. Otherwise, Theorem 3 implies that \(N(\Gamma)\ge 0.4|S\cap I_{j-1}|\). Therefore,

\(|S\cap I_{j-1}|\le\frac{1}{0.4}N(\Gamma)\le\frac{c_1}{0.4}n^{4/3}(log^{(i)}n)^4,\)

which proves the lemma.

If \(N(\Gamma)\le c_1n^{4/3}(log^{(i)}n)^4\), Lemma 6 allows us to terminate the current phase and return _I_<sub>_j_-1</sub> as \(I'\).

Assume henceforth that \(N(\Gamma)>c_1n^{4/3}(log^{(i)}n)^4\). Since \(|S\cap I_{j-1}|\ge N(\Gamma)\), we have \(|S\cap I_{j-1}|>c_1n^{4/3}(log^{(i)}n)^4\). Consequently, by Theorem 3, \(N(\Gamma)\ge 0.4|S\cap I_{j-1}|\).

We next construct expander graphs for the bicliques of \(\Gamma\) and use them to compute a set _E_ of weighted distances. This step is essentially the same as in \[28\], which in turn follows the method in \[20\]. For completeness, we briefly sketch the construction and refer the reader to \[28, Section 3\] or \[20\] for details.

### Computing a weighted distance set _E_.

For convenience, assume that \(|A_t|\ge|B_t|\) for every biclique \(A_t\times B_t\in\Gamma\) (otherwise we could switch the names of _A<sub>t</sub>_ and _B<sub>t</sub>_). Let _m<sub>t</sub>_=|_A<sub>t</sub>_| and _n<sub>t</sub>_=|_B<sub>t</sub>_|.

Partition each _A<sub>t</sub>_ into \(g=\lfloor m_t/n_t\rfloor\) subsets _A_<sub>_t_1</sub>_,A_<sub>_t_2</sub>_,...,A<sub>tg</sub>_, each containing between _n<sub>t</sub>_ and 2_n<sub>t</sub>_ points. Each pair (_A<sub>tf</sub>,B<sub>t</sub>_), \(1\le f\le g\), defines a biclique \(A_{tf}\times B_t\). For every such biclique, we construct a _d_-regular LPS-expander graph _G<sub>tf</sub>_ on \(A_{tf}\cup B_t\) \[20, 21\], where _d_ is a sufficiently large constant to be fixed later. The graph _G<sub>tf</sub>_ has _O_(|_A<sub>tf</sub>_|+|_B<sub>t</sub>_|) edges and can be constructed within the same time bound \[20, 21\]. Let _G<sub>t</sub>_ be the union of all graphs _G<sub>tf</sub>_. Computing all graphs _G<sub>t</sub>_ takes \(O(\sum_t(|A_t|+|B_t|))=O(n^{4/3}/(log^{(i)}n)^2)\) time. The total number of edges in all graphs is bounded by the same bound.

