<tbc>of a window is the _d_-bit prefix of its signature. When the number of stored windows exceeds \(\alpha 2^d\) for an occupancy target \(\alpha\), and unused signature bits remain (_d\<B_), the _entire_ directory doubles: the depth increases to _d_+1 and every entry is rehomed by its next signature bit, available because full signatures are stored. No individual bucket splits on its own and no local depths are kept; a single depth _d_ governs the whole anchor’s directory.

Proposition 4 (Occupancy control). _Splitting whenever the population exceeds_ \(\alpha 2^d\) _keeps mean bucket occupancy at most_ \(\alpha\)_, and within_ \((\alpha/2,\alpha]\) _between splits after the initial fill; the total rehoming work amortizes to O_(1) _per insertion until the signature or implementation depth limit is reached (proof in Appendix C)._

Deeper prefixes reduce bucket size but also reduce the probability that two similar windows share a full prefix. The query side compensates by multi-probing [22]. A query inspects its exact prefix bucket and then buckets at Hamming distance one, in increasing order of the projection margin \(|\langle g_{a,t},F_{q,a}\rangle|\). A small margin indicates a bit that was close to the decision boundary, so the corresponding one- bit variants are the most probable alternative buckets. The number of Hamming-1 probes grows with depth as 1+max(0_,d-d_<sub>0</sub>), for a reference depth _d_<sub>0</sub>, capped by the depth and an implementation limit. Candidates from the probed buckets are deduplicated, filtered by the exclusion rule, and inspected up to the budget \(R=\gamma\alpha\), a fixed multiple \(\gamma\) of the occupancy target \(\alpha\). The target \(\alpha\) is the only parameter exposed to the analyst. When a probed bucket contains more entries than the remaining budget, half of that budget inspects the most recent entries and the other half inspects entries at even intervals across the whole bucket. This avoids bias toward recent arrivals.

Let _Q<sub>a</sub>(q_) denote the candidates retained for query start _q_, with \(|Q_a(q)|\le R\). The streaming pass evaluates exactly the pairs

\(\mathcal{S}_\mathrm{stream}=\{(a,\langle i,q\rangle):i\in Q_a(q),\underline{\mathrm{d}_{K,a}}(i,q)<\mathrm{max}(\hat{P}_a[i],\hat{P}_a[q])\}.\)

Each computed distance updates both cells, \(\hat{P}_a[i]\) and \(\hat{P}_a[q]\). A cell and its neighbor index are overwritten whenever the new distance is smaller.

## 3.5 Batched Online Updates

Batching lets Panache run on any number of threads without changing its output. A batch is a group of \(\beta\le excl\) consecutive arriving samples processed together. At a fixed length, the windows completed by one batch have consecutive start positions, all closer than _excl_, so no two of them can form a valid pair. Windows of the same batch therefore never search each other. The batch is published in full before any of its searches begins. The only windows a search sees early are its own batch-mates, every one of them invalid by the exclusion rule, and skipping an invalid candidate costs none of the verification budget.

A batch runs in three phases. Phase A advances the running state of §3.2 for all anchors in parallel and inserts the completed windows into the directories. Each anchor owns its moments, coefficients, and directory, so the threads share nothing. Phase B searches in parallel, one work unit per completed window. Each unit probes its directory (§3.4), rejects candidates with the bound, computes exact distances for the survivors, and stores the cell improvements in a private buffer. Phase C merges the buffers into the profile in a fixed order of anchor and buffer index, so equal distances resolve<tbc>

<tbc>to the same neighbor on every run. No batch pair is valid, no state is shared, and the merge order is fixed. Nothing in the schedule can therefore change a result, and a window is searched at most \(\beta-1\) samples after it completes.

Proposition 5 (Determinism). _For a fixed input stream, configuration, and seed, the profiles and motifs emitted by Panache are identical for every thread count and schedule (proof in Appendix C)._

## 3.6 Emit-Time Completion

After the streaming pass and before the motifs are reported, the emit stage runs once to close the two gaps the budgeted pass left. A bucket holding more entries than the budget _R_ was never scanned in full. The anchor stride left the lengths between anchors without any online comparison. Emit closes the first gap with a hot-class sieve and the second with local completion, both through exact comparisons only.

_Hot classes_ (S<sub>hot</sub>). In motif discovery, common patterns repeat, such as repeated heartbeats. Panache piles similar windows of the same length into the same bucket, so the bucket spills past the verification budget, and because these windows share the same signature on every bit, no prefix split can separate them. Somewhere in that bucket may sit a motif that went unexamined, since every arriving window scanned at most _R_ of the bucket’s entries during the stream. A hot class is a bucket that remains larger than the verification budget after every usable prefix split. To find the unexamined motifs, the _r_ spilled members of the hot class are considered. Each member’s normalized spectral state is projected onto one seeded Gaussian direction _g_, the inner product \(g\cdot F_x\) collapsing every member _x_ to one scalar, and the hot class is sorted by it. Every pair of members that sits within _w_ positions of each other in this sorted line-up then receives a full exact z-normalized distance evaluation:

\(\mathcal{S}_\mathrm{hot}(C)=\{(a,\langle\pi(u),\pi(v)\rangle):0<|u-v|\le w,|\pi(u)-\pi(v)|\ge excl\},\)

where \(\pi\) is the sorted order of the hot class _C_. The cost per class is _O(r_log_r+rwm_) rather than _O(r_<sup>2</sup>_m_), and profile cells are lowered only through exact distances.

Lemma 3 (Sieve adjacency). _Let_ (_u,v_) _be the closest pair of a class C at feature distance_ \(\delta\)_, and let_ \(r_x=\mathrm{min}(\|x-u\|,\|x-v\|)\) _for other members x. Under a Gaussian projection, the expected number of members landing between u and v in sorted order is at most_ \(\frac{\delta}{2}\sum_x1/r_x\)_, and the probability that the pair is separated by more than w positions is at most this quantity divided by w (proof in Appendix C)._

The lemma bounds how many members can land between the closest pair in the sorted order, so a small width _w_ suffices, and the pair that went unexamined surfaces at its exact distance in the final top-_k_ selection.

_Local completion_ (S<sub>local</sub>). To evaluate the non-anchor lengths, local completion uses seeds. Each round takes as seeds the _M_ current best motif candidates of the induced profile stack. A seed has a length _m_<sub>0</sub>, a start _i_<sub>0</sub>, and a stored neighbor _j_<sub>0</sub>. Re-cutting this pair at nearby lengths and starts usually keeps it close (§3.3). In one round, Panache computes d_<sub>m</sub>(i,j_) exactly for every length _m_ within the radius \(\Delta_m\) of _m_<sub>0</sub> and all starts _i_ and _j_ within \(\Delta_p\) of _i_<sub>0</sub> and _j_<sub>0</sub>. These are the admissible triples<tbc>

\(\{(m,i,j):|m-m_0|\le\Delta_m,|i-i_0|\le\Delta_p,|j-j_0|\le\Delta_p,|i-j|\ge excl\},\)

