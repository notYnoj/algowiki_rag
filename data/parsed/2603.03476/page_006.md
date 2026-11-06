<tbc>CTM-based motif discovery identifies motifs as recurring substrings whose Cartesian tree representations share the same structural shape. Unlike OPM, CTM allows small variations in local ordering as long as the hierarchical arrangement of minima and maxima is preserved. As a result, CTM motifs capture broader waveform structures rather than exact ordinal patterns.

The relationship between OPM and CTM is hierarchical. Every OPM match induces an identical Cartesian tree and therefore constitutes a CTM match. However, the converse does not necessarily hold: two strings may share the same Cartesian tree structure while differing in their exact ordinal relationships. Consequently, OPM identifies a strict subset of the patterns captured by CTM.

In EEG analysis, stringology-based methods enable the identification of recurrent temporal micro-patterns that reflect underlying neural dynamics. By transforming numerical EEG signals into strings and searching for repeated substrings, it becomes possible to characterize temporal organization, stability, and structural regularities in neural activity. Such properties are particularly relevant in the study of ADHD, which has been associated with increased neural variability and disrupted temporal coordination.

Motif discovery in EEG requires similarity measures that are robust to inter- subject variability and amplitude differences. Methods based on relative ordering or structural shape, rather than absolute values, are therefore well-suited for this domain. In this study, OPM is used to detect highly consistent temporal motifs that preserve exact ordinal relationships between consecutive samples. These motifs correspond to strictly recurring rising and falling trends in EEG signals. In addition, CTM is employed to identify motifs that preserve the overall waveform shape while allowing minor ordinal variations. This flexibility enables the detection of broader recurrent neural patterns that may vary slightly in local ordering but retain their essential structural characteristics.

Together, OPM and CTM provide complementary perspectives on EEG dynamics. Their combined use enables a nuanced comparison between the ADHD and control groups by capturing both highly stable ordinal motifs and more flexible structural waveform patterns. The following section describes how OPM- and CTM-based motifs are systematically extracted and quantified from EEG recordings to identify group- specific neural signatures.

1
0
3
2
4

Figure 1: The Cartesian trees of (7,2,16,4,8) and (10,5,17,9,18) are identical, illustrating a Cartesian Tree Matching (CTM) instance. In both cases, the tree nodes are labeled by the positions of the corresponding values in the string, starting from position 0. More generally, any string of length 5 in which the minimum value occurs at position 1 and the second minimum occurs at position 3 will produce the same Cartesian tree structure, regardless of the order relations between the values at positions 0, 2, and 4.

