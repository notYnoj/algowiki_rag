<tbc>extends from the first quartile to the third quartile of the data, with a line at the median; the whiskers extend from the box to the farthest data point lying within 1.5x the inter-quartile range from the box).

By definition, the H_<sub>greedy</sub>_ (in green) heuristic dominates H_<sub>all paths</sub>_ (in red). While the H_<sub>greedy</sub>_ heuristic tends to provide better solutions on smaller instances, its performance seems to deteriorate on larger values of |_K_| where the H_<sub>threshold</sub>_ heuristic appears to be more efficient (as shown in Figure 5b).

## 6.2 DCMCF relaxations

The choice of the lower and upper bounds _u<sub>a</sub>_, _l<sub>a</sub>_, \(u_p^k\), and \(l_p^k\) significantly affects the strength of the resulting relaxations. As described in Section 3.6, bounds can be computed through a closed-formula or a convex optimization problem. In practice, the bounds \(l_ap^k\) are set to 0, while _l<sub>a</sub>_,_u<sub>a</sub>_ and \(u_p^k\) are computed by solving the corresponding convex-optimization problems. Notice that even when we are considering the bounds related to the BIG-M (resp. S or T) formulation, we use the strongest relaxation (i.e., DCMF<sub>env</sub>) to compute them.

We compare the convex relaxations of the DCMCF problem associated with the formulations BIG-M, S, T and CONVEX described above. As S, T and CONVEX include the constraints of the BIG-M relaxation, they necessarily provide tighter upper bounds for the problem. Similarly, all<tbc>

