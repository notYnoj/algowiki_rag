**Claim 6.6** (Implicit in \[CW90\], see also \[DWZ23\])**.** _For a level-_\((\ell-1)\) _block triple_ \(X_IY_JZ_K\in\mathcal{T}\)_, and for every_ \(b\in\{0,\dots,M-1\}\),<tbc>

\(Pr\big[h_X(I)=h_Y(J)=h_Z(K)=b\big]=\frac{1}{M^2}.\)

<tbc>_Furthermore, for two different block triples_ \(X_IY_JZ_K,X_IY_{J^\prime} Z_{K^\prime}\in\mathcal{T}\) _that share the same X-block, and for every_ \(b\in\{0,\dots,M-1\}\),

\(Pr\big[h_X(I)=h_Y(J')=h_Z(K')=b\big|h_X(I)=h_Y(J)=h_Z(K)=b\big]=\frac{1}{M}.\)

_This also holds analogously for different block triples that share the same Y-block or Z-block._

**Claim 6.7.** _For every_ \(b\in B\) _and for every level-_\((\ell-1)\) _block triple_ \(X_IY_JZ_K\in\mathcal{T}\) _that is consistent with_ \(\{\alpha_t\}_{t\in[s^\prime]}\)_, the probability that X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub> remains in_ T<sub>hash</sub> _conditioned on h<sub>X</sub>(I_)=_h<sub>Y</sub>(J_)=_h<sub>Z</sub>(K_)=_b is_ \(\ge\frac{3}{4}\).

**Claim 6.8.** _The expected number of level-_\((\ell-1)\) _block triples in_ T<sub>hash</sub> _is at least_ \(N_\alpha\cdot M_0^{-1-o(1)}\).

## 6.3 Compatibility Zero-Out I

Recall that for every \(W\in\{X,Y,Z\}\) and \(i'+j'+k'=2^{\ell-1}\), \(\beta_{W,t,i^\prime,j^\prime,k^\prime}\) is a level-\((\ell-1)\) complete split distribution, and they satisfy<tbc>

\(\beta_{W,t}=\sum_{i^\prime,j^\prime,k^\prime}\alpha_t(i',j',k')\cdot\big(\beta_{W,t,i^\prime,j^\prime,k^\prime}\times\beta_{W,t,i_t-i^\prime,j_t-j^\prime,k_t-k^\prime}\big).\) (20)

<tbc>Let<tbc>

\(S_{t,i^\prime,j^\prime,k^\prime}^{(I,J,K)}:=\{p\text{is in the}t\text{-th term}|I_p=i',J_p=j',K_p=k'\},\)

<tbc>and

\(S_{t,*,*,k^\prime}^{(K)}:=\{p\text{is in the}t\text{-th term}|K_p=k'\},S_{t,*,*,*}:=\{p\text{is in the}t\text{-th term}\}.\)

If clear from the context, we will drop the superscript (_I,J,K_) or (_K_).

Recall that in T<sub>hash</sub>, every level-\((\ell-1)\) block _X<sub>I</sub>_ is in a unique block triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_. For every level-1 block \(X_\hat{I}\in X_I\), we will zero out \(X_\hat{I}\) if \(\text{split}(\hat{I},S_{t,i^\prime,j^\prime,k^\prime})\neq\beta_{X,t,i^\prime,j^\prime,k^\prime}\) for any \(t,i',j',k'\). Similarly, every level-\(\ell\) block _Y<sub>J</sub>_ is in a unique block triple, and we zero out every \(Y_\hat{J}\in Y_J\) where \(\text{split}(\hat{J},S_{t,i^\prime,j^\prime,k^\prime})\neq\beta_{Y,t,i^\prime,j^\prime,k^\prime}\) for any \(t,i',j',k'\).

For every level-1 block \(Z_\hat{K}\in Z_K\), we zero out \(Z_\hat{K}\) if \(\text{split}(\hat{K},S_{t,*,*,k^\prime})\neq\overline{\beta_{Z,t,*,*,k^\prime}}\) for any \(t,k'\), where

\(\overline{\beta_{Z,t,*,*,k^\prime}}:=\frac{\sum_{i^\prime+j^\prime=2^{\ell-1}-k^\prime}\big(\alpha(i',j',k')+\alpha(i_t-i',j_t-j',k_t-k')\big)\cdot\beta_{Z,i^\prime,j^\prime,k^\prime}}{\sum_{i^\prime+j^\prime=2^{\ell-1}-k^\prime}\big(\alpha(i',j',k')+\alpha(i_t-i',j_t-j',k_t-k')\big)}.\)

We call the tensor after the previous zeroing-outs T<sub>comp</sub>.

Next, we define the notion of compatibility.

**Definition 6.9** (Compatibility)**.** For some _I,J,K_, a level-1 block \(Z_\hat{K}\in Z_K\) is compatible with a level-\((\ell-1)\) triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ if

