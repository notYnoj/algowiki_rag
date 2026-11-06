<tbc>pairs to evaluate. A profile cell is updated only with the exact z- normalized distance of a valid pair (§2). Every written cell therefore holds an exact distance to a valid neighbor.

The central representation is the normalized AC spectrum of a window. If _X<sub>k</sub>_ is a Fourier coefficient of a window, subtracting the window mean changes only _X_<sub>0</sub>. Every coefficient with _k\>_0 is unchanged by centering and is divided only by the window standard deviation. The non-DC coefficients can therefore be maintained online by sliding-DFT recurrences. Beyond serving as the streaming state, this vector is the SimHash key \[6\], a locality-sensitive hash (LSH) under which windows of similar normalized shape collide. The same vector gives the Parseval lower bound that rejects most candidate pairs before exact distance computation.

We introduce four mechanisms that make this representation scale with a growing stream. _Anchor lengths_ restrict the online state to a subset of the interval’s lengths, relying on the persistence of motifs across neighboring lengths. Similar windows collide in the same hash bucket, and _occupancy-controlled prefix hashing_ keeps mean bucket occupancy near a fixed target as the series grows, so a constant per-query budget stays effective for all but the densest classes. _Exclusion-zone batching_ parallelizes the stream while leaving the output bit-identical to serial processing at any thread count. A final _emit_ stage materializes the profile with exact comparisons inside oversized buckets and around the discovered motifs.

Our contributions are as follows.

\(\bullet\) A formulation of one-pass PMP motif discovery around a sound upper pan-profile, which guarantees exact distances and valid neighbors for every written cell (§2).<tbc>

\(\bullet\) A normalized AC-spectrum representation whose non-DC coefficients are maintained online and serve simultaneously as the streaming state, the SimHash key, and a Parseval rejection bound (§3.2).<tbc>

\(\bullet\) The mechanisms required at scale: occupancy-controlled global- depth hashing, anchor-length search, deterministic exclusion- zone batching, and emit-time completion (§3.3-3.6).<tbc>

\(\bullet\) An evaluation on ten UCR datasets across 17 exact-ground- truth configurations, with full top-20 recovery, faster runtime than every comparable public CPU and GPU baseline, and per- configuration statistics of the recovered motif values (§4). Every data-dependent parameter is computed by the algorithm itself, and every design constant stayed at its default in every experiment.

## 2 Background and Problem

A time series is a vector _T_=(_t_<sub>0</sub>_,...,t_<sub>_n_-1</sub>). For a window length _m_, write _T<sub>i,m</sub>_=(_t<sub>i</sub>,...,t_<sub>_i+m_-1</sub>), with \(0\le i<n-m+1\), for the subsequence starting at position _i_. Its z-normalized form is \(Z_{i,m}=(T_{i,m}-\mu_{i,m}\mathbf{1})/\sigma_{i,m}\), where constant windows, for which \(\sigma_{i,m}=0\), are ignored. The distance between two subsequences of length _m_ is the Euclidean distance after z-normalization, \(\mathsf{d}_m(i,j)=\|Z_{i,m}-Z_{j,m}\|_2\), equivalently \(\mathsf{d}_m(i,j)^2=2m(1-\rho_m(i,j))\) for their Pearson correlation \(\rho_m(i,j)\). Exact matrix-profile algorithms exploit this identity. The correlation is the raw dot product corrected by the window moments, \(m\rho_m(i,j)=(T_{i,m}\cdot T_{j,m}-m\mu_{i,m}\mu_{j,m})/(\sigma_{i,m}\sigma_{j,m})\). One dot product and the moments \(\mu\), \(\sigma\) of both windows therefore determine the distance in closed form, without re-reading the samples \[33, 40\].<tbc>

<tbc>In this paper, an exact distance is the value d_<sub>m</sub>(i,j_) itself, never an estimate or a bound.

In a self-join, windows whose starts are very close share most of their samples and are not considered motif pairs. A pair is _valid_ when its start positions satisfy \(|i-j|\ge excl\), for a fixed exclusion parameter _excl_ \[7, 16\]. For one length _m_, the matrix profile is the row pair (_P<sub>m</sub>,I<sub>m</sub>_) \[33\],

\(P_m[i]=min_{|i-j|\ge excl}\mathsf{d}_m(i,j),I_m[i]\in argmin_{|i-j|\ge excl}\mathsf{d}_m(i,j).\)

The pan matrix profile (PMP) \[23\] is the stack of these rows over an interval \[_m_<sub>min</sub>_,m_<sub>max</sub>\]. Let _L=m_<sub>max</sub>-_m_<sub>min</sub>+1. A pan-motif is a low cell of this stack together with its nearest-neighbor index. To avoid reporting the same region repeatedly, the top-_k_ list is formed by sorting cells by distance and skipping any cell that lies within _m/_2 of an already accepted cell at the same length.

_The streaming target._ The exact PMP contains \(\sum_m(n-m+1)\) cells, each requiring a nearest-neighbor search among the windows of its own length. Panache maintains a relaxation of this object. A _sound upper pan-profile_ is a stack of rows \((\hat{P}_m,\hat{I}_m)\) satisfying, for every cell, either \(\hat{P}_m[i]=\infty\) or

\(\hat{P}_m[i]=\mathsf{d}_m(i,\hat{I}_m[i])\text{with}|i-\hat{I}_m[i]|\ge excl,\)

and in all cases \(\hat{P}_m[i]\ge P_m[i]\). If \(\hat{P}_m[i]<\infty\), then \(\hat{I}_m[i]\) is a valid neighbor and \(\hat{P}_m[i]\) is its exact distance. Only the nearest-neighbor quantifier is relaxed: if the algorithm evaluates the true nearest- neighbor pair, \(\hat{P}_m[i]\) attains the exact profile value _P<sub>m</sub>_\[_i_\]; otherwise it remains a valid upper bound, witnessed by an exactly evaluated neighbor. A finite value below the exact profile value cannot occur, because every written value is the exact distance of some valid pair, and the exact value is the minimum over all of them.

_Problem statement._ The problem tackled in this paper is to process the samples once, in stream order, over the full length interval. The method must maintain a sound upper pan-profile and emit top-_k_ pan-motifs whose reported distances are exact distances to valid neighbors. It must find, within its single scan, the valid pairs whose exact distances lower the motif cells, without executing the _L_ self-joins that define the exact PMP. Updates at stream time \(\tau\) may use only \(t_0,\dots,t_\tau\). Space linear in _n_ is inherent to the task, since a materialized pan-profile alone has \(\Theta(nL)\) cells. The memory accounting is given in §3.7.

## 3 The Panache Algorithm

Every PMP construction, exact or approximate, is characterized by the set of subsequence pairs whose distances it evaluates. Let \(\mathcal{U}=\{(m,i,j):m_{min}\le m\le m_{max},0\le i<j\le n-m,j-i\ge excl\}\) denote the admissible comparison universe. The exact PMP evaluates all of it, which is what the _L_ self-joins compute. For an evaluated subset \(\mathcal{S}\subseteq\mathcal{U}\), writing \(\langle i,j\rangle=(min\{i,j\},max\{i,j\})\), the profile _induced_ by S is

\(P_m^\mathcal{S}[i]=min_{j:(m,\langle i,j\rangle)\in\mathcal{S}}\mathsf{d}_m(i,j),\)

with the empty minimum equal to \(\infty\) and \(I_m^\mathcal{S}[i]\) a witness of the minimum.

