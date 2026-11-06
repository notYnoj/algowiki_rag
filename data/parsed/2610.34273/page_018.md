let _N_ be a positive integer. Its _N_-th Kronecker power has degree at most _bN_, and its coefficient of \(\varepsilon^{aN}\) is \(S^{\otimes_KN}\). Evaluate this polynomial at _bN_+1 distinct complex numbers _z_<sub>0</sub>_,...,z<sub>bN</sub>_. Inverting the Vandermonde matrix gives complex numbers _c_<sub>0</sub>_,...,c<sub>bN</sub>_ such that

\(S^{\otimes_KN}=\sum_{r=0}^{bN}c_r\big(L(z_r)\cdot T\big)^{\otimes_KN}.\)

Take _bN_+1 direct-sum copies of \(T^{\otimes_KN}\). On copy _r_, for \(0\le r\le bN\), use the local maps that give \((L(z_r)\cdot T)^{\otimes_KN}\), and multiply the first local map by _c<sub>r</sub>_. Concatenate these maps on each leg. Their image is the displayed coefficientwise sum, including when an evaluation or a coefficient _c<sub>r</sub>_ vanishes. Therefore

\(S^{\otimes_KN}\unknown(T^{\otimes_KN})^{\oplus_K(bN+1)}\sim T^{\otimes_KN}\otimes_K\mathsf{I}_k(bN+1).\)

Taking _h<sub>N</sub>=bN_+1 gives log_h<sub>N</sub>=o(N_), as required.

**Definition 2.18** (asymptotic spectrum)**.** For every integer \(k\ge 2\), the _asymptotic spectrum of complex k-th order tensors_, denoted \(\Phi_k\), is the set of maps \(\phi:\mathsf{Tens}_k(\mathbb{C})\rightarrow\mathbb{R}_{\ge 0}\) such that

\(\phi(0)=0,\phi(\mathsf{I}_k(1))=1,\)<br>
\(\phi(A\oplus_KB)=\phi(A)+\phi(B),\phi(A\otimes_KB)=\phi(A)\phi(B)\)

for all \(A,B\in\mathsf{Tens}_k(\mathbb{C})\), and \(A\unknown B\) implies \(\phi(A)\le\phi(B)\). An element of \(\Phi_k\) is called a _spectral point_.

For every \(\phi\in\Phi_k\) and every positive integer _q_, additivity gives \(\phi(\mathsf{I}_k(q))=q\). Thus \(1\le\phi(T)\le\mathsf{R}(T)\) for every nonzero _T_. Spectral points are also monotone under asymptotic restriction. Indeed, \(S\lesssim T\) gives \(\phi(S)^N\le h_N\phi(T)^N\) for all sufficiently large _N_; taking _N_-th roots and using \(h_N^{1/N}\rightarrow 1\) gives \(\phi(S)\le\phi(T)\). In particular, Lemma 2.17 shows that spectral points are monotone under degeneration. The following theorem supplies the converse and the characterization of asymptotic rank used in Subsection 4.5.

**Theorem 2.19** (Strassen’s spectral duality \[Str88, CVZ23, WZ26\])**.** _For every integer_ \(k\ge 2\) _and every complex k-th order tensor T,_

\(\widetilde{\mathsf{R}}(T)=\mathrm{max}_{\phi\in\Phi_k}\phi(T).\)

_Moreover, for complex k-th order tensors S,T, we have_ \(S\lesssim T\) _if and only if_ \(\phi(S)\le\phi(T)\) _for every_ \(\phi\in\Phi_k\).

## 2.3 Graph tensors and cuts

We next define graph tensors, including the coordinate grouping at each vertex. Their edge decomposition connects them to the spectral inequalities, while graph cuts provide the lower bounds. Throughout the paper, the vertex set of a graph with _k_ vertices is identified with {1_,...,k_}. An undirected edge is written (_i,j_) with _i\<j_; this notation records its endpoints and does not orient the edge.

**Definition 2.20** (edge tensors and graph tensors)**.** Let \(k\ge 2\) and \(q\ge 1\) be integers. For \(1\le i<j\le k\), define the _k_-th order _edge tensor_<tbc>

\(E_{i,j}^{(q)}=\sum_{a=0}^{q-1}\otimes_{d=1}^kv_{d,a},v_{d,a}=\left\{\begin{array}{ c c }
e_a^{(q)}, & d=i\text{or}d=j, \\
e_0^{(1)}, & d\notin\{i,j\},
\end{array}\right.\)

