<tbc>coefficients \(\gamma_i(q)\), or in practice \(q!\gamma_i(q)\), which we know to be polynomials in _q_ that may differ for each residue class of _n_ modulo the period _p_ (Theorem I.4.2). Ehrhart theory says that the leading coefficient of _o_<sub>P</sub>(_q;n_) is the volume of the polytope \[0,1\]<sup>2_q_</sup>, i.e., 1; so \(\gamma_0=1/q!\) for every piece.

Two nonattacking configurations of labelled pieces are said to have the same _labelled combinatorial type_ if for each two pieces P_<sub>i</sub>_ and P_<sub>j</sub>_ and move _m<sub>k</sub>_, P_<sub>j</sub>_ lies on the same side of the move line through P_<sub>i</sub>_ in the direction of _m<sub>k</sub>_ in both configurations. That is, \((z_j-z_i)\cdot m^\perp\) should have the same sign in both. (Section I.5 explains more about combinatorial types.) Two unlabelled configurations have the same _combinatorial type_ if they can be labelled to have the same labelled combinatorial type. For instance, the number of combinatorial types of one piece is 1, and the number of types for 2 copies of a piece with _r_ moves is _r_. We proved in Theorem I.5.3 that the number of combinatorial types of nonattacking configuration of _q_ copies of a piece P is _u_<sub>P</sub>(_q_;-1).  2.2 shows the number of combinatorial types for small numbers of partial queens.

## 3. The Rook and Its Squire

### 3.1. The rook.

Rooks illustrate our approach nicely because they are well understood. The basic move set, of course, is **M**<sub>R</sub>={(1,0),(0,1)}. The well-known elementary formula is

(3.1) \(u_\mathbb{R}(q;n)=q!\genfrac(){pt}{2}{n}{q}^2=\frac{1}{q!}(n)_q^2,\)

\begin{tabular}{cccccccc}
_Name_ & (_h,k_) & _q_=2 & _q_=3 & _q_=4 & _q_=5 & _q_=6 & _q\>_6 \\
Semirook & (1,0) & 1 & 1 & 1 & 1 & 1 & 1 \\
Rook & (2,0) & 2 & 6 & 24 & 120 & 720 & _q!_ \\
Semibishop & (0,1) & 1 & 1 & 1 & 1 & 1 & 1 \\
Anassa & (1,1) & 2 & 6 & 24 & 120 & 720 & _q!_ \\
Bishop & (0,2) & 2 & 6 & 24 & 120 & 720 & _q!_ \\
Semiqueen & (2,1) & 3 & 17 & & & & \\
Trident & (1,2) & 3 & 17 & & & & \\
Queen & (2,2) & 4 & 36 & 574\* & 14206\* & 501552\*\* & \\
\end{tabular}

2.2. The number of combinatorial types of configuration for nonattacking partial queens Q_<sup>hk</sup>_. Values for \(h+k\le 2\) are from Theorem I.5.8. Others are from  III.4.3.<br>
\* is a number inferred from an empirical formula in \[12\].<br>
\*\* is inferred from the empirical formula of Karaev; see \[11, 12\].

