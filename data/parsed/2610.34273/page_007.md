in the broader study of higher-order tensor spectra, and Alman and Li \[AL26\] systematically use spectral inequalities to obtain asymptotic-rank speedups from direct-sum degenerations. We next describe the constructions and the growth estimate that give Theorem 1.1.

**Simultaneous separation of shared legs.** The first component is a higher-order version of the finite separation construction in \[Ope26a\]. Let \(n\ge 3\) and \(M\ge 1\) be integers. In fixed coordinates, form _A_ by placing tensors _A_<sub>0</sub>_,...,A_<sub>_M_-1</sub> in matched, pairwise disjoint sectors on its last two legs, while sharing their first _n_-2 legs. Theorem 3.1 constructs a degeneration

\(A^{\oplus_K((2n-1)M)}\unknown\oplus_Kh_{=0}^{M-1}(A_h\otimes_KE_{n-1,n}^{(M)}).\)

The edge tensor \(E_{n-1,n}^{(M)}\) is an _M_-dimensional identity tensor on the last two legs and a scalar on every other leg, as in Definition 2.20. The relation \(\unknown\) is a degeneration in the sense of Definition 2.15. On the right, the sectors are independent on all _n_ legs.

The construction assigns each shared leg a tentative sector label \(g_j\in\{0,\dots,M-1\}\) for \(1\le j\le n-2\). A Fourier projection retains precisely the terms satisfying

\(u-v+2\sum_{j=1}^{n-2}(g_j-h)=0,\)

where \(h,u,v\in\{0,\dots,M-1\}\). Local weights make the total degree of every surviving term equal to \(\sum_{j=1}^{n-2}(g_j-h)^2\). Degree zero therefore forces _g<sub>j</sub>=h_ for every shared leg and _u=v_. These are exactly the conditions needed for the direct sum and its additional identity tensor. Only linearly many source copies are used, although the tentative labels are assigned independently.

To describe the consequence, let \(\phi\in\Phi_n\) be a spectral point (Definition 2.18). For each pair \(1\le i<j\le n\), define the _spectral edge weight_ \(p_{i,j}^{(\phi)}=\mathrm{log}_2\phi(E_{i,j}^{(2)})\). This number measures the value that \(\phi\) assigns to a resource shared only by legs _i_ and _j_. Lemma 4.4 proves \(\phi(E_{i,j}^{(q)})=q^{p_{i,j}^{(\phi)}}\) for every positive integer _q_. If every block _A<sub>h</sub>_ is nonzero, applying separation to words of a fixed type gives

\(\phi(A)\ge\mathrm{exp}\big(p_{n-1,n}^{(\phi)}H(\theta)\big)\prod_{h=0}^{M-1}\phi(A_h)^{\theta_h}\)

for every probability vector \(\theta=(\theta_0,\dots,\theta_{M-1})\); see Corollary 3.2. Here \(H(\theta)=-\sum_{h=0}^{M-1}\theta_h\mathrm{ln}\theta_h\), with 0ln0=0.

**A low-rank tensor with many input directions.** Following the use of polynomial multiplication in OpenAI \[Ope26a, Section 4\], we retain a separate tensor leg for every input. For positive integers _a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>, put \(D=1+\sum_{j=1}^{n-1}(a_j-1)\). The polynomial multiplication tensor from Definition 4.1 is<tbc>

\(\mathcal{C}_n(a_1,\dots,a_{n-1})=\sum_{0\le i_j<a_j1\le j\le n-1}e_{i_1}^{(a_1)}\otimes_C\cdots\otimes_Ce_{i_{n-1}}^{(a_{n-1})}\otimes_Ce_{i_1+\cdots+i_{n-1}}^{(D)}.\)

<tbc>Evaluation and interpolation show that its rank is exactly _D_. Thus, when every input length equals _a_, the rank is _O<sub>n</sub>(a_) despite the _n_-1 independent inputs. For a spectral point \(\phi\in\Phi_n\), define its average edge weight and its symmetric profile by<tbc>

\(t_\phi=\frac{1}{\genfrac(){pt}{2}{n}{2}}\sum_{1\le i<j\le n}p_{i,j}^{(\phi)},P_\phi(\mathbf{a})=\left(\prod_{\pi\in S_n}\phi\big(\pi\mathcal{C}_n(\mathbf{a})\big)\right)^{1/(n!t_\phi)},\)

