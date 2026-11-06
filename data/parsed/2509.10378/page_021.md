## C FLOP count calculation

We record the per-step FLOP count for base model training, NN-based PCG solve, ICHol-based PCG solve, and the ICHol setup FLOP per new system, to calculate the break-even number _n_ of new systems such that the NN-based preconditioners show advantage.

Denote _m_ as the one-time training cost of the \(\mathcal{N}_{L16}^\mathrm{FCN}\) model, _x_<sub>1</sub> as the NN-based PCG per step cost, _x_<sub>2</sub> the ICHol-based PCG per step cost, _s_<sub>1</sub> the average steps required for NN-based PCG solve, _s_<sub>2</sub> the average steps required for ICHol-based PCG solve, and _y_ the ICHol setup cost per new system. We can compute the minimum number of new systems to amortize the training cost when using NN-based PCG compared to the ICHol-based PCG with the following relation

\(m+nx_1s_1\le n(x_2s_2+y)\)<br>
\(n\ge\frac{m}{x_2s_2+y-x_1s_1}.\)

## D Results of applying even-odd preconditioners

Following \[19\], we perform even-odd decomposition of the Dirac operator _D_ as

\(D=\left(\begin{array}{ c c }
D_{ee} & D_{eo} \\
D_{oe} & D_{oo}
\end{array}\right)\) (9)

which is arranged such that the even sites precede odd sites. Now, the factorization of _D_ becomes

\(D=UAL=\left(\begin{array}{ c c }
I & D_{eo}D_{oo}^{-1} \\
0 & I
\end{array}\right)\left(\begin{array}{ c c }
\bar{D}_{ee} & 0 \\
0 & D_{oo}
\end{array}\right)\left(\begin{array}{ c c }
I & 0 \\
D_{oo}^{-1}D_{oe} & I
\end{array}\right)\) (10)

and

\(U^{-1}=\left(\begin{array}{ c c }
I & -D_{eo}D_{oo}^{-1} \\
0 & I
\end{array}\right),L^{-1}=\left(\begin{array}{ c c }
I & 0 \\
-D_{oo}^{-1}D_{oe} & I
\end{array}\right).\) (11)

\(\bar{D}_{ee}\) is the Schur complement \(\bar{D}_{ee}=D_{ee}-D_{eo}D_{oo}^{-1}D_{oe}\). After obtaining _U_<sup>-1</sup> and _L_<sup>-1</sup>, instead of solving the original equation _Dx=b_ (or equivalently _D_<sup>†</sup>_Dx=D_<sup>†</sup>_b_), we can solve _Ay=c_ (or<tbc>

\begin{tabular}{ccccc}
**Lattice Sizes** & **Unprecond CG** & **NN-precond CG** & **ICHol-precond CG** & **ICHol Setup (sparse)** \\
_L_=8 & \(1.1\times 10^4\) & \(2.0\times 10^4\) & \(7.6\times 10^4\) & \(8.6\times 10^4\) \\
_L_=16 & \(4.4\times 10^4\) & \(7.9\times 10^4\) & \(1.1\times 10^6\) & \(3.2\times 10^5\) \\
_L_=32 & \(1.8\times 10^5\) & \(3.2\times 10^5\) & \(1.7\times 10^7\) & \(1.3\times 10^6\) \\
_L_=64 & \(7.1\times 10^5\) & \(1.3\times 10^6\) & \(2.6\times 10^8\) & \(5.1\times 10^6\) \\
\end{tabular}

10-3
6 x 10-4
Final Validation Loss (offset)
4 x 10-4
3 x 10-4
2 x 10-4
K= 16
K= 32
K= 64
K= 128
K= 256

8. Operation FLOP count comparison (per step)

Fig. 10. Validation loss (offset by 6.869) comparison among models using various number of random vectors for computing the training loss.

