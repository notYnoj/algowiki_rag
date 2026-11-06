_For every stable matching M in_ I_, there exists some_ \(p^*\in[n]\) _such that_ \(M(a_p)\in\{\{c_q,\bar{c}_{q^\prime}\}:q,q'\in[n-1]\}\) _for all p\<p_<sup>∗</sup>, \(M(a_p)\in\{\{d_r,\bar{d}_{r^\prime}\}:r,r'\in[n+1]\}\) _for_ \(p\ge p^*\), \(M(b_p)\in\{\{c_q,\bar{c}_{q^\prime}\}:q,q'\in[n-1]\}\) _for_ \(p\le n-p^*\)_, and_ \(M(b_p)\in\{\{d_r,\bar{d}_{r^\prime}\}:r,r'\in[n+1]\}\) _for i\>n-p_<sup>∗</sup>.

_Proof._ Consider any stable matching _M_. Due to the cut-off gadgets, any agent _c<sub>q</sub>_ is matched to a 2-set \(\{a_p,\bar{c}_{q^\prime}\}\) or \(\{b_p,\bar{c}_{q^\prime}\}\) for some \(p\in[n]\) and \(q'\in[n-1]\), and any agent _d<sub>r</sub>_ is matched to a 2-set \(\{a_p,\bar{d}_{r^\prime}\}\) or \(\{b_p,\bar{d}_{r^\prime}\}\) for some \(p\in[n]\) and \(r'\in[n+1]\). Since \(|\{a_p,b_p:p\in[n]\}|=2n=|\{c_q:q\in[n-1]\}|+|\{d_r:r\in[n+1]\}|\), it follows that any agent _a<sub>p</sub>_ or _b<sub>p</sub>_ is matched to a 2-set \(\{c_q,\bar{c}_{q^\prime}\}\) or \(\{d_r,\bar{d}_{r^\prime}\}\).

Assume for a contradiction that there exists some \(p\in[n]\) such that \(\{a_p,c_q,\bar{c}_{q^\prime}\}\notin M\) for all \(q,q'\in[n-1]\) but \(\{a_{p+1},c_s,\bar{c}_{s^\prime}\}\in M\) for some \(s,s'\in[n-1]\) (the case that there exists such _b<sub>p</sub>_ and _b_<sub>_p_+1</sub> is symmetric). Then \(\{a_p,c_s,\bar{c}_{s^\prime}\}\) is a blocking 3-set, contradicting the stability of _M_.

We now show that it is indeed possible to select an arbitrary vertex in any vertex-selection gadget.

**Lemma 4.9.** _Let_ I _be an_ MDSR-Poset_-instance containing a vertex-selection gadget._

_For any_ \(p^*\in[n]\)_, the matching_ \(M_{p^*}:=\{\{a_p,c_p,\bar{c}_{n-p^*+p}\}:p<p^*\}\cup\{\{a_p,d_{p-p^*+1},\bar{d}_{p+1}\}:p\ge p^*\}\cup\{\{b_p,c_{p+p^*-1},\bar{c}_p\}:p\le n-p^*\}\cup\{\{b_p,d_{p+1},\bar{d}_{p-(n-p^*)}\}:p>n-p^*\}\) _contains no blocking 3-set solely consisting from agents in the vertex-selection gadget._

_Proof._ Let \(p^*\in[n]\) and assume that _M_<sub>_p_<sup>∗</sup></sub> contains a blocking 3-set _t_ inside the vertex-selection gadget. Then _t_ contains two agents _c<sub>q</sub>_ and \(\bar{c}_{q^\prime}\) or _d<sub>r</sub>_ and \(\bar{d}_{r^\prime}\), and an agent _a<sub>p</sub>_ or _b<sub>p</sub>_.

**Case 1:** \(t=\{a_p,c_q,\bar{c}_{q^\prime}\}\). If _p\>p_<sup>∗</sup>, then \(\bar{c}_{q^\prime}\) does not prefer \(t\backslash\{\bar{c}_{q^\prime}\}\) to \(M(\bar{c}_{q^\prime})\), so assume \(p\le p^*\), implying that \(\{a_p,c_p,\bar{c}_{n-p^*+i}\}\in M_{p^*}\). If \(p\le min\{q,q'+p^*-n\}\), then _a<sub>p</sub>_ does not prefer _t_\\{_a<sub>p</sub>_} to _M_<sub>_p_<sup>∗</sup></sub>(_a<sub>p</sub>_). If \(q\le min\{p,q'+p^*-n\}\), then \(\{a_q,c_q,\bar{c}_{n-p^*+q}\}\in M_{p^*}\) and _c<sub>q</sub>_ does not prefer _t_\\{_c<sub>q</sub>_} to _M_<sub>_q_<sup>∗</sup></sub>(_c<sub>q</sub>_). If \(q'\le min\{p,q\}+n-p^*\), then \(\bar{c}_{q^\prime}\) does not prefer \(t\backslash\{\bar{c}_{q^\prime}\}\) to \(M_{p^*}(\bar{c}_{q^\prime})\).

**Case 2:** \(t=\{a_p,d_r,\bar{d}_{r^\prime}\}\). If \(p\le min\{r+p^*-1,r'-1\}\), then _a<sub>p</sub>_ does not prefer _t_\\{_a<sub>p</sub>_} to _M_<sub>_p_<sup>∗</sup></sub>(_a<sub>p</sub>_). If \(r\le min\{p+1,r'\}-p^*\), then \(\{a_{r+p^*-1},d_r,d_{r+p^*}\}\in M_{p^*}\) and _d<sub>r</sub>_ does not prefer _t_\\{_d<sub>r</sub>_} to _M_<sub>_p_<sup>∗</sup></sub>(_d<sub>r</sub>_). If \(r'\le min\{p,r+p^*-1\}+1\), then \(\bar{d}_{r^\prime}\) does not prefer \(t\backslash\{\bar{d}_{r^\prime}\}\) to \(M_{p^*}(\bar{d}_{r^\prime})\).

**Case 3:** \(t=\{b_p,c_q,\bar{c}_{q^\prime}\}\). If _p\>n-p_<sup>∗</sup>, then _c<sub>q</sub>_ does not prefer _t_\\{_c<sub>q</sub>_} to _M_<sub>_p_<sup>∗</sup></sub>(_c<sub>q</sub>_), so assume \(p\le n-p^*\), implying that \(\{b_p,c_{p+p^*-1},\bar{c}_p\}\in M_{p^*}\). If \(p\le min\{q-p^*+1,q'\}\), then _b<sub>p</sub>_ does not prefer _t_\\{_b<sub>p</sub>_} to _M_<sub>_p_<sup>∗</sup></sub>(_b<sub>p</sub>_). If \(q\le min\{p,q'\}+p^*-1\), then _c<sub>q</sub>_ does not prefer _t_\\{_c<sub>q</sub>_} to _M_<sub>_p_<sup>∗</sup></sub>(_c<sub>q</sub>_). If \(q'\le min\{p,q-p^*+1\}\), then \(\bar{c}_{q^\prime}\) does not prefer \(t\backslash\{\bar{c}_{q^\prime}\}\) to \(M_{p^*}(\bar{c}_{q^\prime})\).

**Case 4:** \(t=\{b_p,d_r,\bar{d}_{r^\prime}\}\). If \(p\le min\{r-1,r'+n-p^*\}\), then _b<sub>p</sub>_ does not prefer _t_\\{_b<sub>p</sub>_} to _M_<sub>_p_<sup>∗</sup></sub>(_b<sub>p</sub>_). If \(r\le min\{p,r'+n-p^*\}+1\), then _d<sub>r</sub>_ does not prefer _t_\\{_d<sub>r</sub>_} to _M_<sub>_p_<sup>∗</sup></sub>(_d<sub>r</sub>_). If \(r'\le min\{p,r-1\}-(n-p^*)\), then \(\{b_{r^\prime+n-p^*},d_{r^\prime+n-p^*+1},\bar{d}_{r^\prime}\}\in M_{p^*}\) and \(\bar{d}_{r^\prime}\) does not prefer \(t\backslash\{\bar{d}_{r^\prime}\}\) to \(M_{p^*}(\bar{d}_{r^\prime})\).

In each of the four cases, we have a contradiction, finishing the proof of the lemma.

The parameterized reduction will create a vertex-selection gadget _S<sup>i</sup>_ for each set _V<sup>i</sup>_, \(i\in[k]\). We refer to agent _a<sub>p</sub>_ (respectively \(b_p,c_q,\bar{c}_q,d_r\), or \(\bar{d}_r\)) from the _i_-th vertex-selection gadget via \(a_p^i\) (respectively \(b_p^i,c_q^i,\bar{c}_q^i,d_r^i\), or \(\bar{d}_r^i\)).

We say that a matching _M selects_ the vertex \(v_{p^*}^i\) in vertex-selection gadget _S<sup>i</sup>_ if, for all _p\<p_<sup>∗</sup>, we have \(M(a_p)=\{c_q,\bar{c}_{q^\prime}\}\) for some \(q,q'\in[n-1]\), and for all \(p\ge p^*\), we have \(M(a_p)=\{d_r,\bar{d}_{r^\prime}\}\) for some \(r,r'\in[n+1]\).

We now turn to the edge gadgets, which model the edges of _G_.

