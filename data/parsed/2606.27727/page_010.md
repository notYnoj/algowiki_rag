## 8:10 Beating Trivial Time for Tricky Triangle Tasks

associated with. We will connect its output to every _G<sub>j</sub>_ such that the _j_th bit of the binary representation of _i_ is one. Correctness follows from the fact that at most one of the depth-two circuits will output a 1, so only the _G<sub>j</sub>_’s associated with the set bits of that index will be 1. The bottom level of the circuit has _w_ input bits, the fan-in of each of the _n_ ANDs is at most _w_, and the fan-in of each of the log_w_ ORs is at most _n/_2. Thus, the circuit has polynomial size and depth two, and is therefore AC0. \(\blacktriangleleft\)

Note that we can call this procedure, zero out the associated bit, and then repeat to extract the indices of all of the ones in a particular indicator mask. This only requires us to pay _O_(1) time per set bit whose index we retrieve.

## 4 A Faster Algorithm for All-Edges Sparse Triangle

Armed with the compressed list operations from above, we are ready to solve triangle problems faster. We begin with a subquadratic algorithm for Sparse Triangle Detection, which is quite natural but is not strong enough to solve the All-Edges version faster. The goal here is to emphasize the relationship between triangle problems and equality product-like problems, and to motivate the reduction to set intersection that we will present in Section 4.2.

## 4.1 Warm-Up: Solving Sparse Triangle Detection Faster

We will solve sparse triangle detection by reducing to the following problem:

\(\blacktriangleright\) **Definition 19 (All-Edges Equality Inner Product).** _Let_ \(\delta\in(0,0.5]\) _and_ \(d=O(n^\delta)\)_. Given an_ \(n\times d\) _matrix A and an_ \(d\times n\) _matrix B with entries in_ \([n^{1-\delta}]\cup\{\perp\}\)_, as well as a set P of_ \(O(n^{1+\delta})\) _points in_ \([n]\times[n]\)_, is there an_ (_i,j_) _in P and a value of_ \(k\in[n^\delta]\) _such that_ \(v:=A[i,k]=B[k,j]\) _and_ \(v\neq\perp\)?

\(\blacktriangleright\) **Theorem 20.** _There is a_ \(O(n^{1+\delta})\)_-time randomized reduction from the triangle detection problem on graphs of maximum degree_ \(O(n^\delta)\) _to All-Edges Equality Inner Product. When there is no triangle in the original graph, the All-Edges Equality Inner Product instance is a no instance. When there is a triangle, the All-Edges Equality Inner Product instance is a yes instance with constant nonzero probability._

**Proof of Theorem 20.** We assume without loss of generality that _G_ is tripartite, with parts _I_, _J_, and _K_ each of size at most _n_. We begin by "color-coding" vertices as in [5], but with a large color palette. We impose the following rule: every vertex in \(I\cup J\) has an edge to at most one vertex per color class of _K_. To enforce this, if a vertex \(u\in(I\cup J)\) has multiple edges to one color class, we will select one uniformly at random to keep and delete the rest. We show that every triangle (_u,v,w_) in the graph survives with constant probability.

Suppose we have a pairwise independent hash family \(\mathcal{H}=\{h:[n]\rightarrow[Cn^\delta]\}\) for large constant _C_, where each \(h\in\mathcal{H}\) corresponds to a coloring of the vertices of _K_ with \(Cn^\delta\) colors. Suppose \(u\in I\), \(v\in J\) and \(w\in K\) form a triangle. Let _N(u_) and _N(v_) denote the neighbors of _u_ and _v_ in _K_, respectively. The probability that the triangle _u,v,w_ survives is

