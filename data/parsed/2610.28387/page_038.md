## B.6 Conditional order-three kernel with one fixed pair

We obtain the first projection by conditioning directly on the relative ranks of the three observations, as in the preceding subsection. Fix _Z_<sub>1</sub>=_z_=(_x,y_), write _u<sub>y</sub>=F<sub>Y</sub>(y_), and for a generic pair (_X,Y_) put _W=F<sub>Y</sub>(Y_); for the pair _Z_<sub>2</sub>, _W=F<sub>Y</sub>(Y_<sub>2</sub>). In \(3H_3^{[XY]}(Z_1,Z_2,Z_3)\), the coefficient of _x_ is 1, -2, or 1 according as _y_ is smallest, middle, or largest among the three _Y_ values. Since _Y_<sub>2</sub>_,Y_<sub>3</sub> are iid, its conditional mean equals<tbc>

\((1-u_y)^2-4u_y(1-u_y)+u_y^2=6u_y^2-6u_y+1=P_2(u_y).\)

<tbc>Next fix _Z_<sub>2</sub>=(_X_<sub>2</sub>_,Y_<sub>2</sub>) and average over the position of _Y_<sub>3</sub>. For _Y_<sub>2</sub>_\<y_, the coefficient of _X_<sub>2</sub> in \(3H_3^{[XY]}\) has conditional expectation -2_W_+(1-_W_)=1-3_W_; for _Y_<sub>2</sub>_\>y_, it is _W_-2(1-_W_)=3_W_-2. The same contribution arises from _X_<sub>3</sub> by symmetry. Consequently,

\(3M_{3,1}^{[XY]}(x,y)=xP_2(u_y)+2\mathbb{E}[X\{(1-3W)\mathbf{1}(Y<y)+(3W-2)\mathbf{1}(Y>y)\}]\)<br>
\(=xP_2(u_y)+\mathbb{E}\big[X(2-6W)\big]+\mathbb{E}\big[X(12W-6)\mathbf{1}(Y>y)\big].\)

Here _R<sub>X</sub>_ and _K<sub>X</sub>_ are defined in (3.9). Since \(P'_2(w)=12w-6\) and \(2\lambda_3^{[XY]}=\mathbb{E}\{X(12W^2-12W+2)\}\),<tbc>

\(\mathbb{E}\big[X(2-6W)\big]=2\lambda_3^{[XY]}-K_X,\mathbb{E}\big[X(12W-6)\mathbf{1}(Y>y)\big]=R_X(y),\)

<tbc>where continuity of _Y_ makes _Y\>y_ and \(Y\ge y\) equivalent inside the expectation. Hence

\(M_{3,1}^{[XY]}(x,y)=\frac{1}{3}\{xP_2(u_y)+2\lambda_3^{[XY]}+R_X(y)-K_X\},\)

which establishes (3.10). All calculations have direct reverse-coordinate analogues.

## B.7 Independence covariance: all entries from finite rank sums

Under \(X\perp Y\) , the _Y_ -rank permutation is independent of the _X_ sample. Conditional on that permutation, _X_<sub>\[_q:n_\]</sub> is a fixed relabeling of _X_<sub>1</sub>_,...,X<sub>n</sub>_. Hence the concomitants _X_<sub>\[1:_n_\]</sub>_,...,X_<sub>\[_n:n_\]</sub> are iid with distribution _F<sub>X</sub>_ (David and Nagaraja, 2003). Accordingly,<tbc>

\(\mathrm{Var}(\widehat{\lambda}_m^{[XY]})=\mathrm{Var}(X)\sum_{q=1}^nw_{m,q}^2,\mathrm{Cov}(\widehat{\lambda}_2^{[XY]},\widehat{\lambda}_3^{[XY]})=\mathrm{Var}(X)\sum_qw_{2,q}w_{3,q}.\)

<tbc>We compute these finite sums without asymptotic approximations. Put _z<sub>q</sub>=q_-(_n_+1)/2 and _h=n_<sup>2</sup>-1. The centered power sums are<tbc>

\(\sum_{q=1}^nz_q=0,\sum_{q=1}^nz_q^2=\frac{nh}{12},\sum_{q=1}^nz_q^4=\frac{nh(3n^2-7)}{240}.\)

