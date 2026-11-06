<tbc>both, gives a total coefficient 4 for this monomial. The automorphism condition \(\phi(2)<\phi(3)\) eliminates the second homomorphism, leaving a total coefficient 2 for this monomial. However, the coefficient is still even, and hence this term vanishes identically over _R_.

### Homomorphisms where P<sub>4</sub> embeds as an induced subgraph.

Here the image _P_<sub>4</sub> is an _induced_ copy in B; with no variable repeated and no extra edge between the vertices in the host graph, resulting in a multilinear monomial with co-efficient 2 (the path and its reversal).

For example, take 1-2-3-4 \(\mapsto\) _c-b-e-d_. The automorphism group of _P_<sub>4</sub> consists of the identity and the reversal 1-2-3-4 \(\leftrightarrow\) 4-3-2-1; the reversal sends this mapping to 1-2-3-4 \(\mapsto\) _d-e-b-c_, which is the same walk traversed backward and hence produces the identical monomial _y<sub>c</sub>y<sub>b</sub>y<sub>e</sub>y<sub>d</sub>_. So when we impose the conditions \((\phi(2)<\phi(3))\) to avoid automorphisms, the coefficient becomes odd for all induced copies.

Hence only the multilinear terms of the homomorphism polynomial contributing to the _induced_ subgraph survives, as the terms in the first 3 cases vanish. The terms in the third case vanishes due to even coefficients, since the imposed condition doesn’t stop it from counting the extra _P_<sub>4</sub> due to the extra edge.

## B 5-Vertex Graphs

Here each of the graph is represented as a 10 bit binary string where each bit represent which of the edges[(0,1), (0,2), (0,3), (0,4), (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)] exists in the graph.

**Good Tree Decomposition**: A tree decomposition is Good for a 5-vertex graph, if the tree width is 2 and the vertices can be spanned by a vertex and an edge. **Conditions**: The conditions helps us to reduce the automorphism to odd automorphisms which helps us in cancelling the even terms present in the equation.

For Example for G02, 0011001010, This graph has two automorphisms as we saw in A, corresponding to swapping vertices 1 and 2. To eliminate this symmetry, we impose the condition 1_\<_2. We then consider only those homomorphisms that respect this ordering and discard any homomorphism that violates it.

We can produce all the possible graphs on 5-vertices and 6-vertices using the code below

## C Computational Enumeration of Connected Graphs

Here we have the Sage/Python code which is used to enumerate connected _n_- vertex graphs, compute their normalized embedding matrix, encode their edge sets, test for _K_<sub>_n_-1</sub> minors, and export the matrix to a PDF. The same implementation is used for the cases _n_=5 and _n_=6.

