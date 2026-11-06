## 5.2.2. The linear program.

We now present the linear program, constructed on the _M_-truncated coupling tree from Definition 5.4. Each node of the tree, denoted as \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\), is associated with two variables mimicking \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\) and \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\). The linear constraints of this LP are derived from the properties listed in Proposition 5.3.

**Definition 5.6** (linear program induced by the coupling)**.** Let \(\mathcal{T}=\mathcal{T}_M(\Phi,c_0)\) denote the _M_-truncated coupling tree, constructed according to Definition 5.4. Given two parameters \(0\le r_-\le r_+\), we define a linear program using variables \(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\) and \(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\) for all \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T})\):

I. _Range constraints:_<tbc>

\(\hat{p}_{(\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing,\emptyset)}^X=\hat{p}_{(\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing,\emptyset)}^Y=1;\)<br>
\(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X,\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\in[0,1],\forall(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T}).\)

II. _Non-leaf constraints:_ For each non-leaf node \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T})\backslash\mathcal{L}\):<tbc>

(a) If \(\mathcal{F}^\tau\unknown\in\mathcal{E}^\sigma\), let _c_ be the smallest constraint in \(\mathcal{F}^\tau\backslash\mathcal{E}^\sigma\) and \(\pi=\mathtt{False}(c)\):<tbc>

\(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=\hat{p}_{(\mathcal{E}\cup\{c\},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=\sum_{\rho\in[q]^{\mathrm{vbl}(c)}}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)}^X;\)<br>
\(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y=\hat{p}_{(\mathcal{E}\cup\{c\},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y+\hat{p}_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)}^Y,\forall\rho\in[q]^{\mathrm{vbl}(c)}.\)

(b) Otherwise, if \(\mathcal{F}^\tau\subseteq\mathcal{E}^\sigma\), let _c_ be the smallest constraint in \(\mathcal{E}^\sigma\backslash\mathcal{F}^\tau\) and \(\rho=\mathtt{False}(c)\):<tbc>

\(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=\hat{p}_{(\mathcal{E},\mathcal{F}\cup\{c\},\sigma,\tau,T,\varsigma)}^X+\hat{p}_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\pi)}^X,\forall\pi\in[q]^{\mathrm{vbl}(c)};\)<br>
\(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y=\hat{p}_{(\mathcal{E},\mathcal{F}\cup\{c\},\sigma,\tau,T,\varsigma)}^Y=\sum_{\pi\in[q]^{\mathrm{vbl}(c)}}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\pi)}^Y.\)

III. _Leaf constraints:_ For each leaf node \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}\):<tbc>

(a) If it is a coupled leaf \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}\),<tbc>

<tbc>\(r_-\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\le\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\le r_+\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y.\)<tbc>

(b) If it is an invalid leaf \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{invld}\),<tbc>

\(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y=0,\text{if}\sigma\text{violates}\mathcal{E};\)<br>
\(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=0,\text{if}\tau\text{violates}\mathcal{F}.\)

IV. _Truncation constraints:_ For each truncated leaf node \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}^\mathrm{trun}\):

\(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X,p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\le q^{-|\mathrm{vbl}(T)\cap V_\mathrm{good}|}\cdot\left(1-\mathrm{e}q^{-(1-\varepsilon_1)k}\right)^{-|\mathrm{vbl}(T)|p_1\alpha}.\)

**Remark 5.7.** This linear program closely resembles the one presented in \[WY24\], with the primary distinction being the last class of linear constraints: the truncation constraints. These constraints replace the "overflow constraints" used in the LP from \[WY24\]. Notably, in their design of the LP, this class of overflow constraints also distinguishes their approach from other LP-based algorithms, such as those in \[Moi19, GLLZ19, JPV21, GGGY21\], and is considered a key step in approaching the critical threshold in their context. In contrast, the use of truncation constraints here effectively captures the critical behavior of random instances and is essential for approaching the critical threshold in this new context.

## 5.3. Analysis of the linear program.

We now establish both the correctness and efficiency of the linear program constructed earlier.

