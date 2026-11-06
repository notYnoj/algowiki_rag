## 3.1 Polynomial multiplication tensors

We will define the polynomial multiplication tensors and show that, over every field, P_<sub>a,b</sub>_ has border rank at most _a+b_-1 and P_<sub>n,n</sub>_ degenerates to \(\langle n\rangle\).

**Definition 3.1.** For integers \(a,b\ge 1\), the _polynomial multiplication tensor_ is<tbc>

\(\mathsf{P}_{a,b}:=\sum_{i=1}^a\sum_{j=1}^be_i\otimes e_j\otimes e_{i+j-1}\in\mathbb{F}^a\otimes\mathbb{F}^b\otimes\mathbb{F}^{a+b-1}.\)

<tbc>The tensor P_<sub>a,b</sub>_ corresponds to the multiplication of a polynomial of degree at most _a_-1 by a polynomial of degree at most _b_-1: if _e<sub>i</sub>_ stands for the monomial _t_<sup>_i_-1</sup> in an indeterminate _t_, then the term \(e_i\otimes e_j\otimes e_{i+j-1}\) of P_<sub>a,b</sub>_ records the product _t_<sup>_i_-1</sup>_t_<sup>_j_-1</sup>=_t_<sup>_i+j_-2</sup>. For an integer \(d\ge 0\), let \(\mathbb{F}[t]_{\le d}\) be the space of polynomials of degree at most _d_ in _t_. In this way the tensor P_<sub>a,b</sub>_ corresponds to the bilinear multiplication map

\(\mathbb{F}[t]_{\le a-1}\times\mathbb{F}[t]_{\le b-1}\rightarrow\mathbb{F}[t]_{\le a+b-2}:(f,g)\mapstofg.\) (3.1)

For _a_=1, \(\mathsf{P}_{1,b}=\sum_{j=1}^be_1\otimes e_j\otimes e_j\) is isomorphic to \(\langle 1,1,b\rangle=\sum_{k=1}^bE_{11}\otimes E_{1k}\otimes E_{k1}\): it describes the multiplication of a polynomial of degree at most _b_-1 by a constant, which is nothing else than multiplying a vector of length _b_ by a constant.

**Proposition 3.2.** _Let_ \(a,b\ge 1\) _be integers. Then_ \(\mathsf{P}_{a,b}\triangleleft\langle a+b-1\rangle\).

_Proof._ We extend the field by a formal variable _z_ and consider the function field F(_z_). The field F(_z_) is infinite so \(\mathsf{R}_{\mathbb{F}(z)}(\mathsf{P}_{a,b})\le a+b-1\) \[BCS97, Proposition 14.47\], that is, \(\mathsf{P}_{a,b}\le\langle a+b-1\rangle\) as tensors over F(_z_) (Lemma 2.1(ii)). A restriction over F(_z_) is a degeneration over F (Lemma 2.2(iv)), which proves the claim.

**Lemma 3.3** (\[BCS97, Proposition 14.48(1)\])**.** _For every integer_ \(n\ge 1\)_, we have_ \(\langle n\rangle\triangleleft\mathsf{P}_{n,n}\).

_Proof._ If F has at least _n_ elements, the cited proposition gives \(\langle n\rangle\le\mathsf{P}_{n,n}\): for a product _f_ of _n_ distinct linear factors, the multiplication tensor of the algebra \(\mathbb{F}[t]/(f)\cong\mathbb{F}^n\) is \(\langle n\rangle\). Over every field, we apply Lemma 2.6 to _S_=P_<sub>n,n</sub>_, with the weights _w_<sub>1</sub>(_i_)=2(_i_-1)<sup>2</sup>, _w_<sub>2</sub>(_j_)=2(_j_-1)<sup>2</sup> and _w_<sub>3</sub>(_k_)=-(_k_-1)<sup>2</sup>. The term \(e_i\otimes e_j\otimes e_{i+j-1}\) of P_<sub>n,n</sub>_ has weight 2(_i_-1)<sup>2</sup>+2(_j_-1)<sup>2</sup>-(_i+j_-2)<sup>2</sup>=(_i-j_)<sup>2</sup>\(\ge 0\), which is 0 exactly when _i=j_. So \(\mathsf{P}_{n,n}\unknown\sum_{i=1}^ne_i\otimes e_i\otimes e_{2i-1}\). The linear map on the third leg that maps _e_<sub>2_i_-1</sub> to _e<sub>i</sub>_ for every \(i\in[n]\) and the other basis vectors to 0 maps this tensor to \(\langle n\rangle\), so \(\langle n\rangle\triangleleft\mathsf{P}_{n,n}\).

## 3.2 Separating partial direct sums into direct sums

In this subsection we will prove a separation lemma that degenerates any partial direct sum (Section 2.1) to a direct sum, in the presence of a polynomial multiplication tensor factor.

A degeneration on the second and third legs (Section 2.4) can be applied to some of the summands of a partial direct sum, while the other summands stay as they are: if \(T\triangleleft_1S\), then \(T\oplus_1C\triangleleft_1S\oplus_1C\) for every tensor _C_ with the same first leg as _S_ and _T_. If \((I\otimes A_2\otimes A_3)S=\varepsilon^qT+\varepsilon^{q+1}T_1+\cdots+\varepsilon^{q+d}T_d\), then \(I\otimes(A_2\oplus\varepsilon^qI)\otimes(A_3\oplus I)\) maps \(S\oplus_1C\) to \(\varepsilon^q(T\oplus_1C)+\varepsilon^{q+1}T_1+\cdots+\varepsilon^{q+d}T_d\).

**Lemma 3.4.** _Let_ \(T\in U\otimes V\otimes W\) _be a tensor and let_ \(k\ge 1\) _be an integer. Then the partial direct sum_ \(T\oplus_1\cdots\oplus_1T\) _of k copies of T is isomorphic to_ \(T\otimes\langle 1,1,k\rangle\).

_Proof._ We have \(\langle 1,1,k\rangle=\sum_{\ell=1}^kE_{11}\otimes E_{1\ell}\otimes E_{\ell 1}\). So \(T\otimes\langle 1,1,k\rangle\) is a partial direct sum of _k_ copies of _T_, the \(\ell\)th in \((U\otimes\mathbb{F}^{1\times 1})\otimes(V\otimes\mathbb{F}E_{1\ell})\otimes(W\otimes\mathbb{F}E_{\ell 1})\).

