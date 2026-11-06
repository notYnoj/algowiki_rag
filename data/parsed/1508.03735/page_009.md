**Lemma 3.** _The sampled matching in_ \(G'\) _has expected size at least_ \(\frac{\mathrm{OPT}'}{3\rho}\) .

We will defer the proof to the appendix. We now have all the pieces to prove Theorem 2.

_Proof of Theorem 2._ Suppose that there exists a coordination protocol \((\sigma,\pi)\) for many-to-one matchings with a guaranteed approximation ratio of \(\rho\). By the result of Lemma 3, we know that this coordination protocol for one-to-one matchings has an approximation ratio most \(O(\rho)\). By the lower bound in Theorem 1, we know that the length of \(\sigma(G)\) is at least \(\Omega(k/\rho^4)\).

## 4 Coordination Protocol for Linearly Separable Convex Programs

In this section, we give a coordination protocol for problems which can be expressed as linearly separable convex programs, with coordination complexity scaling only with the number of constraints that bind between agents (so called _coupling constraints_, defined below). In the next section, we show how to specialize this protocol to the special case of many-to-one matchings, which gives coordination complexity nearly matching our lower bound.

**Definition 3.** _A linearly separable convex optimization problem consists of n players and for each player i,_

• _a compact and bounded convex feasible set_ \(\mathcal{F}^{(i)}\subseteq\{x^{(i)}\in\mathbb{R}^l|\|x^{(i)}\|\le 1\}\),<tbc>

• _a concave objective and_ 1_-Lipschitz function_ \(v^{(i)}:\mathcal{F}^{(i)}\rightarrow\mathbb{R}\) _such that v_<sup>(_i_)</sup>(**0**)=0,<tbc>

• _and k convex constraint function_ \(c_j^{(i)}:\mathcal{F}^{(i)}\rightarrow[0,1]\) _(indexed by j_=1_,...,k)._

_The convex optimization problem is:_

\(\mathrm{max}_x\sum_{i=1}^nv^{(i)}(x^{(i)})\)<br>
\(\text{\textit{subject to}}\sum_{i=1}^nc_j^{(i)}(x^{(i)})\le b_j\text{\textit{for}}j=1,\dots,k\text{\textit{(Coupling constraints)}}\)<br>
\(x^{(i)}\in\mathcal{F}^{(i)}\text{\textit{for}}i=1,\dots,n\text{\textit{(Personal constraints)}}\)

_where each player i controls the block of decision variable x_<sup>(_i_)</sup>.

Viewed as a coordination problem, the data held by each agent _i_ is \(D^{(i)}=\{\mathcal{F}^{(i)}v^{(i)},c_1^{(i)},\dots,c_k^{(i)}\}\), his action range is A_<sub>i</sub>_=F<sup>(_i_)</sup>, and the social objective function is _S_ the objective of the convex program.

We will denote the product of the personal constraints by \(\mathcal{F}=\mathcal{F}^{(1)}\times\dots\times\mathcal{F}^{(n)}\), the objective function by _v(x_), and the optimal value by OPT. In this notation we can write the problem as

\(\mathrm{max}_{x\in\mathcal{F}\text{and}\sum_{i=1}^nc_j^{(i)}(x^{(i)})\le b_j\text{for all}j}v(x).\)

Note that here the problem is constrained both by the personal constraints F and by the coupling constraints. We will assume the problem above is feasible and our goal is coordinate the players to play an aggregate solution \(x=(x^{(i)})_{i\in[n]}\) that is approximately feasible and optimal. Our solution consists of two steps:

