<tbc>We now enumerate each point in the proof where we require _b_ to be sufficiently large, and record an explicit condition on _b_ ensuring that step.

\(\bullet\) In (C.1), we require that<tbc>

\(\text{(D.1)}\) \(2\mathrm{exp}\left(-\frac{\alpha b^{2\epsilon}}{3}\right)\le b^{-\epsilon}\Longleftrightarrow\mathrm{log}\left(2b^{1/24}\right)\le\frac{\alpha b^{1/12}}{3}.\)

This condition holds for all \(b\ge(3/\alpha)^{24}\), on which<tbc>

<tbc>\(\mathrm{log}\left(2b^{1/24}\right)\le b^{1/24}\le\frac{\alpha}{3}b^{1/12}.\)<tbc>

\(\bullet\) In (C.2), we require that<tbc>

<tbc>\(\mathrm{exp}\left(-\frac{N}{b}\left[b^{-\epsilon}\left(-\epsilon\mathrm{log}b-\mathrm{log}2+\frac{\alpha b^{2\epsilon}}{3}\right)+(1-b^{-\epsilon})\mathrm{log}\left(\frac{1-b^{-\epsilon}}{1-q_\mathrm{len}}\right)\right]\right)\le\mathrm{exp}\left(-\frac{N}{b}\cdot\frac{\alpha b^\epsilon}{6}\right),\)<tbc>

<tbc>which follows if we have that<tbc>

<tbc>\(b^{-\epsilon}\left(-\epsilon\mathrm{log}b-\mathrm{log}2\right)+(1-b^{-\epsilon})\mathrm{log}(1-b^{-\epsilon})-(1-b^{-\epsilon})\mathrm{log}\left(1-q_\mathrm{len}\right)\ge-\frac{\alpha b^\epsilon}{6}.\)<tbc>

<tbc>In particular, this holds whenever<tbc>

\(\text{(D.2)}\) \(\mathrm{log}b^{1/24}+\mathrm{log}2\le\frac{\alpha b^{1/12}}{12};(1-b^{-1/24})\mathrm{log}(1-b^{-1/24})\ge-\frac{\alpha b^{1/24}}{12}.\)

<tbc>Controlling the two LHS expressions in (D.2) via<tbc>

<tbc>\(\mathrm{log}\left(2b^{1/24}\right)\le b^{1/24};(1-x)\mathrm{log}(1-x)\ge-x\)<tbc>

<tbc>gives that both conditions are satisfied whenever \(b\ge(12/\alpha)^{24}\).<tbc>

\(\bullet\) In (3.14) and (3.17), we require that<tbc>

<tbc>\(B\cdot h(3b^{-\epsilon})+B\cdot 3b^{-\epsilon}\mathrm{log}(b+1)\le B\cdot\frac{\beta^\star(\alpha)^2}{8}\Longleftrightarrow h(3b^{-\epsilon})+3b^{-\epsilon}\mathrm{log}(b+1)\le\frac{\beta^\star(\alpha)^2}{8}.\)<tbc>

<tbc>In particular, this holds whenever

\(\text{(D.3)}\) \(-3b^{-\epsilon}\mathrm{log}(3b^{-\epsilon})\le\frac{\beta^\star(\alpha)^2}{32};-(1-3b^{-\epsilon})\mathrm{log}(1-3b^{-\epsilon})\le\frac{\beta^\star(\alpha)^2}{32};b^{-\epsilon}\mathrm{log}(b+1)\le\frac{\beta^\star(\alpha)^2}{48}.\)

Controlling the three LHS expressions in (D.3) via<tbc>

<tbc>\(-x\mathrm{log}x\le\sqrt{x};-(1-x)\mathrm{log}(1-x)\le x;\mathrm{log}(b+1)\le 48\cdot b^{1/48}\)<tbc>

<tbc>gives that all conditions in (D.3) are satisfied whenever \(b\ge\left(1920/\beta(\alpha)\right)^{96}\).<tbc>

\(\bullet\) In our invocation of Hoeffding’s inequality in (3.15), we assumed that

\(\mathrm{exp}\left(-\frac{2\left(B\left(\frac{1+\beta^\star(\alpha)}{2}-\mathbb{P}\left(\mathrm{maj}(X^\prime^{(i)})=\mathrm{maj}(Y^{(i)}),\Delta(Y^{(i)})>0\right)\right)\right)^2}{B}\right)\le\mathrm{exp}\left(-\frac{B\cdot\beta^\star(\alpha)^2}{4}\right)\)<br>
\(\Longleftrightarrow 2\mathbb{P}\left(\mathrm{maj}(X^\prime^{(i)})=\mathrm{maj}(Y^{(i)}),\Delta(Y^{(i)})>0\right)-1\le\left(1-\frac{1}{\sqrt{2}}\right)\beta^\star(\alpha).\)

