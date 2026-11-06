<tbc>topologies remain unpaired with real-world RNA structures, highlighting potential areas for future research and discovery. As the number of vertices increases, the number of possible topologies grows exponentially, with 92,788 topologies for 9 vertices.

To mitigate the effect of unbalanced data, we create datasets based on the number of vertices. Specifically, we gather all possible graph topologies with 4 and 5 vertices into a dataset named "Dataset V4&5." Similarly, we create "Dataset V6" for 6-vertices graphs, "Dataset V7" for 7-vertices graphs, "Dataset V8" for 8-vertices graphs, and "Dataset V9" for 9-vertices graphs. We also compile all topologies into a comprehensive dataset named "Dataset All." We exclude vertices 2 and 3 from further analysis, as they correspond to known RNA structures. These 6 datasets with 4 and more vertices are used in the clustering analysis in Section 3.1.

## 2.2 Topological Feature Engineering

### 2.2.1 Generalization of persistent spectral graph-based features on dual graphs

We assume that each entry _a<sub>ij</sub>_ of adjacency matrix _A_=(_a<sub>ij</sub>_) of dual graph _G_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>) represents the distance between vertices _v<sub>i</sub>_ and _v<sub>j</sub>_ (when \(i\neq j\)), and _a<sub>ij</sub>_ is an integer in [0,1,2,3]. In this work, we choose the distance-based filtration between two vertices of a dual graph and construct a series of simplicial complexes to form persistent Laplacians. Specifically, given a set of vertices _V_<sup>∗</sup>={_v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>n</sub>_} of a dual graph _G_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>), we consider a nested family of simplicial complexes that are created for a positive real number _d_ (In this work, we set distance filtration parameter _d_=1,2,3). Denoting the simplicial complex generated for _d_ by _K<sub>d</sub>_, the traditional _q_th-order Laplacian is the special case of _q_th-order 0-persistent Laplacian at _K<sub>d</sub>_:

\(L_q^{d,0}=B_{q+1}^{d,0}(B_{q+1}^{d,0})^T+(B_q^d)^TB_q^d.\) (2)

The spectrum of \(L_q^{d,0}\) is simply associated with a snapshot of the filtration,

\(\text{Spec}(L_q^{d,0})=\{\lambda_{1,q}^{d,0},\lambda_{2,q}^{d,0},\cdots,\lambda_{N_q^d,q}^{d,0}\}.\) (3)

With this association, we have the result that the _q_-th 0-persistent Betti number \(\beta_q^{d,0}=\beta_q^d\) is equal to the number of zeros in \(\text{Spec}(L_q^{d,0})\). For simplicity, we call the _q_-th 0-persistent Betti number as Betti _q_ number. Typically, the Betti _q_ number refers to the number of _q_-dimensional holes on a topological surface. For example, Betti 0, 1, and 2 represent the number of connected components, 1-dimensional cycles (i.e., loops), and 2-dimensional cycles (i.e., cavities) of a given system, respectively. Figure 2 shows the dual graph 4.23 with its corresponding simplicial complexes _K_<sub>1</sub>, _K_<sub>2</sub>, and _K_<sub>3</sub> when the distance filtration parameter _d_=1,2, and 3, respectively. The persistent Laplacians \(L_0^{d,0}\) at different distance filtration _d_ of dual graph 4.23 are also shown.

We chose 18 statistical values of the \(\text{Spec}(L_q^{d,0})\) features to describe a dual graph as follows:

• 4 features from \(\text{Spec}(L_0^{d,0})\) when _d_=1: summation, non-zero smallest, variance, and the number of zeros;<tbc>

• 7 features from \(\text{Spec}(L_0^{d,0})\) when _d_=2: summation, non-zero smallest, maximum, average, standard deviation, variance, and the number of zeros;<tbc>

• 7 features from\(\text{Spec}(L_0^{d,0})\) when _d_=3: summation, non-zero smallest, maximum, average, standard deviation, variance, and the number of zeros.

However, the distance filtration does not consider the self-loop information in the adjacency matrix _A_=(_a<sub>ij</sub>_) when _i=j_. Therefore, we include the average degree (Avg(Deg)) as an additional feature to describe a dual graph, which is defined as:

\(\text{Avg(Deg)}=\frac{\sum_ia_{ii}}{2n},\) (4)

