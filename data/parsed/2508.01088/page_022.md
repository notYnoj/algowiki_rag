1. \(\sigma(\mathcal{T}(n))=\{2n-2,(n-3)^{[3]},\dots,\frac{n-3}{2}^{[3]},\frac{n-7}{2}^{[2]},\frac{n-9}{2}^{[3]},\dots,-2^{[3]},-3^{[T(n-3)]}\}\), _when n is odd;_<tbc>

_2._ \(\sigma(\mathcal{T}(n))=\{2n-2,(n-3)^{[3]},\dots,\frac{n-2}{2}^{[3]},\frac{n-4}{2}^{[2]},\frac{n-8}{2}^{[3]},\dots,-2^{[3]},-3^{[T(n-3)]}\}\), _when n is even._

_Proof._ For \(n\in\{1,2,3\}\), it is immediate that T(_n_) is integral.<br>
For \(n\ge 4\), from Theorems 3.6 and 3.7 it follows that 2_n_-2 and -3 are the largest and the least eigenvalues of T(_n_) with multiplicity 1 and _T(n_-3), respectively. Furthermore, from the results obtained in Subsections 3.2 and 3.3, we may conclude that \(n-3,\dots,\lceil\frac{n-4}{2}\rceil,\lfloor\frac{n-7}{2}\rfloor,\dots,-2\) are also eigenvalues of T(_n_) whose lower bounds for their multiplicities were established as follows:

1. there is an eigenvalue with multiplicity _T(n_-3) (which is -3);<tbc>

2. there is a simple eigenvalue (which is 2_n_-2);<tbc>

3. there is an eigenvalue with multiplicity 2 (which is \(\frac{n-7}{2}\) and \(\frac{n-4}{2}\) , when _n_ is odd and even, respectively);<tbc>

4. there are _n_-2 distinct eigenvalues with multiplicity 3 (which are the remaining eigenvalues).

Therefore, taking into account the above lower bounds, there are _T(n_-3)+1+2+3(_n_-2)=_T(n_) known linearly independent eigenvectors of T(_n_), corresponding to the _T(n_) eigenvalues which, consequently, are totally determined.

## 4 Application to the _n_-Queens’ graph

In \[4\] the authors proved that for \(n\ge 4\), -4 is the least eigenvalue of the _n_- Queens’ graph, Q(_n_), and its multiplicity is (_n_-3)<sup>2</sup>. In \[5\], other integer eigenvalues of Q(_n_) were studied and the following was proved.

1. _n_-4 is an eigenvalue of Q(3) with multiplicity \(\frac{3+1}{2}=2\).<tbc>

2. For \(n\ge 4\):<tbc>

(a) when _n_ is even, \(n-4\in\sigma(\mathcal{Q}(n))\), and it has multiplicity at least \(\frac{n-2}{2}\) ;<tbc>

(b) when _n_ is odd, \(n-4,n-5,n-6,\dots,\frac{n-5}{2},\frac{n-11}{2},\dots,-2,-3\in\sigma(\mathcal{Q}(n))\), and _n_-4 has multiplicity at least \(\frac{n+1}{2}\) .<tbc>

3. Additionally, in \[5\], based in numerical computations for several values of _n_, the following conjecture was proposed.

**Conjecture 4.1.** \[5\] _For_ \(n\ge 4\)_, the integers which appear above are the unique integer eigenvalues of_ Q(_n). Furthermore, when n is even the eigenvalue n_-4 _has multiplicity_ \(\frac{n-2}{2}\) _, and when n is odd the eigenvalue n_-4 _has multiplicity_ \(\frac{n+1}{2}\) _. The eigenvalues_ \(n-5,n-6,\dots,\frac{n-5}{2},\frac{n-11}{2},\dots,-2,-3\) _are simple._

From the computations the authors also concluded that this conjecture is true for \(n\le 100\). Note that Q(100) has 10000 vertices.

