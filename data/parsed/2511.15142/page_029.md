**Definition A.7.** The \(\varepsilon\)_-approximate conic dimension_ of a _set_ \(\mathcal{Y}\subseteq\mathbb{R}^d\) denoted by \(\mathrm{ConicDim}_\varepsilon(\mathcal{Y})\) is the largest integer _k_ for which there exists a length-_k_ sequence \(\sigma=(y_1,\dots,y_k)\in(\mathcal{Y})^k\) of points from Y, such that for each \(t\in\{2,\dots,k\}\) we have

\(\mathrm{dist}(y_t-y_1,\mathrm{env}(\sigma^{1:t-1}))\ge\varepsilon.\) (17)

All the notions previously defined extend to the approximate conic dimension with the natural changes. We can extend the notion of a basic subsequence \(B_\varepsilon(\sigma)\) following the same Kruskal-like procedure: we add an element to the basic subsequence if its distance to the previously spanned elements is at least \(\varepsilon\).

If \(k=\mathrm{ConicDim}_\varepsilon(\mathcal{Y})\) we can apply Algorithm 1 with two modifications: after the first iteration, always include the minimum point from the previous iteration in the sample; in step 2 eliminate all points \(x\in\mathcal{P}\backslash\{y\}\) such that \(\mathrm{dist}(x-y,\mathrm{env}(\sigma))<\varepsilon\) obtaining the following results:

**Corollary A.8.** _If_ \(\|w^*\|\le 1\) _and_ \(k=\mathrm{ConicDim}_\varepsilon(\mathcal{Y})\)_, the the variant of Algorithm 1 described above returns a point_ \(\hat{x}\) _such that_ \(\langle w^*,\hat{x}\rangle\le\langle w^*,x\rangle+\varepsilon\) _for all_ \(x\in\mathcal{P}\) _using_ \(O(k\mathrm{log}k\mathrm{log}|\mathcal{P}|)\) _comparisons._

_Proof._ Observe that if _y_ is the smallest point in the sampled subsequence then if \(\mathrm{dist}(x-y,\mathrm{env}(\sigma))<\varepsilon\) then let \(z\in y+\mathrm{env}(\sigma)\) be a point such that \(\|x-z\|_2\le\varepsilon\). We know that

\(\langle w^*,y\rangle\le\langle w^*,z\rangle=\langle w^*,x\rangle+\langle w^*,z-x\rangle\le\langle w^*,x\rangle+\varepsilon\)

Hence we only eliminate points that are at no better than the point _y_ by more than \(\varepsilon\). The modification in step 1 guarantees that the points _y_ selected in each iteration as increasingly better. The remainder of the proof works without any change.

Finally we bound the approximate conic dimension:

**Lemma A.9.** _The_ \(\varepsilon\)_-approximate conic dimension of any set of points_ \(\mathcal{P}\subset\mathbb{B}_d\) _is the smallest k such that_ \(2^k(\varepsilon/2)^d>(2k+1)^d\).

_Proof._ The proof follows by replacing the pigeonhole argument in Lemma A.6 by a volumetric argument. We again consider the set:

\(\big\{\sum_{i\in[k]}\beta_i(y_{i+1}-y_i):\beta_i\in\{0,1\}\big\}\subseteq 2k\cdot\mathbb{B}_d\) (18)

i.e, the ball of radius 2_k_ in R_<sup>d</sup>_, which has volume \((2k)^d\cdot\mathrm{Vol}(\mathbb{B}_d)\). Now, for each vector \(\beta\in\{0,1\}^k\), consider the ball of radius \(\varepsilon/2\) around \(\sum_{i\in[k]}\beta_i(y_{i+1}-y_i)\), which have total volume \(2^k(\varepsilon/2)^d\cdot\mathrm{Vol}(\mathbb{B}_d)\). Each of those balls is contained in the ball of radius 2_k_+1 around zero. If \(2^k(\varepsilon/2)^d>(2k+1)^d\) then two of the smaller balls must intersect, so there exist vectors \(\beta,\gamma\in\{0,1\}^k\) such that:

\(\sum_{i\in[k]}(\beta_i-\gamma_i)(y_{i+1}-y_i)=z,\) (19)

with \(\|z\|_2<\epsilon\). Let _t_<sub>0</sub> be the largest index where \(\beta_{t_0}\neq\gamma_{t_0}\), and assume \(\beta_{t_0}=0\), \(\gamma_{t_0}=1\). Doing the same manipulations as in Lemma A.6 we obtain:

\(z+y_{t_0+1}-y_1=\sum_{i\in[t_0-1]}(\beta_i-\gamma_i+1)(y_{i+1}-y_i)\) (20)

Since \(\beta_i,\gamma_i\in\{0,1\}\), the coefficients are non-negative, so

\(\mathrm{dist}(y_{t_0+1}-y_1,\mathrm{env}(y_1,\dots,y_{t_0}))\le\|z\|_2<\varepsilon\)

which shows that that \(\varepsilon\)-approximate conic dimension is at most _k_.

