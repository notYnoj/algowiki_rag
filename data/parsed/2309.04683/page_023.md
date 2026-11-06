## 5 Applications of kD LWS

In Section 3, we have shown that kD LWS can solve kMin-IP and APSP with different tensors. In this section we discuss more applications of kD LWS.

### 5.1 Higher Dimension Airplane Refueling

The airplane refueling problem was brought by \[HL87\] as an example of LWS.

**Definition 5.1** (Airplane Refueling)**.** _Suppose an airplane needs to fly between 2 given airports which are distance R apart. Suppose there are n_-1 _different refueling stops at distance x_<sub>1</sub>_,...,x_<sub>_n_-1</sub> _from the departure point and all stops lie on the segment between departure and destination points. We can let_ 0=_x_<sub>0</sub>_\<x_<sub>1</sub>_\<...\<x<sub>n</sub>=R. The cost of flying_ \(\ell\) _miles is_ \((k-\ell)^2\) _for some k\>_0 _(we prefer flying close to k miles), and the goal is to fly from departure point to arrival point while minimizing the cost._

It is not hard to see setting _w_\[_i,j_\]=(_x<sub>j</sub>-x<sub>i</sub>-k_)<sup>2</sup> in LWS will solve the problem since _T_\[_j_\] is always the minimum cost of flying from _x_<sub>0</sub> to _x<sub>j</sub>_. _w_ has rank 4 because

\(w[i,j]=x_j^2\cdot 1+1\cdot x_i^2+(-2x_j)\cdot(x_i+2k)+k\cdot(2x_i+k),\)

and \[HL87\] shows that airplane refueling can be solved in linear time.

In the real world, it is usually unlikely that all refueling stops are located on a single line. In addition, the plane can move in multiple directions. The higher dimension airplane refueling problem is motivated by these observations.

**Definition 5.2** (Higher Dimension Airplane Refueling)**.** _Suppose an airplane needs to fly between two given airports on a k-dimensional grid with n points at each dimension. Each point in the grid represents a refueling stop, and the cost of flying from stop_ \((i_1,\dots,i_{\ell-1},j_\ell,i_{\ell+1},\dots,i_k)\) _to_ (_i_<sub>1</sub>_,...,i<sub>k</sub>_) _to is_ \(c(i_1,\dots,i_k,j_\ell)\)_. The problem asks the minimum cost of flying from_ (1_,...,_1) _to_ (_n,...,n)._

Notice that this is closer to real-world scenario where trains need to travel on railways, or we are driving in a city with well-organized roads.

Setting _w_\[_i_<sub>1</sub>_,...,i_<sub>_k_+1</sub>\]=_c_\[_i_<sub>1</sub>_,...,i_<sub>_k_+1</sub>\] in kD LWS will solve the problem because _T_\[_i_<sub>1</sub>_,...,i<sub>k</sub>_\] will always be the minimum cost of flying from (1_,...,_1) to (_i_<sub>1</sub>_,...,i<sub>k</sub>_). If we were to follow the cost function suggested in \[HL87\], then we have \(c[i_1,\dots,i_k,j_\ell]=(L-(i_\ell-j_\ell))^2\), which has constant rank and thus it can be solved in time \(O(n^{k+1-\varepsilon})\) for some \(\varepsilon>0\).

Another natural scenario is that the cost of flying from \((i_1,\dots,i_{\ell-1},j_\ell,i_{\ell+1},i_k)\) to (_i_<sub>1</sub>_,...,i<sub>k</sub>_) only depends on (_i_<sub>1</sub>_,...,i<sub>k</sub>_). It mimics the scenario that the airplane is charged a fee upon arrival.

**Definition 5.3** (Arrival Fee Airplane Refueling)**.** _Suppose an airplane needs to fly between two given airports on a k-dimensional grid with n points at each dimension. Each point in the grid represents a refueling stop, and the cost of flying from stop_ \((i_1,\dots,i_{\ell-1},j_\ell,i_{\ell+1},\dots,i_k)\) _to_ (_i_<sub>1</sub>_,...,i<sub>k</sub>_) _to is c(i_<sub>1</sub>_,...,i<sub>k</sub>). The problem asks the minimum cost of flying from_ (1_,...,_1) _to_ (_n,...,n)._

In the arrival fee airplane refueling problem with dimension _k_, the tensor has slice rank 1, so by Theorem 3.6 it can be solved in time \(O(n^{k+1-\varepsilon})\) for some \(\varepsilon>0\).

### 5.2 Multiple Nested Boxes

Nested boxes problem, or box stacking problem, is a famous example with a DP solution.

**Definition 5.4** (Nested Boxes)**.** _Given n boxes in d dimension of size_ (_b_<sub>1</sub>_,...,b<sub>d</sub>), find the longest chain such that each box fits into the next (without rotation). We say that box a of size_ (_a_<sub>1</sub>_,...,a<sub>d</sub>_) _fits into box b of size_ (_b_<sub>1</sub>_,...,b<sub>d</sub>_) _if_ \(a_i\le b_i\) _for all_ \(1\le i\le d\).

\[KPS17\] proves that nested boxes is sub-quadratic equivalent to the vector domination problem defined in \[ILPS14\] and both can be solved by LWS: sort the boxes by volumn in increasing order as _B_<sub>1</sub>_,...,B<sub>n</sub>_ and set _w<sub>ij</sub>_ to be -1 if _B<sub>j</sub>_ contains _B<sub>i</sub>_ and 0 otherwise.

