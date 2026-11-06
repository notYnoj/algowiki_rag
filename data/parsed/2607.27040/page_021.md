_K_ is also reverted to its initial state as the newly pushed value is popped out when we move back to the parent. By moving to the right child then back to the parent, the same equality \(j'=j'_i\), \(l'=l'_i\), \(r'=r'_i\) and unchanged _K_ holds. Thus, moving to the parent correctly reverses moving to a child.

By induction, starting from the root of the subtree _n<sub>j</sub>_ with the valid initialized ranges, any sequence of moving to the left child, right child, or parent yields a valid state with the correct block of active representatives \(a_{l^\prime}\dots a_{r^\prime}\) for the current node as long as the current node is a valid node in the subtree.

Using the above three move primitives, perform a standard in-order traversal of the subtree rooted at the scapegoat node. Upon reaching a leaf \(n_{j^\prime}\), exchange the active representatives \(a_{l^\prime}\dots a_{r^\prime}\) that should be in \(n_{j^\prime}\) into the first \(r'-l'+1\) positions of the leaf node \(n_{j^\prime}\)’s corresponding gap \(L_{j^{\prime\prime}-s_{\#}^\prime+1}\). We know that a node \(n_{j^\prime}\) is a leaf and has no more children if \(j'\ge s'_\#\) by the definition of the tree.

After dynamic rebalancing, the gap invariant is restored. Before the insertion, all gaps followed the gap invariant and contained less than 7 active representatives. The insertion altered the size of _L<sub>i</sub>_ to 8, triggering the rebalancing. Thus, viewing from the scapegoat node, the size of the child containing _L<sub>i</sub>_ is bounded by\(z'_1\le 7\left(span\left(n_{2j}\right)-1\right)+8=7span\left(n_{2j}\right)+1\), and the size of the other child is bounded by \(z'_2\le 7span\left(n_{2j}\right)\). By condition (A.4), we know the difference in sizes between the two children is at least 2. If \(z'_1>z'_2\), then \(z'_2\le z'_1-2=7span\left(n_{2j}\right)-1\), thus the size of the rebuilt subtree is given by \(z'_1+z'_2\le 2(7span\left(n_{2j}\right))=7span\left(n_j\right)\). In the latter case where \(z'_2>z'_1\), \(z'_1\le z'_2-2=7span\left(n_{2j}\right)-2\), and summing gives the bound \(z'_1+z'_2\le 2(7span\left(n_{2j}\right))-2\le 7span\left(n_j\right)\). Thus, this inequality connecting _z_=size(_n<sub>j</sub>_) and span(_n<sub>j</sub>_) holds in either case.

Because size (_n_<sub>2_k_</sub>)-size (\(n_{2k+1}\)) \(\le 1\) for all nodes in the rebuilt subtree, by induction it can be shown that any two nodes _n_<sub>_k_<sub>1</sub></sub> and _n_<sub>_k_<sub>2</sub></sub> on the same level in the rebuilt subtree obeys \(\left|size\left(n_{k_1}\right)-size\left(n_{k_2}\right)\right|\le 1\). Using this property, the size of a leaf node _n_<sub>leaf</sub> in the rebuilt subtree satisfies

\(size\left(n_\text{leaf}\right)\le\left[\text{size}\left(n_j\right)/span\left(n_j\right)\right]\)

Shown above size \(\left(n_j\right)\le 7span\left(n_j\right)\), so

\(size\left(n_\text{leaf}\right)\le 7\)

Likewise, the size of each leaf node is at least \(\left|size\left(n_j\right)/span\left(n_j\right)\right|\ge 1\) by size \(\left(n_j\right)\ge span\left(n_j\right)\). Thus, the gap invariant 0_\<k\<_8 is restored.

We also show that the rebuild does not change the order of active representatives. The linear scan collects active representatives from the subtree into the rebuild buffer in the same order as they appear in the library. At every step of the traversal downwards to the leaves, we distribute the left half of the active representatives to the left child, and the right half to the right child. By induction, for any two collected active representatives _a<sub>x</sub>_ and _a<sub>y</sub>_ where _x\<y_, _a<sub>x</sub>_ will be placed before _a<sub>y</sub>_ in the library, maintaining local order within the rebuilt subtree. Furthermore, as elements are only rearranged within the rebuilt subtree, global order is also maintained.

Now, let us evaluate the total cost of an instance of dynamic rebalancing.

At any step of the traversal, we set \(z'_1=z\), count \(z'_2=size\left(n_{j\oplus 1}\right)\) using \(z'_2\) comparisons, then set \(z=z'_1+z'_2\), increasing _z_ by \(z'_2\). Thus, it requires 1 comparison to count every additional active representative. Initially, the count starts at 8, thus we counted _z_-8 additional active representatives by this method, which requires _z_-8 comparisons in total. Arithmetic operations during traversal are negligible at _O_(1) per level traversed.

