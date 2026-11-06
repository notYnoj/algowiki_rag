## 3 Small Edit Distance

In this section, we prove our result on small edit distance, when the edit distance is bounded by _k_. In particular, we prove Theorem 3.

**Theorem 3** (Small-EDIT)**.** _Given two strings A=a_<sub>1</sub>_a_<sub>2</sub>_..a<sub>n</sub> and B=b_<sub>1</sub>_b_<sub>2</sub>_..b<sub>n</sub> of length n over alphabet_ \(\Sigma\)_, and a bound on their edit distance,_ \(\mathrm{ED}(A,B)\le k\)_, we can compute their edit distance exactly with O(n_log(_n_))_-time preprocessing and O(k_<sup>2</sup>log(_n_))_-time joint processing._

We first recall an algorithm developed in \[Ukk85, LMS98, LV88, Mye86\] that computes edit distance in _O(n+k_<sup>2</sup>) time.

**Warm-up: An** _O(n+k_<sup>2</sup>) **algorithm for Edit Distance.**

The well-known dynamic programming algorithm computes an \((n+1)\times(n+1)\) edit-distance matrix _D_\[0_...n_\]\[0_...n_\] where entry _D_\[_i,j_\] is the edit distance, ED(_A<sup>i</sup>,B<sup>j</sup>_) between the prefixes _A_\[1_,i_\] and _B_\[1_,j_\] of _A_ and _B_, where _A_\[1_,i_\]=_a_<sub>1</sub>_a_<sub>2</sub>_...a<sub>i</sub>_ and _B_\[1_,j_\]=_b_<sub>1</sub>_b_<sub>2</sub>_...b<sub>j</sub>_. The following is well-known and easy to verify coupled with the boundary condition _D_\[_i,_0\]=_D_\[0_,i_\]=_i_ for all \(i\in[0,n]\).

For all \(i,j\in[0,n]\)

\(D[i,j]=\mathrm{min}\left\{\begin{array}{ c c }
D[i-1,j]+1 & \text{if}i>0; \\
D[i,j-1]+1 & \text{if}j>0; \\
D[i-1,j-1]+\mathbb{1}(a_i\neq b_j) & \text{if}i,j>0.
\end{array}\right.\)

The computation cost for this dynamic programming is _O(n_<sup>2</sup>). To obtain a significant cost saving when \(\mathrm{ED}(A,B)\le k<<n\), the _O(n+k_<sup>2</sup>) algorithm works as follows. It computes the entries of _D_ in a greedy order, computing first the entries with value 0, 1,2_,...k_ respectively. Let diagonal _d_ of matrix _D_, denotes all _D_\[_i,j_\] such that _j=i+d_. Therefore, the entries with values in \[0_,k_\] are located within diagonals \[-_k,k_\]. Now since the entries in each diagonal of _D_ are non-decreasing, it is enough to identify for every \(d\in[-k,k]\), and for all \(h\in[0,k]\), the last entry of diagonal _d_ with value _h_. The rest of the entries can be inferred automatically. Hence, we are overall interested in identifying at most (2_k_+1)∗_k_ such points. The _O(n+k_<sup>2</sup>) algorithm shows how building a suffix tree over a combined string _A_$_B_ (where $ is a special symbol not in \(\Sigma\)) helps identify each of these points in _O_(1) time, thus achieving the desired time complexity.

Let _L<sup>h</sup>(d_)=max{_i:D_\[_i,i+d_\]=_h_}. The _h_-wave is defined by \(L^h=\langle L^h(-k),\dots,L^h(k)\rangle\). Therefore, the algorithm computes _L<sup>h</sup>_ for _h_=0_,..k_ in the increasing order of _h_ until a wave _e_ is computed such that _L<sup>e</sup>_(0)=_n_ (in that case ED(_A,B_)=_e_), or the wave _L<sup>k</sup>_ is computed in the case the algorithm is thresholded by _k_. Given _L_<sup>_h_-1</sup>, we can compute _L<sup>h</sup>_ as follows.

Define<tbc>

\(Equal(i,d)=\mathrm{max}_{q\ge i}(q|A[i,q]=B[i+d,q])\)

<tbc>Then, _L_<sup>0</sup>(0)=_Equal_(0,0) and

\(L^h(d)=\mathrm{max}\left\{\begin{array}{ c c }
Equal(L^{h-1}(d)+1,d) & \text{if}h-1\ge 0; \\
Equal(L^{h-1}(d-1),d) & \text{if}d-1\ge-k,h-1\ge 0; \\
Equal(L^{h-1}(d+1)+1,d) & \text{if}d+1,h+1\le k.
\end{array}\right.\)

Using a suffix tree of the combined string _A_$_B_, any _Equal(i,d_) query can be answered in _O_(1) time. Next, we show that it is possible to preprocess each _A_ and _B_ separately so that even then each _Equal(i,d_) query can be implemented in _O_(log_n_) time.

