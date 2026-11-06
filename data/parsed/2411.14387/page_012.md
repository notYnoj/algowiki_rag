T_<sub>j</sub>_ is constructed by running the following recursive algorithm, which builds a tree T<sub>out</sub>:

Start at the root of T , and let _x_ be the current node.

If \(x\in S_j\), then

make _x_ the root of T<sub>out</sub>;

form _x_’s left subtree in T<sub>out</sub> by recursing on _x_’s left subtree in T ;

form _x_’s right subtree in T<sub>out</sub> by recursing on _x_’s right subtree in T .

If \(x\unknown\in S_j\) then since _S<sub>j</sub>_ is contiguous, at most one of _x_’s left and right subtrees in T can contain elements from _S<sub>j</sub>_.

If there is one such subtree, form T<sub>out</sub> by recursing on it.

Otherwise let T<sub>out</sub> be the empty tree.

This algorithm clearly has the desired properties:

Clearly, by construction, T_<sub>j</sub>_ is a binary search tree and its set of keys is _S<sub>j</sub>_.

If \(b,x\in S_j\) and \(x\prec_\mathcal{T}b\), then \(x\prec_{\mathcal{T}_j}b\), because the only way to get to _x_ is to first pass through _b_, add it as a root of the current subtree, then recurse on _b_’s subtree that contains _x_, which eventually adds _x_ to T_<sub>j</sub>_ as a descendent of _b_.

T_<sub>j</sub>_ is unique since the only nontrivial choice the algorithm makes is to add _x_ as a root, but this is necessary since it must be an ancestor of all of the keys that later get added to this part of T_<sub>j</sub>_.

\(\blacktriangleright\) **Definition 22.** _Let_ \(\widetilde{\mathcal{T}}\) _be the unique binary search tree over_ [_l_] _such that if_ \(x\prec_\mathcal{T}b\) and \(S_{jb},S_{jx}\prec_\mathcal{T}b\) _then_ \(j_x\prec_\widetilde{\mathcal{T}}j_b\).

\(\widetilde{\mathcal{T}}\) is constructed by running the following recursive algorithm, which builds a tree T<sub>out</sub>:

Start at the root of T , and let _x_ be the current node.

If _j<sub>x</sub>_ hasn’t already been seen earlier in the algorithm (which happens iff _x_ is the lowest common ancestor of all of _S<sub>j<sub>x</sub></sub>_ in T ), then

make _j<sub>x</sub>_ the root of T<sub>out</sub>;

form _j<sub>x</sub>_’s left subtree in T<sub>out</sub> by recursing on _x_’s left subtree in T ;

form _j<sub>x</sub>_’s right subtree in T<sub>out</sub> by recursing on _x_’s right subtree in T .

If _j<sub>x</sub>_ has already been seen earlier in the algorithm, then some ancestor of _x_ was also in _S<sub>j<sub>x</sub></sub>_, and _S<sub>j<sub>x</sub></sub>_ is contiguous, so _S<sub>j<sub>x</sub></sub>_ must contain either _x_’s entire left subtree, or _x_’s entire right subtree. That means that at most one of _x_’s subtrees can contain elements \*not\* in _S<sub>j<sub>x</sub></sub>_.

If there is one such subtree, form T<sub>out</sub> by recursing on it.

Otherwise, let T<sub>out</sub> be the empty tree.

This algorithm clearly has the desired properties:

Clearly, by construction, \(\widetilde{\mathcal{T}}\) is a binary search tree and its set of keys is [_l_].

If \(x\prec_\mathcal{T}b\) and \(S_{jb},S_{jx}\prec_\mathcal{T}b\) then:

We can assume \(j_x\neq j_b\) and thus \(x\neq b\), otherwise the claim is trivially true.

Since \(S_{jb}\prec_\mathcal{T}b\), _b_ must be the lowest common ancestor of all of _S<sub>jb</sub>_ in T , so _j<sub>b</sub>_ gets added to \(\widetilde{\mathcal{T}}\) when the algorithm is looking at node _b_.

Also, since \(S_{j_x}\prec_\mathcal{T}b\) and \(j_x\neq j_b\), that means that all the elements from _S<sub>j<sub>x</sub></sub>_ are descendents of _b_, so _j<sub>x</sub>_ will be added to \(\widetilde{\mathcal{T}}\) in one of the recursive branches launched when looking at _b_.

Therefore _j<sub>x</sub>_ will be a descendent of _j<sub>b</sub>_ in \(\widetilde{\mathcal{T}}\).

\(\widetilde{\mathcal{T}}\) is unique since the only nontrivial choice the algorithm makes is to add _j<sub>x</sub>_ as root when it first sees an element from _S<sub>j<sub>x</sub></sub>_, but this is necessary since for any _j_ which will eventually be added to this part of the tree, _S<sub>j</sub>_ must have been completely contained in _x_’s subtree, and therefore _j<sub>x</sub>_ must be an ancestor of _j_.

