<tbc>tical for realistically sized PPI networks. Consequently, the main aim of the existing works \[1, 15, 25\] has been to design efficient and effective _heuristics_ that identify high-quality motif pairs in reasonable time. This need is particularly acute for modern real-world datasets, which are large, noisy, and in need of methods that scale while still capturing biologically meaningful patterns.

Here, however, we present an _exact_ method that remains efficient in practice on modern datasets, thereby showing that the problem can be solved far more effectively than is commonly believed. Our results thus refute the prevailing view that only heuristic approaches are viable for this task. Our crucial observation is that the hardness proof in \[1\] proceeds under the assumption that both \(\ell\) and _d_ are unbounded, which is not realistic in the motivating application. Intuitively, we confine the computational hardness to _parameter_ \(\ell\). Indeed, the values considered for \(\ell\) and _d_ are typically small \[1, 15, 25\].

We make the following theoretical contributions:

(1) We give an _exact_ O(_N_<sup>2</sup>)-time algorithm for CMM (the vanilla version), where \(N:=\sum_{v\in V}|v|\). The space usage is O(_N_). See Section 3.<tbc>

(2) We show that this algorithm is essentially _optimal_: no algorithm can solve CMM in time \(\mathcal{O}(N^{2-\varepsilon}\mathrm{poly}(|E|,|V|))\), for any \(\varepsilon>0\), unless the popular Strong Exponential-Time Hypothesis (SETH) \[9\] is false. See Section 3.<tbc>

(3) We build on the CMM algorithm to give an _exact_ \(\mathcal{O}\left(\genfrac(){pt}{2}{\ell}{d}^2N^2\right)\)-time algorithm for \((\ell,d)\)-CMM (the wildcards version). The space usage is O(_N_); and the algorithm is embarrassingly parallelizable. This improves dramatically on the state of the art from \(\mathcal{O}^*\left(\genfrac(){pt}{2}{\ell}{d}^2|\Sigma|^{2(\ell-d)}\right)\) time to \(\mathcal{O}^*\left(\genfrac(){pt}{2}{\ell}{d}^2\right)\) and from \(\mathcal{O}^*\left(\genfrac(){pt}{2}{\ell}{d}^2|\Sigma|^{2(\ell-d)}\right)\) space to O(_N_).<sup>1</sup> See Section 4.<tbc>

(4) Finally, we observe that \((\ell,d)\)-CMM is W\[1\]-hard parameterized by _d_. See Section 4.

We make the following practical contributions:

(1) We show that the parallelized version of our algorithm for \((\ell,d)\)-CMM processes real-world datasets in a reasonable amount of time.<tbc>

(2) We show that the runtime and space usage predicted by our theoretical results are accurately reflected in practice.<tbc>

(3) We show that our exact algorithm finds motif pairs with significantly higher support than the state of the art, which highlights its usefulness.<tbc>

(4) We show that our exact algorithm finds many top- scoring motif pairs that the state of the art misses.<tbc>

<tbc>For the above practical contributions, see Section 5. We begin with some preliminaries in Section 2.

## 2 Preliminaries.

We assume throughout that arrays and strings start at position 1.

### 2.1 Strings.

A _string_ is a finite sequence of characters over an alphabet \(\Sigma\). In this work, we consider strings over a totally ordered alphabet. We denote the length of a string _T_ by |_T_|. For any index \(i\in[1,|T|]\), we denote the _i_-th character of _T_ by _T_\[_i_\]. A string of the form \(T[i..j]=T[i]T[i+1]\cdots T[j]\), where \(1\le i\le j\le|T|\), is called a _fragment_ of _T_. If _T_ is known, we can encode _T_\[_i..j_\] in O(1) space as the pair (_i,j_). A fragment of the form _T_\[1_..j_\] is called a _prefix_ of _T_, and a fragment of the form _T_\[_i.._|_T_\] is called a _suffix_ of _T_. A string _P_ is a _substring_ of _T_ if _P=T_\[_i..i_+|_P_|-1\], for some _i_. In this case, we say that _P occurs_ in _T_. A _wildcard_ is a special symbol \(\diamond\) matching any \(a\in\Sigma\sqcup\{\diamond\}\).

Given a string _T_ of length _n_, the _suffix array_ of _T_, denoted by SA_<sub>T</sub>_\[1_..n_\], stores a permutation of the indices {1_,...,n_} such that _T_\[SA_<sub>T</sub>_\[_i\..n_\] is the _i_-th lexicographically smallest suffix of _T_. Let lcp(_X,Y_) denote the length of the _longest common prefix_ (LCP) of the strings _X_ and _Y_ . The _LCP array_ of _T_, denoted by LCP_<sub>T</sub>_\[1_..n_\], is defined as follows: LCP_<sub>T</sub>_\[1\]=0, and for every \(i\in[2,n]\), \(\text{LCP}_T[i]=\mathrm{lcp}\left(T[\text{SA}_T[i-1]\dots n],T[\text{SA}_T[i]\dots n]\right)\).

### 2.2 Graphs and motifs.

Let _G_=(_V,E_) be an undirected graph, where \(V\subseteq\Sigma^*\), for an alphabet \(\Sigma\). Let \(N:=\sum_{v\in V}|v|\) denote the total length of all \(v\in V\) . An \((\ell,d)\)_-motif_ is a string \(X\in(\Sigma\sqcup\{\diamond\})^\ell\) containing exactly _d_ wildcard symbols \(\diamond\). When _d_=0, the motif is simply a string over \(\Sigma\) of length \(\ell\). An \((\ell,d)\)_-motif pair_ {_X,Y_} is an unordered pair of \((\ell,d)\)-motifs. We may omit \(\ell\) and _d_ when they are clear from the context and then simply speak of motifs and motif pairs.

### 2.3 Motif-induced subgraphs.

For a motif _X_, let \(V_X:=\{v\in V|X\text{occurs in}v\}\) be the set of nodes where _X_ occurs. If a node _v_ contains multiple occurrences of _X_, then _v_ is included only once in _V<sub>X</sub>_.

For a motif pair {_X,Y_}, the set of edges whose endpoints contain _X_ and _Y_ , respectively, is

\(E_{X,Y}:=\{\{u,v\}\in E|u\in V_X\text{and}v\in V_Y\}.\)

We set _f<sub>E</sub>(G,{X,Y_}):=|_E<sub>X,Y</sub>_|. The subgraph _selected_ by {_X,Y_} is then \(G_{X,Y}:=(V_X\cup V_Y,E_{X,Y})\). If \(V_X\cap V_Y\) is nonempty, we may have an edge between distinct nodes \(v,u\in V_X\) provided that at least one of them is in \(V_X\cap V_Y\). On the other hand, if \(v,u\in V_X\backslash V_Y\), they cannot be adjacent by definition of _E<sub>X,Y</sub>_.

A motif pair {_X,Y_} is called a (_k<sub>X</sub>,k<sub>Y</sub>,k<sub>X,Y</sub>)-motif pair_ for _G_ if _G<sub>X,Y</sub>_ satisfies |_V<sub>X</sub>_|=_k<sub>X</sub>_, |_V<sub>Y</sub>_|=_k<sub>Y</sub>_, and<tbc>

<sup>1</sup>The \(\mathcal{O}^*(\cdot)\) notation suppresses polynomial factors.

