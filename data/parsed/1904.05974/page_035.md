The preferences of _s_ and _t_ do not matter; in fact, they are _unpopular_ vertices in _G_ since \(M^*=\cup_{i=1}^k\{(a_i,d_i),(c_i,b_i),(a'_i,d'_i),(c'_i,b'_i)\}\) is a dominant matching in _G_. To show this, we first claim that the vector \(\unknown\) with \(\alpha_s=\alpha_t=0\), \(\alpha_u=1\) for \(u\in\{a_i,b_i,a'_i,b'_i\}\) for every \(i\in[k]\), and \(\alpha_u=-1\) for \(u\in\{c_i,d_i,c'_i,d'_i\}\) for every \(i\in[k]\) is a witness for _M_<sup>∗</sup>.

Observe that \(\alpha_u=0=\mathsf{wt}_{M^*}(u,u)\) for \(u\in\{s,t\}\), while \(\alpha_u\ge-1=\mathsf{wt}_{M^*}(u,u)\) for all other vertices _u_. Now take an edge (_u,v_). If \((u,v)\in M^*\), then \(\alpha_u+\alpha_v=0=\mathsf{wt}_{M^*}(u,v)\). If \(u\in\{s,t\}\), then \(\alpha_u+\alpha_v=1\ge\mathsf{wt}_{M^*}(u,v)=0\). If \(u\in\{b_i,b'_i\}\) and \(v\in\{a_{i+1},a'_{i+1}\}\) for some _i_, then \(\alpha_u+\alpha_v=2\ge\mathsf{wt}_{M^*}(u,v)\). Observe that for each \(i\in[k]\), we have:

- \(\alpha_{a_i}+\alpha_{b_i}=2=\mathsf{wt}_{M^*}(a_i,b_i);\alpha_{c_i}+\alpha_{d_i}=-2=\mathsf{wt}_{M^*}(c_i,d_i)\).<tbc>

<tbc>The same equalities hold when we replace every vertex _x_ above with vertex \(x'\). It is easy to see that \(\sum_u\alpha_u=0\) and this concludes the proof that \(\unknown\) is a witness for _M_<sup>∗</sup>. Hence _M_<sup>∗</sup> is popular. Moreover, since edges (_c_<sub>1</sub>_,d_<sub>1</sub>) and \((c'_1,d'_1)\) are labeled (-,-), no _M_<sup>∗</sup>-alternating path starting from _s_ in _G_<sub>_M_<sup>∗</sup></sub> can reach _t_. Hence, Theorem 6 implies that _M_<sup>∗</sup> is a dominant matching.

We are now ready to define the family N of matchings. Any matching \(N\in\mathcal{N}\) is constructed by choosing for each _i_=1_,...,k_:

- either the 4 edges in \(\{(a_i,b_i),(c_i,d_i),(a'_i,d'_i),(c'_i,b'_i)\}\)<tbc>

**-** or the 4 edges in \(\{(a_i,d_i),(c_i,b_i),(a'_i,b'_i),(c'_i,d'_i)\}\).

If the former happens, we say that \(\langle a_i,b_i,c_i,d_i\rangle\) is in _stable_ state and \(\langle a'_i,b'_i,c'_i,d'_i\rangle\) is in _dominant_ state. Else we say that \(\langle a_i,b_i,c_i,d_i\rangle\) is in _dominant_ state and \(\langle a'_i,b'_i,c'_i,d'_i\rangle\) is in _stable_ state.

Observe that when \(\langle a_i,b_i,c_i,d_i\rangle\) is in dominant state, the edge (_c<sub>i</sub>,d<sub>i</sub>_) is labeled (-,-) wrt _N_ and similarly, when \(\langle a'_i,b'_i,c'_i,d'_i\rangle\) is in dominant state, the edge \((c'_i,d'_i)\) is labeled (-,-) wrt _N_. Recall that _G<sub>N</sub>_ is _G_ with edges labeled (-,-) wrt _N_ deleted. We now show that the following three properties are true in _G_:

1. every \(N\in\mathcal{N}\) is a max-size popular matching and uses only dominant edges;<tbc>

2. for each \(N\in\mathcal{N}\), _G<sub>N</sub>_ has exactly one _N_-augmenting path \(\rho_N\);<tbc>

3. for each matching _M_ in _G_, \(M\supseteq(\rho_N\backslash N)\) for at most one \(N\in\mathcal{N}\).

_Proof._ (of (1). We will prove the popularity of _N_ by showing a witness \(\unknown\). Define \(\unknown\) as follows: first, let \(\alpha_s=\alpha_t=0\). For \(1\le i\le k\):

- if \(N\supset\{(a_i,b_i),(c_i,d_i),(a'_i,d'_i),(c'_i,b'_i)\}\), i.e., if \(\langle a_i,b_i,c_i,d_i\rangle\) is in stable state and \(\langle a'_i,b'_i,c'_i,d'_i\rangle\) is in dominant state, then let \(\alpha_{a_i}=\alpha_{b_i}=\alpha_{c_i}=\alpha_{d_i}=0\) while \(\alpha_{a_i^\prime}=\alpha_{b_i^\prime}=1\) and \(\alpha_{c_i^\prime}=\alpha_{d_i^\prime}=-1\).<tbc>

**-** else let \(\alpha_{a_i}=\alpha_{b_i}=1\) and \(\alpha_{c_i}=\alpha_{d_i}=-1\) while \(\alpha_{a_i^\prime}=\alpha_{b_i^\prime}=\alpha_{c_i^\prime}=\alpha_{d_i^\prime}=0\).<tbc>

a1
b1
a2
b2
ak
bk
S
d1
C1
d2
C2
dk
ck
t
a'1
b'1
a'2
b'2
ak
b'k
d'1
c'1
d'2
c'2
d'k
c'k

**Fig.13.** The instance _G_ used in our lower bound argument. All matchings in N use only the solid edges.

