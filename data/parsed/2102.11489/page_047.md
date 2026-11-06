We accomplish this by leveraging a tight compaction circuit<sup>10</sup> that is optimal in size, but not so optimal in depth -- since each chunk is small. In fact, to achieve this, we can use the tight compaction circuit by Asharov et al. \[ALS21\], but replace some its building blocks with parallel versions (see Theorem 13.1 for more details). The resulting tight compaction circuit has depth that is super-polylogarithmic in the input length, but when applied to a chunk of polylog_n_ size, the depth would be upper bounded by _O_(log_n_).

**Compressing all chunks.** Now that we have finished the load distribution phase, all chunks on the left and right must be sparse. We therefore compress each chunk to 1/log<sup>2</sup>_m_ of its original size. This can be done by applying to each chunk a tight compaction circuit that is optimal in work but not optimal in depth (same as the building block we used in the online routing phase).

After this, the input is compressed to 1/log<sup>2</sup>_m_ of its original size, without losing any real elements.

## 13.4 Proof of Theorem 13.3

We will run a variant of the lossy loose compactor algorithm described in the proof of Theorem 8.1 in Section 7.

**Bipartite expander graphs with polylogarithmic degree.** Recall the bipartite graph of Margulis \[Mar73\]. Fix a positive \(t\in\mathbb{N}\). The left and right vertex sets are \(L=R:=[t]\times[t]\). A left vertex (_x,y_) is connected to the right vertices (_x,y),(x,x+y),(x,x+y_+1),(_x+y,y),(x+y_+1_,y_) where all arithmetic is modulo _t_. We let _H<sub>m</sub>_ be the resulting graph that has _m=t_<sup>2</sup> vertices on each side.

It is known (Margulis \[Mar73\], Gabber and Galil \[GG81\], and Jimbo and Maruoka \[JM87\]) that for every _m_ which is a perfect square (i.e., of the form _m=i_<sup>2</sup> for some \(i\in\mathbb{N}\)), _H<sub>m</sub>_ is 5-regular and the second largest eigenvalue of its normalized adjacency matrix \(\lambda_2(H_m)\in(1/5,1)\) is a constant. Let \(\epsilon:=1/log^4m\). We will use a graph \(G_{\epsilon,m}:=H_m^\gamma\) that is the \(\gamma\)-th power of _G<sub>m</sub>_, where \(\gamma\) is the smallest odd integer such that \(\lambda_2(G_{\epsilon,m})=\lambda_2(H_m)^\gamma\le\epsilon\). In other words, in \(G_{\epsilon,m}\), the edges are the length-\(\gamma\) paths in _H<sub>m</sub>_. Therefore, \(G_{\epsilon,m}\) is a \(5^\gamma\)-regular bipartite graph. Note that the degree \(5^\gamma\in[log^cm,25log^cm]\) for some constant _c\>_4 (where any constant _c\>_4 works later).

**Sparse loose compactor algorithm.** We first describe the modifications to the meta-algorithm on top of the lossy loose compactor algorithm in the proof of Theorem 8.1. We then described the modified circuit implementation of the meta-algorithm.

<sup>10</sup>In fact, in our formal technical sections, we will define a slight variant of tight compaction called "distribution" to accomplish the online routing -- see Sections 4 and 13.1.

Sparse loose compactor
Expander graph family and parameters. We use a family of bipartite expander graphs
whose special expansion
1/log4m. The expander graph family can be constructed in the aforementioned manner.
Input. The input is an array of length which is promised to be 1/(logn)C
sparse. Interpret
I as an array of super-elements where n'
each super-element consists of logn
consecutive elements in I, and a super-element is real if it consists of at least one real element. Assume that n'
for some perfect square m and =
of the
a
n
and that n' is divisible by
d/2
- see Remark 5

