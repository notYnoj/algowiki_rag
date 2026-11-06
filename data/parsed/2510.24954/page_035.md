## D Omitted Proofs

### D.1 Proof of Lemma 2.5

**Lemma 2.5** (Cf. \[Hes03\])**.** _Let_ \(G\in\mathcal{G}_k\) _with critical pair set P._

• \(|P|=\frac{N\Delta^kr^{dk}}{(r+1)^{dk}}\) .<tbc>

• _Every critical pair_ \((s,t)\in P\) _has a unique s-t path P<sub>s,t</sub> in G, called its_ critical path.<tbc>

• _If two critical paths intersect at_ \(u\in L_i\) _and_ \(v\in L_{i^\prime}\) _then_ \(i'<i+k\).

_Proof._ Each vertex \(((0,0),(p_0,\dots,p_{k-1}))\in S\) is part of \(\Delta^k\) critical pairs because for any critical direction \((\vec{v}_0,\dots,\vec{v}_{k-1})\in\mathcal{B}(r,d)^k\), we have that \(((\ell,0),(p_0+\ell\vec{v}_0,\dots,p_{k-1}+\ell\vec{v}_{k-1}))\in L_{\ell,0}\) is a valid vertex in \(L_{\ell,0}\), since \(p_j+\ell\vec{v}_j\in(-(r+1)r\ell,(r+1)r\ell]^d\). Additionally, the number of vertices in _S_ is at least \(|S|=(2r^2\ell)^{dk}=\frac{Nr^{dk}}{(r+1)^{dk}}\). We conclude that the total number of critical pairs is \(\frac{N\Delta^kr^{dk}}{(r+1)^{dk}}\) .

Turning to the uniqueness claim, if \((s,t)\in P\) is an arbitrary critical pair we can write

\(s=((0,0),(p_0,\dots,p_{k-1}))\in S\)<br>
\(t=((\ell,0),(p_0+\ell\vec{v}_0,\dots,p_{k-1}+\ell\vec{v}_{k-1}))\in L_{\ell,0},\)

One _s-t_ path _P<sub>s,t</sub>_ passes through all vertices of the form<tbc>

\(((i,j),(p_0+(i+1)\vec{v}_0,\dots,p_{j-1}+(i+1)\vec{v}_{j-1},p_j+i\vec{v}_j,\dots,p_{k-1}+i\vec{v}_{k-1})).\)

<tbc>We claim that _P<sub>s,t</sub>_ is the unique _s-t_ path in _G_. By construction, any _s-t_ path \(P'\) in _G_ can be identified with a sequence of \(k\ell\) vectors \(\vec{u}_{0,0},\dots,\vec{u}_{\ell-1,k-1}\) corresponding to the edges of \(P'\) that satisfies

\(\forall j\in[0,k),\sum_{i=0}^{\ell-1}\vec{u}_{i,j}=\ell\vec{v}_j.\)

However, if any \(\vec{u}_{i,j}\neq\vec{v}_j\) then \((\sum_i\vec{u}_{i,j})/\ell\) is not an extreme point on the convex hull B(_r,d_), and therefore cannot be equal to \(\vec{v}_j\). Thus \(\vec{u}_{i,j}=\vec{v}_j\) and \(P'=P_{s,t}\).

Since each critical pair is connected by a unique path, we can refer to it as a _critical path_. The last claim follows since any _k_ consecutive edges along a critical path uniquely determines its critical direction \((\vec{v}_0,\dots,\vec{v}_{k-1})\), which uniquely determines its first vertex in _L_<sub>0,0</sub> and last vertex in \(L_{\ell,0}\).

