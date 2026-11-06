• _(YES) There exists_ \(a\in A\) _and_ \(b\in B\) _with_ \(\left\|a-b\right\|_p\le r\).<tbc>

• _(NO) For all_ \(a\in A\) _and_ \(b\in B\), \(\left\|a-b\right\|_p\ge\gamma r\).

A standard technique [WW18] shows that any \(\gamma\)-ANN algorithm with sublinear query time and polynomial preprocessing time implies a subquadratic algorithm for \(\gamma\)-approximate Bichromatic Closest Pair (See Lemma 3.1).

## 2.3 Lattice Problems

A lattice L is defined as the set of all integer combinations of linearly independent basis vectors \(b_1,\dots,b_n\in\mathbb{R}^d\), i.e.,

\(\mathcal{L}=\mathcal{L}(b_1,\dots,b_n)=\left\{\sum_{i=1}^n\alpha_ib_i|\alpha_i\in\mathbb{Z}\right\}.\)

We denote the rank of L by _n_ and the ambient dimension by _d_.

**Definition 2.6** (Shortest Vector Problem)**.** _The_ \(\gamma\)_-approximate Shortest Vector Problem under the_ \(\ell_p\) _norm (_\(\gamma\)-SVP_<sub>p</sub>) is defined as follows. Let_ L _be a d-dimensional lattice of rank n given in the form of a basis_ B=(_b_<sub>1</sub>_,...,b<sub>n</sub>), where_ \(\mathcal{B}\subset\mathbb{R}^d\)_. Given numbers_ \(\gamma>1\) _and r\>_0_, distinguish between the following two cases:_

• _(YES) There exists a non-zero vector_ \(\vec{\alpha}\in\mathbb{Z}^n\) _such that_<tbc>

<tbc>\(\left\|\sum_{i=1}^n\alpha_ib_i\right\|_p\le r.\)<tbc>

• _(NO) For any non-zero_ \(\vec{\alpha}\in\mathbb{Z}^n\),<tbc>

<tbc>\(\left\|\sum_{i=1}^n\alpha_ib_i\right\|_p\ge\gamma r.\)

**Definition 2.7** (Shortest Vector Problem with Binary Restriction)**.** _The_ \(\gamma\)_-approximate Shortest Vector Problem with Binary Restriction under the_ \(\ell_p\) _norm (_\(\gamma\)-SVP_<sub>p</sub>_<sup>{0,1}</sup>_) is defined as follows. Let_ L _be a d-dimensional lattice of rank n given in the form of a basis_ B=(_b_<sub>1</sub>_,...,b<sub>n</sub>), where_ \(\mathcal{B}\subset\mathbb{R}^d\)_. Given numbers_ \(\gamma>1\) _and r\>_0_, distinguish between the following two cases:_

• _(YES) There exists a non-zero vector_ \(\vec{\alpha}\in\{0,1\}^n\) _such that_<tbc>

<tbc>\(\left\|\sum_{i=1}^n\alpha_ib_i\right\|_p\le r.\)<tbc>

• _(NO) For any non-zero_ \(\vec{\alpha}\in\mathbb{Z}^n\),<tbc>

<tbc>\(\left\|\sum_{i=1}^n\alpha_ib_i\right\|_p\ge\gamma r.\)

**Theorem 2.8** (\[BGSD17, Corollary 6.7\])**.** _Assuming SETH, for any_ \(\varepsilon>0\)_, there exists_ \(\gamma=\gamma(\varepsilon)\) _such that_ \(\gamma\)-SVP\(_\infty^{\{0,1\}}\) _cannot be solved in_ \(2^{(1-\varepsilon)n}\) _time, where n is the rank of the given lattice._

**Remark 2.9.** _The precise form of the approximation factor_ \(\gamma\) _in Theorem 2.8 is_ \(\gamma=1+2/(k-1)\)_, where_ \(k=k(\varepsilon)\) _comes from the hard k_-SAT _instance from SETH. Since the dependence_ \(k=k(\varepsilon)\) _is not known, so is the dependence of_ \(\gamma\) _on_ \(\varepsilon\).

