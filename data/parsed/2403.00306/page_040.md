## 3.2.3 TraverStringRef

TraverStringRef is an improved version of qpMS7. Four improvements were proposed for which will be explained below:

### Feasibility Check without Precomputed

Like qpMS7 feasibility check is not performed by checking an occurrence in the precomputed table. Here a theorem is followed: Three strings _a,b,c_ of the same length satisfy

\(\mathcal{B}(a,da)\cap\mathcal{B}(b,db)\cap\mathcal{B}(c,dc)\neq\emptyset\)

if and only if

\(da\ge 0,db\ge 0,dc\ge 0,\)<br> \(da+db\ge dH(a,b),\)<br> \(db+dc\ge dH(b,c),\)<br> \(dc+da\ge dH(c,a),\)<br> \(da+db+dc\ge|R_2(a,b,c)|+|R_3(a,b,c)|+|R_4(a,b,c)|+|R_5(a,b,c)|\)

### Elimination of unnecessary Combinations

Unnecessary combinations are eliminated in qpMS7 and the procedure is quite same as qPM- SPruneI. The unnecessary checks are suppressed when _q\<n_ and \(\mathcal{T}\leftarrow\{Sh|i_2+1\le h\le n\}\).

### String Reordering

This improvement is ensured by pruning the subtree rooted at current node as early as possible by checking the feasibility occurences in non decreasing order. Here the difference is when the input string from where the input reference occurences are taken is determined. Since the number of string in \(\mathcal{B}(x_0,d)\cap\mathcal{B}(r,d)\) is a non decreasing function of _dH(x_<sub>0</sub>_,r_) the reference _r_ is taken from the input that maximizes minimum hamming distance between _x_<sub>0</sub> and _r_ to reduce size of the search tree.

### Position Reordering

To ensure efficient pruning of subtrees the search tree’s structure is investigated. Only the nodes satisfying the condition of not changing the hamming distance change the structure of the search

