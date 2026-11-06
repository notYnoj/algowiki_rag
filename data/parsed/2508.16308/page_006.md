### 4.1 Proving Lower Bounds by Constructing Indistinguishable Graphs

The lower bound proofs based on indistinguishability graphs rely on the fact, that given two graphs _G_<sub>1</sub> and _G_<sub>2</sub>, and assignment of ids of their respective vertices such that there exist two vertices _v_<sub>1</sub> in _G_<sub>1</sub> and _v_<sub>2</sub> in _G_<sub>2</sub> sharing the same id and _t_-radius view implies that any _t_-round LOCAL algorithm executing on the vertices _v_<sub>1</sub> and _v_<sub>2</sub> cannot _distinguish_ between _G_<sub>1</sub> and _G_<sub>2</sub> and will produce the same output for _v_<sub>1</sub> and _v_<sub>2</sub>. This follows from the radius view based definition of the LOCAL algorithm. The technique of using indistinguishability to prove LOCAL lower bounds have been used extensively in the literature (for example, refer to \[20\], section 7.5 of \[25\], \[19\]).

For designing lower bounds for our problem, we create two _n_-vertex graphs \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\)such that there exist two pairs of vertices \(u_1,v_1\in G_1^{\{\ell,k\}}\)and \(u_2,v_2\in G_2^{\{\ell,k\}}\)such that the following properties hold.

1. There exists an assignment of ids for the vertices of \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\)such that _u_<sub>1</sub> and _u_<sub>2</sub> receive the same id and have the same _t_-radius view for every _t=o(n_). The same holds for _v_<sub>1</sub> and _v_<sub>2</sub> as well.<tbc>

2. Any _k_-partial _k_-colorings \(\chi_1\) and \(\chi_2\) of \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\), respectively, satisfy that \(\chi_1(u_1)=\chi_1(v_1)\) while \(\chi_2(u_2)\neq\chi_2(v_2)\).

For _t=o(n_), any _t_-round algorithm A executing on _u_<sub>1</sub>, _u_<sub>2</sub>, _v_<sub>1</sub> and _v_<sub>2</sub> cannot distinguish \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\)and therefore, assigns the same color to _u_<sub>1</sub>, _u_<sub>2</sub> and _v_<sub>1</sub>, _v_<sub>2</sub> thus incorrectly coloring at least one of the two graphs.

## 5 Hard Instances of Partial Coloring

In this section, we identify the structural properties that make a graph instance hard for _k_-partial _k_-coloring. The goal is to understand which parts of a graph force any partial coloring algorithm to behave like a proper coloring algorithm.

Given a graph _G_ and integers _k_ and _c_, any algorithm for computing a _k_-partial _c_-coloring must implicitly address two subtasks:

1. Identifying a subgraph \(G'\subseteq G\) which must be properly colored to satisfy the _k_-partial coloring condition -- this identification is solely dependent on _k_ and not on the number of colors _c_.<tbc>

2. Assigning colors to \(G'\) in a way that yields a proper coloring using _c_ colors.

The complexity of _k_-partial coloring is therefore inherently tied to the structure of this critical subgraph \(G'\). We formally characterize such subgraphs in the lemma below, which highlights the role of a specific graph parameter in determining where proper coloring becomes unavoidable.

To this end, we introduce the parameter \(\Delta_E\) for a graph _G_=(_V,E_) as follows:

\(\Delta_E:=max_{e=\{u,v\}\in E}min\{deg_G(u),deg_G(v)\}.\)

**Lemma 1.** _A_ \(\Delta_E\)_-partial coloring of G is a proper coloring of G._

