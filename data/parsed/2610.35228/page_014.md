A separation oracle for _F_ can be implemented in polynomial time using exact rational arithmetic. Symmetric Gaussian elimination on _M(y_) either certifies positive semidefiniteness or produces a rational vector _x_ with \(x^\top M(y)x<0\). In the latter case, write the affine function \(x^\top M(z)x\) in the reduced coordinates as \(a^\top z+b\). Every \(z\in F\) satisfies \(a^\top z+b\ge 0\), while \(a^\top y+b<0\), so \(a^\top z\ge-b\) is a separating inequality.

For \(\epsilon>0\), let \(S(F,\epsilon)\) be the set of points at Euclidean distance at most \(\epsilon\) from _F_, and let \(S(F,-\epsilon)\) be the set of points whose closed \(\epsilon\)-ball lies in _F_. By the ellipsoid method for weak optimization over a well-bounded convex body with a separation oracle \[GLS88, Chapter 4\], for every rational \(\epsilon\in(0,\rho_0)\) one can compute a rational \(y^1\in S(F,\epsilon)\) such that

\(f(y^1)\ge f(x)-\epsilon\text{for every}x\in S(F,-\epsilon).\)

The running time is polynomial in _D_, \(log(1/\rho_0)\), \(log(1/\epsilon)\), and the encoding lengths of the rational data.

We next express this guarantee in terms of OPT. Fix a rational \(\eta\in(0,1)\), choose \(x^*\in F\) with _f(x_<sup>∗</sup>)=OPT, and set<tbc>

\(\epsilon:=\frac{\eta\rho_0}{2N},\lambda:=\frac{\epsilon}{\rho_0}=\frac{\eta}{2N},x':=(1-\lambda)x^*+\lambda y^0.\)

<tbc>The identity \(\lambda=\eta/(2N)\) follows by substituting the definition of \(\epsilon\). For every _z_ with \(\|z\|_2\le\epsilon\), the point \(y^0+z/\lambda\) belongs to the ball of radius \(\rho_0\) around _y_<sup>0</sup>, hence to _F_. Convexity then gives \(x'+z=(1-\lambda)x^*+\lambda(y^0+z/\lambda)\in F\). Thus \(x'\in S(F,-\epsilon)\). Moreover,<tbc>

\(f(x')\ge(1-\lambda)\text{OPT}\ge\text{OPT}-\eta/2.\)

<tbc>The first step uses \(f(y^0)\ge 0\), and the second step uses \(\text{OPT}\le N\) and \(\lambda=\eta/(2N)\). The weak optimization guarantee now gives

\(\text{dist}(y^1,F)\le\epsilon\le\eta,f(y^1)\ge f(x')-\epsilon\ge\text{OPT}-\eta.\)

In the distance bound, the first step follows from \(y^1\in S(F,\epsilon)\) and the second step uses \(\epsilon\le\eta/2\). In the objective bound, the first step follows from weak optimization and the second step uses the preceding bound on \(f(x')\) and \(\epsilon\le\eta/2\). The inequality \(\epsilon\le\eta/2\) follows from \(\rho_0\le 1\le N\).

Take \(\eta:=\widehat{\lambda}/(4Nn_r)\) and \(\eta':=\eta n_r=\widehat{\lambda}/(4N)\). Applying Claim 5 to _y_<sup>1</sup> and a nearest point in the compact set _F_ gives \(M(y^1)\unknown-\eta'\text{Id}\). Define<tbc>

\(\theta:=\frac{\eta'}{\eta'+\widehat{\lambda}}=\frac{1}{4N+1},y:=(1-\theta)y^1+\theta y^0,\)

<tbc>and output \(\mu:=\mu_y\). The identity \(\theta=1/(4N+1)\) follows by substituting \(\eta'=\widehat{\lambda}/(4N)\) into the definition of \(\theta\). The vector _y_ is rational and has \(y_\emptyset=1\). Also,<tbc>

\(M(y)=(1-\theta)M(y^1)+\theta M(y^0)\unknown\big(\theta\widehat{\lambda}-(1-\theta)\eta'\big)\text{Id}=0.\)

<tbc>The first step uses that _M_ is affine in the reduced coordinates and the coefficients sum to one. The second step combines Claim 4 with \(M(y^1)\unknown-\eta'\text{Id}\), and the third step follows from the definition of \(\theta\). Thus Claim 1 shows that \(\mu\) is a level-_r_ pseudo-distribution. Finally,<tbc>

\(f(y)\ge(1-\theta)(\text{OPT}-\eta)\ge\text{OPT}-\eta-\theta\text{OPT}\ge\text{OPT}-\frac{1}{2}.\)

