Participants completed a visual attention task. Images of cartoon characters were presented, and the children were instructed to count the number of characters in each image. The number of characters in the images ranged randomly from 5 to 16, ensuring that the task was engaging and visually accessible to the participants. EEG data collection was performed during the task, with each image displayed following the participant’s response, creating a dynamic and interactive recording session.

The dataset is designed to study brain connectivity, attention mechanisms, and the nonlinear dynamics of EEG signals. It provides a valuable resource for investigating diagnostic methods and computational approaches for ADHD.

## 3 Stringology Tools

A string is a finite sequence of characters defined over a well-specified alphabet. For example, if the alphabet is {_a,b,c_}, then the sequence _cbbacabcc_ is a valid string over this alphabet. Research on algorithms and combinatorics applied to strings is known as _stringology_, a term coined by Zvi Galil in 1985 \[19\].

Stringology provides algorithmic methods for analyzing, manipulating, and discovering patterns in strings. It enables the detection of hidden regularities, simplification of data representations, and the efficient analysis of sequential information. Applications of stringology include information retrieval, computational biology, bioinformatics, natural language processing, cryptography, and signal processing \[20\].

In this study, we employ three stringology-based tools: motif discovery, order preserving matching (OPM), and Cartesian tree matching (CTM).

### 3.1 Motif Discovery

Motifs are recurring or statistically significant substrings within a collection of strings \[16\]. They capture structural or functional regularities and constitute a fundamental concept in stringology.

For example, consider the set of strings

\(S=\{abad,xabaxx,cqxzzababaw,dxxcaba\}.\)

The substring _aba_ occurs in all strings in _S_, and thus forms a motif of the group with a support value of 100%. While the substrings _a_, _b_, _ab_, and _ba_ also occur in all strings, we consider only the maximal substring _aba_, as it subsumes these shorter occurrences. Additionally, the substring _xx_ occurs in four strings, i.e., in the majority<tbc>

\begin{tabular}{ccc}
**Brain Region** & ** Electrodes** & **Channels** \\
Frontal & Fp1, Fp2, F3, F4, F7, F8, Fz & 1, 2, 3, 4, 11, 12, 17 \\
Central & C3, C4, Cz & 5, 6, 18 \\
Temporal & T7, T8 & 13, 14 \\
Parietal & P3, P4, P7, P8, Pz & 7, 8, 15, 16, 19 \\
Occipital & O1, O2 & 9, 10 \\
Reference & A1, A2 & — \\
\end{tabular}

1: EEG electrode groups and corresponding channel numbers. This configuration provided comprehensive coverage of frontal, central, temporal, parietal, and occipital brain regions.

