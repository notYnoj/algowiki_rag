Here \(f'_r(y)=4/r+2y(1-1/W)\ge 0\), while _f<sub>r</sub>(W_)=0. Thus \(f_r(y)\le 0\), proving concavity within every sorting interval.

The first derivatives match at the endpoints of these intervals. To check this, suppose that _x_ passes an equal neighboring coordinate at positions _j,j_+1. At the crossing, _L<sub>j</sub>=L_<sub>_j_+1</sub>=_L_. With \(r=d+1-j\ge 2\), the part of the logarithmic derivative coming from these two factors on one side is

\(\frac{2}{rL}+\frac{2}{(r-1)rL}=\frac{2}{(r-1)L},\)

which is the derivative on the other side. All later factors have unchanged derivatives, and all earlier factors have derivative zero. The values also agree, since the equal factors have the same base. Several simultaneous ties can be treated by consecutive adjacent exchanges. Consequently the one-coordinate function is continuously differentiable, with nonincreasing derivative across all intervals. It is therefore globally nondecreasing and concave, and (5) holds throughout its interior.

At (1_,...,_1) every factor _L<sub>j</sub>/_2 is one. Increase the coordinates one at a time from 1 to _a<sub>i</sub>_, and integrate (5). This gives \(lnH_d(\mathbf{a})\le\sum_{i=1}^dlna_i\). Exponentiating proves \(H_d(\mathbf{a})\le\prod_{i=1}^da_i\). At (1_,...,_1_,b_) all factors except the last are one, while the last is _b_ with exponent _c<sub>d</sub>_=1. This proves the stated normalization. On the diagonal, every _L<sub>j</sub>_ equals (_d_+1)_a_-(_d_-1), which gives the last formula in the lemma.

For tripling, fix \(\mathbf{a}\in[1,\infty)^{d-1}\) and set \(M=max_{1\le i\le d-1}a_i\). For \(x\ge M\), the varying coordinate is last in the sorted list and has exponent _c<sub>d</sub>_=1. The remaining factors are independent of _x_. Hence there is a constant _K\>_0 such that<tbc>

\(H_d(\mathbf{a},x)=K(x+S/2)(x\ge M).\)

<tbc>Concavity implies \(H_d(\mathbf{a},h)\le K(h+S/2)\) also for \(1\le h<M\): the secant slope from _h_ to _M_ is at least the slope _K_ of the subsequent affine interval. Since \(S\ge M-1\) and \(h\ge 1\), the number 3_h+S_ is at least _M_. Therefore<tbc>

\(H_d(\mathbf{a},3h+S)=K(3h+3S/2)\ge 3H_d(\mathbf{a},h).\)

<tbc>Finally, fix _d_-1 coordinates equal to _m_. By (5), the function \(x\mapsto H_d(m,\dots,m,x)/x\) is nonincreasing. When \(x\ge m\), its numerator is

\(H_d(m,\dots,m,x)=B_m^{(d-1)/(d+1)}\left(x+\frac{(d-1)(m-1)}{2}\right),B_m=\frac{(d+1)m-(d-1)}{2}\ge m.\)

The ratio therefore tends to \(B_m^{(d-1)/(d+1)}\). Its value at \(t\ge 1\) is at least this limit, which proves \(H_d(m,\dots,m,t)\ge tm^{(d-1)/(d+1)}\).

## 5.4 A certificate and the barrier

We extend the comparison function from atoms to complete expressions. Full sums and products receive ordinary sums and products of values. For a partial sum, a power-sum expression accounts for its shared coordinates. The choice of this power will make the separation budget agree with the edge value.

**Definition 5.9** (operational certificate)**.** For an integer \(n\ge 3\), put _d=n_-1 and \(\eta_n=n/(2(n-1))\). On an atom C**<sub>x</sub>**, remove one largest entry of **x** and denote the remaining _d_ entries by **a**. Define<tbc>

\(\mathcal{V}_n(\mathsf{C}_\mathbf{x})=H_d(\mathbf{a})^{\eta_n}.\)

