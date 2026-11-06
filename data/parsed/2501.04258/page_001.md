# How Large is the Universe of RNA-Like Motifs? A Clustering Analysis of RNA Graph Motifs Using Topological Descriptors

Rui Wang <sup>1</sup> and Tamar Schlick<sup>∗</sup> <sup>1,2,3,4</sup>

<sup>1</sup>Simons Center for Computational Physical Chemistry, New York University, New York, NY 10003, USA

<sup>2</sup>Department of Chemistry, New York University, New York, NY 10003, USA

<sup>3</sup>Courant Institute of Mathematical Sciences, New York University, New York, NY 10012, USA

<sup>4</sup>New York University-East China Normal University Center for Computational Chemistry, New York University Shanghai, Shanghai 200122, China

January 9, 2025

**Abstract**

Identifying novel and functional RNA structures remains a significant challenge in RNA motif design and is crucial for developing RNA-based therapeutics. Here we introduce a computational topology- based approach with unsupervised machine-learning algorithms to estimate the database size and content of RNA-like graph topologies. Specifically, we apply graph theory enumeration to generate all 110,667 possible 2D dual graphs for vertex numbers ranging from 2 to 9. Among them, only 0.11% (121 dual graphs) correspond to approximately 200,000 known RNA atomic fragments/substructures (collected in 2021) using the RNA-as-Graphs (RAG) mapping method. The remaining 99.89% of the dual graphs may be RNA-like or non-RNA-like. To determine which dual graphs in the 99.89% hypothetical set are more likely to be associated with RNA structures, we apply computational topology descriptors using the Persistent Spectral Graphs (PSG) method to characterize each graph using 19 PSG-based features and use clustering algorithms that partition all possible dual graphs into two clusters. The cluster with the higher percentage of known dual graphs for RNA is defined as the "RNA-like" cluster, while the other is considered as "non-RNA-like". The distance of each dual graph to the center of the RNA-like cluster represents the likelihood of it belonging to RNA structures. From validation, our PSG-based RNA-like cluster includes 97.3% of the 121 known RNA dual graphs, suggesting good performance. Furthermore, 46.017% of the hypothetical RNAs are predicted to be RNA-like. Among the top 15 graphs identified as high-likelihood candidates for novel RNA motifs, 4 were confirmed from the RNA dataset collected in 2022. Significantly, we observe that all the top 15 RNA-like dual graphs can be separated into multiple subgraphs, whereas the top 15 non-RNA-like dual graphs tend not to have any subgraphs (subgraphs preserve pseudoknots and junctions). Moreover, a significant topological difference between top RNA-like and non-RNA-like graphs is evident when comparing their topological features (e.g. Betti-0 and Betti-1 numbers). These findings provide valuable insights into the size of the RNA motif universe and RNA design strategies, offering a novel framework for predicting RNA graph topologies and guiding the discovery of novel RNA motifs, perhaps anti-viral therapeutics by subgraph assembly.

### Contents

**1 Introduction 1**<tbc>

**2 Methods 2**<tbc>

arXiv:2501.04258v1 [q-bio.BM] 8 Jan 2025

