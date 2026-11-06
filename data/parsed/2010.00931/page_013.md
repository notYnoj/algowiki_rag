**Algorithm 1.** Transforming an arbitrary STT into a _k_-cut STT.

Input: search tree T on S, constant \(k\ge 3\), node \(x\in V(T)\).<br>
procedure Fix(T,x)<br>
   if x is a leaf then<br>
   return T<sub>x</sub><br>
   else if \(|\delta(T_x)|<k\) then<br>
   \(c_1,c_2,\dots,c_t\leftarrow\) children of x in T<br>
   return tree rooted at x with subtrees Fix(T,c<sub>1</sub>),...,Fix(T,c<sub>t</sub>)<br>
   else if \(|\delta(T_x)|\ge k\) then<br>
   \(v\leftarrow\) leaf centroid of \(\mathtt{ch}(\delta(T_x))\)<br>
   if \(v\neq x\) then<br>
Obtain<br>
\(T'\)<br>
from<br>
_T_<br>
by<br>
rotating<br>
_v_<br>
up<br>
to<br>
become<br>
the<br>
parent<br>
of<br>
_x_<br>
.<br>
   else<br>
   \(T'\leftarrow T\)<br>
   \(c'_1,c'_2,\dots c'_t\leftarrow\) children of v in \(T'\)<br>
   return tree rooted at v with subtrees \(\text{Fix}(T',c'_1),\dots,\text{Fix}(T',c'_t)\)

_Proof._ Observe that \(V(T_x)=V(T'_v)\). The set \(V(T'_c)\) is a connected component of the forest _S_\[_V(T<sub>x</sub>_)\]\\_v_. Let _U_ be the set of nodes _u_ such that \((u,w)\in\mathtt{cut}(V(T_x))\) for some \(w\in V(T'_c)\). Each \(u\in U\) is contained in \(\delta(T_x)\), so it is a leaf of \(S[\mathtt{ch}(\delta(T_x))]\) by Observation 6. Moreover, all \(u\in U\) are in the same component of \(S[\mathtt{ch}(\delta(T_x))\backslash v]\) (the one that contains _c_). As _v_ is a leaf centroid of \(S[\mathtt{ch}(\delta(T_x))]\), we have \(|U|\le\lfloor|\delta(T_x)|/2\rfloor\).

Finally, observe that \(\delta(T'_c)=U\cup\{v\}\) by Lemma 2 and the definition of _U_, so \(|\delta(T'_c)|=|U|+1\).

From Lemmas 4 and 5 and the fact that \(|\delta(T)|=0\), it follows inductively that in each recursive call Fix(_T,c_), the set _V(T<sub>c</sub>_) has boundary size at most _k_ (as \(\lfloor\frac{k}{2}\rfloor+1\le k\)).

## Depth increase.

We now bound the increase in depth due to the transformation for each node in _T_. Intuitively, when following the search path in the resulting tree _T_<sup>∗</sup>, we have a newly added node (compared to _T_) whenever the boundary size of the current tree is _k_, which by Lemma 5 can only happen every \(\lceil\frac{k}{2}\rceil-1\) steps. We proceed with the formal proof.

Let _T_ be a search tree on _S_ with root _r_ and let _T_<sup>∗</sup>=Fix(_T,r_). Let _P_ be the search path in _T_ of an arbitrary node _u_ and let \(P'=(u_1,u_2,\dots,u_t=u)\) be the search path of _u_ in _T_<sup>∗</sup>. Let \(i_1<i_2<\cdots<i_s\) be the indices of nodes in \(P'\) that are not in _P_. We want to show that the number of such nodes is

\(s\le\varepsilon_k|P|=\frac{|P|}{\lceil k/2\rceil-1}.\)

As `depth`<sub>_T_<sup>∗</sup></sub>(_u_)-`depth`_<sub>T</sub>(u_)=_s_ and |_P_|=`depth`_<sub>T</sub>(u_), this shows the bound stated in Lemma 3.

**Lemma 6.** \(i_j+\lceil\frac{k}{2}\rceil\le i_{j+1}\) _for all_ \(j\in[s-1]\).

