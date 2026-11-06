# Stringology-Based Motif Discovery from EEG Signals: an ADHD Case Study

**Abstract**

We propose a novel computational framework for analyzing electroencephalography (EEG) time series using methods from stringology, i.e., the study of algorithmic techniques for efficiently processing and analyzing strings, which enables the systematic identification and characterization of recurrent temporal patterns in neural signals. The goal of this work is to introduce new measures for understanding neural signal dynamics, with the reported findings serving as a proof-of-concept demonstration of the framework. The framework adapts order preserving matching (OPM) and Cartesian tree matching (CTM) to discover temporal motifs that preserve relative ordering and hierarchical relationships while remaining invariant to amplitude scaling, providing a temporally precise representation of EEG dynamics complementary to spectral and global complexity analyses.

To demonstrate its utility, we applied the framework to multichannel EEG recordings from individuals with attention-deficit/hyperactivity disorder (ADHD) and matched controls, a publicly available dataset. Highly recurrent, group-unique motifs (support \(\ge 0.9\)) were identified and quantified using OPM and CTM. ADHD participants showed significantly higher motif frequencies, indicating increased repetitiveness in neural activity. OPM analysis revealed shorter motif lengths and greater gradient instability for the ADHD group, reflected in larger mean and maximal inter- sample amplitude jumps. CTM analysis corroborated these findings and further revealed reduced hierarchical complexity in ADHD, characterized by shallower tree structures and fewer hierarchical levels, despite comparable motif lengths.

These results indicate that ADHD-related EEG alterations manifest as systematic differences in the structure, stability, and hierarchical organization of recurrent temporal patterns, extending beyond spectral or global complexity measures. The proposed stringology-inspired motif framework provides a complementary computational tool for EEG analysis, with potential applications in objective biomarker development and monitoring of neurodevelopmental disorders.

<sup>∗</sup>Corresponding author: samahi@braude.ac.il

Anat Dahan, Samah Ghazawi<sup>∗</sup>

Braude College of Engineering, Karmiel, Israel

