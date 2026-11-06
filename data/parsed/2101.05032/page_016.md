**Proof.** Let \(\mathcal{I}'\) be the set of non-trivial intervals in the input, ordered by non-decreasing left endpoint. We show that there is a set \(Q\subseteq\mathcal{I}'\) of size at most opt<sub>1</sub>+_i_-1 that is a prefix of \(\mathcal{I}'\) in the given ordering and has the property that, after querying _Q_, the instance is solved. Given the existence of such a set _Q_, it is clear that the theorem follows.

Fix an optimum query set OPT<sub>1</sub>, and let _v_<sup>∗</sup> be the _i_-th smallest value. After querying OPT<sub>1</sub>, assume that there are _m_ trivial intervals with value _v_<sup>∗</sup>. Note that \(m\ge 1\), since it is necessary to determine the value _v_<sup>∗</sup>. Those _m_ intervals are either queried in OPT<sub>1</sub> or already were trivial intervals in the input. We classify the intervals in I into the following categories, depending on where they fall _after_ querying OPT<sub>1</sub>:

1. The set _M_ (of size _m_) consisting of trivial intervals whose value is _v_<sup>∗</sup>;

2. The set _X_ consisting of non-trivial intervals that contain _v_<sup>∗</sup>;

3. The set _L_ of intervals that are to the left of _v_<sup>∗</sup>;

4. The set _R_ of intervals that are to the right of _v_<sup>∗</sup>.

We illustrate this classification in Figure 4. Note that intervals in _L_ and _R_ may intersect intervals in _X_, but cannot contain _v_<sup>∗</sup>. Let \(M^*=M\cap\mathrm{OPT}_1\), \(L^*=L\cap\mathrm{OPT}_1\) and \(R^*=R\cap\mathrm{OPT}_1\). Note that \(X\cap\mathrm{OPT}_1=\emptyset\), and that every interval in _M_\\_M_<sup>∗</sup> is trivial in the input.

We claim that the set \(Q=(L\cap\mathcal{I}')\cup X\cup M^*\cup R^*\) is a prefix of \(\mathcal{I}'\) in the given ordering (note that \((X\cup M^*\cup R^*)\backslash\mathcal{I}'=\emptyset\)), that querying _Q_ suffices to solve the instance, and that \(|Q|\le\mathrm{opt}_1+i-1\). Clearly, every interval in \(L\cup X\cup M^*\) comes before all the intervals in _R_\\_R_<sup>∗</sup> in the ordering considered. It also holds that every interval in _R_<sup>∗</sup> comes before all the intervals in _R_\\_R_<sup>∗</sup> in the ordering, since otherwise an interval in _R_<sup>∗</sup> not satisfying this condition could be removed from OPT<sub>1</sub>. Furthermore, querying all intervals in _Q_ is enough to solve the instance, because every interval in _R_\\_R_<sup>∗</sup> is to the right of _v_<sup>∗</sup>, and the optimum solution can decide the problem without querying them. Thus it suffices to bound the size of _Q_. Note then that \(|L|+|X|\le i-1\) since, after querying OPT<sub>1</sub>, the _i_-th smallest interval is in _M_, and any interval in \(L\cup X\) has a left endpoint to the left of _v_<sup>∗</sup>. Therefore,

\(|Q|\le|L|+|X|+|M^*|+|R^*|\le i-1+|M^*|+|R^*|\le\mathrm{opt}_1+i-1,\)

which concludes the proof.

The upper bound of \(\left\lceil\frac{\mathrm{opt}_1+i-1}{k}\right\rceil\) is best possible, because we can construct a lower bound of opt<sub>1</sub>+_i_-1 queries to solve the problem. It uses the same instance as described in [20] for the problem of identifying an _i_-th smallest element (but not necessarily finding its precise value). We include a description of the instance for the sake of completeness. Consider 2_i_ intervals, comprising _i_ copies of (0,5) and _i_ copies of {3}. For the first _i_-1 intervals (0,5) queried by the algorithm, the adversary returns a value of 1, so the algorithm also needs to

M
L
X
R

**Figure 4** An illustration of sets _M_, _X_, _L_ and _R_ in the proof of Theorem 5.1.

