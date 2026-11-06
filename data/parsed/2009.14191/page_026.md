\(\alpha_3^e:\{\{\alpha_1^{e^\prime},\alpha_2^{e^{\prime\prime}}\}:e',e''\in E^{-\unknown e}\}\succ\mathrm{CO}_{\alpha_3^e}.\)

Figure 2 visualizes the 3-sets _t_={_x_<sub>1</sub>_,x_<sub>2</sub>_,x_<sub>3</sub>} such that _x<sub>i</sub>_ prefers _t_\\{_x<sub>i</sub>_} to the 2-sets containing agents from its cut-off gadget for all \(i\in[3]\).

Furthermore, we extend the preferences of \(a_p^\ell\) by inserting the 2-sets \(\{h_a^{e,\ell},\alpha_1^e\}\) for all \(e\in E^{i,j}\) directly after \(\{c_{n-1}^\ell,\bar{c}_{n-1}^\ell\}\) (and before \(\{d_1^\ell,\bar{d}_1^\ell\}\)), and the preferences of \(b_p^\ell\) by the 2-sets \(\{h_b^{e,\ell},\alpha_1\}\) for all \(e\in E^{i,j}\) directly after \(\{c_{n-1}^\ell,\bar{c}_{n-1}^\ell\}\) for every \(p\in[n]\) and \(\ell\in\{i,j\}\).

We now show that if _E<sup>i,j</sup>_ contains an edge between the two vertices selected by _S<sup>i</sup>_ and _S<sup>j</sup>_ for a matching _M_, then _M_ is not stable.

**Lemma 4.10.** _Let_ I _consist of two vertex-selection gadgets S<sup>i</sup> and S<sup>j</sup> and the edge gadget for E<sup>i,j</sup> between S<sup>i</sup> and S<sup>j</sup>._

_If for a matching M in_ I _and an edge_ \(e=\{v_r^i,v_s^j\}\in E^{i,j}\) _vertex-selection gadgets S<sup>i</sup> and S<sup>j</sup> select the vertices_ \(v_r^i\) _and_ \(v_s^j\)_, then matching M contains a blocking 3-set._

_Proof._ We need to show that _M_ contains a blocking 3-set. By the cut-off gadgets, we know that any 3-set from _M_ contains three agents belonging to the same edge. By the cut-off gadgets for _f<sup>e</sup>_ and \(\bar{f}^e\), we know that \(M'\) must contain a 3-set \(\{h_x^{e,\ell},f^e,\bar{f}^e\}\) for some \(\ell\in\{i,j\}\) and \(x\in\{a,b\}\). We assume \(\ell=i\); the case \(\ell=j\) is symmetric. We make a case distinction on whether _x=a_ or _x=b_.

If _x=a_, then we claim that \(\{a_r^i,h_a^{e,i},\alpha_1^e\}\) is a blocking 3-set. Agent \(a_r^i\) prefers \(\{h_a^{e,i},\alpha_1^e\}\) to \(M(a_r^i)=\{d_p^i,\bar{d}_q^i\}\). Agent \(h_a^{e,i}\) prefers \(\{a_r^i,\alpha_1^e\}\) to \(M'(h_a^{e,i})=\{f^e,\bar{f}^e\}\) as \(v_r^i\) is an endpoint of _e_.

{f, f}
b2
h e,i
h e,j b
b2
b1
b1
a2, a3
a1
a2
a2
a1
ha
ha
ha
a1
{g3, ,
Figure 2: The acceptable 3-sets (i.e., 3-sets which are preferred over the cut-off gadget by all agents they contain) of the edge gadget for the edge {v1, v2}. Acceptable 3-sets are drawn in two ways: If they contain one of the ellipses, then they consist of the two agents inside the ellipse and the other endpoint of an edge incident to the ellipse (for example, the edge between {f,} corresponds to the acceptable 3-set {hb e,i, f,}). Otherwise, they are marked by the bold colored paths of length two (for example, the red path {a2}-h a e,i-a1 corresponds to the 3-set {a2},h a e,i, a1).

Figure 2: The acceptable 3-sets (i.e., 3-sets which are preferred over the cut-off gadget by all agents they contain) of the edge gadget for the edge {v1, v2}. Acceptable 3-sets are drawn in two ways: If they contain one of the ellipses, then they consist of the two agents inside the ellipse and the other endpoint of an edge incident to the ellipse (for example, the edge between {hb e,i and {f,} corresponds to the acceptable 3-set {hb e,i, f,}). Otherwise, they are marked by the bold colored paths of length two (for example, the red path {a2}-h a e,i-a1 corresponds to the 3-set {a2},h a e,i, a1).

