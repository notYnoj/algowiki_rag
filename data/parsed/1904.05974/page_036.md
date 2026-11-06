It is easy to check that every edge is _covered_, i.e., \(\alpha_u+\alpha_v\ge\mathsf{wt}_N(u,v)\) for all edges (_u,v_) in _G_. In particular, we have wt_<sub>N</sub>(e_)=0 for every dashed edge _e_ in Fig. 13 and \(\alpha_u\ge 0\) for \(u\in\cup_i\{a_i,b_i,a'_i,b'_i\}\). We also have \(\sum_u\alpha_u=0\) and \(\alpha_u\ge\mathsf{wt}_N(u,u)\) for all vertices _u_. Thus \(\alpha\) is a witness of _N_’s popularity in _G_. Moreover, _N_ matches all vertices other than _s_ and _t_, exactly as the dominant matching _M_<sup>∗</sup> does. Hence _N_ is a max-size popular matching in _G_.

Observe that the matchings \(M=\cup_{i=1}^{k-1}\{(a_i,b_i),(c_i,d_i),(a'_i,b'_i),(c'_i,d'_i)\}\cup\{(a_k,d_k),(c_k,b_k),(a'_k,d'_k),(c'_k,b'_k)\}\) and \(M'=\{(a_1,d_1),(c_1,b_1),(a'_1,d'_1),(c'_1,b'_1)\}\cup_{i=2}^k\{(a_i,b_i),(c_i,d_i),(a'_i,b'_i),(c'_i,d'_i)\}\) are dominant. The proof is analogous to the one previously given for _M_<sup>∗</sup>, hence it is omitted.

Observe that every edge in _N_ is in \(M^*\cup M\cup M'\). Thus _N_ uses only dominant edges. \(\square\)

_Proof._ (of (2)). The main observation here is that if a gadget, say \(\langle a_i,b_i,c_i,d_i\rangle\), is in dominant state in _N_ then no _N_-alternating path in _G<sub>N</sub>_ can pass through \(\langle a_i,b_i,c_i,d_i\rangle\). This is because the edge (_c<sub>i</sub>,d<sub>i</sub>_) is _not_ present in _G<sub>N</sub>_. Thus there is a unique _N_-augmenting path \(\rho_N\) in _G<sub>N</sub>_: for each _i_, \(\rho_N\) uses either (_a<sub>i</sub>,b<sub>i</sub>_) or \((a'_i,b'_i)\) depending on whether \(\alpha_{a_i}=0\) or \(\alpha_{a_i}=1\). If \(\alpha_{a_i}=0\), then \((a_i,b_i)\in\rho_N\), else \((a'_i,b'_i)\in\rho_N\). Note that the edges in \(\rho_N\backslash N\) belong to _G<sub>N</sub>_ since each such edge _e_ (a dashed edge in Fig. 13) satisfies wt_<sub>N</sub>(e_)=0. \(\square\)

_Proof._ (of (3)). Let _M_ be any matching in _G_ and let \(N,N'\in\mathcal{N}\). There is some index _i_ such that one of \(N,N'\) contains the edge (_a<sub>i</sub>,b<sub>i</sub>_) and the other contains the edge \((a'_i,b'_i)\). Let _i_ be the largest such index. Assume without loss of generality that \((a_i,b_i)\in N\) and \((a'_i,b'_i)\in N'\).

- If _i=k_, then the augmenting path \(\rho_N\) ends with the edge (_b<sub>k</sub>,t_) while the augmenting path \(\rho_{N^\prime}\) ends with the edge \((b'_k,t)\). Since only one of \((b_k,t),(b'_k,t)\) can be present in _M_, it follows that _M_ can be a superset of either \((\rho_N\backslash N)\) or \((\rho_{N^\prime}\backslash N')\) but not both.<tbc>

**-** Suppose _i\<k_. By the definition of index _i_, either \((a_{i+1},b_{i+1})\in N\cap N'\) or \((a'_{i+1},b'_{i+1})\in N\cap N'\). Assume the former (without loss of generality). So \(\rho_N\backslash N\) contains (_b<sub>i</sub>,a_<sub>_i_+1</sub>) while \(\rho_{N^\prime}\backslash N'\) contains \((b'_i,a_{i+1})\). Since only one of \((b_i,a_{i+1}),(b'_i,a_{i+1})\) can be present in _M_, it again follows that _M_ can be a superset of only one of \((\rho_N\backslash N)\), \((\rho_{N^\prime}\backslash N')\).

Thus \(M\supseteq(\rho_N\backslash N)\) for at most one \(N\in\mathcal{N}\). \(\square\)

**Our Lower Bound Argument.** For \(N\in\mathcal{N}\), let M_<sub>N</sub>_ be the set of matchings _M_ such that \(M\supseteq(\rho_N\backslash N)\). We show the following claim for every \(N\in\mathcal{N}\) and \(T\notin\mathcal{M}_N\).

**Claim 9** _N satisfies_ \(\mathsf{wt}_N(T)\le-k_T\) _for all matchings_ \(T\notin\mathcal{M}_N\).

_Proof._ Let \(T\notin\mathcal{M}_N\) and let \(e\in(\rho_N\backslash N)\backslash T\). Let _G<sup>e</sup>_ be the instance obtained from _G_ by removing edge _e_. Note that _T,N_ are matchings of _G<sup>e</sup>_, and _N_ is popular in _G<sup>e</sup>_ (since _N_ is popular in _G_). There is no _N_-augmenting path in \(G_N^e\), since \(\rho_N\) was the only _N_-augmenting path in _G<sub>N</sub>_ (from property (2)). Hence, from Theorem 6 we conclude that _N_ is dominant in _G<sup>e</sup>_. That is, \(N\in\mathcal{D}_{G^e}\). Since \(e\notin T\), the value _k<sub>T</sub>_ is the same in both _G_ and _G<sup>e</sup>_. Hence \(\mathsf{wt}_N(T)\le-k_T\). \(\square\)

Since \(I_N\notin\mathcal{D}_G\), there must be some inequality from (25) or (26) that is not satisfied by _I<sub>N</sub>_. We know from property (1) that the incidence vector _I<sub>N</sub>_ of matching _N_ satisfies all constraints in (25). Hence, because of Claim 9, _I<sub>N</sub>_ must be cut off by an inequality \(\mathsf{wt}_N(M)\le-k_M\) for some \(M\in\mathcal{M}_N\). Thus, in any minimal system contained in (25)-(26), at least one inequality \(\mathsf{wt}_N(M)\le-k_M\) for some \(M\in\mathcal{M}_N\) is present.

Since \(\mathcal{M}_N\cap\mathcal{M}_{N^\prime}=\emptyset\) for \(N'\neq N\) in N (from property (3)), any such minimal system contains at least \(|\mathcal{N}|=2^k=2^{\Theta(m)}\) inequalities. The lower bound in Theorem 4 follows from the fact that inequalities in a minimal system are in one-to-one correspondence with the facets of the polyhedron they describe, see e.g. \[8, Theorem 3.30\]. This finishes the proof of Theorem 4.

