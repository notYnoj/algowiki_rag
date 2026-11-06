1 \(\bar{w}(e)\leftarrow w_{in}(e)\cdot 2n\) for all \(e\in E\), \(\bar{G}\leftarrow(V,E,\bar{w})\), \(B\leftarrow 2n\). `// scale up edge weights` 2 Round _B_ up to nearest power of 2 `// still have` \(\bar{w}(e)\ge-B\) `for all` \(e\in E\) 3 \(\phi_0(v)=0\) for all \(v\in V\) `// identity price function` 4 `for` _i_=1 _to t_:=log<sub>2</sub>(_B_) **do** 5 \(\psi_i\leftarrow\) Scale\(\mathrm{Down}(\bar{G}_{\phi_{i-1}},\Delta:=n,B/2^i)\) 6 \(\phi_i\leftarrow\phi_{i-1}+\psi_i\) `// (Claim 5.1)` \(w_{\phi_i}(e)\ge-B/2^i\) `for all` \(e\in E\) 7 \(G^*\leftarrow(V,E,w^*)\) where \(w^*(e)\leftarrow\bar{w}_{\phi_t}(e)+1\) for all \(e\in E\). `// Observe:` _G_<sup>∗</sup> `in above line has non-negative weights` 8 Compute a shortest path tree _T_ from _s_ using Dijkstra(_G_<sup>∗</sup>_,s_) (Lemma 3.1) `// (Claim 5.3) Will Show: any shortest path in` _G_<sup>∗</sup> `is also shortest in` _G_ 9 `return` shortest path tree _T_ .

**Corollary 5.2.** _If G<sub>in</sub> contains a negative-weight cycle then the algorithm does not terminate._

_Proof._ Say, for contradiction, that the algorithm terminates; then by Claim 5.1 we have that \(\bar{w}_{\phi_t}(e)\ge-1\). Now, let _C_ be any negative-weight cycle in _G<sub>in</sub>_. Since all weights in \(\bar{G}\) are multiples of 2_n_ (Line 1), we know that \(\bar{w}(C)\le-2n\). But we also know that \(\bar{w}_{\phi_t}(C)\ge-|C|\ge-n\). So \(\bar{w}(C)\neq\bar{w}_{\phi_t}(C)\), which contradicts Lemma 2.7.

Now we show that the algorithm produces a correct output.

**Claim 5.3.** _Say that G<sub>in</sub> contains no negative-weight cycle. Then, the algorithm terminates, and if P is a shortest sv-path in G_<sup>∗</sup> _(Line 7) then it is also a shortest sv-path in G<sub>in</sub>. Thus, the shortest path tree T of G_<sup>∗</sup> _computed in Line 9 is also a shortest path tree in G<sub>in</sub>._

_Proof._ The algorithm terminates because each call to Scale\(\mathrm{Down}(\bar{G}_{\phi_{i-1}},\Delta:=n,B/2^i)\) terminates, because \(\bar{G}_{\phi_{i-1}}\) is equivalent to _G<sub>in</sub>_ (Lemma 2.7) and so does not contain a negative-weight cycle. Now we show that

\(P\text{is also a shortest path in}\bar{G}_{\phi_t}\) (6)

which implies the claim because \(\bar{G}_{\phi_t}\) and _G<sub>in</sub>_ are equivalent. We assume that \(s\neq v\) because otherwise the claim is trivial. Observe that since all weights in \(\bar{G}\) are multiples of 2_n_ (Line 1), all shortest distances are also multiples of 2_n_, so for any two _sv_-paths _P<sub>sv</sub>_ and \(P'_{sv}\), \(|\bar{w}(P_{sv})-\bar{w}(P'_{sv})|\) is either 0 or _\>n_. It is easy to check that by Lemma 2.7, we also have that

\(|\bar{w}_{\phi_t}(P_{sv})-\bar{w}_{\phi_t}(P'_{sv})|\text{is either 0 or}>n.\) (7)

Moreover, by definition of _G_<sup>∗</sup> we have

\(\bar{w}_{\phi_t}(P_{sv})<w^*(P_{sv})=\bar{w}_{\phi_t}(P_{sv})+|P_{sv}|<\bar{w}_{\phi_t}(P_{sv})+n.\) (8)

Now, we prove (6) . Assume for contradiction that there was a shorter path \(P'\) in \(\bar{G}_{\phi_t}\). Then,

\(\bar{w}_{\phi_t}(P)-\bar{w}_{\phi_t}(P')>^\text{(7)}n.\) (9)

So, \(w^*(P')<^\text{(8)}\bar{w}_{\phi_t}(P')+n<^\text{(9)}\bar{w}_{\phi_t}(P)<^\text{(8)}w^*(P)\), contradicting _P_ being shortest in _G_<sup>∗</sup>.

**Algorithm 2:** Algorithm for SPmain(_G<sub>in</sub>_=(_V,E,w<sub>in</sub>),s<sub>in</sub>_)

