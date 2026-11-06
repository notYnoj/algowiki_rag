Now, let<tbc>

\(\delta_i(\alpha):=\frac{\mathbb{1}_{U_i\ge\alpha}-(1-\alpha)}{\sqrt{\alpha(1-\alpha)}}=\frac{2(\mathbb{1}_{U_i\ge\alpha}-1/2)-(1-2\alpha)}{2\sqrt{\alpha(1-\alpha)}},\)

<tbc>where the last equality is here to show that this is just a renormalized random variable taking values in {-1,1}, much like the \(\xi_i(t)\)’s, random variables with \(\mathbb{P}(\xi_i(t)=1)=(1+\mathrm{e}^{-t})/2\) and \(\mathbb{P}(\xi_i(t)=-1)=(1-\mathrm{e}^{-t})/2\) introduced in \[18\]. We have:

\(\mathbb{E}(\langle T,\delta_i(\alpha)d_iS(X^{(\alpha)})\rangle)=\mathbb{E}\left(\langle T,\frac{\mathbb{1}_{U_i\ge\alpha} d_iS(X^{(\alpha),i})-(1-\alpha)(\mathbb{1}_{U_i\ge\alpha} d_iS(X^{(\alpha),i})+\mathbb{1}_{U_i<\alpha} d_iS(X^{(\alpha),\hat{i}}))}{\sqrt{\alpha(1-\alpha)}}\rangle\right)\)<br>
\(=\mathbb{E}\left(\langle T,\frac{\alpha\mathbb{1}_{U_i\ge\alpha} d_iS(X^{(\alpha),i})}{\sqrt{\alpha(1-\alpha)}}\rangle\right)\)<br>
\(=\mathbb{E}\left(\langle T,\sqrt{\alpha(1-\alpha)}d_iS(X^{(\alpha),i})\rangle\right),\)

hence, with (2.5) we get:

\(\mathbb{E}(\langle T,S\rangle-\Phi^*(T))=\sum_{i=1}^n\int_0^1\frac{\mathbb{E}(\langle T,\delta_i(\alpha)d_iS(X^{(\alpha)})\rangle)}{\sqrt{\alpha(1-\alpha)}}\mathrm{d}\alpha-\mathbb{E}\Phi^*(T)\)<br>
\(=\int_0^1\mathbb{E}(\langle T,\pi\sum_{i=1}^n\delta_i(\alpha)d_iS(X^{(\alpha)})\rangle)-\mathbb{E}\Phi^*(T)\frac{\mathrm{d}\alpha}{\pi\sqrt{\alpha(1-\alpha)}}\)<br>
\(\le\int_0^1\mathbb{E}\Phi\left(\pi\sum_{i=1}^n\delta_i(\alpha)d_iS(X^{(\alpha)})\right)\frac{\mathrm{d}\alpha}{\pi\sqrt{\alpha(1-\alpha)}}.\)

Note that \((U_1,\dots,U_n,X_1^{(\alpha)},\dots,X_n^{(\alpha)})\) has the same distribution as (_U_<sub>1</sub>_,...,U<sub>n</sub>,X_<sub>1</sub>_,...,X<sub>n</sub>_), so

\(\mathbb{E}(\langle T,S\rangle-\Phi^*(T))\le\int_0^1\mathbb{E}\Phi\left(\pi\sum_{i=1}^n\delta_i(\alpha)d_iS(X)\right)\frac{\mathrm{d}\alpha}{\pi\sqrt{\alpha(1-\alpha)}}.\)

Recalling (2.4), the result follows.

Let us see how the above allows to link our approach with the main results of \[18\] for Rademacher random variables. Recalling the notation of \[18\]: for \(x\in\{-1,1\}^n\), let<tbc>

\(D_iS(x):=\frac{S(x_1,\dots,x_i,\dots,x_n)-S(x_1,\dots,-x_i,\dots,x_n)}{2}.\)

<tbc>We can now state the corollary, in the Rademacher case:

**Corollary 2.2.** _Let X<sub>i</sub>’s be i.i.d. Rademacher random variables,_<tbc>

\(\mathbb{E}(\Phi(S-\mathbb{E}S))\le\int_0^1\mathbb{E}\Phi\left(\pi\sum_{i=1}^n\delta_i(\alpha)D_iS(X)\right)\frac{\mathrm{d}\alpha}{\pi\sqrt{\alpha(1-\alpha)}},\)

<tbc>_i.e.,_<tbc>

\(\mathbb{E}(\Phi(S-\mathbb{E}S))\le\int_0^{+\infty}\mathbb{E}\Phi\left(\pi\sum_{i=1}^n\delta_i(\mathrm{e}^{-2t})D_iS(X)\right)\frac{2\mathrm{d}t}{\pi\sqrt{\mathrm{e}^{2t}-1}}.\)

