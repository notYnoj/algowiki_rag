We are now ready to prove Theorem 4.1, the main theorem of this section.

_Proof of Theorem 4.1._ Consider the outcome \((\mathcal{E}^\mathrm{cp},\mathcal{F}^\mathrm{cp},\sigma^\mathrm{cp},\tau^\mathrm{cp},T^\mathrm{cp},\varsigma^\mathrm{cp})\sim\mu^\mathrm{cp}\) of the random process _P_<sup>cp</sup> in Definition 4.8. We first show that for any rooted tree _T_ in \(G_\Phi\) and any \(\varsigma\in[q]^{\mathrm{vbl}(T)}\), we have

(5) \(\mathbf{Pr}\left[T^\mathrm{cp}=T\wedge\varsigma^\mathrm{cp}=\varsigma\right]\le q^{-2|\mathrm{vbl}(T)\cap V_\mathrm{good}|}\cdot\left(1-\mathrm{e}q^{-(1-\varepsilon_1)k}\right)^{-2|\mathrm{vbl}(T)|p_1\alpha}.\)

Recall the pre-generated \(\mathfrak{X}\sim\mu_{\mathcal{C}\backslash\{c_0\}}\) and \(\mathfrak{Y}\sim\mu_\mathcal{C}\), used in the construction of the process _P_<sup>cp</sup> and \(\varsigma^\mathrm{cp}\). By Lemma 4.7, there are two partial assignments \(X,Y\in[q]^{\mathrm{vbl}(T)}\) determined by _T_ and \(\varsigma\) such that

(6) \(T^\mathrm{cp}=T\wedge\varsigma^\mathrm{cp}=\varsigma\Longrightarrow\mathfrak{X}_{\mathrm{vbl}(T)}=X\wedge\mathfrak{Y}_{\mathrm{vbl}(T)}=Y.\)

Since X and Y are independent, the inequality in (5) follows from (6) and Lemma 4.11.

We proceed to prove Theorem 4.1. According to Definition 4.8, all nonempty witness trees _T_<sup>cp</sup> must be rooted at _c_<sub>0</sub>. Let \(\mathbb{T}_M^{c_0}\) denote the set of witness trees of size _M_ rooted at _c_<sub>0</sub>. Then, we have

\(\mathbf{Pr}\left[d_\mathrm{Ham}(X,Y)\ge k\cdot M\right]\)<br>
\(\text{(by Lemma 4.10)}\le\mathbf{Pr}\left[|V(T^\mathrm{cp})|=M\right]\)<br>
\(\le\sum_{T\in\mathbb{T}_M^{c_0}}\sum_{\varsigma\in[q]^{\mathrm{vbl}(T)}}\mathbf{Pr}\left[T^\mathrm{cp}=T\wedge\varsigma^\mathrm{cp}=\varsigma\right]\)<br>
\(\text{(by (5))}\le\sum_{T\in\mathbb{T}_M^{c_0}}\sum_{\varsigma\in[q]^{\mathrm{vbl}(T)}}q^{-2|\mathrm{vbl}(T)\cap V_\mathrm{good}|}\cdot\left(1-\mathrm{e}q^{-(1-\varepsilon_1)k}\right)^{-2|\mathrm{vbl}(T)|p_1\alpha}\)<br>
\(\le\sum_{T\in\mathbb{T}_M^{c_0}}q^{|\mathrm{vbl}(T)|}\cdot q^{-2|\mathrm{vbl}(T)\cap V_\mathrm{good}|}\cdot\left(1-\mathrm{e}q^{-(1-\varepsilon_1)k}\right)^{-2|\mathrm{vbl}(T)|p_1\alpha}.\)(7)

Note that for \(T\in\mathbb{T}_M^{c_0}\), the size of vbl(_T_) can be easily upper bounded by _kM_. We then lower bound \(\left|\mathrm{vbl}(T)\cap V_\mathrm{good}\right|\) as follows:

\(\left|\mathrm{vbl}(T)\cap V_\mathrm{good}\right|=\left|\mathrm{vbl}(T\cap\mathcal{E}_\mathrm{good})\cap V_\mathrm{good}\right|\)<br>
\(\text{(by Fact 3.9)}\ge\left|\mathrm{vbl}(T\cap\mathcal{E}_\mathrm{good})\right|-\varepsilon_1kM\)<br>
\(\text{(by Properties 3.5 and 3.11)}\ge(1-\eta)(1-\varepsilon_2)kM-\varepsilon_1kM.\)

Therefore, we have

\(\mathbf{Pr}\left[d_\mathrm{Ham}(X,Y)\ge k\cdot M\right]\)<br>
\(\le\sum_{T\in\mathbb{T}_M^{c_0}}q^{-(2(1-\eta)(1-\varepsilon_2)-(1+2\varepsilon_1))kM}\cdot\left(1-\mathrm{e}q^{-(1-\varepsilon_1)k}\right)^{-2kMp_1\alpha}\)<br>
\(\text{(by Property 3.6)}\le n^3\cdot(p_2\alpha)^M\cdot q^{-(2(1-\eta)(1-\varepsilon_2)-(1+2\varepsilon_1))kM}\cdot(1-\mathrm{e}q^{-(1-\varepsilon_1)k})^{-2kMp_1\alpha}\)<br>
\(\le\left(2^{3\mathrm{log}n/M}\cdot p_2\alpha\cdot q^{-(2(1-\eta)(1-\varepsilon_2)-(1+2\varepsilon_1))k}\cdot\left(1-\mathrm{e}q^{-(1-\varepsilon_1)k}\right)^{-2kp_1\alpha}\right)^M.\)

We upper bound each term in the bracket separately.

\(\bullet\) Since \(M\ge\mathrm{log}n\), it holds \(2^{3\mathrm{log}n/M}\le 8\);<tbc>

\(\bullet\) Since _p_<sub>2</sub>=e_k_<sup>2</sup>, it holds \(p_2\alpha=\mathrm{e}k^2\alpha\);<tbc>

\(\bullet\) Since \(\eta=\Theta(1/k)\), \(\varepsilon_1=\Theta(1/k)\) and \(\varepsilon_2=\Theta(1/k)\), we deduce that<tbc>

<tbc>\(2(1-\eta)(1-\varepsilon_2)-(1+2\varepsilon_1)\ge 1-2(\eta+\varepsilon_1+\varepsilon_2)=1-\Theta\left(\frac{1}{k}\right),\)<tbc>

<tbc>and hence it holds<tbc>

<tbc>\(q^{-(2(1-\eta)(1-\varepsilon_2)-(1+2\varepsilon_1))k}\le q^{-k+O(1)};\)<tbc>

