## 4 External Memory Lower Bounds

As mentioned in the proof overview in Section 3, we prove our lower bound for external memory sorting via a lower bound for the easier problem of permuting: An input to the permutation problem is specified by a permutation \(\pi\) of {1,2_,...,n_} as well as _n_ bit strings \(d_1,\dots,d_n\in\{0,1\}^w\). We assume \(w\ge lgn\) such that all bit strings may be distinct. The input is given in the form of an array _A_ where the _i_’th entry _A_\[_i_\] stores the tuple \((\pi(i),d_i)\). We assume the input is given in the following natural way: Each \(\pi(i)\) is encoded as a \(\lceil lgn\rceil\)-bit integer and the _d<sub>i</sub>_’s are given as they are - using _w_ bits for each.

The array _A_ is presented to an external memory algorithm as a sequence of blocks, where each block contains \(\lfloor b/(w+lgn)\rfloor\) consecutive entries of _A_ (the blocks have _b=Bw_ bits). For simplicity, we henceforth assume (_w_+l_n_) divides _b_.

The algorithm is also given an initially empty output array _C_. The array _C_ is represented as a sequence of _n_ words of _w_ bits each, and these are packed into blocks containing _b/w_ words each. The goal is to store \(d_{\pi^{-1}(i)}\) in _C_\[_i_\]. That is, the goal is to _copy_ the bit string _d<sub>i</sub>_ from _A_\[_i_\] to \(C[\pi(i)]\). We say that an Algorithm A has an error of \(\varepsilon\) for the permutation problem, if for every input to the problem, it produces the correct output with the probability at least \(1-\varepsilon\).

The best known upper bounds for the permutation problem work also under the _indivisibility_ assumption. These algorithms solve the permutation problem in

\(O\left(min\left\{n,\frac{nw}{b}\cdot lg_{m/b}(nw/b)\right\}\right)=O\left(min\left\{n,\frac{n}{B}\cdot lg_{M/B}(n/B)\right\}\right)\)

I/Os \[2\]. Moreover, this can easily be shown to be optimal under the indivisibility assumption by using a counting argument \[2\]. The _n_ bound is the bound obtained by running the naive "internal memory" algorithm that simply puts each element into its correct position one at a time. The other term is equivalent to the optimal comparison-based sorting bound (one thinks of _d<sub>i</sub>_ as an integer in \[2_<sup>w</sup>_\] and concatenates \(\pi(i)\circ d_i=\pi(i)\cdot 2^w+d_i\) and sorts the sequence). Thus any sorting algorithm that handles (l_n+w_)-bit keys immediately yields a permutation algorithm with the same number of I/Os. We thus prove lower bounds for the permutation problem and immediately obtain the sorting lower bounds as corollaries.

We thus set out to use Conjecture 1 to provide a lower bound for the permutation problem in the external memory model. Throughout the proof, we assume that _nw/b=n/B_ is at least some large constant. This is safe to assume, as otherwise we only claim a trivial lower bound of \(\Omega(1)\).

Let A be a randomized external memory algorithm for the permutation problem on _n_ integers of _w_ bits each. Assume A has error probability at most 1/3 and let _b_ denote the disk block size in number of bits. Let _m_ denote the memory size measured in number of bits. Finally, let _t_ denote the expected number of I/Os made by A (on the worst input).

### I/O-Graphs.

For an input array _A_ representing a permutation \(\pi\) and bit strings _d_<sub>1</sub>_,...,d<sub>n</sub>_, and an output array _C_, define the (random) I/O-graph _G_ of A as follows: Initialize _G_ to have one node per disk block in _A_ and one node per disk block in _C_. Also add one node to _G_ representing the initial memory of A. We think of the nodes representing the disk blocks of _A_ and _C_ as _block nodes_ and the node representing the memory as a _memory node_ (see Figure 1a). We will add more nodes and edges to _G_ by observing the execution of A on _A_. To simplify the description, we will call nodes of _G_ either _dead_ or _live_. We will always have at most one live memory node. Initially all nodes are live. Moreover, we label the block nodes by consecutive integers starting at 0. Thus the block nodes in the initial graph are labeled 1,2_,...,n(w_+l_n)/b+nw/b_.

