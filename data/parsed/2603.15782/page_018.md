Every edge _xy_ of graph \(D_\nu\) belongs to \(\langle\mathcal{Q}\rangle\) and thus satisfies \(d_{xy}=\|x-y\|^2\ge\varepsilon\). By (6) and the choice of \(\gamma\),<tbc>

\(\|v_x-v_y\|^2\ge(1-\gamma)d_{xy}-\gamma\tau\ge\varepsilon-\gamma(\varepsilon+\tau)\ge\varepsilon/2.\)

<tbc>Consequently,

\(N\bullet X=-\sum_{xy\in E(D_\nu)}(D_\nu)_{xy}\|v_x-v_y\|^2\le-\frac{\varepsilon}{2}\text{\texttt{val}}(\nu)\le-\alpha\)

## 6.4 Randomized sampling procedure for a small flow (\(\text{\texttt{val}}(\nu)<2\alpha/\varepsilon\))

Assume now that \(\text{\texttt{val}}(\nu)<2\alpha/\varepsilon\); this implies that \(\text{\texttt{OPT}}_\mathcal{Q}<4\alpha/\varepsilon\). We will prove the following result.

**Lemma 19.** _There are constants_ \(c',\zeta,\Delta>0\) _such that a call to_ `DirectionalFlowCut`(_u_) _with_ \(\mu\ge\Theta(\frac{\alpha\sqrt{\beta}}{\varepsilon n})\) _for an appropriate constant and u_∼N(0_,I<sub>d</sub>_) _has minimum network-cut value_ \(F<c'n\mu\) _and produces a_ \(c'\)_-balanced element cut_ (_X,Y,U_) _of cost at most_ \(2c'n\mu\) _with probability at least_ \(\zeta/2\).

The lemma will imply \(\Theta(lnn)\) independent calls to `DirectionalFlowCut`(_u_) will give a desired element cut with probability at least \(1-\frac{1}{n}\).

Fix some \(\mu>0\). Let \((\eta,\xi)\in\mathbb{R}_{\ge 0}^{V\cup E}\times\mathbb{R}_{\ge 0}^S\) be an optimal solution of the dual problem, then \(\sum_{x\in V}\frac{w(x)}{2}\eta_x+\sum_{xy\in E}w(xy)\eta_{xy}+\mu\sum_{x\in S}\xi_x<4\alpha/\varepsilon\) and<tbc>

\(\sum_{x^\prime\in p}\eta_{x^\prime}+\sum_{x^\prime y^\prime\in p}\eta_{x^\prime y^\prime}+\xi_x+\xi_y\ge 1\forall p\in\mathcal{Q}^\text{\texttt{paths}},\partial p=\{x,y\}\) (8)

<tbc>Let us modify \(\eta_x,\eta_{xy},\xi_x\) as follows: (i) truncate all values \(\xi_x\) with \(\xi_x<1/3\) to 0; (ii) multiply all variables \(\eta_x,\eta_{xy},\xi_x\) by 3; (iii) truncate all values \(\xi_x\) with \(\xi_x>1\) to 1. Clearly, (8) still holds, and the new variables satisfy<tbc>

\(J:=\sum_{x\in V}\frac{w(x)}{2}\eta_x+\sum_{xy\in E}w(xy)\eta_{xy}+\mu\sum_{x\in S}\xi_x<12\alpha/\varepsilon\) (9)

<tbc>Furthermore, \(\xi_x\in\{0,1\}\) for each \(x\in S\). Define<tbc>

\(S^*:=\{x\in S:\xi_x=0\},\xi_{xy}:=\eta_x+\eta_{xy}+\eta_y(xy\in E).\)

<tbc>We have

\(\mu\cdot|S-S^*|\le J<\frac{12\alpha}{\varepsilon}.\) (10)

Let \(\varrho\) be the shortest-path pseudometric on _V_ with edge lengths \(\xi_{xy}\). Consider \(x,y\in S^*\) with \(\|x-y\|^2\ge\Delta\). Every path _p_ with \(\partial p=\{x,y\}\) belongs to Q`<sup>paths</sup>`, and thus satisfies

\(\sum_{x^\prime y^\prime\in p}\xi_{x^\prime y^\prime}\ge\sum_{x^\prime\in p}\eta_{x^\prime}+\sum_{x^\prime y^\prime\in p}\eta_{x^\prime y^\prime}+0+0\ge 1\) (11)

by eq. (8). Therefore,

\(x,y\in S^*,\|x-y\|^2\ge\Delta\Longrightarrow\varrho(x,y)\ge 1,\) (12)

while \(\varrho(x,y)\le\xi_{xy}\) for every edge \(xy\in E\).

Next, we prove a useful property of the metric \(\varrho\) constructed in this way. Below \(\theta\) is assumed to be a parameter in (0,1).

