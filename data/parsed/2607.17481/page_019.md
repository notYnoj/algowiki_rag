## F Breaking the Algorithm

Appendix E moved every design constant and failed to break recovery. This section removes whole mechanisms instead, and the question it answers is attribution: if a mechanism earns its place, disabling it must lose motifs, the losses must be predictable from what the mechanism does, and restoring it must recover them. One guarantee frames the whole section. Every configuration below is sound by Proposition 1: each reports only exact distances to valid neighbors, so disabling a mechanism can lose a motif but can never fabricate one. The factorial therefore isolates recall, and every loss it records is a motif missed, never a motif corrupted.

Panache discovers motifs through three cooperating mechanisms, anchor indexing (§3.3), the hot-class sieve (§3.6), and local completion (§3.6). The factorial disables each independently. Dense indexing (_s_=1) replaces anchoring and maintains online state at every length. A sieve width of zero turns the sweep off. Completion, normally governed by a run-time rule, is forced fully on or fully off so that every configuration is unambiguous, and the control keeps the published rule. The result is a full \(2\times 2\times 2\) factorial over the three mechanisms, run on all 37 benchmark rows with the setup of Appendix E.

A run can miss a reference motif in exactly two ways, and separating them is what lets us attribute each loss to a mechanism. A _coverage loss_ is a reference motif whose length the run never output at all. Anchoring is the only source of these: it maintains online state at every second length and leaves the lengths in between to completion, so an anchored run with completion off emits nothing at those in-between lengths, and every reference motif that lives<tbc>

<tbc>there is lost before any distance is computed. An _evaluation loss_ is different. The motif’s length was indexed and both its windows entered the directory, but their pair was never compared, because it landed in a hash bucket holding more entries than the per-query budget _R_ could scan. The budget is the only source of these. This pairing is the claim the section tests: completion exists to close coverage losses, the sieve exists to close evaluation losses, so if the attribution is right, removing completion should produce only coverage losses and removing the sieve should expose only evaluation losses.  12 reports all eight configurations with every loss split by the length at which it occurred, and s 13 and 14 give the per-row detail.

The factorial has one headline. Both configurations that keep the full emit stage recover all 740 motifs, on either indexing scheme, and<tbc>

\begin{tabular}{ccccccccc}
Dataset & **_n_** & Control & \multicolumn{3}{c}{Maximum performance} & \multicolumn{3}{c}{Maximum performance, _K_=4} \\
 & & rec (p+v) & t(s) & rec (p+v) & t(s) & \(\times\) & rec (p+v) & t(s) & \(\times\) \\
\multicolumn{9}{c}{_Recovery suites - UCR (per-dataset length ranges)_} \\
ECG200 & 8k & 20 (16+4) & 0.14 & 20 (16+4) & 0.05 & 2.8 & 20 (20+0) & 0.05 & 3.0 \\
ItalyPowerDemand & 1,600 & 20 (20+0) & 0.02 & 20 (19+1) & 0.01 & 2.0 & 20 (19+1) & 0.06 & 0.4 \\
Wafer & 8k & 20 (19+1) & 0.24 & 20 (19+1) & 0.07 & 3.6 & 20 (18+2) & 0.06 & 4.1 \\
Earthquakes & 8k & 20 (20+0) & 0.25 & 20 (20+0) & 0.06 & 3.9 & 20 (20+0) & 0.06 & 4.3 \\
StarLightCurves & 8k & 20 (20+0) & 0.23 & 20 (20+0) & 0.07 & 3.4 & 20 (20+0) & 0.06 & 3.9 \\
ChlorineConc. & 8k & 20 (20+0) & 0.21 & 20 (20+0) & 0.07 & 3.1 & 20 (20+0) & 0.06 & 3.5 \\
TwoLeadECG & 8k & 20 (20+0) & 0.15 & 20 (20+0) & 0.05 & 2.9 & 20 (20+0) & 0.05 & 3.3 \\
ECG5000 & 8k & 20 (20+0) & 0.14 & 20 (17+3) & 0.05 & 2.8 & 20 (7+13) & 0.05 & 3.0 \\
FordA & 8k & 20 (20+0) & 0.22 & 20 (20+0) & 0.06 & 3.4 & 20 (20+0) & 0.06 & 3.6 \\
Mallat & 8k & 20 (15+5) & 0.21 & 20 (15+5) & 0.07 & 2.9 & 20 (15+5) & 0.06 & 3.3 \\
\multicolumn{9}{c}{_Recovery suite - 64k, lengths 30-80_} \\
ChlorineConc. & 64k & 20 (20+0) & 2.26 & 20 (20+0) & 0.58 & 3.9 & 20 (20+0) & 0.48 & 4.7 \\
Earthquakes & 64k & 20 (20+0) & 2.63 & 20 (20+0) & 0.58 & 4.6 & 20 (20+0) & 0.48 & 5.4 \\
ECG5000 & 64k & 20 (12+8) & 2.08 & 20 (10+10) & 0.59 & 3.5 & 20 (4+16) & 0.50 & 4.1 \\
FordA & 64k & 20 (15+5) & 2.00 & 20 (19+1) & 0.53 & 3.8 & 20 (19+1) & 0.46 & 4.4 \\
Mallat & 64k & 20 (17+3) & 4.05 & 20 (17+3) & 0.56 & 7.3 & 20 (17+3) & 0.44 & 9.2 \\
StarLightCurves & 64k & 20 (20+0) & 2.20 & 20 (20+0) & 0.58 & 3.8 & 20 (18+2) & 0.45 & 4.9 \\
Wafer & 64k & 20 (16+4) & 1.99 & 20 (16+4) & 0.71 & 2.8 & 20 (15+5) & 0.45 & 4.4 \\
\multicolumn{9}{c}{_Full natural lengths (capped at 1M)_} \\
ItalyPowerDemand & 1,608 & 20 (20+0) & 0.02 & 20 (19+1) & 0.01 & 2.0 & 20 (19+1) & 0.01 & 2.1 \\
ECG200 & 9,600 & 20 (16+4) & 0.17 & 20 (16+4) & 0.06 & 2.8 & 20 (20+0) & 0.06 & 2.9 \\
TwoLeadECG & 93,398 & 20 (12+8) & 2.31 & 20 (6+14) & 0.67 & 3.5 & 20 (2+18) & 0.59 & 3.9 \\
Wafer & 152k & 20 (0+20) & 5.96 & 20 (0+20) & 1.51 & 4.0 & 20 (0+20) & 1.16 & 5.1 \\
Earthquakes & 164,864 & 20 (19+1) & 7.32 & 20 (20+0) & 1.75 & 4.2 & 20 (20+0) & 1.30 & 5.6 \\
ECG5000 & 630k & 20 (8+12) & 19.9 & 20 (2+18) & 4.88 & 4.1 & 20 (2+18) & 4.04 & 4.9 \\
ChlorineConc. & 637,440 & 20 (3+17) & 31.9 & 20 (3+17) & 7.26 & 4.4 & 20 (3+17) & 5.29 & 6.0 \\
FordA & 660k & 20 (13+7) & 33.8 & 20 (18+2) & 7.14 & 4.7 & 20 (18+2) & 5.70 & 5.9 \\
StarLightCurves & 1M & 20 (1+19) & 53.1 & 20 (1+19) & 10.1 & 5.2 & 20 (0+20) & 7.65 & 6.9 \\
Mallat & 1M & 20 (0+20) & 36.1 & 20 (0+20) & 9.72 & 3.7 & 20 (0+20) & 7.25 & 5.0 \\
\multicolumn{9}{c}{_Length scaling - Wafer (tiled beyond 152k), lengths 30-80_} \\
Wafer & 8k & 20 (17+3) & 0.24 & 20 (17+3) & 0.06 & 3.7 & 20 (17+3) & 0.06 & 4.0 \\
Wafer & 16k & 20 (17+3) & 0.41 & 20 (17+3) & 0.12 & 3.3 & 20 (17+3) & 0.11 & 3.7 \\
Wafer & 32k & 20 (19+1) & 0.92 & 20 (19+1) & 0.27 & 3.4 & 20 (19+1) & 0.24 & 3.9 \\
Wafer & 64k & 20 (10+10) & 1.98 & 20 (10+10) & 0.60 & 3.3 & 20 (10+10) & 0.46 & 4.3 \\
Wafer & 128k & 20 (0+20) & 4.77 & 20 (0+20) & 1.23 & 3.9 & 20 (0+20) & 0.95 & 5.0 \\
Wafer & 256k & 20 (0+20) & 15.0 & 20 (0+20) & 2.41 & 6.2 & 20 (0+20) & 1.76 & 8.5 \\
Wafer & 512k & 20 (0+20) & 30.3 & 20 (0+20) & 4.70 & 6.4 & 20 (0+20) & 3.71 & 8.2 \\
Wafer & 1M & 20 (0+20) & 62.6 & 20 (0+20) & 9.51 & 6.6 & 20 (0+20) & 7.07 & 8.8 \\
Wafer & 2M & 20 (0+20) & 135 & 20 (0+20) & 20.2 & 6.7 & 20 (0+20) & 14.9 & 9.0 \\
Wafer & 5M & 20 (0+20) & 362 & 20 (0+20) & 52.1 & 6.9 & 20 (0+20) & 38.2 & 9.5 \\
\end{tabular}

\begin{tabular}{ccccccccc}
Indexing & Sieve & Compl. & rec & pos & val & \multicolumn{2}{c}{lost at lengths} & time \\
 & & & of 740 & of 340 & & non-anc. & anchor & \(\times\) \\
dense & off & off & 714 & 236 & 349 & - & 26 & 0.90 \\
dense & on & off & 714 & 268 & 313 & - & 26 & 0.91 \\
dense & off & on & 736 & 292 & 288 & - & 4 & 2.32 \\
dense & on & on & 740 & 313 & 272 & - & 0 & 1.92 \\
anchored & off & off & 609 & 186 & 301 & 127 & 4 & 0.48 \\
anchored & on & off & 611 & 209 & 275 & 127 & 2 & 0.49 \\
anchored & off & on & 736 & 292 & 289 & 2 & 2 & 1.22 \\
anchored\* & on & on & 740 & 310 & 275 & 0 & 0 & 1.00 \\
\end{tabular}

** 11: Maximum-performance configurations, complete per-row results against the control. _Maximum performance_: the fastest full-recovery combination (_s_=6, \(\alpha=4\), _P_<sub>max</sub>=1).** _K_=4: the same quartered budget at the more aggressive _s_=8 with the spectral width fixed to _K_=4. \(\times\): per-row runtime ratio against the control.

** 12: The mechanism factorial. Each configuration disables a subset of {anchor indexing, hot-class sieve, local completion}; \* marks the published configuration. Losses are counted against the 740 reference motifs and split by whether the lost motif’s length was indexed (anchor) or not (non- anchor). Dense indexing has no non-anchor lengths. Time is total runtime relative to the control.**

