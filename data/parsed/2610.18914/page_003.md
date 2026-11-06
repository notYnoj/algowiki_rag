and set it to zero on components with different _Y_ - and _Z_-labels. Extend by trilinearity. Each coefficient is polynomial in \(\varepsilon\). We will obtain this family by restricting _M+n_-1 copies of _A_.

Put \(\ell=M+n-1\), _Q=F[t]<sub>\<n</sub>_ and \(W=F[t]_{<\ell}\). Let<tbc>

\(\mu:P\otimes Q\longrightarrow W,\mu(p,q)=pq\)

<tbc>be ordinary multiplication, and let<tbc>

\(C_\mu(p,q,\psi)=\psi(pq)(p\in P,q\in Q,\psi\in W^\vee)\)

<tbc>be its trilinear form. For each _h_, define

\(g_h:Q\longrightarrow J[\varepsilon],q\longmapsto q(a_h+\varepsilon u),\iota_h:W\longrightarrow J[\varepsilon],f\longmapsto f(a_h+\varepsilon u).\)

Here and below maps with polynomial coefficients are extended linearly over the parameter ring when composed. Substitution preserves products, so

\(\sigma_h\circ(\mathrm{id}_P\otimes g_h)=\iota_h\circ\mu.\) (2.4)

This is the relation that connects our family to ordinary multiplication.

Work temporarily over \(F[\varepsilon,\varepsilon^{-1}]\), so that _g<sub>h</sub>_ is invertible. Pull back \(A\otimes C_\mu\) along the three maps

\(\alpha=\mathrm{id}_{X\otimes P},\)<br>
\(\beta=\oplus_h(\mathrm{id}_{Y_h}\otimes g_h^{-1}),\)<br>
\(\gamma=\oplus_h(\mathrm{id}_{Z_h}\otimes\iota_h^\vee).\)

The maps on the last two legs take \(\widetilde{Y}\) to \(\oplus_h(Y_h\otimes Q)\) and \(\widetilde{Z}\) to \(\oplus_h(Z_h\otimes W^\vee)\), respectively. On the _h_th component, the auxiliary pairing becomes

\((\iota_h^\vee\varphi)(\mu(p,g_h^{-1}j))=\varphi(\sigma_h(p,j))\)

by (2.4). Hence the pullback is precisely \(\Phi(\varepsilon)\), including its zero terms on unmatched components.

It remains to pay for \(C_\mu\). Choose \(\ell\) distinct points \(b_1,\dots,b_\ell\in F\). Evaluation at these points identifies _W_ with \(F^\ell\). Multiplication in _W_ can therefore be computed by evaluating the two inputs, multiplying their values at the \(\ell\) points, and interpolating the output. Thus

\(\ell\ge C_\mu,A^{\oplus\ell}\cong A\otimes\ell\ge A\otimes C_\mu.\)

Composing this fixed restriction with \(\alpha,\beta,\gamma\) gives Laurent-polynomial pullback maps from \(A^{\oplus\ell}\) whose result is the polynomial family \(\Phi(\varepsilon)\).

Finally, at \(\varepsilon=0\), equation (2.3) reads<tbc>

\(\Phi(0)(x\otimes p,y_h\otimes j,z_h\otimes\varphi)=p(a_h)A_h(x,y_h,z_h)\varphi(j).\)

<tbc>Under \(\mathrm{id}_X\otimes e:X\otimes P\cong\oplus_hX\), the _h_th block reads only the _h_th copy of _X_. Its other two spaces are already separate. Consequently

\(\Phi(0)\cong\oplus_h(A_h\otimes B_X(n)),\)

which proves the degeneration.

The construction uses no roots of unity and no division by factorials. The inverse of _g<sub>h</sub>_ is simply \(j(u)\mapsto j((t-a_h)/\varepsilon)\), using the representative of degree less than _n_ in _J_. In particular, its Laurent-polynomial form is valid in every characteristic. The family \(\Phi\) has degree at most min(_M_-1_,n_-1) in \(\varepsilon\), since powers _u<sup>n</sup>_ and higher vanish in _J_.

