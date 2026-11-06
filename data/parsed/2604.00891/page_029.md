Recall that \(\mathrm{log}(D)\ge 7\) and Lemma 7 states that \(\sqrt{D-3\sqrt{D}}+1\le\sqrt{D}-\frac{1}{10}\). This yields for the last case

\(T[\nu,D,\phi]\le 2T[\frac{3}{4}\nu,D,\phi+\frac{1}{40\mathrm{log}^7(D)}]+2^{99\mathrm{log}^2(D)}T[\nu,\lfloor D-3\sqrt{D}\rfloor,1]+\lambda 2^{3682\sqrt{D}\mathrm{log}^7(D)}\gamma(D)\nu^{\rho+\varepsilon}\)<br>
\(\le 2\cdot\lambda 2^{4000\mathrm{log}^7(D)(\sqrt{D}+\frac{21(\phi+\frac{1}{40\mathrm{log}^7(D)})}{40\mathrm{log}^4(D)})}\gamma(D)(\frac{3}{4}\nu)^\delta\)<br>
\(+2^{99\mathrm{log}^2(D)}\cdot\lambda 2^{4000\mathrm{log}^7(D-3\sqrt{D})(\sqrt{D-3\sqrt{D}}+\frac{21}{40\mathrm{log}^4(D)})}\gamma(D-3\sqrt{D})\nu^\delta\)<br>
\(+\kappa 2^{3682\sqrt{D}\mathrm{log}^7(D)}\gamma(D)\nu^\delta\)<br>
\(\le 2\cdot(\frac{3}{4})^\delta\cdot\lambda 2^{4000\mathrm{log}^7(D)(\sqrt{D}+\frac{21(\phi+\frac{1}{40\mathrm{log}^7(D)})}{40\mathrm{log}^4(D)})}\gamma(D)\nu^\delta\)<br>
\(+2^{99\mathrm{log}^2(D)}\cdot\lambda 2^{4000\mathrm{log}^7(D)(\sqrt{D-3\sqrt{D}}+1)}\gamma(D)\nu^\delta\)<br>
\(+\kappa 2^{3682\sqrt{D}\mathrm{log}^7(D)}\gamma(D)\nu^\delta\)<br>
\(\le 2\cdot(\frac{3}{4})^\delta\cdot\lambda 2^{4000\mathrm{log}^7(D)(\sqrt{D}+\frac{21\phi}{40\mathrm{log}^4(D)}+\frac{21}{1600\mathrm{log}^{11}(D)})}\gamma(D)\nu^\delta\)<br>
\(+2^{99\mathrm{log}^2(D)}\cdot\lambda 2^{4000\mathrm{log}^7(D)(\sqrt{D}-\frac{1}{10})}\gamma(D)\nu^\delta\)<br>
\(+\kappa 2^{3682\sqrt{D}\mathrm{log}^7(D)}\gamma(D)\nu^\delta\)<br>
\(\le\lambda 2^{4000\mathrm{log}^7(D)(\sqrt{D}+\frac{21\phi}{40\mathrm{log}^4(D)})}\gamma(D)\nu^\delta.\)<br>
\(\left(2\cdot(3/4)^\delta\cdot 2^\frac{21\cdot 4000}{1600\mathrm{log}^4(D)}+2^{99\mathrm{log}^2(D)+4000\mathrm{log}^7(D)(-\frac{1}{10})}+\frac{\kappa}{\lambda}\right)\)<br>
\(\le\lambda 2^{4000\mathrm{log}^7(D)(\sqrt{D}+\frac{21\phi}{40\mathrm{log}^4(D)})}\gamma(D)\nu^\delta\cdot\left(2\cdot(3/4)^{2.49}\cdot 2^\frac{210}{4\cdot 7^4}+2^{-300\mathrm{log}^7(D)}+2^{-2000\mathrm{log}^3(D)}\right)\)<br>
\(\le\lambda 2^{4000\mathrm{log}^7(D)(\sqrt{D}+\frac{21\phi}{40\mathrm{log}^4(D)})}\gamma(D)\nu^\delta=\xi(\nu,D,\phi).\)

This concludes the proof.

Note that Theorem 3 only solves the decision version whether a set of at most _k_ vertices with a certain property exists. However, the above algorithm can also easily be modified to output a set of vertices of an optimal solution by simply storing one representative of each partial solution.

## 4 Applications

In this section, we apply Theorem 3 to different problems to achieve subexponential-in-_k_ and subcubic-in-_n_ time algorithms for planar input graphs. We start with _k_-Subgraph Scoring, which acts both as an easy example of to how to use the framework and a convenient way to avoid using the framework. In particular, we will list the different steps required to apply the framework and then show how this is done in the case of _k_-Subgraph Scoring. We will then show that problems like Maximum-Weight Independent Set, Weighted Partial Vertex Cover, Densest _k_-Subgraph, and Maximum (_k,n-k_)-Cut are all special cases of _k_-Subgraph Scoring. Hence, in order to show subexponential parameterized algorithms for these (as well as weighted and directed variant of the last two), one does not need to apply the framework but can just show how to use an algorithm for _k_-Subgraph Scoring instead. Afterwards, we apply the framework to Maximum-Weight Induced Forest, Minimum-Weight Rooted Simple<tbc>

