# On Finding All Connected Maximum-Sized Common Subgraphs in Multiple Labeled Graphs

Johannes B.S. Petersen<sup>2,1</sup>, Akbar Davoodi<sup>1⋆</sup>, Thomas Gärtner<sup>2</sup>, Marc Hellmuth<sup>3</sup>, and Daniel Merkle<sup>4,1</sup>

<sup>1</sup> Department of Mathematics and Computer Science, University of Southern Denmark, Odense, Denmark

<sup>2</sup> Faculty of Informatics, Technical University of Vienna,

<sup>3</sup> Department of Mathematics, Faculty of Science, Stockholm University, Stockholm, Sweden

<sup>4</sup> Algorithmic Cheminformatics Group, Faculty of Technology, Bielefeld University, Germany

**Abstract.** We present an exact algorithm for computing all common subgraphs with the maximum number of vertices across multiple graphs. Our approach is further extended to handle the connected Maximum Common Subgraph (MCS), identifying the largest common subgraph in terms of either vertices or edges across multiple graphs, where edges or vertices may additionally be labeled to account for possible atom types or bond types, a classical labeling used in molecular graphs. Our approach leverages modular product graphs and a modified Bron–Kerbosch algorithm to enumerate maximal cliques, ensuring all intermediate solutions are retained. A pruning heuristic efficiently reduces the modular product size, improving computational feasibility. Additionally, we introduce a graph ordering strategy based on graph-kernel similarity measures to optimize the search process. Our method is particularly relevant for bioinformatics and cheminformatics, where identifying conserved structural motifs in molecular graphs is crucial. Empirical results on molecular datasets demonstrate that our approach is scalable and fast.

**Keywords:** cheminformatics, subgraph isomorphism; graph similarity and graph kernels; modular product; exact algorithms

### 1 Introduction

The maximum common subgraph (MCS) problem stands as a central challenge in numerous domains, including bioinformatics , cheminformatics, pharmacophore mapping, pattern recognition, computer vision, code analysis, compiler design, and model checking [1,2,3,4], to just name a few. Its importance is underscored by applications such as structural alignment in systems biology [5], where large<tbc>

<sup>⋆</sup> corresponding author: akb@sdu.dk

