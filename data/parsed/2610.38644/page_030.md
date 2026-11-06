## B.6 Positive semidefiniteness

The positive semidefiniteness of eq. 66 follows immediately from its feature representation. For arbitrary points \(\{x_i\}_{i=1}^N\) and coefficients \(\{\alpha_i\}_{i=1}^N\),

\(\sum_{i=1}^N\sum_{j=1}^N\alpha_i\alpha_jk_{[a,b]}(x_i,x_j)=\mathbb{E}_c\left[\sum_{i,j}\alpha_i\alpha_j\phi_c(x_i)\phi_c(x_j)\right]\)<br>
\(=\mathbb{E}_c\left[\left(\sum_{i=1}^N\alpha_i\phi_c(x_i)\right)^2\right]\ge 0.\) (90)

Hence, the continuum-center construction defines a valid positive semidefinite kernel independently of the closed-form calculation.

## B.7 Differentiation of the mean kernel

For PDE applications, the essential quantity is not only _k_<sub>[_a,b_]</sub>(_x,y_) itself but its derivatives with respect to both arguments. Since the Gaussian feature and all of its derivatives are smooth, and the center support \[_a,b_\] is bounded, differentiation may be interchanged with integration:

\(\partial_x^p\partial_y^qk_{[a,b]}(x,y)=\frac{1}{b-a}\int_a^b\partial_x^p\phi_c(x)\partial_y^q\phi_c(y)dc.\) (91)

Equation 91 gives a direct mean interpretation of every differentiated kernel block.

For example,

\(\partial_x\phi_c(x)=-\frac{x-c}{\sigma^2}\phi_c(x),\) (92)

and

\(\partial_x^2\phi_c(x)=\left[\frac{(x-c)^2}{\sigma^4}-\frac{1}{\sigma^2}\right]\phi_c(x).\) (93)

Therefore,

\(\partial_x\partial_yk_{[a,b]}(x,y)=\mathbb{E}_c\left[\partial_x\phi_c(x)\partial_y\phi_c(y)\right],\) (94)

and similarly,

\(\partial_x^2\partial_y^2k_{[a,b]}(x,y)=\mathbb{E}_c\left[\partial_x^2\phi_c(x)\partial_y^2\phi_c(y)\right].\) (95)

For a differential operator L,

\(\boxed{\mathcal{L}_x\mathcal{L}_yk_{[a,b]}(x,y)=\mathbb{E}_c\left[(\mathcal{L}\phi_c)(x)(\mathcal{L}\phi_c)(y)\right].}\) (96)

Thus, the operator kernel used in the continuum-feature collocation method is precisely the mean Gram kernel of the operator-applied Gaussian features.

## B.8 Gaussian moment representation

Higher-order derivatives can be evaluated efficiently without repeatedly differentiating the error-function expression eq. 80. After completing the square, every mixed derivative reduces to finite combinations of Gaussian moments of the form

\(J_n(m)=\int_a^b(c-m)^nexp\left(-\frac{(c-m)^2}{\sigma^2}\right)dc.\) (97)

The first moments are

\(J_0=\frac{\sqrt{\pi}\sigma}{2}\left[erf\left(\frac{b-m}{\sigma}\right)-erf\left(\frac{a-m}{\sigma}\right)\right],\) (98)

and

\(J_1=\frac{\sigma^2}{2}\left[exp\left(-\frac{(a-m)^2}{\sigma^2}\right)-exp\left(-\frac{(b-m)^2}{\sigma^2}\right)\right].\) (99)

