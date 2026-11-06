<tbc>If it held that \(\left(Z^{(1)},\dots,Z^{(B)}\right)\in\mathcal{N}\mathcal{E}_\mathrm{ind}(Z)\), then

(C.4) \(T_\mathrm{ind}(x,Z)\ge\frac{1}{B}\sum_{i=1}^BA_\mathrm{loc}\left(x^{(i)},Z^{(i)}\right)=\frac{1}{B}\sum_{i\in\mathcal{I}_x}A_\mathrm{loc}\left(x^{(i)},Z^{(i)}\right)+\frac{1}{B}\sum_{i\notin\mathcal{I}_x}A_\mathrm{loc}\left(x^{(i)},Z^{(i)}\right).\)

We now sequentially derive lower bounds on the two summands of (C.4) which hold with overwhelming probability. Towards this end, we define independent random variables \(\zeta_1\) and \(\zeta_0\) such that

(C.5) \(\zeta_1\sim\mathrm{Bin}\left(\frac{b+\sqrt{b}}{2},\alpha\right);\zeta_0\sim\mathrm{Bin}\left(\frac{b-\sqrt{b}}{2},\alpha\right),\)

for which the central limit theorem and Slutsky’s theorem readily imply that

\(\frac{\zeta_1-\frac{\alpha b}{2}}{\sqrt{b}}\longrightarrow^d_{b\rightarrow\infty}\mathcal{N}\left(\frac{\alpha}{2},\frac{\alpha}{2}(1-\alpha)\right);\frac{\zeta_0-\frac{\alpha b}{2}}{\sqrt{b}}\longrightarrow^d_{b\rightarrow\infty}\mathcal{N}\left(-\frac{\alpha}{2},\frac{\alpha}{2}(1-\alpha)\right).\)

We begin with the first summand of (C.4). We fix \(i\in\mathcal{I}\), and we assume without loss of generality that maj(_x<sub>i</sub>_)=1. It now readily follows that, with the inequality below relying on the fact that \(\Delta\left(x^{(i)}\right)\ge\sqrt{b}\),

\(\mathbb{P}\left(A_\mathrm{loc}\left(x^{(i)},Z^{(i)}\right)=1\right)\)<br>
\(=\mathbb{P}\left(\left\{\mathrm{maj}\left(Z^{(i)}\right)=1\right\}\cap\left\{\delta\Delta\left(Z^{(i)}\right)\ge 1\right\}\right)=\mathbb{P}\left(\left\{\mathrm{maj}\left(Z^{(i)}\right)=1\right\}\cap\left\{\Delta\left(Z^{(i)}\right)\ge b^{1/2-\epsilon}\right\}\right)\)<br>
\(\ge\mathbb{P}\left(\zeta_1-\zeta_0\ge b^{1/2-\epsilon}\right)=\mathbb{P}\left(\frac{\zeta_1-\frac{\alpha b}{2}}{\sqrt{b}}-\frac{\zeta_0-\frac{\alpha b}{2}}{\sqrt{b}}\ge b^{-\epsilon}\right)\)<br>
\(\longrightarrow^{b\rightarrow\infty}\mathbb{P}\left(\mathcal{N}\left(\alpha,\alpha(1-\alpha)\right)\ge 0\right)=^\text{(3.10)}\frac{1}{2}+\beta(\alpha)=^\text{(3.10)}\frac{1}{2}+40\beta^\star(\alpha),\) (C.6)

where it is clear that the constant \(\beta(\alpha)>0\). This implies that, assuming (from (C.6)) _b_ is large enough such that

\(\mathbb{P}\left(A_\mathrm{loc}\left(x^{(i)},Z^{(i)}\right)=1\right)\ge\frac{1}{2}+\frac{3\beta(\alpha)}{4}\)

holds (with this guarantee holding uniformly over all \(i\in[B]\)),

\(\mathbb{P}\left(\frac{1}{|\mathcal{I}|}\sum_{i\in\mathcal{I}_x}A_\mathrm{loc}\left(x^{(i)},Z^{(i)}\right)\le\frac{1+\beta(\alpha)}{2}\right)\le\mathbb{P}\left(\sum_{i\in\mathcal{I}_x}\unknown\left\{A_\mathrm{loc}(x^{(i)},Z^{(i)})=1\right\}\le|\mathcal{I}_x|\cdot\frac{1+\beta(\alpha)}{2}\right)\)<br>
\(\le\mathbb{P}\left(\sum_{i\in\mathcal{I}_x}\unknown\left\{A_\mathrm{loc}(x^{(i)},Z^{(i)})=1\right\}-\mathbb{E}\left[\sum_{i\in\mathcal{I}_x}\unknown\left\{A_\mathrm{loc}(x^{(i)},Z^{(i)})=1\right\}\right]\le-|\mathcal{I}_x|\cdot\frac{\beta(\alpha)}{4}\right)\) (C.7)

\(\le^\text{(Hoeffding)}\mathrm{exp}\left(-\frac{2|\mathcal{I}_x|^2\beta(\alpha)^2}{16|\mathcal{I}_x|}\right)\le^\text{(C.3)}\mathrm{exp}\left(-\frac{B\cdot\beta(\alpha)^2}{80}\right)=\mathrm{exp}\left(-\frac{N\cdot\beta(\alpha)^2}{80b}\right)=e^{-\Omega(N)}.\)

Combining (C.2) and (C.7), it holds with probability \(1-e^{-\Omega(N)}\) that

\(T_\mathrm{ind}(x,Z)\ge^\text{(C.4)}\frac{1}{B}\sum_{i\in\mathcal{I}_x}A_\mathrm{loc}\left(x^{(i)},Z^{(i)}\right)+\frac{1}{B}\sum_{i\notin\mathcal{I}_x}A_\mathrm{loc}\left(x^{(i)},Z^{(i)}\right)\)<br>
\(\ge\frac{|\mathcal{I}_x|}{B}\left(\frac{1+\beta(\alpha)}{2}\right)+\frac{1}{B}\sum_{i\notin\mathcal{I}_x}A_\mathrm{loc}\left(x^{(i)},Z^{(i)}\right).\) (C.8)

