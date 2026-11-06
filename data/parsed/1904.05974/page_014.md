<tbc>\(\alpha_a+\alpha_b-1=\beta_a+\beta_b\). Thus the edge covering constraints hold for all \((a,b)\in E\). Hence \(\unknown\) is a valid witness of _M_<sup>∗</sup>’s popularity in _G_<sup>∗</sup>.

Hence, _M_<sup>∗</sup> is popular. Moreover, by construction, we have \(\beta_a=0\) if and only if _a_ is unmatched in _M_<sup>∗</sup> and \(\beta_a=-1\) for every \(a\in U_A\backslash U^*\). Hence, _M_<sup>∗</sup> has a witness \(\unknown\) that satisfies Definition 3, so _M_<sup>∗</sup> is extra-dominant. \(\sqcap\sqcup\)

_Proof._ (of Lemma 3). Let _N_ be any matching in _G_. Let \(T'=T\cap E\). Matchings _N_ and \(T'\) can be viewed as matchings in _G_<sup>∗</sup> as well since \(E^*\supseteq E\). Since _T_ is popular in _G_<sup>∗</sup>, \(\phi_{G^*}(T,N)\ge\phi_{G^*}(N,T)\), where \(\phi_{G^*}\) is the function \(\phi\) in the graph _G_<sup>∗</sup>.

Let _W_ be the set of unstable vertices in _G_ that get matched along _new_ edges (i.e., those in _E_<sup>∗</sup>\\_E_) in _T_ but are left unmatched in _N_.

- We have \(\phi_{G^*}(T',N)=\phi_{G^*}(T,N)-|W|\). The vertices in _W_ used to vote for _T_ versus _N_, however they are now indifferent between \(T'\) and _N_ because both \(T'\) and _N_ leave them unmatched.<tbc>

**-** We also have \(\phi_{G^*}(N,T')=\phi_{G^*}(N,T)\). Indeed, if a vertex did not prefer _N_ to _T_, then it is either unmatched in _N_ or it was matched in _T_ by an edge in _E_ (since edges from _E_<sup>∗</sup>\\_E_ are at the end of every vertex’s preference list), hence it is matched via the same edge in \(T'\).

Since both \(T'\) and _N_ are matchings in _G_, we have \(\phi_{G^*}(T',N)=\phi(T',N)\) and \(\phi_{G^*}(N,T')=\phi(N,T')\). Consider the subgraph of _G_<sup>∗</sup> whose edges are given by \(T\oplus N\). Its connected components are alternating paths / cycles. We are left to show that, for each such connected component \(\rho\), we have \(\phi(N\cap\rho,T'\cap\rho)\le 2\cdot\phi(T'\cap\rho,N\cap\rho)\). This concludes the proof, since summing both sides over all connected components \(\rho\) of \(T\oplus N\), we get \(\phi(N,T')\le 2\cdot\phi(T',N)\), as \((T\backslash T')\cap N=\emptyset\).

First, let \(\rho\) be an alternating cycle. We know from the popularity of _T_ in _G_<sup>∗</sup> that, if we restrict to vertices of \(\rho\), we have \(\phi_{G^*}(T,N)\ge\phi_{G^*}(N,T)\). Every vertex in \(\rho\) is matched in _N_, hence \(\rho\) cannot contain any element of _W_. Thus \(T'=T\) when restricted to \(\rho\) and so \(\phi(T',N)\ge\phi(N,T')\) when restricted to the vertices of \(\rho\).

Now suppose \(\rho\) is an alternating path, and denote this path by _p_. As in the case of alternating cycles, we have \(\phi_{G^*}(T,N)\ge\phi_{G^*}(N,T)\) restricted to vertices of _p_. If _p_ does not contain any element of _W_, then _T_ and \(T'\) are identical on vertices of _p_ and so \(\phi(T',N)\ge\phi(N,T')\) in _G_. Moreover, note that vertices from _W_ cannot have degree 2 in _p_. So suppose one or both the endpoints of _p_ belong to _W_.

_Case 1._ Both endpoints of _p_ are in _W_. Since, by definition, vertices of _W_ are not matched by _N_, exactly one endpoint of _p_ is in _A_. If _p_ consists of a single edge (_a,b_), then \(a,b\in W\) and these vertices are indifferent between _N_ and \(T'\) since both these matchings leave them unmatched.

So let \(p=\langle a_1,b_1,\dots,a_t,b_t\rangle\), where \((a_i,b_i)\in T\) for \(1\le i\le t\), where \(t\ge 2\), and \(a_1,b_t\in W\) (see Fig. 4, left). Among the 2_t_ vertices of _p_, we have: \(\phi_{G^*}(T,N)=t_2\ge t\ge t_1=\phi_{G^*}(N,T)\).

a1
b1
a0
a2
b2
a1
b1
a3
a2
b3
b2

**Fig.4.** The blue solid edges are in _T_ while the black dashed edges are in _N_. In the figure on the left, both the endpoints of _p_ are in _W_ while in the figure on the right, exactly one endpoint of _p_ (i.e., _a_<sub>2</sub>) is in _W_.

