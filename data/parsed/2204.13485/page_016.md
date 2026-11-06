<tbc>is the set of men and \(W=B\cup\{w\}\cup\{s_1,\dots,s_{n-k}\}\) is the set of women in the new instance. The edges are \(F=E\cup\{s_ia_j|i\in[n-k],a_j\in A\}\cup\{u's_i|i\in[n-k]\}\cup\{uw,u'w\}\). The preferences are fixed only for the men:

• _u: w_,<tbc>

• \(u'\): \(s_1>\cdots>s_{n-k}>w\),<tbc>

• _a<sub>i</sub>_: \([N(a_i)]>s_1>\cdots>s_{n-k}\),

where \[_N(a<sub>i</sub>_)\] denotes the original neighbors of _a<sub>i</sub>_ as in _G_ ranked in their original order, see Figure 3. Finally, let \(\tau\) consists of the single forbidden edge _uw_. We claim that there is a Pareto-optimal matching of size at most _k_ in _G_ if and only if the preferences of the women can be set in a way such that there is a stable matching not containing _uv_ in \(G'\).

We claim that the original min-pom instance has a solution if and only if the 1-forbidden- sm-strat instance thus obtained does. First suppose there exists a Pareto-optimal matching _M_ in _G_ of size _k_. Then extend this matching by assigning _s_<sub>1</sub>_,...,s<sub>n-k</sub>_ to _n-k_ agents in _A_ who are unassigned in _M_ arbitrarily, and assign \(u'\) to _w_. Denote this matching by \(M'\). Set the preferences of each woman such that they prefer their partner the most if they have any, and arbitrarily otherwise. Clearly, \(M'\) does not contain _uw_. Suppose there is a blocking edge _xy_ where \(x\in U\) and \(y\in W\). Then _y_ can only be an unassigned woman, that is, \(y\in B\). This implies that \(x\in A\) and either _x_ is unmatched, _x_ is matched with a selector, or _x_ is matched with a _b<sub>i</sub>_ in \(M'\) that is worse than _y_. In the first two cases _M_ is not maximal, while the third option means that _M_ is not non-wasteful, a contradiction.

For the other direction, suppose there is a preference extension for the women and a matching \(M'\) not containing _uw_ that is stable with respect to those preferences. This is equivalent to the case where each woman’s preference list is just a tie and there is a weakly stable matching \(M'\) not containing _uw_. Since _uw_ does not block, we have \(u'w\in M'\). Therefore, each selector woman _s<sub>i</sub>_ is assigned, since otherwise they would block with \(u'\). Let _M_ be the restriction of \(M'\) to (_A,B;E_). The size of _M_ is at most _k_, because each selector is matched to _A_ and |_A_|=_n_. We claim that _M_ is non-wasteful and maximal. If it is not maximal, then there is an edge _ab_ that can be added, but _ab_ would block \(M'\). Similarly, if an agent _a_ would prefer an unassigned agent _b_ to _M(a_), then again _ab_ would block _M_.

We conclude that there is a maximal and non-wasteful matching _M_ for the original problem of size at most _k_. If _M_ is coalition-free, then we are done. Otherwise, if there is a coalition (_a_<sub>1</sub>_,b_<sub>1</sub>_,...,a<sub>r</sub>,b<sub>r</sub>_), then by changing _M_ to \((M\backslash\{a_ib_i|i\in[r]\})\cup\{a_ib_{i+1}|i\in[r]\}\), we get another matching that covers the same set of vertices, each agent weakly improves, and some agents strictly improve, so it is still maximal and non-wasteful. By iterating this step we get a matching _M_ covering the same set of vertices that is maximal, coalition-free, and non-wasteful, so it is a Pareto-optimal matching of size at most _k_ by theorem 3.

a1
a2
a3
3
2
1
2
1
3
1
b1
b2
b3

a1
a2
a3
u'
u
1
3
4
1
2
1
2
1
3
2
4
2
1
2
1
1
3
1
3
4
1
2
1
2
1
1
2
3
2
1
2
b1
b2
b3
S1
w

(a) An instance of min-pom. Thick edges form a Pareto-optimal matching _M_.

(b) The corresponding 1-forbidden-sm-strat instance. Thick edges form a stable matching \(M'\) not containing _uw_.

Figure 3: An illustration of Theorem 20. Higher values correspond to higher preferences.

