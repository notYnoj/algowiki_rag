## Reduction.

let _G_ be a graph, we define a 3-CNF _f(G_) in the following way:

• For each \(v\in V(G)\) we define variables _v<sub>r</sub>,v<sub>g</sub>,v<sub>b</sub>_. For each edge \(e\in E(G)\), we define variables \(d_e^1,d_e^2,d_e^3\). Thus, _f(G_) has 3(|_V(G_)|+|_E(G_)|) many variables.<tbc>

• For each \(v\in V(G)\), we define the clause \((v_r\vee v_g\vee v_b)\).<tbc>

<tbc>For each \(e=\{u,v\}\in V(G)\) and \(c\in\{r,g,b\}\), we define the clause \((\neg v_c\vee\neg u_c\vee d_e^1)\). Further, we define the clauses<tbc>

<tbc>\((\neg d_e^1\vee d_e^2\vee d_e^3),(\neg d_e^1\vee d_e^2\vee\neg d_e^3),(\neg d_e^1\vee\neg d_e^2\vee d_e^3),(\neg d_e^1\vee\neg d_e^2\vee\neg d_e^3).\)<tbc>

<tbc>Note that theses clauses are constructed in a way that ensures \(d_e^1=0\). This is done to reduce \((\neg v_c\vee\neg u_c\vee d_e^1)\) to \((\neg v_c\vee\neg u_c)\). In total _f(G_) has |_V(G_)|+7|_E(G_)| many clauses.<tbc>

<tbc>Note that _f(G_) is a 3-CNF that is obviously computable in time _O_(|_V(G_)|+|_E(G_)|).

## Correctness.

We show that _G_ is 3-colorable if and only if _f(G_) is solvable.

Let \(\tilde{c}:V(G)\rightarrow\{r,g,b\}\) be a valid 3-coloring of _G_. We use \(\tilde{c}\) to construct a satisfying assignment for _f(g_). We define an assignment **x** via

\(x\mapsto\left\{\begin{array}{ c c }
1 & \text{if}x=v_c\text{for}c\in\{r,g,b\}\text{and}\tilde{c}(v)=c \\
0 & \text{otherwise}
\end{array}\right..\)

Now, let \(e=\{u,v\}\in V(G)\) and assume that **x** does not satisfy \((\neg v_c\vee\neg u_c\neg d_e^1)\). Since \(d_e^1=0\), this is only possible if _v<sub>c</sub>_=1 and _u<sub>c</sub>_=1. However, this would imply that \(\tilde{c}(v)=\tilde{c}(u)\) which is not possible because \(\tilde{c}\) is a proper 3-coloring. Thus, **x** satisfies \((\neg v_c\vee\neg u_c\neg d_e^1)\). Further, it is easy to check that **x** satisfies all other constraints. Hence, _f(g_) is satisfiable.

Next, let **x** be a satisfying assignment for _f(g_). Note that **x** can only satisfy the constraints

\((\neg d_e^1\vee d_e^2\vee d_e^3),(\neg d_e^1\vee d_e^2\vee\neg d_e^3),(\neg d_e^1\vee\neg d_e^2\vee d_e^3),(\neg d_e^1\vee\neg d_e^2\vee\neg d_e^3),\)

by setting \(d_e^1=0\) for each \(e\in E(G)\). We show how to construct a 3-coloring for _G_ using **x**. Due to the constraint \((v_r\vee v_g\vee v_b)\), for each \(v\in V(G)\) there is a \(c\in\{r,g,b\}\) with _v<sub>c</sub>_=1 with respect to **x**. We define \(\tilde{c}(v)=c\) (if _v<sub>c</sub>_=1 is true for multiple \(c\in\{r,g,b\}\) then we choose arbitrarily). We show that \(\tilde{c}\) defines a proper 3-coloring on _V(G_). Assume otherwise, then there is a edge \(e=\{u,v\}\in E(G)\) with \(\tilde{c}(v)=c=\tilde{c}(u)\). However, since \(d_e^1=0\), this would yield that the constraint \((\neg v_c\vee\neg u_c\vee d_e^1)\) is false which is a contradiction. Thus, \(\tilde{c}\) defines a proper 3-coloring.

## Isomorphism preservation.

We show that if _G,H_ are two graphs with \(G\cong H\) then \(f(G)\cong f(H)\).

Let \(\varphi:V(G)\rightarrow V(H)\) be an isomorphisms between _G_ and _H_. For \(v\in V(G)\), we write \(\tilde{v}:=\varphi(v)\). For \(e\in\{u,v\}\), we write \(\tilde{c}:=\{\varphi(u),\varphi(v)\}\in E(H)\). Note that \(v\rightarrow\tilde{v}\) and \(e\rightarrow\tilde{c}\) both define one-to-one mappings between _V(G_) and _V(H_), and between _E(G_) and _E(H_), respectively. We write _V(f(G_)) for the set of variables in _f(G_). Let

\(\psi:V(f(G))\rightarrow V(f(H)),x\mapsto\left\{\begin{array}{ c c }
\tilde{v}_c & \text{if}x=v_c \\
d_\tilde{c}^i & \text{if}x=d_e^i
\end{array}\right..\)

It is now easy to check that \(\psi\) is a isomorphism between _E(G_) and _E(H_).

Thus, _f_ defines a polynomial time many-one reduction from 3-Coloring to 3-SAT is isomorphism- preserving. Hence, 3-Coloring \(\le_p^\cong 3\)-SAT.

