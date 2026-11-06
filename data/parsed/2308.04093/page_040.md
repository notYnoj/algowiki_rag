## A SMAWK algorithm

We review the classic result of Aggarwal, Klawe, Moran, Shor, and Wilber \[AKM<sup>+</sup>87\] on finding row maxima in convex totally monotone matrices (in particular, convex Monge matrices).

We say an \(m\times n\) real matrix _A_ is _convex Monge_ if

\(A[i,j]+A[i',j']\ge A[i,j']+A[i',j]\) (21)

for all \(i<i'\) and \(j<j'\).

More generally, we consider matrices with possibly \(-\infty\) entries. Following the terminology of \[AK90\], a matrix \(A\in(\mathbb{R}\cup\{-\infty\})^{m\times n}\) is called a _reverse falling staircase_ matrix, if the finite entries in each row form a prefix, and the finite entries in each column form a suffix. In other words, if \(A[i,j']>-\infty\), then \(A[i',j]>-\infty\) for all \(i'\in\{i,i+1,\dots,m\}\) and \(j\in\{1,2,\dots,j'\}\). In the definition of convex Monge property, inequality (21) is always considered to hold when its right-hand side evaluates to \(-\infty\).

A reverse falling staircase matrix _A_ is convex Monge implies _A_ is _convex totally monotone_: for all \(i<i'\) and \(j<j'\),

\(A[i,j]<A[i,j']\Rightarrow A[i',j]<A[i',j'].\) (22)

Given an \(m\times n\) convex totally monotone matrix, let _j_<sub>max</sub>(_i_) denote the index of the leftmost column containing the maximum value in row _i_. Note that condition (22) implies

\(1\le j_\mathrm{max}(1)\le j_\mathrm{max}(2)\le\cdots\le j_\mathrm{max}(m)\le n.\) (23)

The SMAWK algorithm \[AKM<sup>+</sup>87\] finds _j_<sub>max</sub>(_i_) for all \(1\le i\le m\). On tall matrices (\(n\checkmark m\)), its time complexity is near-linear in _n_ (instead of _m_), if we allow a compact output representation based on (23). This is formally summarized in the following theorem.

**Theorem A.1** (SMAWK algorithm \[AKM<sup>+</sup>87\])**.** _Let an_ \(m\times n\) _convex Monge reverse falling staircase matrix A be implicitly given, so that each entry of A can be accessed in constant time._

_There is a deterministic algorithm that finds all row maxima of A in_ \(O\left(n(1+\mathrm{log}\left\lceil\frac{m}{n}\right\rceil)\right)\) _time. Its output is compactly represented as n_+1 _integers,_ \(1=r_1\le r_2\le\cdots\le r_n\le r_{n+1}=m+1\)_, indicating that for all_ \(1\le j\le n\) _and_ \(r_j\le i<r_{j+1}\)_, the leftmost maximum element in row i of A is A_\[_i,j_\].

