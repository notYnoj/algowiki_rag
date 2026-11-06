### Case 2: \(P\subset E_2\) and \(P\unknown\subset E_3\)

Let \(e=(a,b)\in E_2\backslash E_3\) be the closest such edge to _v_ so that \(\text{rank}_a(e),\text{rank}_a(b)\ge s_2\). Let _b_ be the closest vertex to _v_. Then, there is \(x\in D_2\) such that \((x,b)\in E_2^*\) and \(\text{rank}_b(x,b)<s_2\le\text{rank}_b(e)\). When we execute **Dijkstra** from _x_, since \(P\subset E_2\), we find,<tbc>

\(\hat{\delta}(x,u)\le\delta(b,u)+\mathsf{wt}(x,b)\le\delta(b,u)+\mathsf{wt}(a,b)\)

<tbc>Then, when we execute **Dijkstra** from _u_, we use the edge (_u,x_) and obtain,

\(\hat{\delta}(u,v)\le\hat{\delta}(x,u)+\mathsf{wt}(x,b)+\delta(b,v)\le\delta(u,v)+2\mathsf{wt}(a,b)\le\delta(u,v)+2h(P)\)

### Case 3: \(P\subset E_3\)

Note _D_<sub>3</sub>=_V_ . In this case, \(P\subset E_3\) so that when we execute **Dijkstra** from \(u\in D_3\) we find exactly the path _P_ and therefore \(\hat{\delta}(u,v)\le\delta(u,v)\).

In all cases, we obtain an approximation \(\hat{\delta}(u,v)\le(1+\varepsilon)\delta(u,v)+2h(P)\) for some shortest path _P_. We complete the proof by taking the minimum over all shortest paths _P_.

_Proof._ (Time Complexity)

The analysis of time complexity is extremely similar to that of Deng et al. \[DKR<sup>+</sup>22\].

From Lemma 6.1, both calls to **WeightedDecompose** require time \(\tilde{O}(n^2)\). In Phase 1, for a fixed \(i\in[l]\), we can bound \(|C_i|=\tilde{O}(t_i)\) and each graph _F<sub>i</sub>_ has at most \(O\left(\frac{n^2}{t_i}\right)\) edges so that all invocations of **Dijkstra** require \(\tilde{O}(n^2)\) time over all _l_. Since \(|C_i|\le\tilde{O}(t_i)=\tilde{O}(n^{1-x})\), the invocations of **ApproximateMinPlus** requires \(\tilde{O}\left(\frac{n^{\omega(1,1-x,1)}}{\varepsilon}\right)\) time.

In Phase 2, \(|D_2|=\tilde{O}(n^{1-x/2}),|E_2|=O(n^{1+x})\) and \(|D_3|=\tilde{O}(n^{1-x}),|E_3|=O(n^{1+x/2})\) so that both invocations of **Dijkstra** require \(\tilde{O}(n^{2+x/2})\) time.

Thus, we solve for _x_ as the solution to,

\(\omega(1,1-x,1)=2+\frac{x}{2}\)

Using \[Bra\], we choose _x_=0.30390661 and obtain the running time \(\tilde{O}(n^{2.15195331})\).

## 6.2 \((1+\varepsilon,\beta w)\) Approximation for \(\beta\ge 4\)

We now extend Algorithm 6 to handle weighted graphs, proving the following analogue of Theorem 5.6.

**Theorem 6.3.** _Let_ \(\beta\ge 2\) _be an integer and_ \(\varepsilon>0\)_. Let G be an undirected, unweighted graph with n vertices. Algorithm 9 computes_ \(\hat{\delta}\) _such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\le(1+\varepsilon)\delta(u,v)+2w_{u,v}(\beta)\) _in time_ \(\tilde{O}\left(\frac{n^{2+\frac{x}{\beta+1}}}{\varepsilon}\right)\) _where x is the solution to,_ \(\omega\left(1-\frac{\beta-1}{\beta+1}x,1-x,1-\frac{\beta-2}{\beta+1}x\right)=2+\frac{x}{\beta+1}\)_. Here,_ \(w_{u,v}(\beta)\) _denotes the total weight of the_ \(\beta\) _heaviest edges of a shortest path P._

### High Level Overview

The weighted approximation differs from **AdditiveAPASP** in two key points. First, we use a weighted decomposition of the graph computed by **WeightedDecompose** in place of **Decompose**. Second, we compute an _approximate_ (min,+) product with in place of an _exact_ (min,+) product.

Whereas **Decompose** returns edge sets _E<sub>i</sub>_ which require that at least one endpoint is of low degree, **WeightedDecompose** returns edge sets _E<sub>i</sub>_ which contain the _s_<sub>_i_-1</sub> edges of least weight incident to each vertex. In particular, for a given vertex _v_ of level _j_, there is an edge (_v,v_<sup>∗</sup>) to \(v^*\in D_j\) that is among the _s_<sub>_j_-1</sub> lightest edges incident to _v_. This ensures that when we encounter<tbc>

