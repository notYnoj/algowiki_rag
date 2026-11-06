Indeed, clipping changes each height by at most _B(u_), hence changes each local extremum, and their midpoint, by at most _B(u_). We bound the two terms separately.

• Let us define<tbc>

\(Z(u)=\widetilde{H}_u(x)-\langle u,x\rangle=\frac{1}{2}min_{P\in\Pi_x}\{\langle u,x_P-x\rangle+d_P\}+\frac{1}{2}max_{P\in\Pi_x}\{\langle u,x_P-x\rangle-d_P\}\)<br>
\(R(u)=max_{P\in\Pi_x}\{\langle u,x_P-x\rangle-d_P\}\)

Clearly, we have _Z(u_)=(_R(u_)-_R_(-_u_))/2. Recall that \(\|x_P-x\|<\sqrt{\Delta}\) for every \(P\in\Pi_x\). Consequently, _R_ and _Z_ are \(\sqrt{\Delta}\)-Lipschitz as functions of _u_. Moreover, _Z_ is odd, so E_Z(u_)=0. The Gaussian Poincaré inequality and Cauchy-Schwarz give<tbc>

<tbc>\(\mathbb{E}A(u)\le\sqrt{\mathbb{E}Z(u)^2}=\sqrt{\mathrm{Var}(Z(u))}\le\sqrt{\Delta}.\)<tbc>

• Recall that \(|\Pi_x|\le M\) and \(\|x_P\|\le 2/\sqrt{c}\) (by Assumption 1). The Gaussian tail bound and integration give

\(\mathbb{E}B(u)^2\le\frac{16M}{c}e^{-cb^2/8}=\Delta,\mathbb{E}B(u)\le\sqrt{\Delta}.\)

Adding the two bounds yields \(\mathbb{E}|H_u(x)-\langle u,x\rangle|\le 2\sqrt{\Delta}\), proving (13).

We are ready to prove Lemma 19.

_Proof of Lemma 19._ Take \(c',\sigma,\zeta\) from Lemma 13. Let \(I\subset\mathbb{R}\) be the projection gap between _A_ and _B_ trimmed by \(\sigma/4\) at both ends (or empty if the gap is at most \(\sigma/2\)). By the lemma, \(\mathtt{Pr}\left[|I|\ge\sigma/2\right]\ge\zeta\). Choose constants \(\theta\in(0,1)\), \(\Delta>0\) and parameter \(\mu\) so that

\(\theta+\frac{16\sqrt{\Delta}}{\sigma}\le\frac{c'\zeta}{4}\mu\ge\frac{24\alpha}{c'\varepsilon n}\left(\frac{4L}{\sigma}+1\right)\)

where \(L=L(c,\Delta,\theta,\Gamma,\beta)\) is the function from Lemma 20. Note that \(\mu\ge\Theta(\frac{\alpha\sqrt{\beta}}{\varepsilon n})\) since \(L=\Theta(\sqrt{\beta})\) and \(\beta\ge 1\). By Lemma 20 and Markov’s inequality, for each \(x\in\widehat{S}\) we have \(\mathtt{Pr}\left[|H_u(x)-\langle u,x\rangle|>\sigma/8\right]\le 16\sqrt{\Delta}/\sigma\). Call a terminal in _S_<sup>∗</sup> _bad_ if it lies outside \(\widehat{S}\) or its approximation error exceeds \(\sigma/8\). Let _N_<sup>bad</sup> be the number of bad terminals. Their expected number is at most \(\left(\theta+\frac{16\sqrt{\Delta}}{\sigma}\right)n\le\frac{c'\zeta n}{4}\) , and thus \(\mathtt{Pr}\left[N^\mathtt{bad}>c'n/2\right]\le\zeta/2\) by Markov’s inequality. By the union bound, we have \(N^\mathtt{bad}\le c'n/2\) and \(|I|\ge\sigma/2\) with probability at least \(\zeta-\zeta/2=\zeta/2\). We will show that under this event the cost of the cut _F_ in the call `DirectionalFlowCut`(`u`) satisfies \(F\le c'n\mu\); Lemma 12(a) will then imply the desired claim (recall that \(k=|A|=|B|=2c'n\)).

On the event above, for \(s\in I\) define

\(A_s=\{x\in V:H_u(x)<s-L\eta_x\}\)<br>
\(B_s=\{x\in V:H_u(x)>s+L\eta_x\}\)<br>
\(C_s=\{x\in V:H_u(x)\in[s-L\eta_x,s+L\eta_x]\}\)

If a good terminal \(x\in A\), then \(\langle u,x\rangle\le s-\sigma/4\) and hence \(H_u(x)\le s-\sigma/8\); symmetrically, a good terminal \(y\in B\) satisfies \(H_u(y)\ge s+\sigma/8\). Thus every good terminal in \(A\cup B\) either belongs to _C<sub>s</sub>_ or lies on its correct height shore. The triple (_A<sub>s</sub>,B<sub>s</sub>,C<sub>s</sub>_) is an element cut of _G_. By Lemma 12(a), there is a valid _s-t_ cut in the graph \(\mathcal{N}(A,B,\mu)\) that maps to this element cut and has capacity at most<tbc>

\(\Phi_s:=\underbrace{w(C_s)}_{2}+\underbrace{w(E(A_s,B_s))}_{\sum_{x\in V}[|s-H_u(x)|\le L\eta_x]\cdot\frac{w(x)}{2}}_{\sum_{(x,y)\in\widehat{E}}[s\in(H_u(x)+L\eta_x,H_u(y)-L\eta_y)]\cdot w(xy)}+\underbrace{\mu|A\cap B_s|+\mu|B\cap A_s|}_\Psi,\)

