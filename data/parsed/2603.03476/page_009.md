• **Rank diff max**: Maximum rank jump,<tbc>

<tbc>\(max\{|r_{i+1}-r_i|\text{for}1\le i\le n-1\},\)<tbc>

<tbc>capturing the most abrupt change in relative ordering.<tbc>

• **Rank correlation**: Spearman correlation coefficient between motif ranks and their temporal positions,<tbc>

<tbc>\(\rho_s=1-\frac{6\sum(r_i-i)^2}{n(n^2-1)}.\)<tbc>

<tbc>High positive correlation indicates a strong monotonic increase; high negative correlation indicates a monotonic decrease.<tbc>

• **Rank turning points**: Number of indices \(2\le i\le n-1\) at which the direction of rank change reverses, i.e.,<tbc>

<tbc>\((r_i-r_{i-1})(r_{i+1}-r_i)<0.\)<tbc>

<tbc>This feature quantifies oscillatory structure in the motif by counting local reversals in the rank trend. Monotonic motifs have zero turning points, unimodal motifs have a single turning point, while motifs with repeated rises and falls exhibit higher values.

Together, the OPM-derived features enabled a comprehensive characterization of EEG temporal dynamics across multiple scales. **gradient features** quantify local temporal dynamics and signal volatility; and **rank-based features** provide scale- invariant measures of ordinal structure. This multi-faceted approach allowed us to characterize not only what patterns appear in the EEG signals, but how they evolve, how consistently they occur, and how their structure differs between experimental groups, hence providing a rich feature space for subsequent classification and group discrimination.

## CTM Motif Tree Structural Features

A Cartesian tree structure maps the hierarchical relationships among local minima and maxima within a segment, where the root of the tree represents the global minimum of the segment, and subsequent branches recursively represent sub-segments. This representation captures the waveform’s intrinsic hierarchical organization and shape independent of amplitude scaling, making it particularly robust for comparing patterns across different signal amplitudes or recording conditions. The following features characterize the topological properties of the Cartesian tree representation of the motif, denoted by _CT_:

• **Tree max depth**: Maximum nesting depth of _CT_, defined as<tbc>

<tbc>\(d_\mathrm{max}=\mathrm{max}(\mathrm{depth}(v)),\)<tbc>

<tbc>for all nodes \(v\in CT\). This measures structural complexity, where deeper trees indicate more hierarchical levels of extrema. For example, a simple oscillation like (1,3,2) has depth 2, while a complex nested pattern has greater depth.<tbc>

• **Tree leaves**: Number of leaves in _CT_, denoted by _N_<sub>leaves</sub>. This reflects structural simplicity (few leaves) versus fragmentation (many leaves). A monotonic sequence has a single leaf, while highly oscillatory signals have many.<tbc>

