_Proof._ We have \((PA)_{ij}=\sum_{k=1}^N(P)_{ik}(A)_{kj}=(A)_{\sigma(i),j}\) and \((\hat{A}P)_{ij}=\sum_{k=1}^N(\hat{A})_{ik}(P)_{kj}=(\hat{A})_{i,\sigma^{-1}(j)}\), thus \((PA)_{ij}=(\hat{A}P)_{ij}\) holds for any \(1\le i,j\le N\).

**Lemma 3.5.** _Let_ M _be an_ \(mN\times mN\) _Hermitian block matrix partitioned into_ \(m\times m\) _blocks_ \(\mathcal{M}=(\mathbf{M}_{ij})_{1\le i,j\le m}\)_, each block_ **M**_<sub>ij</sub> is_ \(N\times N\) _diagonal and_ \(\mathbf{M}_{ji}=\mathbf{M}_{ij}^\dagger\)_. Then there holds:_

\(\lambda(\mathcal{M})=\bigcup_{k=1}^N\lambda(\hat{\mathbf{M}}_k),\text{\textit{where}}\hat{\mathbf{M}}_k\in\mathbb{C}^{m\times m},(\hat{\mathbf{M}}_k)_{ij}=(\mathbf{M}_{ij})_k.\) (3.9)

_Proof._ We introduce matrix \(\hat{\mathcal{M}}\) such that \((\hat{\mathcal{M}})_{ij}=(\mathcal{M})_{\sigma(i),\sigma(j)}\), where \(\sigma\) is a permutation over \(\{1,\cdots,mN\}\) defined by:<tbc>

\(\sigma(i)=(i-(k-1)m-1)N+k,(k-1)m+1\le i\le km,k=1,\cdots,N.\) (3.10)

<tbc>According to the diagonal condition, \((\mathcal{M})_{ij}\neq 0\) if and only if \(i\equiv jmodN\), thus \((\hat{\mathcal{M}})_{ij}\neq 0\) if and only if \(\sigma(i)\equiv\sigma(j)modN\), which means _i,j_ lay in the same interval \[(_k_-1)_m_+1_,km_\], which is equivalent to saying

\(\hat{\mathcal{M}}=\text{diag}(\hat{\mathbf{M}}_1,\cdots,\hat{\mathbf{M}}_N),\hat{\mathbf{M}}_k\in\mathbb{C}^{m\times m}.\) (3.11)

Meanwhile, \((\hat{\mathbf{M}}_k)_{ij}=(\hat{\mathcal{M}})_{(k-1)m+i,(k-1)m+j}=(\mathcal{M})_{(i-1)N+k,(j-1)N+k}=(\mathbf{M}_{ij})_k\), also \((\hat{\mathbf{M}}_k)_{ji}=(\mathbf{M}_{ji})_k=(\mathbf{M}_{ij}^\dagger)_k=(\hat{\mathbf{M}}_k)_{ij}^\dagger\), thus \(\hat{\mathbf{M}}_k\) is also Hermitian. Finally, according to Lemma 3.4, M shares exactly same eigenvalues with \(\hat{\mathcal{M}}\), thus the desired result holds.

**Proposition 3.6.** _The matrix_ M_<sub>Trivial</sub> defined by_ (3.4) _in Subsubsection 3.2.1 satisfies_<tbc>

\(\lambda_\text{min}(\mathcal{M}_{Trivial})\ge\lambda_\text{min}(\hat{\varepsilon}_1),\) (3.12)

<tbc>_where_<tbc>

\(\hat{\varepsilon}_1:=\left(\begin{array}{ c c c }
\hat{\varepsilon}_{11} & \varepsilon_{12} & \varepsilon_{13} \\
\varepsilon_{12}^* & \hat{\varepsilon}_{22} & \varepsilon_{23} \\
\varepsilon_{13}^* & \varepsilon_{23}^* & \hat{\varepsilon}_{33}
\end{array}\right),\hat{\varepsilon}_{ii}=\text{min}\{\varepsilon_{ii},1\}.\) (3.13)

<tbc>_Proof._ Due to Lemma 3.5, we have \(\lambda_\text{min}(\mathcal{M}_\text{Trivial})=\text{min}_{1\le k\le N}\lambda_\text{min}(\mathbf{M}_k)\), where

\(\mathbf{M}_k=\left(\begin{array}{ c c c }
(\varepsilon_{11}-1)(\mathcal{I}_1)_k+1 & \varepsilon_{12}(\mathcal{I}_\mathcal{V})_k & \varepsilon_{13}(\mathcal{I}_\mathcal{V})_k \\
\varepsilon_{12}^*(\mathcal{I}_\mathcal{V})_k & (\varepsilon_{22}-1)(\mathcal{I}_2)_k+1 & \varepsilon_{23}(\mathcal{I}_\mathcal{V})_k \\
\varepsilon_{13}^*(\mathcal{I}_\mathcal{V})_k & \varepsilon_{23}^*(\mathcal{I}_\mathcal{V})_k & (\varepsilon_{33}-1)(\mathcal{I}_3)_k+1
\end{array}\right).\) (3.14)

When (I<sub>V</sub>)_<sub>k</sub>_=0, **M**_<sub>k</sub>_ is diagonal with positive entries; when (I<sub>V</sub>)_<sub>k</sub>_=1, \(\mathbf{M}_k\ge\hat{\varepsilon}_1\). Therefore \(\lambda_\text{min}(\mathcal{M}_\text{Trivial})\ge\text{min}\{\lambda_\text{min}(\hat{\varepsilon}_1)\), \(\hat{\varepsilon}_{11}\), \(\hat{\varepsilon}_{22}\), \(\hat{\varepsilon}_{33}\}\). Moreover, \(\hat{\varepsilon}_{ii}=\mathbf{e}_i^\top\hat{\varepsilon}_1\mathbf{e}_i\ge\lambda_\text{min}(\hat{\varepsilon}_1)\) due to minimality of Rayleigh quotient, we have \(\lambda_\text{min}(\mathcal{M}_\text{Trivial})\ge\lambda_\text{min}(\hat{\varepsilon}_1)\).

Proposition 3.6 proves that Assumption 3.1 is sufficient for M<sub>Trivial</sub> to be HPD.

## _3.3.2. Positive Definiteness for Matrix_ M<sub>**_CrossDoF_**</sub>

We start by considering _S<sub>ij</sub>_’s matrix norms, which can help prove the HPD property under the SDD condition of Assumption 3.2.

**Proposition 3.7.** _The matrices_ \(\{S_{ij}\}_{1\le i<j\le 3}\) _defined in_ (3.8) _satisfies:_

\(\|S_{ij}\|_1\le 1,\|S_{ij}\|_2\le 1,\|S_{ij}\|_\infty\le 1.\) (3.15)

_Here,_ \(\|\cdot\|_1,\|\cdot\|_2,\|\cdot\|_\infty\) _refer to the matrix column sum, spectral norm and row sum, respectively._

