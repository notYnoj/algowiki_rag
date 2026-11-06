<tbc>Differentiating F and evaluating at \(\theta(X_\varepsilon)\) which verifies the properties given in Eq. (80) yields:

\(\frac{\partial\mathcal{F}}{\partial\alpha}(\theta(X_\varepsilon))=-m^\star+\mathcal{O}(e^{-1/\varepsilon^2})=\mathcal{O}(1),\frac{\partial\mathcal{F}}{\partial m_1}(\theta(X_\varepsilon))=\mathcal{O}(e^{-1/\varepsilon^2}),\frac{\partial\mathcal{F}}{\partial m_2}(\theta(X_\varepsilon))=\mathcal{O}(e^{-1/\varepsilon^2}).\)

Using the expression of \(\frac{\partial\alpha}{\partial X}\) from Eq. (45) with \(X:=X_\varepsilon\) and \(\theta:=\theta^\star\) yields \(\frac{\partial\alpha}{\partial X}(X_\varepsilon)=\mathcal{O}(\varepsilon^{-2}e^{-1/\varepsilon^2})\).

With the expressions of \(\frac{\partial m_1}{\partial X}\) and \(\frac{\partial m_2}{\partial X}\) computed in Eq. (59), we obtain \(\frac{\partial m_1}{\partial X}(X_\varepsilon)=\mathcal{O}(1)\) and \(\frac{\partial m_2}{\partial X}(X_\varepsilon)=\mathcal{O}(1)\). Putting everything together, we conclude that the gradient vanishes:

\(\nabla\mathcal{E}_{\mathrm{EM}-\mathrm{MW}_2^2}(X_\varepsilon)=\mathcal{O}(\varepsilon^{-2}e^{-1/\varepsilon^2}).\)

## A.7.4 Source Weights Fixed to the Target Weights

When the source and target GMMs have the same number of components, a natural idea is to keep the weights fixed to the target weights in the source EM steps. However, doing so can result in unwanted local minima, as shown by the following example.

_Proof._ As the Gaussian components have the same variance, their pairwise squared W<sub>2</sub> costs reduce to squared distances between their means. We focus on the open region \(\mathcal{R}_>:=\{(x_1,x_2)\in\mathbb{R}^2,x_1>x_2\}\). In the region R_<sub>\></sub>_,

\(\mathrm{MW}_2^2(\mu_x,\nu)=qx_2^2+(p-q)x_1^2+q(x_1-1)^2.\)

At _x<sup>⋆</sup>_, this quadratic objective has gradient zero and Hessian \(2\mathrm{diag}(p,q)\succ 0\). As _x<sup>⋆</sup>_ lies in the interior of the region R_<sub>\></sub>_, it is a strict local minimum of this function. Direct substitution gives \(\mathrm{MW}_2^2(\mu_{x^\star},\nu)=\frac{q(p-q)}{p}>0\), whereas \(\mu_{(0,1)}=\nu\).

We compare the impact of fixing source weights to target weights or to uniform weights in the colour- transfer experiment in Fig. 19. In this experiment, the colour transfer appears to be slightly more faithful to the target when the source weights are fixed to uniform weights.

q
p
source
p
q
q
q
target
p
q
x
0
1
q/p

0.8
1
global minimum (0, 1), MW2 = 0
0.6
0.5
0.4
MW2
strict local minimum (2/3, 0), MW2 = 2/15
0.2
0
0
0
0.5
1
X1

**Example A.2.** Let \(p\in(\frac{1}{2},1)\), set _q_:=1-_p_ and fix \(\sigma>0\). For \(\mu_x:=p\mathcal{N}(x_1,\sigma^2)+q\mathcal{N}(x_2,\sigma^2)\), and \(\nu:=p\mathcal{N}(0,\sigma^2)+q\mathcal{N}(1,\sigma^2)\), the map \(x\mapsto\mathrm{MW}_2^2(\mu_x,\nu)\) has a strict non-global local minimum at \(x^\star=(\frac{q}{p},0)\), with value \(\frac{q(p-q)}{p}>0\). Its global minimum has value zero at _x_=(0,1).

(a) Configuration at the local minimum

(b) Objective landscape

Figure 18: Local minimum in Example A.2 with fixed non-uniform weights.

