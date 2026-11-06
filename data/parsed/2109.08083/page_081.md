\(|\mathcal{Z}_{i,e,H_1}^-(\alpha,\beta,\gamma)|\le\left\{\begin{array}{ c c }
c_{1,8}|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12} & \text{\textit{if}}\alpha\neq 0\text{\textit{and}}\gamma=0\text{\textit{,}} \\
c_{1,8}j_ik_ip_\mathrm{gr}^{12} & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=0\text{\textit{,}}\gamma=4\text{\textit{,}} \\
c_{1,8}j_ik_ip_\mathrm{gr}^{12} & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{,}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)

<tbc>_Additionally, for every bad edge e,_<tbc>

\(|\mathcal{Z}_{i,e,H_1}^2|\le c_{1,8}k_it_1p_\mathrm{gr}^{12}.\)

<tbc>_Furthermore,_<tbc>

\(|\mathcal{Z}_{i,e,H_1}^+(\alpha,\beta,\gamma)|\ge c_{1,7}|\mathcal{Z}_{i,e,\mathcal{T}}^+(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12}\text{\textit{if}}e\text{\textit{is a bad edge,}}\)

<tbc>_and_<tbc>

\(|\mathcal{Z}_{i,e,H_1}^-(\alpha,\beta,\gamma)|\ge c_{1,7}|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12}\text{\textit{if}}\alpha\neq 0\text{\textit{and}}\gamma=0.\)

_(vi)_ \(|V_O^{X+Y}(H_1)|=|V_O^{X-Y}(H_1)|\) _and_ \(|V_E^{X+Y}(H_1)|=|V_E^{X-Y}(H_1)|\).

Our aim in this chapter is to cover most of the vertices of _H_ by a matching leaving only a small subset \(L^*\subseteq I_{n^{10-5}}\) uncovered. Recall that an additional property required of _L_<sup>∗</sup> is that \(|V_O^{X+Y}(L^*)|=|V_O^{X-Y}(L^*)|\) and \(|V_E^{X+Y}(L^*)|=|V_E^{X-Y}(L^*)|\). As discussed in Section 3.5, this condition is affected by use of wrap- around edges, and only affected when _n_ is odd. Hence, an additional constraint on the matching we find in _H_ is that the number of wrap-around edges using odd- even parity matches the number using even-odd parity in parts _X+Y_ and _X-Y_ . Having reached _H_ which does satisfy these parity requirements, as the process to reach _L_<sup>∗</sup> only removes disjoint matchings we only need to keep an eye on the parity conditions when _n_ is odd.

As described in Section 3.1 we plan to obtain the required matching for _H_ over a sequence of nested subgraphs \(H\supseteq H_0\supseteq H_1\supseteq\dots\supseteq H_{c_h}\supseteq L^*\), where \(H_i\subseteq I_{t_i}\). This process involves \(\Theta(\mathrm{log}(n))\) subgraphs to reach _L_<sup>∗</sup>. It is natural to think that one might try to have a larger distance between vertices of the largest index in consecutive nested intervals, however the factor 1_/c_<sub>vor</sub>∼0.8 needs to be sufficiently large to ensure the process works. In particular, the process to go from _H<sub>i</sub>_ to _H_<sub>_i_+1</sub> requires one to find a matching to cover all vertices in _V(H<sub>i</sub>_)\\_I_<sub>_t<sub>i</sub>_+1</sub>. We do this in two steps: firstly we find an ‘almost-cover’, that is, we find a matching that covers all but a _o_(1) proportion of the vertices which are present in _V(H<sub>i</sub>_)\\_I_<sub>_t<sub>i</sub>_+1</sub>. Then we run a random greedy algorithm to cover the vertices which still remain uncovered in _V(H<sub>i</sub>_)\\_I_<sub>_t<sub>i</sub>_+1</sub> after the almost-cover. To enable the random greedy algorithm to run, we need that every vertex remaining in _V(H<sub>i</sub>_)\\_I_<sub>_t<sub>i</sub>_+1</sub> is in many edges that otherwise contain only vertices in _H<sub>i</sub>_\[_I_<sub>_t<sub>i</sub>_+1</sub>\]. Since every edge that contains a vertex of index |_t_| must also contain a distinct vertex with index of order at least |_t/_2|, we certainly don’t want \(c_\mathrm{vor}\le 1/2\). Additionally, the ‘shape’ of the sets _I<sub>t<sub>i</sub></sub>_ is important to ensure that each vertex in _V(H<sub>i</sub>_) is in enough edges to ensure the random greedy algorithm does not abort. There is some flexibility to be had in both the shape of _I<sub>t<sub>i</sub></sub>_ and the value of _c_<sub>vor</sub> which ensure that the following arguments still work, but of the other possibilities, there is nothing to be gained by using a different choice.

**6.1.1. The weight shuffle.** Recall at the end of Section 3.1 we discuss the required _weight shuffle_, a process that shifts weight between edges preserving the weighted degree at each vertex. As part of the process to obtain the vortex \(H\supseteq H_0\supseteq H_1\supseteq\dots\supseteq H_{c_h}\supseteq L^*\), we obtain the almost-cover for _V(H<sub>i</sub>_)\\_I_<sub>_t<sub>i</sub>_+1</sub> using

