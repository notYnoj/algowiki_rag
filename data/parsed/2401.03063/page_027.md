**Lemma 4.4.** _Let_ \(\varepsilon>0\)_. Let_ 0_\<p_<sub>1</sub>_\<_1_\<p_<sub>2</sub> _be such that_ \(\widetilde{\gamma}(p_1)<\widetilde{\gamma}(1)=\gamma_2\) _and_ \(\widetilde{\gamma}(p_2)<\gamma_2\) _and let_ \(\delta\in(0,\mathrm{min}(\gamma_2-\widetilde{\gamma}(p_1),\gamma_2-\widetilde{\gamma}(p_2)))\)_. Fix the integer v to be such that_ \((1+\mathrm{ln}(1+v))/v\le\delta^2\varepsilon^2/16\)_, then_

\(\mathbb{P}\left(B_{\varepsilon,p_1,p_2}^n\right)\ge 1-\mathrm{exp}\left(-n\left(\frac{\delta^2\varepsilon^2}{16}-\frac{1+\mathrm{ln}(1+v)}{v}\right)\right),\)

_for all n large enough._

_Proof._ Let \(\overrightarrow{r}\in\mathcal{R}\) be such that \(\sum_{i\in(I_{p_1,p_2}(\overrightarrow{r}))^c}N_i>\varepsilon n\). We first prove that<tbc>

\(\mathbb{E}\left(LC_n(\overrightarrow{r})-LC_n\right)\le-\frac{\delta\varepsilon n}{2},\)

<tbc>for all _n_ large enough. We follow the proof of \[14, Lemma 3.1\]. Let \(\delta^*=\mathrm{min}(\gamma_2-\widetilde{\gamma}(p_1),\gamma_2-\widetilde{\gamma}(p_2))\). Using the superadditivity of \(\widetilde{\gamma}\), we get

\(\mathbb{E}\left(LC_n(\overrightarrow{r})\right)\le\gamma_2\left(\sum_{i\in I_{p_1,p_2}(\overrightarrow{r})}\frac{N_i}{2}\right)+(\gamma_2-\delta^*)\left(\sum_{i\in(I_{p_1,p_2}(\overrightarrow{r}))^c}\frac{N_i}{2}\right)\)<br>
\(\le\left(\gamma_2-\frac{\delta^*\varepsilon}{2}\right)n.\)

Moreover, for _n_ large enough,<tbc>

\(-\mathbb{E}\left(LC_n\right)\le-\left(\gamma_2-\frac{(\delta^*-\delta)\varepsilon}{2}\right)n,\)

<tbc>so combining together these two inequalities, we get the desired result:

\(\mathbb{E}\left(LC_n(\overrightarrow{r})-LC_n\right)\le-\frac{\delta\varepsilon n}{2}.\)

The end of the proof is exactly as in \[14\], the only difference is, as pointed out in \[10, Remark 2.2\], that the cardinality of R is now \(\genfrac(){pt}{2}{n+v}{v}\) instead of \(\genfrac(){pt}{2}{n}{v}\) so ln_v_ becomes ln(1+_v_).

**Theorem 4.5.** _There exists C\>_0 _such that for all n large enough,_ \(B_1(2n)\ge C\).

_Proof._ For any \(\overrightarrow{r}\in\mathcal{R}\), let \(S(\overrightarrow{r})=\{i\in\{0,\dots,m-1\};LCS(P_i)=\mathrm{min}(v,r_{i+1}-r_i)\}\) the set of the indices of "saturated" cells, meaning that _LCS(P<sub>i</sub>_) is maximal given the size of the cell. We first show that for some \(\varepsilon>0\), with high probability, for any alignment \(\overrightarrow{r}\), \(|S(\overrightarrow{r})|\le(1-\varepsilon)m\) (still using the notation |.|=Card(.)). The idea behind this fact is that the \(\varepsilon m\) non-saturated cells will guarantee the lower bound on _B_<sub>1</sub>(2_n_), as changing their coordinates might increase _LC<sub>n</sub>_. Let _x_=0.28_,p_<sub>1</sub>=1-_x,p_<sub>2</sub>=1_/p_<sub>1</sub>, we know from \[14\] that \(\widetilde{\gamma}(p_1)<\gamma_2\) and \(\widetilde{\gamma}(p_2)<\gamma_2\). Let \(\eta=\frac{2(1-x)}{2-x}-\gamma_2\), from the upper bound \(\gamma_2\le 0.8263\), see \[20\], it that \(\eta>0\). Let \(\varepsilon\in\left(0,\frac{\eta}{2(\gamma_2+\eta)}\right)\), and, lastly, let \(\delta\in(0,\mathrm{min}(\gamma_2-\widetilde{\gamma}(p_1),\gamma_2-\widetilde{\gamma}(p_2)))\) and fix _v_ to be such that \((1+\mathrm{ln}(1+v))/v<\delta^2\varepsilon^2/16\).

Let \(C_\varepsilon^n\) be the event: for any alignment \(\overrightarrow{r}\), \(|S(\overrightarrow{r})|\le(1-\varepsilon)m\). If \((C_\varepsilon^n)^c\cap B_{\varepsilon,p_1,p_2}^n\) is realized, then there is some alignment \(\overrightarrow{r}\) such that \(|S(\overrightarrow{r})|>(1-\varepsilon)m\), and<tbc>

\(LC_n\ge\sum_{i\in S(\overrightarrow{r})\cap I_{p_1,p_2}(\overrightarrow{r})}\frac{N_i}{2}\frac{\mathrm{min}(v,r_{i+1}-r_i)}{\frac{N_i}{2}}.\)

<tbc>For any \(i\in I_{p_1,p_2}(\overrightarrow{r})\), \(r_{i+1}-r_i\in[\upsilon p_1,\upsilon p_2]\) so<tbc>

\(\frac{\mathrm{min}(v,r_{i+1}-r_i)}{\frac{N_i}{2}}\ge\frac{2}{1+p_2}=\frac{2p_1}{1+p_1}=\frac{2(1-x)}{2-x}=\gamma_2+\eta,\)

<tbc>so<tbc>

\(LC_n\ge\sum_{i\in S(\overrightarrow{r})\cap I_{p_1,p_2}(\overrightarrow{r})}\frac{N_i}{2}(\gamma_2+\eta).\)

