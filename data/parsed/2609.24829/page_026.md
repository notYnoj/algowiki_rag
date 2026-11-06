The oracle will henceforth be used to _define_ whether an edge is heavy or light.<sup>1</sup> Let \(E_\mathbb{H}=\{e\in E:\mathrm{oracle}(e)=\mathbb{H}\}\) and let \(\tilde{T}_0\) be the number of triangles amongst _S_\\_E_<sub>H</sub>. Define<tbc>

<tbc>\(X=\tilde{T}_0C^2+\frac{1}{p}\sum_{e\in P\cap E_\mathbb{H}}\left(t_{e,0}^O+t_{e,1}^O/2+t_{e,2}^O/3\right)\)<tbc>

<tbc>where \(t_{e,i}^O\) is the number of triangles including _e_ where _i_ of the other two edges in _O_ are heavy. The coefficients of \(t_{e,i}^O\) take into account that a triangle with multiple heavy edges can be counted from the perspective of multiple edges and hence we need to compensate for overcounting. If \(X\ge\tau(1-\varepsilon)\) return _X_, if not output `FAIL`.

## A.2 Analysis

We first analyze the space used by the algorithm:

**Theorem A.1** (Space Bound)**.** _The expected space used by the algorithm is_ \(\tilde{O}(\varepsilon^{-2}\delta^{-2}(m/\sqrt{\tau}+T/\tau))\).

_Proof._ The expected numbers of edges in all of the _E<sub>i</sub>_ sets is at most<tbc>

\(m\sum_{i=0}^{\mathrm{log}\sqrt{\tau}}2p_iq_i=O(1)\cdot m\sum_{i=0}^{\mathrm{log}\sqrt{\tau}}2^i/\sqrt{\tau}\cdot\delta^{-1}\varepsilon^{-2}\mathrm{log}(n)/2^i\le\tilde{O}(\delta^{-1}\varepsilon^{-2}m/\sqrt{\tau}).\)

<tbc>The expected number of edges in _P_ is at most

\(\sum_{i=0}^{\mathrm{log}\sqrt{\tau}}t_ep_iq_i^2=O(\delta^{-1}\varepsilon^{-2}\mathrm{log}n)\cdot\sum_{i=0}^{\mathrm{log}\sqrt{\tau}}t_e2^{2i}/\tau\cdot 1/2^i=O(\delta^{-1}\varepsilon^{-2}\mathrm{log}n)\cdot\sum_{i=0}^{\mathrm{log}\sqrt{\tau}}t_e2^i/\tau=O(\delta^{-1}\varepsilon^{-2}(\mathrm{log}n)T/\sqrt{\tau}).\) (9)

The expected number of edges in _S_ is \(m/C=O(\varepsilon^{-2}\delta^{-1}m/\sqrt{\tau})\).

To prove the accuracy guarantees we will argue that a) the oracle distinguishes between edges _e_ with large or small _t<sub>e</sub>_ values with sufficient accuracy, b) the algorithm stores almost all edges with large _t<sub>e</sub>_ values, and c) the number of triangles made of edges with small _t<sub>e</sub>_ values, can be accurately estimated using the colorful sampling.

We start by proving the oracle guarantees in a way that covers both P-PASS and the verified algorithm. We remind the reader of the relevant lemma.

**Lemma 4.2.** Let \(1\le\gamma\le n\) be some predetermined threshold. Let _V<sub>p</sub>_ be a collection of vertices sampled independently with probability \(p=\mathrm{min}(1,50\varepsilon^{-2}(\mathrm{log}n)/\gamma)\). Let _O_ be the set of edges incident to at least one vertex in _V<sub>p</sub>_. Define a function

\(\mathrm{oracle}(e)=\left\{\begin{array}{ c c }
\mathbb{L} & \text{if}t_e^O<p\gamma \\
\mathbb{H} & \text{otherwise}
\end{array}\right.\)

With probability (1-1_/n_<sup>3</sup>), if oracle(_e_)=H then \(t_e^O=(1\pm\varepsilon)t_ep\), and if oracle(_e_)=L then \(t_e\le 2\gamma\).

<sup>1</sup>That is, while we will later show that _e_ being defined as heavy/light will roughly correspond to whether _t<sub>e</sub>_ is larger/smaller than \(\sqrt{\tau}\), the actual definition is a function of the edges sampled by the algorithm; this will help significantly with the analysis. Note that the oracle is defined independently of the ordering of the data stream because \(E_{\mathrm{log}(\sqrt{\tau})}\) is constructed based on the entire stream rather than a strict prefix.

