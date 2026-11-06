elements, for example AVL trees. Additionally, we store the size of the subtree in every node. Then we have the following easy proposition.

**Proposition 4.2.** _We can split BST into at most b smaller BSTs containing_ \(\Theta(s/b)\) _elements each in_ \(\mathcal{O}(b(1+log\frac{s}{b}))\) _time._

_Proof._ As long as there is a BST of size at least 2_s/b_ we split it into two BSTs of (roughly) equal sizes. Assuming for simplicity that both _s_ and _b_ are powers of 2, this takes \(\mathcal{O}(\sum_{i=0}^{logb-1}2^ilog(s/2^i))\) overall time, which can be bounded by calculating \(\int_1^blog(s/x)dx=\mathcal{O}(b(1+log(s/b)))\).

To process a batch of _b_ insertions/queries efficiently, we first sort them in O(_b_(1+log(_n/b_))) time. Then, we split the BST into at most _b_ smaller BSTs containing \(\Theta(s/b)\) elements each, where _s_ is the number of stored elements, using Proposition 4.2. Because insertions/queries are sorted, we can determine for each of them the relevant BST by a linear scan, and then insert/query the relevant BST in O(1+log(_s/b_)) time per operation (if there are more than _s/b_ insertions to the same smaller BST, we split it into trees containing single elements, and partition the insertions into groups of \(\Theta(s/b)\)). Finally, we merge the BSTs into pairs, quadruples, and so on. By the calculation from the proof of Proposition 4.2 this also takes O(_b_(1+log(_s/b_))) time.

Lemma 4.1 is already enough to binary search for the result of (_x,y_) in O(log<sup>2</sup>_n_) time due to the following property.

**Lemma 4.3.** _Consider any r and an already processed matching pair_ \((x',y')\) _with result r. Then either r_=1 _or there exists an already processed matching pair_ \((x'',y'')\) _with result r_-1 _such that_ \(x''<x'\) _and_ \(y''<y'\).

_Proof._ Assume that \(r\ge 2\) and consider a sequence _C_ which realises the result for \((x',y')\). Then _C_\[1..|_C_|-1\] is an increasing subsequence of both \(A[1..(x'-1)]\) and \(B[1..(y'-1)]\). Let \(A[x'']\) and \(B[y'']\) be its last elements in _A_ and _B_, respectively. Then \(x''<x'\), \(y''<y'\), and \(A[x'']=B[y'']\), so \((x'',y'')\) is a matching pair, and because _C_ is strictly increasing this matching pair must have been already processed.

However, our goal is to spend O(1+log<sup>2</sup>(_n/_cnt(_v_))) time per every (_x,y_). We exploit the following property.

**Lemma 4.4.** _Consider two_ \(\sigma[i]\) _pairs_ (_x,y_<sub>1</sub>) _and_ (_x,y_<sub>2</sub>)_, where y_<sub>1</sub>_\<y_<sub>2</sub>_. The result for_ (_x,y_<sub>2</sub>) _is at least as large as for_ (_x,y_<sub>1</sub>).

_Proof._ Consider a sequence _C_ which realises \(LCIS^\rightarrow(x,y_1)\). Then, replacing _y_<sub>1</sub> with _y_<sub>2</sub> we obtain a valid candidate for the value of \(LCIS^\rightarrow(x,y_2)\).

Consider all \(\sigma[v]\) pairs with the same _x_ coordinate (_x,y_<sub>1</sub>),(_x,y_<sub>2</sub>)_,...,(x,y_<sub>cnt(\(\sigma[v]\))</sub>). We binary search for the result of (_x,y<sub>i</sub>_) for _i_=cnt(_v),...,_2,1. By Lemma 4.4, in the _i_-th step we can start with the result found in the (_i_+1)-th step. Using doubling binary search, by convexity of the log function the overall complexity becomes O(cnt(_v_)(1+log(_n/_cnt(_v_)))). This is still too slow, as every step involves a separate invocation Lemma 4.1 and takes O(log_n_) time. To obtain the final speed up, we process all _x_ coordinates _x_<sub>1</sub>_,x_<sub>2</sub>_,...,x_cnt(_v_) together. The high level idea is to synchronise all binary searches and exploit the possibility of asking a batch of queries.

We start with modifying the proof of Lemma 4.1 to allow for more general queries: given _x_, we want to find the smallest _y_ such that there exists \((x',y')\in S\) with \(x'<x\) and \(y'<y\) (or detect that<tbc>

