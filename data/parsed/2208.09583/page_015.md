<tbc>edges to _v<sub>i</sub>_ of type _X_ according to the indices of the other endpoint (the smaller index is ranked higher).

This concludes the construction part. The construction is illustrated in Figure 3

**Claim 17.** _If there are disjoint independent subsets_ \(V_1,V_2\subset V\) _with_ |_V_<sub>1</sub>|+|_V_<sub>2</sub>|=_k in G, then there is a stable matching of size n+k in_ \(G'\).

_Proof._ Let _V_<sub>1</sub>_,V_<sub>2</sub> be two disjoint independent sets in _G_. We create a matching _M_ in \(G'\) as follows. For each \(v_i\in V_1\), we add the edges \(h_{i(1)}=(u_i,x_i)_1,h'_{i(1)}=(y_i,w_i)_1\). For each \(v_i\in V_2\), we add the edges \(h_{i(2)}=(u_i,x_i)_2,h'_{i(2)}=(y_i,w_i)_2\). Finally, for \(v_i\in V\backslash(V_1\cup V_2)\), we add an edge _g_<sub>_i_(1)</sub>=(_u<sub>i</sub>,w<sub>i</sub>_)<sub>1</sub>. Clearly, _M_ has size 2_k_+(_n-k_)=_n+k_.

We claim that _M_ is stable. First, observe that each _u<sub>i</sub>,w<sub>i</sub>_ agent is matched in _M_. No \(g_{i(\ell)}\) type edge can block _M_ because such a blocking edge would imply that there is an index \(i\in[n]\) such that \(h_{i(\ell)},h'_{i(3-\ell)}\in M\) for some \(\ell\in[2]\), which contradicts the construction of _M_. No _e<sub>ij</sub>_ or _f<sub>ij</sub>_ type edge can block _M_ either, because _e<sub>ij</sub>_ (resp., _f<sub>ij</sub>_) could block _M_ only if \(h_{i(\ell)},h'_{j(\ell)}\in M\) for some \(\ell\in[2]\), however, such indices _i,j_ must satisfy \(v_i,v_j\in V_\ell\) by the construction, and as _V_<sub>1</sub> and _V_<sub>2</sub> were independent sets, such an edge _e<sub>ij</sub>_ (resp., _f<sub>ij</sub>_) could not exist in the first place. Any \(h_{i(\ell)}\) (resp., \(h'_{i(\ell)}\)) type edge cannot block _M_ either, as its endpoint _u<sub>i</sub>_ (resp., _w<sub>i</sub>_) is covered by a better or indifferent edge in _M_.

**Claim 18.** _If there is a stable matching of size n+k in_ \(G'\)_, then there are disjoint independent sets_ \(V_1,V_2\subset V\) _in G such that_ |_V_<sub>1</sub>|+|_V_<sub>2</sub>|=_k._

_Proof._ Let _M_ be a stable matching of size _n+k_.

We claim that for any \(i\in[n]\) and \(\ell\in[2]\), if \(h_{i(\ell)}\in M\), then \(h'_{i(\ell)}\in M\). Suppose for contradiction that \(h_{i_0(1)}\in M\) but \(h'_{i_0(1)}\notin M\) for some \(i_0\in[n]\). Since _g_<sub>_i_<sub>0</sub>(1)</sub>=(_u_<sub>_i_<sub>0</sub></sub>_,w_<sub>_i_<sub>0</sub></sub>)<sub>1</sub> does not block _M_ while _u_<sub>_i_<sub>0</sub></sub> prefers it to \(h_{i_0(1)}\in M\), agent _w_<sub>_i_<sub>0</sub></sub> must be covered by some edge that is not worse than (i.e., better than or incomparable with) _g_<sub>_i_<sub>0</sub>(1)</sub>. As \(h'_{i_0(1)}\notin M\), then \(f_{i_1i_0}\in M\) must hold for some \(i_1\in[n]\). Now, we know that \(G'\) has an edge _f_<sub>_i_<sub>0</sub>_i_<sub>1</sub></sub>. Since _f_<sub>_i_<sub>0</sub>_i_<sub>1</sub></sub>=(_u_<sub>_i_<sub>0</sub></sub>_,w_<sub>_i_<sub>1</sub></sub>)<sub>2</sub> and _g_<sub>_i_<sub>1</sub>(1)</sub>=(_u_<sub>_i_<sub>1</sub></sub>_,w_<sub>_i_<sub>1</sub></sub>)<sub>1</sub> do not block _M_ while _u_<sub>_i_<sub>0</sub></sub> prefers _f_<sub>_i_<sub>0</sub>_i_<sub>1</sub></sub> to \(h_{i_0(1)}\in M\) and _u_<sub>_i_<sub>1</sub></sub> prefers _g_<sub>_i_<sub>1</sub>(1)</sub><tbc>

V2
V4
V1
V3
V1 = {v1}
V2 = {v2, V4}

X1
X2
X3
X4
h1(1)
h1(2)
h4(1)
h4(2)
u1
u2
u3
u4
w1
w2
w3
w4
h' 1(1)
h' 1(2)
h' 4(1)
h' 4(2)
y1
y2
y3
y4

(a)

(b)

Figure 3: The reduction for Theorem 3. (a) An instance of independent set with two disjoint independent sets _V_<sub>1</sub> (blue) and _V_<sub>2</sub> (red). (b) The corresponding instance of max-smpo. Parallel edges \(h_{i(\ell)}\) and \(h'_{i(\ell)}\) with \(\ell=1\) are drawn on the left and those with \(\ell=2\) are drawn on the right. Blue and red edges represent the edges corresponding to the two independent sets _V_<sub>1</sub>_,V_<sub>2</sub>, respectively, which are chosen in the constructed matching.

