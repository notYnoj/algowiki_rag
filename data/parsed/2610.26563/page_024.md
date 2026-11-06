its three factors and put the sign in \(C(\lambda)\). The blocks use the scalings \(\lambda^{a_t},\lambda^{b_t},\lambda^{c_t}\), respectively. Uniform reciprocal scalings of the three factor matrices leave \(\sigma(\Xi(\lambda))\) unchanged, although scaling different columns independently can change it. This distribution agrees with the weighted expansion (96), up to column signs. The part projections are injective for conflict-free families by Lemma 3, and for graded families by Lemma 7.

**Proposition 1** (Spectral norms of the centered factors)**.** _For a set of complete tripartitions with injective part projections and the factors of_ (130)_, the row Gram matrices are block diagonal, with each diagonal block equal to a multiple of the identity matrix. Their spectral norms satisfy_

\(\|A(\lambda)\|_2^2=\mathrm{max}_{1\le t\le m}\lambda^{2a_t}(n+1)^{|U_t|}\left(1+\sum_{P\in\mathcal{Q}P\subseteq U_t}(n+1)^{-|P|/3}\right),\)<br>
\(\|B(\lambda)\|_2^2=\mathrm{max}_{1\le t\le m}\lambda^{2b_t}(n+1)^{|V_t|}\left(1+\sum_{P\in\mathcal{Q}P\subseteq V_t}(n+1)^{-|P|/3}\right),\)<br>
\(\|C(\lambda)\|_2^2=\mathrm{max}_{1\le t\le m}\lambda^{2c_t}(n+1)^{|W_t|}\left(1+\sum_{P\in\mathcal{Q}P\subseteq W_t}(n+1)^{-|P|/3}\right).\) (131)

_Proof._ For \(P=\emptyset\) or \(P\in\mathcal{Q}\) with \(P\subseteq U_t\), the unscaled lifting applies _Q_ in \(U_t^c\) and is constant in _U<sub>t</sub>_\\_P_. In its Gram matrix, each retained coordinate gives _Q<sup>T</sup>Q=I_, while each constant coordinate gives **1**_<sup>T</sup>_**1**=_n_+1. Hence this matrix is (_n_+1)<sup>|_U<sub>t</sub>_|-|_P_|</sup>_I_.

To compute a cross block for distinct _U<sub>t</sub>,U<sub>s</sub>_ with \(P\subseteq U_t\cap U_s\), choose a coordinate in their symmetric difference. Interchanging _s,t_ if necessary, let this coordinate be \(r\in U_t\backslash U_s\). It is not deleted by _P_. The _t_th lifting is constant in that coordinate, whereas the _s_th lifting uses a column of _Q_. The inner product therefore contains the factor

\(\sum_{j_r=0}^n1\cdot Q_{j_rb}=0\text{for every column}b,\) (132)

since the columns of _Q_ have zero sum. Thus every cross block vanishes.

Multiplying each lifting by \((n+1)^{|P|/3}\lambda^{a_t}\) makes its Gram block equal to \((n+1)^{|U_t|-|P|/3}\lambda^{2a_t}I\). The main and correction aggregates occupy disjoint column blocks of \(A(\lambda)\), so their contributions add to give

\(A(\lambda)A(\lambda)^*=\oplus_{t=1}^m\lambda^{2a_t}(n+1)^{|U_t|}\left(1+\sum_{P\in\mathcal{Q}P\subseteq U_t}(n+1)^{-|P|/3}\right)I_{n^{d-|U_t|}}.\) (133)

Taking the largest scalar block coefficient gives the first equality. The same argument gives the other two.

For a balanced tripartition set \(\mathcal{S}\subseteq B_{N,N,N}\), each part has size _N_ and _q=n<sup>N</sup>_. An ungraded, correction- free aggregate has _A_(1)_A_(1)<sup>∗</sup>=_B_(1)_B_(1)<sup>∗</sup>=_C_(1)_C_(1)<sup>∗</sup>=(_n_+1)_<sup>N</sup>I_. The weighted embedding instead has Gram blocks (_n_+1+(_n_+1)<sup>2/3</sup>)_<sup>N</sup>I_, since the weight vector of Definition 11 has squared norm _n_+1+(_n_+1)<sup>2/3</sup>. For any selected correction family, we bound the sum over its correction subsets by the sum over all subsets. For any finite set _E_ and scalar _z_, grouping subsets by their cardinality and applying the binomial theorem gives

\(\sum_{P\subseteq E}z^{|P|}=\sum_{s=0}^{|E|}\genfrac(){pt}{2}{|E|}{s}z^s=(1+z)^{|E|}.\) (134)

The coefficient \(\genfrac(){pt}{2}{|E|}{s}\) counts the subsets of size _s_. Applying (134) with _E=U<sub>t</sub>_, |_U<sub>t</sub>_|=_N_, and _z_=(_n_+1)<sup>-1/3</sup>, and including the main aggregate separately, yields

\(1\le 1+\sum_{P\in\mathcal{Q}P\subseteq U_t}(n+1)^{-|P|/3}\le\sum_{P\subseteq U_t}(n+1)^{-|P|/3}=(1+(n+1)^{-1/3})^N.\) (135)

