Filled boxes are cliques: \(X'',X',Y,Y',C',C''\).

White boxes are independent sets: _X_.

Thick gray bands represent complete bipartite edge sets.

Parallel black edges represent the four matchings/copy maps.

Blue/red curves are sample coordinate-incidence edges into \(C'\). More specifically:

Blue: \(x_ic'_k\in E\Longleftrightarrow u_i[k]=1\).

Red: \(y_jc'_k\in E\Longleftrightarrow v_j[k]=0\).

7 A node \(x'\in X'\) cannot dominate any node in _X_ because these nodes have neighbors in \(C'\) and \(x'\) does not.

8 A node \(x'\in X'\) cannot dominate another node in \(X'\) because the two nodes have edges to different nodes in \(X''\). (This means that the nodes in \(X'\) cannot dominate any other node.)

9 Consider a node \(x'\in X'\). Its neighbors are in \(X'\cup X''\cup X\cup Y\) and it has neighbors in all these sets. The only other nodes that have neighbors in all these sets are other nodes \(x'_1\in X'\). But from the above point, we get that no \(x'\in X'\) is dominated by any other node.

10 Consider a node \(x''\in X''\). It can only potentially be dominated by nodes in \(X''\cup X'\), but we already know that the nodes in \(X'\) do not dominate any other nodes. Another node \(x''_1\) in \(X''\) also cannot dominate \(x''\) since \(x''\) and \(x''_1\) have different neighbors in \(X'\) due to the matching. Hence the nodes of \(X''\) are not dominated by any other node.

11 Similarly, a node \(y'\in Y'\) can only be dominated by nodes in \(Y'\cup Y\) , but since \(Y'\) is a clique and each \(y\in Y\) has only one neighbor in \(Y'\), _y_ cannot dominate \(y'\). Also, no other node of \(Y'\) can dominate \(y'\) since they have distinct unique neighbors in _Y_ . Thus the nodes of \(Y'\) are not dominated.

12 Analogous to the above point, the nodes of \(C''\) are not dominated by any other node.

X" clique
X' x' i
Y' clique
C' coordinate clique
X' clique
X' X X Y complete
yjyj
C' ck
X X X Y complete
Xix i
Y clique vectors vj E V
C" coordinate clique
X X Y complete
X independent vectors ui E U

**Figure 6.** A visualization of the graph constructed in Lemma B.2. Here:

