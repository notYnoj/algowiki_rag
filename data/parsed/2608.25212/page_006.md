Previous work on APSP includes an O(_n_<sup>2</sup>log<sup>2</sup>_n_)-time algorithm in classes of bounded twin- width, and in time O(_n_<sup>2</sup>log_n_) on graphs of bounded radius-1 merge-width given with a witness \[12\]. More recently, the O(_n_<sup>2</sup>log<sup>2</sup>_n_)-time APSP algorithm was extended to classes of linear neighborhood complexity \[18\]. In \[13\], an O(_n_<sup>2</sup>log_n_)-time APSP algorithm was given on graphs of bounded twin- width given with their contraction sequence, which was then improved to O(_n_<sup>2</sup>)-time in the paper introducing DAG-compressions \[5\].

Note that Theorems 2 and 5, together with \[12, 11\], also give a randomized O(_kn+m_)-time algorithm for Multi-Source Shortest Path from _k_ sources on _n_-vertex _m_-edge graphs. Another consequence of Theorem 1 and results in \[12\] (see Lemma 14) is:

**Theorem 7.** _For every graph class_ C _of linear neighborhood complexity, there is an_ O<sub>C</sub>(_n_<sup>2</sup>)_-time algorithm that, given any adjacency matrix M of an n-vertex graph of_ C_, yields a data structure that computes the matrix-vector product MX in time_ O<sub>C</sub>(_n_) _for any n-vector X._

_In particular, the product MN can be computed in_ O<sub>C</sub>(_n_<sup>2</sup>) _time for any_ \(n\times n\) _matrix N._

We refer to Fig. 2 for a diagram of the algorithmic pipeline discussed in the previous few paragraphs.

Theorem 6 answers \[12, Question 2\] positively, far beyond classes of bounded twin-width (for which the question was asked). Theorems 6 and 7 improve APSP and matrix-multiplication algorithms in \[14, 2, 12, 35, 18\], all of which have extra polylog factors, and extend results in \[36, 5\], which work on graphs of bounded clique-width and on graphs of bounded twin-width given with contraction sequences, respectively.

By using Theorem 3 rather than Theorem 1, one can solve All-Pairs Shortest Path in graphs of VC density \(\rho\) (or multiply the adjacency matrix of graphs of VC density \(\rho\) with any matrix) in time \(\mathcal{O}(n^{3-1/\rho})\). However, we observe that fast matrix multiplication and Seidel’s algorithm \[47\] have a better running time in general instances as soon as \(\rho>1.591\).

We also obtain a time-optimal triangle-detection algorithm in classes of linear neighborhood complexity, which leverages an sd-degeneracy sequence of constant width.

**Theorem 8.** _For every graph class_ C _of linear neighborhood complexity, Triangle Detection can be solved in expected time_ O<sub>C</sub>(_n+m_) _on n-vertex m-edge graphs of_ C.

Let us recall that on general graphs, the fastest known Triangle Detection algorithm runs in time \(\mathcal{O}(min(n^\omega,m^{2\omega/(\omega+1)}))\) \[1\] where \(\omega\) is the exponent of square matrix multiplication, which currently implies O(min(_n_<sup>2.372</sup>_,m_<sup>1.407</sup>)) time.

Utilizing both an sd-degeneracy sequence and a Welzl order of the input graph, we obtain randomized almost-linear algorithms for finding 4-vertex and 5-vertex cliques, and a deterministic O(_n_<sup>2</sup>)-time algorithm for _K_<sub>4</sub> detection (time-optimal within dense graphs).

**Theorem 9.** _For every graph class_ C _of linear neighborhood complexity, a K_<sub>4</sub> _subgraph can be found in expected_ O<sub>C</sub>(_n_log<sup>5</sup>_n+m_log_n_) _or in deterministic_ O<sub>C</sub>(_n_<sup>2</sup>) _time on n-vertex m-edge graphs of_ C.

**Theorem 10.** _For every graph class_ C _of linear neighborhood complexity, a K_<sub>5</sub> _subgraph can be found in expected time_ O<sub>C</sub>(_n_log<sup>9</sup>_n+m_log<sup>5</sup>_n_) _on n-vertex m-edge graphs of_ C.

Prior to our work, no linear-time algorithm was known for Triangle Detection in the much more restricted classes of bounded clique-width, nor was an almost-linear algorithm known in classes of bounded twin-width (where, for both, the input is a mere graph without a witness of low width).

