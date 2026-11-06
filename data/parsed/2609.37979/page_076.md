**Definition A.8.** An instance of Maximum Flow is a tuple _G_=(_V,E,c,s,t_) where (_V,E_) is a directed graph, \(c:E(G)\rightarrow\mathbb{R}_{\ge 0}\) are edge capacities, and \(s,t\in V\) are the source and sink vertex. A _flow_ is a mapping \(f:E(G)\rightarrow\mathbb{R}_{\ge 0}\) such that

• \(f(e)\le c(e)\) for all \(e\in E(G)\), and<tbc>

• \(\sum_{u\in N_{in}(v)}f(u,v)=\sum_{w\in N_{out}(v)}f(v,w)\) for all \(v\in V\backslash\{s,t\}\).

The objective is to find a flow _f_ that maximizes \(\mathrm{val}(f):=\sum_{w\in N_{out}(s)}f(s,w)\).

**Theorem A.9** (Maximum Flow in the Isomorphic-Priors Model)**.** _There is an algorithm that solves_ Maximum Flow _with k prior instances each having at most n vertices and m edges in O(k(n+m_)log_n_) _preprocessing time and O_((_n+m_)log_n_) _query time. Additionally, if each prior G<sub>i</sub> is equipped with a maximum flow, then the maximum flow for the query graph can be found in O_((_n+m_)log_n_) _query time._

For the proof, we require some additional basic tools. First, we generalize the neighborhood preservation property from Lemma 7.6.

**Lemma A.10** (Folklore)**.** _For every two (attributed) graphs_ \(G=(V_G,E_G,\alpha_G^V,\alpha_G^E)\) _and_ \(H=(V_H,E_H,\alpha_H^V,\alpha_H^E)\) _such that_ \(G\equiv_{1\text{-WL}}H\)_, the following holds:_

1. **_Neighborhood Multiset Preservation:_** _For every_ \(v\in V_G\) _and_ \(v'\in V_H\)_, if_ \(\chi_\infty^G(v)=\chi_\infty^H(v')\)_, then for every stable color C and edge attribute_ \(\ell\)_, it holds that_<tbc>

<tbc>\(\left|\left\{u\in V_G|\alpha_G^E(u,v)=\ell,\chi_\infty^G(u)=C\right\}\right|=\left|\left\{u'\in V_H|\alpha_H^E(u',v')=\ell,\chi_\infty^H(u')=C\right\}\right|.\)<tbc>

<tbc>_The analogous statement holds for outgoing edges._

Now let _G_=(_V,E,c,s,t_) be an instance of Maximum Flow, and let \(\chi_\infty^G\) denote the coloring computed by 1-WL. We define an auxiliary instance \(G/\chi_\infty=(V^*,E^*,c^*,s^*,t^*)\) via

• \(V^*=\{\chi_\infty^G(v)|v\in V\}\),<tbc>

• \(E^*=\{(\chi_\infty^G(v),\chi_\infty^G(w))|(v,w)\in E\}\),<tbc>

• \(c^*(a,b)=\sum_{v\in\chi^{-1}(a),w\in\chi^{-1}(b),(v,w)\in E}c(v,w)\),<tbc>

• \(s^*=\chi_\infty^G(s)\) and \(t^*=\chi_\infty^G(t)\).

The next two lemmas prove that the value of the maximum flow is identical in _G_ and \(G/\chi_\infty\).

**Lemma A.11.** _Let G_=(_V,E,c,s,t_) _be an instance of_ Maximum Flow _and let f be a flow in G. Then there exists a flow f_<sup>∗</sup> _in_ \(G/\chi_\infty\) _such that_ \(\mathrm{val}(f^*)\ge\mathrm{val}(f)\).

_Proof._ For \((a,b)\in E(G/\chi_\infty)\), we define

\(f^*(a,b):=\sum_{v\in\chi^{-1}(a),w\in\chi^{-1}(b),(v,w)\in E}f(v,w).\)

