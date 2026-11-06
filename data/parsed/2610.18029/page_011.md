the form:

\(L(\mathbf{x})=\sum_{i\in V}w_ix_i-\lambda\sum_{(i,j)\in E}x_ix_j,\)

where the first sum is over the nodes of the complement graph and the second sum over the edges.

For some putative solution subgraph, each _x<sub>i</sub>_ takes value 1 if vertex i is in the subgraph, and 0 otherwise, and _w<sub>i</sub>_ is the weight of vertex i. Therefore, we only sum over the weights we include in the subgraph. In the second term, _x<sub>i</sub>x<sub>j</sub>_ takes the value 1 if and only if both _x<sub>i</sub>_ and _x<sub>j</sub>_ is 1, representing the case where the vertices on the ends of each edge are both in the subset. Then, given a sufficiently large Lagrange multiplier, any subgraph that maximises _L_(**x**) will require none of the edges in the graph to be included, i.e. a MWIS, as they get heavily penalised. Notably, all terms are no more than quadratic, so this cost function is naturally in the form that the QUBO method aims to solve.

The QAOA approach requires a slight modification over the general QUBO method, as we must have our binary variable take values over {-1,+1}, rather than {0,1}. Therefore, we require a further step to convert the cost function to a Hamiltonian. The general form of a cost Hamiltonian is

\(H_C=\sum_{ij}Q_{ij}Z_iZ_j+\sum_ib_iZ_i,\)

where the sums are over the qubits and the _Z<sub>i</sub>_ is a Pauli-Z gate on the _i_-th qubit.

In order to rewrite our cost function in this form, first we transform the binary variables \(x_i\in\{0,1\}\) to \(z_i\in\{-1,1\}\) via<tbc>

\(x_i=\frac{1-z_i}{2}\text{or}z_i=1-2x_i.\)

<tbc>Then our cost function becomes:

\(L(\mathbf{x})=\sum_{i\in V}w_i\frac{1-z_i}{2}-\lambda\sum_{(i,j)\in E}\frac{1-z_i}{2}\frac{1-z_j}{2}\)<br>
\(=\sum_{i\in V}w_i\frac{1-z_i}{2}-\lambda\sum_{(i,j)\in E}\frac{(1-z_i)(1-z_j)}{4}\)<br>
\(=\sum_{i\in V}\frac{w_i}{2}-\sum_{(i,j)\in E}\frac{\lambda}{4}-\sum_{i\in V}\frac{w_iz_i}{2}+\frac{\lambda}{4}\sum_{(i,j)\in E}(z_i+z_j)-\frac{\lambda}{4}\sum_{(i,j)\in E}z_iz_j.\)

Now, we can note that for the \(\sum_{(i,j)\in E}(z_i+z_j)\) term, the number of times each _z<sub>i</sub>_ is counted is exactly the degree of the vertex, so we can simplify this term to \(\sum_{i\in V}deg(i)\). Furthermore, there are several things that do not affect the argument that maximises the function: constant terms and multiplicative factors. Therefore, we can remove the first two terms and multiply the whole expression by 4. This gives an equivalent maximization objective, up to additive and positive multiplicative constants

\(L(\mathbf{x})=\sum_{i\in V}\left(\lambda\cdot deg(i)-2w_i\right)z_i-\lambda\sum_{(i,j)\in E}z_iz_j.\)

