Routing a fraction 1/<sup>(_n_+1)</sup> of the original feasible flow through every copy yields a single source flow from _S_<sup>∗</sup> to the super-sinks in \(D'\), to which we apply the Modified DGG Algorithm.

Since \(c'_{a^\prime}+d_{max}\le c_a/_{(n+1)}+\left(1-1/n\right)c_{min}\le c_a\), each copy of _D_ is individually feasible with respect to the original capacities. However, we cannot directly interpret each copy as a routing round, because the Modified DGG Algorithm may split the demand of a sink across multiple copies of _D_ which is incompatible with the notion of routing in rounds. We therefore distinguish two categories of sinks.

A sink is _critically split_ if its demand is divided between forward path(s) contained in a single copy of _D_ and a _singular digraph_ that may span multiple copies; otherwise, it is _non-critically split_ and its entire demand is routed within one copy, which can be interpreted directly as a round where such a sink is routed.

**Observation 8.** _In any fixed copy of D, each arc_ \(a'\) _can be used in the singular digraph of at most one critically split sink. Once used,_ \(a'\) _is deleted and cannot be included in further singular digraphs._

This observation allows us to group the critically split sinks in a controlled manner. Each such sink _t_ is associated with a _label_ \(\ell\in\{1,\dots,n+1\}\) identifying the copy of _D_ containing its forward path(s), and a _demand-share vector_ \(\theta^t=(\theta_1^t,\dots,\theta_{n+1}^t)\), where \(\theta_\alpha^t:=^{d_t^\alpha}/_{d_t}\) denotes the fraction of demand routed through copy \(\alpha\) of _D_.

The demand-share vectors \(\theta^t\) lie in the _n_-dimensional simplex. To group sinks of the same label with similar demand distributions, we discretize this simplex using a uniform grid of granularity \(\varepsilon\le 1/(n^2-1)(n+1)\). For each coordinate, the range \[0,1\) is sliced into intervals of size \(\varepsilon\). For _M_:=(_n_<sup>2</sup>-1)(_n_+1), these intervals are of the form \([k\varepsilon,(k+1)\varepsilon)\) for \(k\in\{0,\dots,M-1\}\).

A _group_ is defined by a label and a choice of one interval per coordinate,<tbc>

\(\left(\ell,\left([a_1,u_1),\dots,[a_{n+1},u_{n+1})\right)^T,u_\alpha=a_\alpha+\varepsilon\text{for}\alpha=1,\dots,n+1.\)

<tbc>Such a group can contain a demand-share vector if and only if<tbc>

\(\sum_{\alpha=1}^{n+1}a_\alpha\le 1\text{and}1\le\sum_{\alpha=1}^{n+1}u_\alpha=\sum_{\alpha=1}^{n+1}(a_\alpha+\varepsilon)=\sum_{\alpha=1}^{n+1}a_\alpha+(n+1)\cdot\varepsilon,\)

<tbc>thus, \(1-(n+1)\varepsilon\le\sum_{\alpha=1}^{n+1}a_\alpha\le 1\), or equivalently, by multiplying with _M_ and using \(a_\alpha=k_\alpha\varepsilon\),<tbc>

\(M-(n+1)\le\sum_{\alpha=1}^{n+1}k_\alpha\le M.\)

<tbc>Hence, for a fixed label, admissible groups correspond to non-negative integer (_n_+1) tuples \((k_\alpha)\) whose total sum lies in {_M_-(_n_+1)_,...,M_}. By the stars-and-bars argument, the total number _N_tot of such groups for a fixed label is

\(N_\text{tot}=\sum_{j=0}^{n+1}\genfrac(){pt}{2}{M-j+n}{n}=\sum_{j=0}^n\genfrac(){pt}{2}{(n^2-1)\cdot(n+1)-j+n}{n}<\infty.\)

We now show that superimposing all paths of critically split sinks within a fixed group yields a feasible routing round. Fix an arc \(a\in A\). In the worst case, each copy \(\alpha\) of _a_ carries the maximum group demand \(u_\alpha\) allowed by its interval. By Observation 8, each copy contributes to at most one<tbc>

