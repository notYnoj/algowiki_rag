## 14 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

Conversely, assume Condition (2) holds. Every vertex \(v\in N(x)\cap N(C_x(a))\) is removed in **G**_<sub>b</sub>_ because \(v\in N(b)\). Since any path from _C<sub>x</sub>(a_) to the rest of the graph must pass through these boundary vertices in _N(x_), their removal isolates _C<sub>x</sub>(a_) in **G**_<sub>b</sub>_. Therefore, no additional vertices can be reached from _a_ in **G**_<sub>b</sub>_, yielding _C<sub>x</sub>(a)=C<sub>b</sub>(a_), so Condition (1) holds.

We now prove a quantitative lemma essential for characterizing AT-free graphs. Let \(\mathcal{C}_x=\{C_x(v):v\in\mathbf{G}_x\}\) denote the set of neighborhood-deleted components of **G**_<sub>x</sub>_. For any subset of components \(\mathcal{H}\subseteq\bigcup_{x\in V}\mathcal{C}_x\), this lemma establishes, for every \(x\in V\) , a lower bound on the number of pairs (_y,C_) such that _C_ is a member of both \(\mathcal{C}_x\cap\mathcal{H}\) and \(\mathcal{C}_y\cap\mathcal{H}\).

**Lemma 4.4.** _Let_ **G**=(_V,E_) _be an AT-free graph. Let_ \(\mathcal{C}_x=\{C_x(v):v\in\mathbf{G}_x\}\) _be the set of connected components in_ **G**_<sub>x</sub>, and define_ \(\mathcal{C}:=\bigcup_{x\in V}\mathcal{C}_x\).

_For any subset_ \(\mathcal{H}\subseteq\mathcal{C}\)_, let_ \(\mathcal{H}_x:=\mathcal{C}_x\cap\mathcal{H}\)_, let_ \(s_x:=max_{C\in\mathcal{H}_x}|C|\) _denote the size of the largest component in_ H_<sub>x</sub>, and let_ \(V_x:=\bigcup_{C\in\mathcal{H}_x}C\) _be the set of all vertices in_ **G**_<sub>x</sub> belonging to components in_ H_<sub>x</sub>. Then, for every_ \(x\in V\) _such that_ H_<sub>x</sub> is non-empty, we have:_

\(|\{(y,C)\in V_x\times\mathcal{H}_x:C\in\mathcal{H}_y\}|\ge|V_x|^2/(4s_x)-|V_x|.\)

**Proof.** Fix \(x\in V\) . We begin by defining an auxiliary undirected graph **H**_<sub>x</sub>_ on the vertex set _V<sub>x</sub>_. An edge {_a,b_} exists in **H**_<sub>x</sub>_ if and only if \(C_x(a)\neq C_x(b)\), \(C_x(a)\neq C_b(a)\), and \(C_x(b)\neq C_a(b)\).

\(\square\) Claim 4.5. _The graph_ **H**_<sub>x</sub> is triangle-free; otherwise,_ **G** _would contain an AT._

Proof. Suppose **H**_<sub>x</sub>_ contains a triangle on vertices _a,b,c_. We show these vertices form an AT in **G**. Since all edges {_a,b},{b,c},{c,a_} exist in **H**_<sub>x</sub>_, we observe:

\(\bullet\) **1** The vertices _a,b_, and _c_ are pairwise non-adjacent. This is because from the existence of the edges {_a,b},{b,c},{c,a_} in **H**_<sub>x</sub>_ follows that _a,b_, and _c_ belong to distinct connected components of **G**_<sub>x</sub>_.

\(\bullet\) **2** There exists an _a-b_ path in **G** that avoids _N_\[_c_\]. Since \(x\notin N[c]\) (as \(c\in\mathbf{G}_x\)), it suffices to show that there are _a-x_ and _b-x_ paths avoiding _N(c_). By symmetry, we focus on the _a-x_ path.

Since \((a,c)\in\mathbf{H}_x\), we have \(C_x(a)\neq C_c(a)\). By Proposition 4.3, there exists a vertex \(v\in N(x)\cap N(C_x(a))\) such that \(v\notin N(c)\). Let \(a'\in C_x(a)\) be a neighbor of _v_. An _a-x_ path avoiding _N(c_) is formed by concatenating a path from _a_ to \(a'\) within _C<sub>x</sub>(a_), the edge \(\{a',v\}\), and the edge {_v,x_}.

By symmetry, _b-c_ and _a-c_ paths exist that avoid _N_\[_a_\] and _N_\[_b_\], respectively. Thus, _a,b,c_ is an AT, contradicting that **G** is AT-free. \(\square\)

By Mantel’s Theorem<sup>11</sup> \[Man07\], the graph **H**_<sub>x</sub>_ contains at most |_V<sub>x</sub>_|<sup>2</sup>/4 edges. This bound allows us to establish the following inequality.

\(\square\) Claim 4.6. _The following inequality holds:_ \(|\{(a,b)\in V_x\times V_x:C_x(a)=C_b(a)\}|\ge|V_x|^2/4-|V_x|\cdot s_x\).

Proof. Recall that \(s_x=max_{C\in\mathcal{H}_x}|C|\). We first note that the number of (unordered) pairs {_a,b_}, within the same component of **G**_<sub>x</sub>_ is upper bounded by:

\(|\{\{a,b\}\subseteq V_x:a\neq b,C_x(a)=C_x(b)\}|=\sum_{C\in\mathcal{H}_x}\genfrac(){pt}{2}{|C|}{2}=\sum_{C\in\mathcal{H}_x}\genfrac(){pt}{2}{|C|^2}{2}-\frac{|C|}{2}\le(s_x-1)\cdot\sum_{C\in\mathcal{H}_x}\frac{|C|}{2}=s_x\cdot\frac{|V_x|}{2}-\frac{|V_x|}{2}.\)

Let _m<sub>x</sub>_ be the number of edges in **H**_<sub>x</sub>_. By the definition of **H**_<sub>x</sub>_, an edge {_a,b_} is absent if and only if _C<sub>x</sub>(a_)=_C<sub>x</sub>(b_), _C<sub>x</sub>(a_)=_C<sub>b</sub>(a_), or _C<sub>x</sub>(b_)=_C<sub>a</sub>(b_), i.e., if {_a,b_} is in either of these sets:

\(|\{\{a,b\}\subseteq V_x:a\neq b,C_x(a)=C_x(b)\}|\text{or}|\{\{a,b\}\subseteq V_x:C_x(a)=C_b(a)\text{or}C_x(b)=C_a(b)\}|.\)

<sup>11</sup> Mantel’s Theorem states that a triangle-free graph on _n_ vertices has at most _n_<sup>2</sup>/4 edges.

