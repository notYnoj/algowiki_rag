<tbc>18000 scalar multiplications while multiplying _A_<sub>1</sub>(_A_<sub>2</sub>_A_<sub>3</sub>) takes \((20\cdot 30\cdot 40)+(10\cdot 20\cdot 40)=32000\) scalar multiplications.

Matrix-chain multiplication is a 2D LWS<sup>PT</sup> problem where _T_\[_i,j_\] is the cost of multiplying matrices _A<sub>i</sub>,...,A<sub>j</sub>_ and we want to find the _k_ which minimizes the cost of multiplying (_A<sub>i</sub>,...,A<sub>k</sub>_) by (_A_<sub>_k_+1</sub>_,...,A<sub>j</sub>_). Multiplying matrices (_A<sub>i</sub>,...,A<sub>k</sub>_) would result in a matrix of dimension (_d_<sub>_i_-1</sub>_,d<sub>k</sub>_) and multiplying (_A_<sub>_k_+1</sub>_,...,A<sub>j</sub>_) would result in a matrix of dimension (_d<sub>k</sub>,d<sub>j</sub>_). Thus _T_\[_i,j_\] equals the cost of multiplying all matrices _A<sub>i</sub>,...,A<sub>k</sub>_ (i.e. _T_\[_i,k_\]) and all matrices _A_<sub>_k_+1</sub>_,...,A<sub>j</sub>_ (i.e. _T_\[_k,j_\]) plus the cost of multiplying those two resultant matrices together (i.e. _d_<sub>_i_-1</sub>_d<sub>k</sub>d<sub>j</sub>_). Setting _w_<sub>1</sub>\[_i,j,k_\]=_w_<sub>2</sub>\[_i,j,k_\]=_d_<sub>_i_-1</sub>_d<sub>k</sub>d<sub>j</sub>_ would solve this problem.

Let us construct a vector _d_=\[_d_<sub>0</sub>_,d_<sub>1</sub>_,...,d<sub>n</sub>_\] with the dimensions of our matrices _A_<sub>1</sub>_,...,A<sub>n</sub>_. Then _w_ has a tensor rank of 1 because it can be represented as the product of different entries of _d_, namely \(w[i,j,k]=d[i-1]\cdot d[j]\cdot d[k]\). Moreover, there exists an _O(n_log_n_) time algorithm for this problem \[HS82, HS84\]. Corollary 4.2 helps explain why this speedup is possible.

### 6.2 Optimal Binary Search Tree

The optimal binary search tree construction problem was introduced in \[Knu71, GM59\] and is defined as follows:

**Definition 6.2** (Optimal Binary Search Tree)**.** _Given a sequence of n distinct keys h_<sub>1</sub>_,...,h<sub>n</sub> in sorted order where the probability of accessing key h<sub>i</sub> is p<sub>i</sub>, construct a binary search tree from these keys which minimizes the expected access time._

This problem is a 2D LWS<sup>PT</sup> instance where _T_\[_i,j_\] is the minimum cost binary search tree with keys _h<sub>i</sub>,...,h<sub>j</sub>_. We want to chose a key _h<sub>k</sub>_ to be the root of the sub-tree containing keys _h<sub>i</sub>,...,h<sub>j</sub>_ which minimizes the expected access time. The expected access time for a key _h<sub>t</sub>_ is \(p_t\cdot(d_t+1)\), the key’s probability times its depth in the tree (i.e. the number of times this item has been accessed). We can compute this quantity incrementally, adding the probability _p<sub>t</sub>_ of key _h<sub>t</sub>_ once at every level it appears in the tree, summing up _p<sub>t</sub>_ a total of _d<sub>t</sub>_ times. Thus the expected cost of accessing keys _h<sub>i</sub>,...,h<sub>j</sub>_ is \(w[i,j,k]=\sum_{t=i}^jp_t\).

_w_ has a slice rank of 1 because it can be written as \(w[i,j,k]=a[k]\cdot b[i,j]\) where _a_\[_k_\]=1 and \(b[i,j]=\sum_{t=i}^jp_t\). This observation, together with Corollary 4.4, recovers the known _O(n_<sup>2</sup>) time algorithm for this problem \[Yao80, Yao82\].

## References

