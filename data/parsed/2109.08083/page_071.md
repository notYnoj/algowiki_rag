<tbc>particular, we have that \(|\Delta Q^\pm(i)|\le(1+o(1))4e_d\) and thus \(\Delta Q^\pm(i)^2np\mathrm{log}^2(n)=O\left(b^{4/3}n^3p\mathrm{log}^4(n)\right)\checkmark b^2n^4\), satisfying the necessary requirements.

The calculations for the secondary variables are very similar to those for the vertex degrees but we provide the details here for completeness. First note that

\(\mathbb{E}'(\Delta E_{v,S}(i))=-\frac{1}{Q(i)}\sum_{e\in E_{T_i}(v,S)}\sum_{u\in e\backslash\{v\}}d_u(i)\pm O\left(\frac{E_{v,S}(i)}{Q(i)}\right),\)<br>
\(\mathbb{E}'(\Delta V_S(i))=-\frac{1}{Q(i)}\sum_{u\in V_i\cap S}d_u(i),\)<br>
\(\mathbb{E}'(\Delta Z_\mathcal{A}(i))=-\frac{1}{Q(i)}\sum_{z\in Z_\mathcal{A}(i)}\sum_{u\in z\backslash\{e\}}d_u(i)\pm O\left(\frac{Z_\mathcal{A}(i)}{Q(i)}\right),\)

The first equality follows identically to the case for vertex degrees. In particular, to see the expected number of edges lost to _E<sub>T<sub>i</sub></sub>(v,S_), since we are assuming that _v_ itself is not contained in the edge that is taken, when we sum over \(u\in e\backslash\{v\}\) we want to take into account all edges that contain _u_ except any that also contain _v_, but since pair degrees are at most two, and _u_ is only summed over since it is in an edge with _v_, that is at most two edge we want to exclude from the sum (explaining the \(\pm O\left(\frac{E_{v,S}(i)}{Q(i)}\right)\)).

To see the case for vertices in a subset of _V_(T), note that summing over the degree of each vertex in \(V(i)\cap S\) will count a particular edge for every vertex in the edge that is also in _S_. Thus the edge gets counted precisely the same number of times as the number of vertices in \(V(i)\cap S\) that would be lost if that edge were removed. For zero-sum configurations, firstly we remark that this calculation assumes that no edge is taken which contains a vertex from the fixed edge _e_ for which the number of zero-sum configurations is being considered. (As with degree-type properties, if this were the case, we set _Z_<sub>A</sub>(_i_+1)=_Z_<sub>A</sub>(_i)._) Now for a zero-sum configuration _z_, consider an edge \(f\in z\) such that \(e\cap f=\emptyset\). Then this edge is counted four times (in the degree of each of the four vertices of _f_) when summing over the vertices in _z_\\{_e_}, which is an over count since this contribution should count the number of edges whose removal would result in _z_ no longer being present in _T_<sub>_i_+1</sub>. However, due to the pair degrees being at most two, since every zero-sum configuration consists of a constant number of vertices, we cannot over count the number of edges interacting with the zero-sum configurations and the effect of their removal on the number of configurations in _Z_<sub>A</sub>(_i_+1) by more than _O(Z_<sub>A</sub>(_i_)).

Additionally note that since _e<sub>E<sub>v,S</sub></sub>_, _e<sub>V<sub>S</sub></sub>_ and _e<sub>Z<sub>A</sub></sub>_ are constant with respect to _p_, their derivatives disappear, and the second derivative of |_S|p_ also disappears. We see that

\(\mathbb{E}'(\Delta E_{v,S}^+(i))\le-\frac{3\big(|E_\mathcal{T}(v,S)|p^3+e_{E_{v,S}}-b^{1/3}|E_\mathcal{T}(v,S)|\big)\big(np^3-e_d-1\big)}{n^2p^4+e_q}\)<br>
\(+\frac{12|E_\mathcal{T}(v,S)|p^2}{|V(0)|}+O\left(\frac{|E_{\mathcal{T}(v,S)}|p}{|V(0)|^2}\right),\)

