**Proof.** Let **G**=(_V,E_). First, we transform **G** into a tripartite graph on 3_n_ nodes by creating three disjoint copies of the vertex set, denoted _A,B_, and _C_, while retaining only those edges that connect vertices in different partitions. It is not difficult to see that the resulting tripartite graph contains a triangle if and only if the original graph **G** contained a triangle.

Therefore, assume that **G** is a tripartite graph with vertex partitions _A_={_a_<sub>1</sub>_,...,a<sub>n</sub>},B_={_b_<sub>1</sub>_,...,b<sub>n</sub>_}, and _C_={_c_<sub>1</sub>_,...,c<sub>n</sub>_}. We construct \(\mathbf{H}=(V',E')\) as follows (see Figure 5):

The vertex set is \(V'=A\cup B\cup C\cup\{u,v,p,p'\}\), where _u,v,p_, and \(p'\) are auxiliary vertices.

The edge set \(E'\) includes all original edges between _A_ and _C_ and between _C_ and _B_. However, it contains the complement of the edges between _A_ and _B_; that is, \(E'\cap(A\times B)=\{\{a,b\}\in A\times B:\{a,b\}\notin E\}\).

Additionally, \(E'\) contains a path \(u,p,p',v\) of length three connecting _u_ and _v_.

Finally, \(E'\) contains edges {_u,a<sub>i</sub>_} and {_v,b<sub>i</sub>_} for all \(i\in[1..n]\).

We observe that (i) holds. This is because the path \(u,p,p',v\) has length three, and \(d_\mathbf{H}(u,v)\ge 3\) because \(N[u]=A\cup\{u,p\}\) and \(N[v]=B\cup\{v,p'\}\) are disjoint, so there is no path of length one or two.

It remains to show that **H** contains a _uv_-trail if and only if **G** contains a triangle. First, assume **G** contains a triangle on vertices {_a<sub>i</sub>,b<sub>j</sub>,c<sub>k</sub>_}. We claim that _u,a<sub>i</sub>,c<sub>k</sub>,b<sub>j</sub>,v_ is a _uv_-trail. To see this, notice that this path has length four and is chordless because _u_ and _v_ have no neighbors in {_c<sub>k</sub>,b<sub>j</sub>_} and {_a<sub>i</sub>,c<sub>k</sub>_}, respectively, and {_a<sub>i</sub>,b<sub>j</sub>_} is not an edge in **H** because it was an edge in **G**.

On the other hand, assume there exists a _uv_-trail \(\pi\) in **H**. We observe that \(\pi\) cannot utilize any nodes in \(\{p,p'\}\). Furthermore, \(\pi\) can contain at most one vertex from each set _A_ and _B_. If \(\pi\) were to contain two distinct vertices \(a_i,a_{i^\prime}\) in that order, the edge \(\{u,a_{i^\prime}\}\) would constitute a chord; a similar argument holds for nodes in _B_. Thus, \(\pi\) must follow the sequence: _u_, followed by some _a<sub>i</sub>_, then vertices in _C_, then some _b<sub>j</sub>_, and finally _v_. Since there are no edges between vertices within _C_, we have \(\pi=u,a_i,c_k,b_j,v\) for some \(c_k\in C\). Because \(\pi\) is chordless and hence \(\{a_i,b_j\}\notin E'\), it follows that **G** contains the triangle \(a_i,c_k,b_j\).

This yields the following result.

**Lemma 4.16.** _For any_ \(k\ge 3\)_, suppose there exists an algorithm that, in time_ \(\mathrm{T}=\Omega(n^2)\)_, determines whether an n-node graph_ **G** _contains a uv-trail for two vertices u,v with d(u,v_)=_k. Then there is an algorithm solving triangle detection in time_ O(T).

**Proof.** For _k_=3, we can use the construction from Lemma 4.15: given an input graph for triangle detection, the graph **H** is constructed and then the _uv_-trail detection algorithm from the problem statement is used.

p
p'
u
a3
b1
a3
b1
v
a3
b2
a2
b2
a2
b3
a1
b3
a1
C1
C2
C3
C1
C2
C3

\(\blacksquare\)

**Figure 5.** An example of the graph **H** used in Lemma 4.15.

