enough to query either _I_<sub>1</sub> or _I_<sub>2</sub>; hence, both {_I_<sub>1</sub>} and {_I_<sub>2</sub>} are feasible query sets. Since those realizations are initially identical to the algorithm, this example shows that no deterministic algorithm can be better than 2-query-competitive, and this example can be generalized by taking multiple copies of the given structure. For Minimum, however, an optimum solution can always be obtained by first querying _I_<sub>1</sub> (and then _I_<sub>2</sub> only if necessary): Since we need the precise value of the minimum element, in Figure 1b it is not enough to just query _I_<sub>2</sub>.

## 3 Sorting

In this section we discuss the Sorting problem. We allow open, half-open, closed, and trivial intervals in the input, i.e., _I<sub>i</sub>_ can be of the form \[_l<sub>i</sub>,u<sub>i</sub>_\] with \(l_i\le u_i\), or \((l_i,u_i]\), \[_l<sub>i</sub>,u<sub>i</sub>_\] or \((l_i,u_i)\) with \(l_i<u_i\).

First, we consider the case where S consists of a single set _S_, which we can assume to contain all _n_ of the given intervals. We wish to find a permutation \(\pi:[n]\rightarrow[n]\) such that \(v_i\le v_j\) if \(\pi(i)<\pi(j)\), by performing the minimum number of queries possible. This problem was addressed for _k_=1 in [21, 22, 27]; it admits 2-query-competitive deterministic algorithms and has a deterministic lower bound of 2.

For Sorting, if two intervals \(I_i=[l_i,u_i]\) and \(I_j=[l_j,u_j]\) are such that \(I_i\cap I_j=\{u_i\}=\{l_j\}\), then we can put them in a valid order without any further queries, because clearly \(v_i\le v_j\). Therefore, we say that two intervals _I<sub>i</sub>_ and _I<sub>j</sub>_ intersect (or are dependent) if either their intersection contains more than one point, or if _I<sub>i</sub>_ is trivial and \(v_i\in(l_j,u_j)\) (or _vice versa_). This is equivalent to saying that _I<sub>i</sub>_ and _I<sub>j</sub>_ are dependent if and only if \(u_i>l_j\) and \(u_j>l_i\). Two simple facts are important to notice, which are proven in [21]:

For any pair of intersecting intervals, at least one of them must be queried in order to decide their relative order; i.e., any intersecting pair is a witness set.

The dependency graph that represents this relation, with a vertex for each interval and an edge between intersecting intervals, is an interval graph [24].

We adapt the 2-query-competitive algorithm for Sorting by Halldórsson and de Lima [21] for _k_=1 to the case of arbitrary _k_. Their algorithm first queries all non-trivial intervals in a minimum vertex cover in the dependency graph. By the duality between vertex covers and independent sets, the unqueried intervals form an independent set, so no query is necessary to decide the order between them. However, the algorithm still must query intervals in the independent set that intersect a trivial interval or the value of a queried interval. To adapt the algorithm to the case of arbitrary _k_, we first compute a minimum vertex cover and fill as many rounds as necessary with the given queries. After the answers to the queries are returned, we use as many rounds as necessary to query the intervals of the remaining independent set that contain a trivial point.

\(\blacktriangleright\) **Theorem 3.1.** _The algorithm of Halldórsson and de Lima [21] yields a_ 2_-round-competitive algorithm for Sorting that runs in polynomial time._

I2
I2
I2
I2
I1
I1
I1
(a)
(b)
(c)
(d)

**Figure 1** Example of Sorting for two intervals and the possible realizations of the precise values. We have that opt<sub>1</sub>=1 in (a), (b) and (d), and opt<sub>1</sub>=2 in (c).

