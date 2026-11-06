Note that in Lemma 23, the constant hidden in the O notation of the resulting data structure is greater than the constant hidden in the prerequisite data structure.

It remains to give a linear-time data structure for sufficiently small universe sizes.

**Lemma 24** (Efficient interval intersections for tiny universes)**.** _Let b be the size of the machine word and_ \(\ell\le\sqrt{b}\)_. There exists a data structure for any instance of Interval-Intersect with the universe size at most_ \(\ell\) _that takes a finite set A of labels and processes q queries in total time_ \(\mathcal{O}(\ell+|A|+q)\)_. The data structure requires a global table, which can be computed given only_ \(\ell\) _in time_ \(\mathcal{O}(2^{\ell^2})\).

_Proof._ Fix \(\ell\) as the universe size; if the universe size of an instance is smaller than \(\ell\), we can artificially increase it to \(\ell\). Define the _state_ of an instance of Interval-Intersect to be the set of _active_ integer intervals of \([\ell]\): the intervals assigned to the active labels of the instance. Note that there are exactly \(2^{\genfrac(){pt}{2}{\ell+1}{2}}\) different states since there are \(\genfrac(){pt}{2}{\ell+1}{2}\) integer subintervals of \([\ell]\). We represent states in memory as bitmasks of length \(\genfrac(){pt}{2}{\ell+1}{2}\); this is permitted in our computation model as \(b\ge\genfrac(){pt}{2}{\ell+1}{2}\).

In the preprocessing stage, we initialize a global two-dimensional table _T_ as follows. For a state _S_ and an interval \(J\subseteq[\ell]\), we define _T_\[_S_\]\[_J_\]=(_S_in_,S_out), where _S_in is the set of intervals of _S_ intersecting _J_, and _S_out is the remaining intervals of _S_. Observe that when an instance of Interval-Intersect is in state _S_, then performing a query _J_ on it transitions it to state _S_out and returns all labels with the corresponding intervals in _S_in. Let also, for a state _S_ and an interval \(I\in S\), the value _F_\[_S_\]\[_I_\] be an integer such that, for each _S_, the mapping from intervals \(I\in S\) to the values _F_\[_S_\]\[_I_\] is a bijection between _S_ and \(\lfloor|S|\rfloor\). We also explicitly compute an \(\mathcal{O}(\ell^2)\)-sized array _M_ mapping integer subintervals of \([\ell]\) to their bit index within the state. The arrays can be constructed in time \(2^{\genfrac(){pt}{2}{\ell+1}{2}}\ell^{\mathcal{O}(1)}\in\mathcal{O}(2^{\ell^2})\).

We now give an implementation of the data structure. On initialization, we compute the initial state _S_init from \(\ell\) and _A_ using _M_. Then create buckets _B_<sub>1</sub>_,...,B_<sub>|_S_init|</sub> of labels from _A_, and for each label \(a\in A\), insert _a_--corresponding to an interval \(I_a\in S_\text{init}\)--into bucket _B_<sub>_F_\[_S_init\]\[_I<sub>a</sub>_\]</sub>. This can be done in total \(\mathcal{O}(\ell+|A|)\) time. Let also _S_ track the current state of the data structure; initially _S=S_init. Then, for a given query _J_, let (_S_in_,S_out)=_T_\[_S_\]\[_J_\]. We update the state of the data structure to _S_out and return all labels of the intervals in _S_in (i.e., all labels in the buckets _B_<sub>_F_\[_S_init\]\[_I_\]</sub> for \(I\in S_\text{in}\)). This can clearly be done in time O(1+_t_), where _t_ denotes the total number of returned labels. Therefore, all queries are processed in total time \(\mathcal{O}(\ell+|A|+q)\).

Given Lemmas 23 and 24, the proof of Lemma 21 is direct.

_Proof of Lemma 21._ Fix the universe size _N\<_2_<sup>b</sup>_, and let \(\ell=max(1,\lceil loglogN\rceil)\). By Lemma 24, after preprocessing in time \(\mathcal{O}(2^{\ell^2})=o(N)\), we can construct a data structure for Interval- Intersect processing instances with a universe of size at most \(\ell\), the set of labels _A_, and _q_ queries in time \(\mathcal{O}(\ell+|A|+q)\). Applying Lemma 23 the first time with \(N_{max}=2^\ell\), we get a data structure for universes of size \(n\le 2^\ell\) with total time O(_n_+|_A_|+_q_). Applying Lemma 23 once again with _N_max=_N_, we end with the required data structure.

## 5 Wrap-up of the algorithmic corollaries

The proof of Theorem 6 now simply wraps the results of previous sections together.

**Theorem 6.** _For every graph class_ C _of linear neighborhood complexity, All-Pairs Shortest Path can be solved in_ O<sub>C</sub>(_n_<sup>2</sup>) _time on n-vertex graphs of_ C.

