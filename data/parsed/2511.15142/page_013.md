Conversely, if the algorithm returns NO, the ellipsoid algorithm runs for all _T_ steps. At every step _t_, we construct a half-space H_<sub>t</sub>_ derived from the violation _n<sub>t</sub>=y<sub>j</sub>-y_<sub>_j_+1</sub>. Since CCO(_w_<sub>_t_-1</sub>) guarantees \(\langle w_{t-1},y_j\rangle\le\langle w_{t-1},y_{j+1}\rangle\), we have \(\langle w_{t-1},n_t\rangle\le 0\), while the violation implies \(\langle w^*,n_t\rangle>0\). Thus, H_<sub>t</sub>_ effectively separates the center _w_<sub>_t_-1</sub> from _w_<sup>∗</sup>.

By Theorem 3.1, such a sequence of separating cuts can have length at most \(d^3\phi=O(d^3\langle\mathcal{P}\rangle)\) where \(\phi\) is the bit-complexity of the seperating hyperplanes which we know is defined by normals of the form _y<sub>i</sub>-y<sub>j</sub>_ for \(y_i,y_j\in\mathcal{P}\). Therefore, for a sufficiently large \(T=\Theta(d^3\langle\mathcal{P}\rangle)\), the algorithm must terminate with an optimal solution.

## 3.5 Query Complexity and Running Time

Let \(T_D:=O(d^3\langle\mathcal{P}\rangle)\) be the number of iterations given by Theorem 3.7 that guarantees that Algorithm 4 terminates with an optimal solution.

**Lemma 3.8** (Query complexity)**.** _Algorithm 2 can be implemented (inefficiently) to output a sequence of length at most_ ConicDim(P)_. The (inefficient) query complexity of Algorithm 4 is at most_ \(T_D\cdot\text{ConicDim}(\mathcal{P})\).

_Proof._ For an input _w_, consider the sequence \(\sigma=(x_1,\dots,x_N)\) of all points in P in increasing order of \(\langle w,x\rangle\). Let \((y_1=x_1,y_2\dots,y_k)\) be the basic subsequence \(B(\sigma)\). From Lemma A.3, we know that \(\text{cone}(\{x_{i+1}-x_i\}_{1\le i\le N-1})\subseteq\text{env}(B(\sigma))\). Using the fact that _y_<sub>1</sub>=_x_<sub>1</sub>, and \(\mathcal{P}\subseteq x_1+\text{cone}(\{x_{i+1}-x_i\}_{1\le i\le N-1})\), we get \(\mathcal{P}\subseteq y_1+\text{env}(y_1,\dots,y_k)\) for \(k\le\text{ConicDim}(\mathcal{P})\). This sequence satisfies all the conditions required by Algorithm 2.

In step \(t\in[T]\) of Algorithm 4, the only place where the comparison oracle is used is to check Equation (6). The number of comparisons is _k<sub>t</sub>_-1, where _k<sub>t</sub>_ is the size of the sequence output by CCO(_w_<sub>_t_-1</sub>). Hence, the query complexity is at most \(\sum_{t=1}^Tk_t\). Using the above implementation for CCO, we know that each _k<sub>t</sub>_ is at most ConicDim(P), giving an overall upper bound of \(T\cdot\text{ConicDim}(\mathcal{P})\).

**Corollary 3.9.** _When_ \(\mathcal{P}\subseteq\{0,1\}^n\)_, the (inefficient) query complexity of Algorithm 4 is_ \(\widetilde{O}(d^5)\).

_Proof._ Using \(\langle\mathcal{P}\rangle=O(d)\) and \(\text{ConicDim}(\mathcal{P})=\widetilde{O}(d)\) when \(\mathcal{P}\subseteq\{0,1\}^d\) (see Lemma A.6) in Lemma 3.8 yields the result.

**Lemma 3.10** (Time complexity)**.** _Given an implementation of_ CCO _with time complexity T<sub>CCO</sub> for inputs w, Algorithm 4 can be implemented to run in_ \(T_D\cdot(T_{CCO}+d^2\cdot\mathcal{M}(d^3\langle\mathcal{P}\rangle))\) _time. Here,_ M(_L_) _is the cost of arithmetic on L-bit numbers_

_Proof._ Note that step _t_ of Algorithm 4, makes one call to CCO with argument _w<sub>t</sub>_ taking _T<sub>CCO</sub>_ time and at most one Ellipsoid update taking \(d^2\cdot\mathcal{M}(d^3\langle\mathcal{P}\rangle)\) time.

## 3.6 Application: Perfect Matchings in Complete Bipartite Graphs

In this section, we present an efficient algorithm for Boolean Linear Optimization, when P is the set of _perfect_ matchings in complete bipartite graphs. Note that while Section E.2 shows how to optimize over matchings using comparisons, it allows us to compare matchings of all sizes. We now show how to optimize over _perfect_ matchings by only comparing _perfect_ matching--at least for complete bipartite graphs. We achieve this by providing efficient implementations of the Conic- Certification Oracle (CCO). By Lemma 3.10, these implementations suffice to ensure the efficient execution of Algorithm 4.

