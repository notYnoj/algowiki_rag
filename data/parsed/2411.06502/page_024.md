<tbc>derive the distances between any two nodes in the former graph from the distances in the latter graph, and vice versa.

To see this, observe that \(\tilde{\mathbf{G}}[i..j][i'..j']\) can be obtained from the subgraph of \(\tilde{\mathbf{G}}\) induced by the vertex set \([i..j]\times[i'..j']\) by performing the following steps iteratively for each \(z\in[i..j)\) where \(v_z\notin\mathbf{F}[l(v_i)..l(v_j))\) (and a similar process for each \(z'\in[i'..j')\) where \(v'_{z^\prime}\notin\mathbf{F}[l(v'_{i^\prime})..l(v'_{j^\prime})))\): identify the vertex \((z,z')\) with vertex \((z+1,z')\) for all \(z'\in[i'..j']\). Throughout these iterations, (_i,j_) denotes the vertex where the vertex (_i,j_) of the subgraph of \(\tilde{\mathbf{G}}\) formed by the vertex set \([i..j]\times[i'..j']\) might have potentially merged.

Let \(\tilde{\mathbf{G}}^{+z}\) be the graph before applying the step for some _z_, and \(\tilde{\mathbf{G}}^{-z}\) denote the graph obtained after this step. Since \(v_z\notin\mathbf{F}[l(v_i)..l(v_j))\), it follows that \(\pi_\mathbf{F}(z)>j\). Therefore, no vertex in \(z\times[i'..j']\) has an outgoing edge of the form (c) in \(\tilde{\mathbf{G}}^{+z}\). Moreover, \(\pi_\mathbf{F}^{-1}(z+1)=\emptyset\), as otherwise it would contradict \(\pi_\mathbf{F}(z)>j\). Thus, no vertex in \((z+1)\times[i'..j']\) has an incoming edge of the form (c) in \(\tilde{\mathbf{G}}^{+z}\). It is not difficult to see that for any pair \((\bar{u},\bar{w})\) where at most one of \(\bar{u},\bar{w}\) is contained in \(\{z,z+1\}\times[i'..j']\), we have \(\mathrm{dist}_{\tilde{\mathbf{G}}^{+z}}(\bar{u},\bar{w})=\mathrm{dist}_{\tilde{\mathbf{G}}^{-z}}(\bar{u},\bar{w})\). Now, it is not difficult to see that if \(\bar{u},\bar{w}\in\{z,z+1\}\times[i'..j']\), then the distance between \(\bar{u}\) and \(\bar{w}'\) in \(\tilde{\mathbf{G}}^{+z}\) and \(\tilde{\mathbf{G}}^{-z}\) is zero if \(\bar{w}\) is reachable from \(\bar{w}\) in \(\tilde{\mathbf{G}}^{+z}\) and \(\tilde{\mathbf{G}}^{-z}\), respectively, and \(-\infty\) otherwise.

## 4.2 FED as border-to-border distances in an alignment graph

Our focus lies in computing paths from the lower-left to the upper-right border of an alignment graph.

We write \((\mathbf{w},\mathbf{F},\mathbf{F}')\)-BBD for the BBD instance with input \(\mathbf{F},\mathbf{F}'\) and w. Moreover, given a \((\mathbf{w},\mathbf{F},\mathbf{F}')\)- BBD instance we say \(\mathrm{max}(n,n')\) is the _size_ of the instance. Note, given a BBD instance of size _m_, the output of such instance is of size O(_m_<sup>2</sup>). Finally, we say that a \((\mathbf{w},\mathbf{F},\mathbf{F}')\)-BBD instance has _diameter_ D if \(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{u},\bar{w})\le\mathrm{D}\) for all \(\bar{u}\in\mathrm{B}^\perp(1,1,n+1,n'+1)\) and \(\bar{w}\in\mathrm{B}^\top(1,1,n+1,n'+1)\) i.e. if the alignment graph \(\tilde{\mathbf{G}}\) has diameter D.

**Lemma 4.5.** _Let_ \(\mathbf{F},\mathbf{F}'\) _be forests with pre-orders v_<sub>1</sub>_,...,v_<sub>|**F**|</sub> _and_ \(v'_1,\dots,v'_{|\mathbf{F}^\prime|}\)_. Then, FED on_ **F** _and_ \(\mathbf{F}'\) _can be reduced to BBD on_ \((\mathbf{w}_{\mathbf{F},\mathbf{F}^\prime},\mathbf{F},\mathbf{F}')\)_, where_ \(\mathbf{w}_{\mathbf{F},\mathbf{F}^\prime}(i,i')=\mathrm{sim}(\mathrm{sub}(v_i),\mathrm{sub}(v'_{i^\prime}))\) _for_ \((i,i')\in[1..|\mathbf{F}|]\times[1..|\mathbf{F}'|]\).

**Proof.** Recall Shasha and Zhang’s dynamic programming algorithm \[SZ89\] for computing the similarity between two forests **F** and \(\mathbf{F}'\) with pre-order _v_<sub>1</sub>_,...,v_<sub>|**F**|</sub> and \(v'_1,\dots,v'_{|\mathbf{F}^\prime|}\), described by the following recursive formula:

\(\mathrm{sim}(\mathbf{F},\mathbf{F})=\left\{\begin{array}{ c c }
0, & \text{if}\mathbf{F}=\emptyset\text{or}\mathbf{F}'=\emptyset, \\
\mathrm{max}\left\{\begin{array}{ c }
\mathrm{sim}(\mathbf{F}\backslash v_1,\mathbf{F}'), & \text{otherwise.}
\end{array}\right.\)

Consider arbitrary \([i..j]\subseteq[1..(|\mathbf{F}|+1)]\) and \([i'..j']\subseteq[1..(|\mathbf{F}'|+1)]\). Then, the dynamic programming computation of the longest path in \(\tilde{\mathbf{G}}[i..j][i'..j']\) between \((i,i')\) and \((j,j')\) aligns with the computation done by Shasha and Zhang’s scheme for \(\mathrm{sim}(\mathbf{F}[l(v_i)..l(v_j)),\mathbf{F}'[l(v'_{i^\prime})..l(u'_{j^\prime})))\). This allows us, given \(x,y\in[1..(2|\mathbf{F}|+1)]\) such that \(x\le y\), to find two nodes in the grid whose longest distance equals

