### 3.3 Key structural ideas

Abstracting away the grid geometry reveals two structural components driving Hirschberg’s efficiency:

• **Topological bisection.** The column _k_ acts as a balanced separator in the topological order induced by the grid. Splitting the problem at _k_ ensures the recursion depth is _O_(log_n_), i.e., logarithmic in one dimension of the topological order.<tbc>

• **Meet-in-the-middle evaluation.** The set of candidate "midpoint" vertices consists of those on the cut column _k_ that lie on some path from source to sink. By combining forward values _f(i_) and backward values _g(i_) at these midpoints, the algorithm locates a vertex which _must_ lie on an optimal path. When the same deterministic tie-breaking is used in all DP evaluations, the argmax of _f(i_)+_g(i_) picks out a canonical midpoint along the canonical optimal path.

Our generalization addresses the following question:

_Can we replicate this divide-and-conquer strategy on an arbitrary DP DAG where no geometric symmetry exists and where "backward" evaluation may be computationally expensive or wide?_

We answer in the affirmative. We will demonstrate that any DAG with small frontier width admits a recursive decomposition into balanced intervals of the topological order, and that one can perform meet-in-the-middle traceback using _only forward_ DP evaluations. The key idea is to recompute suffix costs via local forward DPs, trading time for space, and to organize the recursion via a height-compressed decomposition of the time line.

## 4 Height-Compressed Recursion for DP DAGs

We now construct the structural framework for our algorithm: a hierarchical decomposition of the time-ordered DP DAG together with a notion of local interfaces. This construction mirrors the height- compressed computation trees employed in time-space tradeoff results for Turing machines, but here we exploit random access to the input and are free to recompute local DPs as often as needed while keeping the working frontier bounded by the frontier width.

### 4.1 Recursive decomposition of the time order

Recall that \(\tau:V\rightarrow\{1,\dots,T\}\) defines a fixed topological ordering of the vertices. For the remainder of the exposition, we identify each vertex with its topological index, setting _V_={1_,...,T_} and \(\tau(v)=v\). Edges \((u,v)\in E\) thus satisfy _u\<v_.

We partition the computation not by geometry, but by contiguous intervals of topological time.

**Definition 4** (Interval and midpoint split)**.** _Let I_=\[_i,j_\] _be an interval of indices with_ \(1\le i\le j\le T\)_. We define the_ midpoint _of I as_

\(m(I):=\big\lfloor(i+j)/2\big\rfloor.\)

_The interval I is partitioned into two disjoint sub-intervals: the_ left child _I<sub>L</sub>_=\[_i,m(I_)\] _and the_ right child _I<sub>R</sub>_=\[_m(I_)+1_,j_\].

This bisection scheme induces a canonical binary tree over the time axis.

**Definition 5** (Recursion tree)**.** _The_ recursion tree R _for the time domain_ \[1_,T_\] _is the rooted binary tree defined inductively:_

• _the root of_ R _is the interval_ \[1_,T_\];<tbc>

• _every internal node I_=\[_i,j_\] _(with i\<j) has exactly two children: I<sub>L</sub> and I<sub>R</sub>;_<tbc>

• _the leaves of_ R _are singleton intervals_ \[_k,k_\] _with_ \(k\in\{1,\dots,T\}\).

_In our algorithm we will stop the recursion earlier, at a base-case size_ \(B_\mathrm{base}\ge 1\)_, so leaves will correspond to intervals of length at most B_<sub>base</sub>.

**Lemma 2** (Logarithmic depth)**.** _The depth of the recursion tree_ R _is O_(log_T). Moreover, for any node I at depth d, the length of the interval satisfies_ \(|I|\le\lceil T/2^d\rceil\).

