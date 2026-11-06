## 3.1 Uncrossing Procedure

In this section we show why feasible pairwise-planar instances have uncrossed flows. We focus on congestion instances (_G,H,u,d_) (where a feasible flow must satisfy all demands), since given a feasible flow _x_ for a maximization instance (_G,H,u_), one can define demand values _d(s,t_)=|_x<sup>st</sup>_| and apply the congestion result. We present an inductive proof that a feasible uncrossed flow exists. It is straightforward to convert this into an algorithm, with one catch for polynomial time implementation that we explain at the end.

For fully-planar instances, \[15, 12\] use an algorithm by Matsumoto et al. \[22\] that builds an uncrossed flow from scratch starting from the zero flow. Our procedure has more in common with \[19\] (which concerns finding cycles in higher-genus surfaces that cross at most once) in that we begin with a (potentially highly crossing) feasible flow _x_ and "uncross" it bit-by-bit. The following is an important lemma.

**Lemma 3.3.** _Let_ (_G,H,u,d_) _be a planar congestion instance that is feasible. There exists a feasible flow f_<sup>∗</sup> _such that every pair of support paths crosses at most once, and any pair of support paths that share a terminal do not cross._

We say a flow satisfying this property is _almost-uncrossed_. Proving this lemma formally is somewhat tedious, but such arguments have appeared in the literature before - the essence of the argument is in Lemma 1 of \[24\] and a similar method is used in \[19\]. Loosely, the argument goes as follows. Begin with a feasible flow _x_. One can show that if a pair of support paths cross twice (or cross once but share a terminal), then one can re-route flow on their edges to decrease the "amount of crossing" between the two paths ("uncrossing" the two paths) and argue that this re-routing does not increase crossing with other support paths. Thus the total amount of crossing decreases, and we iterate until _x_ is uncrossed. For completeness we give a careful proof of this lemma (and precisely define "amount of crossing") in the appendix (see Section A.2).

Theorem 3.3 immediately implies single-source layouts are uncrossable. With a small trick it also proves fully-planar layouts are uncrossable: augment the instance by adding leaves. That is, for each \(h=(s,t)\in E(H)\), add nodes _s<sub>h</sub>,t<sub>h</sub>_ into the interior of the face where _h_ is embedded, add supply edges (_s<sub>h</sub>,s),(t<sub>h</sub>,t_), move the endpoints of the demand _h_ to (_s<sub>h</sub>,t<sub>h</sub>_), and extend the flow paths appropriately to route this instance. At first, adding leaves may actually increase the amount of crossing. However, since the demands do not cross, it can be shown that every pair of support paths that cross must cross at least twice. Then Theorem 3.3 allows one to conclude there exists a feasible uncrossed flow in the augmented instance. The leaves can then be contracted away without introducing any new crossing.

Extending this trick to pairwise-planar instances is not immediate. After adding leaves, it may not be the<tbc>

G6
G7
G8
G9
G1
G2
G3
G4
G5

Figure 6: A pairwise-planar layout. Each _G<sub>i</sub>_ is a connected planar graph. The demand edges cannot be simultaneously embedded so that _G+H_ is planar (_G+H_ contains a _K_<sub>3,3</sub>-minor and a _K_<sub>5</sub>-minor). However, taking advantage of multi-faced demands, any _single pair_ of demands can be embedded without crossing. One could make the layout more complicated by putting demands inside the _G<sub>i</sub>_’s following similar patterns.

