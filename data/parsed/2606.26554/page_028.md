Now, fix a single source _s_. By Lemma 5.13 and the fact that we never remove vertices from \(\hat{L}(s,r)\) for any _r_, we have that \(\hat{L}(s,r)\) are always disjoint. Thus, the overall time required by step 1 of increaseLevel is _O(Bn_), since increaseLevel is called at most \(\mathrm{ecc}(s)\le Bn\) times and in each iteration, step 1 requires \(O\left(1+\left|\hat{L}(s,\mathrm{level}(s)+1)\right|\right)\) time.

Note step 2 over all iterations requires _O(nB_log_B_) time.

Finally, in step 3, we observe that any vertex is added to and removed from A(_s,b_) exactly once. When we add or remove a vertex from A(_s,b_), we can also update the score as appropriate by maintaining a membership data structure for each \(V_i^{(b)}\). Thus, the total time required by step 3 is _O(nB_log_B_), since for every _b_ and _s_, the time at one iteration is \(\tilde{O}\left(\left|\bigcup_{\mathrm{level}(s)-b<r\le\mathrm{level}(s)}L(s,r)\right|+1\right)\). Initializing the membership data structures also requires \(\widetilde{O}\left(n\mathrm{log}B\right)\) time.

Thus, the total cost of all increaseLevel calls over all sources is at most \(\tilde{O}\left(|S_\mathrm{in}|nB\right)\) time.

## 5.3 Applications

We give some applications of our MSSP algorithm.

### 5.3.1 Hop-Set Construction

Our first application is the first non-trivial algorithm for explicitly constructing hop-sets.

**Definition 5.22.** _A set of weighted edges F is a_ \(\beta\)_-hop-set for G_=(_V,E,_wt) _if_ \(\mathrm{dist}_G(u,v)=\mathrm{dist}_{G\cup F}(u,v)\) _for all_ \(u,v\in V\) _and for every u,v, there is a path_ \(\pi\) _of at most_ \(\beta\) _hops from u to v such that_ \(\pi\) _is a shortest path between u,v._

We give an efficient algorithm for computing exact \(\beta\)-hop-sets on dense graphs, improving upon the known \(\mathrm{min}\left(n^3/\beta,n^\omega\right)\) time algorithm.

**Theorem 5.23.** _For all_ \(\beta\ge 1\)_, there is a randomized_ \(Bn^{o(1)}\mathsf{T}_\mathrm{MUL}(n/\beta,n,n)\) _time algorithm that computes a_ \(\beta\)_-hop-set with_ \(\widetilde{O}\left(n^2/\beta^2\right)\) _edges on undirected graphs with integer weights in_ \[_B_\].

_Proof._ When \(\beta\le 30\mathrm{log}n\), we observe that the theorem is true by computing APSP in _Bn_<sup>_o_(1)</sup>T<sub>MUL</sub>(_n,n,n_) time and adding edges of weight dist(_u,v_) between every pair of vertices. Thus, we assume \(\beta>30\mathrm{log}n\). Consider the following algorithm.

1. **Input:** Undirected graph _G_ with integer weights in \[_B_\].<tbc>

2. Sample \(S\subseteq V\) by including each vertex independently with probability \(\frac{30\mathrm{log}n}{\beta}\)<tbc>

3. Compute \(\widehat{\mathrm{d}}(S,V)\leftarrow\mathrm{MSSP}(G,S)\).<tbc>

4. Compute \(F\leftarrow\{(a,b)\text{s.t.}a,b\in S\}\) where edge (_a,b_) has weight \(\widehat{\mathrm{d}}(a,b)\).<tbc>

5. **Output:** Weighted edge set _F_.

First, we argue that _F_ is a \(\beta\)-hop-set. Consider a shortest path of at least \(\beta/3\) nodes. Then, the probability that none of these nodes is included in _S_ is at most

\(\left(1-\frac{30\mathrm{log}n}{\beta}\right)^{\beta/3}\le n^{-10}\)

so that union bounding over _O(n_<sup>2</sup>) shortest paths, we can ensure with high probability that all shortest paths of at least \(\beta/3\) nodes include one node in _S_. Then, for any shortest path of length \(\ell\ge\beta\), \(\pi=v_0,\dots,v_{\beta/3},\dots,v_{\ell-\beta/3},\dots,v_\ell\), we have \(v_i,v_j\in S\) for \(i\le\beta/3\) and \(j\ge\ell-\beta/3\). Then, adding _F_, we have<tbc>

