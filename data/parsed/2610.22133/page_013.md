**Lemma 4.2.** _Given two Boolean matrices A and B of size_ \(s\times n\) _and_ \(n\times n\)_, one can construct in time_ O(_n_<sup>2</sup>+_ns_) _an instance of the induced subgraph connected component problem on a_ 2_n-node graph with a set of size s_=|S|_, such that solving this instance yields the product AB._

**Proof.** Based on _B_, we construct the graph **G**=(_V,E_) as follows (for an example, refer to Figure 3):

_V_ contains 2_n_ vertices, denoted by _x_<sub>1</sub>_,...,x<sub>n</sub>,y_<sub>1</sub>_,...,y<sub>n</sub>_; and

_E_ contains edges such that the nodes {_x_<sub>1</sub>_,...,x<sub>n</sub>_} are fully connected (i.e., they form a clique). Moreover, an edge {_x<sub>k</sub>,y<sub>j</sub>_} exists if and only if _B[k,j_]=1.

Based on _A_, we construct the family of sets S as follows: for each row \(i\in[1..s]\), we add a set _Si_ to S containing all nodes _x<sub>k</sub>_ such that _A[i,k_]=1. We also add to _Si_ all nodes in {_y_<sub>1</sub>_,...,y<sub>n</sub>_}. That is, \(Si=\{x_k:k\in[1..n],A[i,k]=1\}\cup\{y_1,\dots,y_n\}\).

Note that by the construction of the clique, for each \(Si\in\mathcal{S}\), there is a unique connected component in **G**[_Si_] that contains all nodes in \(\{x_1,\dots,x_n\}\cap S_i\). We call this the _giant component_ of **G**[_Si_]. (Without loss of generality, we assume all \(\{x_1,\dots,x_n\}\cap S_i\) are non-empty, otherwise the corresponding row is the zero vector and computing the product for that row is trivial.)

To infer the product _AB_, we make the following claim: _AB[i,j_]=1 if and only if the giant component of **G**[_Si_] is non-empty and contains _y<sub>j</sub>_. The only if direction is straightforward: if there is a \(k\in[1..n]\) such that _A[i,k_]=1 and _B[k,j_]=1, then \(x_k\in S_i\) and the edge \(\{x_k,y_j\}\in E\). Therefore, _y<sub>j</sub>_ is in the giant component. For the if direction, assume that _y<sub>j</sub>_ is in the giant component. This is only possible if there is a \(k\in[1..n]\) such that \(\{x_k,y_j\}\in E\), which is equivalent to _B[k,j_]=1. Since \(x_k\in S_i\), we must also have _A[i,k_]=1. Thus, we have _AB[i,j_]=1.

## 4.2 Recognizing AT-free Graphs in Matrix Multiplication Time

In this section, we present an \(\tilde{\mathcal{O}}(n^\omega)\)-time algorithm for recognizing AT-free graphs. To achieve this, we first introduce a helpful relationship between neighborhood-deleted components that share the same vertices across different **G**_<sub>x</sub>_.

**Proposition 4.3.** _Let G_=(_V,E_) _be an undirected graph. Consider a vertex_ \(x\in V\) _and two vertices_ \(a,b\in\mathbf{G}_x\) _such that a and b belong to distinct neighborhood-deleted components of x, i.e.,_ \(C_x(a)\neq C_x(b)\)_. The following conditions are equivalent:_

(1) _The neighborhood-deleted component containing a is identical in_ **G**_<sub>x</sub> and_ **G**_<sub>b</sub>, i.e.,_ \(C_x(a)=C_b(a)\).

(2) _The neighborhood N(b_) _contains the neighborhood of_ \(C_x(a)\).

**Proof.** We first observe that \(C_x(a)\subseteq C_b(a)\) always holds. Since \(C_x(a)\neq C_x(b)\), no vertex in \(C_x(a)\) is adjacent to _b_; thus, \(N[b]\cap C_x(a)=\varnothing\) and all paths within \(C_x(a)\) remain intact in **G**_<sub>b</sub>_.

Suppose Condition (2) fails, i.e., there exists \(v\in N(x)\cap N(C_x(a))\) such that \(v\notin N(b)\). Since _v_ is adjacent to \(C_x(a)\) and is not removed in **G**_<sub>b</sub>_, we have \(v\in C_b(a)\). However, \(v\notin C_x(a)\) (as \(v\in N(x)\)), which implies \(C_x(a)\neq C_b(a)\), so Condition (1) fails.

X1
y1
S1
1
0
1
0
X
0
1
0
1
1
1
0
1
1
0
1
1
0
0
1
1
0
1
1
0
1
1
0
1
1
A
B
AB
X4
y4
G = (V, E)

**Figure 3.** An example for the construction in Lemma 4.2

