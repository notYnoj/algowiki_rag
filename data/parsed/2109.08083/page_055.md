<tbc>by Fact 3.24 the statements hold. Considering the two remaining cases, we start by proving that for every bad edge _e_, \(|\mathcal{Z}_{i,e,\mathcal{T}^{-A}}^+(\mathrm{bad})|=(1\pm O(p_A))|\mathcal{Z}_{i,e,\mathcal{T}}^+(\mathrm{bad})|\). Fix an _i_-bad edge _e_ and let \(v_1,v_2,\dots,v_{\chi^\prime}\) be an enumeration of all vertices in \(I'_{n^{10-4}}\backslash e\), ordered by the modulus of the coordinate they are indexed by, splitting ties arbitrarily. Let _Y<sub>j</sub>_ be the expected number of _i_-legal zero-sum configurations containing _e_ which are known to not be in T<sup>-_A_</sup> as a result of revealing vertices _v_<sub>1</sub>_,...,v<sub>j</sub>_. Then note that for a vertex \(v_j\in J_i\) we have that |_Y<sub>j</sub>-Y_<sub>_j_-1</sub>|=_O(t_<sub>1</sub>), since the number of _i_-legal zero-sum configurations containing _e_ and vertex _v<sub>j</sub>_ leave one degree of freedom which can take _O(t_<sub>1</sub>) values. However, for a vertex \(v_j\in I'_{n^{10-4}}\backslash J_i\) we find that the remaining degree of freedom to dictate an _i_-legal zero-sum configuration containing _e_ and _v<sub>j</sub>_ is of _O(j<sub>i</sub>_) (and there are _O(n_<sup>10<sup>-4</sup></sup>) such vertices to consider). Furthermore, we have that \(Y_0=O(p_A|\mathcal{Z}_{i,e,\mathcal{T}}^+(\mathrm{bad})|)\). Thus by Azuma-Hoeffding we have that<tbc>

\(\mathbb{P}(|Y_{\chi^\prime}-Y_0|\ge p_Aj_it_1)\le 2\mathrm{exp}\left(-\frac{p_A^2j_i^2t_1^2}{\Theta(j_it_1^2)}\right).\)

<tbc>Since \(p_A^2j_i\gg 1\) for every \(i\in[c_g]\), we have, using Fact 3.24, that whp<tbc>

\(|\mathcal{Z}_{i,e,\mathcal{T}^{-A}}^+(\mathrm{bad})|=|\mathcal{Z}_{i,e,\mathcal{T}}^+(\mathrm{bad})|\pm O(p_Aj_it_1),\)

<tbc>or equivalently that whp

\(|\mathcal{Z}_{i,e,\mathcal{T}^{-A}}^+(\mathrm{bad})|=(1\pm O(p_A))|\mathcal{Z}_{i,e,\mathcal{T}}^+(\mathrm{bad})|\)

for any _i_-bad edge _e_ and every \(i\in[c_g]\).

Considering now \(|\mathcal{Z}_{i,e,\mathcal{T}^{-A}}^-(\alpha,\beta,0)|\) with \(\alpha\neq 0\), we have that the statement holds via a greedy argument. In particular, letting _e_ be a fixed edge of type \((\alpha,\beta,0)_i\) with \(\alpha\neq 0\) and consider the _i_-legal zero-sum configurations containing _e_, note that all other vertices in the configuration have index \(\Omega(j_i)\). If \(j_i\gg n^{10-4}\) this implies that all _i_-legal zero-sum configurations containing _e_ survive the removal of _A_ from T . If _j<sub>i</sub>=O(n_<sup>10<sup>-4</sup></sup>) this is not the case, however the number of configurations lost is small. In particular, we have two degrees of freedom to define a zero-sum configuration containing _e_, each of which can take values in a \(\Theta(t_1)\) sized range, and vertices outside _e_ will only fall in \(I'_{n^{10-4}}\) when (at least) one of these degrees of freedom is chosen in a particular _O(n_<sup>10<sup>-4</sup></sup>) range. Thus, we could only lose at most _O(n_<sup>10<sup>-4</sup></sup>_t_<sub>1</sub>) of the _i_-legal configurations containing _e_ moving from T to T<sup>-_A_</sup>. So we find that \(|\mathcal{Z}_{i,e,\mathcal{T}^{-A}}^-(\alpha,\beta,0)|=|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,0)|\pm O(n^{10-4}t_1)\), and since \(|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,0)|=\Theta(t_1^2)\), this gives

\(|\mathcal{Z}_{i,e,\mathcal{T}^{-A}}^-(\alpha,\beta,0)|=(1\pm O(n^{-0.999}))|\mathcal{Z}_{i,e,\mathcal{T}}^-(\alpha,\beta,0)|,\)

which gives the desired result since \(p_A\gg n^{-0.999}\).

Taking union bounds, we find that with high probability all of the above events hold for _A_. We fix _A_ accordingly. This yields \(A\subseteq I'_{n^{10-4}}\) and a template matching \(T'\) covering all vertices in \(A'=A\cap I'_{n^{2.7\times 10-5}}\), such that every possible edge \(e\in\mathcal{T}[A']\backslash T'\) has a cascade such that these cascades are almost-disjoint. For each such cascade, \(C'_{eT}\), taking the edges of \(C'_{eT}\) which are in \(T'\), we obtain a perfect matching for \(C'_{eT}\) by additionally taking the other edges of the same sign as _T<sub>i</sub>_ in each of _Z<sub>i</sub>_. Denote this matching by _M<sub>eT</sub>_. Then \(\bigcup_{eT}M_{eT}\) is a perfect matching for \(\bigcup_{eT}C'_{eT}\) since, by construction, every pair of matchings _M<sub>eT</sub>_ and \(M_{eT}\) are either

