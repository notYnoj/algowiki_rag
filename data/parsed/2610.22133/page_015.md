Note that these two sets are indeed disjoint: if _C<sub>x</sub>(a_)=_C<sub>x</sub>(b_), then \(b\in C_x(a)\). In this case, _C<sub>x</sub>(a_) cannot be a component in **G**_<sub>b</sub>_ because the vertex _b_ itself is removed. Similar holds for _C<sub>x</sub>(b_) in **G**_<sub>a</sub>_. This allows us to lower bound _m<sub>x</sub>_ through the number of non-edges as:

\(m_x=\genfrac(){pt}{2}{|V_x|}{2}-|\{\{a,b\}\subseteq V_x:a\neq b,C_x(a)=C_x(b)\}|-|\{\{a,b\}\subseteq V_x:C_x(a)=C_b(a)\text{or}C_x(b)=C_a(b)\}|\)<br> \(\ge\frac{|V_x|^2}{2}-\frac{|V_x|}{2}-s_x\cdot\frac{|V_x|}{2}+\frac{|V_x|}{2}-|\{\{a,b\}\subseteq V_x:C_x(a)=C_b(a)\text{or}C_x(b)=C_a(b)\}|.\)

Simplifying the latter inequality, combining it with \(m_x\le|V_x|^2/4\), and rearranging, yields that \(|\{\{a,b\}\subseteq V_x:C_x(a)=C_b(a)\text{or}C_x(b)=C_a(b)\}|\ge|V_x|^2/4-s_x|V_x|\). The claim follows by noticing that in \(|\{(a,b)\in V_x\times V_x:C_x(a)=C_b(a)\}|\) each element {_a,b_} of the latter set is counted at least once as (_a,b_) or (_b,a_). \(\triangleleft\)

Finally, we establish the lower bound for \(|\{(y,C)\in V_x\times\mathcal{H}_x:C\in\mathcal{H}_y\}|\). For any pair \((a,b)\in V_x\times V_x\) such that _C<sub>x</sub>(a_)=_C<sub>b</sub>(a_), the pair (_b,C<sub>x</sub>(a_)) is a valid entry in the set \(\{(y,C)\in V_x\times\mathcal{H}_x:C\in\mathcal{H}_y\}\). However, multiple vertices _a_ can belong to the same component _C=C<sub>x</sub>(a_). Specifically, for a fixed _b_ and _C_, there are exactly |_C_| vertices _a_ such that _C<sub>x</sub>(a_)=_C_. Since \(|C|\le s_x\) for all \(C\in\mathcal{H}_x\), each pair (_b,C_) is counted at most _s<sub>x</sub>_ times in the set of pairs (_a,b_). Therefore, we have:

\(|\{(y,C)\in V_x\times\mathcal{H}_x:C\in\mathcal{H}_y\}|\ge|\{(a,b)\in V_x\times V_x:C_x(a)=C_b(a)\}|/s_x\ge|V_x|^2/(4s_x)-|V_x|.\)

This brings us to our main structural result for AT-free graphs.

**Theorem 4.7.** _Let_ **G**=(_V,E_) _be an AT-free graph. Moreover, let_ **G**_<sub>x</sub>_:=**G**[_V_\\_N[x_]]_, and let_ \(\mathcal{C}_x=\{C_x(v)\}_{v\in\mathbf{G}_x}\) _be the set of all connected components of_ **G**_<sub>x</sub>. Then there are at most_ O(_n_log_n_) _distinct components across all_ **G**_<sub>x</sub>; that is,_ \(|\mathcal{C}|\le 400n\mathrm{log}n\) _for_ \(\mathcal{C}:=\bigcup_{x\in V}\mathcal{C}_x\).

**Proof.** Let \(\mathcal{C}:=\bigcup_{x\in V}\mathcal{C}_x\). We begin by partitioning C in O(log<sup>2</sup>_n_) sets, depending on the size of \(C\in\mathcal{C}\) and in how many C_<sub>x</sub>_ a component _C_ appears. More precisely, for \(i,j\in[0..\lceil\mathrm{log}n\rceil]\), we set<tbc>

\(\mathcal{C}^{i,j}:=\{C\in\mathcal{C}:2^i\le|C|<2^{i+1},2^j\le|\{x:C\in\mathcal{C}_x\}|<2^{j+1}\}\text{and}\mathcal{C}_x^{i,j}:=\{C\in\mathcal{C}^{i,j}:C\in\mathcal{C}_x\}\text{for}x\in V.\)

<tbc>Moreover, we introduce the auxiliary bipartite graph **F**_<sup>i,j</sup>_ with vertices \(V\cup\mathcal{C}^{i,j}\) and an edge (_x,C_) if \(C\in\mathcal{C}_x\). That is, \(\mathcal{C}_x^{i,j}\) is the neighborhood of _x_ in **F**_<sup>i,j</sup>_. The graph **F**_<sup>i,j</sup>_ helps us to bound |C<sup>_i,j_</sup>| as follows.

\(\square\) Claim 4.8. _For every_ \(i,j\in[0..\lceil\mathrm{log}n\rceil]\)_, such that_ \(\mathcal{C}^{i,j}\neq\emptyset\)_, we have_ \(|\mathcal{C}^{i,j}|\le(2^{-i+6}+2^{-j+5})\cdot n\).

Proof. Fix such _i,j_, and let deg(_x_) and deg(_C_) denote the degree of _x_ and _C_ in **F**_<sup>i,j</sup>_, respectively.

For every \(x\in V\) , let \(V_x:=\bigcup_{C\in\mathcal{C}_x^{i,j}}C\) and \(D_x:=|\{(y,C)\in V_x\times\mathcal{C}_x^{i,j}:C\in\mathcal{C}_y^{i,j}\}|\). If deg(_x)\>_0, we apply Lemma 4.4 to **G** with H=C_<sup>i,j</sup>_ and obtain<tbc>

\(D_x\ge|V_x|^2/(4s_x)-|V_x|\text{, where}s_x:=\mathrm{max}_{C\in\mathcal{C}_x^{i,j}}|C|.\)

<tbc>The number _D<sub>x</sub>_ counts a subset of the walks of length two from vertex _x_ to some vertex _y_ through a component \(C\in\mathcal{C}_x^{i,j}\cap\mathcal{C}_y^{i,j}\) in the graph **F**_<sup>i,j</sup>_. Since every \(C\in\mathcal{C}_x^{i,j}\) satisfies \(2^i\le|C|<2^{i+1}\), for deg(_x)\>_0 we have:

\(D_x\ge|V_x|^2/(4s_x)-|V_x|\ge(\mathrm{deg}(x)\cdot 2^i)^2/(4\cdot 2^{i+1})-\mathrm{deg}(x)\cdot 2^{i+1}=\mathrm{deg}(x)^2\cdot 2^{i-3}-\mathrm{deg}(x)\cdot 2^{i+1}.\) (2)

