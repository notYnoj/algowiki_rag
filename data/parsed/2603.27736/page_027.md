1.1. _(Unpopular Triangles)_ Enumerate all pairs \((i,j)\in[n_1]\times[n_3]\) with \(C[i,j]\unknown\in P_{i,j}\). By definition, \(C[i,j]\unknown\in P_{i,j}\supseteq P_{4d^\prime/p}(X_i^*,Y_j)\) can be expressed as a sum _x+y_ of elements \(x\in X_i^*\) and \(y\in Y_j\) in at most \(4d'/p\) ways. Enumerate all such representations (_x,y_), then enumerate all \(k\in[n_2]\) with _A_\[_i,k_\]=_x_ and test if (_i,k,j_) is an exact triangle; if yes, we insert it into the set T .<tbc>

1.2. _(Popular Triangles)_ The number of pairs (_i,j_) with \(P_{i,j}\subseteq P_{2d^\prime/p}(X_i^*,Y_j)\neq\emptyset\) is at most _n_<sub>1</sub>_n_<sub>3</sub>_/t_ by Lemma 4.9. For each such pair we enumerate all possible \(k\in[n_2]\), test if (_i,k,j_) is an exact triangle, and in that case store (_i,k,j_) in T .<tbc>

2. _(Ordinary Triangles)_ Enumerate all pairs \(g,h\in[p^2]\). Let _A<sub>h</sub>,B<sub>g</sub>,C<sub>g,h</sub>_ be the matrices defined by

\(A_g[i,k]=\left\{\begin{array}{ c c }
A[i,k]-s_{i,g} & \text{if}A[i,k]\in X_{i,g}, \\
\perp & \text{otherwise},
\end{array}\right.\)<br>
\(B_h[k,j]=\left\{\begin{array}{ c c }
B[k,j]-t_{j,h} & \text{if}B[k,j]\in Y_{j,h}, \\
\perp & \text{otherwise},
\end{array}\right.\)<br>
\(C_{g,h}[i,j]=\left\{\begin{array}{ c c }
C[i,j]-s_{i,g}-t_{j,h} & \text{if}C[i,j]\neq\perp, \\
\perp & \text{otherwise}.
\end{array}\right.\)

Each ordinary triangle (_i,k,j_) appears in exactly one Exact Triangle instance (_A<sub>g</sub>,B<sub>h</sub>,C<sub>g,h</sub>_), namely the instance with \(A[i,k]\in X_{i,g}\) and \(B[k,j]\in Y_{j,h}\). Moreover, the value of the triangle is unchanged in that instance as the terms _s<sub>i,g</sub>_ and _t<sub>j,h</sub>_ cancel:

\(A_g[i,k]+B_h[k,j]-C_{g,h}[i,j]=A[i,k]+B[k,j]-C[i,j].\)

It is easily verified that all non-\(\perp\) entries in _A<sub>g</sub>_ stem from the set _S<sub>g</sub>_ (as \(X_{i,g}-s_{i,g}\subseteq S_g\)) and all non-\(\perp\) entries in _B<sub>h</sub>_ stem from the set _T<sub>h</sub>_ (as \(Y_{j,h}-t_{j,h}\subseteq T_h\)). Recall that further \(|S_g|,|T_h|\le d'\), so in each instance (_A<sub>g</sub>,B<sub>h</sub>,C<sub>g,h</sub>_) the matrices _A<sub>g</sub>_ and _B<sub>h</sub>_ satisfy the \(d'\)-uniformity condition.

In the following we will further modify _C<sub>g,h</sub>_ to also become \(d'\)-uniform. Let _q_ be another parameter to be determined later, and compute the set \(P:=P_{d^\prime/q}(S_g,T_h)\) (by brute-force, say, in negligible time). Then call a pair (_i,j_) _popular_ if \(C_{g,h}[i,j]\in P\) and _unpopular_ otherwise. Consider the following two cases:

2.1. _(Unpopular Entries)_ This case is similar to step 1.1. Our goal is to list all exact triangles (_i,k,j_) in (_A<sub>g</sub>,B<sub>h</sub>,C<sub>g,h</sub>_) where (_i,j_) is unpopular. To this end enumerate all unpopular pairs (_i,j_). Recall that there are at most \(d'/q\) representations of _C_\[_i,j_\] as a sum _x+y_ where \(x\in S_g\) and \(y\in T_h\). We enumerate all such representations, and further all \(k\in[n_2]\) with _A<sub>g</sub>_\[_i,k_\]=_x_. We test if (_i,k,j_) is an exact triangle, and in this case store (_i,k,j_) in T .<tbc>

Running Time: For each pair (i,j) we spend time O(dA) to list the relevant representations, plus time O(d'/p · n2/dA) to enumerate all pairs x,y,k. The total time is:
O(n1n3 · (dA+ 'p · n2
dA
(d+ -
dAt
n2
dA
p
p

Running Time: O(n1n2n3/t).

