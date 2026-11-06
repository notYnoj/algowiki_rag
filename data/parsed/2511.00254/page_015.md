_profits_ \(w(h)\ge 0\) _for_ \(h\in E(H)\)_. Let f be a feasible multiflow such that_ \(|f|_w\ge w_\mathrm{max}=\mathrm{max}_{h\in E(H)}w(h)\)_. There exists a multiflow_ \(\hat{f}\) _satisfying:_

1. \(\hat{f}\) _is feasible,_<tbc>

2. _the support paths of_ \(\hat{f}\) _are a subset of the support paths of f,_<tbc>

_3._ \(|\hat{f}|_w\ge(1-\epsilon)|f|_w\)_, and_<tbc>

_4._ _for every path P,_ \(\hat{f}(P)\) _is a multiple of_ \(\frac{1}{\mathrm{log}^2n}\).

_There is a polynomial time algorithm that computes such an_ \(\hat{f}\).

We prove this in Section B using a randomized rounding and re-scaling argument (which can be de- randomized to give a deterministic algorithm).

The two conditions that \(|f|_w\ge w_\mathrm{max}\) and \(n\ge N_\epsilon\) are only minor technicalities. If |_f|<sub>w</sub>\<w_<sub>max</sub>, then we need not bother with rounding _f_: simply take _f_<sup>∗</sup> as routing one unit of flow on any _st_-path where _w(s,t_)=_w_<sub>max</sub>. The \(n\ge N_\epsilon\) condition is also not a huge obstacle. If \(n<N_\epsilon\) then _n_ is bounded by a constant, and we can obtain \(\hat{f}\) whose fractionality is constant as follows. We set up a linear program formulation of the _w_-weighted maximum multiflow problem using path-variables _x(P_), but only using paths _P_ where _P_ is a support path of _f_. Standard linear programming theory implies there is a feasible solution \(\hat{f}\) whose value is at least that of _f_, is uncrossed (since its support paths are a subset of _f_’s), and whose fractionality is bounded as a function of \(n\le N_\epsilon\), but this is still constant.

This concludes the proof of the unit capacity case. For general capacities, we reduce to the unit capacity case. Ultimately we want to split each edge into parallel unit capacity copies, but need to be careful because this is not a polynomial time operation in general. A key fact we use is the following.

**Lemma 4.5.** _Let f be an uncrossed flow in a planar multiflow layout_ (_G,H). Then f has at most O_(|F(_G_)||_E(H_)|) _support paths, where_ F(_G_) _is the set of faces of G._

_Proof._ It suffices to show that for each \(h=(s,t)\in E(H)\), _x<sup>h</sup>_ has only _O_(|F(_G_)|) support paths. Order the support paths of _x<sup>h</sup>_ clockwise about _s_ using the uncrossed parallelization, say \(P_1,\dots,P_\ell\). Observe that each face _F_ appears in the region bounded between a unique consecutive pair of paths _P<sub>i</sub>,P_<sub>_i_+1</sub> in this clockwise order. Moreover the region between each consecutive pair of paths _P<sub>i</sub>,P_<sub>_i_+1</sub> contains at least one face. The result follows.

The reduction to unit capacities now proceeds as follows. Define an integral flow _f_<sub>int</sub> by \(f_\mathrm{int}(P)=\lfloor f(P)\rfloor\) for all _P_. Let _f_<sub>frac</sub>=_f-f_<sub>int</sub>, which satisfies that _f_<sub>frac</sub>(_P)\<_1 for all _P_, and define capacities \(u'(e)=u(e)-f_\mathrm{int}(e)\). Observe that _f_<sub>frac</sub> is feasible for capacities \(u'\). Let _K_ be the number of support paths of _f_<sub>frac</sub>, which by Theorem 4.5 is polynomially bounded in |_E(G_)|+|_E(H_)| (recall that the number of faces of a planar graph is linear in the number of edges). Now, since _f_<sub>frac</sub>(_P)\<_1 for all _P_, it follows that \(|f_\mathrm{frac}|=\sum_Pf_\mathrm{frac}(P)<K\). Therefore _f_<sub>frac</sub> is still feasible if we bound the capacities to \(u''(e)=\mathrm{min}\{u'(e),K\}\), but these capacities are polynomially bounded in the size of _G_ and _H_. Then splitting each edge _e_ into \(u''(e)\) many unit-capacity copies, we apply the algorithm for the unit capacity case to _f_<sub>frac</sub> and obtain an integral multiflow _f_<sup>∗</sup> that is feasible for \((G,H,u'')\) and has value \(|f^*|_w\ge\frac{1}{\gamma}|f_\mathrm{frac}|_w\). The final flow we output is _f_<sub>int</sub>+_f_<sup>∗</sup>, which is feasible for (_G,H,u_) and has value \(|f_\mathrm{int}+f^*|_w\ge|f_\mathrm{int}|_w+\frac{1}{\gamma}|f_\mathrm{frac}|_w\ge\frac{1}{\gamma}|f|_w\).

It is straightforward to generalize this to the node-capacitated setting - the colouring and integer decomposition property proceed in exactly the same way.

