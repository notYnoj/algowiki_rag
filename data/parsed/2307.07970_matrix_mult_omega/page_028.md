**Claim 5.5** (Implicit in \[CW90\], see also \[DWZ23\])**.** _For a block triple_ \(X_IY_JZ_K\in\mathcal{T}\) _, and for every_ \(b\in\{0,\dots,M-1\}\),<tbc>

\(Pr\big[h_X(I)=h_Y(J)=h_Z(K)=b\big]=\frac{1}{M^2}.\)

<tbc>_Furthermore, for two different block triples_ \(X_IY_JZ_K,X_IY_{J^\prime} Z_{K^\prime}\in\mathcal{T}\) _that share the same X-block, and for every_ \(b\in\{0,\dots,M-1\}\),

\(Pr\big[h_X(I)=h_Y(J')=h_Z(K')=b\big|h_X(I)=h_Y(J)=h_Z(K)=b\big]=\frac{1}{M}.\)

_This also holds analogously for different block triples that share the same Y-block or Z-block._

**Claim 5.6.** _For every_ \(b\in B\) _and for every level-_\(\ell\) _block triple_ \(X_IY_JZ_K\in\mathcal{T}\) _that is consistent with_ \(\alpha\)_, the probability that X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub> remains in_ T<sub>hash</sub> _conditioned on h<sub>X</sub>(I_)=_h<sub>Y</sub>(J_)=_h<sub>Z</sub>(K_)=_b is_ \(\ge\frac{3}{4}\).

_Proof._ The only way that _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ does not remain in T<sub>hash</sub> conditioned on _h<sub>X</sub>(I_)=_h<sub>Y</sub>(J_)=_h<sub>Z</sub>(K_)=_b_ is when some other block triples that share the same _X_-block or the same _Y_ -block are hashed to the same bucket _b_.

Right before the hashing step, the total number of block triples remaining is \(N_{\alpha_{X,\alpha_Y,\alpha_Z}}\), and the number of _X_-blocks is _N_<sub>BX</sub>. By symmetry, each _X_-block is in the same number of block triples, which is \(\frac{N_{\alpha_{X,\alpha_Y,\alpha_Z}}}{N_\mathrm{BX}}\) . Thus, the total number of block triples that share the same _X_-block as _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is \(\frac{N_{\alpha_{X,\alpha_Y,\alpha_Z}}}{N_\mathrm{BX}}-1\). For each of them, the probability that they are hashed to the same bucket _b_ with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is \(\frac{1}{M}\) by Claim 5.5. Therefore, by union bound, the probability that any of them is hashed to the same bucket with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is at most

\(\frac{N_{\alpha_{X,\alpha_Y,\alpha_Z}}}{M\cdot N_\mathrm{BX}}\le\frac{N_{\alpha_{X,\alpha_Y,\alpha_Z}}}{M_0\cdot N_\mathrm{BX}}\le^{Eq.(7)}\frac{1}{8}.\)

Similarly, the probability that any block triple that shares the same level-\(\ell Y\) -block is mapped to the same bucket as _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is at most \(\frac{1}{8}\). By union bound, the probability that _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ will be zeroed out is \(\le\frac{1}{4}\).

**Claim 5.7.** _The expected number of level-_\(\ell\) _block triples in_ T<sub>hash</sub> _is at least_

\(N_\alpha\cdot M_0^{-1-o(1)}.\)

_Proof._ For every level-\(\ell\) block triple \(X_IY_JZ_K\in\mathcal{T}\) that is consistent with \(\alpha\), and for every \(b\in B\), the probability that _h<sub>X</sub>(I_)=_h<sub>Y</sub>(J_)=_h<sub>Z</sub>(K_)=_b_ is \(\frac{1}{M^2}\) by Claim 5.5. Also, by Claim 5.6, _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ will remain in T<sub>hash</sub> with probability \(\ge\frac{3}{4}\cdot\frac{1}{M^2}\).

Summing over all block triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ and all \(b\in B\), we get that the expected number of block triples in T<sub>hash</sub> is at least

\(N_\alpha\cdot|B|\cdot\frac{3}{4}\cdot\frac{1}{M^2}=N_\alpha\cdot M_0^{-1-o(1)}.\)

## 5.3 Compatibility Zero-Out I

Recall that \(\{\beta_{X,i,j,k},\beta_{Y,i,j,k},\beta_{Z,i,j,k}\}_{i+j+k=2^\ell}\) are level-\(\ell\) complete split distributions for the _X_-, _Y_ -, _Z_- blocks.

Let<tbc>

\(S_{i,j,k}^{(I,J,K)}:=\{t\in[n]|I_t=i,J_t=j,K_t=k\},\)

