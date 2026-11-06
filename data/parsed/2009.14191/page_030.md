To show that 3-DSR parameterized by \(\lambda(\mathcal{I})\) is W\[1\]-hard, we give a parameterized reduction from Multicolored Clique, which is W\[1\]-complete \[15, 42\].

The sets _V_<sup>1</sup>_,...,V<sup>k</sup>_ are called _color classes_. Let _E_<sup>_i,j_</sup> be the set of edges with one endpoint in _V<sup>i</sup>_ and one endpoint in _V<sup>j</sup>_. By adding vertices and edges, we may assume without loss of generality that there exists some \(n'\in\mathbb{N}\) such that \(|V^i|=3n'+1\) for all \(i\in[k]\), and that there exists some \(m'\in\mathbb{N}\) such that \(|E^{i,j}|=3m'+1\) for all \(i,j\in[k]\). For each color class _V<sup>i</sup>_, we fix an arbitrary order of the vertices, i.e., \(V^i=\{v_1^i,v_2^i,\dots,v_{3n^\prime+1}^i\}\). Furthermore, for each \(i<j\in[k]\), we fix an arbitrary order of \(E^{i,j}=\{e_1^{i,j},\dots,e_{3m^\prime+1}^{i,j}\}\), and we set \(e_\ell^{j,i}:=e_\ell^{i,j}\). For a vertex \(v\in V(G)\), we denote by \(\delta(v)\) the set of all edges incident to _v_.

As in Section 4.2.2, we only describe the beginning of the preferences of an agent, followed by \(\succ\cdots^{(\text{rest})}\). The remaining acceptable 2-sets can be added in an arbitrary way obeying the strictly ordered master poset (extended to the \(\lambda(\mathcal{I})\) agents not contained in this poset).

The basic idea of the reduction is that we create for every \(i\in[k]\) a vertex-selection gadget _S<sup>i</sup>_ and for every \(i<j\in[k]\) an incidence-checking gadget. The vertex-selection gadget _S<sup>i</sup>_ then encodes the selection of a vertex from _V<sup>i</sup>_ to be part of the multicolored clique, and the incidence- checking gadgets ensure that all vertices selected by the vertex-selection gadgets are indeed incident.

We begin by describing the agents in the MDSR-Poset instance constructed by the reduction, and the master poset. Afterwards, we describe the gadgets used in the reduction.

## 4.3.1 Master poset

Every vertex-selection gadget _S<sup>i</sup>_ has \(3n'+3\) agents, namely \(s^i,\leftarrow\leftarrow s^i\), and every vertex from _V<sup>i</sup>_ will also be an agent in _S<sup>i</sup>_, i.e., _S<sup>i</sup>_ also contains agent \(v_1^i,\dots,v_{3n^\prime+1}^i\). Every incidence-checking gadget _B<sup>i,j</sup>_ contains \(3(3m'+1)+6\) agents: \(b_\ell^{i,j}\) and \(b_\ell^{j,i}\) for \(\ell\in[3m'+1]\), agent \(c_\ell^{i,j}\) for \(\ell\in[3m']\), and agents \(x^{i,j},\leftarrow\leftarrow x^{i,j},x^{j,i},\leftarrow\leftarrow x^{j,i},z_1^{i,j},z_2^{i,j}\), and \(z_3^{i,j}\). Additionally, there are _O(k_<sup>2</sup>) agents contained in so-called "cut-off gadgets" (see Section 4.3.2); however, all these agents will be deleted in order to have the preferences derived from a strictly ordered master poset, and thus, are not considered here. Furthermore, in order to arrive at a strict order as master poset, we delete agents _s<sup>i</sup>_ and \(\leftarrow\leftarrow s^i\) for every \(i\in[k]\) as well as agents _x<sup>i,j</sup>_, \(\leftarrow\leftarrow x^{i,j},x^{j,i},\leftarrow\leftarrow x^{j,i},z_1^{i,j},z_2^{i,j}\), and \(z_3^{i,j}\) for every \(i<j\in[k]\). Inside the vertex-selection gadget _S<sup>i</sup>_, the master poset has the form \(\mathcal{A}^i:=v_1^i\succ_\text{ML}v_2^i\succ_\text{ML}\dots\succ_\text{ML}v_{3n^\prime+1}^i\). Inside incidence-checking gadget _B<sup>i,j</sup>_, the master poset has the form \(\mathcal{B}^{i,j}:=b_1^{i,j}\succ b_1^{j,i}\succ c_1^{i,j}\succ b_e^{i,j}\succ b_2^{j,i}\succ c_2^{i,j}\succ\cdots\succ c_{3m^\prime}^{i,j}\succ b_{3m^\prime+1}^{i,j}\succ b_{3m^\prime+1}^{j,i}\). The complete master poset looks as follows.

\(\mathcal{A}^1\succ_\text{ML}\mathcal{A}^2\succ_\text{ML}\cdots\succ_\text{ML}\mathcal{S}^k\succ_\text{ML}\mathcal{B}^{1,2}\succ_\text{ML}\mathcal{B}^{1,3}\succ_\text{ML}\dots\succ_\text{ML}\mathcal{B}^{1,k}\)<br>
\(\succ_\text{ML}\mathcal{B}^{2,3}\succ_\text{ML}\mathcal{B}^{2,4}\succ_\text{ML}\dots\succ_\text{ML}\mathcal{B}^{2,k}\succ_\text{ML}\mathcal{B}^{3,4}\succ_\text{ML}\dots\succ_\text{ML}\mathcal{B}^{k-1,k}.\)

We continue by describing the gadgets used in the reduction.

## 4.3.2 Cut-off gadget

As in Section 4.2.2, we have a cut-off gadget ensuring for a given agent _a_ and a 2-set _p_ that _a_ is matched to a 2-set it likes at least as much as _p_. Indeed, we use the cut-off gadget<tbc>

