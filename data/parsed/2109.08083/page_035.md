<tbc>Definition 3.23 (\(\mathcal{Z}_{i,G}^2\), \(\mathcal{Z}_{i,e,G}^2\), \(\mathcal{Z}_{i,e,G}^+(\text{bad})\)). For each \(i\in[c_g]\), define \(\mathcal{Z}_{i,G}^2\) to be the set of _i_-legal zero-sum configurations present in _G_ which contain at least two _i_-bad edges (all with positive sign attached). For each bad edge _e_, define \(\mathcal{Z}_{i,e,G}^2:=\{z\in\mathcal{Z}_{i,G}^2:e\in z\}\). Furthermore, we define \(\mathcal{Z}_{i,e,G}^+(\text{bad})\) to be the collection of _i_-legal zero-sum configurations in _G_ which contain the edge _e_ with positive sign, where _e_ is an _i_-bad edge.

This last piece of notation, \(\mathcal{Z}_{i,e,G}^+(\text{bad})\), is useful for when we are only interested in the fact that _e_ is _i_-bad, rather than the fact that _e_ is _i_-bad of a certain type.

Fact 3.24. _For every_ \(i\in[c_g]\) _the following hold:_

\(|\mathcal{Z}_{i,e,\mathcal{T}}^+(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
\Theta\left(j_it_1\right) & \text{\textit{if}}e\text{\textit{is a bad edge}}, \\
O\left(k_it_1\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{, and}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise}}.
\end{array}\right.\)<br>
\(|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
\Theta\left(t_1^2\right) & \text{\textit{if}}\alpha\neq 0\text{\textit{and}}\gamma=0\text{\textit{,}} \\
O\left(j_ik_i\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=0\text{\textit{, and}}\gamma=4\text{\textit{,}} \\
O\left(j_ik_i\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{, and}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise}}.
\end{array}\right.\)

_Finally, for every bad edge e,_

\(|\mathcal{Z}_{i,e,\mathcal{T}}^2|=O\left(k_it_1\right).\)

We note that in the fact above it would be equivalent to have ‘_n_’ in place of ‘_t_<sub>1</sub>’ for each clause, however we write _t_<sub>1</sub> here for convenient use later.

Proof. As previously noted, it is clear by construction for all but the non-zero cases. We start by considering the upper bounds for \(|\mathcal{Z}_{i,e,\mathcal{T}}^+(\alpha,\beta,\gamma)|\). In particular, every edge _e_ for which this is not clearly 0 has at least one vertex \(v\in J_i\). Given it is a bad edge we have \(v\in K_i\). We know that \(|\mathcal{Z}_{i,e,\mathcal{T}}^+(\text{bad})|\) has two degrees of freedom and that one of these must, along with _v_, dictate an edge with negative sign that is contained in _J<sub>i</sub>_. There are _O(j<sub>i</sub>_) choices that could dictate such an edge. Once such an edge is fixed, in order to extend the pair of edges intersecting at vertex _v_ to an _i_-legal zero-sum configuration, there is one remaining degree of freedom, and since all _i_-legal zero-sum configurations are contained in _I_<sub>_t_<sub>1</sub></sub> it is clear that there are _O(t_<sub>1</sub>) such choices. That gives, in total, _O(j<sub>i</sub>t_<sub>1</sub>) configurations when _e_ is an _i_-bad edge. In the case that _e_ is an edge of type (0,1,3)_<sub>i</sub>_, and so \(v\in J_i\backslash K_i\), we know that an edge of negative sign containing _v_ in an _i_-legal zero-sum configuration for _e_ is of type \((\alpha,\beta,0)_i\) with \(\alpha\neq 0\), so one degree of freedom, along with _v_ must dictate an edge containing a vertex in _K<sub>i</sub>_. There can be at most _O(k<sub>i</sub>_) such choices. Then once this is fixed, as before, there are _O(t_<sub>1</sub>) choices for the final degree of freedom given _O(k<sub>i</sub>t_<sub>1</sub>) _i_-legal zero-sum configurations containing _e_ of type (0,1,3)_<sub>i</sub>_ as a positive edge, as claimed. The argument is the same for \(|\mathcal{Z}_{i,e,\mathcal{T}}^2|\), since in this case, though _e_ is bad as in the first case, we know that the edge containing \(v\in e\) of negative sign must contain at least two vertices in _K<sub>i</sub>_. Thus the degree of freedom to dictate such an edge through _v_ has _O(k<sub>i</sub>_) possibilities.

Considering upper bounds on \(|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,\gamma)|\), it is clear when \(\alpha\neq 0\) and \(\gamma=0\), since there are two degrees of freedom and to ensure all vertices are in _I_<sub>_t_<sub>1</sub></sub> means at most _O(t_<sub>1</sub>) available choices for each. It remains to consider when _e_ is of type

