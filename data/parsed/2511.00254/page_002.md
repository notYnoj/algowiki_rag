<tbc>graph _G+H_ is planar<sup>1</sup>. Often approximation algorithms follow a "relax-and-round" approach: relax the integer problem to its fractional version, find a fractional solution with "nice properties", and then round the nice fractional solution to an integral solution.

A recurring "nice property" for planar multiflow is that the support paths (i.e. paths routing non-zero flow) do not cross in the plane. A multiflow satisfying this property is _uncrossed_ (see Figure 1). It is known how to construct uncrossed multiflows for single-source (_H_ is a star) and fully-planar instances, the latter using an algorithm of Matsumoto et al. \[22\]. This was recently leveraged to give constant-factor approximation algorithms for _maximum edge-disjoint paths_ (MEDP) \[15\] and _maximum node-disjoint paths_ (MNDP) \[28, 27\] for fully-planar instances. Very recently uncrossed flows were used to round fractional flows to _unsplittable_ flows, routing the same demand quantities with small additive error, in both single-source \[34\] and fully-planar contexts \[12\]. In an unsplittable flow, each demand is routed on a single path.

In the above results, the uncrossed property of the fractional solution plays a key role, but the arguments are still specialized to the structure of (_G,H_). For example, for the fully-planar context, the uncrossed flow can be shown to be _laminar_: if one considers the family of cycles obtained by joining demand edges of _H_ to their support paths in _G_, the result is a nested family of cycles in the plane. However, this same property does not hold for all instances that admit uncrossed flows. For instance, if _G_ is a cycle and _H_ consists of mutually crossing demands, then no paths within _G_ cross, but the path-plus-demand cycles are not nested. Our aim is to expand on a theory of uncrossed flows - when can we find them, and do they always admit good rounding algorithms, even outside the laminar/single-source cases? We have three motivating questions.

**Question 1.** Do there exist other (interesting) families of (_G,H_) satisfying the following property: for all capacities _u_ and demand values _d_, if (_G,H,u,d_) has a feasible (fractional) multiflow _x_, then (_G,H,u,d_) has a feasible multiflow _y_ that is uncrossed?

We say (_G,H_) is an _uncrossable layout_ if it satisfies the conditions of Question 1. For instance, if (_G,H_) is fully-planar or _H_ is single-source, then (_G,H_) is an uncrossable layout.

**Question 2.** Suppose we are given a feasible fractional multiflow _x_ that is uncrossed (not assuming that the multiflow _x_ is laminar). Can we round _x_ to a "good" integer multiflow _y_? Specifically:

i. (Congestion Setting) Given feasible uncrossed fractional multiflow _x_ for (_G,H,u,d_), can we compute an integer multiflow _y_ feasible for \((G,H,\alpha u,d)\), for some constant \(\alpha\)?<tbc>

ii. (Maximization Setting) Given feasible uncrossed fractional multiflow _x_ for (_G,H,u_), can we compute an integer multiflow _y_ feasible for (_G,H,u_) whose value is \(1/\beta\) times that of _x_, for some constant \(\beta\)?

The answer to Question 1 and both parts of Question 2 is: yes! First, we define a new class of (_G,H_) and prove it gives uncrossable layouts.

<sup>1</sup>In this paper, if we say a multiflow instance is _planar_ we only mean that the supply graph _G_ is planar. If we mean _G+H_ is planar, we will say fully-planar.





Figure 1: A fully-planar multiflow instance with two different multiflows routing its demands. Dashed edges represent demands, and coloured paths are support paths of the flow. The support paths on the left cross, while the multiflow on the right is uncrossed.

