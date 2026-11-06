Therefore,

\(I(X;Q^m,Y^m)\le(1+o(1))\mathbb{E}[m]-(1-o(1))h(p)\mathbb{E}[m]\)<br>
\(\le(1+o(1))I(p)\mathbb{E}[m].\)

Combining with \(I(X;Q^m,Y^m)\ge(1-\delta-o(1))\mathrm{log}n\), we get \(\mathbb{E}[m]\ge(1-\delta-o(1))\frac{\mathrm{log}n}{I(p)}\).

**Lemma 33.** _Fix any (deterministic or randomized) algorithm for_ NoisyBinarySearch(_n_) _with error probability_ \(\delta\le 1/\mathrm{log}n\)_. Let L be the input list and x be the input element of_ NoisyBinarySearch(_n). Let U_≈ _denote the number of noisy comparisons made between x and it the predecessor and suc cessor. Then_ \(\mathbb{E}[U^\approx]\ge(2-o(1))\frac{\mathrm{log}\frac{1}{\delta}}{(1-2p)\mathrm{log}\frac{1-p}{p}}\) _, even if the position of the element to search for is uniformly random._

_Proof._ Let the input list contain elements _y_<sub>1</sub>_,...,y<sub>n</sub>_ in this order. Let _k_ be the index of the predecessor of _x_. Define _W<sub>i</sub>_ to be the number of queries returning _x\<y<sub>i</sub>_, minus the number of queries returning _x\>y<sub>i</sub>_. Note that _W<sub>i</sub>_ is a random variable depending on the transcript. We will first show that \(\mathbb{E}[U^\approx|k\unknown\in\{0,n\}]\ge(2-o(1))\frac{\mathrm{log}\frac{1}{\delta}}{(1-2p)\mathrm{log}\frac{1-p}{p}}\) . Notice that the error probability of the algorithm conditioned on \(k\unknown\in\{0,n\}\) is at most \(\frac{\delta}{\mathrm{Pr}[k\unknown\in\{0,n\}]}\le 1.1\delta\) for sufficiently large _n_.

Define _W=W<sub>k</sub>+W_<sub>_k_+1</sub>. Then E\[_W_\]=(1-2_p_)E\[_U_≈\]. Let us consider the posterior probabilities _q_ of the distributions of _k_ given a fixed transcript. That is,

\(q_i:=\mathbb{P}[k=i|Q^m,Y^m].\)

Then if \(k\unknown\in\{0,n\}\), similarly to the proof of Lemma 29, we have<tbc>

\(q_{k-1}=q_k\cdot\left(\frac{1-p}{p}\right)^{-W_k}\text{and}q_{k+1}=q_k\cdot\left(\frac{1-p}{p}\right)^{-W_{k+1}}\)

<tbc>Thus, by Jensen’s inequality,<tbc>

\(q_{k-1}+q_{k+1}\ge q_k\left(\left(\frac{1-p}{p}\right)^{-W_k}+\left(\frac{1-p}{p}\right)^{-W_{k+1}}\right)\ge 2q_k\left(\frac{1-p}{p}\right)^{-W/2}.\)

<tbc>Suppose for the sake of contradiction that<tbc>

\(\mathbb{E}[U^\approx|k\unknown\in\{0,1\}]\le(2-\sigma)\frac{\mathrm{log}\frac{1}{\delta}}{(1-2p)\mathrm{log}\frac{1-p}{p}}\)

<tbc>for some constant \(\sigma>0\). Then by Lemma 28 (taking _U_≈ as \(\tau\), _W_ as \(X_\tau\), _m_ as \(\frac{(2-\sigma/4)\mathrm{log}\frac{1}{\delta}}{\mathrm{log}\frac{1-p}{p}}\) , \(\delta\) as \(1-\frac{2-\sigma}{2-\sigma/4}\ge\sigma/4\)), with probability \(\ge\sigma/8-o_{1/\delta}(1)\), we have

\(W\le\frac{(2-\sigma/4)\mathrm{log}\frac{1}{\delta}}{\mathrm{log}\frac{1-p}{p}},\)

