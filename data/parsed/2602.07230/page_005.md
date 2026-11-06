_Proof._ In the augmentation step, flow is increased along backward paths and decreased along forward paths by the same amount, preserving the excess (inflow minus outflow) at each vertex, thus maintaining a flow that meets all current demands. \(\square\)<tbc>

(ii) At the beginning of each iteration, every vertex contains at most one irregular sink. If a vertex does contain an irregular sink, then its out-degree is zero and it also contains a regular sink. In particular, every vertex that contains sinks has at least two incoming arcs.<tbc>

<tbc>_Proof._ We refer to the proof of Lemma 3.2 in \[DGG99\]. \(\square\)

Notice that the last part of this invariant is crucial for the construction of alternating cycles since it guarantees that, for each junction vertex, there exists an incoming arc different from the forward arc used to reach it such that a backward path can be constructed.<tbc>

(iii) A singular arc is removed at the end of an iteration in which any sink moves along it.<tbc>

<tbc>_Proof._ A sink moves along a singular arc in an iteration only when the flow on that arc exactly matches the demand of that sink before moving. \(\square\)

Until an arc _a_ becomes singular, its flow never increases and the total demand of sinks moved along it is bounded by its initial flow value _x<sub>a</sub>_. Once _a_ is singular, at most one sink with demand at most _d_<sub>max</sub> can move along it before _a_ disappears. Thus, in the final unsplittable flow, the flow on any arc is less than _x<sub>a</sub>+d_<sub>max</sub>. We refer the interested reader to \[DGG99\] for further details.

## 3 Modified DGG Algorithm for unsplittable transshipments

In this section, we modify the DGG Algorithm and its analysis in order to compute unsplittable transshipments with bounded congestion. We are given an acyclic digraph _D_=(_V,A_) with a set of sources _S_<sup>+</sup> and a set of sinks _S_<sup>-</sup>, together with supplies and demands specified by a balance function \(b:V\rightarrow\PazoBB{R}\) and a fractional _b_-transshipment _x_. We first transform this unsplittable transshipment instance into an SSUF instance by introducing a super-source _s_<sup>∗</sup> and dummy arcs (_s_<sup>∗</sup>_,s_) to each source \(s\in S^+\), each carrying flow _x_<sub>(_s_<sup>∗</sup>_,s_)</sub>:=_b(s_), and by setting _d<sub>t</sub>_:=|_b(t_)| for all sinks \(t\in S^-\).

However, applying the DGG Algorithm to the resulting SSUF instance does not necessarily yield a valid _b_-transshipment. During the execution of the algorithm, the flow on dummy arcs (_s_<sup>∗</sup>_,s_) that lie on alternating cycles may be modified, which can result in an unsplittable flow that no longer satisfies the fixed supply constraints at the sources \(s\in S^+\).

On the other hand, the DGG Algorithm routes the entire demand of each sink along a single path and does not exploit the possibility of sending flow into a sink along multiple paths originating from different sources in _S_<sup>+</sup>. The central idea of our Modified DGG Algorithm is to leverage this flexibility in order to keep the flow on dummy arcs (_s_<sup>∗</sup>_,s_), and hence the supplies at the sources, fixed.

### 3.1 Description of the Modified DGG Algorithm

As in the original DGG Algorithm, the Modified DGG Algorithm begins with the flow _y_:=_x_ and, in a preliminary phase, iteratively moves sinks backward toward the super-source _s_<sup>∗</sup> along flow-carrying arcs incident to sinks whose flow meets or exceeds their demands. After the preliminary phase, the algorithm iteratively attempts to construct alternating cycles that do not contain the super-source _s_<sup>∗</sup>. Augmenting flow along a cycle that includes _s_<sup>∗</sup> would modify the flow on arcs (_s_<sup>∗</sup>_,s_) and thus alter the fixed supply values of such sources \(s\in S^+\). We therefore proceed as follows.

