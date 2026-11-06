(_3)_ _The dual code_ \(C^\perp\) _is MDS._<tbc>

_(4)_ _The code C has a generator matrix in the systematic form G_=(_I<sub>K</sub>|A), where I<sub>K</sub> is the identity matrix_ \(K\times K\) _and A is a superregular matrix._

The Proposition 2.1 can also be extended to linear array MDS codes [_n,k,d_] by using superregular _b_-block matrices. Superregular matrices are not easy to find in general [8]. We will consider particular examples of superregular matrices, specifically the Vandermonde and Cauchy matrices [17,18].

Let \(\alpha_1,\dots,\alpha_{n-k}\) be nonzero elements in F_<sub>q</sub>_. A general form of a Vandermonde matrix \(A\in\mathbb{F}_q^{k\times(n-k)}\) is given by

\(A=\left[\begin{array}{ c c c c }
1 & 1 & \dots & 1 \\
\alpha_1 & \alpha_2 & \dots & \alpha_{n-k} \\
\alpha_1^2 & \alpha_2^2 & \dots & \alpha_{n-k}^2 \\
\vdots & \vdots & \ddots & \vdots \\
\alpha_1^{k-1} & \alpha_2^{k-1} & \dots & \alpha_{n-k}^{k-1}
\end{array}\right].\) (2.3)

We emphasize that, over finite fields, a Vandermonde matrix is not automatically superregular; this property depends on the choice of evaluation points and must be verified.

**Definition 2.3.** Let _x<sub>i</sub>_ and _y<sub>j</sub>_ elements in a field F, for \(i=1,\cdots,m\) and \(j=1,\cdots,n\). A matrix _A_ of dimensions \(m\times n\) is called **Cauchy matrix**, if and only if,

\(A_{ij}=\frac{1}{x_i+y_j},\) (2.4)

where \(x_i+y_j\neq\mathbf{0}\), _x<sub>i</sub>_ are distinct for all \(i=1,\cdots,m\) and _y<sub>j</sub>_ are distinct for all \(j=1,\cdots,n\).

**Definition 2.4.** Let \(p(x)=x^b+p_{b-1}x^{b-1}+\dots+p_1x+p_0\in\mathbb{F}_q[x]\) be a primitive polynomial. We can associate _p(x_) with a matrix called **Frobenius companion matrix** _C_, which is a matrix that contains 1’s (ones) in the sub-diagonal, the coefficients of -_p(x_) in the last column and all other elements being zero, as follows

\(C=\left[\begin{array}{ c c c c }
0 & 0 & \dots & 0 & -p_0 \\
1 & 0 & \dots & 0 & -p_1 \\
\vdots & \ddots & \ddots & \vdots & \vdots \\
0 & 0 & \dots & 0 & -p_{b-2} \\
0 & 0 & \dots & 1 & -p_{b-1}
\end{array}\right].\) (2.5)

**Definition 2.5.** If \(\alpha\) is a primitive element of a finite field F_<sub>q</sub>_, then the **Zech logarithm** _Z_ of an integer _n_ with respect to the base \(\alpha\) is defined by the equation

\(Z(n)=log_\alpha(1+\alpha^n)\Longleftrightarrow\alpha^{Z(n)}=1+\alpha^n,\) (2.6)

where the result of logarithm is limited to the field.

Some properties of this logarithm can be found in [12]. The sum of powers of a primitive element \(\alpha\) can be done alternatively using the Zech logarithm. Let \(\alpha^x\) and \(\alpha^y\) be primitive elements of F_<sub>q</sub>_. If _z_ is the exponent of the sum \(\alpha^x+\alpha^y\), that is, \(\alpha^x+\alpha^y=\alpha^z\), then

\(z=x+Z(y-x)=y+Z(x-y).\) (2.7)

