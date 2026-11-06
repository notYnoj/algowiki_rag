## 6 Constituent Stage

In the constituent stage for level-\(\ell\) for some \(\ell>1\), the input is an _s_-term level-\(\ell\varepsilon\)-interface tensor with parameters

\(\{(n_t,i_t,j_t,k_t,\beta_{X,t},\beta_{Y,t},\beta_{Z,t})\}_{t\in[s]}\)

that meet the following constraints:

1. For every \(t\in[s]\), if \(\hat{i}_1+\hat{i}_2+\cdots+\hat{i}_{2^{\ell-1}}\neq i_t\), then \(\beta_{X,t}(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^{\ell-1}})=0\). Similar constraints hold for \(\beta_{Y,t}\) and \(\beta_{Z,t}\).<tbc>

2. For every \(t\in[s]\) with _j<sub>t</sub>_=0, and every \(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^{\ell-1}}\),<tbc>

<tbc>\(\beta_{X,t}(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^{\ell-1}})=\beta_{Z,t}(2-\hat{i}_1,2-\hat{i}_2,\dots,2-\hat{i}_{2^{\ell-1}}).\)<tbc>

<tbc>Similar relations hold between \(\beta_{X,t}\) and \(\beta_{Y,t}\) where _k<sub>t</sub>_=0 and between \(\beta_{Y,t}\) and \(\beta_{Z,t}\) where _i<sub>t</sub>_=0.

Additionally, we let \(n=\sum_tn_t\) and \(N=2^{\ell-1}\cdot n\). The goal of this stage is to degenerate the input to the tensor product between a matrix multiplication tensor and multiple independent copies of a level-\((\ell-1)\varepsilon'\)-interface tensor for some \(\varepsilon'>0\).

Before we apply the laser method, let us handle the terms \(t\in[s]\) in the level-\(\ell\varepsilon\)-interface tensor where _i<sub>t</sub>_=0, _j<sub>t</sub>_=0 or _k<sub>t</sub>_=0, which are already matrix multiplication tensors. The proof idea of the following theorem is similar to the proof idea of a result in \[Vas12\], who showed the version of the following theorem without complete split distributions.

**Theorem 6.1.** _If k<sub>t</sub>_=0_, then_<tbc>

\(T_{i_t,j_t,k_t}^{\otimes n_t}[\beta_{X,t},\beta_{Y,t},\beta_{Z,t},\varepsilon]\equiv\langle 1,M,1\rangle,\)

<tbc>_where_

\(M=2^{n_t}(H(\beta_{X,t})\pm o_{1/\varepsilon}(1))\pm o(n)\cdot q^{n_t}\sum_{(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^{\ell-1}})}\beta_{X,t}(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^{\ell-1}})\sum_{p=1}^{2^{\ell-1}}[\hat{i}_p=1]}.\)

_Similar results hold when i<sub>t</sub>_=0 _or j<sub>t</sub>_=0.

_Proof._ As _k<sub>t</sub>_=0, there is only one _Z_-variable _z_<sub>0</sub> in the given tensor. Also, for each fixed _X_-variable _x_, there is a unique _Y_ -variable _y_ so that _xyz_<sub>0</sub> is a term in the given tensor (this is because it is a subtensor of \(\mathrm{CW}_q^{\otimes N}\)), and vice versa. Thus, the given tensor is isomorphic to an inner product tensor \(\langle 1,M,1\rangle\) for some \(M\ge 0\). It remains to calculate the number of _X_-variables in the given tensor. The _X_-variables are distributed among several level-1 _X_-blocks. Fixing a complete split distribution \(\xi_{X,t}\) whose \(L_\infty\) distance to \(\beta_{X,t}\) is within \(\varepsilon\), the number of level-1 _X_-blocks in \(T_{i_t,j_t,k_t}^{\otimes n_t}\) that conform with \(\xi_{X,t}\) is

\(2^{n_tH(\xi_{X,t})\pm o(n)}=2^{n_t}(H(\beta_{X,t})\pm o_{1/\varepsilon}(1))\pm o(n).\) (11)

In each of these level-1 blocks, say \(X_\hat{f}\), the number of _X_-variables is

\(q\sum_{p=1}^{n_t\cdot 2^{\ell-1}}[\hat{f}_p=1]=q^{n_t}\sum_{(\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})}\xi_{X,t}(\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\sum_{p=1}^{2^{\ell-1}}[\hat{i}_p=1]\)<br>
\(=q^{n_t}\sum_{(\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})}(\beta_{X,t}(\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\pm o_{1/\varepsilon}(1))\sum_{p=1}^{2^{\ell-1}}[\hat{i}_p=1]}.\) (12)

The product of (11) and (12) gives the number of _X_-variables belonging to level-1 _X_-blocks that are consistent with a certain \(\xi_{X,t}\); taking summation over all \(\xi_{X,t}\) (there are poly(_n_) of which) proves the lemma.

