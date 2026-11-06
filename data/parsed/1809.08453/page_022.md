<tbc>2_n_<sup>2</sup> triples, and _k_-1 components per vector of triples in \(T_{(k-1)}^\downarrow\));

\- Line 5 is in _O(n_<sup>4</sup>);

\- Lines 6-7 are in _O_(2_n_<sup>2</sup>).

Overall, the complexity of Algorithm 1 thus is _O_(2_<sup>K</sup>n_<sup>2_K_+4</sup>).

## Final remarks.

At the end of Algorithm 1, one obtains a set \(T_K^\downarrow\) of vectors of triples. Within this set, one can choose a vector **v**<sup>∗</sup> which realizes:<tbc>

\(min_{\mathbf{v}\in T_K^\downarrow}\mathtt{GGI}_\unknown(\mathbf{v})=min_{\mathbf{x}\in\mathcal{X}}\mathtt{GGI}_\unknown(\mathbf{d}(\mathbf{x})).\)

<tbc>Given this vector **v**<sup>∗</sup>, any stable marriage **x**<sup>∗</sup> such that \(\mathbf{v}^*\in T_K^\downarrow(\mathbf{x}^*)\) verifies

\(\mathtt{GGI}_\unknown(\mathbf{d}(\mathbf{x}^*))=min_{\mathbf{x}\in\mathcal{X}}\mathtt{GGI}_\unknown(\mathbf{d}(\mathbf{x})).\)

Given **v**<sup>∗</sup>, it is easy to compute a stable marriage **x**<sup>∗</sup> such that \(\mathbf{v}^*\in T_K^\downarrow(\mathbf{x}^*)\). In particular, **x**<sub>IN<sub>**v**<sup>∗</sup></sub></sub> (resp. **x**<sub>_P_\\OUT<sub>**v**<sup>∗</sup></sub></sub>) is a best possible stable marriage for men (resp. women) where sets IN<sub>**v**<sup>∗</sup></sub> and OUT<sub>**v**<sup>∗</sup></sub> are generated in the same fashion as in Algorithm 2 (Lines 1-9).

input : the GGISM instance and the value of K<br>
output: \(T_K^\downarrow\)<br>
\(T_0^\downarrow\leftarrow\{()\}\)<br>
for k=1,...,K<br>
   \(T_k^\downarrow\leftarrow\emptyset\)<br>
   for \(\mathbf{v}\in T_{k-1}^\downarrow\)<br>
   \(T\leftarrow\mathtt{NextTriples}(\mathbf{v},k)\)<br>
   for \(t\in T\)<br>
   \(T_k^\downarrow\leftarrow T_k^\downarrow\cup\{\mathbf{v}\circ t\}\)<br>
   return \(T_K^\downarrow\)

input : vector **v** of imposed triples, index k of the next triple<br>
output: set T of possible next triples<br>
\(\mathtt{IN}_\mathbf{v}\leftarrow\emptyset\); \(\mathtt{OUT}_\mathbf{v}\leftarrow\emptyset\); \(\mathcal{A}_\overrightarrow{\mathbf{v}}\leftarrow\mathcal{M}\cup\mathcal{W}\)<br>
for i=1,...,k-1<br>
   \((a,a',d)=v_i\), \(\mathcal{A}_\overrightarrow{\mathbf{v}}\leftarrow\mathcal{A}_\overrightarrow{\mathbf{v}}\backslash\{a\}\)<br>
   \(\mathtt{IN}_\mathbf{v}\leftarrow\mathtt{IN}_\mathbf{v}\cup\{\rho_\mathtt{get}(a,a')\}\cup\mathtt{Anc}(\rho_\mathtt{get}(a,a'))\)<br>
   \(\mathtt{OUT}_\mathbf{v}\leftarrow\mathtt{OUT}_\mathbf{v}\cup\{\rho_\mathtt{break}(a,a')\}\cup\mathtt{Desc}(\rho_\mathtt{break}(a,a'))\)<br>
for \(\rho\in P\backslash\mathtt{OUT}_\mathbf{v}\) s.t. \(d_\mathrm{max}^w(\rho)>d_\mathrm{min}(v)\)<br>
   \(\mathtt{IN}_\mathbf{v}\leftarrow\mathtt{IN}_\mathbf{v}\cup\{\rho\}\cup\mathtt{Anc}(\rho)\)<br>
for \(\rho\in P\backslash\mathtt{IN}_\mathbf{v}\) s.t. \(d_\mathrm{max}^m(\rho)>d_\mathrm{min}(v)\)<br>
   \(\mathtt{OUT}_\mathbf{v}\leftarrow\mathtt{OUT}_\mathbf{v}\cup\{\rho\}\cup\mathtt{Desc}(\rho)\)<br>
return \(\mathtt{NextWomen}(\mathtt{IN}_\mathbf{v},\mathtt{OUT}_\mathbf{v},k,\mathcal{A}_\overrightarrow{\mathbf{v}})\cup\mathtt{NextMen}(\mathtt{IN}_\mathbf{v},\mathtt{OUT}_\mathbf{v},k,\mathcal{A}_\overrightarrow{\mathbf{v}})\)

**Algorithm 1:** `Enumerate`

**Algorithm 2:** `NextTriples`

