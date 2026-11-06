## 3 Preliminaries

### 3.1 Tensors and Tensor Operations

#### Tensors.

A tensor _T_ over variable sets _X_={_x_<sub>1</sub>_,...,x_<sub>|_X_|</sub>}, _Y_={_y_<sub>1</sub>_,...,y_<sub>|_Y_|</sub>}, _Z_={_z_<sub>1</sub>_,...,z_<sub>|_Z_|</sub>} and field F is a trilinear form

\(T=\sum_{i=1}^{|X|}\sum_{j=1}^{|Y|}\sum_{k=1}^{|Z|}a_{i,j,k}\cdot x_iy_jz_k,\)

where all _a<sub>i,j,k</sub>_ are from F. _X,Y,Z_ are also called the _support_ of the tensor. If all \(a_{i,j,k}\in\{0,1\}\), the tensor _T_ can be considered as over any field F, which is the case for all tensors involved in this paper.

In the following, assume _T_ is a tensor over _X_={_x_<sub>1</sub>_,...,x_<sub>|_X_|</sub>}, _Y_={_y_<sub>1</sub>_,...,y_<sub>|_Y_|</sub>}, _Z_={_z_<sub>1</sub>_,...,z_<sub>|_Z_|</sub>} and \(T'\) is a tensor over \(X'=\{x'_1,\dots,x'_{|X^\prime|}\}\), \(Y'=\{y'_1,\dots,y'_{|Y^\prime|}\}\), \(Z'=\{z'_1,\dots,z'_{|Z^\prime|}\}\), written as

\(T=\sum_{i=1}^{|X|}\sum_{j=1}^{|Y|}\sum_{k=1}^{|Z|}a_{i,j,k}\cdot x_iy_jz_k,T'=\sum_{i=1}^{|X^\prime|}\sum_{j=1}^{|Y^\prime|}\sum_{k=1}^{|Z^\prime|}b_{i,j,k}\cdot x'_iy'_jz'_k,\)

#### Tensor Operations.

Recall the following tensor operations between two tensors _T_ and \(T'\):

• The _sum_ \(T+T'\) is only defined when both tensors are supported on the same sets \((X,Y,Z)=(X',Y',Z')\), given by<tbc>

<tbc>\(T+T'=\sum_{i=1}^{|X|}\sum_{j=1}^{|Y|}\sum_{k=1}^{|Z|}(a_{i,j,k}+b_{i,j,k})\cdot x_iy_jz_k.\)<tbc>

• The _direct sum_ \(T\oplus T'\) equals the sum \(T+T'\) over disjoint unions \(X\sqcup X'\), \(Y\sqcup Y'\), and \(Z\sqcup Z'\), i.e., we first relabel the variables so that _T_ and \(T'\) have disjoint supports, and then take their sum. If _T_ and \(T'\) are supported on disjoint variable sets, their sum is the same as their direct sum, in which case we say _T_ and \(T'\) are _independent_. We write \(T^{\oplus n}:=\underbrace{T\oplus T\oplus\cdots\oplus T}_{n\text{copies}}\) to denote the sum of _n_ independent copies of _T_.<tbc>

• The _tensor product_, a.k.a. the _Kronecker product_, is defined as the tensor<tbc>

<tbc>\(T\otimes T'=\sum_{i=1}^{|X|}\sum_{j=1}^{|Y|}\sum_{k=1}^{|Z|}\sum_{i^\prime=1}^{|X^\prime|}\sum_{j^\prime=1}^{|Y^\prime|}\sum_{k^\prime=1}^{|Z^\prime|}a_{i,j,k}\cdot b_{i^\prime,j^\prime,k^\prime}\cdot(x_i,x'_{i^\prime})\cdot(y_j,y'_{j^\prime})\cdot(z_k,z'_{k^\prime})\)<tbc>

<tbc>over variable sets \(X\times X'\), \(Y\times Y'\), and \(Z\times Z'\). We write \(T^{\otimes n}:=\underbrace{T\otimes T\otimes\cdots\otimes T}_{n\text{times}}\) to denote the _n-th tensor power_ of _T_.<tbc>

• We say _T_ and \(T'\) are _isomorphic_, denoted by \(T\equiv T'\), if \(|X|=|X'|\), \(|Y|=|Y'|\), \(|Z|=|Z'|\), and there are permutations \(\pi_X,\pi_Y,\pi_Z\) over \([|X|],[|Y|],[|Z|]\) respectively, such that \(a_{i,j,k}=b_{\pi_X(i),\pi_Y(j),\pi_Z(k)}\) for all _i,j,k_. In other words, both tensors are equivalent up to a relabeling of the variables.<tbc>

