## A Exchanging input and output roles

We recall transposition of bilinear algorithms in the form used here; see \[BCS97, Chapter 14 and Section 13.3\]. For scalar lists, write \(\langle U,V\rangle=\sum_iU_iV_i\). For matrices or lists of matrices, the sum runs over all scalar entries. Number the left input, right input, and output as roles 1,2,3. Define _T_<sup>(12)</sup>(_Y,X_)=_T(X,Y_) and define the other exchanges by

\(\langle T^{(23)}(X,Z),Y\rangle=\langle T(X,Y),Z\rangle=\langle T^{(13)}(Z,Y),X\rangle.\)

For a map of the form (1), an exchange of coefficient roles means exchanging the corresponding scalar indices first, then extending the resulting formula to matrix coefficients. An exchange of an entire matrix computation also exchanges its matrix-entry indices.

**Lemma A.1** (Transposition)**.** _If_ \(T(X,Y)=\sum_jD_jS_j(E_jX,H_jY)\) _is a packing, then_

\(T^{(23)}(X,Z)=\sum_jH_j^\mathsf{T}S_j^{(23)}(E_jX,D_j^\mathsf{T}Z),\)<br>
\(T^{(13)}(Z,Y)=\sum_jE_j^\mathsf{T}S_j^{(13)}(D_j^\mathsf{T}Z,H_jY),\)<br>
\(T^{(12)}(Y,X)=\sum_jD_jS_j^{(12)}(H_jY,E_jX).\)

_The same assertions hold modulo_ \(\varepsilon\).

_Proof._ For fixed _X_, write _T<sub>X</sub>(Y_)=_T(X,Y_). Correctness is the linear-map identity \(T_X=\sum_jD_j(S_j)_{E_jX}H_j\). Transposing it gives the first formula. Fixing _Y_ gives the second, and exchanging the inputs gives the third. Each operation permutes the decoded coefficient array, preserving polynomiality in \(\varepsilon\) and its constant coefficient.

For ordinary matrix multiplication, the corresponding dimension changes follow directly from

\((AB)^\mathsf{T}=B^\mathsf{T}A^\mathsf{T},\langle AB,C\rangle=\langle A,CB^\mathsf{T}\rangle=\langle B,A^\mathsf{T}C\rangle.\)

Thus the exchanges (12),(23),(13) send the dimension triple (_p,q,r_) to (_r,q,p),(q,p,r),(p,r,q_), respectively, up to transposing the input or output matrices.

## B Removing the formal parameter

We state Bini’s amplification and interpolation argument \[Bin80\] in our packing notation and give the proof for completeness. It converts a packing modulo \(\varepsilon\) into an exact identity while making the interpolation cost negligible in the exponent.

**Lemma B.1** (Bini’s approximate-to-exact conversion \[Bin80\])**.** _Suppose matrix multiplication of side_ \(v\ge 2\) _has a packing modulo_ \(\varepsilon\) _using r scalar products, and the coefficients of its decoded map have degree at most D in_ \(\varepsilon\)_. For every positive integer h, there is an exact rational identity for matrix multiplication of side v<sup>h</sup> using at most_ (_hD_+1)_r<sup>h</sup> scalar products. Consequently, for every_ \(\tau>\mathrm{log}_vr\)_, there is such an identity at a finite side V with fewer than_ \(V^\tau\) _scalar products. The identity can be computed from the given packing._

