## 6.4 Dependence on the coarse mesh for fixed _h_

To examine Lemma 5.1 directly, we fix the fine mesh _h_=1/32 and vary the coarse mesh, _H_=1/2,1/4,1/8,1/16.  3 and Figure 1(b) report the relative coarse error \(e_4(\Phi_h-\Phi_H)\), the relative two-grid correction error \(e_E(\Phi_h-\Phi_h^\text{tg})\), the ratio of the corresponding absolute quantities, and the total error. The coarse _L_<sup>4</sup> error converges approximately as _O(H_<sup>2</sup>), and the two-grid correction error with observed order about 3.7, so that the ratio \(\left|\left|\left|\Phi_h-\Phi_h^\text{tg}\right|\left|\left|\Phi_h-\Phi_H\right|\right|_{0,4}^2\) stays bounded (between 0.27 and 0.52 in the asymptotic range), as predicted by (61). The observed order is higher than the guaranteed order _H_<sup>2(_s_-1)+_t/_2</sup>=_H_<sup>5/2</sup> in (65), for the same reason as in  1: the _L_<sup>4</sup> estimate (55) is a worst-case bound. Both quantities are measured against the fine-mesh solution \(\Phi_h\) with _h_=1/32, so that the last row (_H_=2_h_) is at the limit of the asymptotic regime, which explains the slight drift of the ratio. Already for _H_=1/4, i.e., with 343 interior coarse degrees of freedom against 250047 on the fine mesh, the energy error of the two-grid solution exceeds that of the fine-mesh solution by only about 0.01%.

\begin{tabular}{cccccccc}
_H_ & \(e_E(\Phi_h-\Phi_H)\) & \(e_4(\Phi_h-\Phi_H)\) & rate & \(e_E(\Phi_h-\Phi_h^\text{tg})\) & rate & ratio & \(e_E(\Phi-\Phi_h^\text{tg})\) \\
1/2 & 2.06e+00 & 1.080e+00 & - & 3.533e-02 & - & 1.28 & 9.4700e-02 \\
1/4 & 6.78e-01 & 2.097e-01 & 2.36 & 2.822e-04 & 6.97 & 0.27 & 8.6560e-02 \\
1/8 & 3.34e-01 & 5.134e-02 & 2.03 & 2.164e-05 & 3.70 & 0.35 & 8.6552e-02 \\
1/16 & 1.50e-01 & 1.150e-02 & 2.16 & 1.625e-06 & 3.73 & 0.52 & 8.6551e-02 \\
\end{tabular}

(a) Errors of Φh and Φtg H ~ h2/5
(b) Two-grid correction vs. coarse error
fine-mesh Newton, energy norm
two-grid, energy norm
100
fine-mesh Newton, L2 norm
2
two-grid, L2 norm
102
10-1
101
10-2
100
10-1
10-3
10-2
O(H4)
10-3
10-4
1/32
1/16
1/8
1/4
1/16
1/8
1/4
1/2
fine mesh size h
coarse mesh size H (fine mesh h = 1/32)

Figure 1: (a) Relative energy and _L_<sup>2</sup> errors of the fine-mesh solution \(\Phi_h\) and of the two-grid solution \(\Phi_h^\text{tg}\) with _H≈h_<sup>2/5</sup> (s 1 and 2). (b) For the fixed fine mesh _h_=1/32: the relative two-grid correction error \(e_E(\Phi_h-\Phi_h^\text{tg})\) and the squared relative _L_<sup>4</sup> coarse error \(e_4(\Phi_h-\Phi_H)^2\) as functions of _H_ ( 3).

3: Fixed fine mesh _h_=1/32 and varying coarse mesh: relative coarse error in the energy and _L_<sup>4</sup> norms, relative two-grid correction error, the ratio \(\left|\left|\left|\Phi_h-\Phi_h^\text{tg}\right|\left|\left|\left|\Phi_h-\Phi_H\right|\right|\right|_{0,4}^2\) of absolute quantities as in (61), and relative energy error of \(\Phi_h^\text{tg}\) (the fine-mesh solution has \(e_E(\Phi-\Phi_h)\)=8.6551e-02).

