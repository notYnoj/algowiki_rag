Lemma 7 indicates a natural way of defining an assignment for \(\psi\) using a matching _M_ with cost 0 and unpopularity factor at most 2.

**Lemma 8.** _If_ \(G_\psi\) _has a quasi-popular matching M with_ cost(_M_)=0 _then_ \(\psi\) _is satisfiable._

_Proof._ For any variable \(r\in\{X_1,\dots,X_{2n}\}\) consider the edges in \(\neg r\)’s gadget that are in _M_. If \((c_r,d'_r)\) and \((c'_r,d_r)\) are in _M_ then set _r_=false else set _r_=true.

Lemma 7 tells us that when _r_=false then for every clause _i_ that _r_ is present in, the edges (_a<sub>r,i</sub>,b<sub>r,i</sub>_) and \((a'_{r,i},b'_{r,i})\) from _r_’s gadget in the _i_-th clause are in _M_ (where \(a_{r,i},b_{r,i},a'_{r,i},b'_{r,i}\) are the 4 vertices from _r_’s gadget in the _i_-th clause). We now need to show that every clause has at least one literal set to true. Suppose not. We have 3 cases here.

1. Let \(C_i=x\vee y\vee z\). Suppose _x,y,z_ are in false state. Consider the alternating path \(\rho\) wrt _M_:<tbc>

<tbc>\(s-(u_i,v_i)-(a_{x,i},b_{x,i})-(u'_i,v'_i)-(a_{y,i},b_{y,i})-(u''_i,v''_i)-(a_{z,i},b_{z,i})-t.\)<tbc>

<tbc>In the election between \(M\oplus\rho\) and _M_, the 10 vertices \(s,v_i,a_{x,i},b_{x,i},v'_i,a_{y,i},b_{y,i},v''_i,a_{z,i}\), and _t_ vote for \(M\oplus\rho\) while the 4 vertices \(u_i,u'_i,u''_i\), and _b<sub>z,i</sub>_ vote for _M_. Thus \(\phi(M\oplus\rho,M)=10\) and \(\phi(M,M\oplus\rho)=4\). Hence \(u(M)\ge 10/4\) contradicting that \(u(M)\le 2\).<tbc>

2. Let \(C_j=x\vee y\), i.e., this is a positive clause with 2 literals. Suppose both _x_ and _y_ are in false state. Consider the following alternating path \(\rho\) wrt _M_:<tbc>

<tbc>\(s-(u_j,v_j)-(a_{x,j},b_{x,j})-(u'_j,v'_j)-(a_{y,j},b_{y,j})-t.\)<tbc>

<tbc>In the election between \(M\oplus\rho\) and _M_, the 7 vertices \(s,v_j,a_{x,j},b_{x,j},v'_j,a_{y,j}\), and _t_ vote for \(M\oplus\rho\) while the 3 vertices \(u_j,u'_j\), and _b<sub>y,j</sub>_ vote for _M_. Thus \(\phi(M\oplus\rho,M)=7\) and \(\phi(M,M\oplus\rho)=3\). Hence \(u(M)\ge 7/3\) contradicting that \(u(M)\le 2\).<tbc>

3. Let \(D_k=\neg x\vee\neg y\). Suppose both \(\neg x\) and \(\neg y\) are in false state. Consider the following alternating path \(\rho\) wrt _M_:<tbc>

<tbc>\(s-(c_x,d_x)-(u_k,v_k)-(c_y,d_y)-(u'_k,v'_k)-t.\)<tbc>

<tbc>In the election between \(M\oplus\rho\) and _M_, the 7 vertices \(s,d_x,u_k,c_y,d_y,u'_k\), and _t_ vote for \(M\oplus\rho\) while the 3 vertices _c<sub>x</sub>,v<sub>k</sub>_, and \(v'_k\) vote for _M_. Thus \(\phi(M\oplus\rho,M)=7\) and \(\phi(M,M\oplus\rho)=3\). Hence \(u(M)\ge 7/3\) contradicting that \(u(M)\le 2\). \(\sqcap\sqcup\)

This finishes the proof of correctness of our reduction. Hence Theorem 1 follows.

## 6 Lower Bounds on the Extension Complexity

We prove Theorem 3 in this section. Recall that, given polytopes \(\mathcal{P}_1\subseteq\mathbb{R}^k\), \(\mathcal{P}_2\subseteq\mathbb{R}^\ell\) and an affine map \(f:\mathbb{R}^\ell\rightarrow\mathbb{R}^k\) such that _f_(P<sub>2</sub>)=P<sub>1</sub>, we say that P<sub>2</sub> is an _extension_ of P<sub>1</sub>. The number of facets of P<sub>2</sub> (or equivalently, the number of inequalities in a minimal linear description of P<sub>2</sub> that are not valid at equality) is its _size_, and the minimum size of an extension of P<sub>1</sub> is the _extension complexity_ of P<sub>1</sub>, denoted by _xc_(P<sub>1</sub>).

Our starting point in the proof of Theorem 3 is the following lower bound on the extension complexity of the independent set polytope. Let I_<sub>H</sub>_ be the independent set polytope of a graph _H_.

**Theorem 14 (\[20\]).** _There exists an (explicitly constructed) family of graphs H_=(_V<sub>H</sub>,E<sub>H</sub>_) _with bounded degree such that_ \(xc(\mathcal{I}_H)=2^{\Omega(n_H/logn_H)}\)_, where_ |_V<sub>H</sub>_|=_n<sub>H</sub>._

