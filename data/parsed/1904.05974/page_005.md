<tbc>from \[27\] is included in Fig. 2, where _a_<sub>1</sub> is the top choice of _b_<sub>1</sub>_,b_<sub>2</sub> while _a_<sub>2</sub> is their second choice and _a_<sub>0</sub> is their last choice; similarly, _b_<sub>1</sub> is the top choice of _a_<sub>0</sub>_,a_<sub>1</sub>_,a_<sub>2</sub> and _b_<sub>2</sub> is their second choice.

The blue dotted matching {(_a_<sub>1</sub>_,b_<sub>1</sub>),(_a_<sub>2</sub>_,b_<sub>2</sub>)} is the only popular matching here. The red dashed matching {(_a_<sub>1</sub>_,b_<sub>2</sub>),(_a_<sub>2</sub>_,b_<sub>1</sub>)} is not popular since the matching {(_a_<sub>0</sub>_,b_<sub>2</sub>),(_a_<sub>1</sub>_,b_<sub>1</sub>)} is more popular. However there is a convex combination of the red dashed and blue dotted matchings that is popular: this is the half-integral matching **_x_** where _x<sub>e</sub>_=1/2 for all _e_ in {(_a_<sub>1</sub>_,b_<sub>1</sub>),(_a_<sub>1</sub>_,b_<sub>2</sub>),(_a_<sub>2</sub>_,b_<sub>1</sub>),(_a_<sub>2</sub>_,b_<sub>2</sub>)}.

The polytope L_<sub>G</sub>_ is half-integral \[27\] and a compact extended formulation of L_<sub>G</sub>_ was given in \[31\]. Thus, we can find a min-cost popular fractional matching **_q_** in _G_ in polynomial time. We show that **_q_** can be expressed as the convex combination of the edge incidence vectors of two quasi-popular matchings in _G_, thus obtaining in polynomial time a quasi-popular matching of cost at most `opt`<sup>∗</sup>, where `opt`<sup>∗</sup> is the cost of **_q_**.

We remark that all our results - both positive and negative - hold for bipartite graphs. Our proof techniques borrow and extend tools from various approaches to matchings and popular matchings from the literature.

**Conference version.** This version of the paper goes beyond the conference version \[12\] in the following two points: (i) the algorithm for finding a quasi-popular matching of cost at most that of a min-cost popular fractional matching is new; (ii) the proofs from Section 6.1 and Section 7.3 are now self-contained (the conference version used constructions from \[10\] to show these lower bounds).

## 1.2 Background and Related Results

Algorithmic questions for popular matchings were first studied in the one-sided preferences model, where it is only vertices in _A_ that have preferences over their neighbors and cast votes (vertices in _B_ are objects). Popular matchings need not exist here and an efficient algorithm was given in \[2\] to determine if an instance admits a popular matching or not. McCutchen \[35\] introduced the measure of unpopularity factor and showed that computing a matching with _least unpopularity factor_ in the one-sided preferences model is NP-hard. Interestingly, in the one-sided preferences model, \(u(M)\ge 2\) for any unpopular matching _M_ \[35\].

When vertices on both sides have strict preferences, i.e., in a marriage instance, stable matchings always exist and hence popular matchings always exist. As mentioned earlier, efficient algorithms are known to compute max-size popular matchings \[25,29\]. These matchings compute dominant matchings (see Definition 2).<tbc>



a0
a1
b1
a2
b2

**Fig.1.** The dashed wedge is sandwiched between the tetrahedron and the cube. Similarly, `conv`(M<sup>∗</sup>), which has a compact extended formulation, is sandwiched between the popular matching polytope P and the quasi-popular matching polytope Q - neither of which has a compact extended formulation.

**Fig.2.** An instance where the popular fractional matching polytope is not integral.

