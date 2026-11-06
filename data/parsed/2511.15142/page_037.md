and hence the relative order of edge weights \(w_{\{u,v\}}^*\) is simply the reverse of the order of the cuts \(\partial\{u,v\}\) sorted by their cut values. Since these comparisons can be performed using only cut queries, we can recover the rank order of all edge weights.

Because the weights are bounded by _B_, there are at most \(\ell:=n^2B+1\) distinct cut values, corresponding to \(\ell\) ordered _buckets_ of edges. We wish to classify these buckets into _O_(log_B_) weight ranges:

\(0,[2^0,2^1),[2^1,2^2),\dots,[2^{\lfloor log_2B\rfloor},2^{\lfloor log_2B\rfloor+1}).\)

A naive assignment of each bucket to one of these _O_(log_B_) classes would yield \((O(logB))^\ell\) possibilities. However, since the buckets are ordered, we can choose the _O_(log_B_) boundary points separating consecutive classes along this sequence. Thus, the number of possible partitions is \(O(\ell^{O(logB)})\), and one such partition corresponds to a 2-approximation of the true edge weights.

Using these approximate weights, we enumerate all 2-approximate cuts. By Karger’s result, there are only _n_<sup>_O_(1)</sup> such cuts, and these can be enumerated in \(\widetilde{O}(n^2)\) time (see \[HHS24\]). Since our guessed weights form a 2-approximation, the true minimum cut (which is a 2-approximate cut under the guessed weights) appears among them. Comparing all enumerated cuts across all weight guesses and returning the smallest yields a total running time and number of cut comparisons of _O_((_nB_)<sup>_O_(log_B_)</sup>).

The guessing step can be extended to the more general case where there are _r_ distinct weighted degrees. In this case, we first classify the vertices into _V_<sub>1</sub>_,...,V<sub>r</sub>_ according to their degrees (this can be done by comparing their degree cuts). Each edge then lies between some pair (_V<sub>i</sub>,V<sub>j</sub>_), and we accordingly classify all edges into \(r+\genfrac(){pt}{2}{r}{2}\) classes _E_<sub>{_i,j_}</sub>.

Observe that for two edges \(\{u_1,v_1\},\{u_2,v_2\}\in E_{\{i,j\}}\) within the same class, their weights can be compared by comparing the cuts \(\partial\{u_1,v_1\}\) and \(\partial\{u_2,v_2\}\) using Equation (33). Hence, we apply the same guessing procedure as before independently within each class, resulting in a total of \(O(\ell^{O(r^2logB)})\) guesses. We can then proceed exactly as in the uniform-degree case. Consequently, the overall running time and number of cut comparisons are _O_((_nB_)<sup>_O(r_<sup>2</sup>log_B_)</sup>).

## D.3.2 Stronger Oracles

An alternative to imposing structural assumptions is to consider stronger oracle models. We highlight two natural extensions:

1. **Comparing marginals:** Instead of comparing the objective values of feasible sets, i.e., _w(S_) and _w(T_) for \(S,T\in\mathcal{F}\), we allow comparisons between _marginal differences_ such as \(w(S)-w(S')\) and \(w(T)-w(T')\) for \(S,S',T,T'\in\mathcal{F}\).<tbc>

2. **Comparing arbitrary sets:** We relax the restriction that comparisons must involve only feasible sets, and instead allow comparing _w(S_) and _w(T_) for any \(S,T\subseteq U\), while the optimization goal remains finding \(argmin_{S\in\mathcal{F}}w(S)\).

In both of these stronger models, the minimum cut can be found efficiently, even in the weighted setting with arbitrary non-negative weights. The key observation is that the Nagamochi-Ibaraki algorithm \[NI92\] for minimum cuts only requires comparisons of _differences_ of cut values. More specifically, at each step it only needs to find<tbc>

\(argmin_{u\in V\backslash S}\big(w(\partial(S+u))-w(\partial u)\big),\)

