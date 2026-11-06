<tbc>graphs<sup>1</sup>. Each graph _X<sub>i,j</sub>(V<sub>i</sub>,V<sub>j</sub>,L<sub>i,j</sub>_) is defined by two sets of vertices _V<sub>i</sub>_ and _V<sub>j</sub>_ and a set of edges (or links) _L<sub>i,j</sub>_, such that for every link \(l(a,b)\in L_{i,j}\), \(a\in V_i\) and \(b\in V_j\), where _V<sub>i</sub>_ (_V<sub>j</sub>_) is the vertex set of graph _G<sub>i</sub>_ (_G<sub>j</sub>_). Some of _X<sub>i,j</sub>_ can be empty. For HoMLNs, inter-layer graphs are implicit as nodes in layers form a common subset having same identity.<br>
**Problem Addressed:** Given a homogeneous MLN (HoMLN) with _l_ number of layers - _G_<sub>1</sub> (_V, E_<sub>1</sub>), _G_<sub>2</sub> (_V, E_<sub>2</sub>), ..., _G<sub>l</sub>_ (_V, El_), where _V_ and _E<sub>i</sub>_ are the vertex and edge set in the _i<sup>th</sup>_ layer - the goal is to discover _interesting substructures_ of the HoMLN for any _r_ layers **correctly and efficiently** using the decoupling approach. For correctness, _r_ HoMLN layers under consideration are conflated into a simple graph using the Boolean OR operator, and substructures discovered on that simple graph are used as the Ground Truth (GT).<br>
**Why Map/Reduce?:** We have used the Map/Reduce paradigm as an example of the distributed and parallel processing approach. Without loss of generality, any other paradigm (e.g., Spark, Pregel) can be used in its stead without the need to modify the algorithms presented in this paper. Implementation will change slightly based on the choice of the framework.<br>
_Contributions of this paper are:_

\(\bullet\) **Map/Reduce Algorithm** for substructure discovery in a layer.<tbc>

\(\bullet\) **Map/Reduce Composition algorithm** to correctly generate substructures spanning Homogeneous layers.<tbc>

\(\bullet\) Map/Reduce **Partitioned approach** to layer graph processing.<tbc>

\(\bullet\) **Correctness proof** of both independent expansion and the composition algorithm (Ho-ICA).<tbc>

\(\bullet\) Extensive experimental analysis on a large number of **synthetic and real-world** graphs.<tbc>

\(\bullet\) **Accuracy** with ground truth, response time, and speedup comparisons.

**Roadmap:** MLN analysis alternatives are briefly discussed in Section II to highlight our choice. Section III has related work. Preliminaries and terminology are outlined in Section IV. Section V details the substructure and composition algorithm and Map/Reduce implementation of the proposed substructure discovery. Correctness of algorithms is proved in Section VI. Detailed experimental evaluation is given in Section VIII. Section IX has conclusions.

## II. MLN ANALYSIS ALTERNATIVES AND CHALLENGES

Figure 2 shows three alternatives to perform analysis on MLNs. Figure 2(a) shows the traditional approach, where a MLN is conflated into a simple graph using type- independent [5] or projection-based [6] approaches. As both ignore type information for the transformation, they do not support the structure and semantic preservation of MLNs. Moreover, as observed in the literature, _without additional mappings_, these approaches are likely to result in some information loss and distortion of properties [7], or hide the<tbc>

<tbc>effect of different entity types and/or different intra- or inter- layer relationships [8]. At the other end of the spectrum, Figure 2(c) shows computing the result by traversing the whole MLN as a single graph. Although this has been implemented for community detection (e.g., Infomap recently, [9]), this is likely to be computationally expensive and not flexible as the number of layers and data sizes become large and new MLN algorithms need to be developed for each analysis.

Figure 2(b), on the other hand, shows an approach (termed **network decoupling**) where the analysis metric for each layer is computed independently (possibly in parallel) during the analysis (\(\Psi\)) phase **only once** and results composed using a binary operator \(\Theta\) as shown in [10]-[14]. Other layer or inter-layer information is **not used** while processing a layer! This approach has been shown to be effective for Boolean operations without aggregating and losing type information. Furthermore, it has been shown to be more efficient than the approaches shown in Figure 2(a) or Figure 2(c).

The challenges in developing a substructure discovery algorithm are: _i) enumerating all connected subgraphs of any size in a given graph or forest (completeness), ii) identifying duplicates, if any, and remove them (soundness), iii) counting isomorphic substructures to apply the metric for each distinct substructure and ranking them, and iv) retaining top-beam substructures for the next iteration._ The enumeration is typically done by iteratively increasing the connected subgraph size by 1. Evaluation of each substructure with the desired metric (Frequency or Minimum Description Length) is carried out after each iteration. To contain the search space, a heuristic is applied to carry top-_beam_ (_beam_ is a parameter) results from each iteration. Current algorithms do this on a simple graph or forest. **How the decoupling approach has been adapted to the HoMLN substructure discovery is the focus of this paper and is elaborated in Section V.**

## III. RELATED WORK

SUBDUE was the earliest main memory algorithm [15] developed for substructure discovery. It can perform both supervised and unsupervised substructure discovery. It uses an iterative algorithm to systematically generate larger substructures which are evaluated using Minimum Description Length (MDL [16]). SUBDUE uses the notion of a _beam_ to restrict the number of substructures carried to the next iteration.

<sup>1</sup>The number of bipartite graphs can be less or even more than the number of graphs/layers. That is, _m_ can be _\<_= or even _\> n._

AGGREGATED MLN APPROACH
NETWORK DECOUPLING APPROACH
WHOLE MLN APPROACH
W
(Analysis Function)
(Composition Function)
Partial Results 1
Partial Results 2
Combine Layer 2 Partitions
Partial Results
Combined Results of Layer 1 and 2
Partial 1
Partial Results 3
Partial 2
Multilayer Network
Multilayer Network
Partial Results 3
Multilayer Network
Random Wols based Analysis across the MLN
Partial Results 1
Partial Results 2
Analysis on Aggregated Layer
Final RESULT (Combined Results of Layer 1, 2 and 3)
Final RESULT (No Partial Results)
FINAL RESULT
(a)
(b)
(c)

Fig. 2: Lossy (a), Decoupling (b), and MLN (c) approaches

