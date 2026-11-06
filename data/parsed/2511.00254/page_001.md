# Uncrossed Multiflows and Applications to Disjoint Paths

Chandra Chekuri<sup>1</sup>, Guyslain Naves<sup>2</sup>, Joseph Poremba<sup>3</sup>, and F. Bruce Shepherd<sup>3</sup>

<sup>1</sup>Department of Computer Science, University of Illinois, Urbana-Champaign

<sup>2</sup>Laboratoire d’Informatique et des Systèmes, Aix-Marseille Université

<sup>3</sup>Department of Computer Science, University of British Columbia

**Abstract**

A multiflow in a planar graph is _uncrossed_ if the curves identified by its support paths do not cross in the plane. Recently, uncrossed flows have played a role in approximation algorithms for maximum disjoint paths in "fully-planar" instances, where the combined supply-plus-demand graph is planar. They are also used in algorithms to find low-congestion unsplitable flows for both fully-planar and single- source instances. For these two instance classes, any fractional multiflow can be converted into one that is uncrossed, which these algorithms then exploit to obtain their results.

We investigate the utility of uncrossed flow more generally and ask three key questions. First, are there other interesting planar multiflow instances that admit uncrossed flows (beyond fully-planar and single-source)? We answer affirmatively, demonstrating a new family of "pairwise-planar" instances whose fractional flows can be uncrossed. This family subsumes fully-planar but includes substantially more, such as (2-connected) fully-compliant series-parallel instances and some instances that have large clique demand graphs. Second, can we always round a fractional uncrossed flow to a "good" integral flow? We again answer positively. For maximization problems, we show any fractional uncrossed flow can be rounded to an integral flow with a constant fraction of its value. For congestion problems (where we must fully route all given demands), we give a rounding procedure that yields an integral multiflow with edge congestion 2. Consequently, we obtain constant-factor approximation algorithms for maximum disjoint paths and minimum congestion integer multiflow for pairwise-planar instances, and show such instances have a constant integral flow-multicut gap. Finally we ask, given an arbitrary planar instance, can we determine if there exists a congestion-1 uncrossed fractional flow (congestion setting) or find the maximum value uncrossed fractional flow (maximization setting)? For congestion, we show this problem is NP-hard, but finding uncrossed edge-disjoint paths is polytime solvable if the demands span a bounded number of faces. For maximization, we present a strong (almost-polynomial) inapproximability result.

### 1 Introduction

In _multicommodity flow_, we are given an edge-capacitated _supply graph_ (_G,u_) and a set of source-sink pairs called _demands_ or _commodities_. The demands are represented by a _demand graph H_ on the same node set as _G_. Unless otherwise specified, graphs are _undirected_. We seek to route flow for the demands simultaneously, while respecting the capacities of the supply graph. There are two flavours of the multiflow problem. In the _maximization_ setting, the objective is to find a flow _x_ that respects the capacities and maximizes the total sum of demands being routed. A feasible flow for (_G,H,u_) needs to respect the capacities, but has freedom in the quantities of each demand that it routes. In the _congestion_ setting, we are given target amounts _d(s,t_) for each \((s,t)\in E(H)\). To be feasible for (_G,H,u,d_), a flow must (in addition to respecting capacities) fully route this amount for each demand. The objective is to determine whether _d_ can be satisfied in the capacities _u_, or to find the minimum scaling factor \(\alpha\ge 1\) such that _d_ can be satisfied in capacities \(\alpha u\).

Both fractional and integer versions of these problems are fundamental in combinatorial optimization (cf. [31]). Due to applications, the literature often emphasizes problems where the supply graph is planar [21]. The integer problems are hard even for planar supply graphs with 3 demand edges [36]. There exist, however, good approximation algorithms in so-called _fully-planar_ instances where the joint supply-demand

