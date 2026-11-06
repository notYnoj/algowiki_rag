## A.8 Differentiating the Matrix Square Root

We consider the (differentiable) matrix square root function:

\(R:=\left\{\begin{array}{ c c }
S_d^{++}(\mathbb{R}) & \longrightarrow S_d^{++}(\mathbb{R}) \\
A & \longmapsto\sqrt{A}
\end{array}\right.,\)

and provide a formula for its differential which is useful for numerical automatic differentiation.

**Proposition A.3.** Let \(A\in S_d^{++}(\mathbb{R})\) and \(H\in S_d(\mathbb{R})\). Then the differential of the matrix square root at _A_ in the direction _H_ is given by the following matrix in _S<sub>d</sub>_(R):<br>
\(\mathrm{d}_AR(H)=PGP^\top,[G]_{i,j}:=\frac{[P^\top HP]_{i,j}}{\sqrt{\lambda_i}+\sqrt{\lambda_j}},\)<br>
where the orthonormal decomposition of _A_ is given by \(A=P\mathrm{diag}(\lambda_1,\cdots,\lambda_d)P^\top\).

_Proof._ For any \(A\in S_d^{++}(\mathbb{R})\), we have by definition _R(A)R(A_)=_A_, and differentiating this identity at _A_ in the direction _H_ yields that d_<sub>A</sub>R(H_) is a solution of the following Sylvester equation:<tbc>

\(R(A)X+XR(A)=H.\) (81)

<tbc>By \[Bha13, Theorem VII.2.1\], Eq. (81) has a unique solution in \(\mathbb{R}^{d\times d}\), which is therefore d_<sub>A</sub>R(H_). Using the notation of the result statement, we consider the symmetric matrix \(X:=PGP^\top\) and notice that by definition of _G_, we have:

\(\forall i,j\in\unknown 1,d\unknown,\sqrt{\lambda_i}G_{i,j}+G_{i,j}\sqrt{\lambda_j}=[P^\top HP]_{i,j},\)

introducing \(D:=\mathrm{diag}(\lambda_1,\cdots,\lambda_d)\), we deduce that \(R(D)G+GR(D)=P^\top HP\) and then that _X_ is indeed a solution of Eq. (81), hence by uniqueness _X_=d_<sub>A</sub>R(H_).

Below, we provide a PyTorch \[Pas+19\] implementation of this gradient computation, allowing for automatic gradient propagation.

`import torch`

`class MatrixSquareRoot(torch.autograd.Function):`

`@staticmethod`

`def forward(ctx, A):`

`A\_sym = .5 \* (A + A.transpose(-2, -1))`

`L, P = torch.linalg.eigh(A\_sym)`

`S = L.clamp\_min(0).sqrt()`

`R = (P \* S.unsqueeze(-2)) @ P.transpose(-2,-1)`

`ctx.save\_for\_backward(P, S)`









(a) Source image

(b) Fixed to target weights

(c) Fixed uniform weights

(d) Target image

Figure 19: Impact of the treatment of source weights in colour transfer.

