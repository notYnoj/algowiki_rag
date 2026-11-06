where \(fl(x\circ y)\) and \(x\circ y\) are the floating-point and exact outputs, respectively, and **u** is the _unit roundoff_. Every operation in Algorithm 4, including the evaluation of the symbolic encoding matrices and the application of the fast basis transformations, incurs this floating-point error. In addition, we assume that the coefficients \(\alpha_1,\dots,\alpha_p\) are computed to high _relative_ accuracy in line one - i.e., if \(\widehat{\alpha}_1,\dots,\widehat{\alpha}_p\) are the outputs of \(\mathbf{Vandermonde-Solve}(\varepsilon_1,\dots,\varepsilon_p)\) in floating-point arithmetic and \(\alpha_1,\dots,\alpha_p\) are the corresponding exact quantities, then

\(\frac{|\widehat{\alpha}_j-\alpha_j|}{|\alpha_j|}\le\delta\) (4.3)

for some small \(\delta>0\). Theorem A.1 demonstrates that this holds for \(\delta=O(\mathbf{u})\), under some mild conditions, if the \(\alpha_j\) are obtained by evaluating (4.1) directly. Of course, this is not the only way to handle the first step of Algorithm 4 (see for example \[30, 31\]) though it is sufficient for our purposes.

Ultimately, the performance of Algorithm 4 does not depend critically on how the Vandermonde system is solved. After all, the coefficients \(\alpha_1,\dots,\alpha_p\) could be computed ahead of time in higher precision if needed. Nevertheless, Theorem A.1 foreshadows how the stability of alternative basis APA matrix multiplication depends on the choice of \(\varepsilon_1,\dots,\varepsilon_p\). In the worst cases - for example, when the \(\varepsilon_i\) are large/small or tightly clustered - it will be difficult to avoid under/overflow when evaluating (4.1). On the flip side, if the \(\varepsilon_i\) are roots of unity then we can skip **Vandermonde-Solve** altogether, as the corresponding coefficients \(\alpha_j=1/p\) are known exactly.

The final ingredient of our analysis is an error bound of Schwartz et al. \[53\], which covers a single evaluation of an alternative basis APA matrix multiplication routine (that is, Algorithm 2). To state this result, we need the following definitions. Note that Theorem 4.3 and Theorem 4.4 generalize \[53, Definition 3.4\] and \[53, Definition 3.2\], respectively.

**Definition 4.2.** The _error accumulation operator ⋆_ takes as input a vector \(v\in\mathbb{C}^m\) and a matrix \(M\in\mathbb{C}^{m\times n}\) and outputs \(v\star M\in\mathbb{C}^n\) satisfying

\(v\star M=\left(\begin{array}{ c }
\mathrm{nnz}(M(:,1))+\|v\odot\mathbb{I}(M(:,1))\|_\infty \\
\mathrm{nnz}(M(:,2))+\|v\odot\mathbb{I}(M(:,2))\|_\infty \\
\vdots \\
\mathrm{nnz}(M(:,n))+\|v\odot\mathbb{I}(M(:,n))\|_\infty
\end{array}\right),\)

where \(\odot\) is the Hadamard product and where \(\mathrm{nnz}(w)\in\mathbb{N}\) and \(\mathbb{I}(w)\in\mathbb{R}^n\) are, respectively, the number of nonzero entries in the vector \(w\in\mathbb{C}^n\) and a vector that records whether each entry of _w_ is nonzero - that is, the _i_-th entry of I(_w_) is one if _w<sub>i</sub>_ is nonzero and zero otherwise. Following \[53\], we also use the shorthand notation ⋆_M_:=0⋆_M_ for 0 the zero vector.

**Definition 4.3.** Let \(U_\phi(\varepsilon)\), \(V_\psi(\varepsilon)\), and \(W_\nu(\varepsilon)\) be the encoding matrices of an alternative basis APA matrix multiplication algorithm with associated basis transformations \(\phi_\varepsilon\), \(\psi_\varepsilon\), and \(\nu_\varepsilon^{-1}\). Define the vectors \(a_\varepsilon\) and \(b_\varepsilon\) as follows:<tbc>

\(a_\varepsilon=\left(|\phi_\varepsilon|\cdot|U_\phi(\varepsilon)|\right)^T\mathbb{1}\text{and}b_\varepsilon=\left(|\psi_\varepsilon|\cdot|V_\psi(\varepsilon)|\right)^T\mathbb{1},\)

<tbc>where 1 is a vector of all ones (of the appropriate dimension). The algorithm’s _stability vector_ \(e_\varepsilon\) is then

\(e_\varepsilon=\left(|\nu_\varepsilon^{-1}|\cdot|W_\nu(\varepsilon)|\right)(a_\varepsilon\odot b_\varepsilon)\)

where \(\odot\) represents the Hadamard product. The corresponding _stability factor_ is \(E(\varepsilon)=\|e_\varepsilon\|_\infty\).

**Definition 4.4.** Let \(U_\phi(\varepsilon)\), \(V_\psi(\varepsilon)\), and \(W_\nu(\varepsilon)\) be the encoding matrices of an alternative basis APA matrix multiplication algorithm with associated basis transformations \(\phi_\varepsilon\), \(\psi_\varepsilon\), and \(\nu_\varepsilon^{-1}\). Define the vector

\(q_\varepsilon=\left((\star\phi_\varepsilon\star U_\phi(\varepsilon))+(\star\psi_\varepsilon\star V_\psi(\varepsilon))\right)\star W_\nu(\varepsilon)^T\star\nu_\varepsilon^{-T}.\)

The _stability prefactor_ of the algorithm is then \(Q(\varepsilon)=\|q_\varepsilon\|_\infty\).

Note that the stability factor \(E(\varepsilon)\) can be used to bound the norm of the output of a recursive APA algorithm. Indeed, if _C_ is the output of Algorithm 2 (which defaults to exact matrix multiplication after _L_ recursive steps) in exact arithmetic, then<tbc>

\(\|C\|\le(k/k_0^L)E(\varepsilon)^L\|A\|\|B\|\) (4.4)

