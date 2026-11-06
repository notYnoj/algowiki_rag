<tbc>where _n_ is the number of vertices (i.e., |_V_<sup>∗</sup>|). Basic concepts regarding persistent spectral graphs are described in Supporting Information S1.1 and S1.2.

#### 2.2.2 Dual-RAG-IF design setup

We use the Dual-RAG-IF package [18,19,23] to find RNA sequences that fold onto a target 2D fold described as a dual graph. The initial RAG-IF program is based on a genetic algorithm to mutate an initial sequence, determine its 2D folding at each step, and then generate collectively a large number of sequences that fold on the desired motif, which are then sorted by minimal mutations from the starting sequence. More details are available in [23]. Dual-RAG-IF has successfully applied to find structure-altering mutations for the SARS-CoV-2 frameshifting element [18,19].

There are three key steps in Dual-RAG-IF: **1) Mutation region identification**: Mutation regions can be determined either manually or automatically. For manual design, the input must include a target 2D structure in dot-bracket notation defining with the target dual graph, along with a sequence that marks mutation regions by representing residues as ‘N’. For automatic design, we only need the target dual graph information, and the entire sequence is taken as the mutation region. 2) **Candidate sequence generation**: Candidate sequences with mutations are generated using a genetic algorithm. Each candidate is evaluated by applying two 2D folding programs (such as NUPACK [24], IPknot [25], and PKNOTS [26]) capable of handling pseudoknots to verify the resulting fold, and a sequence is considered successful when both programs agree on the target fold. In our application, we use the NUPACK and IPknot packages. 3) **Sequence optimization**: The candidate sequences are ordered by minimal mutations, ensuring an optimal final design.

## 3 Results

### 3.1 Clustering Analysis

#### 3.1.1 Overview

Our two datasets from 2021 and 2022 contain graph topologies. Graphs corresponding to _existing_ 3D RNA structures are assigned the label of 1. The remaining hypothetical RNA topologies can be either non-RNA<tbc>

