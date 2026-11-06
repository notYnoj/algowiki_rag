Claim 13, it has a solution _X_ with _S=E(T_)\\_E(X_) and _D_=Inv(_G,_**w**_,S_)\\_E(X_) such that \(\mathbf{w}(D)\le\mathbf{w}(A)\). Let \(G'=G-D\), and let \(\mathbf{w}'\) be the restriction of **w** to \(E(G')\). By the definition of _D_, it holds that \(E(X)\cap D=\emptyset\), and hence _X_ is a subgraph of \(G'\).

Since \(D\subseteq B\), we have \(\mathrm{MaxST}(G',\mathbf{w}')=T\). Because allowed, blocked, and inverse edges are defined based on the maximum spanning tree, it follows that \(A(G',\mathbf{w}')=A(G,\mathbf{w})\), \(B(G',\mathbf{w}')=B(G,\mathbf{w})\backslash D\), and \(\mathrm{Inv}(G',\mathbf{w}',e)=\mathrm{Inv}(G,\mathbf{w},e)\backslash D\) for each \(e\in E(T)\). We claim that _X_ is an Inv-respecting subgraph in \(G'\). Since _X_ is a solution to I, it is acyclic. By applying Observation 2 to the graph \(G'\), we know that _X_ can contain blocked edges only from the set \(\mathrm{Inv}(G',\mathbf{w}',S)=\mathrm{Inv}(G,\mathbf{w},S)\backslash D\). Additionally, by the definition of _D_, we have Inv(_G,_**w**_,S_)\\_E(X_)=_D_, which implies \(\mathrm{Inv}(G',\mathbf{w}',S)\subseteq E(X)\). Therefore, \(X=T-S+\mathrm{Inv}(G',\mathbf{w}',S)+A'\) for some \(A'\subseteq A\). Note that _X_ is also a solution to \(\mathcal{I}'=(G',\mathbf{w}',k)\). Consequently, \(\mathcal{I}'\) is an Inv-respecting instance.

Lemma 10 provides a family of constraint sets \(\{\mathcal{C}_{A^\prime}|A'\subseteq A\}\) for the instance \(\mathcal{I}'\). Moreover, there exist \(S'\subseteq E(T)\) and \(A'\subseteq A\) such that \(X'=T-S'+\mathrm{Inv}(G',\mathbf{w}',S')+A'\) is a solution to \(\mathcal{I}'\) that satisfies the constraint set \(\mathcal{C}_{A^\prime}\). Let \((F,R,B')\in\mathcal{C}_{A^\prime}\) be the satisfied constraint triple. By definition, we have \(B'\subseteq B(G',\mathbf{w}')=B(G,\mathbf{w})\backslash D\). Additionally, the lemma guarantees that \(\mathbf{w}(B')\le(\mathbf{w}(A)+k)^2\), and each of the sets _F_ and _R_ equals the union of at most 4(**w**(_A_)+_k_+1)<sup>4</sup> directed paths in _T_. Let _P<sub>F</sub>_ and _P<sub>R</sub>_ be the sets of endpoints of such paths for _F_ and _R_, respectively.

From the definition of _D_, \(B'\), _P<sub>F</sub>_, and _P<sub>R</sub>_, it follows that our algorithm must have considered these sets. Moreover, given _P<sub>F</sub>_ and _P<sub>R</sub>_, it constructed exactly the sets _F_ and _R_. Since \((F,R,B')\) is a restriction triple, we have \(B'\subseteq\mathrm{Inv}(G',\mathbf{w}',R)\). Hence, our algorithm applied Lemma 7 to \((G',\mathbf{w}')\) and constraints \((F,R,B')\) and obtained a set \(S''\). Since \(S'\) is also feasible under these constraints and \(S''\) has a maximum profit, we have \(\mathbf{p}(G',\mathbf{w}',S'')\ge\mathbf{p}(G',\mathbf{w}',S')\).

Consider the subgraph \(X''=T-S''+\mathrm{Inv}(G',\mathbf{w}',S'')+A'\). Since \(S''\) is feasible under the constraints given by \((F,R,B')\), \(X''\) satisfies this restriction triple, and therefore it also satisfies \(\mathcal{C}_{A^\prime}\). Hence, Lemma 10 guarantees that \(X''\) is acyclic. Note that

\(\mathbf{w}(X'')=\mathbf{w}(T)+\mathbf{p}(G',\mathbf{w}',S'')+\mathbf{w}(A')\ge\mathbf{w}(T)+\mathbf{p}(G',\mathbf{w}',S')+\mathbf{w}(A')=\mathbf{w}(X')\)

Since \(X'\) is a solution to \(\mathcal{I}'\), we have \(\mathbf{w}(X')\ge\mathbf{w}(T)+k\), and therefore \(\mathbf{w}(X'')\ge\mathbf{w}(T)+k\). Consequently, \(X''\) is a solution to I, which is found by our algorithm.

## 6 Conclusion

We conclude with several open questions and directions for further research. First of all, the parameterized complexity of MAS/MaxST remains unsettled, when we deal with rational weights.

**Open Question 1.** _Is_ \(\mathrm{MAS}/\mathrm{MaxST}(\mathbb{Q}_{\ge 1})\mathsf{W}[1]\)_-hard or fixed-parameter tractable?_

Another standalone question concerns Lemma 2, and it might be of independent interest. Lemma 2 in fact shows that a solution of weight at least \(\mathbf{w}(T)+\lceil\mathbf{w}(A)/3\rceil\) is guaranteed for integer weights and can be found in polynomial time, using known constructions of linear orderings for oriented trees. Can we improve the denominator 3 in this guarantee using more specific constructions? If yes, can we find the required subset of allowed edges in polynomial time? If no, is there a no-instance with integer weights and **w**(_A_)=3_k_-3?

**Open Question 2.** _Can the constant_ 3 _in Lemma 2 be improved?_

