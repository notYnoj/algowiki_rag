(iv) _For all positive integers x, y, z with z=x+y_-1_, we have_ \(x^{1-p}y^p\le F_\theta^\star(x,y,z)\le x^{p_2}y^p\).<tbc>

<tbc>_Proof._ We begin by showing some useful identities on the _p<sub>i</sub>_’s and \(\theta_i\)’s that we will use throughout the proof. For {_i,j,k_}={1,2,3}, we have \(p_i=\theta_i/(\theta_i+\theta_j\theta_k)\), so 0_\<p<sub>i</sub>\<_1. Moreover,<tbc>

\(p_i(1-\theta_j)+p_j(1-\theta_i)=(\theta_i+\theta_j)/(1-\theta_k)=1.\) (5.5)

<tbc>In particular, \(p_i+p_j=1+p_i\theta_j+p_j\theta_i>1\), and<tbc>

\((1-p_i)+p_i\theta_j=p_j(1-\theta_i).\) (5.6)

<tbc>Now set \(f(a,b):=F_\theta^\star(a,b,a+b-1)\) for real numbers \(a,b\ge 1\), and let \(A:=(a-\theta_1)/(1-\theta_1)\) and \(B:=(b-\theta_2)/(1-\theta_2)\). Then _A_ and _B_ are the numbers _A_<sub>1</sub> and _A_<sub>2</sub> of Definition 5.5. Since \(a,b\le a+b-1\) we take _k_=3 in Definition 5.5, which gives

\(f(a,b)=\left\{\begin{array}{ c c }
A^{1-p_1}\big(\theta_2A+(1-\theta_2)B\big)^{p_1} & \text{if}A\le B, \\
B^{1-p_2}\big(\theta_1B+(1-\theta_1)A\big)^{p_2} & \text{if}A>B.
\end{array}\right.\) (5.7)

We show the function _f_ is continuously differentiable. To start, both cases are equal whenever _A=B_, so _f_ is continuous. We compute the derivatives of the functions in the two cases of (5.7) at _A=B_, and show they are equal. We claim the derivatives in _a_ of both cases are equal to _p_<sub>2</sub>. For the second case this is directly clear. By the chain rule, the derivative in _a_ of the first case is equal to its derivative in _A_ divided by \(1-\theta_1\). This derivative in _A_ is equal to (1-_p_<sub>1</sub>)_A_<sup>-_p_<sub>1</sub></sup>_U_<sup>_p_<sub>1</sub></sup>+_p_<sub>1</sub>\(\theta_2A^{1-p_1}U^{p_1-1}\), where \(U=\theta_2A+(1-\theta_2)B\). When _A=B_ this equals \((1-p_1)+p_1\theta_2\), which is \(p_2(1-\theta_1)\) by (5.6). This proves the claim. By a symmetric argument, the derivatives in _b_ of both cases equal _p_<sub>1</sub>. We conclude _f_ is continuously differentiable.

We are now ready to prove the four items.

(i) Each case of (5.7) is a weighted geometric mean, with nonnegative weights of sum 1, and each factor is a convex combination of _A_ and _B_. Thus, \(f\ge min(A,B)\ge min(a,b)\), where the second inequality follows from \(A\ge a\) and \(B\ge b\). For the upper bound, the weighted AM-GM inequality and (5.6) give for the first case an upper bound of<tbc>

\((1-p_1)A+p_1\big(\theta_2A+(1-\theta_2)B\big)=p_2(1-\theta_1)A+p_1(1-\theta_2)B\)<br>
\(=p_2(a-\theta_1)+p_1(b-\theta_2).\)

By (5.5), this equals 1+_p_<sub>2</sub>(_a_-1)+_p_<sub>1</sub>(_b_-1), which is upper bounded by _a+b_-1 because _p_<sub>1</sub>_,p_<sub>2</sub>_\<_1. The second case is upper bounded in an analogous manner.<tbc>

<tbc>Finally, because _A_ and _B_ are affine functions that are nondecreasing in _a_ and _b_, each case of (5.7) is nondecreasing in _a_ and in _b_. Then because _f_ is continuous, _f_ is nondecreasing in each argument.<tbc>

(ii) Fix \(a\ge 1\), and let _g_:=_f_<sup>1_/p_<sub>1</sub></sup>. Because _B_ is an increasing affine function of _b_, it suffices to show that _g_ is concave as a function of the real number \(B\ge 1\). The same is then true for its restriction to the integers _b_. It furthermore suffices to show that _g_ is piece-wise concave, because _f_ and hence also _g_ is continuously differentiable.<tbc>

<tbc>For \(A\le B\), we have that \(g=A^{(1-p_1)/p_1}\big(\theta_2A+(1-\theta_2)B\big)\) is affine, and hence concave.<tbc>

<tbc>Now let _A\>B_. We have _g=B<sup>u</sup>L<sup>v</sup>_, where \(L:=\theta_1B+(1-\theta_1)A\), _u_:=(1-_p_<sub>2</sub>)_/p_<sub>1</sub> and _v_:=_p_<sub>2</sub>_/p_<sub>1</sub>. We will show that the second derivative of _g_ in _B_ is negative. A direct computation of the first and second derivatives w.r.t. _B_ gives<tbc>

\(\frac{\partial}{\partial B}g=uB^{u-1}L^v+\theta_1vB^uL^{v-1},\)<br>
\(\frac{\partial^2}{\partial B^2}g=B^{u-2}L^{v-2}\big(u(u-1)L^2+2uv\theta_1BL+v(v-1)\theta_1^2B^2\big).\)

