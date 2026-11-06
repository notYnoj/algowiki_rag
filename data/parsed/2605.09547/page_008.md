## 3.1 High-Level Idea: Storing Flows in \(\widetilde{O}(n^{1.5})\) Space

Here we outline how to store a flow \(x\in\mathbb{R}^E\) in low-space, such that when given any edge \(e\in E\), its cost _c<sub>e</sub>_, and capacity _u<sub>e</sub>_, then we can query/compute _x<sub>e</sub>_.

Consider the linear programming definition of minimum cost flow. For an \(E\times V\) incidence matrix \(\mathbf{A}\in\{-1,0,1\}^{E\times V}\), edge-cost vector \(c\in\mathbb{R}^E\), demand vector \(b\in\mathbb{R}^V\), and edge capacities \(u\in\mathbb{R}^E\), the following linear program models minimum-cost flows.

\(min_{x\in\mathbb{R}^E}c^\top x\text{subject to}\mathbf{A}^\top x=b0\le x\le u\)

A common idea for computing minimum cost flows is to start with some initial flow, then repeatedly augment the flow via negative cost cycles or circulations. When solving minimum cost flows via interior point methods such as \[Mad13, LS14, Mad16, AMV20\], these circulations are so called "electric circulations." That is, for some feasible flow \(x\in\mathbb{R}^E\), we augment it by a circulation \(\delta_x\in\mathbb{R}^E\) where

\(x\leftarrow x+\delta_x\)<br>
\(\delta_x=\big(\mathbf{I}-\mathbf{R}_x^{-1}\mathbf{A}(\mathbf{A}^\top\mathbf{R}_x^{-1}\mathbf{A})^\dagger\mathbf{A}^\top\big)g_x.\)

Here \(g_x\in\mathbb{R}^E\) is some flow and **R**_<sub>x</sub>_ is an \(E\times E\) diagonal matrix with (**R**_<sub>x</sub>)<sub>e,e</sub>_ being resistance of edge _e_. (Both _g<sub>x</sub>_ and **R**_<sub>x</sub>_ will be defined later to depend on _x_). Flow \(\delta_x\) is a circulation, because it satisfies 0-demand \(\mathbf{A}^\top\delta_x=0\). It is an electric circulation because

\(f=-\mathbf{R}_x^{-1}\mathbf{A}(\mathbf{A}^\top\mathbf{R}_x^{-1}\mathbf{A})^\dagger\mathbf{A}^\top g_x\) (1)

is an electric flow for demand \(d=-\mathbf{A}^\top g_x\in\mathbb{R}^V\) and resistances **R**_<sub>x</sub>_ (i.e., among all demand _d_ flows, _f_ minimizes the energy \(\sum_{e\in E}(\mathbf{R}_x)_{e,e}f_e^2\)).

The idea of our low space representation is that we only store some initial flow \(x^0\in\mathbb{R}_{\ge 0}^E\), and then store all the augmenting circulations \(\delta_x^1,\delta_x^2,\dots\). We will argue that each \(\delta_x^t\in\mathbb{R}^E\) can be stored in only \(\widetilde{O}(n)\) space. It was proven in \[LS14\] that it takes \(\widetilde{O}(\sqrt{n}log(W/\epsilon))\) iterations/augmentations to find a min-cost flow whose cost is at most an additive \(\epsilon\) off from optimal. Thus \(\widetilde{O}(n^{1.5}log(W/\epsilon))\) total space suffices<sup>4</sup>. We can then query the amount of flow on any edge \(e\in E\) by computing \(x_e^0+\sum_{t=1}^{\widetilde{O}(\sqrt{n})}(\delta_x^t)_e\).

Crucial for our low space representation is that the (_t_+1)-th augmenting circulation \(\delta_x^{t+1}\) depends on the _t_-th flow \(x^t=x^0+\sum_{k=1}^t\delta_x^k\). The fact that we can store circulation \(\delta_x^{t+1}\) in only \(\widetilde{O}(n)\) space relies heavily on the following property: when querying/computing \((\delta_x^{t+1})_e\) for some edge _e_, we already know the flow \(x_e^t\) on that edge. This assumption is given by induction: if we know \(x_e^{t-1}\), then we can compute \((\delta_x^t)_e\), thus we know \(x_e^t=x_e^{t-1}+(\delta_x^t)_e\), and so forth. This way we iteratively reconstruct \(x_e^t\) and \((\delta_x^t)_e\) from _t_=1,2,3_,..._ all the way to the final/optimal flow on that edge _e_.

To outline these low-space representations, let us start with the initial flow _x_<sup>0</sup>.

**Storing the initial flow** _x_<sup>0</sup> **(Section 6.1):** We would like to start with an initial flow _x_<sub>0</sub> that is feasible and can be stored in low space. Fortunately, standard constructions for the initial flow in non-streaming settings \[BLL<sup>+</sup>21, LS14, GLP21, BGJ<sup>+</sup>22\] can also be stored in low space and thus directly apply. Consider the following construction.

We pick \(x_e^0=u_e/2\), i.e., each edge carries half its capacity as flow. This flow _x_<sup>0</sup> does not yet satisfy the demand vector \(b\in\mathbb{R}^V\), but we can fix this as follows: add an extra star to the graph (i.e., one vertex that is connected to every other vertex) and route the missing/additional flow along the star edges. The star edges are assigned very large \(poly(n\|c\|_\infty)\) cost so the optimal min-cost flow will not use them, i.e., addition of these edges to the graph does not change optimal solution.

We can store this additional star and the amount of flow \(x_e^0\) on the star-edges in \(\widetilde{O}(n)\) space since there are only _n_ additional edges. For all edges _e_ of the original graph, we can return \(x_e^0=u_e/2\) since the capacity _u<sub>e</sub>_ of the edge is given during the query.

<sup>4</sup>For the rest of the overview, we will hide the \(log(W/\epsilon)\) term in \(\widetilde{O}\)-notation.

