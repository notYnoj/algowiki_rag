separated by it. Many approximation algorithms for the sparsest cut problem are based on solutions to the maximum concurrent flow problem (see, e.g., [31]).

## Flows with delay considerations

When the delay on each link is constant and identical across all links, incorporating delay constraints is equivalent to imposing a bound on the number of links in the selected path. This can be handled efficiently via dynamic programming, by solving shortest-path problems under hop constraints to generate feasible paths [1, 29].<br>
When the delay on a link is given by 1/(_c<sub>a</sub>-y<sub>a</sub>_), and the goal is to to minimize the average end-to-end delay of the demands over a network, the resulting objective function is then \(\sum_ay_a/(c_a-y_a)\), which can be minimized within a convex optimization framework. The survey [27] provides a comprehensive overview of solution approaches for convex-cost multi- commodity flow problems, in which the objective is to minimize the total cost--defined as the sum of convex arc costs--while satisfying all demand requirements.<br>
The average end-to-end delay minimization problem has also been considered with the additional constraint that each flow should be unsplittable. In [34], a near-optimal solution is computed through a Lagrangian relaxation when delay constraints follow Kleinrock functions, while [12] proposes a branch-and-bound approach to solve this problem when average delays are approximated by piecewise-linear functions. A branch-and-price method is described in [5] to solve the problem for convex delay functions.

The work of [3], that formalizes delay constraints and provides some heuristic solutions, is one of the earliest and most closely related contributions to the present study. The cost version of the DCMCF problem was further investigated in [4], where its weak NP-hardness was established through a reduction from the 2-Partition problem. In addition, convex relaxations were proposed to effectively handle the delay constraints.<br>
A relaxation based on a disjunctive formulation of the delay constraints is<tbc>

