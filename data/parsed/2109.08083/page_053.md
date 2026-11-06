<tbc>vertex is in _A_ or not may affect \(|C_{e_T}^A|\) by \(O(n^{5\times 10^{-4}})\) (- since fixing it, there are five free variables remaining to dictate the cascade).

Choosing a cascade greedily, one by one for each of the \(O(n^{5.4\times 10^{-5}})\) edges for which we wish to build a cascade, every edge _e_ (and related quintuple _e<sub>T</sub>_) has a choice of at least \(\Theta(p_A^{48}n^{6\times 10^{-4}})-O(n^{5.4\times 10^{-5}}n_c^5)=\Theta(p_A^{48}n^{6\times 10^{-4}})-O(n^{5.54\times 10^{-4}})\) cascades which are almost-disjoint from any previous choices. □

In what follows we’ll show that with high probability, as well as _A_ being such that Lemmas 4.6, 4.9 and 4.10 are all satisfied simultaneously, we can find \(A^*\supseteq A\) such that _A_<sup>∗</sup> is an absorber for any possible leave _L_ satisfying the conditions noted at the beginning of the chapter, and T<sup>-_A_<sup>∗</sup></sup>:=T\[_V_(T)\\_A_<sup>∗</sup>\] has ‘nice’ properties that leave us in a good position to continue with the random greedy count that follows. In particular, by union bounding we’ll be able to show that Lemmas 4.6, 4.9 and 4.10 are all satisfied simultaneously, and then fixing a collection of almost-disjoint cascades for each of the possible edges \(e\in\mathcal{T}[A']\backslash T'\) (now that _A_ is fixed), we can extend _A_ to a collection of vertices _A_<sup>∗</sup> that has a perfect matching by considering all vertices remaining in _A_ which have not been assigned to any of the almost-disjoint cascades, and covering these vertices by a matching avoiding all other vertices in _A_. We’ll show that |_A_| is small enough that we can do this greedily, without having too much of an adverse effect on any property we wish to maintain, and by nature of _A_ being picked in a uniformly random way, T<sup>-_A_<sup>∗</sup></sup> is well structured.

Theorem 4.11. _There exists a set_ \(A^*\supseteq A\) _such that A_<sup>∗</sup> _is an absorber for any qualifying leave L_<sup>∗</sup>_, and_ T<sup>-_A_<sup>∗</sup></sup> _satisfies the following:_

(_i)_ _every_ T _-valid subset_ \(S\subseteq V(\mathcal{T})\) _satisfies_<tbc>

<tbc>\(|V(\mathcal{T}^{-A^*}[S])|=(1\pm O(p_A))|S|,\)<tbc>

(_ii)_ _for every_ \(v\in V(\mathcal{T}^{-A^*})\) _and every open or closed_ T _-valid tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)_, we have_<tbc>

<tbc>\(|E_{\mathcal{T}^{-A^*}}(v,S_1,S_2,S_3)|=(1\pm O(p_A))|E_\mathcal{T}(v,S_1,S_2,S_3)|,\)<tbc>

_(iii)_ _for every_ \(i\in[c_g]\),<tbc>

<tbc>\(|\mathcal{Z}_{i,e,\mathcal{T}^{-A^*}}^+(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm O(p_A))|\mathcal{Z}_{i,e,\mathcal{T}}^+(\alpha,\beta,\gamma)| & \text{\textit{if}}e\text{\textit{is a bad edge,}} \\
O\left(k_it_1\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{,}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)<tbc>

<tbc>\(|\mathcal{Z}_{i,e,\mathcal{T}^{-A^*}}^-(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm O(p_A))|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,\gamma)| & \text{\textit{if}}\alpha\neq 0\text{\textit{and}}\gamma=0\text{\textit{,}} \\
O\left(j_ik_i\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=0\text{\textit{,}}\gamma=4\text{\textit{,}} \\
O\left(j_ik_i\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{,}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)<tbc>

<tbc>_Finally, for every bad edge e,_<tbc>

<tbc>\(|\mathcal{Z}_{i,e,\mathcal{T}^{-A^*}}^2|=O\left(k_it_1\right).\)<tbc>

_(iv)_ \(|V_O^{X+Y}(\mathcal{T}^{-A^*})|=|V_O^{X-Y}(\mathcal{T}^{-A^*})|\), \(|V_E^{X+Y}(\mathcal{T}^{-A^*})|=|V_E^{X-Y}(\mathcal{T}^{-A^*})|\) _and, furthermore_ \(|V_O^J(\mathcal{T}^{-A^*})|=(1\pm O(p_A))|V_E^J(\mathcal{T}^{-A^*})|\) _for every_ \(J\in\{X,Y,X+Y,X-Y\}\).

_Additionally,_ \(|V_{O/E}^{J_1}(\mathcal{T}^{-A^*}[S])|=(1\pm O(p_A))|V_{O/E}^{J_2}(\mathcal{T}^{-A^*}[S])|\) _for every valid layer interval S, and_ \(J_1,J_2\in\{X,Y,X+Y,X-Y\}\).

