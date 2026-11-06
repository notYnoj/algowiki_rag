_Equivalently, there exists a probability distribution_ \(\mathcal{D}=\{y_F\}_{F\in\mathcal{F}_{2w}(T)}\) _over_ F<sub>2_w_</sub>(_T_) _such that_

\(\sum_{F\in\mathcal{F}_{2w}(T)e\in F}y_F\le\frac{1}{w}\forall e\in E(T).\) (5)

_Proof._ Root the tree _T_ at an arbitrary vertex \(r\in V(T)\). For _i_=0_,...,w_-1, define<tbc>

\(F_i=\{e\in E(T)|d(r,e)=i+kw\text{for some}k\in\mathbb{Z}_{\ge 0}\}.\)

<tbc>Set \(y_{F_i}=\frac{1}{w}\) for each _i_=0_,...,w_-1, and _y<sub>F</sub>_=0 otherwise. Note that the sets _F<sub>i</sub>_ partition _E(T_): we have \(E(T)=\bigcup_{i=0}^{w-1}F_i\) and \(F_i\cap F_j=\varnothing\) for \(i\neq j\). Thus,<tbc>

\(\sum_{F\in\mathcal{F}_{2w}(T)e\in F}y_F=\sum_{i=0e\in F_i}^{w-1}y_{F_i}=\frac{1}{w},\forall e\in E(T).\)

<tbc>It remains to show that each _F<sub>i</sub>_ is a valid 2_w_-diameter decomposition. Fix _F<sub>i</sub>_, and consider a pair of vertices (_u,v_) with \(d(u,v)\ge 2w\). Let _q_ be the lowest common ancestor of _u_ and _v_. The unique _u-v_ path consists of the _u-q_ path and the _q-v_ path. Since \(d(u,v)\ge 2w\), one of these subpaths has length at least _w_. Without loss of generality, suppose \(d(q,v)\ge w\), and denote this path by _Q=e_<sub>0</sub>_,e_<sub>1</sub>_,...,e<sub>p</sub>_. Because _q_ is an ancestor of _v_, we have _d(r,e<sub>i</sub>_)=_d(r,e_<sub>_i_-1</sub>)+1 for _i_=1_,...,p_. Hence there exists some \(e_j\in Q\) such that \(d(r,e_j)\equiv i(modw)\), i.e., \(e_j\in F_i\). Removing _F<sub>i</sub>_ therefore separates _u_ and _v_, as required. This shows that _F<sub>i</sub>_ defines a 2_w_-diameter decomposition, and hence D is a valid _SDD(T,_2_w,_1_/w_).

The 2_w_-diameter decompositions _F_<sub>0</sub>_,...,F_<sub>_w_-1</sub> described in the proof of Theorem 3 will be useful in the remainder of the paper, so we record a formal definition.

**Definition 3.** _Let_ \(w\in\mathbb{N}\)_, and let T be a tree with a distinguished root vertex_ \(r\in V(T)\)_. For each i_=0,1_,...,w_-1_, define_<tbc>

\(F_w^i(T,r):=\{e\in E(T)|d_T(r,e)\equiv i(modw)\},\)

<tbc>_where d<sub>T</sub>(r,e_) _denotes the distance from r to the closer endpoint of e. Then_ \(\{F_w^i(T,r)\}_{i=0}^{w-1}\) _forms a partition of E(T). Moreover, each_ \(F_w^i(T,r)\) _defines a_ 2_w-diameter decomposition of T, and the connected component containing the root r has radius at most i from r, that is,_

\(rad_{F_w^i(T,r)}(r)\le i\le w-1.\)

Thus, the _SDD(T,_2_w,_1_/w_) constructed in the proof of Theorem 3 also satisfies this useful structural property, which we highlight next.

**Observation 1.** _For the_ 2_w-diameter decompositions F_<sub>0</sub>_,...,F_<sub>_w_-1</sub> _described in the proof of Theorem 3, the following properties hold:_

1. _For every i_=0_,...,w_-1_, we have_<tbc>

<tbc>\(rad_{F_i}(r)\le i\le w-1.\)<tbc>

<tbc>_Equivalently,_<tbc>

<tbc>\(\sum_{F:rad_F(r)\le w-1}y_F=1.\)<tbc>

