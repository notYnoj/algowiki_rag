## C.2 Boundary behavior and inverse maps

**Lemma C.2** (Boundary behavior)**.** _Fix_ \(\alpha\in(0,1)\) _and_ \(j\neq i^\star\)_. Then_

\(lim_{w\downarrow 0}I_j^\alpha(w)=0,lim_{w\uparrow\infty} I_j^\alpha(w)=\alpha d(\mu_{i^\star},\mu_j).\)

_Consequently,_ \(I_j^\alpha\) _is a_ \(C^\infty\) _strictly increasing bijection from_ \((0,\infty)\) _onto_ \((0,\alpha d(\mu_{i^\star},\mu_j))\).

_Proof of Lemma C.2._ By Proposition C.1,<tbc>

\(I_j^\alpha(w)=\alpha d(\mu_{i^\star},m_j^\alpha(w))+wd(\mu_j,m_j^\alpha(w)).\)

<tbc>As \(w\downarrow 0\), \(m_j^\alpha(w)\rightarrow\mu_{i^\star}\), so both terms vanish. As \(w\uparrow\infty\), \(m_j^\alpha(w)\rightarrow\mu_j\), and hence<tbc>

\(\alpha d(\mu_{i^\star},m_j^\alpha(w))\rightarrow\alpha d(\mu_{i^\star},\mu_j).\)

<tbc>Moreover,

\(m_j^\alpha(w)-\mu_j=\frac{\alpha(\mu_{i^\star}-\mu_j)}{\alpha+w}=O(w^{-1}),\)

and _d(p,q_)=_O_((_q-p_)<sup>2</sup>) as \(q\rightarrow p\). Therefore \(wd(\mu_j,m_j^\alpha(w))\rightarrow 0\). The bijection claim follows from Proposition C.1 and the two endpoint limits.

**Proposition C.3** (Unique fixed-\(\alpha\) optimizer)**.** _For every_ \(\alpha\in(0,1)\) _there exist a unique vector_ \(w^\alpha(\mu)\in\Delta_{1-\alpha}\) _and a unique scalar_ \(\lambda_\alpha>0\) _such that_<tbc>

\(I_j^\alpha(w_j^\alpha(\mu))=\lambda_\alpha\forall j\neq i^\star.\)

<tbc>_Moreover,_ \(\lambda_\alpha=T_\alpha^\star(\mu)^{-1}\)_, and the map_

\(\alpha\longmapsto\big(w^\alpha(\mu),T_\alpha^\star(\mu)^{-1}\big)\)

_is C_<sup>1</sup> _on compact subsets of_ (0,1).

_Proof of Proposition C.3._ Fix \(\alpha\in(0,1)\) and define<tbc>

\(\Delta_j:=d(\mu_{i^\star},\mu_j)>0,j\neq i^\star.\)

<tbc>By Lemma C.2, for each fixed \(\alpha\) the map \(I_j^\alpha:(0,\infty)\rightarrow(0,\alpha\Delta_j)\) is a strictly increasing \(C^\infty\) bijection. Define<tbc>

\(G_j(\alpha,\lambda):=(I_j^\alpha)^{-1}(\lambda),0<\lambda<\alpha\Delta_j.\)

<tbc>Let<tbc>

\(\Delta_\mathrm{min}:=\mathrm{min}_{j\neq i^\star}\Delta_j,F(\alpha,\lambda):=\sum_{j\neq i^\star} G_j(\alpha,\lambda)-(1-\alpha),\)

<tbc>on the domain<tbc>

\(\{(\alpha,\lambda):\alpha\in(0,1),0<\lambda<\alpha\Delta_\mathrm{min}\}.\)

<tbc>For fixed \(\alpha\), the map \(\lambda\mapsto F(\alpha,\lambda)\) is continuous and strictly increasing. In addition,

\(\mathrm{lim}_{\lambda\downarrow 0}F(\alpha,\lambda)=-(1-\alpha)<0,\)

whereas

\(\mathrm{lim}_{\lambda\uparrow\alpha\Delta_\mathrm{min}}F(\alpha,\lambda)=+\infty,\)

because at least one inverse diverges as \(\lambda\uparrow\alpha\Delta_\mathrm{min}\). Therefore there exists a unique \(\lambda_\alpha\in(0,\alpha\Delta_\mathrm{min})\) satisfying \(F(\alpha,\lambda_\alpha)=0\). Set \(w_j^\alpha(\mu):=G_j(\alpha,\lambda_\alpha)\). Then \(w^\alpha(\mu)\in\Delta_{1-\alpha}\) and \(I_j^\alpha(w_j^\alpha(\mu))=\lambda_\alpha\) for every \(j\neq i^\star\).

For optimality, let \(w\in\Delta_{1-\alpha}\) and write<tbc>

\(m(w):=\mathrm{min}_{j\neq i^\star} I_j^\alpha(w_j).\)

<tbc>Since each \(I_j^\alpha\) is increasing,<tbc>

\(w_j\ge G_j(\alpha,m(w))\forall j\neq i^\star.\)

