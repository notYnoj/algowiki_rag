## 3.1 Background and Motivation

To outperform classical matrix multiplication in practice, the arithmetic and IO complexities of fast matrix multiplication algorithms must have small leading coefficients. To promote this, Karstadt and Schwartz \[38\] introduced alternative basis matrix multiplication, which takes an existing, exact algorithm and computes a set of basis transformations that sparsify the corresponding encoding matrices. That is, if \(U\in\mathbb{C}^{m_0k_0\times t}\), \(V\in\mathbb{C}^{k_0n_0\times t}\), and \(W\in\mathbb{C}^{m_0n_0\times t}\) are the encoding matrices of a \(\langle m_0,k_0,n_0;t\rangle\) matrix multiplication scheme, the alternative basis method computes automorphisms \(\phi:\mathbb{C}^{m_0k_0}\rightarrow\mathbb{C}^{m_0k_0}\), \(\psi:\mathbb{C}^{k_0n_0}\rightarrow\mathbb{C}^{k_0n_0}\), and \(\nu:\mathbb{C}^{m_0n_0}\rightarrow\mathbb{C}^{m_0n_0}\) and factors _U_, _V_ and _W_ as follows:

\(U=\phi\cdot U_\phi,V=\psi\cdot V_\psi,\text{and}W=\nu^{-1}\cdot W_\nu,\) (3.1)

where \(U_\phi\), \(V_\psi\), and \(W_\nu\) are sparse (or at least sparser than _U_, _V_ , and _W_). The key insight is the following: rewriting (1.7) as

\(c=W(U^Ta\odot V^Tb)=\nu^{-1}\left[W_\nu\left(U_\phi^T(\phi^Ta)\odot V_\psi^T(\psi^Tb)\right)\right]\) (3.2)

for _a_, _b_, and _c_ vectorized copies of \(A\in\mathbb{C}^{m_0\times k_0}\), \(B\in\mathbb{C}^{k_0\times n_0}\), and _C=AB_, we observe that \(\nu(C)\in\mathbb{C}^{m_0\times n_0}\) can be computed by applying the bilinear form represented by \(U_\phi\), \(V_\psi\) and \(W_\nu\) to the transformed inputs \(\phi(A)\in\mathbb{C}^{m_0\times k_0}\) and \(\psi(B)\in\mathbb{C}^{k_0\times n_0}\). Here, we use \(\phi(A)\), \(\psi(B)\), and \(\nu(C)\) to denote the matrices that, when vectorized, correspond to \(\phi^Ta\), \(\psi^Tb\), and \(\nu c\). Assuming that \(\phi(A)\), \(\psi(B)\) and _C_ can be obtained cheaply from _A_, _B_, and \(\nu(C)\), respectively, this offers a potentially much more efficient way of computing the output _C_. Note additionally that the basis transformations, like the corresponding encoding matrices, can be applied recursively for use on matrices of arbitrary size.

In \[38\], Karstadt and Schwartz used the alternative basis approach to reduce the leading coefficient in the arithmetic complexity of Strassen’s \(\langle 2,2,2;7\rangle\) algorithm to 5 without increasing communication costs, making it more practical than \[16\]. Efforts to apply this technique to other fast exact algorithms quickly followed \[6, 7, 29\]. Corresponding implementations show CPU and GPU speedups for the resulting alternative basis algorithms (e.g., \[13, 25, 37, 52, 54\]). In all of these, fast basis transformations are used, which can be applied recursively to \(A\in\mathbb{C}^{m\times k}\), \(B\in\mathbb{C}^{k\times n}\) and \(C\in\mathbb{C}^{m\times n}\) at the modest overhead cost of _O(mk_log(_mk_)), _O(kn_log(_kn_)), and _O(mn_log(_mn_)) flops, respectively (see \[38, Section 2.1\]).

Extending this work to the APA setting is relatively straightforward. Given a set of encoding matrices \(U(\varepsilon)\), \(V(\varepsilon)\), and \(W(\varepsilon)\) for \(\langle m_0,k_0,n_0;t\rangle\) APA matrix multiplication, we seek symbolic basis transformations \(\phi_\varepsilon\), \(\psi_\varepsilon\), and \(\nu_\varepsilon\) such that

\(U(\varepsilon)=\phi_\varepsilon\cdot U_\phi(\varepsilon),V(\varepsilon)=\psi_\varepsilon\cdot V_\psi(\varepsilon),\text{and}W(\varepsilon)=\nu_\varepsilon^{-1}\cdot W_\nu(\varepsilon),\) (3.3)

where \(U_\phi(\varepsilon)\), \(V_\psi(\varepsilon)\), and \(W_\nu(\varepsilon)\) are the (parser) encoding matrices of an APA bilinear form in the bases \(\phi_\varepsilon\), \(\psi_\varepsilon\), \(\nu_\varepsilon\). These can then be used to generate an Alternative Basis APA Matrix Multiplication algorithm, which is shown here as Algorithm 2.

**Algorithm 2** Alternative Basis APA Matrix Multiplication (**AltBasis-Recursive-APA**\(_{\langle\phi,\psi,\nu\rangle}\))

**Input:** \(A\in\mathbb{C}^{m\times k}\), \(B\in\mathbb{C}^{k\times n}\), and \(\varepsilon\in\mathbb{C}\).

**Output:** \(M=AB+\varepsilon R_1+\varepsilon^2R_2+\cdots+\varepsilon^{p-1}R_{p-1}\) for residual matrices \(R_1,\dots,R_{p-1}\in\mathbb{C}^{m\times n}\) and _p=dL_+1.

1: \(\widetilde{A}=\phi_\varepsilon(A)\)

2: \(\widetilde{B}=\psi_\varepsilon(B)\)

3: \(\widetilde{M}=\text{\textbf{Recursive-APA}}_{\langle U_\phi(\varepsilon),V_\psi(\varepsilon),W_\nu(\varepsilon)\rangle}(\widetilde{A},\widetilde{B})\)

4: \(M=\nu_\varepsilon^{-1}(\widetilde{M})\)

5: **return** _M_

In this pseudocode, **Recursive-APA**\(_{\langle U_\phi(\varepsilon),V_\psi(\varepsilon),W_\nu(\varepsilon)\rangle}(\widetilde{A},\widetilde{B})\) evaluates the recursive bilinear form corre sponding to \(U_\phi(\varepsilon)\), \(V_\psi(\varepsilon)\), and \(W_\nu(\varepsilon)\) at the transformed inputs \(\widetilde{A}\) and \(\widetilde{B}\), obtained by applying \(\phi_\varepsilon\) and \(\psi_\varepsilon\) to _A_ and _B_. Following the notation from the previous section, _d_ is the degree of the underlying APA matrix multiplication algorithm and _L_ is the number of recursive steps applied. The complexity of Algorithm 2, in terms of _t_ and the sparsity of \(U_\phi(\varepsilon)\), \(V_\psi(\varepsilon)\), and \(W_\nu(\varepsilon)\) and including the cost of the basis transformations, follows from the exact case - e.g., \[32, 38\].

