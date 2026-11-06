_Proof._ Color every vertex independently and uniformly from \[_k_\]. Every edge is monochromatic with probability 1_/k_, and therefore<tbc>

\(\mathbb{E}|M(c)|=\frac{|E(G)|}{k}\le\frac{\genfrac(){pt}{2}{n}{2}}{k}=\frac{n(n-1)}{2k}<\frac{n^2}{2k}.\)

<tbc>Thus some map _c_<sub>0</sub> satisfies |_M(c_<sub>0</sub>)|_\<n_<sup>2</sup>/(2_k_). By Lemma 3.1, every map has at least \(\varepsilon n^2\) monochromatic edges. Hence

\(\varepsilon n^2\le|M(c_0)|<\frac{n^2}{2k},\)

so \(\varepsilon<\frac{1}{2k}\).

## 4 A reconstruction lemma

Our aim is to construct a _k_-coloring with relatively few monochromatic edges. We do this by coloring the vertices in several stages. When coloring a new stage, we only need to count monochromatic edges joining its vertices to vertices in the same stage or in earlier stages. The general strategy is therefore to color the vertices from easy to difficult: vertices with large palette degrees are harder to handle and are deferred to later stages. At a given stage, vertices deferred to later stages are temporarily ignored. This is reflected in the construction below by emptying the palettes of these "more difficult" vertices. To control the total number of monochromatic edges, we assign each vertex a time at which its color is easiest to handle. The running minimum _E<sub>t</sub>_ records these best available thresholds.

**Lemma 4.1.** _Let_ \(P^0\supseteq P^1\supseteq\cdots\supseteq P^T\) _be palette systems with P_<sup>0</sup>(_v_)=\[_k_\] _for every v. Suppose that for every_ \(1\le t\le T\) _and every_ \(v\in U(P^t)\) _there is a color_ \(i\in P^t(v)\) _such that_ \(d_i^{P^t}(v)\le D_t\)_, where_ \(D_t\in[0,n]\)_, and suppose_<tbc>

\(\sum_{t=1}^TD_t\le kn.\) (1)

<tbc>_Let_<tbc>

\(a_t:=|U(P^{t-1})\backslash U(P^t)|,B_t:=\sum_{s=1}^ta_s=n-|U(P^t)|.\)

<tbc>_If_<tbc>

\(B_t\le\alpha tn(1\le t\le T),\) (2)

<tbc>_then there is a map_ \(c:V(G)\rightarrow[k]\) _with_<tbc>

\(|M(c)|\le\left(\alpha(k+1)+\frac{k}{T}\right)n^2.\) (3)

<tbc>_Proof._ Let _r_ be the first index attaining \(min_{1\le t\le T}D_t\). Then \(D_r\le kn/T\) since \(\sum_{t=1}^TD_t\le kn\). Define

\(E_0:=n,E_t:=min_{1\le s\le t}D_s.\)

Thus \(E_0\ge E_1\ge\cdots\ge E_T\) and \(\sum_{t=1}^TE_t\le kn\).

Let \(1=r_1<r_2<\cdots<r_j=r\) be the record indices of the running minimum, so that \(r_{\ell+1}\) is the next strict decrease after \(r_\ell\). Then<tbc>

\(E_{t-1}=D_{r_\ell}\text{whenever}r_\ell<t\le r_{\ell+1}.\) (4)

