<tbc>by a path of the DAG. We have |_M_|=|_E_|=_O(nC_) edges which are the components of our new representation. The gains of the edges going from the node (_i,c_) to the nodes (_i_-1_,c_) and (_i_-1_,c-h<sub>i</sub>_) are 0 and _p<sub>i</sub>_, respectively. Note that the gain associated with each edge is upper-bounded by 1. Most crucially, the sum of the profits of the picked items in the packing is linear in the gains of the edges and the unit-flow polytope has _O(nC_) facets.

## Regret Bounds.

We turn the problem into an equivalent shortest-path problem by defining a loss for each edge \(e\in E\) as \(\ell_e=1-g_e\) in which _g<sub>e</sub>_ is the gain of _e_. Call this new DAG \(\bar{\mathcal{G}}\). Let \(L_\bar{\mathcal{G}}(\pi)\) be the loss of path \(\pi\) in \(\bar{\mathcal{G}}\) and \(G_\mathcal{G}(\pi)\) be the gain of path \(\pi\) in G. Since all paths contain exactly _D=n_ edges, the loss and gain are related as follows: \(L_\bar{\mathcal{G}}(\pi)=n-G_\mathcal{G}(\pi)\). According to our initial assumption logN=O(_n_). Thus using Theorem 10 we obtain:

\(G^*-\mathbb{E}[G_\mathrm{EH}]=(nT-L^*)-(nT-\mathbb{E}[L_\mathrm{EH}])\)<br>
\(=\mathbb{E}[L_\mathrm{EH}]-L^*=\mathcal{O}(n\sqrt{L^*}).\)

Notice that the number of multiedges/edges is |_M_|=|_E_|=_O(nC_) and each path consists of _D=n_ edges. Therefore using Theorem 14 we obtain:

\(G^*-\mathbb{E}[G_\mathrm{CH}]=(nT-L^*)-(nT-\mathbb{E}[L_\mathrm{CH}])\)<br>
\(=\mathbb{E}[L_\mathrm{CH}]-L^*=\mathcal{O}(n^\frac{1}{2}(\mathrm{log}nC)^\frac{1}{2}\sqrt{L^*}).\)

## 5.4 _k_-Sets

Consider the online learning of the _k-sets_ (Warmuth and Kuzmin, 2008): We want to learn subsets of size _k_ of the set {1_..n_}. In each trial, the algorithm predicts with a _k_-set. Then, the adversary reveals the loss of each element \(\ell_i\) for \(i\in\{1..n\}\). The loss is defined as the sum of the losses of the elements in the _k_-set predicted by the algorithm in that trial. The goal is to predict with a sequence of _k_-sets minimizing regret which is the difference between the total loss of the algorithm and the total loss of the single best _k_-set chosen in hindsight.

## The Dynamic Programming Representations.

Finding the optimal _k_-set can be solved via dynamic programming. Each subproblem is denoted by a pair (_i,j_) for \(0\le j\le k\) and \(j\le i\le j+n-k\), indicating the _j_-set problem over the set {1_,...,i_}. The base subproblem is (0,0) and the complete subproblem is (_n,k_). The dynamic programming for the _k_-set problem uses the following min-sum recurrence:

\(\mathrm{OPT}(i,j)=\left\{\begin{array}{ c c }
0 & i=j=0 \\
\mathrm{OPT}(i-1,0) & j=0 \\
\mathrm{OPT}(i-1,i-1)+\ell_i & j=i \\
\mathrm{min}\{\mathrm{OPT}(i-1,j),\mathrm{OPT}(i-1,j-1)+\ell_i\} & \text{otherwise}.
\end{array}\right.\)

This recurrence always recurses on 1 subproblem. Thus the multipaths are regular paths and the problem is essentially the online shortest-path problem from a source to a sink. The associated DAG has the subproblems/vertices \(V=\{(i,j)|0\le j\le k,j\le i\le j+n-k\}\), source _s_=(_n,k_) and sink T={(0,0)}. Also at node (_i,j_), the set \(M_{(i,j)}^{(\mathrm{out})}\) consists of two edges going from the node (_i,j_) to the nodes (_i_-1_,j_) and (_i_-1_,j_-1). Figure 7 illustrates an example of the DAG and a sample path associated with a _k_-set.

