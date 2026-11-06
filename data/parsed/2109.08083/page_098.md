<tbc>We know from Theorems 6.1 and 6.12 that there are \(O\left(t_jp_\mathrm{gr}^3\right)\) such edges, and that there are \(\Theta\left(t_{j+1}p_\mathrm{gr}^3\right)\) edges containing _v_ in _H_<sub>1∗</sub>\[_I_<sub>_t<sub>j</sub>_+1</sub>\]. Thus since each edge in _H_<sub>1∗</sub>\[_I_<sub>_t<sub>j</sub>_+1</sub>\] has weight at least of the same order as those with a vertex in _I<sub>t<sub>j</sub></sub>_\\_I_<sub>_t<sub>j</sub>_+1</sub>, the claim holds.

It remains to consider \(v\in K_{l-1}\backslash K_l\). Then, in _H_<sub>1∗</sub>\[_I<sub>t<sub>j</sub></sub>_\], every edge contain ing _v_ has weight either \(\Theta\left(\frac{1}{p_\mathrm{gr}^3k_{l-1}\mathrm{log}(n)}\right)\) or \(\Theta\left(\frac{1}{p_\mathrm{gr}^3k_l\mathrm{log}(n)}\right)\), and those with weight \(\Theta\left(\frac{1}{p_\mathrm{gr}^3k_l\mathrm{log}(n)}\right)\) are all included in the numerator. The argument follows through in the same way as for the previous case. □

## 6.3. Using the random matching tool

In this section we shall describe the graphs for which we wish to use Theorem 6.2, and show that all the properties we wish to track in such a graph can be described as linear combinations of functions satisfying (6.1). We shall then see in the subsequent sections that each graph to which we wish to apply Theorem 6.2 satisfies the necessary hypotheses. For _H_ and then for each \(i\in[0,c_h]\) we wish to use Theorem 6.2 on a weighted subgraph \((H_i^o,w_i^o)\) of (_H<sub>i</sub>,w<sub>i</sub>_), in such a way as to obtain a matching \(M_i^o\), and show that \(H_i[V(H_i)\backslash V(M_i^o)]\) has ‘nice’ properties with regard to valid subsets of _V_(T), as well as degree-type and zero-sum configuration conditions. We are only required to keep track of zero-sum configurations until we reach (_H_<sub>1</sub>_,w_<sub>1</sub>), as these are only required for the weight shuffle.

### 6.3.1. Key properties as functions.

As seen in the list of properties given for (_H_<sub>1</sub>_,w_<sub>1</sub>) in Theorem 6.1, the properties we are keen to track are those relating to numbers of vertices in given subsets of _V_(T), degree-type conditions, and initially also zero-sum configurations.

In this section we describe the functions and how they will be useful, assuming that they satisfy (6.1). In the section that follows we show that, given that a graph (_H<sub>i</sub>,w<sub>i</sub>_) satisfies various properties, the functions relating to the properties we wish to track in (_H<sub>i</sub>,w<sub>i</sub>_) do indeed satisfy (6.1).

6.3.1.1. _Number of vertices and weighted functions on vertices remaining in an interval._ For a fixed (hyper)graph _G_, \(S\subseteq V(\mathcal{T})\), and for some weight function \(f:V(G)\rightarrow\mathbb{R}_{\ge 0}\), let \(p_S:V(G)\rightarrow\mathbb{R}_{\ge 0}\) be given by \(p_S(v):=f(v)\unknown_{v\in V(G[S])}\). Note that we suppress _f_ in our notation, but wherever used, _f_ will be clear from the context. Then for a matching _M_, \(p_S(M)=\sum_{v\in V(M)}p_S(v)\) yields the sum of the weights _f(v_) on vertices in _V(G_\[_S_\]) which are in _V(M_). In particular, for _f_=1 (i.e. _f(v_)=1 for every \(e\in V(G)\)), _p<sub>S</sub>(M_) counts the number of vertices in _V(G_\[_S_\]) which are in _M_. Hence, the weight _f_ on vertices remaining in _S_ after removing _V(M_) from _G_ is \(\sum_{v\in V(G[S])}f(v)-p_S(M)\) and in particular the number of vertices remaining in _S_ after removing _V(M_) from _G_ is |_V(G_\[_S_\])|-_p<sub>S</sub>(M_).

Given that _p<sub>S</sub>_ satisfies (6.1) we get from Theorem 6.2 that there exists a matching _M_ in _G_ such that

(6.11) \(p_S(M)=(1\pm\Delta^{-\epsilon})\sum_{v\in V(G)}p_S(v)d_{w,G}(v)=(1\pm\Delta^{-\epsilon})\sum_{v\in V(G[S])}f(v)d_{w,G}(v).\)

