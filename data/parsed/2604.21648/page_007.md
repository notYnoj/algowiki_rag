(_1)_ \(\Pi_A\) _is B-orthogonal._<tbc>

(_2)_ \(\Pi_A^+=\Pi_A\).<tbc>

_(3)_ \(\mathcal{R}(\Pi)^{\perp_B}=\mathcal{N}(\Pi_A)\).<tbc>

_(4)_ \(\|\Pi_A\|_B=\|I-\Pi_A\|_B=1\).<tbc>

_(5)_ R(_BP_)=R(_A<sup>H</sup>R)._<tbc>

_(6)_ R(_P_)=R(_B_<sup>-1</sup>_A<sup>H</sup>R)._<tbc>

_(7)_ N(_R<sup>H</sup>A_)=N(_P<sup>H</sup>B)._

In \[2\] condition (6) is used to obtain a _B_-orthogonal coarse-grid correction. There, given a restriction \(R\in\mathbb{C}^{n\times n_c}\) of full rank, the corresponding interpolation that yields a _B_-orthogonal coarse-grid correction is defined as _P_<sub>∗</sub>=_B_<sup>-1</sup>_A<sup>H</sup>R_. Conversely, given \(P\in\mathbb{C}^{n\times n_c}\), the corresponding restriction is defined as _R_<sub>∗</sub>=_A_<sup>-_H_</sup>_BP_. Both operators require the inverse of either _A<sup>H</sup>_ or _B_ which can be problematic. Examples for _P_<sub>∗</sub> and _R_<sub>∗</sub> for special cases of _B_ are discussed in \[2\]. However, when using _P_<sub>∗</sub> or _R_<sub>∗</sub> we obtain

(3.1) \(\Pi_A(P_*,R)=\Pi_A(P,R_*)=P_*(P_*^HBP_*)^{-1}P_*^HB=\Pi_B(P_*,P_*).\)

Choosing _P_<sub>∗</sub> symmetrized the coarse-grid correction in the sense that \(\Pi_B(P_*,P_*)\) has the same structure as \(\Pi_A(P,P)\) in the HPD case. This is no coincidence as for _A=B_ HPD we have _P_<sub>∗</sub>=_R_ and \(\Pi_B(P_*,P_*)\) becomes \(\Pi_A(P,P)\). Note that any interpolation _P_ or restriction _R_ can be multiplied by any nonsingular matrix \(S\in\mathbb{C}^{n_c\times n_c}\) from the right without changing the resulting coarse-grid correction. The spaces R(_P_) and R(_R_) are independent of their choice of bases. Hence, any two operators _P_<sub>1</sub>_,P_<sub>2</sub> or _R_<sub>1</sub>_,R_<sub>2</sub> with R(_P_<sub>1</sub>)=R(_P_<sub>2</sub>) or R(_R_<sub>1</sub>)=R(_R_<sub>2</sub>) produce the same coarse-grid correction. This is especially true for _P_<sub>∗</sub> and _R_<sub>∗</sub> which already shows that there does not exist a unique pair of operators (_P,R_) that results in a _B_-orthogonal coarse-grid projection.<br>
The main advantage of using _P_<sub>∗</sub> or _R_<sub>∗</sub> is the fact that \(\Pi_A(P_*,R)\) and \(\Pi_A(P,R_*)\) are _B_-orthogonal for any HPD matrix _B_. This does not contradict Theorem 2.9 (5) and (2.2) where all possible HPD matrices _B_ such that \(\Pi_A\) can be _B_-orthogonal are characterized, because changes in _B_ result in different operators _P_<sub>∗</sub> and _R_<sub>∗</sub> and thus different \(\Pi_A\). Note, that \(\Pi_A\) is _B_-orthogonal if and only if \(I-\Pi_A\) is _B_-orthogonal.

**3.2. The iteration matrices.** The algebraic two-grid methods and its error propagation matrix consist of pre- and post-smoothing steps combined with the coarse-grid correction. In our framework we consider the two error propagation operators

(3.2) \(E_+^{\nu_1,\nu_2}:=E_+^{\nu_1,\nu_2}(P,R):=(I-(M^{-1}A)^+)^{\nu_2}(I-\Pi_A(P,R))(I-M^{-1}A)^{\nu_1},\)

(3.3) \(E^{\nu_1,\nu_2}:=E^{\nu_1,\nu_2}(P,R):=(I-M^{-1}A)^{\nu_2}(I-\Pi_A(P,R))(I-M^{-1}A)^{\nu_1}.\)

If the dependency of _R_ and _P_ is clear from the context, we simply write \(E_+^{\nu_1,\nu_2}\) and \(E^{\nu_1,\nu_2}\). The exponents \(\nu_1,\nu_2\in\mathbb{N}_0\) are the number of pre- and post-smoothing steps, respectively, and \(M^{-1}\in\mathbb{C}^{n\times n}\) is the smoother which we always assume to be nonsingular. An obvious differences between the two operators is the _B_-adjoint of _M_<sup>-1</sup>_A_ in the post-smoothing step of \(E_+^{\nu_1,\nu_2}\) which introduces the additional dependency of _B_ into the operator.<br>
Since \(\Pi_A\) is a projection, we can always split up both error propagation operators

(3.4) \(E_+^{\nu_1,\nu_2}=E_+^{0,\nu_2}\cdot E_+^{\nu_1,0}\text{and}E^{\nu_1,\nu_2}=E^{0,\nu_2}\cdot E^{\nu_1,0}.\)

