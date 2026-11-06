## 6 Initial Flow and Complete Algorithm

We now show how to initialize our interior point method and start from a feasible point near the central path. Then, we show that after running our algorithm we indeed have found an optimal feasible solution and can query the flow along any edge of it to \(\epsilon\) accuracy. This will conclude the proofs of Theorems 1.1 and 1.2.

### 6.1 Initial Point & Auxiliary Graph

We have shown the following:

**Theorem 4.1.** _Given_ \(\mu^{(\mathrm{target})}\in\mathbb{R}_{>0}\) _and_ \(\epsilon\)_-centered (see Definition 4.4)_ \((x^{(\mathrm{init})},s^{(\mathrm{init})},\mu^{(\mathrm{init})})\) _in implicit representation (i.e., we can query any entry in time T_<sub>0</sub>_), then in_ \(\widetilde{O}(T_0mn\mathrm{log}^2(\mu^{(\mathrm{init})}/\mu^{(\mathrm{target})}))\) _time,_ \(\widetilde{O}(\sqrt{n}\mathrm{log}(\mu^{(\mathrm{init})}/\mu^{(\mathrm{target})}))\) _passes, and_ \(\widetilde{O}(n^{1.5}\mathrm{log}(\mu^{(\mathrm{init})}/\mu^{(\mathrm{target})}))\) _space, we construct_ \(\epsilon\)_-centered_ \((x,s,\mu^{(\mathrm{target})})\) _in implicit representation with query time_ \(O(T_0+\sqrt{n}\mathrm{log}(\mu^{(\mathrm{init})}/\mu^{(\mathrm{target})}))\)_. The algorithm is randomized and the output is correct w.h.p._

In this section we discuss how to create an initial \((x^{(\mathrm{init})},s^{(\mathrm{init})},\mu^{(\mathrm{init})})\) that is feasible and on the central path and calculate _T_<sub>0</sub>. The construction of \[BLL<sup>+</sup>21\] satisfies this and can be implemented in low space, so we can exactly use their construction.

\(\includegraphics{}\text{\textbf{Construction from \[BLL}}^\pm\text{\textbf{21\] We assume that}}u_e\text{and}c_e\text{are integral, and let}W\text{be the maximum absolute value of}u_e\text{and}c_e\text{over all edges}e\text{.
Given a graph}G=(V,E)\text{, let}\widetilde{G}=(V\cup\{z\},\widetilde{E})\text{where}\widetilde{E}=\{(v,z),(z,v)|v\in V\}\text{. That is, we add a bi-directional star rooted at}z\text{into}G\text{. We let}\left[\begin{array}{ c }
x^{(\mathrm{init})} \\
\widetilde{x}^{(\mathrm{init})}
\end{array}\right]\text{denote an initial flow in}\widetilde{G}\text{where}x^{(\mathrm{init})}\text{and}\widetilde{x}^{(\mathrm{init})}\text{specify the flow values on}E\text{and}\widetilde{E}\text{, respectively. For each}e\in E\text{, we set}x_e^{(\mathrm{init})}:=u_e/2\text{. For all star-edges}e\in\widetilde{E}\text{, we first set}\widetilde{x}_e^{(\mathrm{init})}=1\text{(just to prevent them from having flow value too close to zero). Then, we additionally route the excess at each vertex induced by}x^{(\mathrm{init})}\text{using the star-edges from}\widetilde{E}\text{. More formally, for each}v\in V\text{, if the flow excess at}v\text{is}[\mathbf{A}^\top x^{(\mathrm{init})}-F_{es,t}]_v>0\text{, then we set}\widetilde{x}_{(v,z)}^{(\mathrm{init})}:=1+[\mathbf{A}^\top x^{(\mathrm{init})}-F_{es,t}]_v\text{and}\widetilde{x}_{(z,v)}^{(\mathrm{init})}=1\text{. Otherwise, the flow deficit at}v\text{is}[F_{es,t}-\mathbf{A}^\top x^{(\mathrm{init})}]_v\ge 0\text{and we set}\widetilde{x}_{(z,v)}^{(\mathrm{init})}=1+[F_{es,t}-\mathbf{A}^\top x^{(\mathrm{init})}]_v\text{and}\widetilde{x}_{(v,z)}^{(\mathrm{init})}=1\text{. The capacity}u_e\text{and cost}c_e\text{of each original edge}e\in E\text{stay the same. For each star-edge}e\in\widetilde{E}\text{, we set the capacity}\widetilde{u}_e=2\widetilde{x}_e^{(\mathrm{init})}\text{and}\widetilde{c}_e:=50m\|u\|_\infty\|c\|_\infty\text{. Consider the modified linear program for minimum cost flow on}\widetilde{G}\text{:}\mathrm{min}_{\widetilde{\mathbf{A}}^\top\left[\begin{array}{ c }
x \\
\widetilde{x}
\end{array}\right]=F_{es,t}0\le x_e\le u_e\forall e\in E0\le\widetilde{x}_e\le\widetilde{u}_e\forall e\in\widetilde{E}}c^\top x+\widetilde{c}^\top\widetilde{x},\text{where}\widetilde{\mathbf{A}}\text{is an incidence matrix of}\widetilde{G}\text{.
For a small technical reason, we need to further modify the linear program since an incidence matrix is degenerate and our path following algorithm only works on a full rank matrix. Remove a single column that corresponds to the vertex}z\text{.}\)

We first show that this construction works in our low-space setting as well, and analyze the query time of each edge.

**Lemma 6.1.** _The initial flow in the construction from \[BLL_<sup>+</sup>_21\] can be stored in O(n_) _space. Given the capacity along an edge, the flow of each edge can be queried in O_(1) _time._

_Proof._ To keep track of the flow on edges incident to the star vertex we only need to calculate and store all the other vertex demands once, which takes _O(n_) space and _O_(1) time per query.

