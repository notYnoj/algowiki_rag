(iii) Call a pair \((x,y)\in X^2\) _good_ if _f(x,y_)=rank(_x,y_) and _bad_ otherwise. Let \(R\subseteq X^2\) be the subset of bad pairs. Then \(|R|\le K|X|^2/L\). Indeed, fix \(x\in X\) and consider the increasing sequence \(f(x,\cdot)\). For each bad pair (_x,y_), this sequence "jumps" from _f(x,y_) to \(f(x,y')\) by _L_. However, the range of _f_ is \[|_X+X_|\], hence the number of such jumps is at most \(|X+X|/L\le K|X|/L\). Summing over all |_X_| choices of _x_, we obtain the total bound \(|R|\le K|X|^2/L\).

The algorithm now proceeds in two cases:

• _(Good Case)_ Let us call a pair (_i,j_) _good_ if there is some witness _k_ such that \((A[i,k],B[k,j])\in X^2\) is good, and _bad_ otherwise. Our goal in this step is to compute a matrix \(C\ge A*B\) that correctly solves all good entries (i.e., _C_\[_i,j_\]=(_A∗B_)\[_i,j_\] whenever (_i,j_) is good). To this end, construct the matrices \(A'\) indexed by \([n]\times([\sqrt{n}]\times X)\) and \(B'\) indexed by \(([\sqrt{n}]\times X)\times[n]\) as follows:<tbc>

\(A'[i,(k,y)]=f(A[i,k],y),\)<br>
\(B'[(k,y),j]=\left\{\begin{array}{ c c }
0 & \text{if}B[k,j]=y, \\
\perp & \text{otherwise}.
\end{array}\right.\)

<tbc>Denote their min-plus product by \(C'=A'*B'\). Now define the matrix _C_ by \(C[i,j]=\text{select}(C'[i,j])\). Then indeed it holds for all pairs (_i,j_) that

\(C[i,j]=\text{select}(C'[i,j])\)<br>
\(=min_k\text{select}(f(A[i,k],B[k,j]))\)<br>
\(\ge min_k\text{select}(\text{rank}(A[i,k],B[k,j]))\)<br>
\(=min_k(A[i,k]+B[k,j]),\)

where the inequality is due to Property (ii). For any good pair this inequality is an equality by (iii), so the matrix _C_ is as claimed.

It remains to describe how to compute the min-plus product \(C'=A'*B'\). The matrix \(A'\) is not row-bounded-difference, but it is close to that. Indeed, from Property (i) we get that (1) along any row _i_ there are \(\sqrt{n}\cdot|X|\) pairs of adjacent entries \(A'[i,(k,y)]\) and \(A'[i,(k,y')]\) that differ by at most _L_. Moreover, (2) there are \(\sqrt{n}\) pairs of adjacent entries of the form \(A'[i,(k,y)]\) and \(A'[i,(k',y')]\) (where \(k\neq k'\)), and these entries can differ by up to |_X+X_|. To turn \(A'\) into a row-bounded- difference matrix we will now insert new columns to \(A'\), filled with dummy entries whose only purpose is to interpolate the gaps described before. It suffices to add \(\sqrt{n}\cdot|X|\cdot L\) columns to deal with the gaps of type (1), and \(\sqrt{n}\cdot|X+X|\) columns to deal with the gaps of type (2). In total the number of new columns is \(\sqrt{n}\cdot|X|\cdot L+\sqrt{n}\cdot|X+X|=(L+K)n\). For each column added in this way we also add a corresponding row in \(B'\) filled with \(\perp\)-entries. Let \(A'',B''\) denote the resulting matrices. This operation leaves the min-plus product unchanged, \(A'*B'=A''*B''\).

Running Time: In summary we compute the min-plus product \(A''*B''\), where both matrices can be viewed as square matrices of size at most _O_((_K+L)n_), where \(A''\) is row-bounded-difference, has entries bounded by \(|X+X|\le K|X|\le K\sqrt{n}\), and where \(B''\) has at most _n_<sup>1.5</sup> non-\(\perp\) entries. This is an instance of the problem described in the lemma statement of size _N=O_((_K_<sup>2</sup>+_L)n_). Therefore, the running time is \(O(N^{2.5-\epsilon})=O((K^5+L^{2.5})n^{2.5-\epsilon})\).

• _(Bad Case)_ It remains to correct _C_\[_i,j_\] for all bad pairs (_i,j_). To this end enumerate all bad pairs \((x,y)\in R\), and all \(k\in[\sqrt{n}]\). Then enumerate all \(i\in[n]\) with _A_\[_i,k_\]=_x_ and all \(j\in[n]\) with _B_\[_k,j_\]=_y_. We update \(C[i,j]\leftarrow min\{C[i,j],A[i,k]+B[k,j]\}\). If (_i,j_) is bad then by definition we will correctly compute _C_\[_i,j_\] in this step.

