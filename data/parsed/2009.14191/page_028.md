## Proof of the backward direction.

We now turn to the backward direction, showing that a stable matching implies a multicolored independent set.

**Lemma 4.13.** _If there exists a stable matching, then G contains a multicolored independent set._

_Proof._ By Lemma 4.8, every vertex-selection gadget selects a vertex. By Lemma 4.10, no two selected vertices are adjacent. Thus, the selected vertices form a multicolored independent set.

## The parameter.

It remains to show that the preferences of the constructed MDSR-Poset- instance can be derived from a poset \(\succ_\mathrm{ML}\) of bounded width.

The poset \(\succ_\mathrm{ML}\) looks as follows. For each vertex-selection gadget _S<sup>i</sup>_, we have \(a_j^i\succ_\mathrm{ML}a_{j^\prime}^i\), \(b_j^i\succ_\mathrm{ML}b_{j^\prime}^i\), \(c_j^i\succ_\mathrm{ML}c_{j^\prime}^i\), \(\bar{c}_j^i\succ_\mathrm{ML}\bar{c}_{j^\prime}^i\), \(d_j^i\succ_\mathrm{ML}d_{j^\prime}^i\), and \(\bar{d}_j^i\succ_\mathrm{ML}\bar{d}_{j^\prime}^i\) if and only if \(j<j'\). Furthermore, we have for every \(q\in[6]\) that \(z_{a_j^i}^q\succ_\mathrm{ML}z_{a_{j^\prime}^i}^q\), \(z_{b_j^i}^q\succ_\mathrm{ML}z_{b_{j^\prime}^i}^q\), \(z_{c_j^i}^q\succ_\mathrm{ML}z_{c_{j^\prime}^i}^q\), \(z_{\bar{c}_j^i}^q\succ_\mathrm{ML}z_{\bar{c}_{j^\prime}^i}^q\), and \(z_{\bar{d}_j^i}^q\), and \(z_{\bar{d}_j^i}^q\succ_\mathrm{ML}z_{\bar{d}_{j^\prime}^i}^q\).

For each \(i,j\in[k]\) with _i\<j_, each \(e,e'\in E^{i,j}\) and \(p\in[3]\), we have \(h_a^{e,i}\succ_\mathrm{ML}h_a^{e^\prime,i}\), \(h_b^{e,i}\succ_\mathrm{ML}h_b^{e^\prime,i}\), \(h_a^{e,j}\succ_\mathrm{ML}h_a^{e^\prime,j}\), \(h_b^{e,j}\succ_\mathrm{ML}h_b^{e^\prime,j}\), \(h_b^{e,i}\succ_\mathrm{ML}h_b^{e^\prime,i}\), \(g_p^e\succ_\mathrm{ML}g_p^{e^\prime}\), \(f^e\succ_\mathrm{ML}f^{e^\prime}\), and \(\alpha_p^e\succ_\mathrm{ML}\alpha_p^{e^\prime}\) if and only if \(e\succ^{i,j}e'\). Furthermore, we have for every \(p\in[3]\) and \(q\in[6]\) that \(z_{h_a^{e,i}}^q\succ_\mathrm{ML}z_{h_a^{e^\prime,i}}^q\), \(z_{h_b^{e,i}}^q\succ_\mathrm{ML}z_{h_b^{e^\prime,i}}^q\), \(z_{h_a^{e,j}}^q\succ_\mathrm{ML}z_{h_a^{e^\prime,j}}^q\), \(z_{h_b^{e,i}}^q\succ_\mathrm{ML}z_{h_b^{e^\prime,i}}^q\), \(z_{g_p^e}^q\succ_\mathrm{ML}z_{g_p^{e^\prime}}^q\), \(z_{f^e}^q\succ_\mathrm{ML}z_{f^{e^\prime}}^q\), and \(z_{\alpha_p^e}^q\succ_\mathrm{ML}z_{\alpha_p^{e^\prime}}^q\) if and only if \(e\succ^{i,j}e'\).

We arrive at the following observation.

**Observation 4.14.** _The preferences are derived from a poset of width at most O(k_<sup>2</sup>).

_Proof._ It is easy to verify that the preferences are derived from \(\succ_\mathrm{ML}\), so it remains to show that \(\succ_\mathrm{ML}\) has width _O(k_<sup>2</sup>). Note that \(\succ_\mathrm{ML}\) decomposes in _O(k_<sup>2</sup>) chains, from which the observation follows by Dilworth’s Theorem \[14\]: For every vertex-selection gadget _S<sup>i</sup>_, we have 42 chains \(a_1^i\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}a_n^i\), \(b_1^i\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}b_n^i\), \(c_1^i\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}c_n^i\), \(\bar{c}_1^i\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}\bar{c}_n^i\), \(d_1^i\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}d_n^i\), and \(\bar{d}_1^i\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}\bar{d}_n^i\) as well as for every \(q\in[6]\), chains \(z_{a_1^i}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{a_n^i}^q\), \(z_{b_1^i}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{b_n^i}^q\), \(z_{c_1^i}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{c_n^i}^q\), \(z_{\bar{c}_1^i}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{\bar{d}_n^i}^q\), and \(z_{\bar{d}_1^i}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{\bar{d}_n^i}^q\). For every \(i,j\in[k]\) with _i\<j_, let _E<sup>i,j</sup>_={_e_<sub>1</sub>_,...,e<sub>s</sub>_} such that \(e_r\succ^{i,j}e_{r+1}\) for every \(r\in[s-1]\). We have 77 chains \(h_a^{e_1,i}\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}h_a^{e_s,i}\), \(h_b^{e_1,i}\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}h_b^{e_s,i}\), \(h_a^{e_1,j}\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}h_a^{e_s,j}\), \(h_b^{e_1,j}\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}h_a^{e_s,j}\), \(h_b^{e_1,j}\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}h_b^{e_s,j}\), \(h_b^{e_1,i}\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}h_b^{e_s,i}\), \(g_p^{e_1}\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}g_p^{e_s}\) for every \(p\in[3]\), \(f^{e_1}\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}f^{e_s}\), and \(\alpha_p^{e_1}\succ_\mathrm{ML}\alpha_p^{e_s}\) for every \(p\in[3]\) as well as for every \(q\in[6]\), chains \(z_{h_a^{e_1,i}}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{h_a^{e_s,i}}^q\), \(z_{h_b^{e_1,i}}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{h_b^{e_s,i}}^q\), \(z_{h_a^{e_1,j}}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{h_a^{e_s,j}}^q\), \(z_{h_b^{e_1,j}}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{h_a^{e_s,j}}^q\), \(z_{h_b^{e_1,j}}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{h_b^{e_s,j}}^q\), \(z_{f_{e_1}}^q\succ_\mathrm{ML}\cdots\succ_\mathrm{ML}z_{f_{e_s}}^q\), and \(z_{\alpha_p^{e_1}}^q\succ_\mathrm{ML}z_{\alpha_p^{e_s}}^q\) for every \(p\in[3]\).

We now have all ingredients to obtain the following main result.

**Theorem 4.15.** 3DSR-Poset _parameterized by poset width is_ W\[1\]_-hard._

_Proof._ The reduction clearly runs in polynomial time. Lemmas 4.12 and 4.13 prove its correctness, and Observation 4.14 shows that the width of the poset is bounded by _O(k_<sup>2</sup>). Thus, we found a parameterized reduction from Multicolored Independent Set to 3DSR-Poset parameterized by the width of the poset, proving W\[1\]-hardness.

