## B.2 Residual Matrices

The remainder matrices _R_<sub>3</sub>_,R_<sub>4</sub>_,R_<sub>5</sub>_,R_<sub>6</sub>_,R_<sub>7</sub>_,R_<sub>8</sub> for the corresponding algorithm are given below:

\(R_3=\left(\begin{array}{ c c c c c }
0 & 2a_{23}(b_{13}+b_{23}+b_{34}+b_{45})-2a_{24}(b_{13}-b_{44}+b_{45}) & 0 & 0 & 0 \\
0 & 0 & a_{23}(b_{13}+b_{23}+b_{34}+b_{45})-a_{24}(b_{13}-b_{44}+b_{45}) & 0 & 0
\end{array}\right)\)<br>
\(R_4=\left(\begin{array}{ c c c c c }
0 & -2a_{13}(b_{13}+b_{23}+b_{34}+b_{45})+2a_{14}(b_{13}-b_{44}+b_{45}) & 0 & 0 & 0 \\
-a_{23}(b_{13}+b_{23}+b_{34}+b_{45})+a_{24}(b_{13}-b_{44}+b_{45}) & a_{23}(b_{13}+b_{23}+b_{34}+b_{45})-a_{24}(b_{13}-b_{44}+b_{45}) & -a_{13}(b_{13}+b_{23}+b_{34}+b_{45})+a_{14}(b_{13}-b_{44}+b_{45}) & 0 & 0
\end{array}\right)\)<br>
\(R_5=\left(\begin{array}{ c c c c c }
0 & 0 & 0 & 0 \\
a_{13}(b_{13}+b_{23}+b_{34}+b_{45})-a_{14}(b_{13}-b_{44}+b_{45}) & -a_{13}(b_{13}+b_{23}+b_{34}+b_{45})+a_{14}(b_{13}-b_{44}+b_{45}) & 0 & 0
\end{array}\right)\)<br>
\(R_6=\left(\begin{array}{ c c c c c }
0 & -2a_{23}(b_{24}+b_{25})+2a_{24}b_{14} & 0 & 0 & 0 \\
0 & 0 & -a_{23}(b_{24}+b_{25})+a_{24}b_{14} & 0 & 0
\end{array}\right)\)<br>
\(R_7=\left(\begin{array}{ c c c c c }
0 & 2a_{13}(b_{24}+b_{25})-2a_{14}b_{14} & 0 & 0 & 0 \\
a_{23}(b_{24}+b_{25})-a_{24}b_{14} & -a_{23}(b_{24}+b_{25})+a_{24}b_{14} & a_{13}(b_{24}+b_{25})-a_{14}b_{14} & 0 & 0
\end{array}\right)\)<br>
\(R_8=\left(\begin{array}{ c c c c c }
0 & 0 & 0 & 0 \\
-a_{13}(b_{24}+b_{25})+a_{14}b_{14} & a_{13}(b_{24}+b_{25})-a_{14}b_{14} & 0 & 0
\end{array}\right)\)

## B.3 Sparsified Encoding Matrices

Finally, sparsifying these algorithms as described in Section 3, noting that the specialization of Section 3.2.3 applies, yields the following basis transformations and (constant) encoding matrices:

\(\phi_\varepsilon^{-1}=\left(\begin{array}{ c c c c c c c c }
\varepsilon^{-1} & \varepsilon^{-1} & 0 & 0 & -\varepsilon^{-2} & -\varepsilon^{-2} & 0 & 0 \\
0 & 0 & \varepsilon^2 & -\varepsilon^2 & -\varepsilon^{-2} & -\varepsilon^{-2} & 0 & \varepsilon \\
0 & -\varepsilon^{-1} & 0 & 0 & -\varepsilon^{-2} & 0 & \varepsilon & 0 \\
0 & 0 & \varepsilon^2 & 0 & -\varepsilon^{-2} & -\varepsilon^{-2} & 0 & 0 \\
0 & 0 & 0 & 0 & -\varepsilon^{-2} & -\varepsilon^{-2} & 0 & 0 \\
0 & 0 & 0 & 0 & \varepsilon^{-2} & 0 & -\varepsilon & 0 \\
0 & 0 & 0 & 0 & \varepsilon^{-2} & 0 & -\varepsilon & 0 \\
0 & 0 & 0 & 0 & -\varepsilon^{-2} & -\varepsilon^{-2} & \varepsilon & 0 \\
0 & 0 & 0 & 0 & \varepsilon^{-2} & \varepsilon^{-2} & 0 & -\varepsilon
\end{array}\right)\)<br>
\(\nu_\varepsilon^{-1}=\left(\begin{array}{ c c c c c c c c c c }
0 & 0 & \varepsilon & \varepsilon^2 & 0 & 0 & 0 & 0 & 0 & 0 \\
-\varepsilon & -\varepsilon^2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & -\varepsilon^2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 3\varepsilon^2 & 0 & \varepsilon^2 & 0 & -2\varepsilon & 0 & -\varepsilon^{-2} & 0 & -\varepsilon^{-2} \\
-2\varepsilon & -2\varepsilon^2 & -\varepsilon & -\varepsilon^2 & 1 & \varepsilon & 0 & 0 & \varepsilon^{-3} & \varepsilon^{-2} \\
0 & 2\varepsilon^2 & 0 & \varepsilon^2 & 0 & 0 & 0 & 0 & 0 & -\varepsilon^{-2} \\
-3\varepsilon & -3\varepsilon^2 & -\varepsilon & -\varepsilon^2 & 1 & \varepsilon & \varepsilon^{-3} & \varepsilon^{-2} & \varepsilon^{-3} & \varepsilon^{-2} \\
0 & 0 & 0 & 0 & 1 & \varepsilon & \varepsilon^{-3} & \varepsilon^{-2} & 0 & 0 \\
0 & \varepsilon^2 & 0 & 0 & 0 & -\varepsilon & 0 & -\varepsilon^{-2} & 0 & 0 \\
0 & \varepsilon^2 & -2\varepsilon & -\varepsilon^2 & 0 & -\varepsilon & 0 & -\varepsilon^{-2} & 0 & 0
\end{array}\right)\)

