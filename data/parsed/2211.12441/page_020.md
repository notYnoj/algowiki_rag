For a given ranking \(\rho\) of _T_ and a given adjacent-rank transposition \(\tau\), we would like to figure out the effect of \(\tau\) on the objective \(\mathrm{MinInv}(T,\cdot)\), in particular when \(\mathrm{MinInv}(T,\tau\rho)=\mathrm{MinInv}(T,\rho)\). Let \(\ell_\mathrm{lo}\) and \(\ell_\mathrm{hi}\) denote the two leaves that are affected by the transposition \(\tau\) on the ranking \(\rho\), where the subscript "lo" indicates the lower of the two leaves with respect to \(\rho\), and "hi" the higher of the two. Let _v_ be the lowest common ancestor \(\mathrm{LCA}(\ell_\mathrm{lo},\ell_\mathrm{hi})\). We use the same subscripts "lo" and "hi" for the two children of _v_: _u_<sub>lo</sub> denotes the child whose subtree contains \(\ell_\mathrm{lo}\), and _u_<sub>hi</sub> its sibling. Similarly, we denote by _L_<sub>lo</sub> the leaf set of _T_<sub>_u_<sub>lo</sub></sub>, and by _L_<sub>hi</sub> the leaf set of _T_<sub>_u_<sub>hi</sub></sub>. See Figure 9 for the subsequent analysis.

By Proposition 27, the situation before and after the application of \(\tau\) is as follows, where \(x\doteq\mathrm{XInv}_\rho(L_\mathrm{lo},L_\mathrm{hi})\) and \(y\doteq\mathrm{XInv}_\rho(L_\mathrm{hi},L_\mathrm{lo})\).

The objective function remains the same iff min(_x,y_)=min(_y_-1_,x_+1), which happens iff _x-y_=-1, or equivalently iff

\(\mathrm{DInv}_\rho(L_\mathrm{lo},L_\mathrm{hi})=\mathrm{DInv}_\rho(\{\ell_\mathrm{lo}\},\{\ell_\mathrm{hi}\}),\) (7)

where we introduce the following short-hand:

**Definition 30 (cross inversion difference,** \(\mathrm{DInv}.(\cdot,\cdot)\)**).** _For a ranking_ \(\rho\) _of a set X, and two subsets_ \(A,B\subseteq X\),<tbc>

\(\mathrm{DInv}_\rho(A,B)\doteq\mathrm{XInv}_\rho(A,B)-\mathrm{XInv}_\rho(B,A).\)

<tbc>We can split _L_<sub>lo</sub> as \(L_\mathrm{lo}=\{\ell_\mathrm{lo}\}\sqcup A=A_<\sqcup\{\ell_\mathrm{lo}\}\sqcup A_>\), where _A<sub><sub></sub></sub>_ contains all leaves in _L_<sub>lo</sub> that \(\rho\) ranks before \(\ell_\mathrm{lo}\), and _A<sub>>><sub></sub></sub>_ contains all the leaves in _L_<sub>lo</sub> that \(\rho\) ranks after \(\ell_\mathrm{lo}\). We similarly split _L_<sub>hi</sub>, as indicated in Figure 9. We have that

\(\mathrm{DInv}_\rho(L_\mathrm{lo},L_\mathrm{hi})=\mathrm{DInv}_\rho(\{\ell_\mathrm{lo}\},\{\ell_\mathrm{hi}\})+\mathrm{DInv}_\rho(\{\ell_\mathrm{lo}\},B)+\mathrm{DInv}_\rho(A,\{\ell_\mathrm{hi}\})+\mathrm{DInv}_\rho(A,B).\)

Since the ranks of \(\ell_\mathrm{lo}\) and \(\ell_\mathrm{hi}\) under \(\rho\) are adjacent, we have that \(\mathrm{DInv}_\rho(\{\ell_\mathrm{lo}\},B)=|B_<|-|B_>|\) and \(\mathrm{DInv}_\rho(A,\{\ell_\mathrm{hi}\})=|A_>|-|A_<|\). Plugging everything into (7) we conclude:

v
ulo
uhi
Llo = {lo} L A
Lhi = {hi} L B
A = A< L A>
B = B< L B>
P(A<) < P(lo) < P(A>)
lo
lo
lo
P(B<) < P(lo) < P(B>)
Llo
Lhi

\begin{tabular}{cccc}
ranking & \(\mathrm{RInv}(T_v,\cdot,\sigma(\ell_\mathrm{lo})<\sigma(\ell_\mathrm{hi}))\) & \(\mathrm{RInv}(T_v,\cdot,\sigma(\ell_\mathrm{hi})<\sigma(\ell_\mathrm{lo}))\) & \(\mathrm{MinRInv}(T_v,\cdot)\) \\
\(\rho\) & _x_ & _y_ & min(_x,y_) \\
\(\tau\rho\) & _y_-1 & _x_+1 & min(_y_-1_,x_+1) \\
\end{tabular}

Figure 9: Sensitivity analysis for binary trees

