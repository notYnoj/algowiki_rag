<tbc>For almost any \(Z\in\mathbb{C}^{n\times k}\), if \(M_0=V_0\Sigma_0W_0^*\) is the singular value decomposition of _M_<sub>0</sub>, and construct \(\check{M}_1=V_0^*M_1W_0\Sigma_0^{-1}\), and let \(\check{M}_1=S\Lambda S^{-1}\) be the eigenvalue decomposition of \(\check{M}_1\). Then \(\Lambda=\text{diag}\{\lambda_1,\dots,\lambda_k\}\) and _V_<sub>0</sub>_S_=\[_v_<sub>1</sub>_,...,v<sub>k</sub>_\]. So the remaining task is to approximate the contour integrals _M_<sub>0</sub>_,M_<sub>1</sub> by using numerical quadrature rules, which requires solving \(T(\xi_j)\) at many quadrature nodes. These systems have the same right-hand sides, so infGMRES is a natural choice for solving them efficiently. \[16\].

**6.3.1. Benchmarks.** We test six problems, which are all chosen from the NLEVP collections \[1\]. Figure 3 shows their contours, expansion nodes, and computed eigenvalues.

The contours of each problem are the same as in \[16\]. But instead of using multiple expansion nodes, we choose each contour’s geometric center as the only expansion node. This choice can avoid problem-dependent selection of expansion nodes, and also allows the Arnoldi process to be run only once. However, using fewer expansion nodes may require a larger Taylor degree and Arnoldi length to improve the accuracy of infGMRES.

For a computed eigenpair \((\widehat{\lambda},\widehat{v})\), we measure the normwise residual

(6.1) \(\rho(\widehat{\lambda},\widehat{v})=\frac{\|T(\widehat{\lambda})\widehat{v}\|_2}{\|T(\widehat{\lambda})\|_2\|\widehat{v}\|_2},\)

where the matrix norm is estimated with MATLAB’s `normest` at tolerance 0.01.

We test three methods: fully refreshed TiGMRES, Dynamic TiGMRES, and IR- TiGMRES. For a given problem, all methods use the same contour, expansion node,

x10-3
5
0.3
0.2
0.1
0
Imag
-5
-1.575
-1.57
-1.565
-1.56
-1.555
Real A

0.4
0.239
0.238
0.237
0.236
0.235
0.234
0.233
0.247
0.248
0.249
0.25
0.251
0.252
0.253
Real A

0.239
0.238
0.237
0.236
0.235
0.234
0.233
0.247
0.248
0.25
0.251
0.252
0.253
Real A

80
60
40
20
0
Imag
-20
-40
-60
-80
500
1000
1500
Real A

0.2
0.1
0
Imag
-0.1
-0.2
-0.3
0.7
0.8
0.9
1
1.1
1.2
1.3
Real A

x104
4
3
2
1
0
Imag
-1
-2
-3
-4
4
6
8
10
Real A
x104

Contour

Expansion node

* Computed eigenvalues

(a) `spring`.

(b) `acoustic\_wave\_2d`.

(c) `butterfly`.

(d) `loaded\_string`.

(e) `railtrack2\_rep`.

(f) `gun`.

Fig. 3: Contours and expansion nodes for the six NLEVP problems. The blue curve is \(\Gamma\), the blue triangle is \(\lambda_0\), and the red asterisks are the eigenvalues computed by IR-TiGMRES. All three methods use the same contours and expansion nodes.

