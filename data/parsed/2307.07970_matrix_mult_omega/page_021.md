### 3.11 Salem-Spencer Sets

In the hashing step of the laser method, we make use of the existence of a large dense subset of Z_<sub>M</sub>_ that avoids 3-term arithmetic progressions. We recall the following past result.

**Theorem 3.7** (\[SS42, Beh46\])**.** _For every positive integer M\>_0_, there exists a subset_ \(B\subseteq\mathbb{Z}_M\) _of size_

\(|B|\ge M\cdot e^{-O(\sqrt{\mathrm{log}M})}=M^{1-o(1)}\)

_that contains no nontrivial_ 3_-term arithmetic progressions. Specifically, any_ \(a,b,c\in B\) _satisfy_ \(a+b\equiv 2c(\mathrm{mod}M)\) _if and only if a=b=c._

## 4 Algorithm Outline

In the following, we will use \(\kappa\ge 0\) to denote that we want to obtain an upper bound on \(\omega(1,\kappa,1)\).

In this section, we give the outline of our algorithm, which accepts \(\mathrm{CW}_q^{\otimes N}\) as its input for a large enough _N_, and degenerates it into a collection of independent matrix multiplication tensors of the same size \(\langle m,m^\kappa,m\rangle\). By the asymptotic sum inequality (Theorem 3.2), this will give an upper bound on \(\omega(1,\kappa,1)\).

### 4.1 Algorithm Framework

The following notion of _interface tensor_ acts as an interface of our algorithm between different levels. In general, each level of our algorithm takes an interface tensor as input (except the first level, which takes a large tensor power of CW_<sub>q</sub>_), and degenerates it into independent copies of an interface tensor.

**Definition 4.1** (Interface Tensor)**.** For a positive integer \(\ell\ge 1\) and any constant \(0\le\varepsilon\le 1\), a level-\(\ell\varepsilon\)_-interface tensor_ T<sup>∗</sup> with parameter list<tbc>

\(\{(n_t,i_t,j_t,k_t,\beta_{X,t},\beta_{Y,t},\beta_{Z,t})\}_{t\in[s]}\)

<tbc>is defined as

\(\mathcal{T}^*:=\otimes_{t=1}^sT_{i_t,j_t,k_t}^{\otimes n_t}[\beta_{X,t},\beta_{Y,t},\beta_{Z,t},\varepsilon],\)

where \(i_t+j_t+k_t=2^\ell\) for every \(t\in[s]\) (i.e., _T<sub>i<sub>t</sub>,j<sub>t</sub>,k<sub>t</sub></sub>_ is a level-\(\ell\) constituent tensor) and \(\beta_{X,t},\beta_{Y,t},\beta_{Z,t}\) are level-\(\ell\) complete split distributions for _X_-, _Y_ -, _Z_-variables respectively. We call each \(T_{i_t,j_t,k_t}^{\otimes n_t}[\beta_{X,t},\beta_{Y,t},\beta_{Z,t},\varepsilon]\) a _term_ of T<sup>∗</sup>. When \(\varepsilon=0\), we will simply call T<sup>∗</sup> a level-\(\ell\) interface tensor.

Note that the same (_i<sub>t</sub>,j<sub>t</sub>,k<sub>t</sub>_) can appear multiple times in the parameter list, with potentially different \(n_k,\beta_{X,t},\beta_{Y,t},\beta_{Z,t}\). Also note that the tensor product of two level-\(\ell\varepsilon\)-interface tensors is also a level-\(\ell\varepsilon\)- interface tensor, whose parameter list is the concatenation of the parameter lists of the two level-\(\ell\varepsilon\)-interface tensors.

The framework of our algorithm is as follows. First, we apply the _global stage_ algorithm described in Section 5 on input \(\left(\mathrm{CW}_q^{\otimes 2^{\ell^*}}\right)^{\otimes n}\) to degenerate it into independent copies of a level-\(\ell^*\varepsilon_{\ell^*}\)-interface tensor. Then we apply the _constituent tensor stage_ algorithm described in Section 6 for \(\ell=\ell^*,\ell^*-1,\dots,2\) to obtain the tensor product between a matrix multiplication tensor and independent copies of a level-\(1\varepsilon_1\)-interface tensor. More specifically, the constituent tensor stage algorithm takes as input a level-\(\ell\varepsilon_\ell\)-interface tensor and outputs the tensor product between a matrix multiplication tensor and independent copies of a level-\((\ell-1)\)<tbc>

