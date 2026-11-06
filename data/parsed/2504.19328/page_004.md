**Independent Expansion of Substructures:** Substructure discovery uses independent, unconstrained expansion of _k_- edge substructures into (_k_+1)-edge substructures starting from an edge (_k_ = 1 or a 1-edge substructure.) Each expansion of each vertex with an edge becomes a separate substructure. This independent unconstrained expansion ensures the generation of all possible substructures in a principled manner thus ensuring completeness of the substructure generation process. However, this independent expansion results in the generation of duplicate substructure instances, which must be removed to prevent incorrect counting of isomorphic substructures (soundness). Figure 5 shows how independent expansion leads to duplicates. If two substructures have the same set of vertices (with IDs) and edges (labels) and the same connectivity, they are duplicates. To ensure accurate identification of duplicates and differentiate them from isomorphic substructures, we introduce the concept of a canonical instance and canonical substructure<sup>4</sup>.

**Canonical Instance for Duplicate Elimination:** We use lexicographic ordering to convert a substructure instance into its **canonical representation**. First, we order the edges on the edge label. In case edges have the same edge labels, we order them based on the source vertex label. If source vertex labels are also the same, then we further order them based on the destination vertex label. If edge labels and vertex labels are all identical, then we order them based on the source vertex IDs. Finally, if source vertex IDs are also the same, then we order them based on the destination vertex IDs. Using this lexicographic order for **each 1-edge**, a substructure can be uniquely represented, which is called a canonical _k_-edge instance. If two _k_-edge substructure instances are duplicates, they must have the same ordering of their vertex IDs and therefore, will have the same canonical _k_-edge instance. If we convert the duplicates generated in Figure 5 to canonical instances, they will be the same, as shown in Figure 6.

The canonical representation of instances is helpful in identifying and removing duplicate instances. However, counting the frequency of isomorphic substructures requires a canonical form that does not rely on absolute vertex IDs. Therefore, we use a canonical form of the substructure that converts vertex IDs to relative vertex IDs.

**Canonical Substructures for identifying Substructure Isomorphs:** Graph isomorphism refers to the concept of two graphs being structurally identical, with a one-to-one mapping of their vertices, preserving edge connections and edge labels, and edge orientations. Exact matching of substructures is needed to compute frequent substructures accurately. Isomorphs have the same vertex labels and edge labels but different vertex IDs (as they are different instances). To identify them, we need to create a canonical substructure from the canonical instance. For this vertex IDs are changed from absolute to relative ordering. Any two exact substructures will have the same relative ordering of vertex IDs \[27\]. This is used to identify and compute the frequency of a substructure.

As the canonical instance already follows a lexicographic ordering, we can construct a canonical _k_-edge substructure by ordering the unique vertex IDs in the order of their appearance in the canonical instance. Thus, the canonical substructure can be derived by replacing every vertex ID with its relative position in the instance. The resulting canonical substructure allows us to identify isomorphs easily. Figure 7 provides an example of how a canonical substructure is created from the canonical instance. Note that the isomorphs have different canonical instances, but their relative positions following the canonical instance are the same. The relative positioning of vertex ID (1, 4, 2) for the first instance and (3, 4, 2) for the second instance reduces to (1, 2, 3). This leads to both having the exact same canonical substructure.

The process of canonical conversion to both instances and substructures is crucial as it enables us to identify duplicates and isomorphic instances, respectively.

## A. Metrics Used for Ranking Substructures

The Minimum Description Length is an information-theoretic, domain-independent metric \[15\] that has been demonstrated to emphasize the significance of a substructure in terms of its ability to compress a complete graph or forest. Although it is defined, originally, in terms of bits used for graph representation, we use the number of nodes and edges for that purpose. The general formula for MDL (DL(G)/(DL(S) + DL(G|S))) represents the description length of the substructure S being evaluated, DL(G|S) represents the description length of the graph G when compressed by replacing each instance of the<tbc>

<sup>4</sup>A canonical instance has absolute vertex IDs and a canonical substructure has relative vertex IDs.

\begin{tabular}{cc}
**Vertex ID** & **Adjacency List for Partition P1** \\ 1 & (x,1,A,2,B), (z,1,A,3,A), (i,1,A,4,C) \\ 2 & (x,1,A,2,B), (y,2,B,4,C) \\ 3 & (z,1,A,3,A), (i,3,A,4,C) \\ **Vertex ID** & **Adjacency List for Partition P2** \\ 4 & (i,1,A,4,C), (y,2,B,4,C), (i,3,A,4,C), (y,5,c,4,c) \\ 5 & (y,5,c,4,c) \\ \end{tabular}

1
X
2
A
B
1
Z
3
A
A
1
X
2
1
Z
3
A
B
1
A
A
Z
X
A
B
3
2

1
X
2
1
Z
3
A
B
1
A
A
Z
X
A
B
3
2
<x,A,1,2><z,A,1,3>
<x,A,1,2><z,A,1,3>

1
A
B
2
B
i
y
y
C
A
C
4
3
i
4
<1,A,C,1,4><y,B,C,2,4>
<1,A,C,3,4><y,B,C,2,4>
Different Canonical Instances
1 ==> 1
3 ==> 1
4 ==> 2
Using relative positions of vertex ids
4 ==> 2
2 ==> 3
2 ==> 3
<1,A,C,1,2><y,B,C,3,2>
<1,A,C,1,2><y,B,C,3,2>
Same Canonical Substructure

TABLE III: Adjacency Lists for Partitions

Fig. 5: Duplicate Generation

Fig. 6: Canonical Instances Example

Fig. 7: Substructure Isomorphism Example

