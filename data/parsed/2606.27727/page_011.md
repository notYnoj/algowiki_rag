the probability that both (_u,w_) and (_v,w_) survive. Fix a color \(c\in[Cn^\delta]\). We have:

\(Pr[(u,v,w)\text{survivesand}h(w)=c]\)<br> \(=Pr_{h\leftarrow\mathcal{H}}[h(w)=c\wedge(\forall k\in(N(u)\cup N(v))\backslash\{w\})h(k)\neq c]\)<br> \(=\frac{1}{Cn^\delta}Pr_{h\leftarrow\mathcal{H}}[(\forall k\in(N(u)\cup N(v))\backslash\{w\})h(k)\neq c|h(w)=c]\)<br> \(\ge\frac{1}{Cn^\delta}\left(1-Pr_{h\leftarrow\mathcal{H}}[(\exists k\in(N(u)\cup N(v))\backslash\{w\})h(k)=c|h(w)=c]\right)\)<br> \(\ge\frac{1}{Cn^\delta}\left(1-|(N(u)\cup N(v))\backslash\{w\}|\cdot\frac{1}{Cn^\delta}\right)\)<br> \(\ge\frac{1}{Cn^\delta}\left(1-2n^\delta\cdot\frac{1}{Cn^\delta}\right)\ge\frac{1}{Cn^\delta}\left(1-\frac{2}{C}\right).\)

For each of the \(Cn^\delta\) choices of _c_, all of the events in question are disjoint. Summing over all of them, the probability (_u,v,w_) survives is at least 1-2_/C_. Setting \(C\ge 1\) large, we conclude that every triangle in the original graph survives with constant probability.

We now use the color classes to express the remaining graph as a smaller matrix. We note that with probability at least 1-1_/D_<sup>2</sup>, all of the color classes have size at most \(Dn^{1-\delta}\); in the end, we will choose _D_ to be a large constant. To see this, let \(X_c:=\sum_{w\in K}\unknown[h(w)=k]\), the number of vertices that are assigned color class _c_. Note that \(\mathbb{E}[X_c]=n^{1-\delta}/C\). By pairwise independence, \(\mathsf{Var}(X_c)=\sum_{w\in K}\mathsf{Var}(\unknown[h(w)=k])\le n^{1-\delta}/C\). By Chebyshev’s inequality,

\(Pr[X_c-\mathbb{E}[X_c]\ge Dn^{1-\delta}]\le\frac{1}{CD^2n^{1-\delta}}.\)

Union bounding over all \(Cn^\delta\) color classes, we have that all color classes have size at most \(Dn^{1-\delta}\) with probability at least 1-1_/D_<sup>2</sup>. We construct an \(n\times n^\delta\) matrix _A_ that captures edges between _I_ and _K_, as well as a \(n^\delta\times n\) matrix _B_ that captures edges between _K_ and _J_. Note that all indices _i,j_ are in [_n_] and index their respective vertex sets, whereas the _k_ indices are in \([O(n^{1-\delta})]\) and determine a color class of _K_. We also assume that we re-index the nodes in each color class of _K_, so that the tuples \((k,v)\in[n^\delta]\times[O(n^{1-\delta})]\) uniquely identify some node in the _k_th color class of _K_.

We now set the (_i,k_) entry of _A_ to the node in the _k_th color class of _K_ that the vertex _i_ has an edge to (and the (_k,j_) entry of _B_ analogously). If the vertex has no edge to this color class, set the entry to \(\perp\). Now, if there exists a _k_ such that _A[i,k_]=_B[k,j_]=_v_ and \(v\neq\perp\), both _i_ and _j_ share an edge to the _v_th node of the _k_th color class in _K_. Thus, if (_i,j_) is itself an edge, then _i,j,(k,v_) form a triangle.

Thus, with constant probability, the All-Edges Equality Inner Product problem on the matrices _A_ and _B_ with _P_:=_E_, the edge set of _G_, returns the same answer as the Sparse Triangle Detection problem on the original graph. \(\blacktriangleleft\)

We now give an algorithm to solve All-Edges Equality Inner Product faster than the obvious \(n^{1+2\delta}\) time solution. The high-level idea is as follows: we use a linear hash function to hash the matrix entries down to _O_(log_w_) bits, write the problem down in a compressed matrix form by packing multiple entries into a single word, and then use word operations to compute the equality inner product.

\(\blacktriangleright\) **Theorem 21.** _For every_ \(\delta\in(0,1/2]\) _and word size_ \(w\ge\Omega(logn)\)_, there is a Las Vegas_ \(O(n^{1+2\delta}(logw)/w)\)_-time algorithm for the All-Edges Equality Inner Product problem on_ \(n\times n^\delta\) _and_ \(n^\delta\times n\) _matrices._

