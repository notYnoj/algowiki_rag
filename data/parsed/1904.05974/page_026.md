Consider case (ii): here the edge \((a_x,b_x)\in M\). So the edge \((a_x,v_\ell)\) is a blocking edge to _M_ and we have \(\alpha_{a_x}=\alpha_{v_\ell}=1\).

- We have the edges \((a_y,b'_y)\) and \((a'_y,b_y)\) in _M_, thus \(g_M(b_x,u'_\ell)=g_M(a_y,v'_\ell)=g_M(b_y,u''_\ell)=-1\). It is easy to check that all these edges are covered.<tbc>

- If \(z=\mathsf{false}\), then \(g_M(a_z,v''_\ell)=2=\alpha_{a_z}+\alpha_{v_\ell^{\prime\prime}}\); else \(g_M(a_z,v''_\ell)=-1\le\alpha_{a_z}+\alpha_{v_\ell^{\prime\prime}}\).

Consider case (iii): here the edges (_a<sub>x</sub>,b<sub>x</sub>_) and (_a<sub>y</sub>,b<sub>y</sub>_) are in _M_. So both \((a_x,v_\ell)\) and \((a_y,v'_\ell)\) are blocking edges to _M_. We have \(\alpha_{a_x}=\alpha_{v_\ell}=1\) and \(\alpha_{a_y}=2\) and \(\alpha_{v_\ell^\prime}=0\). So the blocking edges are covered.

- We also have \(g_M(b_x,u'_\ell)=g_M(b_y,u''_\ell)=-1\) and we set \(\alpha_{b_x}=-1,\alpha_{u_\ell^\prime}=0\) along with \(\alpha_{b_y}=-2,\alpha_{u_\ell^{\prime\prime}}=1\). Thus these edges are covered.<tbc>

**-** Finally, \(g_M(a_z,v''_\ell)=-1\) and we set \(\alpha_{a_z}=0\) and \(\alpha_{v_\ell^{\prime\prime}}=-1\). Thus all link edges are covered. \(\sqcap\sqcup\)

Claim 4 below shows that edges between _r_’s gadget and \(\neg r\)’s gadget, for any variable _r_, are also covered.

**Claim 4** _For any variable r, edges between r’s gadget and_ \(\neg r\)_’s gadget are covered._

_Proof._ Suppose _r_=false in this assignment. So the edges \((a_r,b_r),(a'_r,b'_r)\), and \((c_r,d'_r)\) are in _M_. Note that \(\alpha_{c_r}=1\) and \(\alpha_{d_r^\prime}=-1\); moreover \(\alpha_{b_r}\ge-2\). We have _g<sub>M</sub>(b<sub>r</sub>,c<sub>r</sub>_)=-1, thus \(\alpha_{b_r}+\alpha_{c_r}\ge-1=g_M(b_r,c_r)\). It is easy to check that, by construction of \(\alpha\)-values, when _r_=false, we have \(\alpha_{a_r^\prime}\ge 0\). We have \(g_M(a'_r,d'_r)=-1\), so \(\alpha_{a_r^\prime}+\alpha_{d_r^\prime}\ge-1=g_M(a'_r,d'_r)\).

Suppose _r_=true in this assignment. So the edges \((a'_r,b_r),(c_r,d_r)\), and \((c'_r,d'_r)\) are in _M_. Note that \(\alpha_{c_r}=-1\) and \(\alpha_{d_r^\prime}=1\); moreover \(\alpha_{a_r^\prime}\ge-2\) (in fact, \(\alpha_{a_r^\prime}\ge-1\)). Thus \(\alpha_{a_r^\prime}+\alpha_{d_r^\prime}\ge-1=g_M(a'_r,d'_r)\). It is easy to check that when _r_=true, we have \(\alpha_{b_r}\ge 0\), thus \(\alpha_{b_r}+\alpha_{c_r}\ge-1=g_M(b_r,c_r)\). \(\sqcap\sqcup\)

Thus \(\alpha\) is a feasible solution to (LP4). Moreover, \(\sum_w\alpha_w=0\) since for each edge \((p,q)\in M\), we have \(\alpha_p+\alpha_q=0\), also \(\alpha_s=\alpha_t=0\). This finishes the proof of Theorem 13. \(\sqcap\sqcup\)

**The Converse.** We also need to show that if \(G_\psi\) admits a quasi-popular matching of cost 0, then \(\psi\) admits a satisfying assignment. This is the easy side of the reduction.

**Lemma 7.** _Let M be any quasi-popular matching in_ \(G_\psi\) _with_ cost(_M_)=0_. Then M contains all u-v,_ \(u'\)_-v’, and_ \(u''\)_-v" edges. For any_ \(r\in\{X_1,\dots,X_{2n}\}\)_, we have:_

1. _From a gadget of r (on vertices_ \(a_r,b_r,a'_r,b'_r\)_), either (i)_ \((a_r,b'_r),(a'_r,b_r)\) _are in M or (ii)_ (_a<sub>r</sub>,b<sub>r</sub>), \((a'_r,b'_r)\) _are in M._<tbc>

- _If (i) happens, we say that r is in_ true state_. If (ii) happens, we say that r is in_ false state.<tbc>

_2._ _From a gadget of_ \(\neg r\) _(on vertices_ \(c_r,d_r,c'_r,d'_r\)_), either (i)_ \((c_r,d'_r),(c'_r,d_r)\) _are in M or (ii)_ (_c<sub>r</sub>,d<sub>r</sub>),_ \((c'_r,d'_r)\) _are in M._<tbc>

**-** _If (i) happens, we say that_ \(\neg r\) _is in_ true state_. If (ii) happens, we say that_ \(\neg r\) _is in_ false state.<tbc>

_3._ _r and_ \(\neg r\) _cannot be simultaneously in true state._

_Proof._ Since cost(_M_)=0, _M_ is forbidden to use any edge other than the _u-v_ edges, the \(u'\)-\(v'\) edges, the \(u''\)-\(v''\) edges, and the 4 edges in the gadget of any literal. Moreover, since _M_ is quasi-popular, _M_ cannot leave two adjacent vertices unmatched. Thus _M_ contains all _u-v_ edges, \(u'\)-\(v'\) edges, and \(u''\)-\(v''\) edges; similarly, points 1 and 2 follow.

The preferences of the vertices are set such that if both \((a'_r,b_r)\) and \((c_r,d'_r)\) are in _M_ then the alternating cycle \(\rho=a'_r-b_r-c_r-d'_r-a'_r\) has a blocking edge (_b<sub>r</sub>,c<sub>r</sub>_) in it.

Consider \(M\oplus\rho\) versus _M_. The 3 vertices _b<sub>r</sub>,c<sub>r</sub>_, and \(d'_r\) prefer \(M\oplus\rho\) to _M_ while the vertex \(a'_r\) prefers _M_ to \(M\oplus\rho\). This means _M_’s unpopularity factor is at least 3, i.e., \(u(M)\ge 3\). However _M_ is quasi-popular, i.e., \(u(M)\le 2\), thus both \((a'_r,b_r)\) and \((c_r,d'_r)\) cannot simultaneously be in _M_ for any \(r\in\{X_1,\dots,X_{2n}\}\). \(\sqcap\sqcup\)<tbc>

