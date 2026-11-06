**Definition 1** (Tensor Contraction)**.** _For_ \(s,t,v\in\mathbb{Z}_{\ge 0}\)_, the contraction of tensors_ \(A\in(\mathbb{C}^n)^{\otimes(s+v)}\) _and_ \(B\in(\mathbb{C}^n)^{\otimes(v+t)}\) _into a tensor_ \(C\in(\mathbb{C}^n)^{\otimes(s+t)}\) _may be written as_<tbc>

\(C_\mathbf{ij}=\sum_{\mathbf{k}\in\unknown 0,n-1\unknown^v}A_{\mathbf{ik}}B_{\mathbf{kj}},\mathbf{i}\in\unknown 0,n-1\unknown^s,\mathbf{j}\in\unknown 0,n-1\unknown^t.\) (7)

<tbc>_The contraction is a bilinear map corresponding to the trilinear form,_

\(\mathcal{T}_n^{s,t,v}(X,Y,Z)=\sum_{\mathbf{i},\mathbf{j},\mathbf{k}}X_{\mathbf{ik}}Y_{\mathbf{kj}}Z_{\mathbf{ij}}.\) (8)

We use restriction notation to select coordinates of a multi-index.

**Definition 2** (Index restriction)**.** _Let_ \(S=\{j_0<\cdots<j_{k-1}\}\subseteq F\)_. For_ **i**=(_i_<sub>0</sub>_,...,i_<sub>_d_-1</sub>)_, define_

\(\mathbf{i}|_S=(i_{j_0},\dots,i_{j_{k-1}}).\) (9)

_The restriction to the empty set is the empty tuple._

The principal notation used in the constructions and their error analysis is summarized in  2.

## 3 Motivation: Symmetric Tensor Contractions

Our starting point is a family of fast bilinear algorithms for symmetric tensor contractions \[35\]. These algorithms reduce bilinear rank by forming a fully symmetrized trilinear aggregate over the index space of the contraction and extracting the desired terms from its partial sums. We use the same treatment of lower-order terms to construct trilinear aggregation algorithms for simultaneous matrix multiplication.

Consider a product between a symmetric matrix \(A\in\mathbb{C}^{n\times n}\) and a vector \(b\in\mathbb{C}^n\). The trilinear form corresponding to the matrix vector product _Ab_ is naively a sum of _n_<sup>2</sup> distinct terms, involving \(\genfrac(){pt}{2}{n+1}{2}\) variables _X<sub>ij</sub>_ with \(j\le i\), i.e.,

\(T_\mathrm{symv}(X,Y,Z)=\sum_{i=0}^{n-1}\big[X_{ii}Y_iZ_i+\big(\sum_{j=0}^{i-1}X_{ij}Y_iZ_j+\sum_{j=0}^{i-1}X_{ij}Y_jZ_i\big)\big].\) (10)

The symmetric matrix-vector tensor has rank at most \(\genfrac(){pt}{2}{n+1}{2}\),

\(T_\mathrm{symv}(X,Y,Z)=\sum_{i=0}^{n-1}\big[(X_{ii}-\sum_{j=0}^{i-1}X_{ij}-\sum_{j=i+1}^{n-1}X_{ji})Y_iZ_i+\sum_{j=0}^{i-1}X_{ij}(Y_i+Y_j)(Z_i+Z_j)\big].\) (11)

The sum over pairs (_i,j_) with _j\<i_ in this low-rank expansion corresponds to a ‘symmetrized’ form of the tensor contraction, i.e., _X<sub>ij</sub>(Y<sub>i</sub>+Y<sub>j</sub>_) is symmetric in (_i,j_), while _X<sub>ij</sub>Y<sub>i</sub>_ is not.

The symmetrization produces unwanted terms, all of which have lower order. More generally, consider a contraction of an order _s+v_ symmetric tensor with a _v+t_ symmetric tensor that is fully symmetrized (i.e., contract _A_ and _B_ to obtain a partially symmetric tensor in the first _s_ and the last _t_ indices, then sum over all permutations of _s+t_ indices into parts of _s_ and _t_ indices to obtain a fully symmetric tensor _C_ of order _s+t_). When _s=t=v_=1, this is _AB+BA_ with symmetric matrices _A_ and _B_. For fixed _s,t,v_, let _w=s+t+v_ and use _d=w_ in the coordinate and complement notation. The corresponding trilinear form is

\(\sum_{(U,V,W)\in B_{s,t,v}}\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^w}X_{\mathbf{i}|_{U^c}}Y_{\mathbf{i}|_{V^c}}Z_{\mathbf{i}|_{W^c}}\) (12)

\(B_{s,t,v}=\{(U,V,W)|U\sqcup V\sqcup W=\unknown 0,w-1\unknown,|U|=t,|V|=s,|W|=v\}.\) (13)

