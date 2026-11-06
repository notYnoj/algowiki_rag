<tbc>We define the GMM \(\mu^\star:=(1-w)\mathcal{N}(0,\varepsilon^2)+w\mathcal{N}(m^\star,\varepsilon^2)\) associated to the vanishing gradient point, and introduce \(\theta^\star:=((1-w),0,m^\star)\) its parameters. For any \(X\in\mathbb{R}^{6\times 1}\), we denote by \(\theta(X)\) the parameters of the GMM fitted by the EM algorithm in one iteration on _X_ with initialisation \(\theta^\star\): \(\theta(X):=F(\theta^\star,X)\) (we remind that in this section, we consider a simplified EM that does not update covariances). We shall first see that \(\theta(X_\varepsilon)\approx\theta^\star\), then that the energy

\(\mathcal{E}_{\mathrm{EM}-\mathrm{MW}_2^2}:=X\longmapsto\mathrm{MW}_2^2(\mu(\theta(X)),\nu),\mu(\theta(X)):=\alpha(X)\mathcal{N}(m_1(X),\varepsilon^2)+(1-\alpha(X))\mathcal{N}(m_2(X),\varepsilon^2),\)

verifies \(\partial_X\mathcal{E}_{\mathrm{EM}-\mathrm{MW}_2^2}(X_\varepsilon)\approx 0\). We summarise our setting in Fig. 17.

## Showing that \(\theta(X_\varepsilon)\approx\theta^\star\).

Using the expressions of the EM update from Eq. (3), we obtain that responsibilities \(\gamma(X_\varepsilon)\) computed with initialisation \(\theta^\star\) verify:

\(\forall i\in\{1,2\},\gamma_{i,1}(X_\varepsilon)=1+\mathcal{O}(e^{-1/\varepsilon^2}),\forall i\in\{3,4,5,6\},\gamma_{i,2}(X_\varepsilon)=1+\mathcal{O}(e^{-1/\varepsilon^2}),\)

as \(\varepsilon\longrightarrow 0^+\). This means that the two points _x_<sub>1</sub>_,x_<sub>2</sub> are considered as belonging to the first component \(\mathcal{N}(0,\varepsilon^2)\) of \(\mu^\star\), and the four points _x_<sub>3</sub>_,x_<sub>4</sub>_,x_<sub>5</sub>_,x_<sub>6</sub> to the second component \(\mathcal{N}(m^\star,\varepsilon^2)\) of \(\mu^\star\). As for the weight \(\alpha(X_\varepsilon)\) and means \(m(X_\varepsilon)\) of the GMM \(F(\theta^\star,X^\star)\), we use Eq. (4) to deduce that:

\(\alpha(X_\varepsilon)=(1-w)+\mathcal{O}(e^{-1/\varepsilon^2}),m_1(X_\varepsilon)=0+\mathcal{O}(e^{-1/\varepsilon^2}),m_2(X_\varepsilon)=m^\star+\mathcal{O}(e^{-1/\varepsilon^2}).\) (80)

In this sense, we have \(\theta(X_\varepsilon)\approx\theta^\star\) as \(\varepsilon\longrightarrow 0^+\).

## Vanishing gradient of the energy \(\mathcal{E}_{\mathrm{EM}-\mathrm{MW}_2^2}\) at \(X_\varepsilon\).

For \(\varepsilon>0\) sufficiently small and _X_ in a sufficiently small open vicinity of \(X_\varepsilon\), it follows by regularity of _F_ that \(\theta(X)=(\alpha(X),m_1(X),m_2(X))\) will be sufficiently close to \(\theta(X_\varepsilon)\) to ensure that \(\alpha(X)<w\) and that _m_<sub>1</sub>(_X)\<m_<sub>2</sub>(_X_), which yields (by property on one-dimensional OT) the following expression for the energy:

\(\mathcal{E}_{\mathrm{EM}-\mathrm{MW}_2^2}(X):=\mathrm{MW}_2^2(\mu(\theta(X)),\nu)=\mathcal{F}(\alpha(X),m_1(X),m_2(X)),\)

where \(\mathcal{F}:(0,1)\times\mathbb{R}\times\mathbb{R}\longrightarrow\mathbb{R}\) is the function defined by:

\(\forall(\alpha,m_1,m_2)\in(0,1)\times\mathbb{R}\times\mathbb{R},\mathcal{F}(\alpha,m_1,m_2):=\alpha m_1^2+(w-\alpha)m_2^2+(1-w)(m_2-1)^2.\)

To determine the gradient of \(\mathcal{E}_{\mathrm{EM}-\mathrm{MW}_2^2}\) at \(X_\varepsilon\), we use the chain rule:

\(\nabla\mathcal{E}_{\mathrm{EM}-\mathrm{MW}_2^2}(X_\varepsilon)=\frac{\partial\mathcal{F}}{\partial\alpha}(\theta(X_\varepsilon))\frac{\partial\alpha}{\partial X}(X_\varepsilon)+\frac{\partial\mathcal{F}}{\partial m_1}(\theta(X_\varepsilon))\frac{\partial m_1}{\partial X}(X_\varepsilon)+\frac{\partial\mathcal{F}}{\partial m_2}(\theta(X_\varepsilon))\frac{\partial m_2}{\partial X}(X_\varepsilon).\)

μ
V
E
X3
X4
X1
0
X2
X5
1
X6
1
2

Figure 17: With the data \(X_\varepsilon:=(x_1,\cdots,x_6)\), one iteration of the EM algorithm initialised at \(\theta^\star\) (corresponding to the GMM \(\mu^\star\)) yields approximately the same parameters \(\theta^\star\). We shall see that the gradient of the energy \(\mathcal{E}_{\mathrm{EM}-\mathrm{MW}_2^2}\) at \(X_\varepsilon\) is approximately zero, illustrating the vanishing gradient phenomenon.

