By the cut-off gadget for \(\alpha_2^e\), we have \(M'(\alpha_1^e)=\{\alpha_2^e,\alpha_3^e\}\), and therefore, \(\alpha_1^e\) prefers \(\{a_r^i,d_a^{e,i}\}\) to \(M'\).

If _x=b_, then we claim that \(\{b_{n-r+1}^i,h_b^{e,i},\alpha_1^e\}\) is a blocking 3-set. Agent \(b_{n-r+1}^i\) prefers \(\{h_b^{e,i},\alpha_1^e\}\) to \(M(b_{n-r+1}^i)=\{d_p^i,\bar{d}_q^i\}\) for some \(p,q\in[n+1]\). Also agent \(h_b^{e,i}\) prefers \(\{b_{n-r+1}^i,\alpha_1^e\}\) to \(M'(h_a^{e,i})=\{f^e,\bar{f}^e\}\) as \(v_r^i\) is an endpoint of _e_. By the cut-off gadget for \(\alpha_2^e\), we have \(M'(\alpha_1^e)=\{\alpha_2^e,\alpha_3^e\}\), and therefore, \(\alpha_1^e\) prefers \(\{a_r^i,d_a^{e,i}\}\) over \(M'\).

We now turn to the reverse direction, i.e., if _S<sup>i</sup>_ and _S<sup>j</sup>_ select two vertices which are not connected by an edge from _E<sup>i,j</sup>_, then we can find a stable matching inside the edge gadget.

**Lemma 4.11.** _Let_ I _consist of two vertex-selection gadgets S<sup>i</sup> and S<sup>j</sup> and the edge gadget for every edge_ \(e\in E^{i,j}\) _between S<sup>i</sup> and S<sup>j</sup>._

_Given a matching M inside the vertex-selection gadgets such that at least one endpoint of e is not selected by a vertex-selection gadget for every_ \(e\in E^{i,j}\)_, then there exists a matching_ \(M'\) _containing M such that there is no blocking 3-set containing an agent from an edge gadget for an edge_ \(e\in E^{i,j}\).

_Proof._ Assume that _S<sup>i</sup>_ selects \(v_{i*}^i\) and _S<sup>j</sup>_ selects \(v_{j*}^j\). Let \(e=\{v_r^i,v_s^j\}\in E^{i,j}\). Since \(e\neq\{v_{i*}^i,v_{j*}^j\}\), we have \(r\neq i^*\) or \(s\neq j^*\). We assume that \(r\neq i^*\) (the case \(s\neq j^*\) is symmetric by switching the roles of _i_ and _j_). If _r\<i_<sup>∗</sup>, then we extend _M_ to the edge gadget by adding the 3- sets \(\{h_a^{e,i},f^e,\bar{f}^e\}\), \(\{h_b^{e,i},g_1^e,\bar{g}_1^e\}\), \(\{h_a^{e,j},g_2^e,\bar{g}_2^e\}\), \(\{h_b^{e,j},g_3^e,\bar{g}_3^e\}\), and \(\{\alpha_1^e,\alpha_2^e,\alpha_3^e\}\). If _r\>i_<sup>∗</sup>, then we extend _M_ to the edge gadget by adding the 3-sets \(\{h_a^{e,i},g_1^e,\bar{g}_1^e\}\), \(\{h_b^{e,i},f^e,\bar{f}^e\}\), \(\{h_a^{e,j},g_2^e,\bar{g}_2^e\}\), \(\{h_b^{e,j},g_3^e,\bar{g}_3^e\}\).

It remains to show that this does not lead to a blocking 3-set. First, note that no blocking 3- set can contain two agents belonging to different edge gadgets (because for two edges \(e,e'\in E^{i,j}\) with \(e\succ^{i,j}e'\), every agent _x_ from the edge gadget for \(e'\) prefers _M(x_) to any 2-set containing an agent from the edge gadget for \(e'\)). We assume again without loss of generality that \(r\neq i^*\). None of the agents \(g_p^e\), \(\bar{g}_p^e\), _f<sup>e</sup>_, and \(\bar{f}^e\) is contained in a blocking 3-set (any blocking 3-set containing \(g_p^e\) also contains \(\bar{g}_p^e\); however, \(\bar{g}_p^e\) ranks the acceptable triples in reverse order to \(g_p^e\); a symmetric argument applies to _f<sup>e</sup>_ and \(\bar{f}^e\)).

If _r\<i_<sup>∗</sup>, then agents \(h_b^{e,i}\), \(h_a^{e,j}\), and \(h_b^{e,j}\) are not part of a blocking 3-set because all 2-sets which they prefer to \(\{g_p^e,\bar{g}_p^e\}\) contain an agent \(g_p^{e^\prime}\). The only remaining possible blocking 3-set is \(\{a_p^i,\alpha_1^e,h_a^{e,i}\}\) for \(p\le r<i^*\). However, \(M(a_p^i)=\{c_q^i,\bar{c}_{q^\prime}^i\}\) and thus \(a_p^i\) prefers \(M(a_p^i)\) to \(\{\alpha_1^e,h_a^{e,i}\}\).

If _r\>i_<sup>∗</sup>, then agents \(h_a^{e,i}\), \(h_a^{e,j}\), and \(h_b^{e,j}\) are not part of a blocking 3-set because all 2-sets which they prefer to \(\{g_p^e,\bar{g}_p^e\}\) contain an agent \(g_p^{e^\prime}\). The only remaining possible blocking 3-set is thus \(\{b_p^i,\alpha_1^e,h_b^{e,i}\}\) for \(p\le n-r+1\). However, since \(n-r+1\le n-i^*\), it follows that \(M(b_p^i)=\{c_q^i,\bar{c}_{q^\prime}^i\}\) and therefore \(b_p^i\) prefers \(M(b_p^i)\) to \(\{\alpha_1^e,h_b^{e,i}\}\).

Having described the reduction and the crucial properties of the gadgets, the correctness of the reduction now easily follows.

## Proof of the forward direction.

We split the proof of correctness into two parts and start by showing that a multicolored independent set implies a stable matching.

**Lemma 4.12.** _If G contains a multicolored independent set I, then there exists a stable matching._

_Proof._ We construct a stable matching as follows. Each vertex-selection gadget _S<sup>i</sup>_ selects the vertex from \(I\cap V^i\). This matching is extended to the edge gadgets and cut-off gadgets as described in Lemmas 4.7 and 4.11. The stability of the constructed matching follows from Lemmas 4.7, 4.9 and 4.11.

