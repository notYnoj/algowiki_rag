**Definition 4.5** (Discrete Fourier Transform, DFT)**.** Let \(\mathbf{x}=(x_0,\cdots,x_{n-1})^T\in\mathcal{K}^n\) be a column vector over the ring K. Define the matrix

\(F_n=\left(\begin{array}{ c c c c c }
1 & 1 & 1 & \cdots & 1 \\
1 & \omega_n^1 & \omega_n^2 & \cdots & \omega_n^{n-1} \\
\vdots & \ddots & \vdots &  &  \\
1 & \omega_n^{1(n-1)} & \omega_n^{2(n-1)} & \cdots & \omega_n^{(n-1)(n-1)}
\end{array}\right)\)

in \(\mathcal{K}^{n\times n}\) where \(\omega_n\) is an _n_th order principal root of unity in K. The discrete Fourier transform is the linear transformation \(\mathbf{x}\mapsto F_n\cdot\mathbf{x}\).

**Corollary 4.6.** Over any (_S,T_)-uniform ring K=K_<sub>n</sub>_, for _n_ a power of 2, if K admits a principal _n_th root of unity, with both that root and its inverse computable in _S_ space and _T_ time, then there exists a catalytic algorithm running in time \(\widetilde{O}\left(nT\right)\), clean space _O_(log(_n_)+log(_T_)+_S_), and dirty space \(\widetilde{O}\left(nlog|\mathcal{K}|\right)\), which takes as input a sequence \(x\in\mathcal{K}^n\), and outputs the discrete Fourier transform _F<sub>n</sub>x_.

_Proof._ The classic Number Theoretic Transform algorithm and its inverse are directly implementable as #NC(K) circuits of multiplicative depth 0 -- i.e., with only addition and scalar multiplication gates -- assuming a principal _n_th root of unity and its inverse are available as constants \[CLRS09, Section 30.2\]. Theorem 4.3 therefore allows such circuits to be evaluated catalytically with only polylogarithmic overhead in time complexity.

We could have obtained a similar result in Section 3, but recall that there our algorithm would have required _n_<sup>1+_o_(1)</sup> time, as opposed to \(\widetilde{O}\left(n\right)\), and would have been difficult to make work over as general a class of rings, since we would have to implement the ring operations themselves as sufficiently low-depth symmetric circuits.

The ability to compute fast Fourier transforms also allows us to obtain quasilinear-time catalytic algorithms for a number of applications. For instance:

**Corollary 4.7.** For any (_S,T_)-uniform ring K, there exists a catalytic algorithm which takes as input two degree-_n_ polynomials \(p,q\in\mathcal{K}[x]\) and outputs their product _pq_, using \(\widetilde{O}\left(nT\right)\) time, _O_(log(_n_)+_S_) clean space, and \(\widetilde{O}\left(nT\right)\) dirty space.

_Proof._ The quasilinear-time algorithm of Cantor and Kaltofen is bilinear, meaning it can be implemented by a #NC(K) circuit of multiplicative depth 1 \[CK91\]. (Note that this algorithm does not even require knowing roots of unity.) Thus, Theorem 4.3 again yields a quasilinear-time catalytic algorithm.

**Corollary 4.8** (#3SUM for Small Universes)**.** Let \(A,B,C\subseteq[0,M]\) be three integer lists for \(2\le M\le poly(n)\), let _t_ be an integer, and let _n_=max{|_A|,|B|,|C_|}. There is a catalytic algorithm counting the number of triplets \(a\in A\), \(b\in B\), and \(c\in C\) such that _a+b+c=t_ using \(\widetilde{O}\left(n+M\right)\) time, \(\widetilde{O}\left(M\right)\) dirty space, and _O_(log_n_) clean space.

_Proof._ As is standard (see, e.g., \[CLRS09, Ex. 30.1-7\]), we can represent _A_, _B_, and _C_ by degree-_M_ polynomials _a_, _b_, and _c_, respectively, where the coefficient on _x<sup>i</sup>_ is equal to the number of times that _i_ appears in the set. (We only need to sequentially iterate over each _A,B,C_ once to add these polynomials to the appropriate registers. Given each _A<sub>i</sub>_ (resp. _B<sub>i</sub>_, _C<sub>i</sub>_) value, add 1 into the corresponding coefficient register.) By two applications of the construction from Corollary 4.7, we can catalytically compute the product of all three of these polynomials over Z/((_M_+1)_n_<sup>3</sup>+1)Z in \(\widetilde{O}\left(n+M\right)\) time, _O(M_log_M_log_n_) dirty space, and _O_(log_n_) clean space. Now, by computing the coefficient on _x<sup>t</sup>_ in this product directly into the clean space as opposed to a catalytic register, we obtain the desired result.

