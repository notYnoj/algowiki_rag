of single-commodity flows \((x^{st}:(s,t)\in E(H))\). For \(e\in E(G)\), we let \(x(e)=\sum_{P\in\mathcal{P}:e\in P}x(P)\) (the amount of flow on _e_), and for \((s,t)\in E(H)\) we let \(|x^{st}|=\sum_{P\in\mathcal{P}_{st}}x(P)\) (the amount of demand (_s,t_) that is routed).

A _maximization instance_ has the form (_G,H,u_), where \(u:E(G)\rightarrow\mathbb{R}_{\ge 0}\) are _capacities_. A multiflow _x_ is _feasible_ for the instance if for every \(e\in E(G)\), \(x(e)\le u(e)\). The objective is to maximize the value of a feasible multiflow, where the value of a multiflow _x_ is \(|x|=\sum_{P\in\mathcal{P}}x(P)=\sum_{(s,t)\in E(H)}|x^{st}|\). If \(u=\vec{1}\) and we restrict to integral _x_, this problem is the _maximum edge-disjoint paths_ problem (MEDP). A _weighted_ maximization instance also comes equipped with per-unit profits \(w:E(H)\rightarrow\mathbb{R}_{\ge 0}\), in which case the value of _x_ is instead defined \(|x|_w=\sum_{(s,t)\in E(H)}w(s,t)|x^{st}|\).

A _congestion instance_ has the form (_G,H,u,d_), where \(u:E(G)\rightarrow\mathbb{R}_{\ge 0}\) are capacities and \(d:E(H)\rightarrow\mathbb{R}_{\ge 0}\) are _demand values_. A multiflow _x_ is _feasible_ for the instance if for every \(e\in E(G)\) we have \(x(e)\le u(e)\) and for every \((s,t)\in E(H)\) we have |_x<sup>st</sup>_|=_d(s,t_). As a decision problem, the goal is to determine whether (_G,H,u,d_) has a feasible multiflow. As an optimization problem, the objective is to find the minimum \(\alpha\ge 1\) such that \((G,H,\alpha u,d)\) has a feasible multiflow.

In either setting, we say an instance is _planar_ if _G_ is planar. We emphasize that _G+H_ is not necessarily planar. We always assume a fixed embedding of planar graph _G_.

## 2.2 Uncrossed Paths and Multiflows

First, we define what it means for paths to cross. Edge-disjoint paths can cross at a common node, but in general we need to consider common subpaths (see Figure 2).

**Definition 2.1** (Crossing)**.** Let _Z_ be a maximal shared subpath of paths _P_ and _Q_ that does not include any of their endpoints. Say the ends of _Z_ are _z_ and \(z'\). The edges of \((P\cup Q)\backslash Z\) incident with _z_ or \(z'\) have a clockwise ordering about _Z_ in the plane. The paths _cross_ at _Z_ if the edges of _P_ and _Q_ alternate clockwise about _Z_. That is, if \(P=P_1,e,Z,e',P_2\) and \(Q=Q_1,g,Z,g',P_2\), the edges occur \(e,g,e',g'\) or \(e,g',e',g\) clockwise about _Z_. Two paths are _uncrossed_ if they do not cross at any such subpath<sup>6</sup>.

The _support paths_ of a multiflow _x_ are the paths with _x(P)\>_0. The following is the natural extension of "uncrossed" to the multiflow setting (though we discuss a stronger condition in Section 2.4).

**Definition 2.2** (Uncrossed Multiflow)**.** A multiflow is _uncrossed_ if its support paths are pairwise uncrossed.

We are interested in when a feasible multiflow _x_ can be converted into an uncrossed one that routes the same demands. Our discussion here focuses on the congestion setting, but still applies to the maximization setting (since we can define target demand values _d_ equal to whatever quantities _x_ routes). As shown in<tbc>

<sup>6</sup>We emphasize that paths can only cross at maximal common subpaths that do _not_ contain their endpoints. Both paths must have edges before and after the common subpath in order to cross. For example, if _P_ contains an endpoint of _Q_ and _Z_ is the maximal common subpath containing that endpoint, then _P_ and _Q_ do not cross at _Z_.

g
z
e
z
e
g
e
g
e'
e'
g'
e'
g'
g'
z'
z'

Figure 2: (Left) Two edge-disjoint paths that cross at a common node. (Center) Two paths that cross at a common subpath. (Right) Two paths that share a common subpath, but are uncrossed. Uncoloured edges are shared between the two paths.

