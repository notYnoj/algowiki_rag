**Assumption 2.1.** The function \(U=G+\Psi\) defined by (9) satisfies \(U\in L^\infty(D_s)\). We write

\(M_U:=\left\|U\right\|_{0,\infty,D_s}.\) (17)

_Remark_ 2.2. Since \(G\in C^\infty(\overline{D_s})\), Assumption 2.1 only concerns \(\Psi\). If \(\Gamma\) is of class _C_<sup>2</sup>, \(\Omega\) is convex (for instance a box, the usual choice for the PBE) and \(\hat{g}\) is smooth, then \(\Psi\in H^2(D_p)\cap H^2(D_s)\) by \[34, Theorem 4.1\] and the regularity theory of elliptic interface problems \[28, 10\]; because _D<sub>s</sub>_ is a Lipschitz domain in R<sup>3</sup>, the Sobolev embedding \(H^2(D_s)\unknown\rightarrow C(\overline{D_s})\) then gives \(U\in C(\overline{D_s})\). More generally, the assumption holds whenever \(\Psi\in H^s(D_s)\) for some _s\>_3/2; since the regularity Assumption 4.1 below also allows \(1<s\le 3/2\), we keep Assumption 2.1 as a separate standing assumption. The constant _M<sub>U</sub>_ depends only on the linear problem (7), i.e., on the potential of the solute in pure water, and can be estimated before the nonlinear problem is solved.

## 3 A _C_<sup>2</sup> truncation of the nonlinearity and a priori bounds

The exponential growth of \(\rho\) in (2) is the main difficulty in the finite element error analysis of (15): a priori, the Galerkin approximation of \(\widehat{\Phi}\) is only bounded in _H_<sup>1</sup>, and the nonlinearity is neither globally Lipschitz nor of subcritical growth. In \[19\] this is handled by discrete \(L^\infty\) bounds, which require a mesh condition guaranteeing a discrete maximum principle. Here we proceed differently, following the idea of the "blow-up" test in \[34, Algorithm 2\]: the exponential is replaced by a _C_<sup>2</sup> function of quadratic growth, and we show that this does not change the solution.

### 3.1 The truncated exponential

For \(\tau>0\) define

\(E_\tau(y):=\left\{\begin{array}{ c c }
e^y, & y\le\tau, \\
e^\tau\big(1+(y-\tau)+\frac{1}{2}(y-\tau)^2\big), & y>\tau.
\end{array}\right.\) (18)

That is, \(E_\tau\) is the exponential up to the level \(\tau\) and its second-order Taylor polynomial beyond it.

**Lemma 3.1.** _For every_ \(\tau>0\) _the function_ \(E_\tau\) _has the following properties._

(i) \(E_\tau\in C^2(\mathbb{R})\), \(E'_\tau(y)>0\) _and_ \(0<E''_\tau(y)\le e^\tau\) _for all_ \(y\in\mathbb{R}\)_; in particular_ \(E_\tau\) _is strictly increasing and strictly convex._<tbc>

(ii) \(E_\tau(y)=e^y\), \(E'_\tau(y)=e^y\) _and_ \(E''_\tau(y)=e^y\) _for all_ \(y\le\tau\).<tbc>

(iii) _For all_ \(y\in\mathbb{R}\),<tbc>

\(0<E_\tau(y)\le e^\tau(1+|y|)^2,0<E'_\tau(y)\le e^\tau(1+|y|).\) \(\text{(19)}\)

<tbc>_Proof._ For \(y>\tau\) we have<tbc>

\(E'_\tau(y)=e^\tau\big(1+(y-\tau)\big),E''_\tau(y)=e^\tau,\)

<tbc>while for \(y\le\tau\) all derivatives equal _e<sup>y</sup>_. The one-sided limits of \(E_\tau\), \(E'_\tau\) and \(E''_\tau\) at \(y=\tau\) coincide, which gives (i) and (ii). For (iii), if \(y\le\tau\) then \(E_\tau(y)=e^y\le e^\tau\) and \(E'_\tau(y)\le e^\tau\); if \(y>\tau\) then, since \(0<y-\tau<y\),

\(E_\tau(y)\le e^\tau\big(1+(y-\tau)\big)^2\le e^\tau(1+y)^2,E'_\tau(y)\le e^\tau(1+y).\)

