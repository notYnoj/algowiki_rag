**Definition 26** (Fraction of retained accuracy)**.** _For x,y with_ \(\mathcal{M}(x,y)\neq 0\) _and a parameter choice_ \(\lambda=\lambda(\epsilon)\in(0,1]\)_, define the relative-error bounds_

\(e(\epsilon,x,y)=\frac{\|x\|_2\|y\|_2}{\|\mathcal{M}(x,y)\|_2}\big[(1+\epsilon)^3\beta(\lambda)+\big((1+\epsilon)^3-1\big)\big(1+(1+\epsilon)^3\sigma(\Xi(\lambda))\big)\big],\) (142)

\(e_c(\epsilon,x,y)=\frac{\|x\|_2\|y\|_2}{\|\mathcal{M}(x,y)\|_2}\big((1+\epsilon)^3-1\big)\big(1+(1+\epsilon)^3\sigma_c\big).\) (143)

_For_ \(0<e(\epsilon,x,y),e_c(\epsilon,x,y)<1\)_, the fraction of classical-reference accuracy retained by the bound is_

\(\theta(\epsilon,x,y)=\frac{log(1/e(\epsilon,x,y))}{log(1/e_c(\epsilon,x,y))}.\) (144)

_The limiting fraction is_ \(\theta=lim_{\epsilon\rightarrow 0}\theta(\epsilon,x,y)\)_, when this limit exists._

The two bounds include the same model for input and output rounding. Their algorithm-dependent terms use \(\sigma(\Xi(\lambda))\) and \(\sigma_c\), respectively. The logarithms measure the digits guaranteed by these bounds; their ratio need not equal the limiting fraction at a particular working precision.

**Lemma 11** (Parameter choice and retained accuracy)**.** _Under the rounding assumptions of Lemma 9, for_ \(0<\lambda\le 1\) _and_ \(\mathcal{M}(x,y)\neq 0\),

\(\frac{\|\widehat{z}-\mathcal{M}(x,y)\|_2}{\|x\|_2\|y\|_2}\le(1+\epsilon)^3\beta(\lambda)+\big((1+\epsilon)^3-1\big)\big(1+(1+\epsilon)^3\sigma(\Xi(\lambda))\big).\) (145)

_For a construction from Theorem 3 with_ \(\mathcal{J}\neq\emptyset\)_, use its normalized grading from Definition 21 and let_

\(\lambda_\text{bal}(\epsilon)=min\left\{1,\big(\frac{3\epsilon\sigma_0}{\beta'(0)}\big)^{1/(h+1)}\right\}.\) (146)

_Then_

\(e(\epsilon,x,y)=O\big(\epsilon^{1/(h+1)}\big),\theta=\frac{1}{1+h}.\) (147)

_For an exact construction,_ \(\lambda=1\) _instead gives_ \(\theta=1\).

_Proof._ Apply Lemma 9 to \(\mathcal{L}=\mathcal{M}_\lambda\), then add the approximation error. By (127) and Lemma 8, \(\|\mathcal{M}_\lambda\|\le 1+\beta(\lambda)\); substituting this bound gives (145). The smallest degree among the remaining mixed products is one, with a positive coefficient in \(\beta\), so \(\beta'(0)>0\) and \(\beta(\lambda)=\beta'(0)\lambda+o(\lambda)\). Equation (139) gives \(\sigma(\Xi(\lambda))=\sigma_0\lambda^{-h}\) for sufficiently small positive \(\lambda\), with \(\sigma_0>0\). If _h_=0, the nonnegative differences _a<sub>t</sub>_-min_<sub>s</sub>a<sub>s</sub>_, _b<sub>t</sub>_-min_<sub>s</sub>b<sub>s</sub>_, and _c<sub>t</sub>_-min_<sub>s</sub>c<sub>s</sub>_ sum to zero for every _t_, making every mixed degree zero, contrary to normalization. Thus _h\>_0, and the leading error terms are

\(\beta'(0)\lambda+3\epsilon\sigma_0\lambda^{-h}.\) (148)

Equating them gives (146), before clipping at one. As \(\epsilon\rightarrow 0\), the choice tends to zero, so the small-parameter norm identity applies and these terms are positive constants times \(\epsilon^{1/(h+1)}\). The contribution independent of the factorization is \(O(\epsilon)\) and hence of smaller order; the higher-order terms in (145) are also smaller. The classical bound satisfies \(e_c(\epsilon,x,y)\sim 3(1+\sigma_c)\|x\|_2\|y\|_2\epsilon/\|\mathcal{M}(x,y)\|_2\). Consequently,

\(log\frac{1}{e(\epsilon,x,y)}=\frac{1}{1+h}log\frac{1}{\epsilon}+O(1),log\frac{1}{e_c(\epsilon,x,y)}=log\frac{1}{\epsilon}+O(1).\) (149)

Their ratio tends to 1/(1+_h_). For an exact construction, \(\beta=0\) and \(\lambda=1\) make both bounds positive constants times \(\epsilon\), so the limiting fraction is one.

For normalized heights \(h\le 1,2,3\), respectively, the limiting retained fraction is at least 1/2,1/3,1/4. The residual coefficients and replicated-coordinate factors in \(\beta\) also affect the finite-precision bound. At a<tbc>

