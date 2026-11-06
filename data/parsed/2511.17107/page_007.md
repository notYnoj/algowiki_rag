_Proof._ A direct computation of A<sup>†</sup>+B<sup>†</sup>B yields a block diagonal matrix, provided that \(\mathcal{D}_i^\dagger\mathcal{D}_j=\mathcal{D}_j\mathcal{D}_i^\dagger\) for \(i\neq j\). This commutativity is guaranteed by the mixed product property of Kronecker products (2.15). The identity \(\mathcal{D}_i^\dagger\mathcal{D}_i=\mathcal{D}_i\mathcal{D}_i^\dagger\) holds because **K**_<sub>i</sub>_:=**D**<sub>1</sub>+i**k**_<sub>i</sub>_**D**<sub>0</sub> is a circulant matrix and thus normal, so is each block _D<sub>i</sub>_; We establish (2.19).

To prove (2), since B<sup>†</sup>B shares the same nonzero eigenvalues with L=BB<sup>†</sup>, we analyze the spectrum of L. The matrix \(\mathbf{K}_i^\dagger\mathbf{K}_i\) is circulant, and by setting \(c_i=\frac{1}{h}+\mathrm{i}^{\mathrm{k}_i}\frac{\mathrm{k}_i}{2}\) , its first row is<tbc>

\((2|c_i|^2,-c_i^2,0,\cdots,0,-\overline{c_i^2}).\)

<tbc>Applying Lemma 2.1, its eigenvalues are

\(\mu_j^{(i)}:=\lambda_j(\mathbf{K}_i^\dagger\mathbf{K}_i)=2\left(|c_i|^2-\Re(c_i^2\omega^j)\right)=\left(\frac{2}{h^2}+\frac{\mathrm{k}_i^2}{2}\right)\left(1-\mathrm{cos}(\phi_i+2j\pi h)\right),\) (2.21)

for \(j=1,\cdots N\) and \(\mathrm{tan}\phi_i=\frac{4\mathrm{k}_ih}{4-\mathrm{k}_i^2h^2}\) . The spectrum of \(\mathcal{L}=I_{N^2}\otimes(\mathbf{K}_1^\dagger\mathbf{K}_1)+I_N\otimes(\mathbf{K}_2^\dagger\mathbf{K}_2)\otimes I_N+(\mathbf{K}_3^\dagger\mathbf{K}_3)\otimes I_{N^2}\) is then presented by

\(\left\{\mu_{j_1}^{(1)}+\mu_{j_2}^{(2)}+\mu_{j_3}^{(3)}:1\le j_1,j_2,j_3\le N\right\}.\) (2.22)

We then aim to find the minimum of \(\mu_j^{(i)}\), which is \(\mathrm{min}\{\mu_{N-1}^{(i)},\mu_N^{(i)}\}\). We define \(f(x)=\mathrm{arctan}\left(\frac{4x}{4-x^2}\right)\), where _x_=k_<sub>i</sub>h_ is such that |_x|\<_1 due to the condition (2.20). By the mean value theorem, \(|f(x)|=|f(x)-f(0)|=|f'(c)x|\) for some _c_ strictly between 0 and _x_. Since \(f'(c)=\frac{4}{4+c^2}\in(0,1)\), we have \(|\phi_i|=|f(x)|<|x|=|\mathrm{k}_ih|\). Thus \(|\phi_i|<\pi h\) and

\(\mathrm{min}_{1\le j\le N}\mu_j^{(i)}=\left(\frac{2}{h^2}+\frac{\mathrm{k}_i^2}{2}\right)\left(1-\mathrm{max}\{\mathrm{cos}(\phi_i),\mathrm{cos}(2\pi h-\phi_i)\}\right)=\mathrm{k}_i^2.\) (2.23)

Here we substitute \(\mathrm{cos}(\phi_i)=\frac{4-\mathrm{k}_i^2h^2}{4+\mathrm{k}_i^2h^2}\) derived from its tangent value into the above computation. Finally, due to (2.22), the minimum eigenvalue of L is \(\left\|\mathbf{k}\right\|_2^2\), and thus \(\lambda_1^B=\left\|\mathbf{k}\right\|_2^2\).

**Proposition 2.5.** _For the kernel compensation formulation_ (2.13) _with coordinate change_ **A**=_I_<sub>3</sub>_, the null space_ H _and the choice of the penalty coefficient_ \(\gamma\) _are determined as follows:_

_(1). The null space_ H _is defined by: If_ **k**=**0**_, then_

\(\mathcal{H}=\mathrm{span}\{o_i\}_{i=1}^3,o_i\in\mathbb{R}^{3N^3},(o_i)_j=\left\{\begin{array}{ c c }
1, & \text{\textit{if}}(i-1)N^3+1\le j\le iN^3, \\
0, & \text{\textit{otherwise.}}
\end{array}\right.\) (2.24)

_If_ \(\mathbf{k}\neq\mathbf{0}\) _and condition_ (2.20) _holds, then_ H={**0**}.

_(2). The following choice of_ \(\gamma\) _is sufficient for the correctness of_ (2.13):

\(\gamma=\left\{\begin{array}{ c c }
\mathrm{max}\left\{1,\lambda_m^\mathcal{A}\right\}, & \mathbf{k}=\mathbf{0}, \\
\mathrm{max}\left\{1,\lambda_m^\mathcal{A}\right\}\cdot\mathrm{max}\left\{1,\left\|\mathbf{k}\right\|_2^{-2}\right\}, & \mathbf{k}\neq\mathbf{0}.
\end{array}\right.\) (2.25)

_Proof._ If \(\mathbf{k}\neq\mathbf{0}\), Lemma 2.4 shows that L is invertible, kerL={0}. It follows that

\(\mathcal{H}=\mathrm{ker}(\mathcal{A}\mathcal{A}^\dagger+\mathcal{B}^\dagger\mathcal{B})=\{\mathbf{0}\}.\)

If **k**=**0**, \(\mathcal{L}=\sum_{i=1}^3\mathcal{D}_i^\dagger\mathcal{D}_i\), we have \(\mathrm{ker}\mathcal{L}=\cap_{i=1}^3\mathrm{ker}\mathcal{D}_i\) due to the positive semi-definiteness. The circulant matrix **D**<sub>1</sub> has a 1D kernel spanned by the vector of all ones, **1**_<sub>N</sub>_. Due to the Kronecker product structure of the _D<sub>i</sub>_, their common<tbc>

