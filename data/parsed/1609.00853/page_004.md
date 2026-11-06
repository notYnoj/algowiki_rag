<tbc>polytope (_n_+1)B_<sup>q</sup>_=(_n_+1)\[0,1\]<sup>2_q_</sup>. For a _nonattacking configuration_ the pieces must be in the interior, (_n_+1)(0,1)<sup>2</sup>, and no two pieces may attack each other. In other words, if there are pieces at positions _z<sub>i</sub>_ and _z<sub>j</sub>_, then _z<sub>j</sub>-z<sub>i</sub>_ is not a multiple of any \(m\in\mathbf{M}\).

The attack lines determine _move hyperplanes_ in R<sup>2_q_</sup>, \(\EuScript{H}_{ij}^{d/c}:(z_j-z_i)\cdot m^\perp=0\) for each \(m=(c,d)\in\mathbf{M}\), where \(m^\perp:=(d,-c)\), whose integral points in the dilated open hypercube (_n_+1)(0,1)<sup>2_q_</sup> represent attacking configurations. The nonattacking configurations are the integral points in the open hypercube and outside every hyperplane, so it is they we want to count. The combination of the hypercube \[0,1\]<sup>2_q_</sup> and the set A<sub>P</sub> of hyperplanes is called an _inside-out polytope_ \[2\]. Its _vertices_ are all the points in \[0,1\]<sup>2_q_</sup> that are intersections of move hyperplanes and facet hyperplanes of \[0,1\]<sup>2_q_</sup>. From \[2\] we know _o_<sub>P</sub>(_q;n_) is a quasipolynomial whose period divides the _denominator D_(\[0,1\]<sup>2_q_</sup>,A<sub>P</sub>), defined as the least common multiple of the denominators of all coordinates of vertices. In Section 6 we continue this exposition for use with the nightrider.

The bishop, rook, and queen are examples of _partial queens_. A partial queen Q_<sup>hk</sup>_ is a rider that has _h_ horizontal or vertical basic moves and _k_ basic moves at \(\pm 45^\circ\) to the horizontal (obviously, \(h,k\le 2\)). We studied partial queens in Part III.  2.1 contains a list of the partial queens with their names and what we know or believe about the periods of their counting quasipolynomials. We think four of the partial queens are uniquely special: we believe the rook, semirook, semibishop, and anassa are the only rider pieces that have period 1--that is, whose labelled counting functions are polynomials in _n_ for every number _q_ of copies. We do know from Theorem IV.2.3 that they are the only riders whose denominators equal 1.

While the number of nonattacking configurations of unlabelled pieces is _u_<sub>P</sub>(_q;n_), the counting is done with labelled pieces; that number is _o_<sub>P</sub>(_q;n_)=_q!u_<sub>P</sub>(_q;n_). Our task is to find the

\begin{tabular}{cccccccc}
_Name_ & (_h,k_) & _q_=2 & _q_=3 & _q_=4 & _q_=5 & _q_=6 & _q\>_6 \\
Semirook & (1,0) & 1 & 1 & 1 & 1 & 1 & 1 \\
Rook & (2,0) & 1 & 1 & 1 & 1 & 1 & 1 \\
Semibishop & (0,1) & 1 & 1 & 1 & 1 & 1 & 1 \\
Anassa & (1,1) & 1 & 1 & 1 & 1 & 1 & 1\* (_q_=7,8) \\
Bishop & (0,2) & 1 & 2 & 2 & 2 & 2 & 2 \\
Semiqueen & (2,1) & 1 & 1 & 2\* & 2\* & 6\* & 12<sup>?</sup> (_q_=7) \\
Trident & (1,2) & 1 & 2 & 6\* & 12<sup>?</sup> & 60<sup>?</sup> & 420<sup>?</sup> (_q_=7) \\
Queen & (2,2) & 1 & 2 & 6\* (6) & 60\* & 840<sup>\*\*</sup> & 360360\* (_q_=7) \\
\end{tabular}

2.1. The quasipolynomial periods (and denominators, when known) for partial queens Q_<sup>hk</sup>_. Denominators are defined in Section 6. All known periods equal the denominators.

\* is a number deduced from an empirical formula in \[12\].

\*\* is deduced from the empirical formula of Karaevaev; see \[11, 12\].

\* is a value we conjecture.

