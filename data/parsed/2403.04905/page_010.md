<tbc>For _i_=2_,...,k_-1 we have \(h_i\cdot n^{\alpha_{i+1}}\le 2|E_i|\), and so

\(h_i=O(n^{1+\frac{\alpha_1+\alpha_i}{2}-\alpha_{i+1}}).\)

In the last step, we are left with the graph \(\mathcal{G}^\times(\mathcal{D}_k)\), for which we have that \(|E_k|\le\sqrt{\frac{4}{c}}n^{1+\frac{\alpha_1+\alpha_k}{2}}\) . We now apply the separator result on string graphs, which states that any string graph with _m_ edges has a separator of size \(O(\sqrt{m})\). Thus \(\mathcal{G}^\times(\mathcal{D}_k)\) has a separator of size \(O(n^\frac{2+\alpha_1+\alpha_k}{4})\) whose vertices we also place in S. As a result, the size of our clique-based separator is given by

\(|\mathcal{S}|=O\left(n^{1-\alpha_1}+\sum_{i=1}^{k-1}h_k+n^\frac{2+\alpha_1+\alpha_k}{4}\right)\)

which gives the following system of _k_ equations:

\(1-\alpha_1=\frac{3+\alpha_1}{2}-\alpha_2\) (4.1)

\(1-\alpha_1=1+\frac{\alpha_1+\alpha_i}{2}-\alpha_{i+1}\text{for}i=2,3,\dots,k-1\) (4._i_)

\(1-\alpha_1=\frac{2+\alpha_1+\alpha_k}{4}\) (4._k_)

This system can be rewritten as

\(3\alpha_1=2\alpha_2-1\) (4.1)

\(3\alpha_1=2\alpha_{i+1}-\alpha_i\text{for}i=2,3,\dots,k-1\) (4._i_)

\(5\alpha_1=2-\alpha_k\) (4._k_)

By multiplying the _i_-th equation above with 2<sup>_i_-1</sup> and summing up, we can see that the terms \(\alpha_2,\dots,\alpha_k\) cancel and we are left with the equation

\(\alpha_1\left(3\sum_{i=0}^{k-2}2^i+5\cdot 2^{k-1}\right)=2^k-1,\)

which solves to

\(\alpha_1=\frac{2^k-1}{2^{k+2}-3}.\)

Thus \(1-\alpha_1=\frac{3\cdot 2^k-2}{4\cdot 2^k-3}\) (which converges to \(\frac{3}{4}\) as \(k\rightarrow\infty\)). By choosing \(k=log_2(1/\varepsilon)\), we have

\(1-\alpha_1=\frac{3-2\varepsilon}{4-3\varepsilon},\)

which is smaller than \(\frac{3}{4}+\varepsilon\) for \(\varepsilon<1\). (We could pick _k_ even larger, say _k_=log_n_, but the resulting bounds will be only marginally better and look more ugly.) Therefore, for these choices of \(\alpha_1\) and _k_, our clique-based separator has a size of \(O(n^\frac{3}{4}+\varepsilon)\) as claimed. \(\blacktriangleleft\)

De Berg _et al._ \[11\] showed that if a class of graphs admits a clique-based separator consisting of _S(n_) cliques, and the separator can be constructed in polynomial time, then one can solve _q_-Coloring in 2<sup>_O(S(n_))</sup> time. Note that if we can compute the boundaries \(\partial D_i\) in

