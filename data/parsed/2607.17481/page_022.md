<tbc>the stream pass already found, and with the sieve off the budgeted pass never reaches into this row’s enormous tie class, where 93% of the directory sits in over-budget buckets ( 16), so completion is handed no seed there to expand from. With the sieve on as well, the full configuration finds those seeds and recovers the row completely.

_The dense half._ Dense indexing has no uncovered lengths, so every loss in the dense configurations is an evaluation loss. This lets each mechanism be judged on evaluation losses alone. The bare configuration loses 26, the sieve alone still loses 26, completion alone loses 4, and the two together lose none. The steady count of 26 under the sieve looks like no effect, but it hides a change of composition. An incomplete top-20 profile is full of borderline ties. Any mechanism that lowers one more cell changes which of them survive the cut, so the twenty-six misses become a different twenty-six even though the total holds. The clear signal is the exact- position column. It rises with every mechanism added, from 236 to 268 to 292 to 313 of 340, while the value-tie count falls from 349 to 272 ( 12). Each mechanism trades a coincidental value match for an exact reproduction, an improvement only the position column can show.

_StarLightCurves anatomy._ One row sits behind every residual in this section, and it also explains why recovery and exact positions can disagree. StarLightCurves 64k is dominated by near-identical repeats. Its largest hash class alone covers 21,531 of its 64,000 windows, and 93% of its directory entries sit in over-budget buckets ( 16). The eight entries the partial configurations lose here are all the same near-identical repeat, recurring near positions (4804,33469) at the non-anchor lengths _m_=31, 33, and 35 ( 15), at distances of 0.0023 to 0.0026. Each sits inside a tie set far larger than twenty. When so many pairs tie at the same tiny distance, the top-20 list is not unique, and two exact algorithms would themselves disagree on which members to report. This makes the row a test of what the two recovery columns mean. The bare dense configuration scores 18 of 20 here yet matches zero exact positions: the score comes entirely from tie values landing in range. Both full configurations score 20 of 20, with all 20 positions exact. Recovery alone cannot separate a lucky tie-value match from an exact reproduction. The exact-position column can, which is why every table in this appendix reports both.

The factorial closes with a complete attribution. Every loss in the six partial configurations belongs to a mechanism. The 127 non- anchor losses equal the reference census exactly and vanish the moment completion is enabled. The evaluation losses at indexed lengths lie on the six rows of  16 and vanish once the sieve and completion work together. The two emit mechanisms close disjoint failures: completion closes the coverage gap that anchoring opens (§3.3), and the sieve closes the evaluation gap that the budget opens (§3.6). With both enabled, the full configuration loses nothing under either indexing scheme. Hence, no mechanism is redundant.

## G Recovery of Determine Motifs

Recovery (§4) credits a reference motif to Panache when it is reported by position or by value. This section examines a stronger criterion, _identity_: whether Panache reports the same window<tbc>

<tbc>as the exact baseline rather than a distinct window at an equal distance. The criterion is well defined only for a motif with a _determinate_ nearest neighbor, that is, a single closest window. When a window has one or more exact duplicates, its nearest-neighbor distance is zero and several identical windows are equidistant; the nearest neighbor is then not unique, and two exact algorithms may themselves report different members of the tie (§D).

We therefore measure, for each configuration’s exact reference top-20 (computed by Stumpy or Scamp-GPU, §4), which of its twenty cells have a determinate nearest neighbor. We read each cell’s exact nearest-neighbor distance: a distance above the zero- snap threshold \(\varepsilon_0=10^{-6}\) marks a single closest window and one correct motif to recover, whereas a distance of zero does not. We then compare Panache’s top-20 with the exact top-20 on the determinate cells, window for window. Of the 740 reference motifs, 320 have a determinate nearest neighbor; the other 420 are distance- zero duplicates, almost all in the tiled Wafer scaling rows.

Panache recovers every one of the 320 determinate motifs, and its top-20 agrees with the exact top-20 on all of them: 272 at the identical start position and 48 as equal-distance value matches ( 17). On the shorter series the two lists are identical, window for window, as on FordA, ChlorineConcentration, ECG5000, and TwoLeadECG at 8k, on ItalyPowerDemand, and on StarLightCurves. Counting the distance-zero duplicates, which are all recovered as well, benchmark recovery is 740/740.

\begin{tabular}{ccccc}
Dataset & _n_ & det. (pos+val) & dist-0 & rec. \\
\multicolumn{5}{c}{_Recovery suites - UCR (per-dataset length ranges)_} \\
ECG200 & 8k & 20 (16+4) & 0 & 20 \\
ItalyPowerDemand & 1,600 & 20 (20+0) & 0 & 20 \\
Wafer & 8k & - & 20 & 20 \\
Earthquakes & 8k & - & 20 & 20 \\
StarLightCurves & 8k & 20 (20+0) & 0 & 20 \\
ChlorineConc. & 8k & 20 (20+0) & 0 & 20 \\
TwoLeadECG & 8k & 20 (20+0) & 0 & 20 \\
ECG5000 & 8k & 20 (20+0) & 0 & 20 \\
FordA & 8k & 20 (20+0) & 0 & 20 \\
Mallat & 8k & - & 20 & 20 \\
_Recovery suite - 64k, lengths 30-80_ & & & & \\
ChlorineConc. & 64k & 20 (20+0) & 0 & 20 \\
Earthquakes & 64k & - & 20 & 20 \\
ECG5000 & 64k & 20 (12+8) & 0 & 20 \\
FordA & 64k & 20 (15+5) & 0 & 20 \\
Mallat & 64k & - & 20 & 20 \\
StarLightCurves & 64k & 20 (20+0) & 0 & 20 \\
Wafer & 64k & - & 20 & 20 \\
_Full natural lengths (capped at 1M)_ & & & & \\
ItalyPowerDemand & 1,608 & 20 (20+0) & 0 & 20 \\
ECG200 & 9,600 & 20 (16+4) & 0 & 20 \\
TwoLeadECG & 93,398 & 20 (12+8) & 0 & 20 \\
Wafer & 152k & - & 20 & 20 \\
Earthquakes & 164,864 & - & 20 & 20 \\
ECG5000 & 630k & 20 (8+12) & 0 & 20 \\
ChlorineConc. & 637,440 & - & 20 & 20 \\
FordA & 660k & 20 (13+7) & 0 & 20 \\
StarLightCurves & 1M & - & 20 & 20 \\
Mallat & 1M & - & 20 & 20 \\
_Length scaling - Wafer (tiled beyond 152k), lengths 30-80_ & & & & \\
Wafer (10 rows, 8k-5M) & & - & 200 & 200 \\
**Total** & **320 (272+48)** & **420** & **740** & \\
\end{tabular}

** 17: Same-motif recovery, default configuration. A reference motif has a _determinate_ nearest neighbor when its exact nearest-neighbor distance is nonzero, so its closest window is a single, well-defined window; a distance-zero cell has one or more duplicate windows and no single closest neighbor. det. (pos+val): motifs with a determinate neighbor, of 20, split into position and value matches (all recovered). dist-0: distance-zero cells, of 20. rec.: motifs recovered by position or value, of 20. "-" marks configurations whose reference top-20 is entirely distance-zero duplicates.**

