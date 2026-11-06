- Set cost(_e_)=0 where _e_ is any of the _u-v_, \(u'\)-\(v'\), and \(u''\)-\(v''\) edges.<tbc>

- Set cost(_e_)=0 where _e_ is an intra-gadget edge of any literal.<tbc>

**-** For all other edges _e_, set cost(_e_)=1.

In particular, for all edges _e_ incident to _s_ and _t_, we have cost(_e_)=1. Similarly, for any edge _e_ between _r_’s gadget and \(\neg r\)’s gadget for any variable _r_, we have cost(_e_)=1. In our figures all dashed edges have cost 1 and the solid edges have cost 0.

**Theorem 13.** _If_ \(\psi\) _is satisfiable then_ \(G_\psi\) _admits a quasi-popular matching M with_ cost(_M_)=0.

_Proof._ There is a natural way of constructing the matching _M_ in our instance \(G_\psi\). Include all _u-v_, \(u'\)-\(v'\), and \(u''\)-\(v''\) edges in _M_. Then, we will use the satisfying assignment for \(\psi\) to choose edges from each literal gadget. For any variable \(r\in\{X_1,\dots,X_{2n}\}\):

- if _r_=true then take the pair of edges \((c_r,d_r),(c'_r,d'_r)\) from \(\neg r\)’s gadget and the pair of edges \((a_{r,i},b'_{r,i})\), \((a'_{r,i},b_{r,i})\) from _r_’s gadget in clause _i_ (for every clause that _r_ belongs to).<tbc>

**-** if _r_=false then take the pair of edges \((c_r,d'_r),(c'_r,d_r)\) from \(\neg r\)’s gadget and the pair of edges (_a<sub>r,i</sub>,b<sub>r,i</sub>_), \((a'_{r,i},b'_{r,i})\) from _r_’s gadget in clause _i_ (for every clause that _r_ belongs to).

It is easy to see that cost(_M_)=0. We will now show a witness \(\alpha\in\{0,\pm 1,\pm 2\}^n\) to prove \(u(M)\le 2\). Since _s_ and _t_ are unmatched in _M_, we will set \(\alpha_s=\alpha_t=0\). This will ensure that \(\alpha_u\ge g_M(u,u)\) for all vertices _u_ since \(\alpha_v=0=g_M(v,v)\) for \(v\in\{s,t\}\) while \(\alpha_u\ge-2=g_M(u,u)\) for all vertices _u_ matched in _M_.

We now set \(\alpha\)-values for vertices matched in _M_. Consider any negative clause, say \(D_k=\neg x\vee\neg y\). Note that a satisfying assignment sets exactly one of _x,y_ to be true (this is by our transformation of the formula \(\psi\): if _x=X<sub>i</sub>_ then \(y=X_{n+i}=\neg X_i\)). Thus we have two cases here: either (i) _x_=true and _y_=false, or (ii) _x_=false and _y_=true.

Let \(c_x,d_x,c'_x,d'_x\) be the 4 vertices in \(\neg x\)’s gadget and let \(c_y,d_y,c'_y,d'_y\) be the 4 vertices in \(\neg y\)’s gadget. The \(\alpha\)-values of these 8 vertices along with those of \(u_k,v_k,u'_k,v'_k\) in cases (i) and (ii) are given below.

