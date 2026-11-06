## 4 The emulation algorithm as implemented

Algorithm 1 summarizes the pipeline for one output tile; in the common case the whole matrix _C_ forms a single tile. All steps run on the GPU, and the host only computes tables of size _O(s_). In the following we describe each step and indicate where it follows the literature and where it departs from it.

### 4.1 Choice of the scaling width _t_

For _x\>_0 let e(_x_) denote the binary exponent returned by the C function `frepxp`, i.e. the integer with \(2^{\mathrm{e}(x)-1}\le x<2^{\mathrm{e}(x)}\). The scaling exponents in Eq. (1) are<tbc>

\(D_i=t-\mathrm{e}\big(\mathrm{max}_p|a_{ip}|\big),E_j=t-\mathrm{e}\big(\mathrm{max}_p|b_{pj}|\big),\) (3)

<tbc>so that |_a<sub>ip</sub>_2<sup>_D<sub>i</sub>_</sup>|_\<_2_<sup>t</sup>_ and, after rounding, \(|\hat{a}_{ip}|\le 2^t\) (likewise for _B_). To choose _t_, we impose the a-priori bound

\(|\hat{c}_{ij}|\le k2^{2t}\le M/4,\) (4)

which is half of the range required for uniqueness in Eq. (2). This factor of 1/2 is the price of the fast quotient evaluation described in Section 4.4; it costs one bit of _t_ per two moduli.  2 lists _t_ for typical values of _k_. For \(s\ge 16\) and \(k\le 2^{14}\) we have \(t\ge 53\), so every element within _t_-53 binades of its row maximum is represented exactly.

### 4.2 Residue generation without floating-point arithmetic

Because FP64 is slow on Xe2, we compute \(\hat{a}=\mathrm{rint}(a2^D)\) directly from the bit pattern of _a_. Writing \(a=\pm\mu 2^{e_a-1075}\) with integer significand \(\mu<2^{53}\), we obtain \(\hat{a}=\pm\mu 2^\sigma\) for \(\sigma=\)<tbc>

\(\text{\textbf{Algorithm 1} Emulated DGEMM (Ozaki scheme II), one tile, op}=\mathbb{N}\text{\textbf{Require:}}A\in\mathbb{R}^{m\times k}\text{,}B\in\mathbb{R}^{k\times n}\text{,}s\text{moduli}m_1..m_s\text{1:}t\leftarrow\text{largest integer with}k2^{2t+2}\le M\text{, capped at 100}\triangleright\text{host, Eq. (4) 2:}D_i,E_j\leftarrow\text{Eq. (3)}\triangleright\text{kernels RowMax, ColMax 3:}(A^{(t)})_{t=1}^s\leftarrow\text{Split}(A,D)\text{,}(B^{(t)})_{t=1}^s\leftarrow\text{Split}(B,E)\triangleright\text{one pass each, Alg. 2 4:}C^{(t)}\leftarrow A^{(t)}B^{(t)}\text{for}t=1..s\triangleright\text{one strided-batch INT8 GEMM 5:}C\leftarrow\alpha\text{CRT}(C^{(1..s)},D,E)+\beta C\triangleright\text{Alg. 3}\)

\begin{tabular}{ccccccc}
_s_ & log<sub>2</sub>_M_ & _N<sub>L</sub>_ & _t_, _k_=1024 & _t_, _k_=4096 & _t_, _k_=16384 & _t_, _k_=65536 \\
4 & 31.9 & 2 & 9 & 8 & 7 & 6 \\
6 & 47.8 & 2 & 17 & 16 & 15 & 14 \\
8 & 63.6 & 2 & 25 & 24 & 23 & 22 \\
10 & 79.3 & 3 & 33 & 32 & 31 & 30 \\
12 & 94.9 & 3 & 41 & 40 & 39 & 38 \\
14 & 110.4 & 4 & 49 & 48 & 47 & 46 \\
16 & 125.6 & 4 & 56 & 55 & 54 & 53 \\
18 & 140.8 & 5 & 64 & 63 & 62 & 61 \\
20 & 155.8 & 5 & 71 & 70 & 69 & 68 \\
22 & 170.6 & 6 & 79 & 78 & 77 & 76 \\
24 & 185.2 & 6 & 86 & 85 & 84 & 83 \\
\end{tabular}

2: Moduli configuration: log<sub>2</sub>_M_, number of 32-bit limbs used in the reconstruction, and scaling width _t_ for several values of _k_.

