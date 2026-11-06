# A Clique-Based Separator for Intersection Graphs of Geodesic Disks in R<sup>2</sup>

**Boris Aronov**<br> Department of Computer Science and Engineering, Tandon School of Engineering, New York<br> University, Brooklyn, NY 11201 USA

**Mark de Berg**<br> Department of Mathematics and Computer Science, TU Eindhoven, the Netherlands

**Leonidas Theocharous**<br> Department of Mathematics and Computer Science, TU Eindhoven, the Netherlands

**Abstract**

Let _d_ be a (well-behaved) shortest-path metric defined on a path-connected subset of R<sup>2</sup> and let D={_D_<sub>1</sub>_,...,D<sub>n</sub>_} be a set of geodesic disks with respect to the metric _d_. We prove that \(\mathcal{G}^\times(\mathcal{D})\), the intersection graph of the disks in D, has a clique-based separator consisting of \(O(n^{3/4+\varepsilon})\) cliques. This significantly extends the class of objects whose intersection graphs have small clique-based separators.

Our clique-based separator yields an algorithm for _q_-Coloring, which runs in time \(2^{O(n^{3/4+\varepsilon})}\), assuming the boundaries of the disks _D<sub>i</sub>_ can be computed in polynomial time. We also use our clique-based separator to obtain a simple, efficient, and almost exact distance oracle for intersection graphs of geodesic disks. Our distance oracle uses \(O(n^{7/4+\varepsilon})\) storage and can report the hop distance between any two nodes in \(\mathcal{G}^\times(\mathcal{D})\) in \(O(n^{3/4+\varepsilon})\) time, up to an additive error of one. So far, distance oracles with an additive error of one that use subquadratic storage and sublinear query time were not known for such general graph classes.

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Design and analysis of algorithms

**Keywords and phrases** Computational geometry, intersection graphs, separator theorems

**Related Version** A preliminary version of this work will appear in _SoCG’24_[4]

**Funding** _Boris Aronov_: Work has been supported by NSF grant CCF 20-08551.

_Mark de Berg_: MdB is supported by the Dutch Research Council (NWO) through Gravitation-grant NETWORKS-024.002.003.

_Leonidas Theocharous_: LT is supported by the Dutch Research Council (NWO) through Gravitation- grant NETWORKS-024.002.003.

## 1 Introduction

**(Clique-based) separators.** The Planar Separator Theorem states that any planar graph with _n_ nodes has a _balanced separator_ of size \(O(\sqrt{n})\). In other words, for any planar graph G=(_V,E_) there exists a subset \(S\subset V\) of size \(O(\sqrt{n})\) with the following property:<sup>1</sup> _V_\\_S_ can be split into subsets _A_ and _B_ with \(|A|\le 2n/3\) and \(|B|\le 2n/3\) such that there are no edges between _A_ and _B_. This fundamental result was first proved in 1979 by Lipton and Tarjan [20] and has been simplified and refined in several ways, see, e.g., [12, 13]. The Planar Separator Theorem proved to be extremely useful for obtaining efficient divide-and-conquer algorithms for a large variety of problems on planar graphs.

<sup>1</sup> Hereafter we will simply refer to such a subset as a _separator_, omitting the word "balanced" for brevity. Moreover, we do not require the balance factor to be 2/3, but we allow the size of the subsets _A_ and _B_ to be at most \(\delta n\), for some fixed constant \(\delta<1\).







