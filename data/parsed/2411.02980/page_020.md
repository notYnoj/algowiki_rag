For each \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{V}^\mathrm{cp}\), we define the following pair of marginal probabilities:

\(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\unknown\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{cp}|X=x\right],\)<br>
\(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\unknown\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{cp}|Y=y\right].\)

where \(x,y\in[q]^V\) are arbitrary assignments satisfying \(\mathcal{E}\wedge\sigma\) and \(\mathcal{F}\wedge\tau\), respectively.

Note that each marginal probability \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\) is defined by conditioning on _X_ being an arbitrary assignment \(x\in[q]^V\) that satisfies \(\mathcal{E}\wedge\sigma\) (and similarly for each \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\)). The well-definedness of these probabilities is ensured by the following proposition.

**Proposition 5.2.** _Assume_ \(\Phi\) _is satisfiable. Fix any_ \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{V}^\mathrm{cp}\)_. The following sets are nonempty:_

\(\Omega^{\mathcal{E}\wedge\sigma}\unknown\{\pi\in[q]^V|\pi\text{\textit{satisfies}}\mathcal{E}\wedge\sigma\},\)<br>
\(\Omega^{\mathcal{F}\wedge\tau}\unknown\{\pi\in[q]^V|\pi\text{\textit{satisfies}}\mathcal{F}\wedge\tau\}.\)

_Furthermore, for any_ \(x,x'\in\Omega^{\mathcal{E}\wedge\sigma}\) _and_ \(y,y'\in\Omega^{\mathcal{F}\wedge\tau}\)_, it holds that_

\(\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{cp}|X=x\right]=\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{cp}|X=x'\right],\)<br>
\(\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{cp}|Y=y\right]=\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{cp}|Y=y'\right].\)

_This means that_ \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\) _and_ \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\) _are well-defined. Moreover, it holds that_

(9) \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=\mu_\mathcal{C}(\mathcal{F}\wedge\tau)\text{\textit{and}}p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y=\mu_{\mathcal{C}\backslash\{c_0\}}(\mathcal{E}\wedge\sigma).\)

Proposition 5.2 can be proved by following the same argument as in \[WY24, Proposition 4.2\]. In fact, the same proof applies as long as the coupling is well-defined. Therefore, we omit the proof here.

The following proposition outlines families of linear constraints satisfied by the marginal probabilities.

**Proposition 5.3.** _Assume_ \(\Phi\) _is satisfiable. Fix any_ \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{V}^\mathrm{cp}\)_. The following properties hold for_ \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\) _and_ \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\):

(_1)_ _It always holds that_ \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X,p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\in[0,1]\)_. In particular,_<tbc>

<tbc>\(p_{(\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing,\emptyset,\varnothing)}^X=p_{(\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing,\emptyset,\varnothing)}^Y=1.\)<tbc>

_(2)_ _If_ \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\notin\mathcal{L}^\mathrm{cp}\)_, then the following holds:_<tbc>

_(a)_ _If_ \(\mathcal{F}^\tau\unknown\subseteq\mathcal{E}^\sigma\)_, let c be the smallest constraint in_ \(\mathcal{F}^\tau\backslash\mathcal{E}^\sigma\)_, and define_ \(\pi\unknown\mathtt{False}(c)\)_. Then,_<tbc>

\(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=p_{(\mathcal{E}\cup\{c\},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=\sum_{\rho\in[q]^\mathrm{vbl}(c)}p_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)}^X;\)<br>
\(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y=p_{(\mathcal{E}\cup\{c\},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y+p_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)}^Y,\)<br>
\(\text{\textit{for any}}\rho\in[q]^\mathrm{vbl}(c)\text{\textit{such that}}(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)\in\mathcal{V}^\mathrm{cp}.\)

_(b)_ _If_ \(\mathcal{F}^\tau\subseteq\mathcal{E}^\sigma\)_, let c be the smallest constraint in_ \(\mathcal{E}^\sigma\backslash\mathcal{F}^\tau\)_, and define_ \(\rho\unknown\mathtt{False}(c)\)_. Then,_<tbc>

\(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=p_{(\mathcal{E},\mathcal{F}\cup\{c\},\sigma,\tau,T,\varsigma)}^X+p_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\pi)}^X,\)<br>
\(\text{\textit{for any}}\pi\in[q]^\mathrm{vbl}(c)\text{\textit{such that}}(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\pi)\in\mathcal{V}^\mathrm{cp};\)<br>
\(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y=p_{(\mathcal{E},\mathcal{F}\cup\{c\},\sigma,\tau,T,\varsigma)}^Y=\sum_{\pi\in[q]^\mathrm{vbl}(c)}p_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\pi)}^Y.\)

