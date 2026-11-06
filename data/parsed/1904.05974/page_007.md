## 2.1 A Polyhedral Overview of Popular Matchings

Given any matching _M_ in _G_, for any edge \((a,b)\notin M\), define vote_<sub>a</sub>(b,M_) as follows: (here _M(a_) is _a_’s partner in the matching _M_ and _M(a_)=null if _a_ is unmatched)

\(\mathsf{vote}_a(b,M)=\left\{\begin{array}{ c c }
+ & \text{if}a\text{prefers}b\text{to}M(a); \\
- & \text{if}a\text{prefers}M(a)\text{to}b.
\end{array}\right.\)

We similarly define vote_<sub>b</sub>(a,M_). Label every edge \((a,b)\notin M\) by (vote_<sub>a</sub>(b,M),_vote_<sub>b</sub>(a,M_)). Thus, every edge outside _M_ has a label in \(\{(\pm,\pm)\}\), and it is labeled (+,+) if and only if it blocks _M_.

Let \(\tilde{G}\) be the graph _G_ augmented with self-loops. That is, we assume each vertex is its own last choice neighbor. So we can henceforth regard any matching _M_ in _G_ as a perfect matching \(\tilde{M}\) in \(\tilde{G}\) by adding self-loops for all vertices left unmatched in _M_. The following edge weight function wt_<sub>M</sub>_ in \(\tilde{G}\) will be useful to us. For any edge (_a,b_) in _G_, define:

\(\mathsf{wt}_M(a,b)=\left\{\begin{array}{ c c }
2 & \text{if}(a,b)\text{is labeled}(+,+); \\
-2 & \text{if}(a,b)\text{is labeled}(-,-); \\
0 & \text{if}(a,b)\in M\text{or labeled otherwise}.
\end{array}\right.\)

For any \(u\in A\cup B\), let wt_<sub>M</sub>(u,u_)=0 if _u_ is left unmatched in _M_, else wt_<sub>M</sub>(u,u_)=-1. Let _N_ be any matching in _G_. Then \(\mathsf{wt}_M(\tilde{N})\) is the difference in the number of votes for _N_ and for _M_ in their head-to-head election, i.e., \(\mathsf{wt}_M(\tilde{N})=\phi(N,M)-\phi(M,N)\).

Hence _M_ is popular in _G_ if and only if every perfect matching in the graph \(\tilde{G}\) (with edge weights given by wt_<sub>M</sub>_) has weight at most 0. Equivalently, _M_ is popular if and only if \(\tilde{M}\) is an optimal solution to the max-weight perfect matching problem in \(\tilde{G}\) (since \(\mathsf{wt}_M(\tilde{M})=0\)). In other words, every popular matching is a _self-optimal_ matching.

_Remark._ Suppose we replace "perfect matching" with "matching" in the above statement (so \(\tilde{M}\) and \(\tilde{G}\) can be replaced by _M_ and _G_, respectively). Observe that this characterizes _stable_ matchings, i.e., a matching _M_ is a max-weight matching in _G_ with edge weights given by wt_<sub>M</sub>_ if and only if _M_ is stable.<sup>5</sup> This is because wt_<sub>M</sub>(M_)=0, so we need to have \(\mathsf{wt}_M(e)\le 0\) for every edge _e_ if _M_ is a max-weight matching under wt_<sub>M</sub>_. Equivalently, blocking edges are forbidden for _M_.

Going back to the max-weight perfect matching problem in \(\tilde{G}\) with edge weights given by wt_<sub>M</sub>_, consider the LP in variables \(\alpha_u\) for \(u\in A\cup B\) that is dual to the max-weight perfect matching LP. The characterization of popular matchings given below follows from LP-duality and total unimodularity of the system.

**Theorem 5 (\[30,31\]).** _A matching M in_ \(G=(A\cup B,E)\) _is popular if and only if there exists a vector_ \(\alpha\in\{0,\pm 1\}^n\) _such that_ \(\sum_{u\in A\cup B}\alpha_u=0\),

\(\alpha_a+\alpha_b\ge\mathsf{wt}_M(a,b)\forall(a,b)\in E\text{\textit{and}}\alpha_u\ge\mathsf{wt}_M(u,u)\forall u\in A\cup B.\)

For any popular matching _M_, a vector \(\alpha\in\{0,\pm 1\}^n\) as given in Theorem 5 will be called _M_’s _witness_. A popular matching may have several witnesses. Any stable matching _M_ has **0** as a witness, since \(\mathsf{wt}_M(e)\le 0\) for all edges _e_ in \(\tilde{G}\).

**Popular Fractional Matchings.** Rather than fixing a matching _M_, we could generalize the above characterization to any point **_x_** in the matching polytope. This would extend the notion of popularity to fractional matchings. Roughly speaking, a fractional matching **_x_** is popular if and only if **_x_** is a _self-optimal_ fractional matching, i.e., **_x_** is a max-weight perfect fractional matching in \(\tilde{G}\) under the edge weight function wt_<sub>x</sub>_, which is the extension of wt_<sub>M</sub>_, described below.

<sup>5</sup> This view of stable matchings was shared with us by Tamás Fleiner.

