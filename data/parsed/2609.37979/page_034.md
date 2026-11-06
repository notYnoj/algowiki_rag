## 8 More on Weisfeiler-Leman (Advanced Arguments)

The two algorithms from Section 7 highlight a general approach for obtaining algorithms in the Isomorphic-Priors model: if optimal solution values are preserved under WL equivalence (see, e.g., Theorems 7.11 and 7.12), then we obtain efficient algorithms in our model. This strategy is not limited to 1-WL, but also holds for higher-dimensional Weisfeiler-Leman. More precisely, for each \(\ell\ge 1\), the \(\ell\)-dimensional Weisfeiler-Leman (\(\ell\)-WL) algorithm is a heuristic for graph isomorphism testing that accumulates information by coloring \(\ell\)-tuples of vertices. For increasing \(\ell\ge 1\), the algorithm becomes more expressive, but it also becomes computationally more expensive.

In this section, we present a systematic way to use the \(\ell\)-WL algorithm within the Isomorphic- Priors model. After describing the algorithm in Section 8.1, we begin by showing in Section 8.2 that every problem \(\Pi\) that is invariant under \(\ell\)-WL is polynomial time solvable inside the Isomorphic- Priors model (see Theorems 8.3 and 8.4). We then develop a technique that helps us prove when a problem is in fact \(\ell\)-WL invariant.

In Section 8.3 and Section 8.4, we apply this technique to the CSP and CST problems and show that they are 1-WL invariant and 2-WL invariant, respectively. As a result, we obtain fast algorithms for both problems in the Isomorphic-Priors model. Furthermore, additional examples are discussed in Appendix A. However, the Weisfeiler-Leman algorithm has its limits. In Section 8.5, we present an example of a problem that lies in P (and can therefore be efficiently solved in the Isomorphic-Priors model) but that is not \(\ell\)-WL invariant for any constant \(\ell\). This means that Weisfeiler-Leman cannot be used to obtain a fast algorithm for this problem in the Isomorphic-Priors model.

### 8.1 The Weisfeiler-Leman Algorithm

We start with a description of the \(\ell\)-WL algorithm (see, e.g., \[GN21, Kie20b, Kie20a\]). Fix some \(\ell\ge 2\) and let \(G=(V,E,\alpha_V,\alpha_E)\) be an attributed graph. For two colorings \(\chi,\chi':V^\ell\rightarrow\mathcal{C}\), we say \(\chi\) _refines_ \(\chi'\), denoted \(\chi\unknown\chi'\), if \(\chi(\bar{v})=\chi(\bar{w})\) implies \(\chi'(\bar{v})=\chi'(\bar{w})\) for all \(\bar{v},\bar{w}\in V^\ell\). The colorings \(\chi\) and \(\chi'\) are _equivalent_, denoted \(\chi\equiv\chi'\), if \(\chi\unknown\chi'\) and \(\chi'\unknown\chi\).

We define the initial coloring \(\chi_0^{G,\ell}:V^\ell\rightarrow\mathcal{C}\) computed by \(\ell\)-WL as the coloring where each tuple is colored with the isomorphism type of its underlying ordered subgraph. More precisely, for a second attributed graph \(G'=(V',E',\alpha'_V,\alpha'_E)\), and vertices \(v_1,\dots,v_\ell\in V\) and \(v'_1,\dots,v'_\ell\in V'\) we have \(\chi_0^{G,\ell}(v_1,\dots,v_\ell)=\chi_0^{G^\prime,\ell}(v'_1,\dots,v'_\ell)\) if and only if, for all \(i,j\in[\ell]\), we have

• _v<sub>i</sub>=v<sub>j</sub>_ if and only if \(v'_i=v'_j\),<tbc>

• \(\alpha_V(v_i)=\alpha'_V(v'_i)\),<tbc>

• \((v_i,v_j)\in E\) if and only if \((v'_i,v'_j)\in E'\), and<tbc>

• if \((v_i,v_j)\in E\), then \(\alpha_E(v_i,v_j)=\alpha'_E(v'_i,v'_j)\).

<tbc>We then recursively define the coloring \(\chi_i^{G,\ell}\) obtained after _i_ rounds of the algorithm. For \(\bar{v}=(v_1,\dots,v_k)\in V^\ell\), set<tbc>

\(\chi_{i+1}^{G,\ell}(\bar{v}):=\big(\chi_i^{G,\ell}(\bar{v}),\mathcal{M}_i(\bar{v})\big),\)

<tbc>where

\(\mathcal{M}_i(\bar{v}):=\big\{\big(\chi_i^{G,\ell}(\bar{v}[w/1]),\dots,\chi_i^{G,\ell}(\bar{v}[w/\ell])\big)\big|w\in V\big\}\)

and \(\bar{v}[w/i]:=(v_1,\dots,v_{i-1},w,v_{i+1},\dots,v_\ell)\) is the tuple obtained from substituting the _i_-th entry of \(\bar{v}\) with _w_. By definition, \(\chi_{i+1}^{G,\ell}\unknown\chi_i^{G,\ell}\) holds for all \(i\ge 0\). So there is a minimal \(i_\infty\ge 0\) such that \(\chi_{i_\infty}^{G,\ell}\equiv\chi_{i_\infty+1}^{G,\ell}\), and we set \(\chi_\infty^{G,\ell}:=\chi_{i_\infty+1}^{G,\ell}\).

