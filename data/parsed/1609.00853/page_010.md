<tbc>The fact that _s(n_+1_,n_+1-_q_) is a polynomial in _n_ of degree 2_q_ follows from Schlömlch’s formula (3.4) and is well known (see e.g. \[9\]). We give a proof here which we believe to be new, using Ehrhart theory in the spirit of our chess series. We do not know a prior reference for the fact that the coefficients themselves are polynomials.

_Proof._ We prove both propositions together.

The \(n\times n\) integral right triangle board has _n_ diagonals (parallel to the hypotenuse) of lengths 1,2_,...,n_, each of which can have at most one semibishop. The number of ways to place _q_ labelled semibishops is the sum of all products of _q_ of these _n_ values, i.e., the elementary symmetric function _e<sub>q</sub>_(1,2_,...,n_), which equals |_s(n_+1_,n_+1-_q_)|. That proves Proposition 4.4.

Next, we prove _s(n_+1_,n_+1-_q_) is a polynomial function of _n_. Proposition IV.3.1 applies because the semibishop is a one-move rider. The corners of the triangular board T are (0,0), (1,1), and (0,1). For the move (1,1), their antipodes are the opposite points of the boundary along the \(45^\circ\) diagonal. The corner (0,1) has no antipode while the corners (0,0) and (1,1) serve as each other’s antipodes. Thus, every vertex is integral and the denominator _D_(T_<sup>q</sup>,_A<sub>Q<sup>01</sup></sub>)=1, so _q!u_<sub>Q<sup>01</sup></sub>(_q;n_) is a polynomial in _n_.

Finally, Theorem I.4.2 says that the coefficients are polynomials in _q_ with the stated degrees. □

## 5. The Queen and Its Less Hardy Sisters

There are four pieces in this section: the queen, and three others that are like defective queens without being similar to bishops or rooks, which we call the semiqueen, the trident, and the anassa. As they are all partial queens, counting formulas for _q_=2,3 are special cases of our Theorems III.4.1 and III.4.2 and are presented in s III.4.1 and III.4.2. The four leading coefficients of the general counting polynomial are implied by Theorems III.3.1, III.4.2, and III.4.2; see s III.3.1 and III.3.2. All our formulas that were also calculated by Kotˇcešovec in \[12\] agree with his.

Let \(\zeta_r:=e^{2\pi i/r}\) be a primitive _r_-th root of unity. We index the Fibonacci numbers _F<sub>i</sub>_ so that _F_<sub>0</sub>=_F_<sub>1</sub>=1.

### 5.1. The queen.

