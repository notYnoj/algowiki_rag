## H Recovery of the Rarest Patterns

Motif discovery must surface rare patterns, those that occur only once in a series, as well as common ones that repeat many times. This section is a dedicated study of rare-pattern discovery: we rank every reference motif in the benchmark by how rarely its shape recurs, isolate the rarest, and measure whether Panache discovers them and reports the same patterns as the exact baseline.

We measure rarity directly from the raw series, independently of Panache. Take a determinate reference motif: a window starting at _q_ at length _m_ whose exact nearest-neighbor distance is _d_<sub>1</sub> (§G). We z-normalize every length-_m_ window of the series and compute the z-normalized Euclidean distance from each to the window at _q_, its distance profile. Discarding the trivial matches inside the exclusion zone, we count the windows whose distance is at most 2_d_<sub>1</sub>. A window that close is another near-occurrence of the same shape, so this count is the number of times the pattern occurs, the size of its near-duplicate class. A recurring pattern, a repeated heartbeat say, has a large class; a one-off pattern has an empty one but for its single partner. We call a motif _isolated_ when the count is exactly one: the pattern occurs once, as a pair that matches each other and no third window. To order the isolated motifs by how distinct they are, we use the gap _d_<sub>2</sub>_/d_<sub>1</sub>, the ratio of the second-smallest to the smallest distance in the profile; _d_<sub>1</sub> is the matched pair and _d_<sub>2</sub> the nearest unrelated window, so a large ratio means the match stands alone and the pattern is sharply distinct. The twenty rarest patterns are the isolated motifs with the largest gap.

Of the 320 determinate reference motifs (§G), 123 are isolated, occurring across six datasets and lengths from 8 to 35. Panache recovers _all_ 123: every isolated motif the exact baseline reports is found, with no miss on any dataset, at any length, or at any stream size ( 18). Rarity does not cost recovery. Whatever a series’ mix of common and one-off patterns, and however few or many of its motifs are isolated, each dataset’s recovered count equals its isolated count exactly. Of the 123, 110 are matched at the identical start position and the other 13 as equal-distance motifs, the latter only on the two largest streams (FordA 660k, ECG5000 630k), where the budgeted scan returns an equally close neighbor. The twenty rarest patterns of all, those with the largest gap to their second-nearest window, are recovered 20/20 at the identical position ( 19): Panache returns the same one-off motif the exact baseline reports, on series from 1,600 to 660,000 samples. Across the study, no rare pattern the exact baseline reports goes undiscovered.

\begin{tabular}{ccccc}
Dataset & det. & isolated & rec. & exact pos. \\
ItalyPowerDemand & 40 & 10 & 10 & 10 \\
ECG200 & 40 & 0 & 0 & 0 \\
TwoLeadECG & 40 & 17 & 17 & 17 \\
ECG5000 & 60 & 5 & 5 & 3 \\
FordA & 60 & 48 & 48 & 37 \\
ChlorineConc. & 40 & 22 & 22 & 22 \\
StarLightCurves & 40 & 21 & 21 & 21 \\
**Total** & **320** & **123** & **123** & **110** \\
\end{tabular}

\begin{tabular}{cccccc}
Dataset & _n_ & _m_ & _d_<sub>1</sub> & _d_<sub>2</sub>_/d_<sub>1</sub> & match \\
StarLightCurves & 8k & 34 & 0.007 & 8.9 & pos \\
StarLightCurves & 8k & 34 & 0.007 & 8.7 & pos \\
ChlorineConc. & 8k & 30 & 0.136 & 5.0 & pos \\
FordA & 660k & 31 & 0.053 & 5.0 & pos \\
FordA & 660k & 30 & 0.051 & 4.9 & pos \\
FordA & 660k & 31 & 0.053 & 4.8 & pos \\
FordA & 660k & 30 & 0.051 & 4.8 & pos \\
ChlorineConc. & 8k & 30 & 0.136 & 4.8 & pos \\
FordA & 660k & 32 & 0.056 & 4.8 & pos \\
FordA & 660k & 33 & 0.059 & 4.7 & pos \\
FordA & 660k & 32 & 0.056 & 4.6 & pos \\
StarLightCurves & 64k & 30 & 0.002 & 4.6 & pos \\
StarLightCurves & 64k & 30 & 0.002 & 4.5 & pos \\
FordA & 660k & 33 & 0.059 & 4.5 & pos \\
FordA & 8k & 31 & 0.195 & 4.3 & pos \\
ChlorineConc. & 8k & 31 & 0.162 & 4.3 & pos \\
FordA & 8k & 32 & 0.201 & 4.3 & pos \\
FordA & 8k & 32 & 0.201 & 4.2 & pos \\
FordA & 8k & 31 & 0.195 & 4.2 & pos \\
StarLightCurves & 8k & 30 & 0.006 & 4.2 & pos \\
\end{tabular}

** 18: Isolated-pattern recovery by dataset. det.: determinate motifs (nonzero-distance nearest neighbor, §G). isolated: those whose near-duplicate class has size one, so the pattern occurs exactly once in the series. rec.: isolated motifs recovered by position or value. exact pos.: recovered at the identical start. Datasets whose determinate motifs are all repeated (ECG200) contribute no isolated patterns.**

** 19: The twenty rarest patterns in the benchmark, ranked by the gap** _d_<sub>2</sub>_/d_<sub>1</sub> **between the motif distance** _d_<sub>1</sub> **and the distance to the second-nearest window (larger is more isolated). match: Panache recovers the pattern at the identical start position (pos) or as an equal-distance motif (val). All twenty are recovered at the identical position, across series from 1,600 to 660,000 samples.**

