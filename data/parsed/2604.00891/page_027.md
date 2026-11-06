\(\le(40\sqrt{\frac{5}{14\mathrm{log}(d)}}+\frac{11}{\sqrt{2}})\sqrt{d}\mathrm{log}(d)\)<br>
\(\le(\frac{40}{7}\sqrt{\frac{5}{2}}+\frac{11}{\sqrt{2}})\le 17\sqrt{d}\mathrm{log}(d).\)

Here, the second inequality is due to the fact that \(\alpha_\pi\le\frac{\mathrm{log}(d)}{7}\) as \(d\ge 2^{7\alpha_\pi}\) and the second to last inequality is due to the fact that \(\mathrm{log}(d)\ge 7\) as _d\>_2<sup>7</sup>. The (non-strict) interior and exterior of \(C'\) hence contain at most

\(\lfloor|Z|-20\sqrt{d}\mathrm{log}(d)+17\sqrt{d}\mathrm{log}(d)\rfloor\le\lfloor d-3\sqrt{d}\mathrm{log}(d)\rfloor\le\lfloor d-3\sqrt{d}\rfloor\text{vertices from}Z.\)

Due to the induction hypothesis, the solutions res<sub>1</sub> and res<sub>2</sub> in Line 1 are correct. It only remains to show that the algorithm behind Requirement R4 can combine them. This is slightly non-trivial in this case as the value for _d_ is reduced in the recursive calls, so we need to argue that all pebble sets for \((B,d,\alpha_\pi,x)\) are also pebble sets for \((B,d'=\lfloor d-3\sqrt{d}\rfloor,\alpha_\pi,x'=2x+1)\), that is, the algorithm can access all required results. By definition, each pebble set for \((B,d,\alpha_\pi,x)\) contains at most \(20x\alpha_\pi\sqrt{d}\mathrm{log}(d)\) vertices in _B_li. By Lemma 8, we have that \(x\sqrt{d}\mathrm{log}(d)\le x'\sqrt{d'}\mathrm{log}(d')\) and each such pebble set therefore contains at most \(20x'\alpha_\pi\sqrt{d'}\mathrm{log}(d')\) vertices from _B_li. Thus, each such pebble set is also a pebble set for \((B,d',\alpha_\pi,x')\) and Requirement R4 applies. This concludes the proof of correctness.

It remains to analyze the running time of `solve-\(\pi\)-r`. To this end, let \(\varepsilon>0\) be any constant. We start with the running time of one recursive call. In the following, we will again use the fact that \(\alpha_\pi\le\frac{\mathrm{log}(d)}{7}\) . First, note that the number of possible pebble sets is upper bounded by

\(2^{|B_\mathrm{he}|}\cdot\left(\begin{array}{ c }
|B_\mathrm{li}| \\
20x\alpha_\pi\sqrt{d}\mathrm{log}(d)
\end{array}\right)\le 2^{40(200\mathrm{log}^7(d))\alpha_\pi\sqrt{d}}\cdot 2^{(20(200\mathrm{log}^7(d)\alpha_\pi\sqrt{d}\mathrm{log}(d))\cdot\mathrm{log}(60(200\mathrm{log}^7(d))\alpha_\pi d\mathrm{log}(d))}\)<br>
\(\le 2^\frac{8000}{7}\sqrt{d}\mathrm{log}^8(d)+\frac{3200}{7}\sqrt{d}\mathrm{log}^8(d)\mathrm{log}(d^8)\)<br>
\(\le 2^{(\frac{8000}{7\mathrm{log}^2(d)}+\frac{8:3200}{7})\sqrt{d}\mathrm{log}^9(d)}\)<br>
\(\le 2^{3681\sqrt{d}\mathrm{log}^6(d)}.\)

The number of separators in S is upper-bounded by \(2^{44\mathrm{log}^2(2\alpha_\pi d+3)}\le 2^{44\mathrm{log}^2(d^{1.5})}=2^{99\mathrm{log}^2(d)}\) by Lemma 6. This bounds the number of iterations of the for-loops in one recursive call. If Line 1 is reached, then the number of operations is constant. By Lemmas 1 and 6, Corollary 1, and Requirements R2, R3, and R4, all lines can be computed in \(\mathcal{O}(\gamma(d)n^{\mathrm{max}(2,\rho)}\mathrm{log}(n))\subset\mathcal{O}(\gamma(d)n^{\rho+\varepsilon})\) time each. Thus, the running time of a single recursive call is in

\(\mathcal{O}(2^{3681\sqrt{d}\mathrm{log}^7(d)+99\mathrm{log}^2(d)}\gamma(d)n^{\rho+\varepsilon})\subset\mathcal{O}(2^{3682\sqrt{d}\mathrm{log}^7(d)}\gamma(d)n^{\rho+\varepsilon}).\)

We next analyze the running time of all calls of `solve-\(\pi\)-r` and `red-portals` combined. To this end, we define three functions \(\phi\), _T_, and \(\xi\). The function \(\Phi(d,x)=\mathrm{min}(\frac{x}{40\mathrm{log}^7(d)},1)\) is a potential function measuring how close a recursive call is to calling `red-portals`.

The function \(T[n,D,\phi]\) upper-bounds the number of operations performed by the current recursive call and all future recursive calls of `solve-\(\pi\)-r` and `red-portals` when the current recursive call solves an instance with \(\nu\) vertices, _d=D_, and \(\Phi\) evaluating to \(\phi\). Let \(\kappa\) be a constant such that each recursive call of `solve-\(\pi\)-r`,`red-portals` and `base-case` performs at<tbc>

