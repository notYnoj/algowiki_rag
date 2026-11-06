## 4.3 Matrix Transpose

In this subsection, we reprove the lower bound of Adler et al. \[1\] for external memory matrix transpose algorithms, however this time without an assumption of obliviousness. Let the input to the matrix transpose problem be an \(n\times n\) matrix _A_, with _w_-bit integer entries. The matrix _A_ is stored in row-major order, meaning that we have _n/B_ disk blocks for each input row of _A_. The first such disk block stores the first _B_ entries of the row and so on. The goal is to compute _A<sup>T</sup>_, i.e. output _n/B_ blocks per column of _A_, containing the corresponding entries in order.

Let A be a randomized algorithm for transposing an \(n\times n\) matrix in expected _O(t_) I/Os, having error probability at most 1/3. By aborting A when it spends more than 6_t_ I/Os, we obtain an algorithm with worst case _t_<sup>∗</sup>=_O(t_) I/Os and error probability 1/2. We re-define _t_ to equal this new worst case number of I/O’s (to avoid having to write _t_<sup>∗</sup> or 6_t_ in all places). As in our proof of the external memory sorting lower bound, we can again define the I/O-graph _G_ corresponding to an execution of A on a matrix _A_. This graph again has an input block node for each block in the rows of _A_ and an output block node for each block in the rows of _A<sup>T</sup>_ (columns of _A_).

Consider the execution of A on a uniform random matrix _A_ (each entry is chosen independently as a _w_-bit integer). We now fix the random choices of this algorithm to obtain a deterministic algorithm A<sup>∗</sup> with the same error probability over the random input matrix _A_. As in our proof of the sorting lower bound, we now fix an I/O-graph which is the result of running A<sup>∗</sup> on many different matrices:

**Lemma 14** _There exists a set_ \(\Gamma\) _containing at least_

\(\frac{2^{n^2w}}{2(t+2n^2/B+1)^{t+1}}\)

_different input matrices A, such that_ A<sup>∗</sup> _is correct on all matrices_ \(A\in\Gamma\) _and the I/O-graph is the same for all_ \(A\in\Gamma\).

**Proof.** First we bound the number of different I/O graphs that may result from the execution of A<sup>∗</sup> (equivalent of Lemma 9). There are 2_n_<sup>2</sup>_/B_ initial block nodes, hence each I/O accesses one of at most _t_+2_n_<sup>2</sup>_/B_+1 nodes (the plus one to account for the creation of a new node). There are _t_+1 choices for the number of I/Os. Thus the number of distinct I/O-graphs that may result from the execution of A<sup>∗</sup> is no more than \((t+1)(t+2n^2/B+1)^t\le(t+2n^2/B+1)^{t+1}\). The lemma follows by observing that A<sup>∗</sup> is correct on at least 2<sup>_n_<sup>2</sup>_w_</sup>/2 input matrices.

We can again define the distance that an entry of an input matrix _A_ has to travel in an I/O- graph _G_. Formally, define dist(_i,j,G_) to be the distance from the input block node in _G_ storing the entry (_i,j_), to the output block node in _G_ storing the entry (_i,j_) after the transpose. We have the following equivalent of Lemma 10:

**Lemma 15** _For any I/O-graph G, there are at least_ (4/5)_n_<sup>2</sup> _entries_ (_i,j_) _for which_ \(dist(i,j,G)\ge(1/2)lg_{2m/b}B\).

**Proof.** The degree of nodes in _G_ is at most 2_m/b_. Thus for any input block node, there can be at most (2_m/b)<sup>d</sup>_ output block nodes in _G_ within distance _d_. But all entries of an input block node have distinct destination output block nodes. This is true since all entries in an input block node resides in the same row of _A_ and hence reside in distinct columns. Thus there can be at most \(\sqrt{B}\) indices _j_ among the _B_ indices in an input block for which \(dist(i,j,G)\le(1/2)lg_{2m/b}B\). The lemma follows immediately.

