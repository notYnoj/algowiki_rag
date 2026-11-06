## Analysis on R<sub>=</sub>.

For \((x_1,x_2,\alpha)\in\mathcal{R}_=\), we have:<tbc>

\(\mathcal{E}^-(x_1,x_2,\alpha)=\mathcal{E}_=^-(x_1,x_2):=\gamma c(x_1,y_1)+(1-\gamma)c(x_2,y_2),\)

<tbc>thus a local minimum \((x_1,x_2,\alpha)\in\mathcal{R}_=\) of E<sup>-</sup> must satisfy the stationarity conditions:

\(0=\frac{\partial\mathcal{E}_=^-}{\partial x_1}=\gamma\nabla\phi(x_1-y_1)\Longrightarrow_{(\text{H3})}x_1=y_1,\)<br>
\(0=\frac{\partial\mathcal{E}_=^-}{\partial x_2}=(1-\gamma)\nabla\phi(x_2-y_2)\Longrightarrow_{(\text{H3})}x_2=y_2,\)

Since \((x_1,x_2,\alpha)=(y_1,y_2,\gamma)\) is a global minimum of \(\mathcal{E}_=^-\), we conclude that the only local minimum of E<sup>-</sup> in D is \((y_1,y_2,\gamma)\).

Using Eq. (78), we deduce that the only local minimum of E<sup>+</sup> in D is \((y_2,y_1,1-\gamma)\), which is a global minimum of E<sub>2</sub> in D. Finally, there are two local minima of E<sub>2</sub> in D, which are the two global minima corresponding to \(\mu(x_1,x_2,\alpha)=\nu\).

## Local minimum for a single-Dirac source, and how to avoid it.

The constraint \((x_1,x_2,\alpha)\in\mathcal{D}\) imposes in particular that \(\mu(x_1,x_2,\alpha)\) is composed of two distinct Dirac masses. We now focus on the pathological case where \(\alpha=0\), showing the existence of a local optimum. For simplicity, we consider _d_=1 and the cost _c(x,y_):=|_x-y_|<sup>2</sup>. Set<tbc>

\(z^\star:=(x_1^\star,x_2^\star,\alpha^\star):=(-1,1-\gamma,0),y_1:=0,y_2:=1,\gamma\in(0,1).\)

<tbc>For \((x_1,x_2,\alpha)\) in an open vicinity of _z<sup>⋆</sup>_, the cost simplifies to<tbc>

\(\mathcal{E}_2(x_1,x_2,\alpha)=\alpha x_1^2+(\gamma-\alpha)x_2^2+(1-\gamma)(x_2-1)^2.\)

<tbc>To show that _z<sup>⋆</sup>_ is a local minimum, we compute the gradient of E<sub>2</sub> at _z<sup>⋆</sup>_:<tbc>

\(\frac{\partial\mathcal{E}_2}{\partial x_1}(z^\star)=2\alpha^\star x_1^\star=0,\)<br>
\(\frac{\partial\mathcal{E}_2}{\partial x_2}(z^\star)=2\left(x_2^\star-(1-\gamma)\right)=0,\)<br>
\(\frac{\partial\mathcal{E}_2}{\partial\alpha}(z^\star)=x_1^2-x_2^2=1-(1-\gamma)^2>0.\)

<tbc>Consider a perturbation \(h:=(h_1,h_2,h_3)\in\mathbb{R}^3\) with _h_<sub>3</sub>_\>_0 (as \(\alpha\ge 0\)). For _z_:=_z<sup>⋆</sup>+h_, we have:

\(\mathcal{E}_2(z)=\mathcal{E}_2(z^\star)+\underbrace{\frac{\partial\mathcal{E}_2}{\partial\alpha}}_{>0}(z^\star)h_3+\mathcal{O}(\|h\|^2),\)

so every feasible perturbation increases the objective. Thus _z<sup>⋆</sup>_ is a strict local minimiser, but is not global. When \(\alpha\) arises as a mixture weight in EM, two remedies are possible: fixing uniform weights, or enforcing \(\alpha\ge\varepsilon>0\): both methods sidestep the degenerate local minimum above.

## A.7.3 Essential Stationary Points for the MW2-EM Loss: Computations

We illustrate a phenomenon of points where the gradients are infinitesimally small on a simple example with two Gaussian components, and studying a variant of the EM algorithm that does not update the covariances for simplicity. We fix \(\varepsilon>0\) and the following parametrised input GMM:<tbc>

\(\forall\alpha\in(0,1),\forall m_1,m_2\in\mathbb{R},\mu(\alpha,m_1,m_2):=\alpha\mathcal{N}(m_1,\varepsilon^2)+(1-\alpha)\mathcal{N}(m_2,\varepsilon^2),\)

<tbc>and for \(w:=\frac{2}{3}\), the target GMM: \(\nu:=w\mathcal{N}(0,\varepsilon^2)+(1-w)\mathcal{N}(1,\varepsilon^2)\). We consider the particular dataset \(X_\varepsilon\in\mathbb{R}^{6\times 1}\) defined by:<tbc>

\(X_\varepsilon:=(x_1,\cdots,x_6),x_1:=-\varepsilon,x_2:=\varepsilon,x_3:=x_5:=m^\star-\varepsilon,x_4:=x_6:=m^\star+\varepsilon.\)

