### 2.1 Linear Programming Relaxation for the Minimum Multicut Problem

We begin by describing an integer programming (IP) formulation for the minimum multicut problem. For each edge \(e\in E(G)\), we introduce an integer variable \(x(e)\in\{0,1\}\), which indicates whether the edge is selected in the multicut. For a given path _P_, we define \(x(P)=\sum_{e\in E(P)}x(e)\). A feasible multicut must include at least one edge from each source-sink path, so we impose the constraint \(x(P)\ge 1\) for all \(P\in\mathcal{P}\), ensuring that each path is _cut_ by at least one edge. We relax the integrality constraints to obtain the linear programming (LP) relaxation of the multicut problem, which is formulated as follows:

\(min\sum_{e\in E(G)}c(e)x(e)\text{s.t.}x(P)\ge 1\forall P\in\mathcal{P},x(e)\ge 0\forall e\in E(G).\text{(1)}\)

Even though there are an exponential number of constraints, it is well known that the optimal solution to this LP can be computed in polynomial time \[GVY96\]. We denote the optimal solutions of the integer and linear programs as OPT_<sub>IP</sub>_ and OPT_<sub>LP</sub>_, respectively. We refer to OPT_<sub>LP</sub>_ as the minimum fractional multicut. We know that the value of the maximum multiflow is equal to the minimum fractional multicut. Furthermore, a bound on the integrality gap of the LP relaxation for the multicut problem provides the same bound for the multiflow-multicut gap. Therefore, from this point onward, we will focus solely on the integrality gap of the multicut LP. We now formally define the integrality gap of the minimum multicut problem on a family of graphs.

**Definition 1.** _Let_ G _be a family of graphs, and let_ M(G) _denote the family of all instances of the minimum multicut problem on_ G_, obtained by assigning arbitrary costs to the edges and selecting a set of source-sink pairs. The integrality gap_ \(\alpha_{\mathcal{M}(\mathcal{G})}\) _of the minimum multicut problem on_ M(G) _is defined as_

\(\alpha_{\mathcal{M}(\mathcal{G})}:=max_{M\in\mathcal{M}(\mathcal{G})}\frac{OPT_{IP}(M)}{OPT_{LP}(M)},\)

_where OPT<sub>IP</sub>(M_) _is the optimal value of the integer program and OPT<sub>LP</sub>(M_) _is the optimal value of its linear relaxation_ (1).

As mentioned in the introduction, \(\alpha_{\mathcal{M}(\text{tree})}=2\) \[GVY97\], where tree denotes the family of all trees, and \(\alpha_{\mathcal{M}(\text{planar})}=\mathcal{O}(1)\) \[KPR93\], where planar denotes the family of all planar graphs.

## 3 Our Results and Techniques

We provide a partial answer to the questions raised above by showing that the integrality gap of the minimum multicut problem for the family of cactus graphs (and therefore for series-parallel graphs and planar graphs) is strictly greater than 2. In particular, we show that the multiflow-multicut gap is at least \(\frac{16}{7}\) for the class of _cactus_ graphs.

We first develop a novel technique to argue that the integrality gap of the multicut LP is at least \(\frac{20}{9}\) , and later refine it to obtain an improved lower bound of \(\frac{16}{7}\) . We observe that the integrality gap of the multicut LP for a class of graphs is \(\alpha\) if and only if any fractional solution to the natural linear programming relaxation of the minimum multicut problem can be approximately written as a convex combination (or equivalently a probability distribution) of feasible multiccuts. Furthermore, a feasible multicut can be interpreted in terms of small diameter decompositions (i.e., a set of edges whose removal results in connected components of small diameter) with an appropriate distance function.

