**Objective** We obtain the upper bound by taking the longest \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) path in this graph.

We consider applying Claim 6.13 to this graph. Note that:

• The graph has _o(n_<sup>0.03</sup>) vertices and has (_n/I<sub>s</sub>_+1) layers. Edges only connect vertices from adjacent layers with weight either 0 or _I<sub>s</sub>_;<tbc>

• Each edge weight is _I<sub>s</sub>_ with probability \(exp\left(-\omega\left(log^{0.02}(n)\right)\right)\);<tbc>

• Since we sample \(\eta_{l,r,1\dots M}\) independently for each (_l,r_\], edges from different layers are independent in weights;<tbc>

• Fix a vertex \(\langle x,y\rangle\). If an edge from \(\langle x',y'\rangle\) to \(\langle x'+I_s,y''\rangle\) is reachable from \(\langle x,y\rangle\) within \(exp\left(\Theta\left(log^{0.02}(n)\right)\right)\) hops (i.e., number of edges visited), then \(max(|x'-x|,|y'-y|)=I_s\cdot exp\left(\Theta\left(log^{0.02}(n)\right)\right)\) and \(|y''-y'|\le I_s\). Since _I<sub>s</sub>_ divides each of \(x,x'\) and \((I_s/\phi_y)\) divides each of \(y,y',y''\), the number of reachable edges is less than<tbc>

<tbc>\(\underbrace{exp\left(\Theta\left(log^{0.02}(n)\right)\right)}_{x^\prime}\cdot\underbrace{exp\left(\Theta\left(log^{0.02}(n)\right)\right)\cdot\phi_y}_{y^\prime}\cdot\underbrace{\phi_y}_{y^{\prime\prime}}=exp\left(\Theta\left(log^{0.02}(n)\right)\right).\)<tbc>

<tbc>From Claim 6.13 (with weights scaled up by _I<sub>s</sub>_) with

• _h_:=_O(n/I<sub>s</sub>_);<tbc>

• _N_:=_O(n_<sup>0.03</sup>);<tbc>

• \(B:=exp\left(\Theta\left(log^{0.02}(n)\right)\right)\);<tbc>

• \(d:=exp\left(\Theta\left(log^{0.02}(n)\right)\right)\);<tbc>

• \(p:=exp\left(-\omega\left(log^{0.02}(n)\right)\right)\);<tbc>

• \(u:=\langle 0,n_X\rangle\).

we obtain that with probability \(1-n^{-\omega(1)}\), an upper bound for the overestimation on each scale due to "bad" estimates (type II error) is<tbc>

\(n\cdot\sqrt{log(n^{0.03})}/exp\left(\Theta\left(log^{0.02}(n)\right)\right)=n\cdot exp\left(-\Omega\left(log^{0.02}(n)\right)\right).\)

<tbc>By union bound across all scales, we obtain that with probability 1-_o_(1), the total type II error is

\(n\cdot S\cdot exp\left(-\Omega\left(log^{0.02}(n)\right)\right)=n\cdot exp\left(-\Omega\left(log^{0.02}(n)\right)\right).\)

Since \(w(\widehat{p})=n/2^{o\left(log^{0.01}(n)\right)}\), this is \(o(w(\widehat{p}))\).

