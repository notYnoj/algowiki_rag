It is often convenient to talk about a specific \(\langle m_0,k_0,n_0;t\rangle\) algorithm, APA or exact, in terms of a trio of _encoding matrices_ \(U\in\mathbb{C}^{m_0k_0\times t}\), \(V\in\mathbb{C}^{k_0n_0\times t}\), and \(W\in\mathbb{C}^{m_0n_0\times t}\), which record the dependence of each scalar multiplication on the entries of _A_ and _B_ (in the case of _U_ and _V_ ) and the dependence of each entry of _C_ on the scalar multiplications (in the case of _W_). To be specific, these encoding matrices satisfy

\(c=W(U^Ta\odot V^Tb),\) (1.7)

where \(\odot\) is the Hadamard product and _a_, _b_, and _c_ are (row-wise) vectorized copies of _A_, _B_, and _C_.<sup>5</sup> In the APA case, these encoding matrices are dependent on the evaluation parameter \(\varepsilon\) and are therefore denoted \(U(\varepsilon)\), \(V(\varepsilon)\) and \(W(\varepsilon)\). An example of these matrices for the \(\langle 3,2,2;10\rangle\) APA algorithm of Bini et al. \[10\] is given in Figure 2.

This example also highlights the connection between the encoding matrices of an exact (or APA) matrix<tbc>

<sup>5</sup>If, for example, _A_, _B_, and _C_ are the \(3\times 2\) and \(2\times 2\) matrices pictured in Figure 1, we have _a<sup>T</sup>_=(_a_<sub>11</sub>_,a_<sub>12</sub>_,a_<sub>21</sub>_,a_<sub>22</sub>_,a_<sub>31</sub>_,a_<sub>32</sub>), _b<sup>T</sup>_=(_b_<sub>11</sub>_,b_<sub>12</sub>_,b_<sub>21</sub>_,b_<sub>22</sub>), and _c<sup>T</sup>_=(_c_<sub>11</sub>_,c_<sub>12</sub>_,c_<sub>21</sub>_,c_<sub>22</sub>_,c_<sub>31</sub>_,c_<sub>32</sub>).

\begin{tabular}{ccccccccccccccccccccc}
\(U(\varepsilon)=\left(\begin{array}{ c c c c c c c c c }
\varepsilon & 0 & 0 & 0 & 0 & \varepsilon & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1
\end{array}\right)\)<br>
\(W(\varepsilon))=\left(\begin{array}{ c c c c c c c c c c c c c c c c c c c }
\varepsilon^{-1} & -\varepsilon^{-1} & -\varepsilon^{-1} & \varepsilon^{-1} & \varepsilon^{-1} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & -\varepsilon^{-1} & 0 & 0 & 0 & \varepsilon^{-1} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & -1 & 0 & 1 & 0 & 0 & 0 & -1 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \varepsilon^{-1} & -\varepsilon^{-1} & -\varepsilon^{-1} & \varepsilon^{-1} & \varepsilon^{-1} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & -\varepsilon^{-1} & 0 & 0 & 0 & 0 & 0 & \varepsilon^{-1} & \varepsilon^{-1} & \varepsilon^{-1} & \varepsilon^{-1} & \varepsilon^{-1} & \varepsilon^{-1} & \varepsilon^{-1} & \varepsilon^{-1} & \varepsilon^{-1}
\end{array}\right)\)

(a) Parameterized encoding matrices

\(\mathcal{M}_{\langle 3,2,2\rangle}\approx\left(\begin{array}{ c c c }
\varepsilon & 0 \\
1 & 0 \\
0 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 0 \\
0 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
\varepsilon^{-1} & 1 & 0 \\
0 & 0
\end{array}\right)+\left(\begin{array}{ c c }
0 & 1 \\
0 & 0 \\
0 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 \\
0 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
-\varepsilon^{-1} & 0 \\
-\varepsilon^{-1} & -1 & 0
\end{array}\right)\)<br>
\(+\left(\begin{array}{ c c c }
0 & 0 \\
1 & 0 \\
0 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 1 \\
\varepsilon & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
-\varepsilon^{-1} & 0 & 0 \\
0 & 0 & 0
\end{array}\right)+\left(\begin{array}{ c c }
0 & 1 \\
1 & 0 \\
0 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 \\
\varepsilon & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
\varepsilon^{-1} & 0 & 0 \\
0 & 1 & 0
\end{array}\right)\)<br>
\(+\left(\begin{array}{ c c }
\varepsilon & 1 \\
0 & 0 \\
0 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 \\
0 & \varepsilon
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
\varepsilon^{-1} & 0 & 0
\end{array}\right)+\left(\begin{array}{ c c }
0 & 0 \\
0 & 1 \\
0 & \varepsilon
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 \\
0 & 0
\end{array}\right)\)<br>
\(+\left(\begin{array}{ c c }
0 & 0 \\
0 & 0 \\
1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & -1 & -\varepsilon^{-1}
\end{array}\right)+\left(\begin{array}{ c c }
0 & 0 \\
0 & 1 \\
0 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
\varepsilon & 0 \\
1 & 1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 0 & 0
\end{array}\right)\)<br>
\(+\left(\begin{array}{ c c }
0 & 0 \\
0 & 1 \\
1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
\varepsilon & 0 \\
0 & 1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 1 & 0
\end{array}\right)+\left(\begin{array}{ c c }
0 & 0 \\
0 & 0 \\
1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & \varepsilon \\
0 & 1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 0
\end{array}\right)\)

(b) Tensor decomposition

Figure 2: Two ways of representing the \(\langle 3,2,2;10\rangle\) APA matrix multiplication algorithm of Bini et al. \[10\] (see Figure 1).

