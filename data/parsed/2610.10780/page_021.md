## Implicit biclique partition.

To obtain an _O(n_<sup>4/3</sup>)-time algorithm for enumerating \(S\cap I\), one would ideally compute a full biclique partition \(\Gamma=\{A_t\times B_t\}\) in _O(n_<sup>4/3</sup>) time such that \(\sum_t(|A_t|+|B_t|)=O(n^{4/3})\). We achieve a weaker form of this goal in which the sets _A<sub>t</sub>_ are represented only implicitly.

Specifically, our algorithm outputs the sets _B<sub>t</sub>_ explicitly, together with a collection A of explicitly represented subsets \(A'_s\subseteq A\). For each _B<sub>t</sub>_, the algorithm also outputs a subcollection \(\mathcal{A}_t\subseteq\mathcal{A}\) such that the sets in A_<sub>t</sub>_ form a partition of _A<sub>t</sub>_. In particular, \(A_t=\cup_{A_s^\prime\in\mathcal{A}_t}A'_s\). Furthermore, given _B<sub>t</sub>_, the sets of A_<sub>t</sub>_ can be accessed one at a time in _O_(1) time per set. Consequently, the points of _A<sub>t</sub>_ can be enumerated in _O_(|_A<sub>t</sub>_|) time. We refer to the pair \((\Gamma,\mathcal{A})\) as an _implicit full biclique partition_ of \(S\cap I\). Our main result is stated below.

**Theorem 4** (Implicit biclique partition)**.** _Given an interval I, one can compute an implicit full biclique partition of_ \(S\cap I\) _in O(n_<sup>4/3</sup>) _time._

_The output consists of a collection_ A _of subsets_ \(A'_s\subseteq A\) _and a collection_ \(\Gamma\) _of edge-disjoint bicliques_ \(A_t\times B_t\) _that together record all distances in_ \(S\cap I\)_. The sets_ \(B_t\subseteq B\) _are represented explicitly, whereas each set_ \(A_t\subseteq A\) _is represented implicitly as follows. For every biclique_ \(A_t\times B_t\)_, there is an associated subcollection_ \(\mathcal{A}_t\subseteq\mathcal{A}\) _containing O_(logloglog_n_) _subsets_ \(A'_s\)_, and these subsets form a partition of A<sub>t</sub>. Moreover, the elements of_ A_<sub>t</sub> can be accessed one at a time in O_(1) _time per element._

_Finally,_

\(\sum_{A_t\times B_t\in\Gamma}|B_t|=O(n^{4/3})\text{\textit{and}}\sum_{A_s^\prime\in\mathcal{A}}|A'_s|=O(n^{4/3}).\)

_Proof._ We run the algorithm of Lemma 1 from Section 2.1 with _m=n_. Whenever the algorithm reaches Recurrence (1), for each cell \(\sigma\in\Xi\) we add the biclique \(A_\sigma\times B_\sigma\) to \(\Gamma\), add \(A_\sigma\) to A as a subset \(A'_s\), and define \(\mathcal{A}_\sigma=\{A_\sigma\}\). Thus \(\mathcal{A}_\sigma\) contains exactly one subset.

We then continue with the dual algorithm and obtain Recurrence (2). We update \(\Gamma\) and A analogously for the dual subproblems. In this way we obtain Recurrence (3). Note that these additional bookkeeping operations do not affect the asymptotic running time, so the recurrence remains unchanged. Setting _r=n_<sup>1/3</sup>/log<sup>2</sup>_n_ yields Recurrence (5).

To solve _T(q,q_), unlike in Section 3.2, we do not use the parameter _g_ (or equivalently, we set _g_=1). Applying the algorithm corresponding to Recurrence (2) with _m=n=q_ and _r=q_<sup>1/3</sup>, we obtain

\(T(q,q)=O(q^{4/3})+O(q^{2/3})\cdot T(q^{1/3},q^{2/3}).\) (10)

As before, every biclique generated during this step is inserted into \(\Gamma\), and its associated subset is inserted into A. At this stage, each biclique \(A_t\times B_t\in\Gamma\) is associated with a single subset \(A'_s\in\mathcal{A}\).

We next consider a subproblem \(T(m',n')\) arising from Recurrence (10), where \(m'\le q^{1/3}\) and \(n'\le q^{2/3}\). Let \(A'\subseteq A\) and \(B'\subseteq B\) denote the corresponding point sets.

Let \(\mathcal{D}'\) be the set of annuli defined by the points of \(A'\) with respect to the interval _I_. We construct a hierarchical \((1/r')\)-cutting \(\{\Xi_0,\Xi_1,\dots,\Xi_k\}\) for \(\mathcal{D}'\), with \(r'=m'\). This takes \(O(m'r')\) time. Since \(r'=m'\), we can assume that every cell in the last cutting \(\Xi_k\) has an empty conflict list. Equivalently, no annulus of \(\mathcal{D}'\) has a boundary circle intersecting the interior of such a cell. Consequently, there are no uncertain pairs, which will allow us to obtain a full biclique partition.

Let \(\Xi\) denote the set of all cells in the hierarchical cutting. For each cell \(\sigma\in\Xi\), define the canonical subset \(A'_\sigma\) exactly as in Lemma 1: a point \(a\in A'\) belongs to \(A'_\sigma\) if the annulus _D<sub>a</sub>_ contains \(\sigma\) but does not contain the parent of \(\sigma\). We insert each nonempty subset \(A'_\sigma\) into A. All canonical subsets can be computed in \(O(m'r')\) time.

In addition, for every cell \(\sigma\in\Xi\) with \(A'_\sigma\neq\emptyset\), for a reason to be clear later, we store an _ancestor link_ from \(\sigma\) to its lowest ancestor \(\sigma'\) satisfying \(\sigma'\neq\sigma\) and \(A'_{\sigma^\prime}\neq\emptyset\). These links can be established in \(O(m'r')\) time by traversing the cutting tree.

