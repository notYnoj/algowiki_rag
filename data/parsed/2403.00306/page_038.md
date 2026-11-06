\(1\le i\neq j\le n-q+2\) and _l_-mer \(x\epsilon s_i^l\) and _l_-mer \(y\epsilon s_j^l\) such that _M_ is in \(\mathcal{B}(x,d)\cup\mathcal{B}(y,d)\) and _M_ is a (_l,d,q_-2)-motif of the input strings excluding _s<sub>i</sub>_ and _s<sub>j</sub>_.

Algorithm qPMS7 uses a routine based on the above observations which finds all of the possible motifs. Algorithm qPMSPrune explores B(_x,d_) by traversing the tree T_<sub>d</sub>(x_). In Algorithm qPMS7, \(\mathcal{B}(x,d)\cup\mathcal{B}(y,d)\) is explored by traversing an acyclic graph, denoted as G_<sub>d</sub>(x,y_) with similar constructing rule as T_<sub>d</sub>(x_).

The time and space complexity of Algorithm qPMS7 are _O_((_n-q_+1)<sup>2</sup>_nm_<sup>2</sup>_n_<sub>B</sub>(_x,d_)) and _O(nm_<sup>2</sup>) respectively. So in worst case scenario the time runtime of qPMS7 is worse than that of Algorithm qPMSPrune by a factor of _n-q_+1. However, Algorithm qPMS7 is much faster than Algorithm qPMSPrune in practice.

**Algorithm 5** qPMS7

1: \(\mathcal{M}\leftarrow\emptyset\) 2: **for** _i_<sub>1</sub>=1 **to** _n-q_+1 **do** 3: **for** _j_<sub>1</sub>=1 **to** _m-l_+1 **do** 4: **for** _i_<sub>2</sub>=_i_<sub>1</sub>+1 **to** _n-q_+1 **do** 5: **for** _j_<sub>2</sub>=1 **to** _m-l_+1 **do** 6: \(\mathcal{T}\leftarrow\{S_h|1\le h\le N,h\neq i_1,h\neq i_2\}\) 7: qPMS7\_Tree(\(0,s_{i_1,j_1}^l,s_{i_2,j_2}^l,s_{i_1,j_1}^l,0,\mathcal{T}\)) 8: **end for** 9: **end for** 10: **end for** 11: **end for** 12: Output M

X = 1010 y = 1100 0100 1110 1000 0000 0110 0101 1100 1111 1001

Figure 3.2: G<sub>2</sub>(1010,1100) with alphabet \(\Sigma=\{0,1\}\)

