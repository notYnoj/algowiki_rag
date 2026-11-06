## A Discussion on Space Upper and Lower Bounds

In this section we state the lower bound of \[CJWY25\] for \(\ell_p\)-regression and restate it for undirected maximum flow (Theorem A.2). We also discuss that on unweighted (i.e., capacity 1) graphs, the max-flow can easily be stored in subquadratic space because it uses at most _O(n_<sup>1.5</sup>) edges (Theorem A.3).

**Theorem A.1** (\[CJWY25, Theorem 5\])**.** _Let_ \(p\in(1,\infty]\) _and let q=p/(p_-1) _be its Hölder conjugate exponent. Let_ \(\epsilon\in(0,1/(8q))\) _and_ \(d\in\mathbb{N}\)_. Any randomized algorithm that computes a B-bit summary of_ \(a\in\{\pm 1\}^d\) _from which_ \(\overline{x}\in\mathbb{R}^d\) _can be produced such that, with probability at least 2/3, we have_ \(a^\top\overline{x}=d\) _and_ \(\|\overline{x}\|_p\le(1+\epsilon)min_{a^\top x=d}\|x\|_p\) _requires_ \(B=\Omega(d)\).

Now, we’re ready to prove Theorem A.2.

**Theorem A.2.** _Any randomized algorithm_ E _that computes_ \(\mathcal{E}(G)\in\{0,1\}^B\) _such that with probability at least 2/3, another algorithm_ D(E(_G_)) _returns a_ \((1+\epsilon)\)_-approximate st-max flow for_ \(\epsilon\in(0,1/36)\)_, requires_ \(B=\Omega(n^2)\).

_Proof._ Given E we will construct a randomized algorithm that receives \(a\in\{\pm 1\}^d\) for _d=n_<sup>2</sup>, and computes a _B=O(B_) bit summary.

Then we show that from this summary, we can produce an \(\overline{x}\in\mathbb{R}^d\) such that \(a^\top\overline{x}=d\) and \(\|\overline{x}\|_\infty<(1+1/8)min_{a^\top x}\|x\|_\infty\).

Hence by Theorem A.1 \((p=\infty,q=1)\), this implies \(B=\Omega(n^2)\).

### Constructing the _O(B_)-bit summary

Given the vector \(a\in\{\pm 1\}^d\), we consider a complete bipartite graph _G_ with edges oriented from left to right where the capacity of the _i_-th edge is \(2+a_i\in\{1,3\}\) forall \(i\in[d]\). We add an extra vertex _s_ that connects to every vertex on the left, and an extra vertex _t_ reachable from every vertex on the right. The capacity of these edges is 4_d_ so that the maximum flow will use _f<sub>e</sub>=c<sub>e</sub>_ for all edges of the bipartite graph. We run E(_G_) to get the _B_-bit summary \(s\in\{0,1\}^B\) of a \((1+\epsilon)\)-approximate _st_-maximum flow. We also run the decoding algorithm D(_s_) on that summary to obtain the approximate flow \(f\in\mathbb{R}^E\) and compute \(\sum_{i=1}^da_i(c_i-max(1,f_i))\). Attach this sum to our summary _s_. Thus we now have a \((B+\widetilde{O}(1))\)-bit summary.

### Constructing vector <o>_x_</o> from _O(B_)-bit summary.

Given the summary, we can construct the \((1+\epsilon)\)- approximate max flow _f_ and know

\(r:=\sum_{i=1}^da_i(c_i-max(1,f_i)).\) (16)

We define for all \(i\in[d]\)

\(\overline{x_i}:=(max(1,f_i)-2)\cdot\frac{1}{1-r/d}.\) (17)

Observe that for the true max-flow, each edge of the bipartite graph would be at full capacity. So if the flow was exact, we would have _f<sub>i</sub>_-2=_a<sub>i</sub>_ and _r_=0. In particular, we would trivially have

\(a^\top\overline{x}=\sum_{i=1}^da_i^2=d.\)

