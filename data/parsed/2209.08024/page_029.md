## B Centroid and median

**Lemma 2.3.** _Let_ T _be a graph and w be a weight function on V_(T)_. For each_ \(u\in V(\mathcal{T})\)_, define_ \(W(u)=\sum_{v\in V(\mathcal{T})}d_\mathcal{T}(u,v)\cdot w(v)\)_, where d_<sub>T</sub>(_u,v_) _denotes the number of edges on the path from u to v in_ T _. Then_ \(c\in V(\mathcal{T})\) _is a centroid of_ (T_,w_) _if and only if W(c_) _is minimal._

_Proof._ Let \(u\in V(\mathcal{T})\) minimize _W(u_), and suppose there is a component \(\mathcal{H}\in\mathbb{C}(\mathcal{T}-u)\) with \(w(\mathcal{H})>\frac{1}{2}w(\mathcal{T})\). Let _v_ be the neighbor of _u_ in H. For each \(x\in V(\mathcal{T})\), we have _d_<sub>T</sub>(_v,x_)=_d_<sub>T</sub>(_u,x_)-1 if \(x\in V(\mathcal{H})\), and _d_<sub>T</sub>(_v,x_)=_d_<sub>T</sub>(_u,x_)-1 otherwise. Thus, _W(v_)=_W(u_)+_w_(T-H)-_w_(H)_\<W(u_), a contradiction.

On the other hand, let _c_ be a centroid of (T_,w_), and let \(u\in V(\mathcal{T})-\{c\}\). We show that \(W(u)\ge W(c)\). Let _c=u_<sub>1</sub>_,u_<sub>2</sub>_,...,u<sub>k</sub>=u_ be the path from _c_ to _u_ in T . We claim that \(W(u_i)\le W(u_{i+1})\) for all \(i\in[k-1]\). This in particular implies \(W(c)\le W(u)\), as desired.

Towards our claim, let \(i\in[k-1]\), and let H_<sub>i</sub>_ be the component of T-_u_<sub>_i_+1</sub> that contains _u<sub>i</sub>_ (see Figure 11). Note that H_<sub>i</sub>_ encompasses _c_ and all but one component of C(T-_c_), so \(w(\mathcal{H}_i)\ge\frac{1}{2}w(\mathcal{T})\). For each \(x\in V(\mathcal{T})\), we have _d_<sub>T</sub>(_u<sub>i</sub>,x_)=_d_<sub>T</sub>(_u_<sub>_i_+1</sub>_,x_)-1 if \(x\in V(\mathcal{H}_i)\), and _d_<sub>T</sub>(_v,u<sub>i</sub>_)=_d_<sub>T</sub>(_u,u_<sub>_i_+1</sub>)+1 otherwise. Thus, _W(u<sub>i</sub>_)-_W(u_<sub>_i_+1</sub>)+_W_(H_<sub>i</sub>_)+\(W(\mathcal{T}-\mathcal{H}_i)\le W(u_{i+1})\). This concludes the proof

## C Tie-breaking

**Lemma 2.4.** _Let_ T _be a tree,_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\) _a weight function and let C be a centroid tree of_ (T_,w). For every_ \(\varepsilon>0\) _there exists a weight function_ \(w':V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\) _such that C is the unique centroid tree of_ \((\mathcal{T},w')\) _and_ \(\|w'-w\|_\infty<\varepsilon\).

We prove Lemma 2.4 by the following series of simple observations.

**Observation C.1.** _Let_ \(w_1,w_2:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\) _be two weight functions. Assume that a vertex_ \(c\in V(\mathcal{T})\) _is a centroid of both_ (T_,w_<sub>1</sub>) _and_ (T_,w_<sub>2</sub>)_. Assume further that c is the unique centroid of_ (T_,w_<sub>2</sub>)_. Then c is the unique centroid of_ (T_,w_<sub>1</sub>+_w_<sub>2</sub>).

_Proof._ Denote \(W_i(u)=\sum_{v\in V(\mathcal{T})}d_\mathcal{T}(u,v)\cdot w_i(v)\). If _c_ is a minimum of _W_<sub>1</sub> and is the unique minimum of _W_<sub>2</sub>, then it is the unique minimum of _W_<sub>1</sub>+_W_<sub>2</sub>, and by Lemma 2.3 it is a unique centroid of (T_,w_<sub>1</sub>+_w_<sub>2</sub>).

**Observation C.2.** _Let_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\) _and m=w_(T)_. If_ \(w(u)\ge m/2\) _then u is a centroid of_ (T_,w). Moreover, if w(u)\>m/_2_, then u is the unique centroid of_ (T_,w)._

_Proof. u_ is a centroid since the total weight of T-_u_ is \(\le m/2\). Assume _w(u)\>m/_2 and let \(v\neq u\). The connected component of T-_v_ in which _u_ is has weight _\>m/_2, therefore _v_ is not a centroid.

**Observation C.3.** _Let T be a search tree on_ T _. There exists a_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\) _such that T is the unique centroid tree of_ (T_,w)._

_Proof._ By induction on _n_. When _n_=1 every _w_ has the desired property. Assume _n\>_1. Let _r_=`root`(_T_) and let _T_<sub>1</sub>_,...,T<sub>d</sub>_ be the subtrees of _T_ rooted at the children of _r_. Let T_<sub>i</sub>_=T\[_V(T<sub>i</sub>_)\]. By the induction hypothesis there are \(w_i:V(\mathcal{T}_i)\rightarrow\mathbb{R}_{\ge 0}\) such that _T<sub>i</sub>_ is the unique centroid tree of (T_<sub>i</sub>,w<sub>i</sub>_). Let \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\) be defined by<tbc>

\(w(u)=\left\{\begin{array}{ c c }
w_i(u), & u\in V(\mathcal{T}_i) \\
1+\sum_{i=1}^dw_i(\mathcal{T}_i), & u=r.
\end{array}\right.\)

C
u2
ui
ui+1
u
Hi

Figure 11: An illustration of the second part of Lemma 2.3.

