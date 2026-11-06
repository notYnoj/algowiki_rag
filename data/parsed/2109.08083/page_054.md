(_v)_ _For every_ \(J\in\{X,Y,X+Y,X-Y\}\) _and every valid J-layer interval I<sup>J</sup> and_ \(v\notin J\),<tbc>

<tbc>\(|E_{\mathcal{T}^{-A^*}}(v,I^J,O/E)|=(1\pm O(p_A))|E_\mathcal{T}(v,I^J,O/E)|.\)<tbc>

_(vi)_ \(|\mathcal{T}^{-A^*}|=(1\pm O(p_A))n^2\).

Proof. We start by showing that whp _A_ is such that T<sup>-_A_</sup> satisfies all of the statements claimed for T<sup>-_A_<sup>∗</sup></sup>, with the exception that we shall not show that \(|V_O^{X+Y}(\mathcal{T}^{-A})|=|V_O^{X-Y}(\mathcal{T}^{-A})|\), nor the final claim on the number of edges in T<sup>-_A_<sup>∗</sup></sup> (since this will be easy to show directly in T<sup>-_A_<sup>∗</sup></sup>). Additionally we’ll upper bound |_A_| whp. We’ll then fix _A_ so that all of these hold, alongside the statements of Lemma 4.6, Proposition 4.9 and Lemma 4.10, which will be possible by a union bound.

When looking at the change from T to T<sup>-_A_</sup> for any property considered above, first note that the property is only affected if it involves consideration of vertices inside \(I'_{n^{10-4}}\). It follows from Chernoff bounds that whp \(|A|=(1\pm o(1))p_A|I'_{n^{10-4}}|\). Furthermore, for any subset \(S\subseteq I'_{n^{10-4}}\) with \(|S|=\Omega(n^{10-5})\) whp we have by Chernoff bounds that \(|S\cap A|=(1\pm o(1))p_A|S|\), and so then for any set \(S\subseteq V(\mathcal{T})\) (still with \(|S|=\Omega(n^{10-5})\)) we have that \(|V(\mathcal{T}[S])|\ge|V(\mathcal{T}^{-A}[S])|=|S|-|S\cap A|\ge(1\pm 2p_A)|S|\). Furthermore, \(|V_O^J(\mathcal{T})|=t_0\pm 1\), and \(|V_E^J(\mathcal{T})|=t_0\pm 1\) for every \(J\in\{X,Y,X+Y,X-Y\}\). Thus in (i) and (iv) where we are considering polynomially many subsets \(S\subseteq V(\mathcal{T})\), by union bounds with high probability all the statements of (i) and (iv) (apart from that \(|V_O^{X+Y}(\mathcal{T}^{-A})|=|V_O^{X-Y}(\mathcal{T}^{-A})|\)) hold with _A_ in place of _A_<sup>∗</sup>.

Considering degree-type properties, fix a vertex _v_ and a tuple (_S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) such that we are interested in _E_<sub>T<sup>-_A_</sup></sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>). (By abuse of notation, we let this include _J_-layer intervals as per (v).) Recall from Definitions 3.25 and 3.27 that we have \(|E_\mathcal{T}(v,S_1,S_2,S_3)|=\Theta(|S_1|)\). Let \(v_1,v_2,\dots,v_\chi\) be an enumeration of all vertices in \((I'_{n^{10-4}}\backslash\{v\})\cap(S_1\cup S_2\cup S_3)\). Using the vertex exposure martingale, let _X<sub>j</sub>_ be the expected number of edges from _E_<sub>T</sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) which are known to not be in _E_<sub>T<sup>-_A_</sup></sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) as a result of revealing vertices _v_<sub>1</sub>_,...,v<sub>j</sub>_. We have that \(|X_j-X_{j-1}|\le 2\) for every _j_, since the pair degree of _v_ and _v<sub>i</sub>_ is at most 2 for every \(i\in[\chi]\), and |_X<sub>j</sub>-X_<sub>_j_-1</sub>|=0 if there is no edge \(e\supseteq\{v,v_j\}\) such that \(e\in E_\mathcal{T}(v,S_1,S_2,S_3)\). Noting that _X_<sub>0</sub>=_O(p<sub>A</sub>|E_<sub>T</sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)|), by Azuma-Hoeffding we have that<tbc>

\(\mathbb{P}(|X_\chi-X_0|\ge p_A|S_1|)\le 2exp\left(-\frac{p_A^2|S_1|^2}{\Theta(|S_1|)}\right).\)

<tbc>Since \(p_A^2|S_1|\gg 1\) for every _S_<sub>1</sub> of interest, we have that whp<tbc>

\(|E_{\mathcal{T}^{-A}}(v,S_1,S_2,S_3)|=|E_\mathcal{T}(v,S_1,S_2,S_3)|\pm O(p_A|S_1|),\)

<tbc>where since \(|E_\mathcal{T}(v,S_1,S_2,S_3)|=\Theta(|S_1|)\) it follows that whp

\(|E_{\mathcal{T}^{-A}}(v,S_1,S_2,S_3)|=(1\pm O(p_A))|E_\mathcal{T}(v,S_1,S_2,S_3)|\)

for any tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) as in (ii) or (v). Hence, by union bounds, we have that (ii) and (v) hold for _A_ in place of _A_<sup>∗</sup>. It remains to consider the case for zero-sum configurations.

First note that the only cases that are non-trivial are when _e_ is a bad edge, or \(\alpha\neq 0\) and \(\gamma=0\). Otherwise, we only reduced numbers of configurations and so

