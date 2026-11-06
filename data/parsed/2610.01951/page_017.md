## C Population Allocation Calculus and the Discrete Penalized Benchmark

### C.1 Bernoulli two-arm calculus

Fix \(\alpha\in(0,1)\), \(j\neq i^\star\), and _w\>_0. Define<tbc>

\(m_j^\alpha(w):=\frac{\alpha\mu_{i^\star}+w\mu_j}{\alpha+w}.\)

<tbc>By Remark B.2, the infimum in the definition of \(I_j^\alpha(w)\) is uniquely attained at \(x=m_j^\alpha(w)\), and<tbc>

\(I_j^\alpha(w)=\alpha d(\mu_{i^\star},m_j^\alpha(w))+wd(\mu_j,m_j^\alpha(w)).\)

<tbc>**Proposition C.1** (Bernoulli population-allocation calculus)**.** _The map_ \(I_j^\alpha\) _is_ \(C^\infty\) _on_ \((0,\infty)\)_, strictly increasing, and strictly concave. More precisely,_<tbc>

\(\frac{d}{dw}I_j^\alpha(w)=d(\mu_j,m_j^\alpha(w))>0,\)

<tbc>_and_<tbc>

\(\frac{d^2}{dw^2}I_j^\alpha(w)=-\frac{\alpha^2(\mu_{i^\star}-\mu_j)^2}{(\alpha+w)^3m_j^\alpha(w)(1-m_j^\alpha(w))}<0.\)

<tbc>_Proof of Proposition C.1._ For \(x\in(0,1)\), let<tbc>

\(f_w(x):=\alpha d(\mu_{i^\star},x)+wd(\mu_j,x).\)

<tbc>Since<tbc>

\(\frac{\partial}{\partial x}d(p,x)=-\frac{p}{x}+\frac{1-p}{1-x}=\frac{x-p}{x(1-x)},\)

<tbc>we obtain<tbc>

\(f'_w(x)=\frac{(\alpha+w)x-(\alpha\mu_{i^\star}+w\mu_j)}{x(1-x)}.\)

<tbc>Hence \(f'_w(x)=0\) if and only if \(x=m_j^\alpha(w)\). Also,

\(f''_w(x)=\frac{\alpha\mu_{i^\star}+w\mu_j}{x^2}+\frac{\alpha(1-\mu_{i^\star})+w(1-\mu_j)}{(1-x)^2}>0,\)

so _f<sub>w</sub>_ is strictly convex and the minimizer is unique.

Because \(w\mapsto m_j^\alpha(w)\) is smooth, so is \(I_j^\alpha\). The envelope theorem gives<tbc>

\(\frac{d}{dw}I_j^\alpha(w)=\frac{\partial}{\partial w}f_w(m_j^\alpha(w))=d(\mu_j,m_j^\alpha(w)).\)

<tbc>Since \(\mu_j<\mu_{i^\star}\), one has \(m_j^\alpha(w)\in(\mu_j,\mu_{i^\star})\), and therefore \(d(\mu_j,m_j^\alpha(w))>0\). Finally,<tbc>

\(\frac{d}{dq}d(p,q)=\frac{q-p}{q(1-q)},\frac{d}{dw}m_j^\alpha(w)=\frac{\alpha(\mu_j-\mu_{i^\star})}{(\alpha+w)^2}.\)

<tbc>Differentiating once more yields<tbc>

\(\frac{d^2}{dw^2}I_j^\alpha(w)=\frac{m_j^\alpha(w)-\mu_j}{m_j^\alpha(w)(1-m_j^\alpha(w))}\cdot\frac{\alpha(\mu_j-\mu_{i^\star})}{(\alpha+w)^2}.\)

<tbc>Using

\(m_j^\alpha(w)-\mu_j=\frac{\alpha(\mu_{i^\star}-\mu_j)}{\alpha+w},\)

we recover the stated formula, which is strictly negative.

