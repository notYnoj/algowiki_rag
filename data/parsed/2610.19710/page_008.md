\(\blacktriangleright\) **Lemma 7** (Transitivity of \(\unknown\unknown\unknown\))**.** _Potential-separation is transitive along the shortest path, i.e., if y lies on the shortest path from x to z, then_

\(x\unknown\unknown y\wedge y\unknown\unknown z\Longrightarrow x\unknown\unknown z.\)

**Proof.** By triangle inequality, \(|\phi(x)-\phi(y)|+|\phi(y)-\phi(z)|\ge|\phi(x)-\phi(z)|\). Because _y_ lies on the shortest path from _x_ to _z_, we know that

\(d_G(x,z)=d_G(x,y)+d_G(y,z)\)<br> \(\ge|\phi(x)-\phi(y)|+|\phi(y)-\phi(z)|\)<br> \(\ge|\phi(x)-\phi(z)|,\)

which proves \(x\unknown\unknown z\). \(\blacktriangleleft\)

## 4.2 The dynamic-LOCAL algorithm

We design a dynamic-LOCAL algorithm that maintains a potential function \(\phi:V(G)\rightarrow\mathbb{N}\) with potential-separation and parity-consistency between all pairs of nodes. These constraints are enough to ensure that the function \(mod(\phi,3)\) produces a 3-coloring on the nodes of the graph, as we showed in Theorem 5. The algorithm is presented in Algorithm 1. An example execution is shown in Figure 2. We summarize and comment the update algorithm on an edge insertion here:

1. _Fix parity_: If the newly inserted edge connects two previously disconnected components, check whether they are parity-consistent. If they are not consistent, increment the potential of all nodes in one of the components by 3. This makes all pairs of nodes parity-consistent, but does not change the coloring. For balancing purposes, we increment the potential on the component that has the lower peak potential. This step is illustrated in Figure 2b.

2. _Clear edit area_: While the nodes are parity-consistent, they are not potential-separated, meaning that at the inserted edge, two nodes with a large difference in potential might be adjacent. To fix this, clear the potential of all nodes in the edit radius _D_ to an unassigned state. The radius _D_ is chosen proportional to the maximal potential, guaranteeing that the remaining assigned nodes are potential-separated (see the proof of \(x\unknown\unknown y\) in Lemma 8 for the precise analysis). This step is illustrated in Figure 2c.

3. _Expand borders_: For every assigned node _v_ that neighbors an unassigned node _w_, assign \(\phi(w)=\phi(v)-1\). Start from the nodes with the highest potential, and repeat until only nodes with potential 0 have unassigned neighbors. It is important to follow this order to avoid growing potential differences. This step is illustrated in Figure 2d.

4. _Fill the coloring_: The remaining unassigned nodes are surrounded by nodes of potential 0. All assigned nodes are parity-consistent, which for the surrounding nodes of equal potential means that all pairs among them have even distance, so a 2-coloring of the unassigned nodes is possible. Assign potentials 1 and 0 alternately to the remaining nodes of the bipartite graph, completing the coloring. This step does not happen in Figure 2, since no unassigned nodes are remaining. In fact, it may be possible to avoid this step in the algorithm entirely by choosing the edit radius _D_ exactly such that the previous step never leaves any unassigned nodes, but we will not explore this further as it requires additional analysis without affecting the worst-case locality.

