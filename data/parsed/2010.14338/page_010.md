since we can handle pairs with _x(p)\<x(q_) and _y(p)\>y(q_) symmetrically.

**Definition 8** (Left & right demand segments)**.** Let (_P,D_) be an input instance. For \(R(p,q)\in Q\), denote by \(\lambda(p,q)\) the vertical segment that connects (_x(p),y(p_)) and (_x(p),y(q_)). Similarly, denote by \(\rho(p,q)\) the vertical segment that connects (_x(q),y(p_)) and (_x(q),y(q_)). That is, \(\lambda(p,q)\) and \(\rho(p,q)\) are simply the left and right boundaries of rectangle _R(p,q_).

**Boundary Independent Sets.** A _left boundary independent set_ consists of pairwise non- overlapping segments \(\lambda(p,q)\), a _right boundary independent set_ of pairwise non-overlapping segments \(\rho(p,q)\). A _boundary independent set_ refers to either a left or a right boundary independent set. Denote by IS(_P,D_) the size of a maximum boundary independent set.

The following lemma implies that it suffices to work with boundary independent sets instead of vertical separability. The main advantage of doing so, is that (i) for IS, we do not have to identify any ordering of the demand subset, (ii) one can compute IS(_P,D_) efficiently, and (iii) we can exploit geometric properties of interval graphs, as we will do below.

**Lemma 9.** _For any instance_ (_P,D_) _we have that_ \(\mathsf{IS}(P,D)\unknown\mathsf{VS}(P,D)\)_. Moreover, one can compute a maximum boundary independent set in polynomial time._

_Proof._ Let \(I\subseteq D\) be a maximum boundary independent set, and let _b_ be the vertical line corresponding to the smallest _x_-coordinate of the input points. Assume _I_ consists of left sides of demand rectangles. Consider all the demands \((p,q)\in I\) where \(\lambda(p,q)\) lies on the vertical line _b_. Since the left sides of the corresponding demand rectangles form an independent set we can cut them in any order along _b_ without intersecting any other demand in _I_. We can then remove these demands and proceed recursively to the next smallest _x_-coordinate until all demands have been cut. This completes the proof of the inequality.

Now, we discuss efficient computability. Note that a left (and thus a right or general) maximum boundary independent set can be computed efficiently by determining a maximum independent set of the intervals \(\lambda(p,q)\) for \((p,q)\in D\) along all _x_-coordinates separately. The maximum independent set of intervals can be computed in polynomial time \[19\].

**Algorithm Description.** In Algorithm 1, we present algorithm HorizontalManhattan, which produces a Manhattan solution of cost \(O(logs)\cdot\mathsf{IS}(P,D)\), where _s_ is the number of _x_-groups in _P_. The algorithm initially computes a set of "crucial rows" \(\mathcal{R}\subseteq\mathbb{R}\) by computing a minimum hitting set in the interval set \(\mathcal{I}=\{[y(p),y(q)]|(p,q)\in D\}\). In particular, the set R has the following property. For each \(j\in\mathcal{R}\), let \(\ell_j\) be a horizontal line drawn at _y_-coordinate _j_. Then the lines \(\{\ell_j\}_{j\in\mathcal{R}}\) stab every rectangle in \(\{R(p,q)\}_{(p,q)\in D}\). The following observation follows from the fact that the interval hitting set is equal to the maximum interval independent set.

_Observation_ 1. \(|\mathcal{R}|\unknown\mathsf{IS}(P,D)\)

After computing R, the algorithm calls a subroutine HorizontalDC (see Algorithm 2), which recursively adds points to each such row in a way that guarantees a feasible solution.

**Analysis.**

**Lemma 10** (Feasibility)**.** _The algorithm_ HorizontalManhattan _produces a feasible solution in polynomial time._

