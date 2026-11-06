### Restriction.

Restriction is a special type of degeneration that considers the case where the maps \(\phi_X,\phi_Y,\phi_Z\) are F-linear maps. More specifically, \(T'\) is a restriction of _T_ if there exist F-linear maps<tbc>

\(\phi_X:\text{span}_\mathbb{F}(X)\rightarrow\text{span}_\mathbb{F}(X'),\)<br>
\(\phi_Y:\text{span}_\mathbb{F}(Y)\rightarrow\text{span}_\mathbb{F}(Y'),\)<br>
\(\phi_Z:\text{span}_\mathbb{F}(Z)\rightarrow\text{span}_\mathbb{F}(Z'),\)

<tbc>such that

\(T'=\sum_{i=1}^{|X|}\sum_{j=1}^{|Y|}\sum_{k=1}^{|Z|}a_{i,j,k}\cdot\phi_X(x_i)\cdot\phi_Y(y_j)\cdot\phi_Z(z_k).\)

It is not hard to see that since the maps \(\phi_X,\phi_Y,\phi_Z\) are linear transformations, we have \(R(T')\le R(T)\) and consequently \(\widetilde{R}(T')\le\widetilde{R}(T)\).

### Zero-out.

In the laser method, we only consider a limited type of restriction called zero-outs, namely the maps \(\phi_X,\phi_Y,\phi_Z\) set some variables to zero. More specifically, we choose subsets \(X'\subseteq X\), \(Y'\subseteq Y\) , \(Z'\subseteq Z\) and define the maps as<tbc>

\(\phi_X(x_i)=\left\{\begin{array}{ c c }
x_i & \text{If}x_i\in X', \\
0 & \text{otherwise},
\end{array}\right.\)

<tbc>and similarly for \(\phi_Y,\phi_Z\). The resulting tensor

\(T'=\sum_{i=1}^{|X|}\sum_{j=1}^{|Y|}\sum_{k=1}^{|Z|}a_{i,j,k}\cdot\phi_X(x_i)\cdot\phi_Y(y_j)\cdot\phi_Z(z_k)=\sum_{x_i\in X^\prime}\sum_{y_j\in Y^\prime}\sum_{z_k\in Z^\prime} a_{i,j,k}\cdot x_iy_jz_k\)

is called a zero-out of _T_. Throughout this paper, we use the notation \(T'=T|_{X^\prime,Y^\prime,Z^\prime}\) to denote such a tensor \(T'\) obtained as a zero-out of _T_ and we say that the variables in \(X\backslash X'\), \(Y\backslash Y'\), \(Z\backslash Z'\) are zeroed out. In this case, we also call \(T'\) the _subtensor_ of _T_ over \(X',Y',Z'\).

## 3.4 Matrix Multiplication Tensors

For positive integers _a,b,c_, the \(a\times b\times c\) matrix multiplication tensor \(\langle a,b,c\rangle\) is a tensor over the variable sets \(\{x_{ij}\}_{i\in[a],j\in[b]},\{y_{jk}\}_{j\in[b],k\in[c]},\{z_{ki}\}_{i\in[a],k\in[c]}\) defined as the tensor computing the \(a\times c\) product matrix \(\{z_{ki}\}_{i\in[a],k\in[c]}\) of an \(a\times b\) matrix \(\{x_{ij}\}_{i\in[a],j\in[b]}\) and \(b\times c\) matrix \(\{y_{jk}\}_{j\in[b],k\in[c]}\). Specifically, \(\langle a,b,c\rangle\) can be written as the trilinear form

\(\langle a,b,c\rangle=\sum_{i\in[a]}\sum_{j\in[b]}\sum_{k\in[c]}x_{ij}y_{jk}z_{ki}.\)

It is not hard to check that \(\langle a,b,c\rangle\otimes\langle d,e,f\rangle\equiv\langle ad,be,cf\rangle\).

Following from the recursive approach introduced by Strassen in \[Str69\], for any integer \(q\ge 2\), if \(R(\langle q,q,q\rangle)\le r\), then one can use the rank decomposition of \(\langle q,q,q\rangle\) to design an arithmetic circuit of size _O(n_<sup>log<sub>_q_</sub>(_r_)</sup>) to multiply two \(n\times n\) matrices. This motivates the definition of the _matrix multiplication exponent_ \(\omega\) as follows:

\(\omega:=inf_{q\in\mathbb{N},q\ge 2}log_q(R(\langle q,q,q\rangle)).\)

