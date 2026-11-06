<tbc>Therefore:

\(\mathbb{E}\left[\sum_{e\in E^\mathrm{H}\backslash P}t_e\right]\le\sum_{e\in E^\mathrm{H}}\frac{4\delta\sqrt{\tau}}{\varepsilon^{-2}t_e}\cdot t_e\le|E^\mathrm{H}|\cdot\frac{4\delta\sqrt{\tau}}{\varepsilon^{-2}}\le\frac{16\delta T}{\varepsilon^{-2}}\)

using the fact \(|E^\mathrm{H}|\le 4T/\sqrt{\tau}\). The result then follows by an application of the Markov bound assuming \(\varepsilon<1/16\).

The total number of triangles can be written as:

\(T=T_0+\sum_{e\in E_\mathrm{H}}\left(t_{e,0}+t_{e,1}/2+t_{e,2}/3\right)\)

where _T_<sub>0</sub> is the number of triangles with 0 heavy edges and _T_<sub>H</sub> is the number of triangles with at least 1 heavy edge. _t<sub>e,i</sub>_ is the number of triangles including _e_ where exactly _i_ of the other edges are heavy. The next two lemmas consider errors incurred when estimating the terms _T_<sub>0</sub> and _T_<sub>1</sub>+_T_<sub>2</sub>+_T_<sub>3</sub>.

**Lemma A.3** (Light Triangles)**.** \(\mathrm{Pr}\left[|\tilde{T}_0C^2-T_0|\ge\varepsilon\mathrm{max}(T,\tau/2)\right]\le\delta\).

_Proof._ Since \(C\le\tau\), we can bound the variance as:<tbc>

\(\mathrm{Var}\left[\tilde{T}_0C^2\right]\le T_0C^2+3T_0C\cdot(\eta_\mathrm{L}-1)\le T_0C^2+6T_0\sqrt{\tau}C\le 7CT_0\sqrt{\tau}\)

<tbc>where \(\eta_\mathrm{L}\le 2\sqrt{\tau}\) is the maximum number of triangles amongst _E_\\_E_<sub>H</sub> sharing the same edge. Hence, by an application of Chebyshev bound<tbc>

\(\mathrm{Pr}\left[|\tilde{T}_0C^2-T_0|\ge\varepsilon\mathrm{max}(T,\tau/2)\right]\le\frac{7CT_0\sqrt{\tau}}{\varepsilon^2\mathrm{max}(T,\tau/2)^2}\)

<tbc>If \(T\ge\tau/2\), this is at most<tbc>

\(7C\sqrt{\tau}\varepsilon^{-2}T^{-1}\le 14C\varepsilon^{-2}/\sqrt{\tau}\)

<tbc>and if \(T\le\tau/2\), this is also at most

\(7C\sqrt{\tau}(\tau/2)\varepsilon^{-2}(\tau/2)^{-2}\le 14C\varepsilon^{-2}/\sqrt{\tau}.\)

Hence, setting \(C=\delta\varepsilon^2\sqrt{\tau}/14\) suffices to ensure the probability is at most \(\delta\).

**Lemma A.4** (Heavy Triangles)**.** With probability at least 1-1/poly(_n_),<tbc>

\(\frac{1}{p}\sum_{e\in E_\mathrm{H}}\left(t_{e,0}^O+t_{e,1}^O/2+t_{e,2}^O/3\right)=(1\pm\varepsilon)(T_1+T_2+T_3).\)

<tbc>_Proof._ By an application of the Chernoff bound, for each heavy edge _e_, with high probability

\(t_{e,0}^O+t_{e,1}^O/2+t_{e,2}^O/3=(1\pm\varepsilon)p(t_{e,0}+t_{e,1}/2+t_{e,2}/3).\)

The result follows by summing over the heavy edges.

We conclude with the proof of Theorem 3.1.

