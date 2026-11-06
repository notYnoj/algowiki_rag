# Unsplittable Transshipments<sup>∗</sup>

**Abstract**

We introduce the _Unsplittable Transshipment Problem_ in directed graphs with multiple sources and sinks. An unsplittable transshipment routes given supplies and demands using at most one path for each source-sink pair. Although they are a natural generalization of single source unsplittable flows, unsplittable transshipments raise interesting new challenges and require novel algorithmic techniques. As our main contribution, we give a nontrivial generalization of a seminal result of Dinitz, Garg, and Goemans (1999) by showing how to efficiently turn a given transshipment _x_ into an unsplittable transshipment _y_ with _y<sub>a</sub>\<x<sub>a</sub>+d_max for all arcs _a_, where _d_max is the maximum demand (or supply) value. Further results include bounds on the number of rounds required to satisfy all demands, where each round consists of an unsplittable transshipment that routes a subset of the demands while respecting arc capacity constraints.

### 1 Introduction

Network flows constitute one of the most fundamental classes of problems in combinatorial optimization and mathematical programming. We refer to the historical book by Ford and Fulkerson [FF62], the classical textbook by Ahuja, Magnanti, and Orlin [AMO93], as well as the more recent textbook by Williamson [Wil19] for comprehensive treatments of the subject.

Starting with the pioneering work of Kleinberg [Kle96a; Kle96b], the past three decades have witnessed substantial progress in the study of unsplittable flows, in which the demand of each commodity must be routed along a single path from its source to its sink subject to given arc capacity constraints. Unsplittable flows are crucial in applications such as logistics, traffic, and telecommunication networks, where splitting a commodity across multiple paths may degrade quality of service, increase operational complexity, or be infeasible altogether, as exemplified by optical networks requiring specialized equipment for path splitting and freight logistics where dividing loads across routes is often impractical.

The most general multicommodity version of the problem, in which each commodity has its own source and sink, generalizes the arc-disjoint paths problem and is notoriously difficult to approximate. If the maximum demand is smaller than the minimum arc capacity, the randomized rounding technique of Raghavan and Thompson [RT87] achieves a logarithmic approximation factor for minimizing congestion, while for densely embedded unit-capacity graphs, Kleinberg [Kle96a] obtains a constant-factor approximation with high probability. We refer to the survey

<sup>∗</sup>The first and the last author are supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany ́s Excellence Strategy – The Berlin Mathematics Research Center MATH+ (EXC-2046/1, EXC- 2046/2, project ID: 390685689). <sup>†</sup>Institute of Mathematics, TU Berlin, Germany, `debgupta@math.tu-berlin.de` <sup>‡</sup>Faculty of Mathematics and Computer Science, University of Bremen, Germany, `morell@uni-bremen.de` \(^\mathsection\)Institute of Mathematics, TU Berlin, Germany, `martin.skutella@tu-berlin.de`

Srinwanti Debgupta<sup>†</sup>

Sarah Morell<sup>‡</sup>

Martin Skutella<sup>§</sup>

February 6, 2026

