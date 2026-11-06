<tbc>the cut but not the flow. Observe that for unweighted graphs, any max flow uses at most _O(n_<sup>1.5</sup>) edges (Theorem A.3), but for weighted graphs the number of used edges can be as large as _O(n_<sup>2</sup>). So minimizing space complexity is generally harder for the weighted case.

### Regarding Accuracy

If we care only about the cost of the flow (or size of max-flow), then the algorithm’s output is exact by choosing \(\epsilon\le 1/3\) and then rounding the computed cost to the nearest integer.

If the minimum-cost flow is unique, then rounding each _f<sub>e</sub>_ to the nearest integer also results in the exact flow on each edge. If the flow is not unique, then the algorithm might compute a fractional flow and thus rounding is not guaranteed to provide an exact solution for the edges. However, given the logarithmic complexity dependence on \(\epsilon\), we can reduce the error to an arbitrary small \(\epsilon=1/\mathrm{poly}(n,W)\) on each edge. Thus we get an almost exact fractional min-cost flow \(f\in\mathbb{R}_{\ge 0}^E\).

Usually, uniqueness can be guaranteed via Isolation Lemma \[CRS95, DS08a\], which adds small random perturbation to the problem instance, but this requires large additional space to store \(\Omega(n^2)\) random bits. It is open whether _o(n_<sup>2</sup>) random bits suffice to isolate maximum/min-cost flows, and in our streaming algorithm we cannot afford to store these. This issue does not occur in the setting of communication complexity, as each player can independently store their own perturbed edge weights.

### Communication Complexity

There is a general reduction from 2-party communication to streaming, resulting in \(O(space\times passes)\) amount of communication, by simulating the streaming algorithm and sending the entire memory in each pass. While our streaming algorithm needs \(\widetilde{O}(n^{1.5})\) total space, it generates only \(\widetilde{O}(n)\) new information in each of the \(\widetilde{O}(\sqrt{n})\) passes. Thus it suffices to send only the \(\widetilde{O}(n)\) additional information in each pass, leading to \(\widetilde{O}(n^{1.5})\) communication.

**Theorem 1.2** (Min-cost Flow, Communication)**.** _There is a randomized communication protocol that, given an input graph G_=(_V,E_) _with integer capacities_ \(u\in[1,W]^E\) _and costs_ \(c\in[1,W]^E\)_, vertex demand vector_ \(b\in\mathbb{R}^V\)_, where the edges are split among two parties, computes w.h.p. an exact min-cost flow in_ \(\widetilde{O}(n^{1.5}\mathrm{log}(W))\) _communication. At the end, each party knows the amount of flow on each of their own edges._

Unlike Theorem 1.1, there is no \(\epsilon\) dependence in Theorem 1.2, because we can make the flow unique via Isolation-Lemma. A subquadratic communication algorithm for weighted flows (but also the simpler weighted _st_-min-cut problem where solutions have size _O(n_)) was stated as open problem in \[BBE<sup>+</sup>22\].

The same \(\widetilde{O}(n^{1.5})\)-communication bound is also obtained in concurrent work \[GJ25\]. We remark that 2-party communication is an easier model than multi-pass streaming, because each party can use unlimited amount of space. In particular, \[GJ25\] does not give a streaming algorithm because each party explicitly stores _f<sub>e</sub>_ on their own edges _e_, thus using \(\Omega(n^2)\) space.

### Space and Bit-Complexity

In above theorems, space is measured in words where each word can store a real number. The algorithms also work over Word-RAM and finite bit numbers, where each number is stored as fixed-point number using \(\widetilde{O}(\mathrm{log}(nW/\epsilon))\)-bit. Thus if we want to measure space complexity of Theorems 1.1 and 1.2 in bits, all space, communication and time complexities increase by a logarithmic \(\widetilde{O}(\mathrm{log}(nW/\epsilon))\) factor.

## 1.2 Techniques

Our algorithm is based on solving the linear program representation of min-cost flow. The linear program representation of related problems such as bipartite matching or transshipment to obtain streaming algorithms has been used before, e.g., in \[AJJ<sup>+</sup>22, LSZ<sup>+</sup>23, AG11\]. A natural approach for matching is to maintain the smaller _n_-dimensional dual iterate (i.e., fractional vertex cover). However, this does not extend to min-cost/maximum flows, because the capacity constraints increase the dimension of the dual solution from _n_ to _m+n_.

Our algorithm works by implementing the interior point method/central path method by \[BLL<sup>+</sup>21\], while maintaining the primal solution (i.e., flow) in low space, rather than the dual. One can show that for flows on the central path, an \(\widetilde{O}(n)\) space representation is possible<sup>3</sup>. Unfortunately, this observation does not directly<tbc>

<sup>3</sup>Technical details: Centered flows are minimizers of some potential function \(\Phi(x)\) subject to \(\mathbf{A}^\top x=b\) for edge-vertex incidence matrix **A** and demand \(b\in\mathbb{R}^V\). Minimizers satisfy \(\nabla\Phi(x)=\mathbf{A}y\) for some \(y\in\mathbb{R}^V\), thus by storing _y_ we can reconstruct _x_.

