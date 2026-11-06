<tbc>each _M<sub>i</sub>_, we compute the set of all isomorphic embeddings in the data graph, denoted _Res(M<sub>i</sub>_). These partial embeddings are then incrementally combined through _join_ operations, followed by a _filter_ step to ensure that only valid matches of the full pattern are retained. The final result, _Res(G<sub>p</sub>_), contains all complete isomorphisms of _G<sub>p</sub>_ within _G<sub>d</sub>_. This divide-and-conquer strategy is simple yet effective: reducing the matching task to motif-level computations achieves computational efficiency through parallelization, and reusing motif embeddings avoids the redundant searches common in tree- search-and-prune approaches.

To make this process concrete, we now present a step-by- step example of finding all subgraph isomorphisms. As a first step, we select a set of motifs to be used to decompose _G<sub>p</sub>_. Because the number of unique motifs grows rapidly with graph size, we limit ourselves to a small, predefined subset. The motif set M can be predefined or adaptively selected based on the characteristics of the data graph. The efficiency of the overall decomposition process depends heavily on this choice. We discuss detailed motif selection strategies in Section VI-B, and for now, we focus on demonstrating the workflow.

In this example, we only use two motifs: _M_<sub>2</sub>, a simple 2- node edge, and _M_<sub>4</sub>. The embeddings of _M_<sub>2</sub>, _Res(M_<sub>2</sub>), are always available since they can be obtained by enumerating all edges in _G<sub>d</sub>_, and hence serve as a default primitive in our method. Building on these primitives, _Res(M_<sub>4</sub>) can be computed by calling the complete workflow of our solver, which constructs larger motif embeddings from smaller ones like _Res(M_<sub>2</sub>). We defer the details of this computation to Section III-D, where the underlying components are formalized in Algorithm 2; for now, we assume that both _Res(M_<sub>2</sub>) and _Res(M_<sub>4</sub>) have been computed and stored in tabular form like<tbc>

<tbc>a dataframe structure, as illustrated in Fig. 2(c). Each row in the dataframe corresponds to a matched subgraph in the data graph, and each column represents the vertex indices assigned to the corresponding positions in the motif.

With the motif embeddings prepared, the next step is to decompose the pattern graph using these motifs as templates. There are many valid ways to decompose a pattern graph - we only need to find one. We prioritize larger motifs, as they tend to reduce the number of decomposition steps, a design choice we validate empirically in Sec. VI-B. Additionally, we require that adjacent components share overlapping vertices, which serve as join key constraints during the _join_ phase, as detailed later in this section and formalized in Algorithm 1.

In Fig. 2(d), we illustrate two valid decompositions using only _M_<sub>4</sub>, with each slice _S<sub>i</sub>_ highlighted in a different color. For this example, we choose one such decomposition: _S_<sub>0</sub>:_v_<sub>2</sub>-_v_<sub>3</sub>-_v_<sub>4</sub>-_v_<sub>5</sub> and _S_<sub>1</sub>:_v_<sub>5</sub>-_v_<sub>0</sub>-_v_<sub>1</sub>-_v_<sub>2</sub>. Here, _S<sub>i</sub>_ denotes the _i_-th graph slice of the decomposition, and the two slices share overlapping vertices at _v_<sub>2</sub> and _v_<sub>5</sub>. To clarify the terminology, _M_<sub>4</sub> represents the generic motif structure used as a reusable matching template, while each _S<sub>i</sub>_ is a concrete subgraph of _G<sub>p</sub>_ with fixed vertex assignments. Since we use _M_<sub>4</sub> for decomposition, both _S_<sub>0</sub> and _S_<sub>1</sub> are instances of _Res(M_<sub>4</sub>), and together they reconstruct the full cycle of _G<sub>p</sub>_.

Our decomposition records the overlapping vertices between slices, which later serve as constraints in the _join_ phase. In this example, the overlaps occur at _v_<sub>2</sub> and _v_<sub>5</sub>, corresponding to the constraints _S_<sub>0</sub>\[0\]=_S_<sub>1</sub>\[3\] and _S_<sub>0</sub>\[3\]=_S_<sub>1</sub>\[0\]. We now proceed to join the motif embeddings corresponding to the slices. For clarity, we denote the two dataframes as _Res(M_<sub>4</sub>)<sub>L</sub> and _Res(M_<sub>4</sub>)<sub>R</sub>, representing the left and right sides<tbc>

(a)
(b)
(e)
2
3
4
6
2
3
4
join with key matching
1
0
5
1
0
5
C1
data graph
pattern graph
C2
key-matching constraints:
0
1
2
3
0
1
2
3
C1: Res(M), [0] = Res(M), [3]
(c)
0
5
4
3
0
5
4
3
C2: Res(M), [3] = Res(M), [0]
0
1
0
1
2
3
0
5
4
6
0
5
4
6
2
3
4
5
5
0
1
2
0
5
0
5
4
3
0
5
4
6
2
3
4
5
2
3
4
5
5
4
3
2
1
0
0
5
4
6
2
3
4
5
2
3
4
5
2
3
4
5
5
4
3
2
1
2
2
3
4
5
2
1
5
0
1
2
5
0
1
2
5
4
3
2
5
4
3
2
5
0
1
2
(f)
5
0
5
4
3
2
filter
Res(M,
Res(M,
(# of duplicated vertices) = (# of constraints)
(d)
2
2
3
4
2
3
4
4
2
3
4
5
5
0
1
2
2
3
4
5
5
0
1
2
2
3
4
5
5
1
2
1
0
5
5
1
1
0
5

Fig. 2. A motivating example illustrating subgraph isomorphism: (a) the input data graph and (b) the pattern graph. The decomposition uses two motifs, _M_<sub>2</sub> and _M_<sub>4</sub>, along with (c) their corresponding isomorphic embeddings in the data graph, _Res(M_<sub>2</sub>) and _Res(M_<sub>4</sub>). Panel (d) shows two possible decompositions of the pattern graph using _M_<sub>4</sub>. Both are valid, but for this example, we use the second decomposition to demonstrate the workflow. Panels (e) and (f) visualize the _join_ and _filter_ operations in tabular form, which are used to reconstruct valid matches of the pattern graph from motif embeddings. The tables are color-coded to distinguish _Res(M_<sub>4</sub>)_<sub>L</sub>_ and _Res(M_<sub>4</sub>)_<sub>R</sub>_. The two join key constraints, labeled _C_1 and _C_2, are highlighted with arrows pointing to their corresponding columns.

