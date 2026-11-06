<tbc>where now _V<sub>m</sub>_, _T_<sub>_m_+1_,m_</sub> and _T<sub>m</sub>_ obey relation (3.4). Computationally, we obtain short recurrences for the iterates _x<sub>m</sub>_ by updating factorizations of _T<sub>m,m</sub>_ and _T_<sub>_m_+1_,m_</sub> just as in the non-flexible case; see the discussion at the end of section 2. Commented Matlab implementations of FMR and FGAL are available from the authors on request.

Note that the FGAL iterates do not fulfill a strict _H_<sup>-1</sup>-orthogonality relation for the residuals, nor do the FMR iterates minimize the _H_<sup>-1</sup>-norm of the residual exactly. But, of course, if we solve for _H_ exactly in the flexible Lanczos process, FGAL and FMR reduce to right preconditioned counterparts of \(\ell\)FOM and \(\ell\)MR from (2.3) and (2.4), respectively.

A flexibly preconditioned CG method (FCG) for Hermitian positive definite matrices using a preconditioner which may change from one iteration to the next has been proposed in [8] and further analyzed in [16]. The FGAL method can be used in this situation, too, with \(\sigma=0\). FCG and FGAL are similar in spirit but not identical: FCG constructs search directions by applying the variable preconditioner to the current residual and then _A_-orthogonalizing against a fixed number _s_ of the previous search directions. In contrast, FGAL orthogonalizes the next preconditioned Lanczos vector in the \(\ell_2\)-inner product against the two previous ones. This is different, even when _s_=2.

**4. Properties.** In this section we first state two known convergence bounds for the left preconditioned methods where systems with _H_ are solved exactly. We then show that a result from [5] can be used to improve one of these bounds, a fact that seems to have gone unnoticed so far. We continue the section considering the flexible variants for which we establish two somewhat more basic but algorithmically important properties.

Theorem 4.1. _Let_ \(\lambda\ge 0\) _be the smallest value such that the interval_ \([-i\lambda,i\lambda]\) _contains all the (purely imaginary) eigenvalues of the H-anti-selfadjoint matrix H_<sup>-1</sup>_S and let x_<sub>∗</sub> _denote the solution of the system Ax=b. Then_

(_i)_ _For the_ \(\ell\)_GAL iterates x<sub>m</sub> from_ (2.1) _we have_<tbc>

<tbc>\(\|x_{2m}-x_*\|_H\le\|x_0-x_*\|_H\cdot 2\left(\frac{\sqrt{1+\lambda^2}-1}{\sqrt{1+\lambda^2}+1}\right)^m\)<tbc>

<tbc>_and_<tbc>

<tbc>\(\|x_{2m+1}-x_*\|_H\le\|x_1-x_*\|_H\cdot 2\left(\frac{\sqrt{1+\lambda^2}-1}{\sqrt{1+\lambda^2}+1}\right)^m.\)<tbc>

(_ii)_ _For the_ \(\ell\)_MR residuals r<sub>m</sub>=b-Ax<sub>m</sub> from_ (2.2) _we have_<tbc>

<tbc>\(\|b-Ax_m\|_{H^{-1}}\le\|b-Ax_0\|_{H^{-1}}\cdot 2\left(\frac{\lambda}{\sqrt{1+\lambda^2}+1}\right)^m.\)<tbc>

<tbc>Part (i) of the theorem goes back to [4, 11, 25], and part (ii) to [25]; see [9] for a detailed discussion. What seems to have gone unnoticed so far is that a better bound for the \(\ell\)MR iterates results from [5, Theorem 4], adapted to _H_-selfadjoint matrices. We first formulate the result for an arbitrary value for the shift \(\sigma\) before comparing to Theorem 4.1(ii). Note that the original theorem in [5] considers residuals for the matrix \(i\sigma I+W\) with _W_ Hermitian and the \(\ell_2\)-norm. For the residuals belonging to matrices \(i\sigma I+W\) with _WH_-selfadjoint it holds in exactly the same manner, but now<tbc>

