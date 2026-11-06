<tbc>_the paths in_ G _from s to t. Then with proper tuning of the learning rate_ \(\eta\) _over the trials, EH guarantees the following regret bound:_

\(\mathcal{R}_{EH}\le\sqrt{2L^*Dlog\mathcal{N}}+Dlog\mathcal{N}.\) (1)

## 2.2 Component Hedge on Paths

The generic Component Hedge algorithm of Koolen et al. (2010) can be applied to the online shortest path problem. The components are the edges _E_ in the DAG. Each path is encoded as a bit vector \(\unknown\) of |_E_| components where the 1-bits indicate the presence of the edges in the path \(\unknown\). The convex hull of all paths is called the _unit-flow polytope_ and CH maintains a mixture vector \(f=[f_e]_{e\in E}\) in this polytope. The constraints of the polytope enforce an outflow of 1 from the source node _s_, and flow conservation at every other node but the sink node _t_. In each trial, each edge _e_ receives a loss of \(\ell_e\) and the weight of that edge _f<sub>e</sub>_ is updated multiplicatively by the factor \(exp(-\eta\ell_e)\). Then the weight vector is projected back to the unit-flow polytope via a relative entropy projection. This projection is achieved by iteratively projecting onto the flow constraint of a particular vertex and then repeatedly cycling through the vertices (Bregman, 1967). Finally, to sample with the same expectation as the mixture vector in the polytope, this vector is decomposed into paths using a greedy approach which removes one path at a time and zeros out at least one edge in the remaining mixture vector in each iteration. CH provides the regret guarantees below.

**Theorem 2 (Koolen et al. (2010))** _Given a DAG_ G=(_V,E_) _with designated source node_ \(s\in V\) _and sink node_ \(t\in V\) _, let D be an upper-bound on the number of edges of the paths in_ G _from s to t. Also denote the total loss of the best path by L_<sup>∗</sup>_. Then with proper tuning of the learning rate_ \(\eta\) _over the trials, CH guarantees the following regret bound:_

\(\mathcal{R}_{CH}\le\sqrt{4L^*Dlog|V|}+2Dlog|V|.\) (2)

**Remark.** In a moment, we will compare the regret bounds of EH (1) and CH (2). We will observe that compared to EH, CH guarantees better regret bounds as it does not have additional loss range factors in its bounds. In fact, the regret bounds of CH are typically optimal. Koolen et al. (2010) prove lower bounds which matches the guarantees of CH for various problems such as _k_-sets and permutations. The lower bounds are shown by embedding the combinatorial online learning into the original expert problem. To form the experts, a set of solutions is chosen which partitions all of the components. Moreover, all solutions in the set must have the same number of present components (i.e. same number of ones in the bit-vector representation). Given this proof technique, a lower bound on the regret for arbitrary graphs is difficult to obtain since choosing a set of paths with the aforementioned characteristics is non-trivial. Perhaps the regret of CH is tight within constant factors for all graphs, but this question is still open.

## 2.3 Component Hedge vs Expanded Hedge

To have a concrete comparison between CH and EH on paths, consider the following path learning setting. Let G=(_V,E_) be a complete DAG with _V_={_v_<sub>1</sub>_,...,v<sub>n</sub>_} where for all \(1\le i<j\le n\), _v<sub>i</sub>_ is connected to _v<sub>j</sub>_. Also let _s=v_<sub>1</sub> and _t=v<sub>n</sub>_ be the designated source<tbc>

