by Kolliopoulos \[Kol07\] for an overview of results on general unsplitable flows. The difficulty of the general problem has motivated extensive study of the special single source case, in which all commodities share a common source. In this setting, the underlying problem of computing a fractional (i.e., not necessarily unsplitable) flow that satisfies all demands reduces to a classical single commodity flow problem and can be solved via a maximum flow computation.

## Unsplittable transshipments.

We study unsplitable transshipments as an extension of single source unsplitable flows to networks with multiple sources and sinks and prescribed supplies and demands, where for each source-sink pair flow is routed along at most one path. More precisely, we are given a directed graph _D_=(_V,A_) together with a vertex balance function \(b:V\rightarrow\PazoBB{R}\) satisfying \(\sum_{v\in V}b(v)=0\). A vertex _v_ is called a _source_ if _b(v)\>_0, and the set of all sources is denoted by _S_<sup>+</sup>. Similarly, a vertex _v_ is called a _sink_ if _b(v)\<_0, and the set of all sinks is denoted by _S_<sup>-</sup>. A flow \(x\in\PazoBB{R}_{\ge 0}^A\) is a _b-transshipment_ if

\(\sum_{a\in\delta^\mathrm{out}(v)}x_a-\sum_{a\in\delta^\mathrm{in}(v)}x_a=b(v)\text{for all}v\in V,\)

where \(\delta^\mathrm{in}(v)\) and \(\delta^\mathrm{out}(v)\) denote the sets of incoming and outgoing arcs of vertex _v_, respectively. Given arc capacities \(c\in\PazoBB{R}_{\ge 0}^A\), a _b_-transshipment _x_ is _feasible_ if \(x_a\le c_a\) for all \(a\in A\). As for the special single source case, finding a feasible _b_-transshipment reduces to a maximum flow computation. An _unsplittable b-transshipment_ is a _b_-transshipment together with a path decomposition consisting of source-sink paths only, and with at most one path for each source-sink pair. In order to emphasize the fact that a particular transshipment _x_ is not necessarily unsplitable, we sometimes refer to _x_ as a _fractional_ transshipment.

## Single source unsplitable flows.

The special case of unsplitable transshipments with a single source, that is, _S_<sup>+</sup>={_s_}, coincides with the well-studied Single Source Unsplittable Flows (SSUF) problem. The rich literature on SSUF mostly refers to the demand values at sinks as _d<sub>t</sub>_:=|_b(t_)| for \(t\in S^-\). Arguably the most influential work on SSUF is due to Dinitz, Garg, and Goemans \[DGG99\]. Their central result shows that any fractional flow _x_ satisfying all demands can be efficiently transformed into a single source unsplitable flow _y_ such that

\(y_a<x_a+d_\mathrm{max}\text{for all arcs}a\in A,\)

where \(d_\mathrm{max}:=\mathrm{max}_{t\in S^-}d_t\) denotes the maximum demand of any sink. In particular, in a capacitated single source network in which all arc capacities are at least _d_<sub>max</sub> (so that any commodity can be routed along any arc) this result immediately yields a 2-approximation algorithm for finding an unsplitable flow that minimizes congestion. The result has also inspired a substantial body of subsequent research, ranging from contributions by Kolliopoulos and Stein \[KS01\] and Skutella \[Sku02\] in the early 2000s, to recent work by Morell and Skutella \[MS22\], Traub, Vargas Koch, and Zenklusen \[TVZ24\], Majthoub Almoghrabi, Skutella, and Warode \[MSW25\], as well as Swamy, Traub, Vargas Koch, and Zenklusen \[Swa+26\].

Beyond the congestion-minimization problem discussed above, Kleinberg \[Kle96b\] introduces further variants of unsplitable flow problems. The _minimum number of rounds_ problem asks for a partition of the set of sinks into a minimum number of subsets (rounds), together with a feasible unsplitable flow for each subset. Building upon their main result, Dinitz, Garg, and Goemans \[DGG99\] obtain a 5-approximation algorithm for this problem, improving upon earlier approximation results by Kleinberg \[Kle96b\] and Kolliopoulos and Stein \[KS01\]. In particular, if a<tbc>

