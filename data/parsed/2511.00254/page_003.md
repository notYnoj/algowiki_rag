**Theorem 1.1.** _Let G be a planar graph with a fixed embedding. Let H be such that for any pair of demands_ \(h_1,h_2\in E(H)\)_, h_<sub>1</sub> _and h_<sub>2</sub> _can be embedded inside (possibly different) faces of G so they do not cross each other. Then_ (_G,H_) _is an uncrossable layout._

We say any (_G,H_) satisfying this property is _pairwise-planar_ (see Figure 6 in Section 3 for a depiction). The pairwise-planar class includes fully-planar as a subset, but includes substantially more. For instance, it contains layouts where _G+H_ is highly non-planar (and thus, do not admit laminar flows). It also includes the 2-connected _fully-compliant_<sup>2</sup> family introduced in \[7\], which were not previously known to give uncrossed layouts to our knowledge. Pairwise-planar also differs from previous uncrossable layouts in an important structural sense. Namely, fully-planar and single-source (_G,H_) are _cut-sufficient_ (essentially, they have a Max-Flow Min-Cut theorem in the congestion setting), while some pairwise-planar (_G,H_) are not.

As for Question 2, we prove the following results. We begin with the maximization setting.

**Theorem 1.2.** _Let_ (_G,H,u_) _be a planar maximization instance where u is integral. Let f be a feasible fractional flow that is uncrossed. There exists a feasible integral flow_ \(f'\) _that achieves an_ \(\Omega(1)\) _fraction of the value of f. This integral flow can be computed in polynomial time._

We prove this result by establishing an "approximate integer decomposition property", exploiting colouring results on a restricted class of string graphs (path intersection graphs). This integer decomposition also implies \(\Omega(1)\) rounding holds for the _weighted_ maximization version, where each \((s,t)\in E(H)\) has an associated weight _w(s,t_), and a flow achieves _w(s,t_) value for each unit of (_s,t_)-flow that it routes. Additionally, this result extends to _node-capacitated_ multiflows (i.e. _u_ is a capacity function on nodes rather than edges).

For the congestion setting, we give a factor 2 rounding for converting a fractional uncrossed multiflow into an integral multiflow. Moreover, for an extra additive penalty we can round to an unsplitable flow.

**Theorem 1.3.** _Let_ (_G,H,u,d_) _be a planar congestion instance where u,d are integral. Let f be a feasible fractional multiflow that is strongly uncrossed_<sup>3</sup>_. Then there exists both:_

1. _an integral multiflow_ \(f'\) _that is feasible for_ \((G,H,u',d)\) _where_ \(u'(e)\le 2u(e)\) _for each_ \(e\in E(G)\)_, and_<tbc>

_2._ _an unsplittable multiflow_ \(f''\) _that is feasible for_ \((G,H,u'',d)\) _where_ \(u''(e)<2u(e)+d_\mathrm{max}\) _for every_ \(e\in E(G)\)_, where_ \(d_\mathrm{max}=\mathrm{max}_{h\in E(H)}d(h)\).

_The integral and unsplittable multiflows can be computed in polynomial time._

Using Theorems 1.1, 1.2, and 1.3, we obtain constant-factor approximation algorithms for integer multiflow problems with pairwise-planar inputs.

**Corollary 1.4.** _There exist polynomial time constant-factor approximation algorithms for maximum edge- disjoint paths and maximum node-disjoint paths (and more generally, maximum integer multiflow), as well as minimum congestion integer multiflow, for inputs where_ (_G,H_) _is pairwise-planar._

Another interesting corollary concerns the _integral flow-multicut gap_, which is the ratio of the minimum capacity of a multicut (a set \(F\subseteq E(G)\) whose removal destroys all paths connecting demands of _H_) to the maximum value of an _integral_ multiflow. Using their flow rounding algorithms, \[18\] \[15\] show the gap is constant for fully-planar (_G,H_), but the gap can be as large as \(\Theta(|E(H)|)\) even for planar supply graphs \[14\]. Combining our results with a theorem of \[33\], we obtain a constant gap for pairwise-planar instances.

**Corollary 1.5.** _For any maximization instance_ (_G,H,u_) _where_ (_G,H_) _is pairwise-planar, the minimum capacity of a multicut is at most O_(1) _times the maximum value of an integral multiflow._

<sup>2</sup>(_G,H_) is fully-compliant if _G_ is series-parallel and _G+h_ is series-parallel for every \(h\in E(H)\). <sup>3</sup>We defer the more technical definition of strongly uncrossed to Section 2.4. Importantly, the uncrossable layouts mentioned in this paper, including pairwise-planar, admit strongly uncrossed flows.

