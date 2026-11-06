the definition of inverse edges, we have \(\mathrm{Inv}(G',\mathbf{w}',e)=\mathrm{Inv}(G,\mathbf{w},e)\backslash B'\) for each _e_. Consequently, there is an edge between _e_<sub>1</sub> and _e_<sub>2</sub> in \(H_{G^\prime,\mathbf{w}^\prime}\) if and only if \(\mathrm{Inv}(G,\mathbf{w},e_1)\cap\mathrm{Inv}(G,\mathbf{w},e_2)\unknown\subseteq B'\). Let \(E':=E(T)\backslash(F'\cup R)\) and let _I_ be the maximum-weight independent set in \(H_{G^\prime,\mathbf{w}^\prime}[E']\). We aim to show that \(S:=I\sqcup R\) satisfies all the required properties and maximizes the profit.

First, by construction of _S_, it holds that \(F'\cap S=\emptyset\) and \(R\subseteq S\). Suppose that for some distinct \(s_1,s_2\in S\), we have \(\mathrm{Inv}(G,\mathbf{w},s_1)\cap\mathrm{Inv}(G,\mathbf{w},s_2)\unknown\subseteq B'\). Then there is an edge in \(H_{G^\prime,\mathbf{w}^\prime}\) between _s_<sub>1</sub> and _s_<sub>2</sub>. Since _I_ is an independent set in \(H_{G^\prime,\mathbf{w}^\prime}\), it cannot contain both _s_<sub>1</sub> and _s_<sub>2</sub>. Without loss of generality, assume that \(e_1\notin I\) and thus \(e_1\in R\). By the definition of \(F'\), from \(e_1\in R\) and \(\mathrm{Inv}(G,\mathbf{w},e_1)\cap\mathrm{Inv}(G,\mathbf{w},e_2)\unknown\subseteq B'\) it follows that \(e_2\in F'\), which is a contradiction because \(S\cap F'=\emptyset\). Therefore, _S_ satisfies all three constraints.

Next, we establish a connection between **p**(_G,_**w**_,S_) and the weight of _I_ in \(H_{G^\prime,\mathbf{w}^\prime}[E']\). By definition, we have **p**(_G,_**w**_,S_)=**w**(Inv(_G,_**w**_,S_))-**w**(_S_). We express Inv(_G,_**w**_,S_) as \(\mathrm{Inv}(G,\mathbf{w},R)\sqcup(\mathrm{Inv}(G,\mathbf{w},I)\backslash\mathrm{Inv}(G,\mathbf{w},R))\) and _S_ as \(R\sqcup I\). Then we have<tbc>

\(\mathbf{p}(G,\mathbf{w},S)=(\mathbf{w}(\mathrm{Inv}(G,\mathbf{w},R))-\mathbf{w}(R))+(\mathbf{w}(\mathrm{Inv}(G,\mathbf{w},I)\backslash\mathrm{Inv}(G,\mathbf{w},R))-\mathbf{w}(I))\)

<tbc>Since \(I\cap F'=\emptyset\), Inv(_G,_**w**_,e_) and Inv(_G,_**w**_,r_) with \(e\in I\) and \(r\in R\) can intersect only by the elements of \(B'\). Therefore, Inv(_G,_**w**_,I_)\\Inv(_G,_**w**_,R_)=Inv(_G,_**w**_,I_)\\\(B'=\mathrm{Inv}(G',\mathbf{w}',I)\). Plugging this into the equation above, we obtain **p**(_G,_**w**_,S_)=**p**(_G,_**w**_,R_)+**p**(\(G',\mathbf{w}',I\)). Moreover, since _I_ is an independent set in \(H_{G^\prime,\mathbf{w}^\prime}\), its elements do not share inverse edges in \(G'\). Thus, by the third point of Observation 4, we have

\(\mathbf{p}(G,\mathbf{w},S)=\mathbf{p}(G,\mathbf{w},R)+\sum_{e\in I}\mathbf{p}(G',\mathbf{w}',e)\)

Notice that sum of profits in \(G'\) over all elements of _I_ is exactly the weight of _I_ in \(H_{G^\prime,\mathbf{w}^\prime}[E']\).

Now, assume that there is another set \(S'\subseteq E(T)\) that satisfies all the required constraints, and has a larger profit in _G_ than _S_. We know that \(S'\cap F'=\emptyset\) and \(R\subseteq S'\). Let \(I':=S'\backslash R\). Observe that \(I'\subseteq E'\). The third constraint guarantees that for each distinct \(e_1,e_2\in I'\), we have \((\mathrm{Inv}(G,\mathbf{w},e_1)\cap\mathrm{Inv}(G,\mathbf{w},e_2))\subseteq B'\). Consequently, \(I'\) is an independent set in \(H_{G^\prime,\mathbf{w}^\prime}[E']\). Then for analogous reasons we have that<tbc>

\(\mathbf{p}(G,\mathbf{w},S')=\mathbf{p}(G,\mathbf{w},R)+\sum_{e\in I^\prime}\mathbf{p}(G',\mathbf{w}',e)\)

<tbc>Combining this with \(\mathbf{p}(G,\mathbf{w},S')>\mathbf{p}(G,\mathbf{w},S)\), we obtain that

\(\sum_{e\in I^\prime}\mathbf{p}(G',\mathbf{w}',e)>\sum_{e\in I}\mathbf{p}(G',\mathbf{w}',e)\)

In other words, the weight of \(I'\) in \(H_{G^\prime,\mathbf{w}^\prime}[E']\) exceeds the weight of _I_, contradicting the maximality of _I_. Therefore, _S_ maximizes the profit.

Since \(H_{G^\prime,\mathbf{w}^\prime}\) is a perfect graph by Lemma 6, its induced subgraph \(H_{G^\prime,\mathbf{w}^\prime}[E']\) is also perfect. Therefore, by Proposition 4, the set _I_ (and hence _S_) can be found in polynomial time.

Observe that no single triple \((F,R,B')\) allows _S_ to have an arbitrary structure. Intuitively, if \(B'\) is small, we forbid the elements of _S_ from having strongly overlapping sets of inverse edges. Conversely, if \(B'\) is large, then each of its elements has a corresponding edge in \(R\subseteq S\), and hence any feasible _S_ must be fairly large as well. Therefore, this lemma alone is not sufficient to solve even instances with \(A=\emptyset\). The following result completes the picture.

