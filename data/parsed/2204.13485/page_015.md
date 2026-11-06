## 5 Preference extension problems

### 5.1 Fixed and arbitrary preferences

Now we turn our attention to problems where the preference list of each agent is either fixed or can be set arbitrarily. Such problems may arise, for example, when dealing with cheating strategies, where some of the agents might submit falsified preferences in order to get a desired stable matching.

Similar problems have been considered before, see e.g. \[15, 20\]. Kobayashi et al. \[20\] investigated problems where each preference list has to be complete. They showed that if the preferences are fixed for each man, then deciding whether there are preference lists of the women such that a partial matching _M_ is included in the men-optimal stable matching is NP-complete. On the positive side, they showed that if the preferences of all the women unmatched by _M_ are fixed too, then the problem becomes polynomial-time solvable.

The problems that we consider differ from previous results in several aspects: the completeness of the preference lists is not always assumed, the underlying graph might be non-bipartite, and some of the edges might be forced or forbidden to be contained in a stable matching. It should be emphasized that we are interested not only in men-optimal stable matchings, but in the existence of a stable matching satisfying the constraints in general.

The problems that are featured in this section are the followings.

K-forced-sm-strat

**Input:** A bipartite graph _G_=(_A,B;E_), strict preferences _\><sub>a</sub>_ for each man \(a\in A\), strict preferences _\><sub>b</sub>_ for some women \(b\in B\), and a partial matching \(\mu\) with \(|\mu|=K\).

**Question:** Are there preferences for the rest of the women such that there exists a stable matching containing \(\mu\)?

K-forbidden-sm-strat

**Input:** A bipartite graph _G_=(_A,B;E_), strict preferences _\><sub>a</sub>_ for each man \(a\in A\), strict preferences _\><sub>b</sub>_ for some women \(b\in B\), and a set of forbidden edges \(\tau\) with \(|\tau|=K\).

**Question:** Are there preferences for the rest of the women such that there exists a stable matching disjoint from \(\tau\)?

sr-strat

**Input:** A graph _G_=(_V,E_) and strict preferences _\><sub>v</sub>_ for some agents \(v\in V\) .

**Question:** Are there preferences for the rest of the agents such that there exists a stable matching _M_?

First we consider the complexities of 1-forced-sm-strat and 1-forbidden-sm-strat.

**Theorem 20.** 1-forced-sm-strat _and_ 1-forbidden-sm-strat _are NP-complete even if the preference list is fixed for none of the women._

_Proof._ We start with the proof for 1-forbidden-sm-strat; the problem is clearly in NP. To show NP-hardness, we reduce from min-pom, see the definition in Section 2.

Given an instance (_G_=(_A,B;E),\>),k_ of min-pom, we construct another bipartite graph _H_=(_U,W;F_), where _U_ is the set of men and _W_ is the set of women as follows. Let _n_:=|_A_|. We extend the original bipartite graph by adding _n-k_ women _s_<sub>1</sub>_,...,s_<sub>_n-k_</sub> to _B_ that will be called _selectors_. Finally, we add two men _u_ and \(u'\) to _A_ and a woman _w_ to _B_. So \(U=A\cup\{u,u'\}\)<tbc>

