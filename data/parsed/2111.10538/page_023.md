We now use the fact that \(\mathsf{NF}_\lambda\) is dense to argue that it contains a large bi-clique.

**Claim 3.11** (\(\mathsf{NF}_\lambda\) contains a large bi-clique)**.** _With probability at least_ 0.98 \(\mathsf{NF}_\lambda\)_, contains a complete bipartite subgraph_ \(K_{\gamma/(5\beta),\gamma/(5\beta)}\).

_Proof._ Using Turán’s Theorem (Lemma A.4), we know, for any integer \(s\ge 2\), that a graph _G_ with _n_ vertices and _n_<sup>2-1_/s_</sup> edges has at least one _K<sub>s,s</sub>_ subgraph. We apply this to graph \(\mathsf{NF}_\lambda\). Since \(\lambda\) is constant then \(\beta/\gamma\) becomes constant and thus \(|V(\mathsf{NF}_\lambda)|^{\beta/\gamma}\) is super constant. It follows from Claim 3.9 that

\(|E(\mathsf{NF}_\lambda)|\ge\frac{|V(\mathsf{NF}_\lambda)|^{2-4\beta/\gamma}}{128}>|V(\mathsf{NF}_\lambda)|^{2-5\beta/\gamma}\)

holds with probability at least 0.98. This in turn implies that with probability at least 0.98 \(\mathsf{NF}_\lambda\) contains a complete bipartite subgraph \(K_{\gamma/(5\beta),\gamma/(5\beta)}\).

The last step in the proof is to use the large bi-clique to exhibit an undetected-constructive tuple.

**Lemma 3.12.** _Let X and Y be two sets of windows such that for every_ \(w_i\in X\) _and_ \(w_j\in Y\) _there is an edge_ (_i,j_) _in_ \(E(\mathsf{NG}_\lambda)\)_. If_ \(|X|\ge 16\mathsf{w}_\mathsf{layers}\mathsf{w}_\mathsf{gap}/(\epsilon\lambda^3)\) _and_ \(|Y|\ge 16\mathsf{w}_\mathsf{layers}\mathsf{w}_\mathsf{gap}/(\epsilon\lambda^3)\)_, then there exist_ \(w_i,w_a,w_b,w_j\in X\cup Y\) _such that_ \(\langle w_i,w_a,w_b,w_j\rangle\) _is_ \((\epsilon,\lambda)\)_-constructive, i.e.,_

\(\left\|\mathsf{opt}_{i,a}\cap\mathsf{opt}_{a,b}\cap\mathsf{opt}_{b,j}\right\|\ge(1-\epsilon)\lambda^3\)

_and either_ \(w_i,w_b\in X\) _and_ \(w_a,w_j\in Y\) _or_ \(w_i,w_b\in Y\) _and_ \(w_a,w_j\in X\).

_Proof._ Let \(\epsilon'=\epsilon/4\). By assumption, we know that \(|X|,|Y|\ge 4\mathsf{w}_\mathsf{layers}\mathsf{w}_\mathsf{gap}/(\epsilon'\lambda^3)\). Moreover the total number of different window sizes is bounded by w<sub>layers</sub>. Thus, there exist two sets \(\widehat{X}\subseteq X\) and \(\widehat{Y}\subseteq Y\) such that \(|\widehat{X}|,|\widehat{Y}|\ge 4\mathsf{w}_\mathsf{gap}/(\epsilon'\lambda^3)\) and the windows within \(\widehat{X}\) are of the same size and the windows within \(\widehat{Y}\) are of the same size (though the windows of \(\widehat{X}\) and \(\widehat{Y}\) may have different sizes). Let _d<sub>x</sub>_ denote the window size for each window in \(\widehat{X}\), and _d<sub>y</sub>_ denote the window size for each window in \(\widehat{Y}\).

We select \(X'\subseteq\widehat{X}\) and \(Y'\subseteq\widehat{Y}\) such that

1. \(|X'|\ge 4/(\epsilon'\lambda^3)\).<tbc>

2. \(|Y'|\ge 4/(\epsilon'\lambda^3)\).<tbc>

3. \(|X'|d_x\le(1+\epsilon')|Y'|d_y\).<tbc>

4. \(|Y'|d_y\le(1+\epsilon')|X'|d_x\).

To do this, if \(|\widehat{X}|d_x>(1+\epsilon')|\widehat{Y}|d_y\), then we set \(Y'=\widehat{Y}\) and select \(X'\) as an arbitrary subset of \(\widehat{X}\) with size \(\left\lceil\frac{|Y'|d_y}{d_x}\right\rceil\). Otherwise, we set \(X'=\widehat{X}\) and select \(Y'\) an arbitrary subset of \(\widehat{Y}\) with size \(\left\lceil\frac{|X'|d_x}{d_y}\right\rceil\).

We define a character-based (bipartite) graph _G<sub>C</sub>_=(_V<sub>C</sub>,E<sub>C</sub>_) as follows: Each window of \(X'\) has _d<sub>x</sub>_ nodes in the character-based graph such that each node represents a character of the window. Similarly, each window of \(Y'\) has _d<sub>y</sub>_ nodes in the character-based graph. Two nodes _x,y_ in the character-based graph are adjacent if and only if \((x,y)\in\mathsf{opt}_{i,j}\) where _w<sub>i</sub>_ is the window containing character _x_ and _w<sub>j</sub>_ is the window containing character _y_. Let \(l_x=|X'|\) and \(l_y=|Y'|\).

