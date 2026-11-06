potential output for the enumeration sub-routine. This turns out to place quite a substantial limitation on the pruning, and one we address in section 5.1.

The key to the preprocessing part of the algorithm is the repetition until the reduction strategies can have no further impact on the size of the graph. This strategy allows us to iteratively uncover and remove vertices that cannot be in a clique without resorting to complex checking procedures.

Each loop starts with a greedy algorithm to obtain a clique that functions as an approximation to the MWC. This yields a lower bound for the MWC size, and allows the algorithm to more efficiently rule out solutions. The algorithm achieves this by systematically removing the vertex with most conflicts (in the MWC case, a "conflict" would be a missing edge) to the remaining subgraph until there are no conflicts left, giving us a clique. It should be noted that clearly this clique is not necessarily optimal, but is generally sufficient for the next steps.

This is followed by a greedy vertex colouring algorithm, which takes the ordering from the previous step and assigns each vertex the lowest colour that does not conflict. Given a vertex colouring, two vertices of the same colour by definition cannot share an edge, so cannot be in the same clique.

Suppose that the graph induced by the neighbourhood, _N<sub>G</sub>(v_), of a vertex _v_ has a proper colouring with colour classes _P_<sub>1</sub>_,...,P<sub>k</sub>_. A clique containing _v_ contains at most one vertex from each colour class. Therefore,

\(U(v)=w(v)+\sum_{r=1}^kmax_{u\in P_r}w(u)\)

is a valid upper bound on the weight of every clique containing _v_. Different proper colourings may give different weighted bounds even when they use the same number of colours.

It should be noted that the converse is not true: simply picking a vertex from each colour does not guarantee a clique, as having different colours does not guarantee they share an edge. Combining this upper bound with the lower bound established by exhibiting a clique, this gives a pruning algorithm specifically for the enumeration of all optima: a vertex _v_ can be removed only when the upper bound based on colouring _U(v_) on the weight of any clique containing _v_ is strictly smaller than the current lower bound _L_. Equality cases must be retained, since a vertex with _U(v_)=_L_ may still belong to a maximum weight clique if the current lower bound is already optimal.

While improving the number of colours required to colour the graph does not directly cause an improvement in our bounds, it reduces the number of terms we must sum over to establish the upper bound for each vertex, leading to generally lower upper bounds. Clearly, the specifics of the colouring are also important for establishing our bounds. In the ideal world, we would find the optimal colouring for each vertex and its neighbours, which would allow us to more accurately prune the graph. However, this would dramatically increase the computational complexity of a step that is looped and is not guaranteed to produce results. Therefore, the algorithm in [5] uses a single greedy colouring, which approximates an optimal<tbc>

