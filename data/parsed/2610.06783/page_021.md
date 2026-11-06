with |_Q_|=_m_, and set the inputs of the others to zero. As we now make precise, the product for such a _Q_ multiplies an \(N_0\times D\) matrix by a \(D\times N_0\) matrix: the _L-m_ outer levels, with three left and three right outer variables each, give its _N_<sub>0</sub>=3<sup>_L-m_</sup> rows and _N_<sub>0</sub> columns, and the _m_ inner levels, with four left and four right inner variables each, give the _D_=4_<sup>m</sup>_ terms of the sum in each of its entries. (To prove Theorem 5, we will ultimately set _L_=19_m_, a choice we will explain in Section 2.4.3 below.)

We will index the rows and columns of the matrices in these products by strings of variables. For an \(N_0\times D\) matrix, we index its _N_<sub>0</sub> rows by the _N_<sub>0</sub> strings of _L-m_ outer left variables, and its _D_ columns by the _D_ strings of _m_ inner left variables. Similarly, for a \(D\times N_0\) matrix, we index its _D_ rows by the strings of _m_ inner right variables, and its _N_<sub>0</sub> columns by the strings of _L-m_ outer right variables. To multiply an \(N_0\times D\) matrix _A_ by a \(D\times N_0\) matrix _B_, we match the column of _A_ indexed by the string \(\pi=p_{i_1j_1}p_{i_2j_2}\cdots p_{i_mj_m}\) with the row of _B_ indexed by the string \(\pi'=q_{i_1j_1}q_{i_2j_2}\cdots q_{i_mj_m}\) with the same indices, so that the entry of _AB_ in row _r_ and column _c_ is

\((AB)[r,c]:=\sum_\pi A[r,\pi]B[\pi',c],\)

where the sum is over all the _D_ strings \(\pi\) of _m_ inner left variables. Thus, the rows of the product are indexed by the strings of outer left variables and its columns by the strings of outer right variables.

Let _Q_ be a subset of {1_,...,L_} of size _m_. As above, the outer part of a left string _u_ with inner set _Q_ is a row of an \(N_0\times D\) matrix and its inner part is a column, so the left strings with inner set _Q_ index the entries of such a matrix. For an \(N_0\times D\) matrix _X<sub>Q</sub>_ we write _X<sub>Q</sub>_\[_u_\] for its entry at the row and the column of _u_. Similarly, the right strings _v_ with inner set _Q_ index the entries of a \(D\times N_0\) matrix _Y<sub>Q</sub>_, the row given by the inner part of _v_ and the column by the outer part, and we write _Y<sub>Q</sub>_\[_v_\] for this entry. Finally, the output strings with inner set _Q_ index the entries of the product _X<sub>Q</sub>Y<sub>Q</sub>_: if the variables of _w_ at the levels outside _Q_ are _z_<sub>_i_<sub>1</sub>_j_<sub>1</sub></sub>_,...,z_<sub>_i<sub>L</sub>-mj<sub>L</sub>-m_</sub>, in the order of the levels, then the **_row_** of _w_ is the string \(x_{i_1}\cdots x_{i_{L-m}}\) and its **_column_** is the string \(y_{j_1}\cdots y_{j_{L-m}}\), and we write (_X<sub>Q</sub>Y<sub>Q</sub>_)\[_w_\] for the entry there (Figure 4).

We can now check that Full, which returns Mult(_a,b_), really computes these products. For each of the \(K:=\genfrac(){pt}{2}{L}{m}\) subsets _Q_ of {1_,...,L_} of size _m_, let _X<sub>Q</sub>_ be any \(N_0\times D\) matrix and _Y<sub>Q</sub>_ be any \(D\times N_0\) matrix. Let the input arrays _a_ and _b_ be these matrices laid side by side, by setting

\(a[u]:=X_Q[u],b[v]:=Y_Q[v]\)

for all the left strings _u_ and the right strings _v_ whose inner set _Q_ has exactly _m_ elements, and _a_\[_u_\]:=0, _b_\[_v_\]:=0 at every other string.

**Lemma 9.** _For the input arrays a,b above and every output string w whose inner set Q has exactly m elements,_

\(\mathrm{Mult}(a,b)[w]=(X_QY_Q)[w].\) (4)

_Proof._ By Lemma 8, Mult(_a,b_)\[_w_\] is the sum, over all left strings _u_ and right strings _v_, of \(\gamma(u_1,v_1,w_1)\cdots\gamma(u_L,v_L,w_L)a[u]b[v]\), where \(\gamma(s,t,z)\) is the coefficient of _stz_ in _G+E_. We determine which summands can be nonzero. First, \(a[u]b[v]\neq 0\) requires the inner sets of _u_ and _v_ to have exactly _m_ elements. Next, at a level \(\ell\in Q\) we have \(w_\ell=z_0\), and the only monomials of _G+E_ that contain _z_<sub>0</sub> are the _p<sub>ij</sub>q<sub>ij</sub>z_<sub>0</sub>, with coefficient 1. So \((u_\ell,v_\ell)=(p_{ij},q_{ij})\) for some _i,j_. Thus _u_ and _v_ have an inner variable at every level of _Q_, and their inner sets are therefore exactly _Q_. Finally, at a level \(\ell\notin Q\) we have \(w_\ell=z_{ij}\) for some _i,j_, and \(u_\ell\) and \(v_\ell\) are outer. The<tbc>

