**Lemma 3.7.** _If there exists a stable matching M, then there is a truth assignment for_ I _satisfying exactly one literal in each clause._

_Proof._ Consider the assignment \(f:\{x_i\}\rightarrow\{\mathsf{true},\mathsf{false}\}\), with _f(x<sub>i</sub>_):=true if and only if all \(x_i^k\) are matched to a 2-set of the form {_c<sub>j</sub>,d<sub>j</sub>_}.

Assume that _f_ is not a solution to I. We distinguish two cases.

**Case 1:** There is a clause _C<sub>j</sub>_ which is not satisfied by _f_.

By Lemma 3.4, for each \(j\in[m]\), there exists some \(\ell\in[3]\) such that \(\{c_j,d_j,y_j^\ell\}\in M\). Let \(y_j^\ell=x_i^k\). By Lemma 3.6, for every \(k'\in[3]\), agent \(x_i^{k^\prime}\) is matched to 2-set {_c<sub>p</sub>,d<sub>p</sub>_} for some \(p\in[m]\). Thus, the clause _C<sub>j</sub>_ is satisfied by _f_, a contradiction.

**Case 2:** There is a clause _C<sub>j</sub>_ which is satisfied by at least two variables _x<sub>i</sub>_ and \(x_{i^\prime}\).

Matching _M_ can only contain one 3-set containing _c<sub>j</sub>_ and _d<sub>j</sub>_, and so without loss of generality \(x_i^k\) is not matched to {_c<sub>j</sub>,d<sub>j</sub>_} for any \(k\in[3]\). By Lemma 3.4, literal \(x_i^{k^\prime}\) contained in _C<sub>j</sub>_ does not match to any 2-set {_c<sub>q</sub>,d<sub>q</sub>_} for \(q\in[m]\), and thus, we have _f(x<sub>i</sub>_)=false, a contradiction.

Altogether, we conclude that _f_ is a solution to I.

Finally, we are ready to prove the main theorem of this section.

**Theorem 3.8.** 3-DSR-ML _is_ NP_-complete._

_Proof._ Observe that 3-DSR-ML is in NP (the stability of a matching can be checked in _O(n_<sup>3</sup>) time by enumerating all 3-sets, where _n_ is the number of agents).

The reduction described in Section 3.2.1 can be performed in linear time. Thus, the NP- completeness of 3-DSR-ML follows directly from Lemma 3.2 and Lemma 3.7.

We have seen that the strong restriction that the preferences of each agent are complete and derived from a common master list of _d_-sets presumably does not lead to an efficient algorithm, even for _d_=2. Thus, in order to get tractable cases, other restrictions of the preferences are needed. One possibility would be to additionally require that every agent has consistent preferences. In this case, the master list implies that the preferences of every agent is indeed derived from a master poset which is a strict order, and we will see in the beginning of Section 4 that this implies that there exists a unique stable matching which can be found efficiently.

## 4 Master poset of agents

In this section, we consider the case when there does not exist a master list of (_d_-1)-sets of agents, but a master poset \(\succ_\mathsf{ML}\) of single agents; in other words, we study the complexity of the problem MDSR-Poset. Each agent can derive its preferences from this master list, meaning that if for two (_d_-1)-sets \(t\neq t'\), one can find a bijection \(\sigma\) from the elements of _t_ to the elements of \(t'\) such that \(a\unknown_\mathsf{ML}\sigma(a)\) for all \(a\in t\), then any agent (not occurring in _t_ or \(t'\)) shall prefer _t_ to \(t'\). We show that this problem is easily polynomial-time solvable if the master poset is a strict order (Section 4.1). Afterwards, following the approach of distance- from-triviality parameterization \[21, 37\], we generalize this result by showing fixed-parameter tractability for the parameter \(\kappa\), the "maximum number of agents incomparable to a single agent" (Section 4.2.1). On the contrary, for the stronger parameter width of the poset, we show W\[1\]-hardness (Section 4.2.2), leaving open whether it can be solved in polynomial time for constant width (in parameterized complexity known as the question for containment in XP). Afterwards, in Section 4.3, again employing a distance-from-triviality parameterization we show W\[1\]-hardness of MDSR-Poset parameterized by the number of agents one needs to delete in order to have the preferences derived from a strict order. Finally, we show that the variation of MDSR-Poset where agents may declare an arbitrary part of (_d_-1)-sets as unacceptable<tbc>

