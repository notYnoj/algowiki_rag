<tbc>_be nonsingular and_ \(\hat{P},\hat{R}\in\mathbb{C}^{n\times n_c}\) _be defined so that_<tbc>

\(\mathcal{R}(\hat{P})=\mathcal{R}(\big[v_1\cdots v_{n_c}\big])\text{\textit{and}}\mathcal{N}(\hat{R}^HA)=\mathcal{R}(\big[v_{n_c+1}\cdots v_n\big]).\)

<tbc>_Then, for_ \((\nu_1,\nu_2)\in\{(0,1),(1,0),(1,1)\}\) _and all_ \(P,R\in\mathbb{C}^{n\times n_c}\) _such that R<sup>H</sup>AP is nonsingular it holds_<tbc>

\(\|E_+^{\nu_1,\nu_2}(\hat{P},\hat{R})\|_B^2=(1-\mu_{n_c+1})^2\le\|E_+^{\nu_1,\nu_2}(P,R)\|_B^2.\)

<tbc>_Proof._ Let the smoothing assumption be satisfied. By Proposition 3.3 and Theorem 3.5 the matrix \(\widehat{M}^{-1}B\) is then _B_-unitarily diagonalizable with real eigenvalues \(0<\mu_1\le\cdots\le\mu_n\le 1\) and correspondingly sorted _B_-unitary eigenvector matrix _V_ . Furthermore, let \(I-\widehat{M}^{-1}B\) be nonsingular. Since<tbc>

\(I-\widehat{M}^{-1}B=(I-M^{-1}A)(I-M^{-1}A)^+\)

<tbc>the matrix _I-M_<sup>-1</sup>_A_ is also nonsingular. With (_C_<sup>+</sup>)<sup>-1</sup>=_B_<sup>-1</sup>_C_<sup>-_HB_</sup>=(_C_<sup>-1</sup>)<sup>+</sup> we get<tbc>

\((I-\widehat{M}^{-1}B)^{-1}=\big((I-M^{-1}A)(I-M^{-1}A)^+\big)^{-1}=\big((I-M^{-1}A)^{-1}\big)^+(I-M^{-1}A)^{-1}.\)

<tbc>The _B_-orthogonality of _V_ implies _B=V_ <sup>-_H_</sup>_V_ <sup>-1</sup>. For all \(P,R\in\mathbb{C}^{n\times n_c}\) such that _R<sup>H</sup>AP_ is nonsingular it now holds

\(\|E_+^{\nu_1,\nu_2}(P,R)\|_B^2=\|(I-(M^{-1}A)^+)^{\nu_2}(I-\Pi_A(P,R))(I-M^{-1}A)^{\nu_1}\|_B^2\)<br>
\(=sup_{y\neq 0}\frac{\|(I-(M^{-1}A)^+)^{\nu_2}(I-\Pi_A(P,R))(I-M^{-1}A)^{\nu_1}y\|_B^2}{\|y\|_B^2}\)<br>
\(=sup_{x\neq 0}\frac{\|(I-(M^{-1}A)^+)^{\nu_2}(I-\Pi_A(P,R))x\|_B^2}{\|((I-M^{-1}A)^{-1})^{\nu_1}x\|_B^2}\)<br>
\(\ge sup_{x\in\mathcal{N}(R^HA)x\neq 0}\frac{\|(I-(M^{-1}A)^+)^{\nu_2}x\|_B^2}{\|((I-M^{-1}A)^{-1})^{\nu_1}x\|_B^2}\)<br>
\(=sup_{x\in\mathcal{N}(R^HA)x\neq 0}\frac{\langle(I-(M^{-1}A)^+)^{\nu_2}x,(I-(M^{-1}A)^+)^{\nu_2}x\rangle_B}{\langle((I-M^{-1}A)^{-1})^{\nu_1}x,((I-M^{-1}A)^{-1})^{\nu_1}x\rangle_B}\)<br>
\(=sup_{x\in\mathcal{N}(R^HA)x\neq 0}\frac{\langle x,(I-\widehat{M}^{-1}B)^{\nu_2}x\rangle_B}{\langle x,((I-\widehat{M}^{-1}B)^{-1})^{\nu_1}x\rangle_B}\)<br>
\(=sup_{x\in\mathcal{N}(R^HA)x\neq 0}\frac{x^H(V^{-H}(I-D)V^{-1})^{\nu_2}x}{x^H(V^{-H}(I-D)^{-1}V^{-1})^{\nu_1}x}=:sup_{x\in\mathcal{N}(R^HA)x\neq 0}\frac{x^H\mathcal{A}^{\nu_2}x}{x^H\mathcal{C}^{\nu_1}x}\)

where C is HPD and A is Hermitian. Then \(\mathcal{C}^{-1}\mathcal{A}=V(I-D)^{\nu_1+\nu_2}V^{-1}\) and has eigenvalues \((1-\mu_i)^{\nu_1+\nu_2}\). By Theorem 4.3 it holds the following

\(min_{P,R\in\mathbb{C}^{n\times n_c}}\|E_+^{\nu_1,\nu_2}(P,R)\|_B^2=min_{P\in\mathbb{C}^{n\times n_c}}min_{R\in\mathbb{C}^{n\times n_c}}\|E_+^{\nu_1,\nu_2}(P,R)\|_B^2\)<br>
\(\ge min_{P\in\mathbb{C}^{n\times n_c}}min_{R\in\mathbb{C}^{n\times n_c}}sup_{x\in\mathcal{N}(R^HA)x\neq 0}\frac{x^H\mathcal{A}^{\nu_2}x}{x^H\mathcal{C}^{\nu_1}x}\)

