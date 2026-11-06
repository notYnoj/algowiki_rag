**Parameter:** We set \(k'=k+k(k-1)/2\), _q_=5_k_+3_k(k_-1)/2, and \(t=k'\).

Clearly, this construction can be carried out in polynomial time. Next, we will prove some structural properties about our construction, namely that the graph \(G'\) is bipartite (Claim 18) and \(\mu\) is a stable matching (Claim 19).

**Claim 18** _Graph_ \(G'\) _is bipartite._

_Proof._ We show that \(G'\) is a bipartite graph by creating a bipartition for \(G'\) as follows. For each \(i\in[k]\), and each \(u\in V_i\), we assign \(p_1^i\), _u_<sub>2</sub> and _u_<sub>4</sub> to one part and \(p_2^i\), _u_<sub>1</sub> and _u_<sub>3</sub> to another part. For each \(\{i,j\}\subseteq[k]\), _i\<j_, since a vertex \(e\in V(G')\) (corresponding to the edge \(e=uv,u\in V_i,v\in V_j\)) is connected to _u_<sub>3</sub> and _v_<sub>3</sub>, we assign _e_ and \(q_2^{ij}\) to the part containing \(p_1^i\), and assign \(\tilde{e}\) and \(q_1^{ij}\) to the part containing \(p_2^i\). Observe that each part is an independent set. Hence \(G'\) is a bipartite graph.

**Claim 19** \(\mu\) _is a stable matching._

_Proof._ We begin by noting that for any vertex \(u\in V(G)\), vertices _u_<sub>1</sub> and _u_<sub>2</sub> prefer each other over any other vertex in \(G'\). Therefore, edge _u_<sub>1</sub>_u_<sub>2</sub> is a static edge and must belong to every stable matching in \(G'\). Similarly, for each \(e\in E(G)\), we note that \(e\tilde{e}\) is a static edge in \(G'\), and thus belongs to every stable matching in \(G'\). Since _u_<sub>3</sub> is the first preference of _u_<sub>4</sub>, and the vertices which _u_<sub>3</sub> prefers over _u_<sub>4</sub> ( i.e., _u_<sub>2</sub> and vertices in E_<sub>u</sub>_) are matched to their first preferred vertices, it follows that there is no blocking edge with respect to \(\mu\). Hence, \(\mu\) is a stable matching in \(G'\).

**Correctness.** Next, we show the equivalence between the instance I of MCQ and J of LS-ASM. Formally, we prove the following:

U1 u2 u3 u4
X1 X2 X3 X4
v1 v2 v3 v4
y1 y2 y3 y4
P1
P2
P1
P2
2
P2
e1
e1
q1
q2
12
e2
e2

**Fig.3.** An illustration of the construction of graph \(G'\) in W\[1\]-hardness of LS-ASM. Here, blue colored edges belongs to the stable matching \(\mu\). Note that _V_<sub>1</sub>={_u,v,w_} and _V_<sub>2</sub>={_x,y,z_}, and _e_<sub>1</sub> and _e_<sub>2</sub> are edges in _E_<sub>12</sub>.

