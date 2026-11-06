The separation identifies a structural limit of the Cohn–Elkies formulation in dimensions 10 and 11. Even exact optimization of this formulation cannot recover the true packing density; a sharp bound requires additional constraints or a different bounding method.

## 5.3 Narrowing the Interval for the _n_-Queens Constant

The number _Q(n_) of placements of _n_ non-attacking queens on an \(n\times n\) board has an asymptotic form governed by a constant \(\alpha\),

\(Q(n)=\left(ne^{-\alpha+o(1)}\right)^n.\) (3)

Bounds on \(\alpha\) can be obtained from finite convex optimization problems. Nobel et al. (2023) develop a scalable Newton method for these formulations and report the interval

\[1.944000752,1.944001082\].

Épi refines the lower and upper bounds separately. Rational feasibility checks and directed rounding give

\(1.9440010223327\le\alpha\le 1.9440010262694.\) (4)

The interval width decreases from \(3.30\times 10^{-7}\) to approximately \(3.94\times 10^{-9}\), a factor of approximately 84. Figure 5 places the two intervals on a common axis.

\begin{tabular}{cccc}
**Dimension** & **Earlier dual bound** & **Épi dual bound Lid** & **Packing upper bound Ud**\\
9 & 1/20 & 0.058044329039 & \\
10 & 1/24 & 0.056433853144 & 0.05623600\\
11 & 1/24 & 0.057731808202 & 0.05664550\\
13 & 1/28 & 0.066440082613 & \\
\end{tabular}



A Higher dual bounds
B Two dimensions ruled out
d = 9
d = 10
0.35% gap
Packing upper bound
CE lower bound
0.05623600
0.05643385
d = 11
1.92% gap
d = 11
Packing upper bound
CE lower bound
0.05664550
0.05773180
0.04
0.05
0.06
0.07
Center density
Earlier bound
Épi

** 2:** New lower bounds on the optimal Cohn–Elkies bound in dimensions 9, 10, 11, and 13, rounded downward. The packing upper bounds are converted from  1.1 of Cohn et al. (2022) to center density and rounded upward. All values use center-density normalization.

**Figure 4:** Left: paired markers compare the earlier and improved dual lower bounds on the Cohn–Elkies optimum in each dimension. Right: in dimensions 10 and 11, the new lower bounds exceed known upper bounds on actual packing density. The displayed values use center density, and the relative gaps are _L<sub>d</sub>/U<sub>d</sub>_-1.

