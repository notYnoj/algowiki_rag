**Corollary 10.** _Given an unsplittable transshipment instance, deciding whether there exists a feasible unsplittable transshipment in which all paths leaving the same source and all paths entering the same sink carry identical flow values is NP-complete._

## Appendix B Non-integrality result

Figure 3 presents an unsplittable transshipment instance with integral arc capacities and integral supplies and demands, following the construction in [BKS05, Figure 4]. The instance admits a feasible non-integral unsplittable transshipment, as shown in the figure. However, no feasible integral unsplittable transshipment exists. To see this, notice that the total demand is 20, and each path has capacity at most 9, so at least 4 paths are required. At vertex _v_ (resp. _w_), two paths must route flow upward and two downward.

Consider the possibilities for integral flows along these paths: If any path carries flow strictly less than 1, then some other path must carry more than 9, violating capacity constraints. If all paths carry flow strictly greater than _\>_2, arcs of capacity 2 cannot be used, making the transshipment infeasible. If a path carries exactly 1 (resp. 2), another path must carry 9 (resp. 8), forcing a third to carry 3=12-9 (resp 4=12-8) along the arc of capacity 12. The remaining path would then carry 7 (resp. 6), again exceeding capacity at the arc of capacity 15 (resp. 5).

Thus, at least one path must carry flow strictly between 1 and 2, implying that no integral unsplittable transshipment can satisfy all balance values and capacities.

## Appendix C Tightness of upper bound in highly connected instances

We show that _d_<sub>max</sub> remains tight even when each sink is connected to an arbitrarily large number (_k_+1) of sources, by constructing the following family of instances parameterized by any integer \(q\ge 3\) and _q\>(k_+1); see Figure 4 for an illustration.

Our instance consists of _q_ sinks _t_<sup>1</sup>_,...,t<sup>q</sup>_, each with demand _d<sub>j</sub>_=1. For each \(j\in\{1,\dots,q\}\), there is a dedicated source _s<sup>j</sup>_ connected to _t<sup>j</sup>_ by _q-k_ parallel arcs. In addition, there are _k_ sources _s_<sup>_q_+1</sup>_,...,s_<sup>_q+k_</sup>, each connected to every sink _t<sup>j</sup>_ by a path of length 2, which consists of an arc _a<sub>i</sub>_ shared across all sinks and one arc entering _t<sup>j</sup>_. The balance values of the sources and the sinks can be found in Figure 4. We now define a feasible fractional _b_-transshipment as follows:<tbc>

+5
S1
t1
-8
7
5
10
8
4
w
9
15
10
12
2
+15
S2
t2
-12

Figure 3: A non-integral unsplittable transshipment, formed by the _s_<sup>1</sup>-_t_<sup>1</sup>-path with flow value <sup>3</sup>/2 highlighted in _yellow_, the _s_<sup>1</sup>-_t_<sup>2</sup>-path with flow value <sup>7</sup>/2 highlighted in _magenta_, the _s_<sup>2</sup>-_t_<sup>1</sup>-path with flow value <sup>13</sup>/2 highlighted in _blue_, and the _s_<sup>2</sup>-_t_<sup>2</sup>-path with flow value <sup>17</sup>/2 highlighted in _green_.

