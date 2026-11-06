## 8:4 Beating Trivial Time for Tricky Triangle Tasks

**An Attack on the 4-Cycle Problem.** Finally, we consider the notorious problem of detecting a 4-cycle in an undirected graph on _n_ nodes and _m_ edges. An _O(n_<sup>2</sup>)-time algorithm is known [33] and an _O(m_<sup>4/3</sup>)-time algorithm is known [6], but these running times coincide when the number of edges is \(\Theta(n^{1.5})\). Indeed, the "hard case" of 4-cycle detection is when the graph has _O(n_<sup>1.5</sup>) edges: Bondy and Simonovits showed that any graph with _cn_<sup>1.5</sup> edges for sufficiently large constant _c_ must have a 4-cycle [11], and works due to Brown and Erdős, Rényi, and Sós gave algebraic constructions of 4-cycle free graphs that match this bound [12, 21]. There are essentially no hardness results known for the detection version of this problem, and yet no algorithmic improvements are known beyond the _O(n_<sup>2</sup>)-time solution, which enumerates pairs of neighbors of nodes and looks for a collision. We note that by contrast, much progress has been made on 4-cycle listing. In particular, there is a _O_(min(_n_<sup>2</sup>_,m_<sup>4/3</sup>)+_t_) time algorithm [2], where _t_ is the number of 4-cycles, along with a matching lower bound under the 3SUM hypothesis [1, 28].

We give two results on 4-cycle detection. First, building on our ideas for finding triangles in sparse graphs, we reduce 4-cycle detection to a variant of the Element Distinctness problem.

\(\blacktriangleright\) **Definition 5** (Concatenated Element Distinctness)**.** _We are given k lists L_<sub>1</sub>_,...,L<sub>k</sub>, where each list has n elements of_ \(\ell\)_-bit strings. For every_ \(i,j\in[k]\)_, element-wise concatenate them to a produce a new list L<sub>i,j</sub> containing n elements, each of which now have_ \(2\ell\) _bits. The task is to decide whether or not for all_ \(i\neq j\)_, all n strings in L<sub>i,j</sub> are distinct._

In other words, the _k_ lists form _O(k_<sup>2</sup>) instances of Element Distinctness on _n_ elements, and we accept if and only if all of the generated instances have distinct elements.

\(\blacktriangleright\) **Theorem 6.** _For_ \(T(n,k,\ell)\ge n+k+\ell\)_, if Concatenated Element Distinctness can be solved in_ \(O(T(n,k,\ell))\) _time, then 4-cycle detection in n-node graphs can be done in_ \(O(T(n,\sqrt{n},(log_2n)/2))\) _time._

Motivated by this reduction, we show how to sort _n_ items over a universe of size 2_<sup>u</sup>_ in _O(nu_log_n)/w_ time in the AC0 Word RAM model on _w_-bit words. Prior work either required more complex word operations such as 2_<sup>w</sup>_-size lookup tables [13], or extra logarithmic factors [4]. As sorting easily solves Element Distinctness, we obtain the following:

\(\blacktriangleright\) **Theorem 7.** _We can detect a 4-cycle in n-node graphs in O(n_<sup>2</sup>log<sup>2</sup>_n)/w time in the_ AC0 _Word RAM._

For word size \(w\le log^2n\), this result is suboptimal, as we already know an _O(n_<sup>2</sup>)-time algorithm when \(w=\Theta(logn)\). Nevertheless, it was not obvious how to improve over _O(n_<sup>2</sup>) time even for large word sizes: the known algorithms involve making _O(n_<sup>2</sup>) unstructured probes into a table, enumerating all pairs of neighbors of a given node to find a common pair of neighbors. We believe the reduction of Theorem 6 may be useful for future work.

**Sublinear Time 4-Cycle Detection in Denser Graphs.** Finally, we observe that 4-cycles can be found surprisingly quickly in graphs that have slightly more than _n_<sup>1.5</sup> edges. In fact, they can be found in _sublinear time_ in the number of edges.

\(\blacktriangleright\) **Theorem 8.** _There is a Las Vegas algorithm that, given a graph with n vertices and at least_ \(n^{3/2+\delta}\) _edges for_ \(\delta\in(0,\frac{1}{2})\)_, returns a 4-cycle and runs in expected_ \(O(n^{5/4-\delta/2})\) _time._

Therefore, on graphs with \(\varepsilon n^{3/2}\) edges where \(\varepsilon>0\) is a small constant, the best known method for detecting (and finding) a 4-cycle remains _O(n_<sup>2</sup>) time. However, on graphs

