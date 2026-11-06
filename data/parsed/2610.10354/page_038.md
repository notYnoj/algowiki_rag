<tbc>prime in the range \([\hat{p},2\hat{p}]\). Then construct the cyclic sequences \(P,Q\in([0,u]\cup\{\perp\})^{\mathbb{Z}/p\mathbb{Z}}\) by

\(P[\hat{i}]=\left\{\begin{array}{ c c }
A_0[i] & \text{for some arbitrary}i\in[0,n]\text{anchored in}X_\ell\text{with}\hat{i}\equiv i\cdot 2n+A_1[i](\mathrm{mod}p), \\
\perp & \text{if such}i\text{does not exist,}
\end{array}\right.\)<br>
\(Q[\hat{j}]=\left\{\begin{array}{ c c }
B_0[j] & \text{for some arbitrary}j\in[0,n]\text{anchored in}Y_\ell\text{with}\hat{j}\equiv j\cdot 2n+B_1[j](\mathrm{mod}p), \\
\perp & \text{if such}j\text{does not exist.}
\end{array}\right.\)

We compute the cyclic min-plus convolution _P∗Q_; it is well-known that this reduces to _O_(1) non- cyclic instances. Moreover, we list some witness of \(\hat{i}\) for each output entry \((P*Q)[\hat{k}]\) by Lemma 2.14. For each such pair, letting \(\hat{j}=\hat{k}-\hat{i}\), we determine the indices _i_ and _j_ corresponding to \(\hat{i}\) and \(\hat{j}\) that were used in defining \(P[\hat{i}]\) and \(Q[\hat{j}]\) (via \(\hat{i}\equiv i\cdot 2n+A_1[i]\), and analogously for _j_) and update \(C[i+j]\leftarrow\mathrm{min}\{C[i+j],A[i]+B[j]\}\).

## Correctness.

Let us analyze the correctness of the light step. Our goal is to show that, for each light index _k_, we eventually correctly assign _C_\[_k_\]=(_A∗B_)\[_k_\]. Fix any such _k_, let _i_ be a witness of (_A∗B_)\[_k_\], and let _j=k-i_. Let _x_ be the anchor of _i_, and let _y_ be the anchor of _j_. Since _k_ is light, we know that _x_ is _A-light_ and that _y_ is _B-light_. Thus, \((x,L_A[x])\in\mathcal{A}\) and \((y,L_B[y])\in\mathcal{B}\). Let _z=x+y_. We claim that<tbc>

\(L_A[x]+L_B[y]<L_C[z]+2\Delta_Y.\) (8)

<tbc>Suppose otherwise, and let \(x'+y'=z\) be such that \(L_A[x']+L_B[y']=L_C[z]\), \(x'\in X\) is _A_-light, and \(y'\in X\) is _B_-light. Let \(i'=i-x+x'\) and note that \(i'\) is anchored at \(x'\). Similarly, let \(j'=j-y+y'\) and note that \(j'\) is anchored at \(y'\). Thus,

\(A[i']+B[j']\le U_A[x']+U_B[y']\)<br>
\(<L_A[x']+L_B[y']+2\Delta_Y\)<br>
\(=L_C[z]+2\Delta_Y\)<br>
\(\le L_A[x]+L_B[y]\)<br>
\(\le A[i]+B[j],\)

which, together with \(i'+j'=k\), contradicts the assumption that _i_ is a witness of (_A∗B_)\[_k_\]. Therefore, (8) holds and by definition, \((z,L_A[x]+L_B[y])\in\mathcal{C}\).

By Property (i) of Theorem 5.7 there are two possible cases: the pair ((_x,L<sub>A</sub>_\[_x_\]),(_y,L<sub>B</sub>_\[_y_\])) appears in the remainder R or in some set \(\mathcal{A}_\ell\times\mathcal{B}_\ell\). In the former case we directly enumerate the pair (_i,j_) in the algorithm and set _C_\[_k_\] as intended. So focus on the latter case. Focus on the \(\ell\)-th iteration, and let _p_ be a random prime as in the algorithm. Define

\(\hat{i}=(i\cdot 2n+A_1[i])\mathrm{mod}p,\)<br>
\(\hat{j}=(j\cdot 2n+B_1[j])\mathrm{mod}p,\)<br>
\(\hat{k}=(k\cdot 2n+A_1[i]+B_1[j])\mathrm{mod}p.\)

We now argue that three success events happen simultaneously with good probability.

First, \(P[\hat{i}]=A_0[i]\), unless there is a collision of the form \(i\cdot 2n+A_1[i]\equiv i'\cdot 2n+A_1[i'](\mathrm{mod}p)\). By the Prime Number Theorem, for any fixed \(i'\) (distinct from _i_) this collision takes place only<tbc>

