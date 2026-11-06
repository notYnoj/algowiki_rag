<tbc>**Theorem 1.2** (Mixed spiders)**.** _Let_ \(k\ge 0\) _and_ \(l\ge 1\)_, and put N_=2_<sup>k</sup>. The tree T<sub>k,l</sub> has N_+1 _maximal independent sets. Its unique centre-containing maximal independent set has greedy probability_<tbc>

\(p_c=\frac{1}{N}\sum_{j=0}^k\genfrac(){pt}{2}{k}{j}\frac{1}{l+2j+1},\)

<tbc>_and each particular non-centre maximal independent set containing exactly j of the inner vertices u<sub>i</sub> has probability_

\(q_j=\frac{l+2j}{N(l+2j+1)},\)

_with multiplicity_ \(\genfrac(){pt}{2}{k}{j}\).

_For_ \(k\ge 1\)_, under the tuning l_=2_<sup>k</sup>-k, set A_=2_<sup>k</sup>_+1_, let J_∼Bin(_k,_1/2)_, and put W_=2_J-k. Then_

\(b(T_{k,2^k-k})=\frac{1}{2}\left(\mathbb{E}\frac{W^2}{A^2(A+W)}+\mathbb{E}\frac{|W|}{A(A+W)}\right)>0.\)

_Consequently, with n<sub>k</sub>_=2_<sup>k</sup>+k_+1,

\(b(T_{k,2^k-k})=O\left(\frac{\sqrt{k}}{4^k}\right)=O\left(\frac{\sqrt{logn_k}}{n_k^2}\right)(k\rightarrow\infty).\)

Thus exact flatness of the greedy terminal law is confined to the two trivial trees, while an explicit connected sequence approaches the flat law with the upper bound \(O(\sqrt{logn}/n^2)\) along its vertex counts. We do not prove an all-_n_ upper bound, a matching lower bound, an extremal characterization, or optimality of the mixed-spider family.

The stochastic process itself is classical, as are random-priority and random-sequential- adsorption viewpoints. A targeted literature audit described in section 3 found no checked source containing either theorem 1.1 or the formulas and tuning in theorem 1.2; because such searches cannot certify worldwide priority, we use the deliberately bounded assessment that the contribution-level results are _plausibly new with bounded uncertainty_.

## 2 Model and permutation fibres

Let _G_=(_V,E_) be a finite simple graph and let \(\pi=(v_1,\dots,v_n)\) be an ordering of _V_ . Starting from the empty set, scan _v_<sub>1</sub>_,...,v<sub>n</sub>_ and accept _v<sub>i</sub>_ if it has no accepted neighbour. Denote the output by \(\mathrm{Greedy}(G,\pi)\). Every rejected vertex has an accepted neighbour at the moment it is scanned, so the final set is independent and dominates every vertex outside it; hence it is maximal independent.

For \(I\in\mathcal{M}(G)\) define its _permutation fibre_<tbc>

\(\mathcal{F}_G(I)=\{\pi:\mathrm{Greedy}(G,\pi)=I\},g_G(I)=|\mathcal{F}_G(I)|.\)

<tbc>Since all |_V_|! orders are equally likely,

\(\mathsf{G}_G(I)=\frac{g_G(I)}{|V|!}.\)

Therefore G_<sub>G</sub>_ is uniform on M(_G_) exactly when _g<sub>G</sub>(I_) is constant over \(I\in\mathcal{M}(G)\).

We shall use a finite order certificate. Write \(u\prec_\pi v\) when _u_ appears before _v_ in \(\pi\).

**Lemma 2.1** (Order certificate)**.** _Let_ \(I\in\mathcal{M}(G)\)_. Then_ \(\mathrm{Greedy}(G,\pi)=I\) _if and only if every_ \(w\notin I\) _has a neighbour_ \(u\in I\) _with_ \(u\prec_\pi w\).

