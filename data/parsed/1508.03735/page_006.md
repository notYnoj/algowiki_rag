**Definition 2** (Coordination Complexity)**.** _A coordination protocol_ \((\sigma,\pi)\) _has_ coordination complexity \(\ell\) _if:_

\(max_{D\in\mathcal{X}^n}|\sigma(D)|=\ell.\)

The coordination complexity of obtaining a \(\rho\) approximation to a problem is the minimum value of the coordination complexity of all protocols \((\sigma,\pi)\) that obtain a \(\rho\) approximation to the problem.

We conclude by making several observations about coordination protocols. First, as we have defined them, they are _non-interactive_ - the coordinator first broadcasts a signal, and then the agents respond. This is without loss of generality, since the coordinator has full knowledge of the problem instance. Any interactive protocol could be reduced at no additional communication cost to a non-interactive protocol, simply by having the coordinator publish the transcript that would have arisen from the interactive protocol. This is in contrast to the setting of communication complexity, in which interactive protocols can be more powerful than non-interactive protocols (and makes it easier to prove lower bounds for coordination complexity).

Second, the coordination complexity of a problem is trivially upper bounded both by the description length of the problem instance (as is communication complexity), _and_ by the description length of the problem’s optimal solution (unlike in non-deterministic communication complexity, there is no need to pair the optimal solution with a certificate allowing individual agents to verify it). Hence, non-trivial bounds will be asymptotically smaller than both of these quantities.

### Bipartite Matching

The primary coordination problem we study in this paper is the _bipartite matching problem_. In this problem, there is a bipartite graph _G_=(_V,W,E_), in which every node in _V_ is associated with a player and every node in _W_ represents a good. Each player _i_’s private data is the set of edges incident to her node - i.e. \(D^{(i)}=\{j:(i,j)\in E\}\). We study two variants of this problem. In the _one- to-one_ matching problem, _W_ represents a set of distinct goods, and the goal is to coordinate a maximum cardinality matching \(E'\subseteq E\) such that for every \(i\in V\) , \(|\{j\in W:(i,j)\in E'\}|\le 1\) and for every \(j\in W\), \(|\{i\in V:(i,j)\in E'\}|\le 1\). In the _many-to-one_ matching problem, _W_ represents a set of _k_ commodities _j_, each with a supply _b<sub>j</sub>_. The goal is to coordinate a maximum cardinality many-to-one matching \(E'\subseteq E\) such that for every \(i\in V\) , \(|\{j\in W:(i,j)\in E'\}|\le 1\) and for every \(j\in W\) , \(|\{i\in V:(i,j)\in E'\}|\le b_j\). The social objective in this setting is the welfare or the cardinality of the matching, and we will use OPT(_G_) to denote the optimal welfare objective.

Note that the resulting solution might not be feasible since the players’ demands are not always satisfied. We need to make sure that we are not over-counting when measuring the welfare. In one-to-one matchings, if more than one players select a good, only the first player is matched to it. In many-to-one matchings, if more than _b<sub>j</sub>_ players select a good of type _j_, only the first _b<sub>j</sub>_ players are matched the good _j_.

### Notation

We use \(\|\cdot\|\) to denote the \(\ell_2\) norm, and more generally use \(\|\cdot\|_p\) to denote the \(\ell_p\) norm.

## 3 Lower Bounds for Bipartite Matchings

In this section, we present lower bounds on the coordination complexity of bipartite matching problems. As a building block, we prove a lower bound for the one-to-one matching problem on a bipartite graph with _n_ vertices on each side, showing an \(\Omega(n)\) lower bound - i.e. that no substantial improvement on the trivial solution is possible. We then extend this lower bound to the problem of many-to-one matchings, in which there are _n_ agents who must be matched to _k_ goods (each good can be matched to many agents, up to its supply). Here, we show an \(\Omega(k)\) lower bound. In the next section, we give a nearly matching upper bound, which substantially improves over the trivial solution.

