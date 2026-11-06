**Lemma 3.3** (Multinomial power-sum inequality)**.** _If_ \(T\unknown\sum_{h=1}^sT_h\) _is a splitting into matched sectors sharing leg i and p<sub>i</sub>\>_0_, then_

\(\lambda(T)^{1/p_i}\ge\sum_h\lambda(T_h)^{1/p_i}.\) (14)

_For fully independent summands,_ \(T\unknown\oplus_hT_h\) _gives_ \(\lambda(T)\ge\sum_h\lambda(T_h)\) _directly by additivity._

The counting idea is to sum over all multiplicities. With \(a_h=\lambda(T_h)^{1/p_i}\), applying the character to (13) and using the multinomial theorem gives

\(\left(\sum_ha_h\right)^N\le(N+1)^s2^{1/p_i}\lambda(T)^{N/p_i}.\)

The number of multiplicity tuples is polynomial in _N_, so it disappears when we take _N_-th roots and let \(N\rightarrow\infty\). The full calculation is in Appendix F.

Rank bounds and restrictions give

\(1\le f_{ij}(r,s)\le r+s-1,f_{ij}(r,s)=f_{ji}(s,r),\) (15)

and coordinatewise monotonicity. The equality merely interchanges the two polynomial inputs of the same convolution.

**Lemma 3.4** (Powered concavity and tripling)**.** _For p<sub>i</sub>\>_0_, the sequence_ \(s\mapsto f_{ij}(r,s)^{1/p_i}\) _is concave, and for all integers_ \(r,s\ge 1\),

\(f_{ij}(r,3s+r-1)^{1/p_i}\ge 2f_{ij}(r,s)^{1/p_i}+f_{ik}(r,s)^{1/p_i},\) (16)

_where i,j,k are distinct. For p<sub>j</sub>\>_0_, the sequence_ \(r\mapsto f_{ij}(r,s)^{1/p_j}\) _is also concave._

For example, the two-sector splitting gives

\(2f_{ij}(r,s)^{1/p_i}\ge f_{ij}(r,s+1)^{1/p_i}+f_{ij}(r,s-1)^{1/p_i},\)

which is discrete concavity. The three-sector splitting gives (16); input interchange gives concavity in the other coordinate. Appendix F supplies the proof.

## 4. Rescaling the convolution profiles

We next pass from integer input lengths to real ones, so we can compare convolution shapes at any scale. Replication from Section 2 lets us enlarge both inputs together; the bounds, monotonicity, concavity, and tripling inequalities from the preceding section control the resulting limit. We obtain continuous profiles that retain concavity and tripling and scale linearly when both lengths grow by the same factor.

Applying a character to Lemma 2.2 gives

\(f_{ij}(mr,ms)\ge mf_{ij}(r,s).\) (17)

This makes the rescaled values stable under further replication. For real _r,s\>_0, define

\(g_{ij}(r,s)=lim_{m\rightarrow\infty}\frac{f_{ij}(\lceil mr\rceil,\lceil ms\rceil)}{m},m\in\mathbb{Z}_{>0}.\) (18)

The following lemma justifies this limit and lets us work with real lengths throughout the remaining analysis.

