We extend Roditty’s deterministic algorithm that uses 4 levels significantly to consider _k_+1=8 levels. We handle paths of length longer than twelve using a (1,12)-approximation algorithm of \[DHZ00\] which requires time _n_<sup>2+1/17</sup> and does not dominate the total running time. We consider the following degree thresholds \(s_0=n^x,s_1=n^\frac{6}{7}x,s_2=n^\frac{5}{7}x,\dots,s_6=n^\frac{1}{7}x\) and _s_<sub>7</sub>=0. We will leave _x_ as a parameter to be optimized later. Given these degree thresholds, we compute dominating sets \(D_0\subset D_1\subset\dots\subset D_6\subset D_7=V\) according to `Decompose` (Lemma 2.6) where _D<sub>i</sub>_ dominates \(V_i=\{v\in V\text{s.t.}\mathrm{deg}(v)\ge s_i\}\) and \(E_i=\{(u,v)\in E\text{s.t.}\mathrm{min}(\mathrm{deg}(u),\mathrm{deg}(v))<s_{i-1}\}\) for _i_=0,1_,..,_7 (take _s_<sub>-1</sub>=_n_+1).

## High Degree Vertices: Paths of length \(\le C\).

We handle high degree vertices in a similar way as we did for our randomized algorithm, that is we compute a dominating set of size \(\tilde{O}\left(n^{1-x}\right)\) in \(\tilde{O}\left(n^2\right)\) time, and compute `boundedMinPlus` to obtain a +2-additive approximation of all paths of length at most _C_ going through some vertex in _V_<sub>0</sub>. This step requires \(\tilde{O}\left(n^{\omega(1,1-x,1)}\right)\) time.

## Paths of length \(\ge C\).

For paths of lengths at least _C_=12, we will use known results from \[DHZ00\]. Consider paths _P_ such that all vertices on _P_ have degree less than _n<sup>x</sup>_. Here, we have decomposed the remaining graph into _k_=7 levels. `SparseAPASP` with _k_=7 levels achieves a +12 approximation. So, we can simply run it. The algorithm `SparseAPASP` executes \(\text{\texttt{Dijkstra}}(G_{i,w},w,\hat{\delta})\) from all \(w\in D_i\) where \(G_{i,w}=(V,E_i\cup E^*\cup(w\times V))\) is equipped with the current estimates \(\hat{\delta}\) as edge weights, which requires \(\tilde{O}(n^{2+\frac{x}{7}})\) time as _D<sub>i</sub>_ has size \(\tilde{O}(n^{1-\frac{7-i}{7}x})\) and the graph _G<sub>i,w</sub>_ has \(O\left(n^{1+\frac{7-(i-1)}{7}x}\right)\) edges. If path _P_ has a vertex in _V_<sub>0</sub>, then we can run `DenseAPASP` with a run ning time of \(\tilde{O}\left(n^{2+1/17}\right)=\tilde{O}\left(n^{2.0588}\right)\). Again, since we only need `DenseAPASP` to compute good approximations on paths with high degree vertices, we can choose any constant value of _C_ large enough such that executing `DenseAPASP` does not dominate the running time.

## Low Degree Vertices: Paths of length \(\le C\).

## Paths of length 6 or more

For paths of length at least 6, we compute a +6 approximation following `boundedAdaptiveAPASP` in Section 5.3. We give a brief overview here with special attention to the specific application required with more details provided in Section 5.3. We use fast rectangular matrix multiplication judiciously to improve upon \[DHZ00\].

We compute `BoundedAdaptiveAPASP` on the original graph _G_ and therefore choose new degree thresholds and use a new degree decomposition of the graph _G_. We first describe our algorithm combinatorially, and then mention where fast matrix multiplication can be applied. For a full discussion, see Section 5.3. To obtain a +6 approximation, choose 7 degree thresholds _r_<sub>1</sub>_,...,r_<sub>7</sub> and decompose the vertex and edge sets of _G_ as \(C_1\subset\dots\subset C_8=V\) and \(F_8\subset F_7\subset\dots\subset F_1=E\). At level _i_, compute `Dijkstra` from each \(w\in C_i\) on the graph

\(G_{i,w}=\left(V,F_i\cup\left(\bigcup_{i+j_1+j_2\le 17}C_{j_1}\times C_{j_2}\right)\cup F^*\cup(w\times V)\right)\)

noting that both \(F_i,C_{j_1}\times C_{j_2}\) have size \(O\left(n^{1+\frac{8-(i-1)}{8}}\right)\). Here \(F^*=\bigcup_{i=1}^7F_i^*\) is output by `Decompose`.

Consider a shortest path _P_. We use the following definition of blocking vertices and blocking levels.

