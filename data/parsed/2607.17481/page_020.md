<tbc>every configuration that loses a motif is missing an emit mechanism. The dense full configuration matches 313 of 340 exact positions against the control’s 310, so anchoring at stride two costs no motif and just three exact positions of 340, inside the tie noise of this study (Appendix E), while running at half the dense runtime. The losses in the remaining six configurations total 300 motif instances, and each one is attributed below to the mechanism whose absence caused it, with the evidence in s 15 and 16.

_Dense pass, no emit stage (no anchoring, no sieve, no completion)._ This configuration turns off all three mechanisms. Because it indexes every length, it has no in-between lengths, so no coverage loss is even possible, and any motif it misses must be an evaluation loss. It recovers 714 of 740, and all 26 misses lie at indexed lengths, as expected. The emitted output shows directly that these are evaluation losses, because it contains pairs worse than the ones that were missed: a motif can only be an evaluation loss if a better pair than anything reported was available but never compared. On TwoLeadECG 93k the eight lost reference motifs at length _m_=21 have z-normalized distances between 0.0448 and 0.0483, yet the smallest distance this configuration reported at any length is 0.0526, so eight pairs closer than everything in its output existed and went uncompared. ECG5000 8k shows the same signature: its two lost motifs at _m_=23 have distance 0.192, inside the 0.182-0.206 range of distances the configuration did report, so their quality was well within what it emitted elsewhere, yet their pairs were never evaluated. What stopped the comparisons is the verification budget.  16 counts, per losing row, the directory buckets whose population exceeded the budget _R_=128: TwoLeadECG 93k has a single bucket of 9,994 windows, and across the six rows between 56% and 93% of all directory entries sit in such over-budget buckets. These are not hashing failures. Near-duplicate windows collide with near- certainty (Prop. 3), so the two windows of each lost motif did reach the same bucket; the budget simply could not scan far enough into it to reach them. This is precisely the failure the hot-class sieve is built to repair.

_Anchored pass, no emit stage (anchoring on, no sieve, no completion)._ Anchoring is on and both emit mechanisms are off, so this configuration should exhibit coverage losses, and it does. It recovers 609 of 740, and the 131 misses split into 127 at non-anchor lengths and 4 at anchor lengths. The 127 are coverage losses, and they are not explained after the fact but predicted before the run. With completion off, the configuration emits only the anchor (even) lengths, so every reference motif at a non-anchor (odd) length is lost by construction. Counting the reference motifs at odd lengths from the ground-truth lists alone, before running anything, gives 127, spread over the 17 of the 37 benchmark rows that carry any reference motif at a non-anchor length (the remaining 20 place their entire top-20 at anchor lengths, so anchoring alone loses nothing on them), and  15 shows this count matching the observed losses row by row and length by length. **The entire non-anchor loss ledger is predicted by the reference lists alone.** The remaining 4 losses fall at anchor lengths, so they are evaluation losses, not coverage losses. All four are tie entries at _m_=34 on StarLightCurves 8k, the row whose largest hash class alone holds 46% of its windows ( 16), and the sieve and completion recover them below.

_Anchored pass with the sieve (anchoring and sieve on, no completion)._ Turning the sieve on should touch only evaluation losses and never coverage losses, because the sieve re-scans crowded buckets at lengths that are already indexed and adds no new length to the output. That is what happens. The non-anchor column of  15 does not move: the 127 coverage losses remain exactly as the census predicts. The change is at the anchor lengths, where recovery rises from 609 to 611 and exact positions from 186 to 209 of 340 as the sieve reaches pairs the budgeted scan had skipped. The dense side isolates this effect further, with no coverage losses to confound it: there the same sieve lifts exact positions from 236 to 268 ( 12). The sieve recovers the four StarLightCurves 8k ties, and the top-20 of StarLightCurves 64k shifts by two tie entries at _m_=32, the tie behavior explained below.

_Anchored pass with completion (anchoring and completion on, no sieve)._ Completion should close the coverage gap, and it nearly does. Recovery jumps from 609 to 736 of 740: completion evaluates the neighborhoods of the motifs the stream pass found, at the skipped lengths around them, which restores 125 of the 127 non-anchor coverage losses and the four StarLightCurves 8k anchor ties. Four losses remain, all on StarLightCurves 64k, two at _m_=34 and two at _m_=35. This is the one row where the two emit mechanisms depend on each other. Completion can only search around a motif<tbc>

\begin{tabular}{cccccc}
Dataset & _n_ & refs & at lengths _m_ & \multicolumn{2}{c}{lost, completion off} \\
 & & & & sieve off & sieve on \\
ChlorineConc. & 64k & 10 & 31, 33 & 10 & 10 \\
ChlorineConc. & 8k & 10 & 31, 33 & 10 & 10 \\
ECG200 & 8k & 8 & 21, 23 & 8 & 8 \\
ECG200 & 9,600 & 8 & 21, 23 & 8 & 8 \\
ECG5000 & 630k & 2 & 21 & 2 & 2 \\
ECG5000 & 64k & 8 & 31 & 8 & 8 \\
ECG5000 & 8k & 7 & 21, 23 & 7 & 7 \\
FordA & 64k & 6 & 31 & 6 & 6 \\
FordA & 660k & 8 & 31, 33 & 8 & 8 \\
FordA & 8k & 6 & 31, 33 & 6 & 6 \\
ItalyPowerDemand & 1,600 & 7 & 9 & 7 & 7 \\
ItalyPowerDemand & 1,608 & 7 & 9 & 7 & 7 \\
Mallat & 8k & 10 & 31 & 10 & 10 \\
StarLightCurves & 64k & 8 & 31, 33, 35 & 8 & 8 \\
StarLightCurves & 8k & 6 & 31, 33, 35 & 6 & 6 \\
TwoLeadECG & 8k & 8 & 21, 23, 25 & 8 & 8 \\
TwoLeadECG & 93,398 & 8 & 21 & 8 & 8 \\
Total & & 127 & & 127 & 127 \\
\end{tabular}

\begin{tabular}{cccccc}
Dataset & _n_ & hot & largest class & dir. share & sweep \\
 & & buckets & (% windows) & (%) & updates \\
ECG5000 & 8k & 258 & 1,490 (19) & 56 & 9,479 \\
StarLightCurves & 8k & 290 & 3,695 (46) & 82 & 82,329 \\
TwoLeadECG & 93,398 & 1517 & 9,994 (11) & 89 & 358,587 \\
ECG5000 & 630k & 9878 & 67,806 (11) & 81 & 1,170,444 \\
FordA & 660k & 21502 & 31,489 (5) & 68 & 1,911,441 \\
StarLightCurves & 64k & 1043 & 21,531 (34) & 93 & 933,207 \\
\end{tabular}

** 15: Census of reference motifs at non-anchor lengths against the observed losses of the two anchored configurations without completion. refs counts the reference motifs at odd lengths per row; the two loss columns count the reference motifs lost at those lengths with the sieve off and on.**

** 16: Hot-class census of the six rows that lose motifs at indexed lengths, measured by the control run’s own counters. hot buckets counts directory buckets whose population exceeded the verification budget** _R_=128**; dir. share is the fraction of all directory entries inside such buckets; sweep updates counts the profile cells the hot-class sieve improved on that row.**

