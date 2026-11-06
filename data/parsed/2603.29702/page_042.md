**Definition 6.14** (Upper Bound for Underestimation due to "Bad" Estimates)**.** Consider the following graph:

**Vertices** We only consider vertices \(\langle x,y\rangle\) in the Sparsified Edit Distance Grid Graph with the additional constraint that _I<sub>s</sub>|x_;

**Edges** There is an edge from \(\langle x,y\rangle\) to \(\langle x+I_s,y'\rangle\) such that \(|y'-y|\le I_s\) with a weight of either _I<sub>s</sub>_, if \(\mathrm{est}[x,y,x+I_s,y']\) is "bad," or 0 otherwise.

**Objective** We obtain the upper bound by taking the longest \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) path in this graph.

We consider applying Claim 6.13 to this graph. Note that:

• The graph has _o(n_<sup>0.03</sup>) vertices and has (_n/I<sub>s</sub>_+1) layers. Edges only connect vertices from adjacent layers (i.e., layer-_L_ to layer-(_L_+1) for some _L_) with weight either 0 or _I<sub>s</sub>_;<tbc>

• Each edge weight is _I<sub>s</sub>_ with probability \(\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\);<tbc>

• Since we sample \(\eta_{l,r,1\dots M}\) independently for each (_l,r_\], edges from different layers are independent in weights;<tbc>

• Fix a vertex \(\langle x,y\rangle\). If an edge from \(\langle x',y'\rangle\) to \(\langle x'+I_s,y''\rangle\) is reachable from \(\langle x,y\rangle\) within \(\mathrm{exp}\left(\Theta\left(\mathrm{log}^{0.02}(n)\right)\right)\) hops (i.e., number of edges visited), then \(\mathrm{max}(|x'-x|,|y'-y|)=I_s\cdot\mathrm{exp}\left(\Theta\left(\mathrm{log}^{0.02}(n)\right)\right)\) and \(|y''-y'|\le I_s\). Since _I<sub>s</sub>_ divides each of \(x,x'\) and \((I_s/\phi_y)\) divides each of \(y,y',y''\), the number of reachable edges is less than<tbc>

\(\underbrace{\mathrm{exp}\left(\Theta\left(\mathrm{log}^{0.02}(n)\right)\right)}_{x^\prime}\cdot\underbrace{\mathrm{exp}\left(\Theta\left(\mathrm{log}^{0.02}(n)\right)\right)}_{y^\prime}\cdot\underbrace{\phi_y}_{y^{\prime\prime}}=\mathrm{exp}\left(\Theta\left(\mathrm{log}^{0.02}(n)\right)\right).\)

From Claim 6.13 (with weights scaled up by _I<sub>s</sub>_) with

• _h_:=_O(n/I<sub>s</sub>_);<tbc>

• _N_:=_O(n_<sup>0.03</sup>);<tbc>

• \(B:=\mathrm{exp}\left(\Theta\left(\mathrm{log}^{0.02}(n)\right)\right)\);<tbc>

• \(d:=\mathrm{exp}\left(\Theta\left(\mathrm{log}^{0.02}(n)\right)\right)\);<tbc>

• \(p:=\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\);<tbc>

• \(u:=\langle 0,n_X\rangle\).

<tbc>we obtain that with probability \(1-n^{-\omega(1)}\), an upper bound for the underestimation on each scale due to "bad" estimates (type II error) is

\(n\cdot\sqrt{\mathrm{log}(n^{0.03})}/\mathrm{exp}\left(\Theta\left(\mathrm{log}^{0.02}(n)\right)\right)=n\cdot\mathrm{exp}\left(-\Omega\left(\mathrm{log}^{0.02}(n)\right)\right).\)

By union bound across all scales, we obtain that with probability 1-_o_(1), the total type II error is

\(n\cdot S\cdot\mathrm{exp}\left(-\Omega\left(\mathrm{log}^{0.02}(n)\right)\right)=n\cdot\mathrm{exp}\left(-\Omega\left(\mathrm{log}^{0.02}(n)\right)\right).\)

Since \(w(\widehat{p})=n/2^{o\left(\mathrm{log}^{0.01}(n)\right)}\), this is \(o(w(\widehat{p}))\).

