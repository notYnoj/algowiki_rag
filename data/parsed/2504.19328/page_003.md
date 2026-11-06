<tbc>AGM \[17\] and FSG \[18\] are two popular main memory graph mining algorithms that use the _apriori_ concept. These approaches generate frequent (_k_+1) subgraphs from frequent _k_-subgraphs. The FSG identifies repeating substructures in graphs using an apriori approach \[18\]. This is different from Subdue since it entails finding interesting substructures in a graph or forest. Canonical labeling is added to the apriori algorithm. The property that identical graphs have identical canonical labeling has been strategically used to identify frequent substructures. FSG determines canonical labels using a flattened graph adjacency matrix.

Disk-based graph mining algorithms \[19\]-\[21\] were developed to deal with larger graph sizes. Portions of the graph are staged into memory for processing using buffer-management techniques. Indexing was used to improve retrieval for staging. gIndex \[22\] uses frequent substructures as units for indexing. However, these solutions need explicit data marshalling between disk and main memory entailing developing buffer management strategies. To avoid developing complex buffer management policies, the use of relational databases has been leveraged for graph mining to leverage buffer management and query optimization. HDB-Subdue \[23\] used the RDBMS for graph representation and SQL to discover substructures. This approach was able to scale to handle graphs with millions of edges. However, self-joins on large relations and the number of joins needed for canonical form generation (column sorting instead of row sorting) limited scaling further.

A number of graph mining methods have shown success in cloud-based deployments \[24\]. Additionally, research has explored patterns in big graphs using the Map/Reduce framework \[25\]. However, the pattern searching technique in \[25\] requires a specified pattern to search for all instances of that pattern in the graph. If we need to find a pattern with the highest compressibility, we cannot supply it beforehand. Splitting/partitioning large graphs into manageable chunks for distributed processing is explored in \[26\]. Scalable substructure discovery on large simple graphs using Map/Reduce has been developed in \[27\]. A graph can be split into partitions in different ways, processed by distributed and parallel architecture, and results from across partitions combined to obtain correct results.

_This paper’s focus is on MLNs instead of simple graphs, and specifically HoMLNs. Further, the decoupling-approach is chosen which entails the development of a composition function for its efficient and flexible analysis. It also uses extant substructure discovery for each layer. Correctness of the algorithm is also shown._

## IV. PRELIMINARIES AND TERMINOLOGY

**Edge List as graph input:** A graph (layer, inter-layer, or a partition) is represented as a list of unordered edges. Each edge is completely represented by a 5-element tuple<sup>2</sup>_\<E<sub>l</sub>,V<sub>sid</sub>,V<sub>sl</sub>,V<sub>did</sub>,V<sub>dl</sub>\>_ where, _E<sub>l</sub>_ is edge label, _V<sub>sid</sub>_ is source vertex ID, _V<sub>sl</sub>_ is source vertex label, _V<sub>did</sub>_ is destination<tbc>

<tbc>vertex ID and _V<sub>dl</sub>_ is destination vertex label. In this context, it is important to note that the vertex IDs (_V<sub>sid</sub>_ and _V<sub>did</sub>_) are guaranteed to be unique. However, vertex labels (_V<sub>sl</sub>_ and _V<sub>dl</sub>_) and the edge label (_E<sub>l</sub>_) need not be unique.  I shows the edge list representation for the input graph (or a layer) shown in Figure 3.

This 5-element tuple edge representation (that includes direction) is used to represent a _k_-edge substructure (a connected graph with _k_ edges and at most _k_+1 nodes) as a collection of _k_ 1-edge substructures. Our algorithm takes an input graph represented as a text file with a 1-edge substructure per line.

**Adjacency List:** Adjacency list is a representation where each vertex on which the edges are incident (both in and out) are associated with the node using a list (of 1-edge substructures.)  II shows the edge list and adjacency list of the graph shown in Figure 3.

**Graph Partitioning:** A MLN layer _L<sub>i</sub>_ can be partitioned into p partitions (\(L_1^i\), \(L_2^i\),..., \(L_p^i\)) for distributed processing. We use _range-based partitioning_ \[27\] to create the partitions using the vertex IDs. Each graph partition<sup>3</sup> is a range of node IDs and the size of each partition need not be the same. There can be missing vertex IDs in a given range. As the ranges are disjoint, nodes in adjacency list partitions are also disjoint. Each vertex ID in the range and its adjacency list corresponds to a single adjacency list partition. If neighboring nodes are in two partitions, the edge connecting them will be in the adjacency list of both partitions. As a result, during expansion, the same substructure can belong to many graph partitions. As adjacency list partitions are indexed on vertex IDs, each substructure is expanded only once.

Two partitions of the graph in Figure 3 are shown in Figure 4. Partition _p_1 is assigned vertex IDs from 1 to 3, whereas partition _p_2 is allotted vertex IDs 4 to 5. Both partitions are connected by red edges, which appear in different adjacency list partitions. The adjacency list partitions are displayed in table III. The edges that occur in both adjacency list partitions are _\<i,_1_,A,_4_,C\>,\<y,_2_,B,_4_,C\>_, and _\<i,_3_,A,_4_,C\>_.

<sup>2</sup>This representation is generic and can be extended to attributed graphs by using a distinct edge identifier in the edge representation. However, MLN layers are simple graphs by definition. <sup>3</sup>Graph partition and partition are used interchangeably. Adjacency List partition is an adjacency list for a specific graph partition.

\begin{tabular}{cc}
**Edge List** & **Adjacency List** \\
(x,1,A,2,B) & 1 (x,1,A,2,B), (z,1,A,3,A), (i,1,A,4,C) \\
(z,1,A,3,A) & 2 (x,1,A,2,B), (y,2,B,4,C) \\
(i,1,A,4,C) & 3 (z,1,A,3,A), (i,3,A,4,C) \\
(y,2,B,4,C) & 4 (i,1,A,4,C), (y,2,B,4,C), (i,3,A,4,C), (y,5,c,4,c) \\
(i,3,A,4,C) & 5 (y,5,c,4,c) \\
(y,5,c,4,c) & \\
\end{tabular}

1
X
2
5
A
B
C
i
y
Z
y
A
C
3
i
4

1
X
2
5
A
B
C
i
y
Z
y
A
C
3
i
4

Fig. 3: Input Graph

TABLE I: Edge List

Fig. 4: Partitioned Input Graph

TABLE II: Adjacency List

