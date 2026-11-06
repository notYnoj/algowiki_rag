## F Towards Better Approximation

In this section, we state some structural properties and show that these would imply a better approximation ratio of _O_(loglog_n_). Furthermore, we prove that those properties hold for a special class of demands.

### F.1 Structural Properties for _O_(loglog_n_)-approximation

Let _f_ be a lower bound function on OPT, that is \(f(P,D)\le O(\mathsf{OPT}(P,D))\) for any input (_P,D_). We say that _f_ satisfies _subadditivity_ if for any strip partitioning S, we have

\(f(\pi_\mathcal{S}(P,D))+\sum_{S\in\mathcal{S}}f(P\cap S,D\cap(S\times S))\le f(P,D).\)

For any lower bound function _f_, an _f-sparsification algorithm_ is an efficient algorithm that, on input (_P,D_), produces an instance \((\tilde{P},\tilde{D})\) such that (i) any feasible solution _Q_ for \((\tilde{P},\tilde{D})\) is feasible for (_P,D_) as well, and (ii) \(|\tilde{P}|=O(f(\tilde{P},\tilde{D}))\). The following theorem is given implicitly in \[1\]. The proof is a verbatim adaptation of the original proof and therefore omitted.

**Theorem 21.** _Let f be a lower bound function. Assume that f is subadditive and that there exists an f-sparsification algorithm. Then there exists an efficient algorithm for_ MinGMConn _producing a solution of cost at most_ \(O(\mathrm{loglog}n)f(P,D)\le O(\mathrm{loglog}n)\mathsf{OPT}(P,D)\).

We do not know how to prove the existence of sparsification algorithms for general instances and leave this as an interesting open problem. However, we will show that such an algorithm exists when the demand graph is a complete _k_-partite graph.

The existence of a sparsification algorithm can be seen as a stronger property than the previously considered existence of an _O_(log_s_)-approximation algorithm when input points have at most _s_ distinct _x_-coordinates.

**Lemma 22.** _If there exists an f-sparsification algorithm for an instance_ (_P,D_) _with at most s distinct x-coordinates, then there exists an algorithm that returns a solution with cost at most O_(log_s)f(P,D)._

_Proof._ The algorithm is as follows. First, apply the _f_-sparsification algorithm on (_P,D_) to obtain \((P',D')\). Specifically, we have that \(|P'|\le O(f(P,D))\). We say that an _x_-coordinate is active if there is an input point on it. Draw a vertical partitioning line \(\ell\) in the middle such that there are \(\lceil s/2\rceil\) active _x_-coordinates to the left of \(\ell\) and the rest to the right. Let S consist of the two strips _S<sub>L</sub>,S<sub>R</sub>_ resulting from drawing the line \(\ell\). That is the strips _S<sub>L</sub>_ and _S<sub>R</sub>_ are the regions on the left and right of line \(\ell\) respectively. For each point \(p\in P'\), we add a point \(p'\) to the solution that lies on \(\ell\) and is horizontally aligned with _p_. Notice that this satisfies all demands crossing \(\ell\). Next, we recurse inside \((P'\cap S_L,D'\cap(S_L\times S_L))\) and \((P'\cap S_R,D'\cap(S_R\times S_R))\). It is easy to see that this algorithm produces a feasible solution.

To analyze the cost, notice that there are _O_(log_s_) levels of recursions. The input instance is called _level_-0 _instance_ and creates 2 sub-instances (called _level_-1 _instances_) and so on until the last level instances. There are at most 2_<sup>j</sup>_ level-_j_ instances. Let I_<sub>j</sub>_ be the collection of all level- _j_ instances. Note that the instances in I_<sub>j</sub>_ lie on 2_<sup>j</sup>_ different strips which are pairwise disjoint. Additionally, each \((\hat{P},\hat{D})\in\mathcal{I}_j\) creates \(O(f(\hat{P},\hat{D}))\) points before making recursive calls, so the total cost of level-_j_ recursions is \(O(\sum_{(\hat{P},\hat{D})\in\mathcal{I}_j}f(\hat{P},\hat{D}))\). Since these instances \((\hat{P},\hat{D})\in\mathcal{I}_j\) lie on disjoint strips, we have that \(O(\sum_{(\hat{P},\hat{D})\in\mathcal{I}_j}f(\hat{P},\hat{D}))\le O(f(P,D))\).

