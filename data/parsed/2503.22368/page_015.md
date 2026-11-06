# Maximum Common Subgraphs

15

\((V(G),\nu_G,\varepsilon_G)\) and call such structures labeled graphs. In essence, one can think of such labeled graphs as "complete edge- and vertex-colored graphs."

Two labeled graphs _G_ and _H_ are isomorphic, in symbols \(G\simeq H\), if there is a bijective map \(\varphi:V(G)\rightarrow V(H)\) such that the following conditions are satisfied.

1. \(\nu_G(v)=\nu_H(\varphi(v))\) for all \(v\in V(G)\); and<tbc>

2. \(\{u,v\}\in\genfrac(){pt}{2}{V(G)}{2}\) if and only if \(\{\varphi(u),\varphi(v)\}\in\genfrac(){pt}{2}{V(H)}{2}\); and<tbc>

**3.** \(\varepsilon_G(\{u,v\})=\varepsilon_H(\{\varphi(u),\varphi(v)\})\) for all \(\{u,v\}\in\genfrac(){pt}{2}{V(G)}{2}\).

An _(induced) subgraph_ \(H\subseteq G\) of labeled graph _G_ is a labeled graph _H_ such that \(V(H)\subseteq V(G)\) and \(\nu_H(v)=\nu_G(v)\) for all \(v\in V(H)\) and \(\varepsilon_H(\{u,v\})=\varepsilon_G(\{u,v\})\) for all \(\{u,v\}\in\genfrac(){pt}{2}{V(H)}{2}\). A _common subgraph_ of labeled graphs \(G_1,\dots,G_\ell\) is a labeled graph _H_ that is isomorphic to an induced subgraph _H<sub>i</sub>_ in each _G<sub>i</sub>_.

### D Related works

In this section, we provide an overview of the problem and closely related topics in the literature. The maximum common subgraph (MCS) problem has long been central to molecular informatics, as it provides a rigorous means for comparing molecular structures \[21,22\]. Due to its wide range of applications, several variants of the MCS problem have been investigated in the literature. Early work in chemical database management highlighted the need for robust molecular representations and efficient subgraph matching techniques, leading researchers to adopt graph-based models that capture both atom connectivity and functional group organization \[23,24,25,26,27,28\]. A key insight from these studies was the dual nature of the MCS problem: while many investigations have focused on pairwise comparisons between two molecular graphs, there is also significant interest in extending these methods to handle more than two molecules simultaneously in order to extract common structural motifs \[29\].

A further complication in the MCS domain is the distinction between two related formulations. Many methods target the maximal common induced subgraph (MCIS), defined as the largest vertex-induced subgraph common to the compared molecules, while other methods focus on the maximal common edge subgraph (MCES), which maximizes the number of shared edges \[30,31\]. This duality has led to a generalized classification framework for MCS algorithms that not only categorizes them as exact or approximate but also distinguishes whether the resulting subgraph must be connected or may be disconnected \[32,33,34,35\].

Several early approaches recast the MCS problem as a maximal clique detection problem in the modular product or so-called compatibility (or association) graph. In these methods, potential correspondences between atoms or bonds in two molecular graphs are represented as vertices in a compatibility graph, and a maximal clique corresponds directly to an MCIS (or MCES) of the original graphs. Pioneering clique-detection algorithms such as those by Bron and Kerbosch \[32\] and subsequent adaptations like the method of Carraghan and

