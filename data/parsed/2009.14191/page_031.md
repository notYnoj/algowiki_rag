from Section 4.2.2. Since we will use only _O(k_<sup>2</sup>) many cut-off gadgets, adding these agents may increase the deletion distance to a strict master poset by at most _O(k_<sup>2</sup>); thus, we can choose the preferences arbitrarily and do not have to consider the master poset.

We already showed in Lemma 4.7 that cut-off gadgets work as desired. Having described the cut-off gadgets, we can now describe the remaining gadgets, namely the vertex-selection gadget and the incidence-checking gadget. We start with the vertex-selection gadget.

## 4.3.3 Vertex-selection gadget

For each color class _V<sup>i</sup>_, the reduction adds a vertex selection gadget _S<sup>i</sup>_. This vertex-selection gadget contains an agent for each vertex \(v_p^i\) with \(p\in[3n'+1]\); we identify the agent and the vertex and call both \(v_p^i\). Furthermore, the vertex-selection gadget contains two agents _s<sup>i</sup>_ and \(\overleftarrow{s}^i\). The vertex-selection gadget also contains a cut-off gadget for each of the three agents _s<sup>i</sup>_, \(\overleftarrow{s}^i\), and \(v_{3n^\prime+1}^i\).

The intuitive idea behind the vertex-selection gadget is as follows. Selecting a vertex \(v_\ell^i\) to be part of a multicolored clique corresponds to matching this vertex to \(\{s^i,\overleftarrow{s}^i\}\), and partitioning the remaining agents from \(\{v_1^i,\dots,v_{3n^\prime+1}^i\}\backslash\{v_\ell^i\}\) into \(n'\) 3-sets which are contained in the stable matching. Since _s<sup>i</sup>_ prefers being matched to \(\{\overleftarrow{s}^i,v_\ell^i\}\) with small \(\ell\) while \(\overleftarrow{s}^i\) prefers being matched to \(\{s^i,v_\ell^i\}\) with large \(\ell\), how much _s<sup>i</sup>_ and \(\overleftarrow{s}^i\) like their partners in a matching encodes which vertex is selected. The cut-off gadget for \(v_{3n^\prime+1}^i\) actually implies that in every stable matching _M_, there has to exist some \(\ell\in[3n'+1]\) such that \(\{v_\ell^i,s^i,\overleftarrow{s}^i\}\in M\) (see Lemma 4.23). This implies that every vertex has to be matched this way, and thus, the vertex-selection gadget has to select a vertex in each stable matching.

The preferences of an agent \(v_p^i\in V^i\) start with all 2-sets containing an agent from a vertex- selection gadget _S<sup>j</sup>_ with _j\<i_, and continue with \(\{s^i,\overleftarrow{s}^i\}\succ\left\{\{v_1^i,v_q^i\}:q\in[3n'+1]\right\}\succ\left\{\{v_2^i,v_q^i\}:q\in[3n'+1]\right\}\succ\cdots\succ\left\{\{v_{3n^\prime+1}^i,v_q^i\}:q\in[3n'+1]\right\}\succ\dots\right.\)

For the agent \(v_{3n^\prime+1}^i\), a cut-off gadget follows; for the other agents, the preferences are extended in an arbitrary way obeying the master poset.

The preferences of _s<sup>i</sup>_ and \(\overleftarrow{s}^i\) are as follows (the agents _x<sup>i,j</sup>_, \(\overleftarrow{x}^{i,j}\), and \(b_\ell^{i,j}\) are contained in incidence-checking gadgets (see Section 4.3.4)).

\(s^i:\{\overleftarrow{s}^i,v_1^i\}\succ\left\{\{b_\ell^{i,j},\overleftarrow{x}^{i,j}\}:j\in[k]\backslash\{i\},e_\ell^{i,j}\in E^{i,j}\cap\delta(v_1^i)\right\}\succ\{\overleftarrow{s}^i,v_2^i\}\)<br>
\(\succ\left\{\{b_\ell^{i,j},\overleftarrow{x}^{i,j}\}:j\in[k]\backslash\{i\},e_\ell^{i,j}\in E^{i,j}\cap\delta(v_2^i)\right\}\succ\{\overleftarrow{s}^i,v_3^i\}\succ\cdots\succ\left\{\overleftarrow{s}^i,v_{3n^\prime+1}^i\right\}\succ\mathrm{CO}_{s_i}\)<br>
\(\overleftarrow{s}^i:\{s^i,v_{3n^\prime+1}^i\}\succ\left\{\{b_\ell^{i,j},x^{i,j}\}:j\in[k]\backslash\{i\},e_\ell^{i,j}\in E^{i,j}\cap\delta(v_{3n^\prime+1}^i)\right\}\succ\{s^i,v_{3n^\prime}^i\},\)<br>
\(\succ\left\{\{b_\ell^{i,j},x^{i,j}\}:j\in[k]\backslash\{i\},e_\ell^{i,j}\in E^{i,j}\cap\delta(v_{3n^\prime}^i)\right\}\succ\{s^i,v_{3n^\prime-1}^i\}\succ\cdots\succ\{s^i,v_1^i\}\succ\mathrm{CO}_\overleftarrow{s}_i.\)

Next, we turn to the incidence-selection gadget.

## 4.3.4 Incidence-checking gadget

For each pair (_V<sup>i</sup>,V<sup>j</sup>_) of color classes with _i\<j_, we add an incidence-checking gadget _B<sup>i,j</sup>_. For each edge \(\ell\in[3m'+1]\), the incidence-checking gadget _B<sup>i,j</sup>_ contains two agents \(b_\ell^{i,j}\) and \(b_\ell^{j,i}\). Furthermore, there are \(3m'\) agents \(c_1^{i,j},\dots,c_{3m^\prime}^{i,j}\). The gadget also contains seven agents _x<sup>i,j</sup>_, \(\overleftarrow{x}^{i,j}\), _x<sup>j,i</sup>_, \(\overleftarrow{x}^{j,i}\), \(z_1^{i,j}\), \(z_2^{i,j}\), and \(z_3^{i,j}\), which do not have the master preferences, and a cut-off gadget for \(z_2^{i,j}\).

The idea of the gadget is as follows: Every stable matching has to contain \(\{b_\ell^{i,j},b_\ell^{j,i},c_\ell^{i,j}\}\) or \(\{b_\ell^{i,j},b_\ell^{j,i},c_{\ell-1}^{i,j}\}\) for all \(\ell\in[3m'+1]\backslash\{r\}\) for some \(r\in[3m'+1]\), while for the remaining _r_, agent \(b_r^{i,j}\) must be matched to \(\{x^{i,j},\overleftarrow{x}^{i,j}\}\) and \(b_r^{j,i}\) must be matched to \(\{x^{j,i},\overleftarrow{x}^{j,i}\}\). Thus, the<tbc>

