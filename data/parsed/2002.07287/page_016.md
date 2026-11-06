\(\blacktriangleright\) **Definition 14.** _(rooted tree isomorphism) By induction two rooted trees T and T_ \(T'\) _are isomorphic if and only if_

(_a)_ _T and T_ \(T'\) _consist of only one node, or_

_(b)_ _the roots r and_ \(r'\) _of T and T_ \(T'\)_, respectively, have the same number m of children, and there is some ordering T_<sub>1</sub>_,...,Tm of the maximal subtrees below the children of r and some ordering_ \(T'_1,\dots,T'_m\) _of the maximal subtrees below the children of_ \(r'\) _such that Ti and T_ \(T'_i\) _are isomorphic for all_ \(1\le i\le m\).

We start to describe a folklore algorithm for tree isomorphism that requires \(\Theta(nlogn)\) bits on _n_-node trees. Let _T_<sub>1</sub> and _T_<sub>2</sub> be two rooted trees. The algorithm processes the nodes of each tree in rounds. In each round, all nodes of depth _d_=max_,...,_0 are processed. Within a round, the goal is to compute a _classification number_ for every node _u_ of depth _d_, i.e., a number out of {0_,...,n_} that represents the structure of the maximal subtree below _u_. The correctness of the algorithm is shown in [30] and follows from the invariant that two subtrees in the trees _T_<sub>1</sub> and _T_<sub>2</sub> get the same classification number exactly if they are isomorphic.

Since we later want to modify the algorithm, we now describe it in greater detail. In an initial process assign the classification number 0 to every leaf in each tree. Then, starting with the maximal depth do the following: start by computing (for each tree) the _classification vector_ of each non-leaf _v_ of depth _d_ consisting of the classification numbers of _v_’s children, sorted lexicographically. After doing this in each tree, compute the classification number for the non-leafs as follows: for each tree _T_<sub>1</sub>_,T_<sub>2</sub> put the classification vectors of depth _d_ into a single sequence S<sub>1</sub> and S<sub>2</sub>, respectively. Sort each of these sequences lexicographically by interpreting each classification vector in the sequence as a number. Then assign classification numbers 1,2,3, etc. to the vectors in the (now sorted) sequences S<sub>1</sub>,S<sub>2</sub> such that two vectors get the same number exactly if they are equal (among both sequences). By induction the invariant holds for all new classification numbers. Repeat the whole procedure iteratively for the remaining depths until reaching the root. By the invariant above, both trees are isomorphic exactly if the roots of both trees have the same classification number.

The algorithm above traverses the nodes in order of their depth, starting from the largest and moving to the smallest, until it reaches the root. One key modification we make to achieve our goal of making the aforementioned algorithm space efficient, is that we traverse the nodes in order of their height starting from height 0 (first round) until reaching the root with the largest height (last round), i.e., in _increasing height_. As mentioned, the standard algorithm requires the nodes of the tree to be output in _shrinking depth_. While there is a succinct data structure due to He et al. [45] that provides us with all necessary

1 1
1 1
2 0
1 2
0 1
1 2
0 1
0 1
0 0
0 0
0 0
1 0
1 0
0 ((0)) ((0)) ((0))

**Figure 4** An example of the algorithm with isomorphic trees _T_<sub>1</sub> (left) and _T_<sub>2</sub> (right). The numbers inside the nodes and above the vectors are classification numbers. The vectors within the parenthesis are the sorted classification vectors of maximal subtrees.

