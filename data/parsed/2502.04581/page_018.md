_variables_ \(\{x_i[j]:i\in\{1,\dots,k\},j\in\{1,\dots,d_i\}\}\) _and the free variables such that_ \(\psi(x_1,\dots,x_k)\) _is equivalent to_ \(\psi'(L_1,\dots,L_s)\).

In the following, we look at the class of problems \(\mathsf{FOP}_\mathbb{Z}^k\) with the restriction of inequality dimension at most 3. We use the following naming convention for boxes.

\(\blacktriangleright\) **Definition 26.** _A d-box in_ R_<sup>d</sup> is the cartesian product of d proper intervals_ \(s_1\times\cdots\times s_d\)_, where s<sub>i</sub> is an open, closed or half-open interval. We call a cartesian product of only closed intervals a closed box and a cartesian product of only open intervals an open box._

Given a set _R_ of _n_ closed boxes (represented as 2_d_ integer coordinates), and _d_-dimensional points \(a\in A,b\in B\), we can express in \(\mathsf{FOP}_\mathbb{Z}(\exists\exists\exists)\) whether _a+b_ lies in one of the boxes as follows:

\(\exists a\in A\exists b\in B\exists r\in R:\wedge_{i=1}^dr[i]\le a[i]+b[i]\wedge a[i]+b[i]\le r[d+i].\)

In fact, we are not limited to closed boxes, if a box is open or half open in a dimension, one can adjust the inequalities in this dimension appropriately.

In order to prove our main theorem in this section, we need to partition the union of _n_ unit cubes in R<sup>3</sup> into pairwise interior- and exterior-disjoint boxes. While Chew et al. [23] studied such a decomposition of unit cubes with the requirement of only interior-disjoint boxes, we need an extension of their result to guarantee disjoint exteriors.

\(\blacktriangleright\) **Lemma 27** (Disjoint decomposition of the union of cubes in R<sup>3</sup>)**.** _Let_ C _be a set of n axis- aligned congruent cubes in_ R<sup>3</sup>_. The union of these cubes, can be decomposed into O(n_) _boxes whose interiors and exteriors are disjoint in time O(n_log<sup>2</sup>_n)._

The proof is deferred to the full version.

\(\blacktriangleright\) **Theorem 28.** _There is an algorithm deciding_ 3_-SUM in randomized time_ \(O(n^{2-\epsilon})\) _for an_ \(\epsilon>0\) _if and only if for each problem P in the classes_ \(\mathsf{FOP}_\mathbb{Z}(\forall\forall\exists)\) _and_ \(\mathsf{FOP}_\mathbb{Z}(\exists\forall\exists)\) _of inequality dimension at most_ 3 _there exists some_ \(\epsilon'>0\) _such that we can solve P in randomized time_ \(O(n^{2-\epsilon^\prime})\).

**Proof.** For the first direction due to Theorem 10, we can reduce 3-SUM to an instance of Additive Sumset Approximation,

\(\forall a\in A\forall b\in B\exists c\in C:c\le a+b\wedge a+b\le c+t,\)

which has inequality dimension 2. Let us continue with the other direction. Let \(\phi:=Q_1a\in A\forall b\in B\exists c\in C:\varphi\), where \(Q_1\in\{\exists,\forall\}\) and \(\varphi\) is a quantifier free linear arithmetic formula with inequality dimension 3. Let \(L_1:=\alpha_1^Ta+\beta_1^Tb\le\gamma_1^Tc+S_1,L_2:=\alpha_2^Ta+\beta_2^Tb\le\gamma_2^Tc+S_2\) and \(L_3:=\alpha_3^Ta+\beta_3^Tb\le\gamma_3^Tc+S_3\) after replacing the free variables. Assume that the formula \(\varphi\) is given in DNF, thus each co-clause has at most 3 atoms, chosen from _L_<sub>1</sub>_,L_<sub>2</sub>_,L_<sub>3</sub> and their negations. Let

\(A':=\left\{\left(\begin{array}{ c } \alpha_1^Ta \\ \alpha_2^Ta \\ \alpha_3^Ta \end{array}\right):a\in A\right\},B':=\left\{\left(\begin{array}{ c } \beta_1^Tb \\ \beta_2^Tb \\ \beta_3^Tb \end{array}\right):b\in B\right\},C':=\left\{\left(\begin{array}{ c } \gamma_1^Tc+S_1 \\ \gamma_2^Tc+S_2 \\ \gamma_3^Tc+S_3 \end{array}\right):c\in C\right\}\)

Thus each co-clause consists of conjunctions of a subset of the following set

\(\{a'[0]+b'[0]\le c'[0],a'[0]+b'[0]\ge c'[0]+1,a'[1]+b'[1]\le c'[1],a'[1]+b'[1]\ge c'[1]+1,a'[2]+b'[2]\le c'[2],a'[2]+b'[2]\ge c'[2]+1\}.\)

