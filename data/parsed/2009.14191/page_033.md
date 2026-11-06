## 4.3.6 Proof of the forward direction

We prove that if _G_ contains a clique of size _k_, then \(\mathcal{I}'\) admits a stable matching. So let \(\{v_{p_1}^1,\dots,v_{p_k}^k\}\) be a multicolored clique. We construct a stable matching _M_ as follows.

For the vertex-selection gadget _S<sup>i</sup>_, we add the 3-set \(\{v_i^{p_i},s^i,\leftarrow\overline{s^i}\}\). All other vertex agents \(v_i^q\) are matched to each other, according to their index _q_ (i.e., we match the three agents with lowest index together, then the next three agents, and so on). Next, we consider an incidence gadget _B<sup>i,j</sup>_. Assume that \(\{v_{p_i}^i,v_{p_j}^j\}\) is the \(\alpha\)-th edge in the order of _E<sup>i,j</sup>_ fixed in Section 4.3.4. We add \(\{x^{i,j},\leftarrow\overline{x^{i,j}},b_\alpha^{i,j}\}\) and \(\{x^{j,i},\leftarrow\overline{x^{j,i}},b_\alpha^j\}\) to _M_. Furthermore, we add the 3-sets \(\{b_\ell^{i,j},b_\ell^{j,i},c_\ell^{i,j}\}\) for \(\ell<\alpha\), and \(\{b_\ell^{i,j},b_\ell^{j,i},c_{\ell-1}^{i,j}\}\) for \(\ell>\alpha\). Finally, we add the 3-set \(\{z_1^{i,j},z_2^{i,j},z_3^{i,j}\}\). The agents from the cut-off gadgets are matched as described in Lemma 4.7. We call the resulting matching _M_.

It remains to show that _M_ is stable. In order to do so, we will show step by step that no agent is part of a blocking 3-set. We start with the agents _s<sup>i</sup>_ and \(\leftarrow\overline{s^i}\).

**Lemma 4.17.** _For any_ \(i\in[k]\)_, agents s<sup>i</sup> and_ \(\leftarrow\overline{s^i}\) _are not part of a blocking 3-set._

_Proof._ We prove the lemma for \(\leftarrow\overline{s^i}\); the proof for _s<sup>i</sup>_ is symmetric. All 2-sets which \(\leftarrow\overline{s^i}\) ranks better than \(\{s^i,v_{p_i}^i\}\) are of the form \(\{s^i,v_\ell^i\}\) for \(\ell>p_i\) or \(\{\leftarrow\overline{x^{i,j}},b_\ell^{i,j}\}\) for an edge \(e_\ell\in E^{i,j}\) whose endpoint in _V<sup>i</sup>_ is \(v_q^i\) with _q\>p<sub>i</sub>_.

For the 2-sets \(\{s^i,v_\ell^i\}\) with \(\ell>p_i\), note that _s<sup>i</sup>_ does not prefer \(\{\leftarrow\overline{s^i},v_\ell^i\}\) to \(\{\leftarrow\overline{s^i},v_{p_i}^i\}\), and thus, \(\{\leftarrow\overline{s^i},s^i,v_\ell^i\}\) is not blocking.

For the 2-set \(\{\leftarrow\overline{x^{i,j}},b_\ell^{i,j}\}\), note that \(\leftarrow\overline{x^{i,j}}\) does not prefer \(\{b_\ell^{i,j},\leftarrow\overline{s^i}\}\) to \(\{\leftarrow\overline{x^{i,j}},b_r^{i,j}\}\) for the edge \(e_r=\{v_{p_i}^i,v_{p_j}^j\}\) as _q\>p<sub>i</sub>_.

Thus, \(\leftarrow\overline{s^i}\) is not part of a blocking 3-set.

We now turn to the remaining agents from vertex-selection gadgets.

**Lemma 4.18.** _For each_ \(i\le k\)_, no agent from V<sup>i</sup> is part of a blocking 3-set._

_Proof._ We prove the statement by induction. For _i_=0 there is nothing to show.

Fix \(i\in[k]\). Note that for all \(j\in[k]\), agents \(v_{p_j}^j\) are matched to their first choice, and thus not part of a blocking 2-set. By Lemma 4.17, no agent _s<sup>j</sup>_ or \(\leftarrow\overline{s^j}\) is involved in a blocking 3-set. Thus, by induction on _p_, one easily sees that all 2-sets which \(v_p^i\) prefers to the 2-set it is matched to in _M_, contain an agent about which we already know that it is not contained in a blocking 3-set, implying that also \(v_i^p\) is not contained in a blocking 3-set.

Thus, no agent of _V<sup>i</sup>_ is part of a blocking 3-set.

Next, we turn to the incidence-checking gadgets and start with agents _x<sup>i,j</sup>_ and \(\leftarrow\overline{x^{i,j}}\).

**Lemma 4.19.** _For any_ \(i,j\in[k]\) _with_ \(i\neq j\)_, agents x<sup>i,j</sup> and_ \(\leftarrow\overline{x^{i,j}}\) _are not part of a blocking 3-set._

_Proof._ A blocking 3-set cannot contain _s<sup>i</sup>_, \(\leftarrow\overline{s^i}\), _s<sup>j</sup>_, or \(\leftarrow\overline{s^j}\) by Lemma 4.17. Thus, it is of the form \(\{x^{i,j},\leftarrow\overline{x^{i,j}},b_\alpha^{i,j}\}\) for some \(\alpha\in[3m'+1]\). Since _x<sup>i,j</sup>_ prefers \(\{\leftarrow\overline{x^{i,j}},b_\alpha^{i,j}\}\) to \(M(x^{i,j})=\{\leftarrow\overline{x^{i,j}},b_\beta^{i,j}\}\) for some \(\beta\in[3m'+1]\), agent \(\leftarrow\overline{x^{i,j}}\) does not prefer \(\{x^{i,j},b_\alpha^{i,j}\}\) to \(\{x^{i,j},b_\beta^{i,j}\}\), and thus, \(\{x^{i,j},\leftarrow\overline{x^{i,j}},b_\alpha^{i,j}\}\) is not blocking.

Now we consider agents \(z_1^{i,j}\), \(z_2^{i,j}\), and \(z_3^{i,j}\).

**Lemma 4.20.** _For every_ \(i<j\in[k]\)_, agents_ \(z_1^{i,j}\), \(z_2^{i,j}\)_, and_ \(z_3^{i,j}\) _are not part of a blocking 3-set._

