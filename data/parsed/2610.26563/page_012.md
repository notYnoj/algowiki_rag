_The input and output modes are indexed by S, in increasing order. In index notation,_

\((\mu^{\otimes|S|}(T))_\mathbf{j}=\sum_{\mathbf{a}\in\unknown 0,n-1\unknown^S}T_\mathbf{a}\prod_{r\in S}Q_{j_ra_r},\mathbf{j}\in\unknown 0,n\unknown^S.\) (50)

The tensor centering embedding preserves tensor contraction trilinear forms.

**Lemma 4.** _For any_ \(s,t,v\in\mathbb{Z}_{\ge 0}\)_, let_<tbc>

\(X\in(\mathbb{C}^n)^{\otimes(s+v)},Y\in(\mathbb{C}^n)^{\otimes(v+t)},Z\in(\mathbb{C}^n)^{\otimes(s+t)}.\)

<tbc>_Let_ \(\bar{X}=\mu^{\otimes(s+v)}(X)\), \(\bar{Y}=\mu^{\otimes(v+t)}(Y)\)_, and_ \(\bar{Z}=\mu^{\otimes(s+t)}(Z)\)_. Then_<tbc>

\(\mathcal{T}_n^{s,t,v}(X,Y,Z)=\mathcal{T}_{n+1}^{s,t,v}(\bar{X},\bar{Y},\bar{Z}).\)

<tbc>_Proof._ By Definition 9,

\(\bar{X}=\sum_{\mathbf{k}\in\unknown 0,n-1\unknown^{s+v}}X_\mathbf{k}\prod_{m=0}^{s+v-1}Q_{t_mk_m},\) (51)

and similar for \(\bar{Y}\), \(\bar{Z}\), so

\(\mathcal{T}_{n+1}^{s,t,v}(\bar{X},\bar{Y},\bar{Z})=\sum_{\alpha\beta\mathbf{j}\mathbf{k}}\prod_{m=0}^{s-1}\underbrace{\left(\sum_{\ell=0}^nQ_{\ell\alpha_m}Q_{\ell\beta_m}\right)}_{\delta_{\alpha_m\beta_m}}X_{\alpha\mathbf{k}}Y_{\mathbf{kj}}Z_{\beta\mathbf{j}},\) (52)

where the analogous _Q<sup>T</sup>Q=I<sub>n</sub>_ identities have already been applied over the _j_ and _k_ indices. Applying the remaining identities over the \(\alpha\) and \(\beta\) indices gives the stated equality.

**Lemma 5.** _If a term in a trilinear form satisfies the linear reducibility condition (Definition 4), it vanishes when evaluated on centered tensors. Specifically, if an index f appears in exactly one variable, the term is zero for centered X, Y , and Z._

_Proof._ Assume the index _f_ appears only in the tensor _X_. We can factor the summation over _f_ from the rest of the trilinear form,

\(\sum_{\text{all indices}}(\dots)=\sum_{\text{indices}\backslash\{f\}}\left(\sum_fX_{\dots f\dots}\right)Y_\dots Z_\dots.\) (53)

The inner sum is the marginal sum of _X_ along mode _f_. Since _X_ is a centered tensor, this marginal sum is zero. Therefore, the entire term vanishes.

## 5.4 Padding and Weighting

We now handle the replicated cross terms by an embedding into C<sup>_n_+2</sup>. Beyond centering, this embedding simply pads the tensor with zeros, which are used in the trilinear form to annihilate the replicated terms via a suitable choice of weighting in the trilinear form.

**Definition 10** (Padding)**.** _Define the padding map_ \(\nu:\mathbb{C}^{n+1}\rightarrow\mathbb{C}^{n+2}\) _by_

\(\nu(x)=\left[\begin{array}{ c }
x \\
0
\end{array}\right].\) (54)

_Thus_ \(\nu\circ\mu\) _is the padded centering embedding._

The padded centering embedding becomes interesting when combined with a weighting.

