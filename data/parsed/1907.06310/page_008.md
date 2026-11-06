<tbc>\(q'_i\) for _q<sub>i</sub>_ in _T_<sub>_i_-1</sub>. Form the key sequence _U<sub>i</sub>_ by relabeling the keys in Figure 3 via the reverse index for _q<sub>i</sub>_ and recording the sequence of keys in marked nodes on the path from _q<sub>i</sub>_ to \(q'_i\), excluding the key marked in \(q'_i\). Splaying _U<sub>i</sub>_ starting from _q<sub>i</sub>_ results in final tree \(q'_i\). The structure of the subtrees hanging from the path do not affect the transition tree of a splay operation. Thus, using splay operations to induce a restricted rotation in a four-node rooted hull in a larger tree _T_ also performs the restricted rotation in _T_, and the request sequence \(V=U_1\oplus\cdots\oplus U_k\) induces Splay to successively enact the restricted rotations that transform _T_ into \(T'\). Each of these rotations corresponds to at most thirteen requests in _V_ . Every access path in Splay’s execution of _V_ starting from _T_ has length at most four. Since _k\<_4|_T_|, the total cost of this execution is at most 208|_T_|.

**Theorem 3.5.** _Splay is dynamically optimal if and only if it is approximately monotone._

_Proof._ We prove Splay is coercible. Let _E_ be an execution for _X_=(_x_<sub>1</sub>_,...,x<sub>m</sub>_) starting from _T_ comprising rooted hulls _Q_<sub>1</sub>_,...,Q<sub>m</sub>_, transition trees \(Q'_1,\dots,Q'_m\), and after-trees _T_<sub>1</sub>_,...,T<sub>m</sub>_. For initial trees of size three or less set S(_E_)=_X_. Otherwise, let \(\mathcal{S}(E)=V_1\oplus\cdots\oplus V_m\) where, for \(1\le i\le m\), _V<sub>i</sub>_ is the request sequence constructed in Theorem 3.4 for inducing Splay to transform _Q<sub>i</sub>_ into \(Q'_i\). (If \(Q_i=Q'_i\) then _V<sub>i</sub>_ is the singleton request sequence whose sole term is _x<sub>i</sub>_.) Splaying _V<sub>i</sub>_ starting from _T_<sub>_i_-1</sub> induces a substitution of \(Q'_i\) for _Q<sub>i</sub>_ in _T_<sub>_i_-1</sub> to form _T<sub>i</sub>_, where _T_<sub>0</sub>=_T_. A splay operation always places the requested key as the root of the after-tree. Since _x<sub>i</sub>_ is the root of \(Q'_i\) it must be the last key in _V<sub>i</sub>_. Therefore, _X_ is a subsequence of S(_E_), and by Theorem 3.4 \(\mathrm{cost}(\mathcal{S}(E),T)\le 208(|Q'_1|+\cdots+|Q'_m|)\). Hence, S is a simulation embedding for Splay and Splay is coercible. Apply Theorem 3.2.

2
1
1
4
2
4
3
4
4
1
2
2
XIV
1
3
3
XIII
1
4
3
2
2
4
XII
1
3
4
1
3
XI
IV
2
2
3
1
4
X
2
V
4
1
3
1
4
3
IX
VI
2
1
1
3
VIII
VII
4
2
4
4
3
3
2
3
1
4
*
1
2
2

Figure 3: Splay at starred nodes to convert one tree into the next.

