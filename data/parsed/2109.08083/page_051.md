<tbc>\(2\sum c_i^2=\Theta(n^{2.7\times 10^{-5}})\). Hence, taking \(t=n^{1.4\times 10^{-5}}\) we have that<tbc>

\(\mathbb{P}(||Z_{(e^+,e^-)}^A|-\mathbb{E}(|Z_{(e^+,e^-)}^A|)|\ge n^{1.4\times 10^{-5}})\le 2\mathrm{exp}\left(-\Omega(n^{10^{-6}})\right).\)

<tbc>Taking union bounds we have that with high probability

\(|Z_{(e^+,e^-)}^A|=\mathbb{E}(|Z_{(e^+,e^-)}^A|)\pm n^{1.4\times 10^{-5}}=\Theta(p_A^9n^{2.7\times 10^{-5}})\pm n^{1.4\times 10^{-5}}\)

for every pair (_e_<sup>+</sup>_,e_<sup>-</sup>).

Now, suppose that _j\>i_ and consider the affect to \(|Z_{(e_j^+,e_j^-)}^*|\) as a result of the choice for \(z_{(e_i^+,e_i^-)}\). Such a choice forbids only _O_(1) subsequent choices for any feasible pair \((e_j^+,e_j^-)\). There are \(O(p_Ln^{2.6\times 10^{-5}})\) pairs to consider in the running of Algorithm 4.7 and we initially have \(\Theta(p_A^9n^{2.7\times 10^{-5}})\gg p_Ln^{2.6\times 10^{-5}}\) possible configurations for each pair (_e_<sup>+</sup>_,e_<sup>-</sup>). Hence, since each choice forbids only _O_(1) subsequent choices, the algorithm will not abort. □

Now let \(T'\) be a fixed matching covering the vertices of \(A'\) so that \(\bigcup T'\backslash A'\subseteq A\).

Proposition 4.9. _With high probability such a matching_ \(T'\) _exists._

Proof. First note that (by Chernoff bounds), with high probability we have that \(|A'|=\Theta(p_An^{2.7\times 10^{-5}})\). Now for each \(v\in A'\), let _d<sub>A</sub>(v_) be the degree of _v_ in _A_. Then \(\mathbb{E}(d_A(v))=p_A^3d_{I_{n^{10^{-4}}}^\prime}(v)=\Theta(p_A^3n^{10^{-4}})\). Thus by Chernoff and union bounds, with high probability \(d_A(v)=\Theta(p_A^3n^{10^{-4}})\) for every \(v\in A'\). Since \(p_A^3n^{10^{-4}}\gg p_An^{2.7\times 10^{-5}}\) with high probability we may greedily find such a matching \(T'\) for \(A'\), as required. □

We call \(T'\) the \(A'\)_-template_. Before describing how we use \(T'\), we introduce _cascades_, the notion of which comes from \[**32**\].

**4.2.1. Cascades.** Here we describe a general _cascade_ in terms of zero-sum configurations. A cascade is a gadget comprising of zero-sum configurations for a fixed tuple of five edges _e<sub>T</sub>_:=(_e,T_<sub>1</sub>_,T_<sub>2</sub>_,T_<sub>3</sub>_,T_<sub>4</sub>) such that \(e\cap T_i=\{e_i\}\) for every \(i\in[4]\), where _e_=(_e_<sub>1</sub>_,e_<sub>2</sub>_,e_<sub>3</sub>_,e_<sub>4</sub>), and \(|e\cup\bigcup_{i\in[4]}T_i|=16\), so there are no other intersections between edges. Informally, we can think of _T_<sub>1</sub>_,T_<sub>2</sub>_,T_<sub>3</sub>_,T_<sub>4</sub> as edges chosen to cover the vertices of _e_, chosen so that they are disjoint from one another. Then a _cascade_ for _e<sub>T</sub>_, is a collection _C<sub>e<sub>T</sub></sub>_ of zero-sum configurations as follows. Let \(Z'\) be a zero-sum configuration containing _e_ and no other vertices from \(\bigcup_{i\in[4]}T_i\). Let _S<sub>i</sub>_ be the edge of \(Z'\backslash\{e\}\) which intersects _e<sub>i</sub>_ (i.e. the edge in the matching of opposite sign to _e_ which contains _e<sub>i</sub>_). Then for each pair (_S<sub>i</sub>,T<sub>i</sub>_) we also build a zero-sum configuration, _Z<sub>i</sub>_, ensuring that all additional vertices for _Z<sub>i</sub>_ have not already been used. Then our cascade _C<sub>e<sub>T</sub></sub>_ is the graph induced on this collection of zero-sum configurations. As well as considering _C<sub>e<sub>T</sub></sub>_ as a subgraph, we also associate it with the quintuple of zero-sum configurations \(C_{e_T}:=(Z',Z_1,Z_2,Z_3,Z_4)\) which make it. We write C_<sub>e<sub>T</sub></sub>_ for the collection of cascades for _e<sub>T</sub>_. Note that a cascade _C<sub>e<sub>T</sub></sub>_ consists of 64 vertices and induces two distinct perfect matchings each consisting of 16 edges; one which uses edge _e_, and one which uses edges _T_<sub>1</sub>_,T_<sub>2</sub>_,T_<sub>3</sub>_,T_<sub>4</sub>.

