• _T<sub>i</sub>_ contains all \(\alpha\)-vertices: let us fix \(S=N(C(b,\Omega))\). If _S_ contains every vertex of _M_, then again _S_ is a minimal (_a,b_)-separator extending _M_. Assume by way of contradiction that it is not the case. Component \(C(b,\Omega)\) is adjacent to all vertices in \(\{a_i,b_i\}_{1\le i\le n}\). So, \(C(b,\Omega)\) is not adjacent to some clause vertex _C<sub>j</sub>_. Then, in the gadget where |_T<sub>i</sub>_|=3, since we added an \(\alpha\)-vertex, vertex _b<sub>i</sub>_ is not adjacent to \(C(a,\Omega)\). Finally, as _C<sub>j</sub>_ is not adjacent to \(C(b,\Omega)\) and \((b_i,C_j)\notin E(G(\Phi))\), then (_b<sub>i</sub>,C<sub>j</sub>_) is a conflict pair for \(\Omega\), which yields a contradiction.

In brief, the existence of a PMC \(\Omega\) extending _M_ and avoiding {_a,b_} allows us to identify a minimal (_a,b_)-separator extending _M_ in \(G(\Phi)\).

The hardness of PMC Extension thus comes naturally.

**Theorem 3.** PMC Extension _is NP-complete._

_Proof._ By Theorem 12, it is NP-hard to find a minimal (_a,b_)-separator extending _M_ in graphs \(G(\Phi)\). By Lemma 23, finding such a separator is equivalent to solving PMC Extension on graphs \(G(\Phi)\) with _M_ fixed as in subsection 5.1 and _F_={_a,b_}.

## 5.3 NP-hardness of PMC subset

In this subsection, we provide a more refined hardness result regarding PMC Extension. We prove that PMC Extension is NP-hard, even restricted to \(F=\emptyset\). This subproblem is called PMC Subset and defined below.

PMC Subset<br>
**Input:** A graph _G_=(_V,E_), a set \(M\subseteq V\) of _mandatory_ vertices.<br>
**Question:** Is there a PMC \(\Omega\) of _G_ satisfying \(M\subseteq\Omega\)?

The avoidance of set _F_={_a,b_}, used as an essential argument in the previous subsection, can in fact, with additional effort, be withdrawn to draw the equivalence between PMCs and minimal (_a,b_)-separators extending _M_.

**Theorem 13.** _In_ \(G(\Phi)\)_, there is no PMC_ \(\Omega\) _extending M containing both a and b. Moreover, if a or b belongs to_ \(\Omega\)_, then_ \(\Omega\) _contains a minimal_ (_a,b)-separator extending M._

_Proof._ We assume that formula \(\Phi\) is non trivial and contains at least one clause and two variables, hence \(G(\Phi)\) admits at least one clause vertex and two variable gadgets. In this setting, if both _a_ and _b_ belong to \(\Omega\), then, any mandatory vertex _a<sub>i</sub>_ (or _b<sub>i</sub>_) can only reach an _a<sub>p</sub>_ (or _b<sub>p</sub>_), \(p\neq i\), by either _a_, _b_ or a clause vertex. Since they all are in \(\Omega\), it follows that \(\Omega\) is not a PMC: the reachability property is not satisfied. Then both _a_ and _b_ cannot belong to the same PMC.

Let us suppose now that exactly one vertex among _a_ or _b_ belongs to \(\Omega\). Starting from set \(Y=M\cup\{a\}\) or \(Y=M\cup\{b\}\), graph \(G(\Phi)\backslash Y\) contains a component full for _Y_ . It is thus necessary to add vertices from variable gadgets if we want to obtain a PMC \(\Omega\) fulfilling \(Y\unknown\Omega\). Our objective is to show that _a_ and _b_ cannot see each other despite \(\Omega\), formally \(a\notin R_G^+(b,\Omega)\).

We assume w.l.o.g. that \(b\in\Omega\): the same symmetric reasoning works for case \(a\in\Omega\). Then, \(S=N(C(a,\Omega)\) is a minimal separator of _G_. Assume by contradiction that \(b\in S\) and let us denote by \(v\in\Omega\) a vertex separated from _a_ by _S_. From Lemma 2, there exists an<tbc>

