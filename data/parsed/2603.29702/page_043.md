We now prove the auxiliary claim from before:

**Claim 6.13** (Restated)**.** _Let G be an N-vertex h-layer directed graph with 0-1 edge weights with a source u. Specifically:_

• _Every vertex belongs to a layer in_ \[_h_\];<tbc>

• _For any edge from vertex v to vertex w, v’s layer is equal to w’s layer minus one;_<tbc>

• _Each edge has a weight_ \(\in\{0,1\}\).

_We say an edge is a layer-L edge if it connects a layer-L vertex to a layer-_(_L_+1) _vertex._

_Suppose that for any vertex v on layer L, for any layer_ \(L'<L+B\)_, the number of layer-_\(L'\) _edges reachable by v is at most d._

_Suppose that the edge weights satisfy the following:_

• _Each edge has weight_ 1 _with probability at most p=O_(1_/d_<sup>2</sup>);<tbc>

• _Edges from different layers are independent in weights. Specifically, let E be a set of edges, and let e be a layer-L edge. Suppose that no edge in E is also a layer-L edge. Then_ **Pr**(_e’s weight is_ 1)=**Pr**(_e’s weight is_ 1|_weights of E are known)._

_With probability_ \(1-N^{-\omega(1)}\)_, no path from u has a length (sum of edge weights) of_ \(\omega(h\sqrt{\mathrm{log}(N)}/\mathrm{min}(d,B))\).

_Proof._ Fix a vertex _v_. Fix an integer \(0\le B'<B\). Suppose that _v_ is on layer _L_. We know that there are at most _d_ layer-\((L+B')\) edges reachable by _v_. Note that _p=O_(1_/d_<sup>2</sup>). From the union bound, with probability at least 1-_O_(1_/d_), no layer-\((L+B')\) edges reachable by _v_ has weight 1. Let _X<sub>k</sub>_ be the indicator variable of whether the (_L+k_-1)-th layer contains a reachable edge with weight 1. From the independence condition in the claim statement, \(\sum_{1\le k\le\mathrm{min}(d,B)}X_k\) is the sum of min(_d,B_) independent Bernoulli random variables each with mean _O_(1_/d_), and this sum has mean _O_(1). By the standard concentration bound on this sum, the probability that, before layer-(_L_+min(_d,B_)), there are \(\omega(\mathrm{log}(N))\) layers on which there are at least one reachable edge with weight 1 (i.e., the sum is in the \(\omega(\sqrt{\mathrm{log}(N)})\)-tail), is \(N^{-\omega(1)}\). Thus with probability \(1-N^{-\omega(1)}\), there are no paths from _v_ visiting at most min(_d,B_) edges with length (sum of edge weights) \(\omega(\sqrt{\mathrm{log}(N)})\). By union bound over every vertex _v_, there are no paths visiting at most min(_d,B_) edges with length \(\omega(\sqrt{\mathrm{log}(N)})\).

Consider the longest path _p<sub>u</sub>_ from _u_. This path visits at most _h_ edges. Consider partitioning _p<sub>u</sub>_ into _O(h/_min(_d,B_)) consecutive blocks containing at most _B_ edges. Each block is a path visiting no more than min(_d,B_) edges. Thus we know that with probability \(1-N^{-\omega(1)}\), the length of each block is \(O\left(\sqrt{\mathrm{log}(N)}\right)\) and the length of _p<sub>u</sub>_ is \(O(h\sqrt{\mathrm{log}(N)}/\mathrm{min}(d,B))\).

## 6.3.4 Our Can be computed Efficiently

Finally we show that our algorithm is efficient:

**Lemma 6.11** (Restated)**.** _Computation of all_ appr _values take o(n_<sup>0.09</sup>) _time. With probability_ 1-_o_(1)_, to compute_ est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>_\]_, the running time is at most o(n_<sup>0.09</sup>)_, and the total number of edge weight queries is at most_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\).

