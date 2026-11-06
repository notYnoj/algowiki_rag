## 6 Completeness Theorems for _k_-SUM and Geometric Friends

### Hausdorff Distance under _n_ Translations

Among the most common translation-invariant distance measures for given point sets _B_ and _C_ is the Hausdorff Distance under Translation \[24, 18, 19, 23, 45, 38\]. To define it, we denote the directed Hausdorff distance under the \(L_\infty\) metric by \(\delta_\overrightarrow{H}(B,C):=max_{b\in B}min_{c\in C}\|b-c\|_\infty\).<sup>9</sup> The Hausdorff distance under translation \(\delta_\overrightarrow{H}^T(B,C)\) is defined as the minimum Hausdorff distance of _B_ and an arbitrary translation of _C_, i.e.,

\(\delta_\overrightarrow{H}^T(B,C):=min_{\tau\in\mathbb{R}^d}\delta_\overrightarrow{H}(B,C+\{\tau\})=min_{\tau\in\mathbb{R}^d}max_{b\in B}min_{c\in C}\|b-(c+\tau)\|_\infty.\)

For _d_=2, Bringmann et al. \[18\] were able to show a (|_B_||_C_|)<sup>1-_o_(1)</sup> time lower bound based on the orthogonal vector hypothesis, and there exists a matching \(\tilde{O}(|B||C|)\) upper bound by Chew et al. \[25\].

We shall establish that restricting the translation vector to be among a set of _m_ candidate vectors yields a central problem in FOP<sub>Z</sub>. Specifically, we define the Hausdorff distance under Translation in _A_, denoted as \(\delta_\overrightarrow{H}^{T(A)}(B,C)\), by

\(\delta_\overrightarrow{H}^{T(A)}(B,C):=min_{\tau\in A}\delta_\overrightarrow{H}(B,C+\{\tau\})=min_{\tau\in A}max_{b\in B}min_{c\in C}\|b-(c+\tau)\|_\infty.\)

Correspondingly, we define the problem _Hausdorff distance under m Translations_ as: Given \(A,B,C\subseteq\mathbb{Z}^d\) with \(|A|\le m\), \(|B|,|C|\le n\) and a distance value \(\gamma\in\mathbb{N}\), determine whether \(\delta_\overrightarrow{H}^{T(A)}(B,C)\le\gamma\). Note that this can be rewritten as a \(\mathsf{FOP}_\mathbb{Z}(\exists\forall\exists)\)-formula, see the full version of the paper for details.

The Hausdorff distance under _m_ Translations occurs naturally when approximating the Hausdorff distance under translation: Specifically, common algorithms compute a set _A_ of \(|A|=f(\epsilon)\) translations such that \(\delta_\overrightarrow{H}^{T(A)}(B,C)\le(1+\epsilon)\delta_\overrightarrow{H}^T(B,C)\). Generally, this prob lem is then solved by performing |_A_| computations of the Hausdorff distance, which yields \(\tilde{O}(|A|n)=\tilde{O}(f(\epsilon)n)\)-time algorithms \[48\]. Improving over the \(\tilde{O}(mn)\)-time baseline for Hausdorff Distance under _m_ Translations would thus lead to immediate improvements for approximating the Hausdorff Distance under Translation. Our results will establish additional consequences of fast algorithms for this problem: an \(O(n^{2-\epsilon_d})\)-time algorithm with \(\epsilon_d>0\) for Hausdorff distance under _n_ Translations would give an algorithmic improvement for the classes of \(\mathsf{FOP}_\mathbb{Z}(\exists\forall\exists)\)- and \(\mathsf{FOP}_\mathbb{Z}(\forall\exists\forall)\)-formulas.

### Verification of Pareto Sums

Our second geometric problem is a verification version of computing _Pareto sums_: Given point sets \(A,B\subseteq\mathbb{Z}^d\), the Pareto sum _C_ of _A,B_ is defined as the Pareto front of their sumset \(A+B=\{a+b|a\in A,b\in B\}\). Put differently, the Pareto sum of _A,B_ is a set of points _C_ satisfying (1) \(C\subseteq A+B\), (2) for every \(a\in A\) and \(b\in B\), the vector _a+b_ is dominated<sup>10</sup> by some \(c\in C\) and (3) there are no distinct \(c,c'\in C\) such that \(c'\) dominates _c_. The task of computing Pareto sums appears in various multicriteria optimization settings \[8, 47, 30, 44\]; fast output-sensitive algorithms (both in theory and in practice) have recently been investigated by Hespe, Sanders, Storandt, and Truschel \[37\].

<sup>9</sup> Since we will exclusively consider the _directed_ Hausdorff distance under Translation, we will drop "directed" throughout the paper. <sup>10</sup>We consider the usual domination notion: A vector \(u\in\mathbb{Z}^d\) is dominated by some vector \(v\in\mathbb{Z}^d\) (written \(u\le v\)) if and only if in all dimensions \(i\in[d]\) it holds that \(u[i]\le v[i]\).

