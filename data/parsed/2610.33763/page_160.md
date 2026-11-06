<tbc>_the matrix_ \(\widetilde{G}(\kappa,\xi)(x,\theta)\) _and put_ \(D=[0,1]\times[-\pi,\pi]\) _(so_ \(\mu(D)=2\pi\)_). Define the probability space by the triple_<tbc>

\((\Omega,\mathcal{F},\mathbb{P}),\Omega=D\times\{1,\dots,r\},\mathcal{F}=\mathcal{B}(D)\otimes 2^{\{1,\dots,r\}}.\)

<tbc>_Here,_ B(_D_) _denotes the Borel_ \(\sigma\)_-algebra on D,_ 2<sup>{1_,...,r_}</sup> _denotes the power set of_ {1_,...,r}, and the product measure is_<tbc>

\(\mathbb{P}(A\times B)=\frac{\mu(A)}{2\pi}\frac{|B|}{r},A\in\mathcal{B}(D),B\subseteq\{1,\dots,r\}.\)

<tbc>_With this choice,_

\(\mathbb{P}(\Omega)=\frac{\mu(D)}{2\pi}\cdot\frac{r}{r}=1,\)

_so that_ \((\Omega,\mathcal{F},\mathbb{P})\) _is indeed a probability space._

_Introduce the random variable_

\(X(x,\theta,i):=\lambda_i\big(\widetilde{G}(\kappa,\xi)(x,\theta)\big),(x,\theta,i)\in\Omega,\)

_where the eigenvalues are ordered non-decreasingly. The quantile function of X is precisely the_ non-decreasing rearrangement \(\widetilde{G}^\dagger\) _of the matrix-valued symbol._

_Because spectral distributions are defined only up to measure-preserving rearrangements, we deduce that_

\(\{G_n\}_n\sim_\lambda\widetilde{G}\Longrightarrow\{G_n\}_n\sim_\lambda\widetilde{G}^\dagger,\)

_so verifying convergence to the quantile_ \(\widetilde{G}^\dagger\) _is equivalent and numerically simpler than verifying convergence to the symbol_ \(\widetilde{G}(\kappa,\xi)\) _itself._

_Furthermore, whenever_ \(\widetilde{G}^\dagger\) _is continuous at_ \(t\in(0,1)\)_, the sorted eigenvalues satisfy_ \(\lambda_{\lceil tdn_n\rceil}(G_n)\rightarrow\widetilde{G}^\dagger(t)\) _as_ \(n\rightarrow\infty\)_, and the empirical proportion of eigenvalues below a small threshold t_<sub>0</sub> _(we take t_<sub>0</sub>=0.1_) converges to_ \(\mathbb{P}[X\le t_0]\)_, therefore it can be used as an estimate of the measure of the rank-deficient subset_ \(\{(x,\theta):\widetilde{G}(\kappa,\xi)(x,\theta)=0\}\).

## Numerical results

In this section, we compare the sorted eigenvalues of each geometric mean matrix _G(A<sub>n</sub>,B<sub>n</sub>_) with the rearranged eigenvalue distribution predicted by the candidate symbol \(\widetilde{G}(\kappa,\xi)\). Plots are provided for each block size.

### Case 1.

Figures 9.3-9.4 display the ordered eigenvalues of _G(A<sub>n</sub>,B<sub>n</sub>_) (colored markers) together with the ordered samples of \(\widetilde{G}(\kappa,\xi)\) (solid red line).

_Example 1._ Because the supports of \(\kappa\) and \(\xi\) are essentially disjoint, \(\widetilde{G}(\kappa,\xi)\equiv 0\). Most of the eigenvalues match the zero line, showing convergence to the zero- distribution. Only a small number of positive outliers remain above the line. For small values of _n_, the eigenvalue plot appears to be governed by a GLT momentary symbol that, when rearranged, follows a power law that rapidly collapses to the zero function as \(n\rightarrow\infty\).

_Example 2._ Here, the supports of \(\kappa\) and \(\xi\) intersect on \(\theta\in[-0.25,0.25]\). As a result, \(\widetilde{G}(\kappa,\xi)\) takes two values: zero outside the overlap and a positive constant matrix<tbc>

