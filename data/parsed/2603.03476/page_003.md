<tbc>ogy, i.e., the study of algorithmic techniques for efficiently processing and analyzing strings. Specifically, order preserving matching (OPM) [14] and Cartesian tree matching (CTM) [15] frameworks are used to analyze EEG dynamics in ADHD. These pattern matching approaches preserve the relative ordering and hierarchical structure of EEG time-series segments, respectively, enabling comparisons of temporal patterns independent of amplitude scaling. By applying motif discovery [16], i.e., the identification of highly recurrent temporal patterns, we discover recurring structures in the EEG signal based on OPM and CTM. Comparing these motif characteristics between the ADHD and control groups allows us to examine differences in temporal organization, stability, and structural complexity that may reflect dysregulation in attentional and executive control networks. Specifically, this study seeks to:

(1) Identify motif-based features that distinguish EEG dynamics in ADHD from those in typical EEG.<tbc>

(2) Examine how these motifs relate to known measures of temporal stability and complexity.<tbc>

(3) Establish motif-based analysis as a complementary framework to conventional spectral and nonlinear methods for understanding the temporal architecture of ADHD brain activity.

Importantly, the primary goal of this work is to introduce new measures for understanding neural signal dynamics, with the reported findings serving as a proof-of- concept demonstration of the framework’s analytical potential rather than as definitive clinical conclusions.

The paper is organized as follows: first, we describe the dataset collected during an experimental task in Section 2. Second, we define the analytic tools, i.e., OPM and CTM, in Section 3. This is followed by a detailed implementation of preprocessing and analysis steps in Section 4. Next, we present the results in Section 5. The final sections, i.e., Sections 6 and 7, focus on discussion and conclusions, respectively.

## 2 Dataset

The dataset<sup>1</sup> consists of EEG recordings from 121 children (boys and girls) aged 7-12 years, divided into two groups, ADHD and control [17]. The ADHD group includes 61 children diagnosed according to the DSM-IV criteria [18], all of whom had been under Ritalin treatment for up to six months before the EEG recording. The control group consists of 60 typically developing children with no reported history of psychiatric disorders, epilepsy, or high-risk behaviors.

EEG signals were acquired using a 19-channel system (see  1) arranged according to the standard 10-20 electrode placement scheme, with reference electrodes (A1 and A2) positioned on the earlobes. The recordings were sampled at 128Hz, and the duration of each EEG session varied according to the child’s response time during the experimental tasks. Before analysis, the EEG signals were preprocessed to reduce noise and remove artifacts.

<sup>1</sup>The dataset is available at https://dx.doi.org/10.21227/rzfh-zn36

