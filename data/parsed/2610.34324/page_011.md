<tbc>The integral defining _q_ gives the analogous bound \(|q(w)-q(v)|\le Cd^{-2}|w-v|\). Interpolation from the net therefore costs at most _Cn_<sup>-3</sup>_d_<sup>-2</sup>=_Cn_<sup>-13/5</sup>, smaller than _n_<sup>-1/2</sup>_d_<sup>-1/4</sup>=_n_<sup>-9/20</sup>. This includes the real endpoints. Finally, _R_(<o>_w_</o>)=<o>_R(w_)</o> and _q_(<o>_w_</o>)=<o>_q(w_)</o> extend the same bound to the lower semicircle. The estimate consequently holds simultaneously on all of \(\Gamma\).

Both resolvents are analytic in a neighborhood of the closed disk on this event. Applying Cauchy’s formula to their difference multiplies its contour bound by at most _C<sub>j</sub>d_<sup>-(_j_-1)</sup> for the (_j_-1)-st derivative.

Since the (_j_-1)-st derivative of (_zI-W_)<sup>-1</sup> is (-1)<sup>_j_-1</sup>(_j_-1)!(_zI-W_)<sup>-_j_</sup>, we obtain, for _j_=3,4,

\([(zI-W)^{-j}]_{ii}=a_j+O_\prec(n^{-1/2}d^{3/4-j}),\)<br>
\(a_j=\int(z-x)^{-j}d\mu_\mathrm{sc}(x)\unknown d^{3/2-j}.\)

The last estimate follows by substituting 2-_x=dt_ and using the square-root density at the edge. These formulas serve two purposes: the case _j_=4 controls the diagonal normalization, while _j_=3 controls the objective through _WP=zP_-(_zI-W_)<sup>-3</sup>. Both have the same relative error. In particular,<tbc>

\(u:=\mathrm{max}_i|P_{ii}/a_4-1|=O_\prec(n^{-1/2}d^{-3/4})=O_\prec(n^{-7/20}).\)

<tbc>The diagonal normalization is therefore a small perturbation. Let _C<sub>D</sub>_=(_D/a_<sub>4</sub>)<sup>-1/2</sup>. Since \(\|C_D-I\|_\mathrm{op}=O(u)\) and \(P\unknown 0\), the trace norm satisfies

\(\|X-P/a_4\|_\mathrm{tr}=\|C_D(P/a_4)C_D-P/a_4\|_\mathrm{tr}\)<br>
\(\le O(u)\mathrm{tr}(P/a_4)=O(nu).\)

Using _WP=zP_-(_zI-W_)<sup>-3</sup> and \(\|W\|_\mathrm{op}=O(1)\) with high probability, we conclude that<tbc>

\(\frac{\langle W,X\rangle}{n}=z-\frac{a_3}{a_4}+O_\prec(n^{-7/20})\ge 2-Cd+O_\prec(n^{-7/20}).\)

<tbc>Indeed, the estimates \(a_3\unknown d^{-3/2}\) and \(a_4\unknown d^{-5/2}\) give \(0<a_3/a_4\le Cd\); together with _z_=2+_d_, this proves the last inequality. Moreover, \(\|X\|_\mathrm{op}\le\|P\|_\mathrm{op}/\mathrm{min}_iP_{ii}\le Cd^{-3/2}\), and therefore

\(\frac{\mathbf{1}^\top\mathbf{1}}{n^{3/2}}\le\frac{\|X\|_\mathrm{op}}{\sqrt{n}}\le Cn^{-1/5}.\)

The stochastic error is _o(n_<sup>-1/5</sup>) even after a sufficiently small fixed power loss. This proves (3).

_Comparing the two values._ It remains to make the errors smaller than the 1_/r_ loss in 2_c<sub>r</sub>_. Choose \(r=\lfloor c(n/(\mathrm{log}n)^3)^{1/7}\rfloor\). Then

\(r^2\sqrt{\frac{\mathrm{log}n}{n}}=o(1),rn^{-1/5}=o(1),\)<br>
\(rn^{-1/4}(r\mathrm{log}n)^{3/4}\le c^{7/4}.\)

Take _c\>_0 small enough that the constant in (2) times _c_<sup>7/4</sup> is less than 1/8. Equations (2)-(3) then give, with probability tending to one,

\(\mathrm{max}_{X\in\mathcal{E}_n\mathrm{rank}X\le r}F_n(X)\le M_r(W)\le n\left(2-\frac{1}{4r}\right)\)<br>
\(<\mathrm{max}_{X\in\mathcal{E}_n}F_n(X).\)

Every optimizer has rank greater than _r_, proving the theorem. □

