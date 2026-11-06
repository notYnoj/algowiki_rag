## A. Leaf centroid

**Lemma 18.** _Every tree S with_ \(n\ge 3\) _nodes has a leaf centroid, that can be found in_ O(_n_) _time._

_Proof._ Let _L_ be the set of leaves of _S_ and let \(\ell=|L|\). For an arbitrary node \(v\in V(S)\), let \(t(v)=(\ell(v),k(v))\) be the lexicographically largest tuple \((|L\cap V(C)|,|V(C)|)\) among the connected components _C_ of _S_\\_v_. We claim that if \(\ell(v)>\lfloor\frac{\ell}{2}\rfloor\), then there is a neighbor _u_ of _v_ such that _t(u_) is lexicographically smaller than _t(v_). By repeatedly moving to such a neighbor we will find a node _v_ with \(\ell(v)\le\lfloor\frac{\ell}{2}\rfloor\), as there are only finitely many possible values for _t(v_). Each connected component _C_ of _S_\\_v_ has at most one leaf that is not a leaf of _S_, namely the node that is adjacent to _v_. It follows that _v_ is a leaf centroid.

We now prove the claim. Let \(v\in V(S)\) with \(\ell(v)>\lfloor\frac{\ell}{2}\rfloor\). Let _C_ be the connected component of _S_\\_v_ with \(|L\cap V(C)|=\ell(v)>\lfloor\frac{\ell}{2}\rfloor\) and let _u_ be the neighbor of _v_ in _S_ which is contained in _V(C_). Let \(S'=S[V(S)\backslash V(C)]\).

Clearly, \(S'\) is one connected component of _S_\\_u_. First, consider the case when _u_ has degree at least 3 in _S_. Then _S_\\_u_ has at least two connected components besides \(S'\), each containing at least one leaf of _S_. Each of these components thus contains at most \(|L|-|V(S')\cap L|-1\le|V(C)|-1<\ell(v)\) leaves of _S_. Moreover, \(|S'\cap L|\le|L|-|L\cap V(C)|<\ell-\lfloor\frac{\ell}{2}\rfloor=\lceil\frac{\ell}{2}\rceil\le\ell(v)\). Thus, we have \(\ell(u)<\ell(v)\).

Second, consider the case when _u_ has degree 2 in _S_. Then _S_\\_u_ has two connected components, \(S'\) and, say, \(S''\). We have \(|L\cap V(S'')|=|L\cap V(C)|>\lfloor\frac{\ell}{2}\rfloor\), i.e. \(S''\) has more than half the leaves of _S_, and in particular \(|L\cap V(S'')|>|L\cap V(S')|\). Thus, by definition, \(t(u)=(|L\cap V(S'')|,|V(S'')|)\). But \(|V(S'')|=|V(C)|-1=k(v)-1\). As such, _t(u_) is lexicographically smaller than _t(v_).

The tuples _t(v_) can be computed for all nodes _v_ in _O(n_) time via a depth-first traversal of _S_. When deciding where to move from _v_, we need to query the tuples of neighbors of _v_, and pick the smallest. For each neighbor _u_ we charge the query to the (oriented) edge (_v,u_) of _S_. As we cannot revisit a vertex, each edge is charged at most once.

