\(\le exp\left(-\frac{\varepsilon^2p^6max(T,\tau)^2}{2p(1-p)\sum_{i\in[m^\prime]}(2c_i)^2+2/3\cdot\varepsilon p^3max(T,\tau)max_i(2c_i)}\right)+(1-Pr[\Gamma])\sum_i\frac{1}{\gamma_i}\)

<tbc>To bound the second term, first note that by an application of the Chernoff bound<tbc>

\(Pr[Y_i>c_i]=Pr[Y_i>\mathbb{E}[Y_i]+(1+\frac{30lnn}{p^2t_i})\mathbb{E}[Y_i]]\le\left\{\begin{array}{ c c }
exp(-p^2t_i/3) & \text{if}p^2t_i\ge 30lnn \\
exp(-(30lnn)/3) & \text{if}p^2t_i\le 30lnn
\end{array}\right.\)

<tbc>and is at most _n_<sup>-10</sup> in either case. Hence, we can bound the second term using the union bound as follows:<tbc>

\((1-Pr[\Gamma])\sum_{i\in[m^\prime]}\frac{1}{\gamma_i}\le 3T\sum_{i\in[m^\prime]}n^{-10}\le n^{-6}\)

<tbc>To bound the first term, note that by using the inequality that \((x+y)^2\le 2x^2+2y^2\),

\(2p(1-p)\sum_{i\in[m^\prime]}(2c_i)^2+2/3\cdot\varepsilon p^3Tmax_i(2c_i)\) (2)

\(\le 8p\sum_{i\in[m^\prime]}(2p^4t_i^2+1800ln^2n)+4/3\cdot\varepsilon p^3max(T,\tau)max_ic_i\) (3)

\(=16p\sum_{i\in[m^\prime]}p^4t_i^2+14400p\sum_{i\in[m^\prime]}ln^2n+4/3\cdot\varepsilon p^3max(T,\tau)max_ic_i\) (4)

\(\le 48p^5T\eta+43200pTln^2n+4/3\cdot\varepsilon p^3max(T,\tau)max_ic_i\) (5)

\(\le max(T,\tau)\cdot(48p^5\eta+43280pln^2n+8/3\cdot\varepsilon p^5\eta)\)

Hence,

\(Pr[f(X_1,\dots,X_{m^\prime})\ge(1+\varepsilon)p^3T]\le exp\left(-\frac{\varepsilon^2p^6max(T,\tau^*)}{\Theta(p^5\eta+pln^2n+\varepsilon p^5\eta)}\right)+n^{-6}\)

The lower tail bound follows identically.

**Remark 4.5.** _In particular, when_ \(T\ge\tau\)_, with probability_ \(\ge 1-n^{-4}\), \(T_p\in(1\pm\varepsilon)p^3T\).

We proceed to show the guarantees of the oracle used in pass 3_i_.

**Lemma 4.2.** Let \(1\le\gamma\le n\) be some predetermined threshold. Let _V<sub>p</sub>_ be a collection of vertices sampled independently with probability \(p=min(1,50\varepsilon^{-2}(logn)/\gamma)\). Let _O_ be the set of edges incident to at least one vertex in _V<sub>p</sub>_. Define a function

\(oracle(e)=\left\{\begin{array}{ c c }
\text{L} & \text{if}t_e^O<p\gamma \\
\text{H} & \text{otherwise}
\end{array}\right.\)

With probability (1-1_/n_<sup>3</sup>), if oracle(_e_)=H then \(t_e^O=(1\pm\varepsilon)t_ep\), and if oracle(_e_)=L then \(t_e\le 2\gamma\).

_Proof._ For every edge, \(t_e^O\sim Bin[t_e,p]\). The result follows from standard applications of the Chernoff bound and taking the union bound over all edges. We provide a detailed proof in A for completeness.

We use this lemma repeatedly, with different thresholds \(\gamma\) and different sampling probabilities. We mention that the correctness of the first pass is proved in Claim 3.4 and proceed to the main part of the algorithm.

