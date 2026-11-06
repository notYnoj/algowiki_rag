Since all of them are nonzero, errors occurred in the information symbols. So, this example falls on Case 4. The algorithm is followed by assuming a second error in _l_<sub>2</sub>=2. So we have to test the Equation (4.8) through the calculations of _r_<sub>_i_-2</sub> as in (4.9), for _i_=3,4:

\(r_1=\sigma(3,2)-\sigma(2,2)+Z(\sigma(3,1)-\sigma(3,2)-\sigma(2,1)+\sigma(2,2))-Z(\sigma(2,1)-\sigma(2,2)\)<br>
\(-\sigma(1,1)+\sigma(1,2))=10-12+Z(5-10-11+12)-Z(11-12-12+11)\)<br>
\(=-2+Z(-4)-Z(-2)=5,\)

and

\(r_2=\sigma(4,2)-\sigma(3,2)+Z(\sigma(4,1)-\sigma(4,2)-\sigma(3,1)+\sigma(3,2))-Z(\sigma(3,1)-\sigma(3,2)\)<br>
\(-\sigma(2,1)+\sigma(2,2))=4-10+Z(1-4-5+10)-Z(5-10-11+12)\)<br>
\(=-6+Z(2)-Z(-4)=-6+9-14=-11.\)

Then

\(\mathbf{y}_3^T\neq C^5\mathbf{y}_2^T\text{and}\mathbf{y}_4^T\neq C^{-11}\mathbf{y}_3^T.\)

As for _l_<sub>2</sub>=2 the above equations fail we test to _l_<sub>2</sub>=3,

\(r_1=\sigma(3,3)-\sigma(2,3)+Z(\sigma(3,1)-\sigma(3,3)-\sigma(2,1)+\sigma(2,3))-Z(\sigma(2,1)-\sigma(2,3)\)<br>
\(-\sigma(1,1)+\sigma(1,3))=11-5+Z(5-11-11+5)-Z(11-5-12+10)\)<br>
\(=6+Z(-12)-Z(4)=7\)

and

\(r_2=\sigma(4,3)-\sigma(3,3)+Z(\sigma(4,1)-\sigma(4,3)-\sigma(3,1)+\sigma(3,3))-Z(\sigma(3,1)-\sigma(3,3)\)<br>
\(-\sigma(2,1)+\sigma(2,3))=9-11+Z(1-9-5+11)-Z(5-11-11+5)\)<br>
\(=-2+Z(-2)-Z(-12)=-2+7-4=1.\)

Then we confirm that

\(\mathbf{y}_3^T=C^7\mathbf{y}_2^T\text{and}\mathbf{y}_4^T=C^1\mathbf{y}_3^T.\)

Therefore, there are errors in positions _l_<sub>1</sub>=1 and _l_<sub>2</sub>=3. In order to obtain the magnitude of the errors we solve the linear system from (4.10) and we obtain the errors

\(\mathbf{e}_1=[0110]\text{and}\mathbf{e}_3=[1110].\)

And so, the codeword is

\(\mathbf{c}=[10110101011001100010110111001]\)<br>
\(-[\mathbf{0110}000\mathbf{1110}00000000000000000]\)<br>
\(=[1101010101100110011000101101110011].\)

One of the main computational challenges of Algorithm 2, as analyzed in Theorem 4.1, arises in Case 4, where it is necessary to compute the quantities in (4.26) in order to substitute them into (4.25). The following corollary provides a direct expression for these terms when _A_ is a superregular Vandermonde matrix.

**Corollary 4.1.** _If A is superregular a Vandermonde matrix and_ \(H=\left[\psi(A)|I_{(n-k)b}\right]\) _follows the construction in Theorem 3.1, then Equation (4.26) simplifies to_

\(r_{i-2}=l_2,\) (4.27)

_for all i_=3,4_,...,m, where l_<sub>2</sub> _is the position of the second error._

