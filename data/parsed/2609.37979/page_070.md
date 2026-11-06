## A Further Problems that are Invariant under 1-WL

We first provide the deferred proof of Lemma 7.14 concerning color-consistent strategies for Energy Game. We then give further examples of problems that are invariant under 1-WL and can therefore be solved in near-linear time in the Isomorphic-Priors model.

### A.1 Color-Consistent Strategies for Energy Game

_Proof of Lemma 7.14._ Let _h(v_) be the minimum initial energy required to win from _v_. By assumption, \(\sigma\) wins from every starting vertex _v_ with initial energy _h(v_). The shadow-play argument using Neighborhood Preservation in the proof of Theorem 7.12 shows that vertices of the same stable 1-WL color have the same minimum initial energy. Thus _h_ is constant on each color class.

For each color class _C_, choose an arbitrary representative \(r_C\in C\) and define _H(C_):=_h(r<sub>C</sub>_). For each stable color class \(C\subseteq V_1\) and each \(u\in C\), choose

\(\widehat{\sigma}(u)\in\big\{v\in V\big|(u,v)\in E,w(u,v)=w(r_C,\sigma(r_C)),\chi_\infty^G(v)=\chi_\infty^G(\sigma(r_C))\big\}.\)

This set is nonempty by Neighborhood Preservation.

Let \((u,v)\in E\) be an edge consistent with \(\widehat{\sigma}\), meaning that either \(u\in V_2\) or \(v=\widehat{\sigma}(u)\). Denote \(C=\chi_\infty^G(u)\) and \(D=\chi_\infty^G(v)\). There exists a \(\sigma\)-consistent edge (_r<sub>C</sub>,z_) with _w(r<sub>C</sub>,z_)=_w(u,v_) and<tbc>

