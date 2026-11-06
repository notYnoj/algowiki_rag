## Motif Gradient Features

These features capture the dynamics of signal transitions, reflecting the rate and variability of change within motifs: Let

\(J_i=|x_{i+1}-x_i|,\)

for \(1\le i\le n-1\), i.e. the difference between adjacent values in the motif _x_.

• **Max jump**: Maximum absolute difference between consecutive points:<tbc>

<tbc>\(max\{J_i|1\le i\le n-1\},\)<tbc>

<tbc>. This captures the most dramatic transition in the motif. For example, in (10,12,20,18), the max jump is |20-12|=8.<tbc>

• **Mean jump**: Average gradient magnitude,<tbc>

<tbc>\(\bar{J}=\frac{1}{n-1}\sum_{i=1}^{n-1}J_i,\)<tbc>

<tbc>representing typical transition steepness.<tbc>

• **Std jump**: Standard deviation of jump magnitudes, defined formally as<tbc>

<tbc>\(\sigma^J=\sqrt{\frac{1}{n-1}\sum_{i=1}^{n-1}(J_i-\bar{J})^2},\)<tbc>

<tbc>measuring variability in the rate of change (smoothness vs. irregularity).<tbc>

• **Normalized jumps**: Jumps scaled by the motif’s amplitude range to enable cross-motif comparison, defined formally as<tbc>

<tbc>\(J_i^\mathrm{norm}=\frac{J_i}{max(x)-min(x)},\)<tbc>

<tbc>for \(1\le i\le n-1\), where<tbc>

<tbc>\(max(x)=max\{x_i|1\le i\le n\},\)<tbc>

<tbc>and<tbc>

<tbc>\(min(x)=min\{x_i|1\le i\le n\}.\)<tbc>

<tbc>This makes features comparable across motifs with different scales.

The same gradient-based features were computed for both OPM and CTM motifs; in the CTM case, these features were extracted directly from the motif before Cartesian tree construction. Next, we analyze the OPM and CTM motifs, considering each motif type independently and applying different analytical procedures.

## OPM Motif Rank Features

These features assess the ordinal structure of motifs, making them robust to amplitude scaling and focusing on relative temporal ordering: Let _r<sub>i</sub>_ define the rank of _x<sub>i</sub>_ within the motif.

• **Rank diff mean**: Mean absolute difference in ranks between consecutive points,<tbc>

<tbc>\(\bar{R}=\frac{1}{n-1}\sum_{i=1}^{n-1}|r_{i+1}-r_i|.\)<tbc>

<tbc>This measures monotonicity, where perfectly monotonic motifs have minimal rank differences. For example, (5,2,8,1) has ranks (3,2,4,1) with rank differences |2-3|=1, |4-2|=2, |1-4|=3, yielding mean =2.0.<tbc>

