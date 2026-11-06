For a fixed _M_, wt_<sub>x</sub>(M_) is a linear function of **_x_**, hence the set \(\mathcal{X}_G\subset\mathbb{R}^m\) of points that satisfy (25) and (26) is a polytope. We now prove that X_<sub>G</sub>_ is the convex hull of dominant matchings in _G_.

The starting point is the fact that there is an efficient separation oracle for the constraints that define X_<sub>G</sub>_. We show next that, given a point **_x_** that satisfies the constraints in (25), we can efficiently determine if **_x_** satisfies all the constraints in (26) by solving the max-weight perfect matching problem in the graph \(\tilde{G}\) (this is _G_ augmented with self-loops) with the edge weight function _c<sub>x</sub>_. Recall that _c<sub>x</sub>_ is exactly the same as wt_<sub>x</sub>_ defined in (1) for edges (_a,b_) where neither _a_ nor _b_ is in _U_ and _c<sub>x</sub>(a,b_)=1 if _a_ or _b_ is in _U_. We extend the function _c<sub>x</sub>_ to self-loops as _c<sub>x</sub>(u,u_)=0 for \(u\in U\) and _c<sub>x</sub>(u,u_)=-1 for \(u\notin U\). Note that _c<sub>x</sub>_ is an affine function of **_x_**.

**Claim 7** _Let **x** satisfy all constraints in (25). Then_ \(\mathbf{x}\in\mathcal{X}_G\) _if and only if_ \(c_x(M)\le 0\) _for every perfect matching M in_ \(\tilde{G}\).

If we had assigned _c<sub>x</sub>(a,b_)=0 for edges (_a,b_) where _a_ or _b_ is in _U_, then for \(e\in E\), _c<sub>x</sub>(e_)=wt_<sub>x</sub>(e_), which is the sum of votes of the endpoints of _e_ for each other versus their respective assignments in **_x_**. Then it would have been _c<sub>x</sub>(M_)=wt_<sub>x</sub>(M_) for any perfect matching _M_ in \(\tilde{G}\). With the above assignment of weights, i.e., with _c<sub>x</sub>(a,b_)=1 for edges (_a,b_) where _a_ or _b_ is in _U_, we now have _c<sub>x</sub>(M_)=wt_<sub>x</sub>(M_)+_k<sub>M</sub>_ for any perfect matching _M_ in \(\tilde{G}\). Thus Claim 7 follows.

Consider the max-weight perfect matching LP in \(\tilde{G}=(A\cup B,\tilde{E})\) with respect to _c<sub>x</sub>_: this is (LP5) below in variables _y<sub>e</sub>_ for \(e\in\tilde{E}\). The linear program (LP6) in variables \(\alpha_u\) for \(u\in A\cup B\) is its dual.

\(\text{maximize}\sum_{e\in\tilde{E}}c_x(e)\cdot y_e\) (LP5)

\(\text{subject to}\)<br>
\(\sum_{e\in\tilde{\delta}(u)}y_e=1\forall u\in A\cup B\)<br>
\(y_e\ge 0\forall e\in\tilde{E}.\)

\(\text{minimize}\sum_{u\in A\cup B}\alpha_u\) (LP6)

\(\text{subject to}\)<br>
\(\alpha_a+\alpha_b\ge c_x(a,b)\forall(a,b)\in E\)<br>
\(\alpha_u\ge c_x(u,u)\forall u\in A\cup B.\)

So \(\mathbf{x}\in\mathbb{R}^m\) that satisfies the constraints in (25) also satisfies the constraints in (26) if and only if the optimal solution of (LP5) is 0, equivalently, if and only if the optimal solution of (LP6) is 0; thus \(\mathbf{x}\in\mathcal{X}_G\) if and only if there exists a dual feasible \(\unknown\in\mathbb{R}^n\) such that \(\sum_{u\in A\cup B}\alpha_u=0\). Hence X_<sub>G</sub>_ has the following compact extended formulation:

\(\sum_{u\in A\cup B}\alpha_u=0\) (27) \(\alpha_a+\alpha_b\ge c_x(a,b)\forall(a,b)\in E\) (28) \(\alpha_u\ge c_x(u,u)\forall u\in A\cup B\) (29) \(x_e=0\forall e\in E\backslash E_D\) (30) \(x_e\ge 0\forall e\in E_D.\) (31) \(x_e\ge 0\forall e\in E_D.\) (32)

