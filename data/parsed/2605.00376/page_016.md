for _i_=4_,...,m_. Observe that the dependence on _r_<sub>(_i_-1)2</sub> in <o>_r_</o><sub>(_i_-1)2</sub> disappears after substitution into (4.41) and (4.42), since (4.47) allows us to rewrite _r_<sub>(_i_-1)2</sub> in terms of _r_<sub>_i_2</sub> and _l_<sub>3</sub>, and the resulting terms are then absorbed into Zech logarithm expressions and cancel, yielding formulas depending only on _l_<sub>2</sub> and _l_<sub>3</sub>. Finally, substituting (4.49) into (4.41) and (4.42) and simplifying the resulting expressions, we obtain

\(\widehat{r_{i1}}=l_3-Z(l_2-l_3)+Z(2l_2-2l_3)\) (4.50)

and

\(\widehat{r_{i2}}=3l_2-l_3-Z(l_2-l_3)+Z\big(l_3-l_2-Z(l_2-l_3)+Z(2l_2-2l_3)\big)\) (4.51)

for _i_=4_,...,m_, which proves Corollary 4.2. These expressions depend only on the error positions _l_<sub>2</sub> and _l_<sub>3</sub>. □

Presented below is an example of correcting three symbol errors. Note that the decoding steps are the same as those in Algorithm 2, with the adaptations presented above.

**Example 4.5.** Consider the primitive polynomial \(p(x)=x^5+x^2+1\in\mathbb{F}_2[x]\), generating an MDS array code C with parameters \[11,5,7\] over \(\mathbb{F}_2^5\). The superregular Vandermonde matrix _A_ and the Frobenius companion matrix _C_ are given, respectively, by

\(A=\left[\begin{array}{ c c c c c c c }
1 & 1 & 1 & 1 & 1 & 1 \\
\alpha & \alpha^2 & \alpha^3 & \alpha^4 & \alpha^5 & \alpha^2 & \alpha^4 & \alpha^6 & \alpha^8 & \alpha^{10} \\
\alpha^3 & \alpha^6 & \alpha^9 & \alpha^{12} & \alpha^{15} & \alpha^4 & \alpha^8 & \alpha^{12} & \alpha^{16} & \alpha^{20} \\
\alpha^5 & \alpha^{10} & \alpha^{15} & \alpha^{20} & \alpha^{25}
\end{array}\right]\text{and}C=\left[\begin{array}{ c c c c c c }
0 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0
\end{array}\right].\)

Thus

\(H=\left[\begin{array}{ c c c c c c c }
I_5 & I_5 & I_5 & I_5 & I_5 & \\
C & C^2 & C^3 & C^4 & C^5 & \\
C^2 & C^4 & C^6 & C^8 & C^{10} & I_{30} \\
C^3 & C^6 & C^9 & C^{12} & C^{15} & \\
C^4 & C^8 & C^{12} & C^{16} & C^{20} & \\
C^5 & C^{10} & C^{15} & C^{20} & C^{25}
\end{array}\right]\)

is the parity-check matrix of the code C. Assume the vector received is

\(\mathbf{v}=[0101110010111000010010001011100001110101010101000101000001].\)

The syndromes from (4.2) are given by

\(\mathbf{s}_1^T=\left[\begin{array}{ c }
1 \\
1 \\
1 \\
0
\end{array}\right],\mathbf{s}_2^T=\left[\begin{array}{ c }
0 \\
0 \\
1 \\
0 \\
0
\end{array}\right],\mathbf{s}_3^T=\left[\begin{array}{ c }
1 \\
1 \\
0 \\
1 \\
1
\end{array}\right],\mathbf{s}_4^T=\left[\begin{array}{ c }
0 \\
0 \\
1 \\
0 \\
0
\end{array}\right],\mathbf{s}_5^T=\left[\begin{array}{ c }
0 \\
1 \\
0 \\
0 \\
0
\end{array}\right],\mathbf{s}_6^T=\left[\begin{array}{ c }
0 \\
1 \\
0 \\
0 \\
1
\end{array}\right].\)

As all syndromes are nonzero, taking _l_<sub>1</sub>=1 we calculate **y**_<sub>i</sub>_ for _i_=1,2_,...,_6, as in Equation (4.3),

\(\mathbf{y}_1^T=\left[\begin{array}{ c }
0 \\
1 \\
1 \\
0 \\
1
\end{array}\right],\mathbf{y}_2^T=\left[\begin{array}{ c }
0 \\
1 \\
0 \\
1 \\
1
\end{array}\right],\mathbf{y}_3^T=\left[\begin{array}{ c }
1 \\
1 \\
0 \\
0 \\
1
\end{array}\right],\mathbf{y}_4^T=\left[\begin{array}{ c }
1 \\
1 \\
0 \\
1 \\
1
\end{array}\right],\mathbf{y}_5^T=\left[\begin{array}{ c }
0 \\
1 \\
0 \\
1 \\
0
\end{array}\right],\mathbf{y}_6^T=\left[\begin{array}{ c }
0 \\
1 \\
1 \\
0 \\
1
\end{array}\right].\)

