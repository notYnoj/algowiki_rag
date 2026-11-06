**Lemma 7.6** (1-WL Properties; Folklore)**.** _For every two (attributed) graphs_ \(G=(V_G,E_G,\alpha_G^V,\alpha_G^E)\) _and_ \(H=(V_H,E_H,\alpha_H^V,\alpha_H^E)\) _such that_ \(G\equiv_{1\text{-WL}}H\)_, the following holds:_

1. **_Refinement:_** _For every_ \(v\in V_G\) _and_ \(v'\in V_H\)_, if_ \(\chi_\infty^G(v)=\chi_\infty^H(v')\)_, then their initial colors match:_ \(\alpha_G^V(v)=\alpha_H^V(v')\).<tbc>

_2._ **_Neighborhood Preservation:_** _For every_ \(v\in V_G\) _and_ \(v'\in V_H\)_, if_ \(\chi_\infty^G(v)=\chi_\infty^H(v')\)_, then for every stable color C and edge attribute_ \(\ell\)_, there exists an incoming edge_ \((u,v)\in E_G\) _in G such that_ \(\alpha_G^E(u,v)=\ell\) _and_ \(\chi_\infty^G(u)=C\) _if and only if there exists an incoming edge_ \((u',v')\in E_H\) _in H such that_ \(\alpha_H^E(u',v')=\ell\) _and_ \(\chi_\infty^H(u')=C\)_. The analogous bi-conditional holds for outgoing edges._

_Remark_ 7.7. The 1-WL algorithm actually guarantees stronger properties than the above (see Lemma A.10). However, the properties above suffice to get results in this section.

_Proof Sketch of Lemma 7.6._ Let \(v\in V_G\) and \(v'\in V_H\) such that \(\chi_\infty^G(v)=\chi_\infty^H(v')\). Also let \(i_\infty\ge 0\) be minimal such that \(\chi_{i_\infty}^G\equiv\chi_{i_\infty+1}^G\). So \(\chi_\infty^G\equiv\chi_{i_\infty+1}^G\) and, since \(G\equiv_{1\text{-WL}}H\) and \(\chi_\infty^G(v)=\chi_\infty^H(v')\), we also get that \(\chi_\infty^H\equiv\chi_{i_\infty+1}^H\). By definition, it holds for all \(i\ge 0\) that, if \(\chi_{i+1}^G(v)=\chi_{i+1}^H(v')\), then \(\chi_i^G(v)=\chi_i^H(v')\). So the first part follows by induction.

To prove Neighborhood Preservation, consider the coloring \(\chi^*:V(G)\unknown V(H)\rightarrow\mathcal{C}\) defined on the disjoint union of _G_ and _H_ via \(\chi^*(w):=\chi_\infty^G(w)\) for all \(w\in V(G)\), and \(\chi^*(w'):=\chi_\infty^H(w')\) for all \(w'\in V(H)\). Since \(G\equiv_{1\text{-WL}}H\), it can be verified that the coloring \(\chi^*\) is stable for the disjoint union of _G_ and _H_, and in fact \(\chi_\infty^{G\unknown H}\equiv\chi^*\) (since all refinements being made on _G_ or _H_ also happen on \(G\unknown H\)). In particular, we get that \(\chi_\infty^{G\unknown H}(v)=\chi_\infty^{G\unknown H}(v')\). By definition, we conclude that

\(\left\{\left\{\left(\chi_\infty^{G\unknown H}(u),\alpha_G^E(u,v)\right)|u\in N_{in}(v)\right\}\right\}=\left\{\left\{\left(\chi_\infty^{G\unknown H}(u'),\alpha_H^E(u',v')\right)|u'\in N_{in}(v')\right\}\right\}.\)

In particular, a pair \((C,\ell)\) appears in the first set if and only if it appears in the second set.

By repeatedly applying Lemma 7.6 (Neighborhood Preservation), every sequence of valid steps in _G_ can be identically mirrored step-by-step in _H_. This sequential matching gives rise to the Walk Lifting property.

**Lemma 7.8** (Walk Lifting)**.** _Let_ \(G=(V_G,E_G,\alpha_G^V,\alpha_G^E)\) _and_ \(H=(V_H,E_H,\alpha_H^V,\alpha_H^E)\) _be (attributed) graphs such that_ \(G\equiv_{1\text{-WL}}H\)_. Also let_ \(v_0\in V_G\) _and_ \(v'_0\in V_H\) _such that_ \(\chi_\infty^G(v_0)=\chi_\infty^{G^\prime}(v'_0)\)_. For every directed walk W_=(_v_<sub>0</sub>_,e_<sub>1</sub>_,v_<sub>1</sub>_,...,e<sub>r</sub>,v<sub>r</sub>_) _in G, there exists a corresponding directed walk_ \(W'=(v'_0,e'_1,v'_1,\dots,e'_r,v'_r)\) _in H such that_ \(\chi_\infty^G(v_i)=\chi_\infty^H(v'_i)\) _for all_ \(0\le i\le r\)_, and_ \(\alpha_G^E(e_j)=\alpha_H^E(e'_j)\) _for all_ \(1\le j\le r\).

_Proof._ We proceed by induction on the length of the walk _r_.

In the case case _r_=0, the walk _W_ consists of a single vertex _v_<sub>0</sub>. We set \(W'\) to be the walk consisting only of \(v'_0\). By the lemma’s hypothesis, \(\chi_\infty^G(v_0)=\chi_\infty^H(v'_0)\), so the condition holds trivially.

So assume the claim holds for walks of length _k\<r_. Let _W<sub>k</sub>_=(_v_<sub>0</sub>_,...,e<sub>k</sub>,v<sub>k</sub>_) be the prefix of length _k_ in _G_, which by the inductive hypothesis lifts to a valid walk \(W'_k=(v'_0,\dots,e'_k,v'_k)\) in _H_ where \(\chi_\infty^G(v_k)=\chi_\infty^H(v'_k)\).

The next step in _W_ traverses the edge _e_<sub>_k_+1</sub>=(_v<sub>k</sub>,v_<sub>_k_+1</sub>) with some attribute \(\ell=\alpha_G^E(e_{k+1})\). Let \(C=\chi_\infty^G(v_{k+1})\) be the stable color of the destination vertex. By Lemma 7.6 (Neighborhood Preservation), since \(\chi_\infty^G(v_k)=\chi_\infty^{G^\prime}(v'_k)\), the existence of an outgoing edge from _v<sub>k</sub>_ to a vertex of color _C_ with attribute \(\ell\) guarantees the existence of an outgoing edge \(e'_{k+1}=(v'_k,v'_{k+1})\) in _H_ with attribute \(\alpha_H^E(e'_{k+1})=\ell\) such that \(\chi_\infty^H(v'_{k+1})=C\). Appending this edge \(e'_{k+1}\) and vertex \(v'_{k+1}\) to \(W'_k\) yields a valid walk of length _k_+1 satisfying all conditions.

