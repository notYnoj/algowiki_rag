<tbc>to have _o_(log_n_)-competitiveness, they have substantially better bounds for special cases. For example, both Splay trees and GreedyFuture are dynamically optimal for _sequential access_ sequences [18, 19]. For _deque sequences_, Splay trees are \(O(\alpha^*(n))\)-competitive [32] whereas GreedyFuture is \(O(\alpha(n))\)-competitive [10]. Here, \(\alpha(n)\) denotes the inverse Ackermann function and \(\alpha^*(n)\) is the iterated function of \(\alpha(n)\). The sequential and deque sequences are special cases of the _pattern-avoiding access_ sequences [8]. For any fixed-size pattern, GreedyFuture is \(O(2^{(1+o(1))\alpha(n)})\)-competitive for pattern-avoiding access sequences [13]. It was shown recently that an optimal BST algorithm takes _O(n_) total cost for any fixed pattern [3] and there is an optimal algorithm for sorting pattern-avoiding sequences [**?**]. The bounds for specific classes of patterns can be improved if preprocessing is allowed [8, 21] (i.e., the initial tree can be set before executing the online search sequences). Recently, a slight modification of GreedyFuture was shown to be \(O(\sqrt{logn})\)-competitive [11]. An important application of GreedyFuture (or any competitive online BSTs) includes adaptive sorting using treesort [4, 13] and heapsort [26].

The lower bounds in the literature other than Wilber’s bounds include the _maximum independent rectangle_ and _SignedGreedy_ bounds [15], which subsume Wilber’s Alternation and Funnel bounds. A similar lower bound was presented by Derryberry et al. [17]. Recently, _Guillotine_ Bound [6] was introduced, which is a generalization of Wilber’s Alternation bound. Unfortunately, it is unclear how to design an algorithm that utilizes these bounds. Recently, Sadeh and Kaplan [36] proved that the competitive ratio of GreedyFuture cannot be less than 2 for the multiplicative factor, or _o(m_loglog_n_) for the additive factor.

## 1.3 Paper Organization

We first describe terminologies and notations in Section 2. We prove the direct-sum results for Wilber’s bounds (Theorem 1) in Section 3. In Section 4, we prove the hardness amplification of Wilber’s bounds while maintaining their separation (Theorem 2) and we also prove Theorem 3. We prove the superadditivity of the Funnel Bound in Section 5.

## 2 Preliminaries

We follow notations and terminologies from [27].

\(\blacktriangleright\) **Definition 6** (access sequence)**.** _An access sequence is a finite sequence_ \(X=(X_1,\dots,X_m)\in S^m\) _of values from a finite set of keys_ \(S\subseteq\mathbb{R}\)_. Usually, we let S_:=[_n]._

To make our definitions and proofs easier, we will work directly in the geometric representation of access sequences as (finite) sets of points in the plane R<sup>2</sup>.

\(\blacktriangleright\) **Definition 7** (geometric view)**.** _Any access sequence_ \(X=(X_1,\dots,X_m)\in S^m\) _can be represented as the set of points_ \(G_X:=\{(X_t,t)|t\in[m]\}\)_, where the x-axis represents the key and the y-axis represents time (see Figure 1)._

By construction, in _G<sub>X</sub>_, no two points share the same _y_-coordinate. We will say such a set has "distinct _y_-coordinates". In addition, we note that it is fine to restrict our attention to sequences _X_ without repeated values.<sup>5</sup> The geometric view _G<sub>X</sub>_ of such sequences also

<sup>5</sup> Indeed, Appendix E in [8] gives a simple operation that transforms any sequence _X_ into a sequence split(_X_) without repeats such that \(\mathsf{OPT}(\mathsf{split}(X))=\Theta(\mathsf{OPT}(X))\). Thus if we found a tight lower bound _L(X_) for sequences without repeats, a tight lower bound for general _X_ could be obtained as _L_(split(_X_)).

