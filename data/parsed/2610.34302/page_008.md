Input: metric (P,d), parameter \(\alpha\ge 1\)<br>
Output: navigable graph G=(P,E)<br>
\(\delta\leftarrow 1/\alpha\), \(L\leftarrow\left\lceil\mathrm{log}_{1+\delta}\Delta\right\rceil\)<br>
Define \(r_i=(1+\delta)^i\) for every \(0\le i\le L+1\)<br>
foreach \(0\le i\le L\) do<br>
   \(\rho_i\leftarrow r_i/(\alpha+2)\)<br>
   \(\mathcal{N}_i\leftarrow\mathrm{SeparatedBallCover}(P,\mathsf{d},\rho_i)\)<br>
foreach \(s\in P\) do<br>
   \(E_s\leftarrow\emptyset\)<br>
   foreach \(0\le i\le L\) do<br>
   Compute \(A_i(s)\leftarrow\{v\in P:r_i-\rho_i<\mathsf{d}(s,v)\le r_{i+1}+\rho_i\}\)<br>
   \(E_s^i\leftarrow\{(s,p)|(C,p)\in\mathcal{N}_i,p\in A_i(s)\}\)<br>
   \(E_s\leftarrow E_s\cup E_s^i\)<br>
return \((P,\bigcup_{s\in P}E_s)\)

Input: metric (P,d), parameter \(\alpha\ge 1\)<br>
Output: navigable graph G=(P,E)<br>
\(\delta\leftarrow 1/\alpha\), \(L\leftarrow\left\lceil\mathrm{log}_{1+\delta}\Delta\right\rceil\)<br>
Define \(r_i=(1+\delta)^i\) for every \(0\le i\le L+1\)<br>
foreach \(0\le i\le L\) do<br>
   \(\rho_i\leftarrow r_i/(\alpha+2)\)<br>
   \(\mathcal{G}_i\leftarrow\mathrm{GreedyBallCover}(P,\mathsf{d},\rho_i)\)<br>
foreach \(s\in P\) do<br>
   \(E_s\leftarrow\emptyset\)<br>
   foreach \(0\le i\le L\) do<br>
   Compute \(A_i(s)\leftarrow\{v\in P:r_i-\rho_i<\mathsf{d}(s,v)\le r_{i+1}+\rho_i\}\)<br>
   \(E_s^i\leftarrow\{(s,p)|(C,p)\in\mathcal{G}_i,p\in A_i(s)\}\)<br>
   \(E_s\leftarrow E_s\cup E_s^i\)<br>
return \((P,\bigcup_{s\in P}E_s)\)

takes O(n<sup>2</sup>L) time and also bounds the output size. Thus both Algorithm 2.3 and Algorithm 2.4 run in \(\tilde{O}(\alpha n^2\mathrm{log}\Delta)\) time, which is \(\tilde{O}(n^2\mathrm{log}\Delta)\) for constant \(\alpha\).

## 2.3 Proof of Correctness.

**Lemma 2.1** (Ball Coverage)**.** _Let_ (P,d) _be a metric space and let_ \(\alpha\ge 1\)_. For any_ \(u,c,v\in P\)_, if_<tbc>

\(\mathsf{d}(c,v)<\frac{\mathsf{d}(c,u)}{\alpha+1},\)

<tbc>_then the directed edge_ (u,c) _is an_ \(\alpha\)_-navigation from u to v, i.e.,_

\(\mathsf{d}(c,v)<\frac{\mathsf{d}(u,v)}{\alpha}.\)

**Algorithm 2.3:** ConstantApproxNavigable\(\mathrm{Graph}(P,\mathsf{d},\alpha)\)

**Algorithm 2.4:** LogApproxNavigable\(\mathrm{Graph}(P,\mathsf{d},\alpha)\)

