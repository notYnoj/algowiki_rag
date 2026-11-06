<tbc>of the join operation. Based on the overlapping nodes identified during decomposition, the join constraints are defined as _Res(M_<sub>4</sub>)<sub>L</sub>\[0\]==_Res(M_<sub>4</sub>)<sub>R</sub>\[3\] and _Res(M_<sub>4</sub>)<sub>L</sub>\[3\]==_Res(M_<sub>4</sub>)<sub>R</sub>\[0\], where the bracket notation refers to entire columns of vertex assignments at the respective motif embeddings. These constraints are used as join keys, implemented as hash joins in standard dataframe libraries and relational database systems, whose cost grows linearly with the input and output table sizes. The _join_ step eliminates invalid combinations and retains only those pairs of embeddings that satisfy the required boundary conditions. Fig. 2(e) illustrates the join operation and its output to clarify the overall process.

Although the _join_ operation enforces the specified boundary constraints between motif embeddings, it may still produce combinations with unintended vertex overlaps. These arise when two embeddings share additional vertices beyond the expected overlaps, violating the one-to-one vertex mapping required for valid subgraph isomorphism. To address this, we introduce a _filter_ step that removes such invalid combinations. Fig. 2(f) illustrates an example of this issue. In general, the number of duplicated vertices in each joined row should exactly match the number of join constraints. Any row containing additional duplicates is deemed invalid and discarded. This is similar to the pruning phase of a tree-search.

By applying this _join_-and-_filter_ process, we ensure that only valid subgraph isomorphisms are retained in the final result. _Algorithm 1_ outlines the procedure at a high-level. In the following subsections, we formalize this methodology and show how it enables a highly parallelizable, data-centric algorithm built entirely on open-source, commodity data science tools, without requiring any custom GPU kernels. Nevertheless, the approach delivers strong performance and scalability.

## C. Pattern Graph Decomposition Using Motifs

We now generalize the decomposition and show that any pattern graph can be decomposed using a broader set of motifs.

In principle, many motifs could be used for decomposing the graph; we typically restrict ourselves to a small, carefully- chosen family that balances coverage and computational cost. The choice of motifs has a significant impact on the performance of the algorithm. Larger motifs do not necessarily guarantee faster execution, as their embeddings _Res(M_) often result in more expensive join operations. Including more<tbc>

<tbc>**Algorithm 1** \(\Delta\)-Motif Join-and-Filter Loop: _R_ collects the final result, _D_ is the decomposition of the pattern graph into _motifs_

function \(\Delta\)-MOTIF(_G<sub>p</sub>,DB_)

2: \(R\leftarrow\emptyset\)

3: \(D\leftarrow\text{DECOMPOSE}(G_p,DB)\)

4: \(M,C\leftarrow\text{NEXTMOTIFTOPROCESS}(D)\triangleright\langle\mathcal{M},Constraints\rangle\)

5: **while** \(M\neq\emptyset\) **do**

6: \(R\leftarrow\text{INNERJOIN}(R,M,C)\triangleright\) Join

7: \(R\leftarrow\text{FILTEROVERLAPPINGNODES}(R)\triangleright\) Filter

8: \(M,C\leftarrow\text{NEXTMOTIFTOPROCESS}(D)\)

9: **end while**

10: **return** _R_

11: **end function**

<tbc>motifs in the set also increases the upfront preparation time. In section VI-B, we discuss how to select an appropriate motif set based on the characteristics of both the data and pattern graphs, and support these design choices with empirical results.

Given a defined set of motifs M, we now turn to decomposing the pattern graph _G<sub>p</sub>_ into smaller slices. At each iteration, we traverse the chosen motif set in descending order of size, favoring larger motifs to reduce the number of decomposition steps. For each motif in the set, we invoke a subgraph isomorphism solver, such as VF2, to find a valid matching slice _S<sub>i</sub>_. If a match is found, it becomes the next slice in the decomposition; otherwise, we continue to the next motif in the list. VF2 is chosen here because it quickly returns a single match, which suits our needs for this iterative, one-slice- at-a-time decomposition process. Because this search runs on the small pattern graph and stops at the first match, its cost depends only on the pattern size, not on the much larger data graph.

While this may seem counterintuitive as we replace one subgraph isomorphism problem with another, we highlight the following: 1) instead of performing subgraph isomorphism on the data graph, we apply it to the typically much smaller pattern graph, 2) the motifs we seek are typically orders of magnitude smaller than both the data and pattern graph, and 3) in our motif decomposition, we only require finding a single match of the motif in the pattern, allows us to terminate the search early rather than exhaustively enumerating all possible matches. Under these conditions, the tree-search based algorithm is actually more suitable and efficient for this task. Lastly, the motif decomposition searches for **a** decomposition rather than the ideal decomposition.

Once a slice _S<sub>i</sub>_ is identified, the algorithm inspects all vertices in _S<sub>i</sub>_ to determine which have outgoing edges that remain uncovered in the current pattern graph. These vertices are designated as boundary nodes. Boundary nodes serve as connection points for subsequent slices. For example, in Section III-B, vertices _v_<sub>2</sub> and _v_<sub>5</sub> from _S_<sub>0</sub> play this role. The non-boundary nodes from _S<sub>i</sub>_ are removed from the pattern graph to form a reduced graph for the next iteration, while the boundary nodes are retained to ensure overlap with subsequent matches. This procedure is repeated in the following iterations. Each new slice is matched using the reduced pattern graph, and its overlapping vertices with the union of previously selected slices are recorded. These overlapping vertices define structural dependencies across slices and are stored as join constraints. These constraints are later used in the _join_ step, formalized in Algorithm 1, to reassemble the full pattern structure.

As a result of the decomposition process, we obtain a sequence of slices _S_<sub>0</sub>_,S_<sub>1</sub>_,...,S<sub>n</sub>_ along with their corresponding list of motifs. This sequence determines the order in which the motifs appear within the pattern graph, and consequently, the order in which the associated _Res(M_) dataframes are joined during reconstruction.

In practice, the decomposition step is computationally inexpensive and contributes only a negligible portion to the overall<tbc>

