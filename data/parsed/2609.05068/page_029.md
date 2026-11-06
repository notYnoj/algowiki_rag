Because \(x\ge 0\) for all \((x,\mathbf{y})\in E\), the condition \(xf(x,\mathbf{y})\le 0\) is logically equivalent to _x_=0 or \(f(x,\mathbf{y})\le 0\). Therefore, \(D=D_\mathrm{on}\cup D_\mathrm{off}\).

Assume there exists a convex set \(D'\subseteq D\) that is neither included in _D_<sub>on</sub> nor in _D_<sub>off</sub>. There exist two points \(p_\overline{\mathrm{off}}=(x_\overline{\mathrm{off}},\mathbf{y}_\overline{\mathrm{off}})\in D'\backslash D_\mathrm{off}\) (so \(x_\overline{\mathrm{off}}>0\)) and \(p_\overline{\mathrm{on}}=(x_\overline{\mathrm{on}},\mathbf{y}_\overline{\mathrm{on}})\in D'\backslash D_\mathrm{on}\) (so \(f(x_\overline{\mathrm{on}},\mathbf{y}_\overline{\mathrm{on}})>0\))

Figure 4 illustrates this proof for _E_=\[0,1\]<sup>2</sup> and \(f(x,y)=x^2+y^2-\frac{1}{4}\). The domain _D_ is the union of three disjoint subsets: \(D_\mathrm{on}\cap D_\mathrm{off}\) in red, _D_\\_D_<sub>off</sub> in orange, and _D_\\_D_<sub>on</sub> in green. As we will see, a set containing both _p_<sub><o>on</o></sub> and _p_<sub><o>off</o></sub> is either non-convex or contains points outside _D_.

Since \(p_\overline{\mathrm{off}}\in D'\subseteq D\) and _x_<sub><o>off</o></sub>_\>_0, we must have \(f(x_\overline{\mathrm{off}},\mathbf{y}_\overline{\mathrm{off}})\le 0\). Similarly, since \(p_\overline{\mathrm{on}}\in D\) and \(f(x_\overline{\mathrm{on}},\mathbf{y}_\overline{\mathrm{on}})>0\), we must have _x_<sub><o>on</o></sub>=0.

Because _f_ is continuous on _E_ and \(f(x_\overline{\mathrm{on}},\mathbf{y}_\overline{\mathrm{on}})>0\), there exists a ball B centered at _p_<sub><o>on</o></sub> with radius _r\>_0 such that _f(x,_**y**)_\>_0 for all \((x,\mathbf{y})\in E\cap\mathcal{B}\).

Consider the convex combination \(p_\alpha=(x_\alpha,\mathbf{y}_\alpha)=(1-\alpha)p_\overline{\mathrm{on}}+\alpha p_\overline{\mathrm{off}}\) with \(\alpha=\frac{r}{2\|p_\overline{\mathrm{off}}-p_\overline{\mathrm{on}}\|}\in]0,1]\).

• \(\|p_\alpha-p_\overline{\mathrm{on}}\|=\alpha\|p_\overline{\mathrm{off}}-p_\overline{\mathrm{on}}\|<r\), so \(p_\alpha\in\mathcal{B}\) and \(f(p_\alpha)>0\).<tbc>

• \(x_\alpha=(1-\alpha)x_\overline{\mathrm{on}}+\alpha x_\overline{\mathrm{off}}=\alpha x_\overline{\mathrm{off}}>0\).

Therefore, \(x_\alpha f(x_\alpha,\mathbf{y}_\alpha)>0\) and \(p_\alpha\notin D\) which implies that \(p_\alpha\notin D'\) and \(D'\) cannot be a convex set. This proves that there is no convex subset of _D_ that is neither a convex subset of _D_<sub>on</sub> nor _D_<sub>off</sub>.

y
1
Pon
Px
Poff
0
1

Figure 4: Illustration of the proof of Lemma 5.1 for _E_=\[0,1\]<sup>2</sup>, and \(f(x,y)=x^2+y^2-\frac{1}{4}\).

