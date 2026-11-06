or equivalently,

\(\mathbb{E}[d(\rho)]\ge log_2(g(\mathbb{E}[deg_\overline{H}(\rho)]+1)/n).\)

The result follows since _A_ is an arbitrary deterministic algorithm for \(\Pi\), \(\mathbb{E}[d(\rho)]\) equals the query complexity of _A_ with respect to the uniform distribution D, \(\mathbb{E}[deg_\overline{H}(\rho)]\ge\mathbb{E}[deg_\overline{G(\Pi)}(\rho)]=s(\Pi)\), and _g_ is nondecreasing.

Proposition 40 allows us to prove a lower bound on the \(\varepsilon\)-error distributional query complexity of \(\Pi\) with respect to the uniform distribution. In order to do so, we view a deterministic algorithm with distributional error \(\varepsilon\) for \(\Pi\) as an exact deterministic algorithm for a modified problem \(\Pi'\), apply Proposition 40, and lower bound the sensitivity of \(\Pi'\) in terms of the sensitivity of \(\Pi\).

**Proposition 41.** _Let_ \(\Pi\) _be a problem in the comparison-query model with n items,_ D _the uniform distribution on the inputs_ \(\rho\), \(\varepsilon\in[0,1]\)_, and_ \(g:[1,\infty)\rightarrow\mathbb{R}\) _a nondecreasing log-convex function with g(x_)=_x! for_ \(x\in[n]\).

\(\mathrm{Dist}\mathrm{Q}_\varepsilon(\Pi,\mathcal{D})\ge log_2\left(\frac{g(s(\Pi)+1-2(n-1)\varepsilon)}{n}\right)\) (19)

_Proof._ Consider any algorithm _A_ with error \(\varepsilon\) for \(\Pi\), or in other words, \(\mathbb{P}[A(\rho)\neq\Pi(\rho)]\le\varepsilon\). Let \(\Pi_A\) be the problem of determining the output of _A_. We prove that

\(s(\Pi_A)\ge s(\Pi)-2(n-1)\varepsilon,\)

which implies the desired result by Proposition 40, since _A_ is a deterministic algorithm for \(\Pi_A\) and _g_ is nondecreasing.

Let _G_ denote the full permutahedron graph for _n_ items. We use the fact that \(s(\Pi)=(n-1)\cdot\mathbb{P}_{e\in G}[e\in G(\Pi)]\), and similarly, \(s(\Pi_A)=(n-1)\cdot\mathbb{P}_{e\in G}[e\in G(\Pi_A)]\), where all the underlying distributions are uniform. Suppose the endpoints of _e_ are \(\rho_1\) and \(\rho_2\). Note that if \(e\in G\) is picked uniformly at random, then the marginal distributions of both \(\rho_1\) and \(\rho_2\) are also uniform. If \(A(\rho_1)=\Pi(\rho_1)\), \(A(\rho_2)=\Pi(\rho_2)\), and \(e\in G(\Pi_A)\), then \(e\in G(\Pi)\), as well. By a union bound, the probability that \(A(\rho_1)\neq\Pi(\rho_1)\) or \(A(\rho_2)\neq\Pi(\rho_2)\) is at most \(2\varepsilon\).

\(\mathbb{P}_{e\in G}[e\in G(\Pi_A)]\ge\mathbb{P}_{e\in G}[e\in G(\Pi)]-\mathbb{P}_{e\in G}[A(\rho_1)\neq\Pi(\rho_1)\text{or}A(\rho_2)\neq\Pi(\rho_2)]\)<br>
\(\ge\mathbb{P}_{e\in G}[e\in G(\Pi)]-2\varepsilon.\)

Multiplying both sides by _n_-1 gives \(s(\Pi_A)\ge s(\Pi)-2(n-1)\varepsilon\).

Since \(s(\Pi)\le n-1\), Proposition 41 only yields nontrivial lower bounds for small \(\varepsilon\). In order to establish lower bounds for the standard \(\varepsilon=1/3\), we first reduce the error using standard techniques. Doing so such that the argument of _g_ on the right-hand side of (19) remains \(\Omega(s(\Pi))\), and picking \(g(x)=\Gamma(x+1)\), we conclude:

**Lemma 42 (Bounded-Error Sensitivity Lemma).** _For any problem_ \(\Pi\) _in the comparison-query model with n items,_

\(\mathrm{RQ}_{1/3}(\Pi)=\Omega\left(\frac{s\mathrm{log}s}{\mathrm{log}(2n/s)}\right),\)

_where_ \(s\doteq s(\Pi)\).

