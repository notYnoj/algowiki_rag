_Proof._ The zero target is trivial. For a fixed integer \(N\ge 2\), put \(D_i=\lceil N^{h_i}\rceil\) and \(M_N=\otimes_iB_i(D_i)\). Since \(D_i\le 2N^{h_i}\) and \(0\le p_i\le 1\), every character satisfies<tbc>

\(\lambda(M_N)=\prod_iD_i^{p_i}\le 8N\sum_ih_ip_i\le 8N^E.\)

<tbc>Theorem 3.2 therefore gives

\(\widetilde{R}(M_N)\le 8N^E.\) (26)

Fix any positive exponent slack \(\eta\). First choose _N_ so large that \(8<N^{\eta/2}\). The infimum defining \(\widetilde{R}(M_N)\) then gives a fixed integer _K_ and an exact rank decomposition with

\(R:=rank(M_N^{\otimes K})\le N^{K(E+\eta)}.\)

This is a finite bilinear algorithm for matrix dimensions \((D_Y^K,D_Z^K,D_X^K)\). Apply it recursively \(\ell\) times to blocks. By (3), the resulting dimensions are \((D_Y^{K\ell},D_Z^{K\ell},D_X^{K\ell})\) and there are \(R^\ell\) scalar multiplications.

Each input and output dimension, viewed as a number of scalar entries, is at most _R_, by the corresponding matrix-rank lower bound. Thus the linear substitutions and additions over all recursion levels use \(O(\ell R^\ell)\) operations. Given input size _n_, choose \(\ell=\lceil log_Nn/K\rceil\) and pad to these dimensions. They cover the target shape because \(D_i^{K\ell}\ge n^{h_i}\), while \(R^\ell=O(n^{E+\eta})\). This proves the bound for every positive slack, and hence the lemma under our exponent convention. All choices of _N_, _K_, and the finite identity precede the limit \(n\rightarrow\infty\).

It remains to bound these weighted sums using the angular constraint.

_Proof of Theorem 1.1._ Reorder the character’s dot-product parameters so that the objective is _ap_<sub>1</sub>+_bp_<sub>2</sub>+_cp_<sub>3</sub>, and write \(p_i=cos^2\theta_i\) with \(\theta_i\in[0,\pi/2]\). By Proposition 5.2, their sum is at least \(\pi/2\). Decreasing angles to make the sum exactly \(\pi/2\) only increases the objective, so it suffices to bound that case. If _b_=0, then _c_=0 and the objective is at most _a_.

For _a,b,c\>_0, put \(\beta_i=2\theta_i\) and<tbc>

\(u=\sqrt{\frac{bc}{a}},v=\sqrt{\frac{ac}{b}},w=\sqrt{\frac{ab}{c}}.\)

<tbc>Thus _vw=a_, _wu=b_, _uv=c_, and \(\beta_1+\beta_2+\beta_3=\pi\). Wolstenholme’s inequality \[8, Equation (1)\], applied with weights _u,v,w_, gives<tbc>

\(2(acos\beta_1+bcos\beta_2+ccos\beta_3)\le u^2+v^2+w^2.\)

<tbc>The inequality also holds at zero angles by continuity. Since \(p_i=(1+cos\beta_i)/2\), it gives

\(ap_1+bp_2+cp_3\le\frac{a+b+c}{2}+\frac{1}{4}\left(\frac{ab}{c}+\frac{ac}{b}+\frac{bc}{a}\right).\)

For _a,b\>_0, set \(c_0=\frac{ab}{a+b}\). If \(0\le c\le c_0\), replace _c_ in the objective by _c_<sub>0</sub>, which only increases it. The displayed bound at _c_<sub>0</sub> equals _a+b_. This proves both branches, including _c_=0.

We have bounded the objective for every tensor character. Lemma 6.1, with target **h**=(_c,a,b_), gives (1).

_Proof of Corollary 1.2._ Apply Theorem 1.1 to the sorted dimensions of (1_,k,_1). For \(0\le k\le 1\), the first branch applies exactly when \(k\le\frac{1}{2}\). In the remaining range, both possible orderings give

\(\frac{2+k}{2}+\frac{1}{4}\left(2k+\frac{1}{k}\right)=1+k+\frac{1}{4k}.\)

The output-size lower bound \(\omega(k)\ge 2\) proves equality for \(0\le k\le\frac{1}{2}\) and hence \(\alpha\ge\frac{1}{2}\).

