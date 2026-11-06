_Proof._ It suffices to prove the same properties for **D**<sub>0</sub>. \(\|\mathbf{D}_0\|_1=\|\mathbf{D}_0\|_\infty=1\) is trivial due to (2.6). By Lemma (2.1), it is known that \(\|\mathbf{D}_0\|_2=1\). Therefore Kronecker 2-norm of products of \(\mathbf{D}_0,\mathbf{D}_0^\top\) and _I<sub>N</sub>_ also equals 1, which implies \(\|S_{ij}\|_2\le 1\). Next we verify that \(\|A\otimes B\|_\infty=\|A\|_\infty\|B\|_\infty\) for any matrix _A_, _B_. If this holds, then \(\|S_{ij}\|_\infty\le 1\) holds. Also \(\|A\otimes B\|_1=\|A^\top\otimes B^\top\|_\infty=\|A^\top\|_\infty\|B^\top\|_\infty=\|A\|_1\|B\|_1\), which implies \(\|S_{ij}\|_1\le 1\).

For simplicity we assume _A_=(_a<sub>ij</sub>_), \(B=(b_{st})\in\unknown^{N\times N}\). Since \((A\otimes B)_{I,J}=a_{ij}b_{st}\), where _I_=(_i_-1)_N+s,J_=(_j_-1)_N+t_, thus

\(\|A\otimes B\|_\infty=max_I\sum_J|(A\otimes B)_{I,J}|=max_{i,s}\sum_{j,t}^N|a_{ij}b_{st}|=max_i\sum_j|a_{ij}|max_s\sum_t|b_{st}|=\|A\|_\infty\|B\|_\infty,\)

where _I,J_ vary from 1 to _N_<sup>2</sup> and _i,j,s,t_ vary from 1 to _N_. The proof is completed.

**Proposition 3.8.** _If Assumptions 3.1 and 3.2 hold, then_ M<sub>_CrossDoF_</sub> _is SDD. Hence_ M<sub>_CrossDoF_</sub> _is HPD according to Gerschogrin’s theorem \[4, Theorem 7.2.1\]._

_Proof._ M<sub>CrossDoF</sub> being SDD is a straightforward result from \(\|S_{ij}\|_1,\|S_{ij}\|_\infty\le 1\) by shrinking the diagonal blocks M_<sub>ii</sub>_ to \(\epsilon_{ii}I_{N^3}\).

Next we prove a general conclusion in verifying positive-definiteness of Hermitian block matrix to verify the sufficiency of Assumption 3.3, as is illustrated in the following lemma.

**Lemma 3.9.** _We assume a set of m_<sup>2</sup> _matrices_ \(\{S_{ij}\}_{1\le i<j\le m}\)_, where_ \(S_{ij}\in\unknown^{N\times N}\)_, to satisfy: S<sub>ii</sub>=I<sub>N</sub> for_ \(i=1,\cdots,N\) _and_ \(S_{ji}=S_{ij}^\dagger\), \(\|S_{ij}\|_2\le 1\) _for_ \(1\le i<j\le N\)_. We define_ \(mN\times mN\) _block matrix_ M _with blocks_ \(\mathcal{M}:=\{\epsilon_{ij}S_{ij}\}_{1\le i,j\le m}\)_, where_ \((\epsilon_{ij})\) _forms an_ \(m\times m\) _HPD matrix. If_ \(\epsilon\) _is tridiagonal, then_ M _is HPD._

_Proof._ For any \(z_1,\cdots,z_m\in\unknown\), we denote \(z_i=a_iexp(\mathrm{i}\theta_i)\) with _a<sub>i</sub>_=|_z<sub>i</sub>_| and \(\theta_i=argz_i\). Then

\(0<(z_1^*,\cdots,z_m^*)\epsilon\left(\begin{array}{ c }
z_1 \\
\vdots \\
z_m
\end{array}\right)=\sum_{i=1}^m\epsilon_{ii}a_i^2+2\sum_{i=1}^{m-1}\Re(\epsilon_{i,i+1}z_i^*z_{i+1})=\sum_{i=1}^m\epsilon_{ii}a_i^2+2\sum_{i=1}^{m-1}|\epsilon_{i,i+1}|a_ia_{i+1}\mathrm{cos}\left(\theta_{i+1}-\theta_i+arg(\epsilon_{i,i+1})\right).\text{(3.16)}\)

By inductively setting \(\theta_1=0\) and \(\theta_{i+1}=\theta_i-arg(\epsilon_{i,i+1})+\pi\), we obtain

\(\sum_{i=1}^m\epsilon_{ii}a_i^2-2\sum_{i=1}^{m-1}|\epsilon_{i,i+1}|a_ia_{i+1}>0,\forall a_1,\cdots,a_m\ge 0,(a_1,\cdots,a_m)\neq\mathbf{0}.\) (3.17)

Then for any \(x_1,\cdots,x_m\in\unknown^N\), there holds

\((x_1^*,\cdots,x_m^*)\mathcal{M}\left(\begin{array}{ c }
x_1 \\
\vdots \\
x_m
\end{array}\right)=\sum_{i=1}^m\epsilon_{ii}\big\|x_i\big\|_2^2+2\sum_{i=1}^{m-1}\Re(\epsilon_{i,i+1}x_i^*S_{i,i+1}x_{i+1})\ge\sum_{i=1}^m\epsilon_{ii}\big\|x_i\big\|_2^2-2\sum_{i=1}^{m-1}|\epsilon_{i,i+1}|\big\|x_i\big\|_2\big\|x_{i+1}\big\|_2,\text{(3.18)}\)

where we apply the condition \(\|S_{ij}\|_2\le 1\). Thus (3.17) implies that right-hand side of (3.18) is nonnegative and equals zero if and only if all **_x_**_<sub>i</sub>_ vanish.

With the help of Lemma 3.9, the sufficiency of Assumption 3.3 is apparent.

**Proposition 3.10.** _When Assumptions 3.1 and 3.3 hold,_ M<sub>_CrossDoF_</sub> _defined by_ (3.8) _is HPD._

