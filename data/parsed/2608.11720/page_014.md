<tbc>_Proof._ Define<tbc>

\(U=\sum_{A\in V}\mathrm{im}(A),K=\cap_{A\in V}\mathrm{ker}(A)\text{and}W=K^\perp.\)

<tbc>Let _p_ and _q_ be the orthogonal projections on _U_ and _W_, respectively. The first part is to prove that

(6) \(V\mathrm{Mat}_d(\mathbb{C})=\{T\in\mathrm{Mat}_d(\mathbb{C}):\mathrm{im}(T)\subseteq U\}=p\mathrm{Mat}_d(\mathbb{C})\mathrm{Mat}_d(\mathbb{C})V=\{T\in\mathrm{Mat}_d(\mathbb{C}):T_{|W^\perp}=0\}=\mathrm{Mat}_d(\mathbb{C})q.\)

To prove one inclusion of the first equality, consider \(A\in V\) and \(M\in\mathrm{Mat}_d(\mathbb{C})\). Clearly, \(\mathrm{im}(AM)\subseteq\mathrm{im}(A)\subseteq U\). Hence, for all \(|x\rangle\in\mathbb{C}^d\), \(AM|x\rangle\in U\). Since _p_ is a projection on _U_, it follows that \(AM|x\rangle=pAM|x\rangle\), meaning that _AM=pAM_. This proves that \(V\mathrm{Mat}_d(\mathbb{C})\subseteq p\mathrm{Mat}_d(\mathbb{C})\).

To prove the other inclusion, fix an orthonormal basis |_u_<sub>1</sub>〉_,...,|u<sub>r</sub>_〉 of _U_ and recall that \(p=\sum_i|u_i\rangle\langle u_i|\). By definition, for each |_u<sub>i</sub>_〉 there exists matrices \(A_{i,1},\dots,A_{i,m_i}\in V\) and vectors \(|x_{i,1}\rangle,\dots,|x_{i,m_i}\rangle\in\mathbb{C}^d\) such that \(|u_i\rangle=\sum_jA_{i,j}|x_{i,j}\rangle\). For a matrix \(M\in\mathrm{Mat}_d(\mathbb{C})\), observe that \(|u_i\rangle\langle u_i|M=\sum_jA_{i,j}|x_{i,j}\rangle\langle u_i|M\) and \(|x_{i,j}\rangle\langle u_i|M\in\mathrm{Mat}_d(\mathbb{C})\). Hence, \(|u_i\rangle\langle u_i|M\in V\mathrm{Mat}_d(\mathbb{C})\), and \(pM\in V\mathrm{Mat}_d(\mathbb{C})\) follows as the sum of such terms.

To prove the second equality, let \(A\in V\) and \(M\in\mathrm{Mat}_d(\mathbb{C})\). Clearly, \(MA|x\rangle=0\) for all \(|x\rangle\in K\). By rewriting \(|x\rangle=q|x\rangle+(\mathbb{1}-q)|x\rangle\), this means \(MA|x\rangle=MAq|x\rangle\) because \((\mathbb{1}-q)|x\rangle\in K\). Hence, \(\mathrm{Mat}_d(\mathbb{C})V\subseteq\mathrm{Mat}_d(\mathbb{C})q\), proving one direction of the equality.

To prove the other inclusion, let us first observe that \(W=R:=\sum_{A\in V}\mathrm{im}(A^\dagger)\). To see why, observe that \(|x\rangle\in R^\perp\) if and only if \(\langle x,A^\dagger y\rangle=0\) for all \(A\in V\) and \(|y\rangle\in\mathbb{C}^d\), which we can rewrite as \(\langle Ax,y\rangle=0\) for all \(A\in V\) and \(|y\rangle\in\mathbb{C}^d\). Hence, \(|x\rangle\in R^\perp\) is equivalent to _A|x_〉=0 for all \(A\in V\) , which is equivalent to \(|x\rangle\in\cap_{A\in V}\mathrm{ker}(A)=K\). Now, let |_w_<sub>1</sub>〉_,...,|w<sub>r</sub>_〉 be an orthonormal basis of _W_. For all |_w<sub>i</sub>_〉, there exists \(A_{i,1},\dots,A_{i,m_i}\in V\) and vectors \(|x_{i,1}\rangle,\dots,|x_{i,m_i}\rangle\in\mathbb{C}^d\) such that \(|w_i\rangle=\sum_jA_{i,j}^\dagger|x_{i,j}\rangle\), whose adjoint is \(\langle w_i|=\sum_j\langle x_{i,j}|A_{i,j}\). For a matrix \(M\in\mathrm{Mat}_d(\mathbb{C})\), then \(M|w_i\rangle\langle w_i|=\sum_jM|w_i\rangle\langle x_{i,j}|A_{i,j}\). Since \(M|w_i\rangle\langle x_{i,j}|\in\mathrm{Mat}_d(\mathbb{C})\), we get that \(M|w_i\rangle\langle w_i|\in\mathrm{Mat}_d(\mathbb{C})V\) , and \(Mq\in\mathrm{Mat}_d(\mathbb{C})V\) follows as the sum of such terms.

The key observation is that, with respect to the decomposition<tbc>

\(\mathbb{C}^d\otimes\mathbb{C}^d=(U\oplus U^\perp)\otimes(W\oplus W^\perp)=(U\otimes W)\oplus(U\otimes W^\perp)\oplus(U^\perp\otimes W)\oplus(U^\perp\otimes W^\perp),\)

<tbc>every \(M\in\mathcal{A}:=\bigcup_{k\ge 1}S^k\) has block form

\(M=\left[\begin{array}{ c c c c c }
\tau(M) & 0 & * & 0 \\
* & 0 & * & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right]\text{where}\tau(M)=P_EM_{|E}\text{and}E=U\otimes W.\)

Before we prove it, let us argue that Lemma 5.2 follows directly from this. Indeed, (T1) and (T2) are direct from the block decomposition. To prove (T3), fix \(X\in\mathrm{End}(U)\) and \(Y\in\mathrm{End}(W)\) arbitrarily and define \(\widetilde{X}\) and \(\widetilde{Y}\) that extends them on C_<sup>d</sup>_ with zero on \(U^\perp\) and \(W^\perp\) respectively. Since \(\mathrm{im}(\widetilde{X})\subseteq U\) and \(\widetilde{Y}_{|K}=0\), by Eq (6), we have that \(\widetilde{X}\in V\mathrm{Mat}_d(\mathbb{C})\) and \(\widetilde{Y}\in\mathrm{Mat}_d(\mathbb{C})V\) . This means that \(\widetilde{X}\in V\mathrm{Mat}_d(\mathbb{C})\) and \(\widetilde{Y}\in\mathrm{Mat}_d(\mathbb{C})V\) , and thus that \(\widetilde{X}\otimes\widetilde{Y}\in V\mathrm{Mat}_d(\mathbb{C})\otimes\mathrm{Mat}_d(\mathbb{C})V\) . This space is equal to _S_<sup>2</sup>. Indeed, _S_<sup>2</sup> is spanned by elements of the form \((A\otimes B)P(C\otimes D)P=AD\otimes BC\), where \(A,C\in V\) and \(B,D\in\mathrm{Mat}_d(\mathbb{C})\), thus \(S^2\subseteq V\mathrm{Mat}_d(\mathbb{C})\otimes\mathrm{Mat}_d(\mathbb{C})V\) . Conversely, any simple tensor of the form \(AD\otimes BC\) is an element of _S_<sup>2</sup>, which implies that \(V\mathrm{Mat}_d(\mathbb{C})\otimes\mathrm{Mat}_d(\mathbb{C})V\subseteq S^2\) by linearity. By construction, on the subspace \(E=U\otimes W\), the map \(\widetilde{X}\otimes\widetilde{Y}\) acts as \(X\otimes Y\) , hence \(\tau(\widetilde{X}\otimes\widetilde{Y})=X\otimes Y\) . In finite dimension, \(T\in\mathrm{End}(U\otimes W)\) can be written as the sum of \(X_i\otimes Y_i\) with \(X_i\in\mathrm{End}(U)\) and \(Y_i\in\mathrm{End}(W)\), hence (T3) follows from linearity.

