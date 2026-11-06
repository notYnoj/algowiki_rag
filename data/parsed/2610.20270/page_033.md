## G.1 Full order: proof of Theorem 6.1

_Proof of Theorem 6.1._ Define the point indicators \(\ell_a(x):=2^{-n}\prod_{i=1}^n(1+a_ix_i)=2^{-n}\sum_{T\subseteq[n]}a^Tx^T\). Modulo _I_<sub>B</sub>, \(\ell_a^2\equiv\ell_a\) and \(\sum_a\ell_a\equiv 1\). At full order the moment PSD condition tests the square of every Boolean function, so \(\pi_a:=L_y(\ell_a)=L_y(\ell_a^2)\ge 0\) and \(\sum_a\pi_a=1\); the interpolation identity \(h\equiv\sum_ah(a)\ell_a\) gives \(L_y(h)=\sum_a\pi_ah(a)\), i.e. the simplex representation. The vectors _b<sub>n</sub>(a_) are mutually orthogonal because \(b_n(a)^\top b_n(b)=\prod_i(1+a_ib_i)=2^n\mathbf{1}_{\{a=b\}}\), which proves uniqueness of the coefficients and, for uniquely minimized _f_, uniqueness of the optimizer \(b_n(x_\star)b_n(x_\star)^\top\).

For upward persistence, let _d_<sub>0</sub> be an order at which _f_ is uniquely rank-one exact and let \(d_0<d\le n\). An order-_d_ optimizer truncates to an order-_d_<sub>0</sub> feasible matrix with the same objective value, since \(\mathrm{deg}f\le 2d_0\). Hierarchy monotonicity and the feasible lift of _x<sub>⋆</sub>_ give \(p_{d_0}(f)\le p_d(f)\le f(x_\star)=p_{d_0}(f)\). So the truncation is the unique lower-order optimum; in particular _y_<sub>{_i_}</sub>=_x<sub>⋆,i</sub>_ for all _i_. Choose Gram vectors _g<sub>A</sub>_ of the higher-order optimizer with \(\langle g_A,g_B\rangle=y_{A\triangle B}\) and \(\|g_A\|=1\). Whenever \(A,A\triangle\{i\}\in\mathcal{I}_d\), \(\langle g_A,g_{A\triangle\{i\}}\rangle=x_{\star,i}\in\{\pm 1\}\), so equality in Cauchy-Schwarz gives \(g_{A\triangle\{i\}}=x_{\star,i}g_A\). Adding the elements of _A_ one at a time gives \(g_A=x_\star^Ag_\emptyset\). Hence the optimizer is \(b_d(x_\star)b_d(x_\star)^\top\).

For the certificate: with _g_:=_f-f(x<sub>⋆</sub>_) and _c<sub>a</sub>_:=2<sup>-_n_</sup>_b<sub>n</sub>(a_), set

\(S_\mathrm{full}:=\sum_{a\neq x_\star} g(a)c_ac_a^\top.\) (G.1)

One has \(b_n(x)^\top c_ac_a^\top b_n(x)\equiv\ell_a(x)^2\), so _S_<sub>full</sub> represents \(\sum_{a\neq x_\star} g(a)\ell_a^2\equiv\sum_ag(a)\ell_a\equiv g\); all displayed weights _g(a_) are positive by unique minimality, and orthogonality of the _b<sub>n</sub>(a_) gives ker(_S_<sub>full</sub>)=span{_b<sub>n</sub>(x<sub>⋆</sub>_)}.

## G.2 Fixed-order cells: proof of Theorem 6.2

Recall the cells of §6: for _u=b<sub>d</sub>(a_),

\(\mathcal{Q}(a,d):=\{g\in\mathcal{P}_{\le 2d}:g(a)=0\},\mathcal{E}(a,d):=\big\{g\in\mathcal{Q}(a,d):\mathrm{argmin}_{X\in\mathcal{X}_d}\langle C_g,X\rangle=\{uu^\top\}\big\},\mathcal{E}_\mathrm{sc}(a,d):=\{g\in\mathcal{Q}(a,d):\exists S\unknown 0,\mathcal{G}_d(S)=g,\mathrm{ker}(S)=\mathrm{span}\{u\}\}.\text{(G.2)}\)

Suppose a certificate _S_ of E<sub>sc</sub>(_a,d_) exists. Every feasible _X_ has value \(\langle S,X\rangle\ge 0\), while \(uu^\top\) has value zero. Equality forces \(\mathrm{ran}(X)\subseteq\mathrm{ker}(S)=\mathrm{span}\{u\}\), and \(X_{\emptyset,\emptyset}=1\) then gives \(X=uu^\top\). Hence \(\mathcal{E}_\mathrm{sc}(a,d)\subseteq\mathcal{E}(a,d)\). In particular, the definition of E<sub>sc</sub>(_a,d_) may ask only that some PSD Gram matrix with kernel span{_u_} represents _g_; optimality is automatic.

The family (6.1) gives a linear right inverse of G_<sub>d</sub>_ on Q(_a,d_). Each \(w_\Gamma\) satisfies \(w_\Gamma^\top u=0\) and \(\mathcal{G}_d(w_\Gamma w_\Gamma^\top)=\psi_\Gamma:=2(1-a^\Gamma x^\Gamma)\). The |I<sub>2_d_</sub>|-1 polynomials \(\psi_\Gamma\) form a basis of Q(_a,d_). Define the section \(\mathscr{B}_{a,d}(\sum_\Gamma t_\Gamma\psi_\Gamma):=\sum_\Gamma t_\Gamma w_\Gamma w_\Gamma^\top\). It obeys G_<sub>d</sub>_(B<sub>_a,d_</sub>(_h_))=_h_ and B<sub>_a,d_</sub>(_h)u_=0. Since \(t_\Gamma=-a^\Gamma h_\Gamma/2\) and \(\|w_\Gamma w_\Gamma^\top\|_\mathrm{op}=2\),

\(\|\mathscr{B}_{a,d}(h)\|_\mathrm{op}\le\sum_{\Gamma\neq\emptyset}|h_\Gamma|\le\sqrt{|\mathcal{I}_{2d}|-1}\|h\|_\mathrm{coef},\) (G.3)

where \(\|h\|_\mathrm{coef}\) is the Euclidean norm of the coefficient vector. By the split convention of §6, \(w_A=e_A-a^Ae_\emptyset\), and these _N_-1 vectors are orthogonal to _u_ and linearly independent. Hence the interior certificate _S_<sub>int</sub> of (6.1) satisfies \(S_\mathrm{int}\unknown 0\), ker(_S_<sub>int</sub>)=span{_u_}, and G_<sub>d</sub>(S_<sub>int</sub>)=_r<sub>a,d</sub>_:=2\(\sum_{\emptyset\neq A\in\mathcal{I}_d}(1-a^Ax^A)\). In particular \(r_{a,d}\in\mathcal{E}_\mathrm{sc}(a,d)\), so the cell is nonempty.

