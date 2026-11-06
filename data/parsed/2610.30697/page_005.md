the certified lower bound \(\beta(\mathbf{q},\mathbf{x})\le\|\mathbf{q}-\mathbf{x}\|^2\) under finite- precision rounding \[64\]. An in-register predicate compares \(\beta(\mathbf{q},\mathbf{x})\) against the threshold _U_(**q**) of that query, retaining vector **x** only if \(\beta(\mathbf{q},\mathbf{x})\le U(\mathbf{q})\). The vectors of list _L<sub>j</sub>_ satisfying this predicate form the list survivors, depicted as coral dots in Figure 2 (panel 2). Aggregating these survivors over all _n<sub>p</sub>_ probed lists of query **q** produces the complete candidate survivor set:

\(C\leftarrow\big\{\mathbf{x}\in S(\mathbf{q})\big|\beta(\mathbf{q},\mathbf{x})\le U(\mathbf{q})\big\},\) (5)

which is forwarded to Stage 3.

The following proposition establishes that certified screening prunes unpromising vectors with zero false dismissals.

**Proposition 3.3** (Screening Soundness)**.** _Consider the exact top-k nearest neighbors_ \(A_k(\mathbf{q})\subseteq S(\mathbf{q})\) _of query_ **q** _in its probed lists (Eq._ (2)_). If the list-local threshold satisfies_ \(U(\mathbf{q})\ge r_k(\mathbf{q})\)_, then every true neighbor survives the certified screening:_ \(A_k(\mathbf{q})\subseteq C\).

_Proof._ Consider any vector \(\mathbf{x}^*\in A_k(\mathbf{q})\). By definition of the _k_-th distance, \(\|\mathbf{q}-\mathbf{x}^*\|^2\le r_k(\mathbf{q})\). Because the certified lower bound is sound under finite-precision arithmetic, \(\beta(\mathbf{q},\mathbf{x}^*)\le\|\mathbf{q}-\mathbf{x}^*\|^2\). By transitivity and the validity of the threshold, \(\beta(\mathbf{q},\mathbf{x}^*)\le r_k(\mathbf{q})\le U(\mathbf{q})\). Vector **x**<sup>∗</sup> therefore satisfies the screening predicate, so \(\mathbf{x}^*\in C\).

## 3.5 Ordered Bound Verification

In Stage 3, Lychee verifies the survivors of the screening in increasing order of their certified lower bounds \(\beta(\mathbf{q},\mathbf{x})\), computing exact squared distances \(\|\mathbf{q}-\mathbf{x}\|^2\) at full precision. Algorithm 1 summarizes the search of a query across the three stages.

Lines 5 to 10 execute the ordered verification over the survivor set _C_. Verification stops as soon as the next lower bound, raised to 0 since a squared distance is never negative, reaches the current _k_-th exact distance _h<sub>k</sub>_ (Figure 2, panel 3). Every remaining survivor in _C_ then has an exact distance at least as large, so that it can at best tie with the _k_-th neighbor already found. Stopping verification at equality is critical for datasets with duplicate vectors (such as DataComp), in which thousands of candidates share the _k_-th distance of a query and would otherwise all be verified. On the GPU, the verification runs with one warp per query computing exact distances in float64.

**Proposition 3.4.** _Algorithm 1 returns_ min(_k,|S_(**q**)|) _vectors of S_(**q**) _whose squared distances to_ **q** _equal those of A<sub>k</sub>_(**q**).

_Proof._ Consider any \(\mathbf{x}\in A_k(\mathbf{q})\). Its squared distance is at most _r<sub>k</sub>_(**q**), which is at most _U_ by Proposition 3.2. The certified bound satisfies \(\beta(\mathbf{q},\mathbf{x})\le\|\mathbf{q}-\mathbf{x}\|^2\le U\), so that **x** belongs to _C_. The loop over _C_ visits the survivors in increasing order of \(\beta\) and stops at a survivor \(\mathbf{x}'\) only if |_H_|=_k_ and \(max(\beta(\mathbf{q},\mathbf{x}'),0)\) reaches the _k_-th distance in _H_. Every survivor that follows \(\mathbf{x}'\) in the order has a bound at least<tbc>

<tbc>**Algorithm 1** Certified screening of the probed lists of a query.

Require: query q, number of probed lists n<sub>p</sub>, anchor budget b Ensure: A<sub>k</sub>(q), the k nearest vectors of the probed lists<br>
\(J\leftarrow\) the n<sub>p</sub> centers nearest to q; \(S\leftarrow\bigcup_{j\in J}L_j\)<br>
\(\mathcal{A}\leftarrow\) the first b anchors of S in the order of J \(\triangleright\) Def. 3.1<br>
\(U\leftarrow(1+\tau)d_{(k)}(\mathbf{q},\mathcal{A})\triangleright\) Eq. (4)<br>
\(C\leftarrow\{\mathbf{x}\in S:\beta(\mathbf{q},\mathbf{x})\le U\}\triangleright\) certified screening<br>
\(H\leftarrow\emptyset\triangleright\) top k so far; h<sub>k</sub>: its k-th distance<br>
for \(\mathbf{x}\in C\) in increasing order of \(\beta(\mathbf{q},\mathbf{x})\) do<br>
   if |H|=k and \(max(\beta(\mathbf{q},\mathbf{x}),0)\ge h_k\) then break<br>
   end if<br>
   insert x into H with distance \(\|\mathbf{q}-\mathbf{x}\|^2\), keeping the k nearest<br>
end for<br>
return H

\(\beta(\mathbf{q},\mathbf{x}')\)

<tbc>and a nonnegative distance, so that its distance is at least the _k_-th distance in _H_. The distances in _H_ are therefore the _k_ smallest distances over _C_. Since \(A_k(\mathbf{q})\subseteq C\subseteq S(\mathbf{q})\), the _k_ smallest distances over _C_ are those over _S_(**q**), namely the distances of _A<sub>k</sub>_(**q**). \(\square\)

## 3.6 Cost Analysis

Algorithm 1 runs in time _O_(|_S_(**q**)|(_m_+5)+_bD_+|_C_|log|_C_|+_V_(**q**)_D_) per query, where _V_(**q**) counts the survivors verified in Lines 6 to 10. The four terms account for the certified screening on tensor cores, the exact distances of the anchors, the sort of the survivors, and the verification at full precision, compared to _O_(|_S_(**q**)|_D_) for IVF-Flat. The extra space per query is _O(b_+|_C_|).

The memory traffic of Lychee depends on the probed rows primarily through the short lifted rows (2(_m_+5) bytes each). Full-precision 4_D_-byte reads are restricted to the _b_ anchors and _V_(**q**) verified survivors. Against the 4_D|S_(**q**)| bytes read by IVF-Flat, the per-query traffic ratio approaches 2_D/(m_+5) as _n<sub>p</sub>_ grows (e.g., \(3\times\) for DINOv2 at _m_=507). The routed pass of Section 3.4 divides this traffic further, because a probed list streams through the tensor cores once for its whole query group _G<sub>j</sub>_, whereas IVF-Flat reads the list once for every query that probes it. The reuse across the batch therefore accounts for the speedup on 8- bit descriptors, whose lifted rows are longer than the vectors (256 against 128 bytes for SIFT at _m_=123). Device memory per vector is 2(_m_+5)+4_D_ bytes when full vectors reside on the GPU and 2(_m_+5)+4_D/s_ bytes when they reside in pinned host memory, since only the anchors stay on the GPU at full precision. Finally, while CertEx \[64\] screens all _N_ lifted rows of the dataset, Lychee screens only the probed set |_S_(**q**)|≈_n<sub>p</sub>N/P_, scaling down the screening work by _n<sub>p</sub>/P_ (e.g., 9.8% of the lists on SIFT1M and 3.1% on BIGANN-100M at recall 0.999).

