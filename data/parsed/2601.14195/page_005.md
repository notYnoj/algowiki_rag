We adopt the following classical stability notion.

**Definition 2.4** (Stability)**.** _Let_ \(I=(A,\succ)\) _be an_ sri _(or_ smi_) instance and let M be a matching of I. A_ blocking pair _admitted by M is a pair of distinct agents_ \(a_i,a_j\in A\) _such that_ \(a_i\succ_jM(a_j)\) _and_ \(a_j\succ_iM(a_i)\)_. We denote the_ set of blocking pairs _by bp(M), and the subset thereof that involves an agent a<sub>i</sub> by bp<sub>a<sub>i</sub></sub>(M). Furthermore, the set of_ blocking agents _ba(M_) _consists of all agents involved in blocking pairs._

_If_ \(bp(M)=\varnothing\)_, then M is referred to as_ stable_, and as_ unstable _otherwise. We refer to I as_ solvable _if it admits at least one stable matching and as_ unsolvable _otherwise._

In the absence of stable matchings in sr, we previously argued that one might want to find an "almost-stable" matching that minimises the number of blocking pairs \[1\]. A definition of this problem follows below.

MinBP-AlmostStable-sri<br>
**Input:** sri instance _I_.<br>
**Output:** A matching _M_ of _I_ such that \(|bp(M)|=min_{M^\prime\in\mathcal{M}}|bp(M')|\).

As noted before, even when considering only smi instances, the set of stable matchings might not intersect with M<sup>+</sup>. Then, we may want to find a maximum-cardinality matching that is "as stable as possible", i.e., minimises the number of blocking pairs \[10\]. This problem is defined as follows.

MinBP-AlmostStable-Max-smi<br>
**Input:** smi instance _I_.<br>
**Output:** A maximum-cardinality matching _M_ of _I_ such that \(|bp(M)|=min_{M^\prime\in\mathcal{M}^+}|bp(M')|\).

For our complexity reductions, we will take advantage of the fact that the problem (2,2)- e3-sat, which we formally define below, is known to be NP-complete \[6\].

(2,2)-e3-sat<br>
**Input:** Boolean formula _B_ in conjunctive normal form, where every variable occurs exactly twice unnegated and twice negated, and every clause contains exactly three literals.<br>
**Question:** Does there exist a satisfying truth assignment _f_ of _B_?

To illustrate this problem for 3 variables _V<sub>i</sub>_, \(B=(V_1\vee V_2\vee V_3)\wedge(\bar{V}_1\vee\bar{V}_2\vee\bar{V}_3)\wedge(V_1\vee\bar{V}_2\vee V_3)\wedge(\bar{V}_1\vee V_2\vee\bar{V}_3)\) is a yes-instance to (2,2)-e3-sat because it admits satisfying truth assignments \(f:V\rightarrow\{T,F\}\). For example, the assignment _f(V_<sub>1</sub>)=_T,f(V_<sub>2</sub>)=_F_ and _f(V_<sub>3</sub>)=_F_ satisfies _B_.

## 2.2 Related Work

MinBP-AlmostStable-sri was shown to be NP-hard regardless of whether preference lists are of length at most 3 or complete \[1, 9\], NP-hard to approximate within \(n^{1/2-\varepsilon}\) (for any \(\varepsilon>0\), where _n_ is the number of agents) \[1\], and W\[1\]-hard with respect to \(min_{M\in\mathcal{M}}|bp(M)|\) even when preference lists are of length at most 5 \[12\].

Biró, Manlove and Mittal \[10\] conducted a thorough study of the computational complexity of the trade-off between matching size and stability in smi, where stability is measured in terms of the number of blocking pairs or blocking agents. They showed that MinBP-AlmostStable- Max-smi (and similarly for blocking agents) is NP-hard to approximate within \(n^{1-\varepsilon}\) (for any \(\varepsilon>0\)) \[10\]. Hamada et al. \[32\] strengthened this result to the case where all preference lists are of length at most 3. On the positive side, the problem is known to be solvable in polynomial time when one side of the bipartition has preference lists of length at most 2 \[10\]. Gupta et al. \[29\] showed that MinBP-AlmostStable-Max-smi remains W\[1\]-hard for the combined<tbc>

