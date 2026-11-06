Two vertices of _A<sub>G</sub>_ are adjacent if and only if they are incompatible. In particular, \((c,\ell)\) and \((\ell,c)\) are adjacent, so an independent set cannot select both orientations of one edge. The first coordinate specifies the centre of a selected star and the second specifies a leaf; for a single-edge component, either endpoint may serve as its centre.

**Lemma 2** (\[13\])**.** _For every graph G,_ \(\rho_\mathrm{e}^\mathrm{o}(G)=\alpha(A_G)\).

_Proof._ For completeness, let _D_ be an edge open packing. By Observation 1, the connected components of _G_\[_V(D_)\] are stars. Orient their edges from centre to leaf, choosing either centre for each _K_<sub>2</sub>. The resulting |_D_| oriented edges satisfy the two compatibility rules and form an independent set in _A<sub>G</sub>_. Conversely, an independent set _I_ contains at most one orientation of each edge. Its members with a common first coordinate describe a star with pairwise nonadjacent leaves. Those with different first coordinates have disjoint endpoint sets with no edge between them. Thus their |_I_| underlying edges form an edge open packing, proving the equality.

For example, let _G=C_<sub>5</sub> with vertices _v_<sub>0</sub>_,...,v_<sub>4</sub> in cyclic order, and read subscripts modulo five. Write _a<sub>i</sub>_=(_v<sub>i</sub>,v_<sub>_i_-1</sub>) and _b<sub>i</sub>_=(_v<sub>i</sub>,v_<sub>_i_+1</sub>). The pair _a<sub>i</sub>,b<sub>i</sub>_ is compatible for each _i_. Oriented edges with different centres are incompatible, since _C_<sub>5</sub> has no induced 2_K_<sub>2</sub>. Hence <o>_A<sub>G</sub>_</o>=5_K_<sub>2</sub>, or equivalently _A<sub>G</sub>=K_<sub>2,2,2,2,2</sub>, with parts {_a<sub>i</sub>,b<sub>i</sub>_}. In particular, \(\rho_\mathrm{e}^\mathrm{o}(C_5)=\alpha(A_{C_5})=2\). Figure 2 shows the complement to display the compatibility pairs without drawing all forty conflict edges.

## 3.2 Preservation of AT-freeness

**Theorem 3.** _If G is AT-free, then A<sub>G</sub> is AT-free._

_Proof._ We prove the contrapositive. Suppose that _A<sub>G</sub>_ contains an asteroidal triple {_e_<sub>1</sub>_,e_<sub>2</sub>_,e_<sub>3</sub>}, where \(e_i=(c_i,\ell_i)\) for \(i\in\{1,2,3\}\). Since the three vertices are pairwise nonadjacent in _A<sub>G</sub>_, the corresponding oriented edges are pairwise compatible. Therefore, \(\ell_1,\ell_2,\ell_3\) are distinct and pairwise nonadjacent in _G_.

We show that \(\{\ell_1,\ell_2,\ell_3\}\) is an asteroidal triple in _G_. Fix distinct \(i,j,k\in\{1,2,3\}\). Since {_e_<sub>1</sub>_,e_<sub>2</sub>_,e_<sub>3</sub>} is an asteroidal triple in _A<sub>G</sub>_, there is an _e<sub>i</sub>-e<sub>j</sub>_ path in _A<sub>G</sub>_ avoiding _N<sub>A<sub>G</sub></sub>_\[_e<sub>k</sub>_\]. Write this path as _P=e<sub>i</sub>=f_<sub>0</sub>_,f_<sub>1</sub>_,...,f<sub>t</sub>=e<sub>j</sub>_, where _f<sub>s</sub>_=(_a<sub>s</sub>,b<sub>s</sub>_), and write \(e_k=(c_k,\ell_k)\). For \(0\le s\le t\), put _R<sub>s</sub>_={_b<sub>s</sub>_} if _a<sub>s</sub>=c<sub>k</sub>_, and _R<sub>s</sub>_={_a<sub>s</sub>,b<sub>s</sub>_} otherwise.

Every vertex _f<sub>s</sub>_ of _P_ is compatible with _e<sub>k</sub>_. If _a<sub>s</sub>=c<sub>k</sub>_, then compatibility of (_c<sub>k</sub>,b<sub>s</sub>_) and \((c_k,\ell_k)\) gives \(b_s\neq\ell_k\) and \(b_s\ell_k\notin E(G)\). If \(a_s\neq c_k\), compatibility gives \(a_s,b_s\notin N_G[\ell_k]\). Hence, \(R_s\cap N_G[\ell_k]=\varnothing\) for every _s_.

We next claim that consecutive sets _R<sub>s</sub>_ and _R_<sub>_s_+1</sub> touch in _G_; that is, they intersect or an edge of _G_ has one endpoint in each set. Suppose otherwise. Write _f<sub>s</sub>_=(_a,b_) and _f_<sub>_s_+1</sub>=(_d,r_). If _a=d=c<sub>k</sub>_, then _R<sub>s</sub>_={_b_} and _R_<sub>_s_+1</sub>={_r_}; the assumption gives \(b\neq r\) and \(br\notin E(G)\), so the two oriented edges are compatible by the same-centre rule. If \(a=d\neq c_k\), then both sets contain _a_, contrary to their being disjoint.

Now suppose that \(a\neq d\). If neither _a_ nor _d_ equals _c<sub>k</sub>_, then _R<sub>s</sub>_={_a,b_} and _R_<sub>_s_+1</sub>={_d,r_}. Their disjointness and the absence of an edge between them show that _a,b,d,r_ are distinct and that all four cross edges are absent. Thus, _f<sub>s</sub>_ and _f_<sub>_s_+1</sub> are compatible. If _a=c<sub>k</sub>_, then _R<sub>s</sub>_={_b_} and _R_<sub>_s_+1</sub>={_d,r_}. The assumption gives \(b\neq d,r\) and \(bd,br\notin E(G)\). Compatibility of (_d,r_) with \((c_k,\ell_k)\) gives \(c_k\neq d,r\) and \(c_kd,c_kr\notin E(G)\). Again the two oriented edges are compatible. The case _d=c<sub>k</sub>_ is symmetric.

V0
a0
a1
a2
a3
a4
V4
V1
V3
V2
bo
b1
b2
b3
b4
(a) =C5
(b) = =

Figure 2: The cycle _C_<sub>5</sub> and the complement of its oriented star-conflict graph. Each edge on the right joins compatible orientations; all other pairs are adjacent in _A<sub>G</sub>_. The highlighted pair _a_<sub>0</sub>_,b_<sub>0</sub> represents the highlighted maximum edge open packing on the left.

