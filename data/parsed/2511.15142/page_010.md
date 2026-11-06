<tbc>\(\langle y\rangle\) denote its bit complexity. For a subset \(\mathcal{P}\subseteq\mathbb{R}^d\), let \(\langle\mathcal{P}\rangle:=\mathrm{max}_{y\in\mathcal{P}}\langle y\rangle\) be the maximum bit complexity of all its points.

The first two conditions are natural: we output a sequence of points such that _y_<sub>1</sub> is the minimizer, and each point has at least as much cost as its predecessor. Condition 3 requires some explanation: this condition is equivalent to the statement that

\(\big(\langle w',y_1\rangle\le\langle w',y_2\rangle\le\cdots\le\langle w',y_k\rangle\big)\Longrightarrow\big(\langle w',y_1\rangle\le\langle w',x\rangle,\forall x\in\mathcal{P}\big)\) (1)

holds for all \(w'\in\mathbb{R}^d\). In other words, the sequence (_y_<sub>1</sub>_,...,y<sub>k</sub>_) serves as a certificate: conditioned on the inclusion \(\mathcal{P}\subseteq y_1+\mathrm{env}(y_1,\dots,y_k)\), the optimality of _y_<sub>1</sub> with respect to a weight vector _w_ is guaranteed if the weights of the points in the sequence are non-decreasing. (Section A.1 gives more context, via Lemma A.1.)

At a high level, the second and third conditions in Algorithm 2 can be viewed as a valid certification of the optimality of _y_<sub>1</sub> (for the input weight _w_) over all points in P, based solely on comparisons within a small set of points {_y_<sub>1</sub>_,...,y<sub>k</sub>_}.

## 3.2 The Ellipsoid Algorithm

Before describing our Dual Ellipsoid approach, we recall the standard ellipsoid subroutine for rational polytopes in Algorithm 3:

For any query point \(x\in\mathbb{Q}^d\), the separation oracle SEP_<sub>P</sub>_ asserts that \(x\in P\) or returns a separating hyperplane (defined by a violated constraint of _P_) that separates _x_ from _P_.

**Theorem 3.1** (\[Sch86, Chapter 14\], \[GLS93, Chapter 3\])**.** _Let_ \(P\subseteq\mathbb{R}^d\) _be a full-dimensional rational polytope with facet complexity_ \(\phi\)_. The Ellipsoid Method returns a point in P or determines_ \(P=\emptyset\) _within the following bounds:_

1. **_Iterations:_** _The algorithm terminates after at most_ \(T_E=O(d^3\phi)\) _calls to the separation oracle. This follows from T<sub>E</sub>=O(d_ln(Vol(_B_<sub>2</sub>(**0**_,R_))/Vol(_P_))) _and the bounds on R,_Vol(_P)._<tbc>

**Algorithm 2:** Conic-Certification Oracle

**2.1 Input:** A vector \(w\in\mathbb{R}^d\).

**2.2 Output:** A sequence \((y_1,\dots,y_k)\in\mathcal{P}^k\) of points in P satisfying:

1. \(y_1\in\mathrm{arg}\mathrm{min}_{y\in\mathcal{P}}\langle w,y\rangle\).<tbc>

2. \(\langle w,y_1\rangle\le\langle w,y_2\rangle\le\cdots\le\langle w,y_k\rangle\).<tbc>

3. \(\mathcal{P}\subseteq y_1+\mathrm{env}(y_1,\dots,y_k)\) and \(k=\mathrm{poly}(d,\langle\mathcal{P}\rangle)\).

**Algorithm 3:** Ellipsoid Method

**3.1 Input:**

1. A strong separation oracle SEP_<sub>P</sub>_ for a bounded polyhedron \(P\subseteq\mathbb{R}^d\).<tbc>

2. A bit complexity upper bound \(\phi\) for the inequalities defining _P_.<br>
_(Note: This implies_ \(P\subseteq B_2(\mathbf{0},R)\) _with_ \(R=2^{O(d\phi)}\)_. Furthermore, if P is full-dimensional, then_ \(\mathrm{Vol}(P)\ge 2^{-O(d^2\phi)}\)_.)_

**Output:** A point \(x\in P\), or correct assertion that _P_ is empty.

