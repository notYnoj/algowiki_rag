Thus the number of metric points is _N_=|_P_|=_K(m+n_+1).

To define the metric (_P,_d), we construct an undirected weighted graph \(H=(P,F,\mu)\) and let \(\mathsf{d}(\cdot,\cdot)\) be the shortest-path metric of _H_. The edges and weights in _H_ are defined as follows; see Figure 1 for an illustration.

1. For each \(i\in[K]\), if element \(e\in\mathcal{U}_i\) is contained in set \(S\in\mathcal{F}_i\), add an edge (_S,e_) with weight \(\mu(S,e)=1\).<tbc>

2. For each \(i\in[K]\), add an edge (_c<sub>i</sub>,S_) with weight \(\mu(c_i,S)=1\) for every \(S\in\mathcal{F}_i\).<tbc>

3. For any two points \(p\in P_i\) and \(q\in P_j\) with \(i\neq j\), add an edge (_p,q_) with weight \(\mu(p,q)=2\alpha\).

Now run a polynomial-time \((\alpha,2\alpha-\eta)\)-bicriteria approximation algorithm on this metric and let _G_=(_P,E_) be the resulting \(\alpha\)-navigable graph. Among all pairs (_s,j_) with \(s\in P_i\) and \(i,j\in[K]\), \(i\neq j\), choose one that minimizes the number of out-neighbors of _s_ in \(\mathcal{F}_j\cup\mathcal{U}_j\). Denote by \(V_{s,j}=\{p\in\mathcal{F}_j\cup\mathcal{U}_j:(s,p)\in E\}\) the set of these out-neighbors.

**Lemma 3.2.** _The set_ \(V_{s,j}\cap\mathcal{F}_j\) _forms a set cover of_ U_<sub>j</sub>_\\_V<sub>s,j</sub>._

_Proof._ Consider any element \(x\in\mathcal{U}_j\backslash V_{s,j}\). Since _G_ is \(\alpha\)-navigable, there exists an edge \((s,p)\in E\) such that \(\mathsf{d}(p,x)<\mathsf{d}(s,x)/\alpha\). Since _s_ and _x_ belong to different copies, \(\mathsf{d}(s,x)=2\alpha\), and hence d(_p,x)\<_2. All edge weights in _H_ are at least 1, and the only points at distance strictly less than 2 from _x_ are the sets in F_<sub>j</sub>_ that contain _x_. Moreover, \(x\notin V_{s,j}\), so \(p\neq x\). Therefore \(p\in V_{s,j}\cap\mathcal{F}_j\) and _p_ contains _x_.

For every element \(v\in\mathcal{U}_j\cap V_{s,j}\), choose an arbitrary set \(S_v\in\mathcal{F}_j\) containing _v_, which exists because the original Set Cover instance is feasible. Define

\(C=(V_{s,j}\cap\mathcal{F}_j)\cup\{S_v:v\in\mathcal{U}_j\cap V_{s,j}\}.\)

By Lemma 3.2, _C_ is a valid set cover for the _j_-th copy, and therefore for the original instance, with \(|C|\le|V_{s,j}|\).

copy i: {ci} U Ui
copy j: {cj} U Uj
2a
cj
hub
ci
1
1
sets Fi
Si 1
Si 2
Si 3
2a
Si 1
Si 2
Si 3
1
1
elements Ui
ei 1
ei 2
ei 3
ei 4
ei 1
ei 2
ei 3
ei 4
2a
for every p E Pi, q E Pj with i = j: μ(p,q) = 2a

Figure 1: The weighted graph _H_ whose shortest-path metric is (_P,_d) in the lower-bound construction. Each _P<sub>i</sub>_ consists of the hub _c<sub>i</sub>_, the set vertices F_<sub>i</sub>_, and the element vertices U_<sub>i</sub>_. Solid edges have weight 1: hub-to-set edges and set-element incidence edges. Dashed edges indicate that every pair of vertices in two different copies is connected by an edge of weight \(2\alpha\).

