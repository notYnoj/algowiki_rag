better _x<sup>i,j</sup>_ is matched, the worse \(\overleftarrow{x}^{i,j}\) is matched. Unless _e<sub>r</sub>_ is incident to the vertex selected by vertex-selection gadget _S<sup>i</sup>_, it follows that either _x<sup>i,j</sup>_ and _s<sup>i</sup>_ or \(\overleftarrow{x}^{i,j}\) and \(\overleftarrow{s}^i\) are part of a blocking 3-set together with the vertex selected by _S<sup>i</sup>_. By symmetric arguments, _e<sub>r</sub>_ is incident to the vertex selected by _S<sup>j</sup>_ in any stable matching, and thus, the vertices selected by the vertex-selection gadgets form a clique.

Let _Z<sup>i,j</sup>_ be the set of agents which are before \(b_1^{i,j}\) in the master poset. As the agents from _Z<sup>i,j</sup>_ are before every agent from \(B^{i^\prime,j^\prime}\) in the master poset, we have to add them in the beginning of the preferences of agent \(b_\ell^{i,j}\) and \(b_\ell^{j,i}\). Let \(X:=\{x^{i,j},\overleftarrow{x}^{i,j},x^{j,i},\overleftarrow{x}^{j,i}\}\) and let _A_ denote the set of all agents.

The preferences of \(b_\ell^{i,j}\) (resp. \(b_\ell^{j,i}\)) are as follows (deleting all 2-sets containing \(b_\ell^{i,j}\) (resp. \(b_\ell^{j,i}\)).

\(\{\{z,a\}:z\in Z^i,a\in A\}\succ\big\{\{a,x\}:a\in\{s^i,\overleftarrow{s}^i,s^j,\overleftarrow{s}^j\},x\in X\big\}\)<br>
\(\succ\{\{x,x'\}:x,x'\in X\}\succ\big\{\{x,b_q^{i,j}\},\{x,b_q^{j,i}\}:x\in X,q\in[3m'+1]\big\}\)<br>
\(\succ\big\{\{b_q^{i,j},z_1^{i,j}\},\{b_q^{j,i},z_1^{i,j}\}:q\in[\ell-1]\big\}\succ\left(\begin{array}{ c }
\{b_q^{i,j},b_q^{j,i},c_q^{i,j}:q\in[\ell]\} \\
2
\end{array}\right)\)<br>
\(\succ\big\{\{b_q^{i,j},z_1^{i,j}\},\{b_q^{j,i},z_1^{i,j}\}:q\in[\ell,3m'+1]\big\}\succ\dots^{(\text{rest})}.\)

The preferences of \(c_q^{i,j}\) are arbitrary preferences obeying the master poset.<br>
The preferences of \(z_1^{i,j}\) are as follows. \(\big\{\{b_p^{i,j},b_q^j\}:p\in[3m'+1],q\in[3m'+1]\big\}\succ\{z_2^{i,j},z_3^{i,j}\}\succ\dots^{(\text{rest})}\). The preferences of \(z_2^{i,j}\) are as follows. \(\{z_1^{i,j},z_3^{i,j}\}\succ\text{CO}_{z_2^{i,j}}\).<br>
The preferences of \(z_3^{i,j}\) are as follows. \(\{z_1^{i,j},z_2^{i,j}\}\succ\dots^{(\text{rest})}\).

To describe the preferences of _x<sup>i,j</sup>_ and \(\overleftarrow{x}^{i,j}\), we define sublists \(\mathcal{C}_\ell^\alpha\) and \(\overleftarrow{\mathcal{C}}_\ell^\alpha\) for \(\ell\in[3n'+1]\) and \(\alpha\in\{i,j\}\). The sublist \(C_\ell^i\) contains the 2-sets \(\{\overleftarrow{x}^{i,j},b_r^{i,j}\}\) for all \(e_r^{i,j}\in E^{i,j}\cap\delta(v_\ell^i)\), ordered increasingly by _r_. The sublist \(\overleftarrow{\mathcal{C}}_\ell^i\) contains the 2-sets \(\{x^{i,j},b_r^{i,j}\}\) for \(e_r^{i,j}\in E^{i,j}\cap\delta(v_\ell^i)\), but is ordered _decreasingly_ by _r_. Similarly, sublist \(\mathcal{C}_\ell^j\) contains the 2-sets \(\{\overleftarrow{x}^{j,i},b_r^{j,i}\}\) for all \(e_r^{j,i}\in E^{i,j}\cap\delta(v_\ell^i)\), ordered increasingly by _r_, and sublist \(\overleftarrow{\mathcal{C}}_\ell^j\) contains 2-sets \(\{x^{j,i},b_r^{j,i}\}\) ordered decreasingly by _r_. The preferences of _x<sup>i,j</sup>_ and \(\overleftarrow{x}^{i,j}\) look as follows.

\(x^{i,j}:\mathcal{C}_{3n^\prime+1}^i\succ\{\overleftarrow{s}^i,v_i^{3n^\prime+1}\}\succ\mathcal{C}_{3n^\prime}^i\succ\{\overleftarrow{s}^i,v_i^{3n^\prime}\}\succ\cdots\succ\mathcal{C}_1^i\succ\{\overleftarrow{s}^i,v_i^1\}\succ\text{CO}_{x^{i,j}},\)<br>
\(\overleftarrow{x}^{i,j}:\overleftarrow{\mathcal{C}}_1^i\succ\{s^i,v_i^1\}\succ\overleftarrow{\mathcal{C}}_2^i\succ\{s^i,v_i^2\}\succ\cdots\succ\overleftarrow{\mathcal{C}}_{3n^\prime+1}^i\succ\{s^i,v_i^{3n^\prime+1}\}\succ\text{CO}_{\overleftarrow{x}^{i,j}},\)<br>
\(x^{j,i}:\mathcal{C}_{3n^\prime+1}^j\succ\{\overleftarrow{s}^j,v_j^{3n^\prime+1}\}\succ\mathcal{C}_{3n^\prime}^j\succ\{\overleftarrow{s}^j,v_j^{3n^\prime}\}\succ\cdots\succ\mathcal{C}_1^j\succ\{\overleftarrow{s}^j,v_j^1\}\succ\text{CO}_{x^{j,i}},\)<br>
\(\overleftarrow{x}^{j,i}:\overleftarrow{\mathcal{C}}_1^j\succ\{s^j,v_j^1\}\succ\overleftarrow{\mathcal{C}}_2^j\succ\{s^j,v_j^2\}\succ\cdots\succ\overleftarrow{\mathcal{C}}_{3n^\prime+1}^j\succ\{s^j,v_j^{3n^\prime+1}\}\succ\text{CO}_{\overleftarrow{x}^{j,i}}.\)

## 4.3.5 The reduction

Given an instance (_G,k_) of Multicolored Clique, we construct an MDSR-instance \(\mathcal{I}'\) as follows. Instance \(\mathcal{I}'\) contains _k_ vertex-selection gadgets _S<sup>i</sup>_, one for each color class _V<sup>i</sup>_. Between each pair (_S<sup>i</sup>,S<sup>j</sup>_) of vertex-selection gadgets with _i\<j_, there is an incidence-checking gadget _B<sup>i,j</sup>_.

We first show that our parameter \(\lambda\) is indeed bounded by _O(k_<sup>2</sup>) for the constructed instance \(\mathcal{I}'\).

**Lemma 4.16.** \(\lambda(\mathcal{I}')=O(k^2)\).

_Proof._ The master poset is described in Section 4.3.1. It is a strict order and contains all agents but the _O(k_<sup>2</sup>) agents _s<sup>i</sup>_, \(\overleftarrow{s}^i\), \(x^{i,j}\), \(\overleftarrow{x}^{i,j}\), \(z_1^{i,j}\), \(z_2^{i,j}\) for \(i,j\in[k]\) with \(i\neq j\), and all agents contained in cut-off gadgets. It is easy to verify that the preferences obey this master poset.

