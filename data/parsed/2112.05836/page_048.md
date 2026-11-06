### 8.3 Approximation Algorithm

Let the k-SD distance be _k(N-k-SD(X_<sub>1</sub>_,...,X<sub>k</sub>_)). In other words, the k-SD distance is the total number of unmatched characters.

**Theorem 8.4.** _There is an_ \(O\left(|\Sigma|N^{\lceil(k-1)/\ell\rceil} lg(|\Sigma|N)\right)\) _time algorithm to get an_ \(\ell\) _approximation of the k-Shift Distance distance for any integer_ \(\ell\ge 2\).

_Proof._ Partitions the _k_-1 of the strings into \(\ell\) groups \(G'_1,\dots,G'_\ell\) which each contain as close to \((k-1)/\ell\) strings as possible, the maximum number of strings in each group is \(\lceil(k-1)/ell\rceil\). Now, take the final string, _S<sub>k</sub>_ and add it to all the sets to make new sets \(G_1,\dots,G_\ell\), now the maximum number of strings in each group is \(\lceil(k-1)/ell+1\rceil\).

On each of these partitions run the algorithm for _k_-Shift Distance. The time for this is<br>
\(O\left(\ell|\Sigma|N^{\lceil(k-1)/\ell+1\rceil-1} lg(|\Sigma|N)\right)\) and \(\ell\) is a constant. Now, using the value of _k_-Shift Distance we can compute the _k_-Shift Distance distance. Let the distances of the sets of strings in \(G_1,\dots,G_\ell\) be \(\Delta_1,\dots,\Delta_\ell\). Now, note that these call be framed as distances to the last string _X<sub>k</sub>_. So, the distance of all these strings together is at most \(\Delta_1+\cdots+\Delta_\ell\) and is at least \(max(\Delta_1,\dots,\Delta_\ell)\). Finally, note that

\(1\le\frac{\Delta_1+\cdots+\Delta_\ell}{max(\Delta_1,\dots,\Delta_\ell)}\le\ell.\)

As a result there is an approximation factor of \(\ell\) and a running time \(O\left(|\Sigma|N^{\lceil(k-1)/\ell\rceil} lg(|\Sigma|N)\right)\).

## 9 On High-Dimensional Generalizations of DIST Matrices

Many of the crucial properties of DIST matrices derived in, e.g., \[Tis15\] used for two-string algorithms rely on the Monge property. For LCS, the Monge property is that given two strings _X,Y_ and the alignment graph **G**_<sub>X,y</sub>_ then letting _d(u,v_) be the longest path from _u_ to _v_, we have \(d(v_{0,i},v_{|X|,j})+d(v_{0,i-1},v_{|X|,j+1})\le d(v_{0,i-1},v_{|X|,j})+d(v_{0,i},v_{|X|,j+1})\). For example, in this paper we used the ability to take min-plus products of unit Monge matrices efficiently, and our use of the SMAWK algorithm was enabled by the Monge property.

However, it appears no analogous property holds for even DIST "3-tensors", the three-string generalization of DIST matrices. Intuitively, this is because it is not possible to enforce that any path from _v_<sub>1</sub> to _v_<sub>2</sub> intersects any path from _v_<sub>3</sub> to _v_<sub>4</sub> for four distinct vertices _v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>3</sub>_,v_<sub>4</sub>, unlike in the two-dimensional alignment graph. We will use LCS as the metric for our examples here, but one can find similar examples for edit distance.

For example, let _A_\[_i_<sub>1</sub>_,i_<sub>2</sub>_,j_<sub>1</sub>_,j_<sub>2</sub>\] be the longest path length from _v_<sub>0_,i_<sub>1</sub>_,i_<sub>2</sub></sub> to _v_<sub>_n_<sub>1</sub>_,j_<sub>1</sub>_,j_<sub>2</sub></sub> in the three- dimensional alignment graph of three strings. An analog of the Monge property in three dimensions might be:

\(A(i_1,i_2,j_1,j_2)+A(i_1-1,i_2,j_1+1,j_2)\le A(i_1-1,i_2,j_1,j_2)+A(i_1,i_2,j_1+1,j_2)\)

However, this does not seem true in general. Consider the following example, where there are two sets of length 1 edges. The first (in blue) has \(\ell\) such edges, and is contained entirely between "layer" _i_<sub>1</sub> and _j_<sub>1</sub> of the DAG. The second (in red) has \(\ell+1\) edges, however two of these edges are outside the part of the DAG between (0_,i_<sub>1</sub>_,i_<sub>2</sub>) and (_m,j_<sub>1</sub>_,j_<sub>2</sub>).

