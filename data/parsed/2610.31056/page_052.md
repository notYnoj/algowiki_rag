Therefore, L_<sub>i</sub>_ contains _m_ linearly independent vectors, each of norm at most \(\lambda_n(\mathcal{L})\), because orthogonal projection cannot increase Euclidean norm. It follows that \(\lambda_m(\mathcal{L}_i)\le\lambda_n(\mathcal{L})\). Hence

\(\|\mathbf{b}_i^*\|_2=\|\mathbf{y}_i\|_2\le\gamma(m)\lambda_m(\mathcal{L}_i)\le\gamma(n)\lambda_n(\mathcal{L}),\)

where we used the monotonicity of \(\gamma\).

From this point onward, the remainder of the proof is the same: the size-reduction step gives \(|\mu_{i,j}|\le 1/2\), and therefore

\(\|\mathbf{b}_i\|_2^2=\|\mathbf{b}_i^*\|_2^2+\sum_{j=1}^{i-1}\mu_{i,j}^2\|\mathbf{b}_j^*\|_2^2\le n\gamma(n)^2\lambda_n(\mathcal{L})^2,\)

which implies

\(\|\mathbf{b}_i\|_2\le\sqrt{n}\gamma(n)\lambda_n(\mathcal{L}).\)

## C Statistical Distance

**Lemma C.0.1.** _Let D_<sub>0</sub> _and D_<sub>1</sub> _be two distributions on the same sample space such that_ \(\Delta(D_0,D_1)\le\epsilon\)_. Consider the following two distributions on n-tuples._

• \(P:=D_0\times D_0\times\cdots\times D_0=D_0^n\).<tbc>

• _Q: sample independent uniform bits_ \(b_1,\dots,b_n\in\{0,1\}\)_, and then output an n-tuple whose i-th coordinate is sampled independently from D<sub>b<sub>i</sub></sub>._

_Then_ \(\Delta(P,Q)\le n\epsilon/2\).

_Proof._ We define hybrid distributions _H_<sub>0</sub>_,H_<sub>1</sub>_,...,H<sub>n</sub>_ by \(H_k:=D_1^k\times D_0^{n-k}\), for _k_=0,1_,...,n_. In particular, \(H_0=D_0^n=P\) and \(H_n=D_1^n\). However, the distribution _Q_ is not equal to _H<sub>n</sub>_. Instead, it is the product distribution<tbc>

\(Q=\left(\frac{D_0+D_1}{2}\right)^n,\)

<tbc>since each coordinate is sampled independently from _D_<sub>0</sub> or _D_<sub>1</sub> with equal probability. We now prove the desired bound by changing one coordinate at a time. Define<tbc>

\(G_k:=\left(\frac{D_0+D_1}{2}\right)^k\times D_0^{n-k},\)

<tbc>for _k_=0,1_,...,n_. Then _G_<sub>0</sub>=_P_ and \(G_n=\left(\frac{D_0+D_1}{2}\right)^n=Q\). By the triangle inequality,<tbc>

\(\Delta(P,Q)=\Delta(G_0,G_n)\le\sum_{k=0}^{n-1}\Delta(G_k,G_{k+1}).\)

<tbc>Now _G<sub>k</sub>_ and _G_<sub>_k_+1</sub> differ only in the (_k_+1)-st coordinate, so<tbc>

\(\Delta(G_k,G_{k+1})=\Delta\left(D_0,\frac{D_0+D_1}{2}\right).\)

