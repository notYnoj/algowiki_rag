and, consequently, \(T=\emptyset\). We set _w=b_. For the domination rules, let \(D=D_1\cup D_w\) where<tbc>

\(D_1=\{(\{\{u,v\}\},\{u,v'\})|\{u,v\},\{u,v'\}\in E,\{u,v\}\in L\text{or}\{v,v'\}\in L\}.\)

<tbc>The case of _k\>_1 matching edges can be handled via auxiliary agents as explained for socially stable matching above. Again, this essentially affects only the domination rules, which allow more flexibility with respect to consistency. More formally, we define _N_, C_,w_ and _T_ as outlined above and change the remaining definitions to

\(\mathcal{C}_g=\mathcal{C}\)<br>
\(D=D_1\cup D_w\text{with}\)<br>
\(D_1=\{(\{\{u_i,v_j,e_{u,v}\}\},\{u_{i^\prime},v'_{j^\prime},e_{u,v}\})|\)<br>
\(\{u,v\},\{u,v'\}\in E,\{u,v\}\in L\text{or}\{v,v'\}\in L,i,i',j,j'=1\dots k\}.\)

## Friendship Matching

To embed an instance of friendship matching given by graph _G_=(_V,E_), edge benefits _b_, symmetric friendship values \(\alpha\), we use _N=V_ , C=C_<sub>g</sub>=E_, and, consequently, \(T=\emptyset\). To model the perceived utilities, we assume \(w(\{u,v\})=b(\{u,v\})+\alpha_{u,v}b(\{u,v\})\). For the domination rules, let \(D=D_1\cup D_2\cup D_w\) where

\(D_1=\{(\{\{u,v\}\},\{u,v'\})|\)<br>
\(\alpha_{v^\prime,v}b(\{u,v\})+\alpha_{v^\prime,u}b(\{u,v\})\ge b(\{u,v'\})+\alpha_{v^\prime,u}b(\{u,v'\})\}\)<br>
\(D_2=\{(\{\{u,v\},\{u',v'\}\},\{u,v'\})|\)<br>
\(b(\{u',v'\})+\alpha_{v^\prime,u^\prime} b(\{u',v'\})+\alpha_{v^\prime,v}b(\{u,v\})+\alpha_{v^\prime,u}b(\{u,v\})\)<br>
\(\ge b(\{u,v'\})+\alpha_{v^\prime,u}b(\{u,v'\})\}.\)

The domination rules in _D_<sub>1</sub> describe that \(v'\) earns more from existing {_u,v_} through friendship than from the candidate \(\{u,v'\}\). In _D_<sub>2</sub>, agent \(v'\) earns more from the combination of benefits from dropped agents than from the candidate \(\{u,v'\}\). Again, the case of _k\>_1 edges per agent can be included using auxiliary agents and preserves consistency as it affects only the domination rules.

Regarding correctness we only prove the case of _k_=1. The other cases are very similar.

Let _M_ be a matching in _G_. Now assume we have a perceived blocking pair \(\{u,v'\}\) for _M_ that we intend to resolve. Domination can only occur through edges involving _u_ or \(v'\).

Firstly, if _u_ and \(v'\) are unmatched, there cannot be any edges dominating \(\{u,v'\}\), and we can generate all matching edges as candidate coalitions via C_<sub>g</sub>_=C. Hence, perceived blocking pairs between unmatched agents are also undominated candidate coalitions. After adding \(\{u,v'\}\), no edge is removed. Hence, the set of coalitions resulting from the rules above exactly represents the matching after resolving the perceived blocking pair \(\{u,v'\}\).

