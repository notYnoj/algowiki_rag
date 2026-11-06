<tbc>_Let q be a weight function on E(H_) _such that_

(6.4) \(q(E(H))\ge\frac{\Delta^{1+\delta}}{1-\Delta^{-1}}max_{e\in E(H)}q(e).\)

_Then there is a distribution on matchings M in H such that with high probability_<tbc>

\(q(M)=\big(1\pm\Delta^{-\epsilon}\big)\sum_{e\in E(H)}q(e)w(e).\)

<tbc>Proof. From (_H,w_) we define an unweighted multigraph \(H'\) where \(V(H')=V(H)\) and every edge \(e\in E(H)\) appears in \(E(H')\) with multiplicity \(\lfloor Dw(e)\rfloor\), where \(D=\Delta^2\). First note that \(Dw(e)\ge\Delta\), and so \(\lfloor Dw(e)\rfloor=(1\pm\Delta^{-1})Dw(e)\). In addition \(\Delta(H')=max_{v\in V(H)}\sum_{e\unknown v}\lfloor Dw(e)\rfloor\le D\), and<tbc>

\(\Delta^\text{co}(H')=max_{\{u,v\}\in\genfrac(){pt}{2}{V(H)}{2}}\sum_{e\supseteq\{u,v\}}\lfloor Dw(e)\rfloor\le D\cdot\Delta^{-\delta}=D^{1-\frac{\delta}{2}}.\)

<tbc>Finally \(e(H')\le De(H)\le Dexp(\Delta^{\epsilon^2/4})\le exp(D^{\epsilon^2/4})\). Now we define weight function \(q':H'\rightarrow\mathbb{R}_{\ge 0}\) on the multigraph \(H'\) via \(q'(e)=q(e)\) for every \(e\in H'\). Note first that \(max_{e\in E(H)}q(e)=max_{e\in E(H^\prime)}q'(e)\) and also that given \(q(E(H))\ge\frac{\Delta^{1+\delta}}{1-\Delta^{-1}}max_{e\in E(H)}q(e)\), we have that

\(q'(E(H'))=\sum_{e\in E(H^\prime)}q'(e)=\sum_{e\in E(H)}q(e)\lfloor Dw(e)\rfloor\)<br>
\(=(1\pm\Delta^{-1})\sum_{e\in E(H)}q(e)Dw(e)\)<br>
\(\ge(1-\Delta^{-1})\sum_{e\in E(H)}q(e)D/\Delta\)<br>
\(=(1-\Delta^{-1})\Delta\sum_{e\in E(H)}q(e)\)<br>
\(\ge\Delta^{2+\delta} max_{e\in H}q(e)=D^{1+\delta/2}max_{e\in H^\prime} q'(e)\)

It follows from Theorem 6.3 with parameters \(\delta'=\delta/2,r,L\), and assuming \(\Delta\) sufficiently large, that there exists a matching _M_ in \(H'\) such that<tbc>

\(q'(M)=(1\pm\frac{D^{-\epsilon/2}}{2})\sum_{e\in H^\prime}\frac{q'(e)}{D}.\)

<tbc>Furthermore, _M_ is a matching in (_H,w_) and, by construction,

\(\sum_{e\in H^\prime}\frac{q'(e)}{D}=\sum_{e\in H}\frac{q(e)}{D}\lfloor Dw(e)\rfloor=(1\pm\Delta^{-1})\sum_{e\in H}q(e)w(e).\)

Hence

\(q(M)=(1\pm\Delta^{-\epsilon})\sum_{e\in H}q(e)w(e),\)

as claimed. □

Of course, we could have derived a weighted version that applies to all clean _l_-set weight functions, however we only require the weighted edge version for one specific application which relates only to individual edges, rather than to sets of edges. (This application comes up in the initial steps of the iterative matching

