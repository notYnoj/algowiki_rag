or fewer "steps" outward, we have found a cycle of length at most 5. Since the graph is bipartite by assumption, it cannot have odd cycles, so we can return "4-cycle." After verifying that none of the nodes in _N_ participate in a 4-cycle, we can return \(G'\), the subgraph of _G_ induced by _V_\\_N_. Both the correctness and the degree bound follow directly from the construction. \(\blacktriangleleft\)

Because of this, it suffices to solve 4-cycle in the following setting:

\(\blacktriangleright\) **Definition 27 (4-Cycle Detection).** _Given a graph with m=O(n_<sup>3/2</sup>) _edges and maximum degree_ \(\Delta=O(\sqrt{n})\)_, decide whether there exists a 4-cycle._

\(\blacktriangleright\) **Definition 28 (Concatenated Element Distinctness).** _Given k column vectors L_<sub>1</sub>_,...,L<sub>k</sub> of n_ \(\ell\)_-bit elements each, for every pair i,j of columns, element-wise concatenate them to a produce a new list Li,j containing n length-_\(2\ell\) _elements. If for all i,j, the list Li,j has distinct elements, accept, else reject._

We now reduce 4-cycle detection to this problem, and then use the word tricks from Section 3 on Concatenated Element Distinctness to improve the 4-cycle runtime when we have large word size.

**Reminder of Theorem 6.** For \(T(n,k,\ell)\ge n+k+\ell\), if Concatenated Element Distinctness can be solved in \(O(T(n,k,\ell))\) time, then 4-cycle detection in _n_-node graphs can be done in \(O(T(n,\sqrt{n},(log_2n)/2))\) time. This reduction succeeds with constant probability.

**Proof of Theorem 6.** We begin by imposing a bipartition on the graph, randomly assigning half the vertices to each side and deleting all edges within each side. The probability that all edges in a particular 4-cycle survive is constant. We then use color coding to reduce to an equality product-like problem, similarly to the sparse triangle reductions.

In particular, let \((L\cup R,E)\) be the new graph. Randomly partition _R_ into \(\sqrt{n}\) color classes, and for every vertex \(v\in L\), if _v_ has multiple neighbors in a particular color class, delete all but one of the associated edges. As before, every edge in the graph survives with constant probability. Once we have this more structured instance, we can write column vectors corresponding to each color class.

For every color class \(k\in[\sqrt{n}]\), write a column vector _L<sub>k</sub>_ such that _L<sub>k</sub>[i_] is the element of the _k_th color class that \(i\in L\) has an edge to (or \(\perp\) if there is no such edge). Now, we claim that it suffices to solve the Concatenated Element Distinctness problem to solve Bounded-Degree Four Cycle Detection. To see this, if we have a yes-instance of the former, there are columns _i_ and _j_ such that if we concatenate them elementwise, the resulting column has duplicate values, say at indices _u_ and _v_. By construction, this implies that _Li[u_]=_Li[v_] and _L<sub>j</sub>[u_]=_L<sub>j</sub>[v_], so _u_ and _v_ share a neighbor in the _i_th color class, namely _Li[u_], and also in the _j_th color class, _L<sub>j</sub>[u_]. Thus, these four nodes form a 4-cycle. The reverse direction is symmetric.

Each of the steps here take linear time in the size of the graph, which here is _O(m+n_)=_O(n_<sup>3/2</sup>) time. We note that there are a total of \(k:=\sqrt{n}\) columns, corresponding to the color classes, and that the indices of each node within a color class requires \(\ell:=log_2n/2\) bits to write down as they are over the universe \([\sqrt{n}]\). \(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 29.** _There is a deterministic algorithm for Concatenated Element Distinctness, on_ \(O(\sqrt{n})\) _lists each containing n elements of size O_(log_n_) _that runs in O(n_<sup>2</sup>log<sup>2</sup>_n/w_) _time._

