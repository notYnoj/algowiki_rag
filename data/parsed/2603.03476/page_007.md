## 4 Implementation

Our analysis proceeded through a systematic pipeline designed to discover and characterize meaningful patterns, i.e., motifs, from the EEG data. We began by organizing the dataset hierarchically, examining each experimental group’s recordings independently. Within each channel, we processed the individual sequences through a standardized preprocessing workflow that included high-pass and low-pass filtering to remove artifacts and noise, Independent Component Analysis (ICA) to separate signal sources, and finally, 1-in-4 downsampling was performed to reduce computational complexity while preserving essential frequency information.

Once the signals were preprocessed, we considered each sequence as a string (per group, per participant, and per channel), i.e., each preprocessed EEG channel time series from an individual participant was treated as a separate string. In total, we have \(61\times 19+60\times 19=2299\) strings to consider in the motif discovery phase. For each string, we systematically explored maximal motifs, defined as motifs that are not strictly contained within any longer motif, of varying lengths _\>_5 (motifs of length _\<_5 were excluded, as they were insufficient to capture meaningful temporal structure). At each length scale, we applied two complementary mining approaches as mentioned previously: OPM motifs and CTM motifs. To ensure we captured only robust and frequently occurring motifs, we set a minimum support threshold of 0.9 for both mining methods, meaning that discovered motifs had to appear in at least 90% of the analyzed strings. To ensure group specificity, we retained only motifs that did not appear in the other group. This stringent criterion ensures we identify only robustly recurrent patterns that represent characteristic features of group-level neural dynamics rather than idiosyncratic patterns present in small subsets of individuals. Lower thresholds would increase false discovery of spurious patterns due to individual variability, while higher thresholds for support would overly restrict the analysis to near-universal patterns.

### 4.1 Motif Feature Definitions

We extracted four categories of features from discovered motifs: initial characteristics, gradient dynamics, rank-based ordinal properties, and hierarchical tree structures.

#### Motif Initial Features

For both types, i.e., OPM motifs and CTM motifs, the following initial features were obtained:

• **Length**: Length of the motif string.<tbc>

• **Frequency**: How many times this motif occurs in all strings within the group.<tbc>

• **Support**: The number of strings containing the motif divided by the total number of strings within the group.<tbc>

• **Mean**: The position-wise average amplitude computed across all instances of motifs.

To characterize the temporal dynamics and structural properties of identified OPM and CTM motifs, we consider a comprehensive set of gradient characteristic features. These features capture different aspects of motif behavior, based on their fine-grained temporal evolution, enabling robust discrimination between EEG patterns across groups. Let

\(x=(x_1,\dots,x_n),\)

represent the motif, i.e. _x<sub>i</sub>_ is the amplitude value at position _i_ of the motif _x_.

