In  2, we list several parameter settings for Theorems 24 and 25. Theorem 5 is the entry _c_=19, _q_=0.43, applied to a set _W_ of \(N^2/\sqrt{D}\) wanted entries (that is, \(\kappa=\frac{1}{2}\)). We next state explicitly the parameter setting that we use in the introduction and in our reductions in Sections 3 and 5. It is the entry _c_=21, _q_=0.43 of  2, whose switching order is _t=m/_9, as in Section 2, with the logarithmic factors absorbed into the exponents.

**Corollary 26.** _Let_ \(N\ge D^{18}\)_, and let_ \(X\in\mathbb{Z}^{N\times D}\) _and_ \(Y\in\mathbb{Z}^{D\times N}\) _have entries of absolute value at most N_<sup>_O_(1)</sup>_. We can preprocess them deterministically in O(N_<sup>2</sup>_/D_<sup>0.063</sup>) _time and space, after which any single entry_ (_XY_)\[_I,J_\] _can be computed deterministically in O(D_<sup>0.437</sup>) _time. Hence, for every set W of positions of an_ \(N\times N\) _matrix, the entries_ (_XY_)\[_I,J_\], \((I,J)\in W\)_, can be computed deterministically in O_(|_W|D_<sup>0.437</sup>+_N_<sup>2</sup>_/D_<sup>0.063</sup>) _time, which is O(N_<sup>2</sup>_/D_<sup>0.063</sup>) _whenever_ \(|W|\le N^2/\sqrt{D}\).

## 4.2 Boxes

In this subsection, we define the boxes and prove two important facts about them. Intuitively, a box is a group of leaves that is shared by many output strings. In preprocessing we will add up the products at the leaves of each box, and then that value can help to answer many queries. In terms of the switching order _t_, we will ensure that the boxes of an output string partition its leaves of order at least _t_, and that there are only \(\alpha_t\) of them. We will thus see, in Lemmas 27 and 28, that every output entry is the sum of a few products and a few values of boxes.

### Cubes.

A **_cube_** is a string \(\pi=\pi_1\cdots\pi_L\) of _L_ symbols, each of which is one of the ten terms of Schönhage’s identity or a star ∗. Its **_leaves_** are the leaves obtained by replacing each star by any of the ten terms, so a cube with _e_ stars has 10_<sup>e</sup>_ leaves, and a cube without stars is a single leaf.<tbc>

\begin{tabular}{ccccccccccccc}
 & & \multicolumn{5}{c}{Theorem 24: the data structure} & \multicolumn{5}{c}{Theorem 25: the wanted entries} \\
ratio & \(D\le N^\varepsilon\) & \multicolumn{5}{c}{\(\gamma\) for query time _D<sup>q</sup>_, _q_=} & \multicolumn{5}{c}{\(\gamma\) for \(|W|\le N^2/D^\kappa\), \(\kappa=\)} \\
_c_ & \(\varepsilon\) & 0.10 & 0.25 & 0.43 & 0.50 & 0.75 & 0.90 & 0.10 & 0.25 & 0.50 & 0.75 & 1.00 \\
40 & 0.029 & 0.0205 & 0.0608 & 0.1175 & 0.1429 & 0.2417 & 0.3095 & 0.0166 & 0.0473 & 0.1060 & 0.1720 & 0.2442 \\
21 & 0.056 & 0.0112 & 0.0331 & **0.0640** & 0.0778 & 0.1316 & 0.1685 & 0.0099 & 0.0286 & 0.0653 & 0.1074 & 0.1546 \\
19 & 0.062 & 0.0097 & 0.0287 & **0.0555** & 0.0675 & 0.1142 & 0.1463 & 0.0087 & 0.0253 & 0.0578 & 0.0954 & 0.1379 \\
15 & 0.079 & 0.0061 & 0.0183 & 0.0354 & 0.0430 & 0.0728 & 0.0932 & 0.0057 & 0.0168 & 0.0389 & 0.0646 & 0.0941 \\
12 & 0.099 & 0.0028 & 0.0083 & 0.0160 & 0.0195 & 0.0330 & 0.0423 & 0.0027 & 0.0080 & 0.0186 & 0.0312 & 0.0459 \\
10.5 & 0.114 & 0.0007 & 0.0022 & 0.0043 & 0.0052 & 0.0089 & 0.0114 & 0.0007 & 0.0022 & 0.0052 & 0.0087 & 0.0129 \\
\end{tabular}

2: Explicit parameters for Theorems 24 and 25. Each row is a choice of the ratio _c=L/m_. The parameter \(\varepsilon\) is determined by _c_ and says how thin the product must be, i.e., every entry of the row holds whenever \(D\le N^\varepsilon\). On the left, the columns correspond to a choice of _q_, and the numerical entry is a value \(\gamma\) for which Theorem 24 holds, meaning that after \(O(N^2log^2D/D^\gamma)\) preprocessing, a query takes _O(D<sup>q</sup>_log_D_) time. On the right, the columns correspond to a choice of \(\kappa\), and the numerical entry is a value \(\gamma\) for which Theorem 25 holds, meaning that any \(|W|\le N^2/D^\kappa\) wanted entries take \(O(N^2log^2D/D^\gamma)\) time. On the left side, the column _q_=0.43 uses the switching order _t=m/_9 of Section 2 (more precisely, _q_=0.4277_..._), and its two bold entries are Theorem 5 (_c_=19, where \(\gamma=1/18=0.0555\dots\)) and Corollary 26 (_c_=21). A larger _c_ gives a larger \(\gamma\) but a smaller \(\varepsilon\), and a slower query or a sparser _W_ allows a larger \(\gamma\). We round all values down, and we will explain how we compute them in Section 4.4.

