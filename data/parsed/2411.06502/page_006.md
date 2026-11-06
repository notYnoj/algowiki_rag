applications of MUL. However, this did not result in a true reduction, as the algorithm ran in O(_n_<sup>4</sup>) time (Chen initially claimed a running time of O(_n_<sup>3.5</sup>), but this was later corrected in \[SPA17\]). The second work, by \[Mao22\], uses bounded difference min-plus products (a special case of bounded monotone min-plus multiplication) to achieve truly subcubic time for the unweighted (and very small weight) tree edit distance problem. However, Mao’s scheme was not powerful enough to achieve a fine-grained reduction from the general weight case of TED to MUL.

**Other related works.** Recently, there has been significant interest in TED approximation algorithms \[BGHS19, SS22\] as well as TED when the distance is bounded \[AJ21, DGH<sup>+</sup>22, DGH<sup>+</sup>23\].

## 2 Technical Overview

### 2.1 Similarity and alignment graphs

We examine TED through its _mapping formulation_ (as in \[Mao22\]). This means that rather than thinking of TED as finding a least-cost transformation via insertions, deletions, and matches, we shift our perspective towards seeking a maximum weight mapping between two forests.

**String similarity.** To ease into this formulation, we first discuss the mapping formulation of (weighted) string edit distance. In the (String) Edit Distance Problem (ED), we are given two strings \(A=a_1a_2\cdots a_n\) and \(B=b_1b_2\cdots b_m\), and a cost function \(\delta\). The goal is to find the least cost needed to transform _A_ into _B_, by substituting, inserting or deleting characters. The costs \(\delta(a_i,b_j)\), \(\delta(a_i,\varepsilon)\), and \(\delta(\varepsilon,b_j)\) describe the cost of substituting _a<sub>i</sub>_ with _b<sub>j</sub>_, deleting _a<sub>i</sub>_, and inserting _b<sub>j</sub>_, respectively.

We define \(\eta(a_i,b_j):=\delta(a_i,\varepsilon)+\delta(\varepsilon,b_j)-\delta(a_i,b_j)\) to be _the weight of matching a<sub>i</sub> with b<sub>j</sub>_. Determining the string edit distance between _A_ and _B_ translates into calculating the _similarity between A and B_, defined as

\(\text{sim}(A,B)=max_{i_1<\cdots<i_k\in[1..n]j_1<\cdots<j_k\in[1..m]}\left\{\eta(a_{i_1},b_{j_1})+\eta(a_{i_2},b_{j_2})+\cdots+\eta(a_{i_k},b_{j_k})\right\}.\)

Thereby, we obtain \(\text{sim}(A,B)=\sum_i\delta(a_i,\varepsilon)+\sum_j\delta(\varepsilon,b_j)-\text{ed}(A,B)\).

**String alignment graphs.** The value sim(_A,B_) can be computed using the following recurrence

\(\text{sim}(A,B)=\left\{\begin{array}{ c c }
0, & \text{if}|A|=0\text{or}|B|=0, \\
max\left\{\begin{array}{ c }
\text{sim}(A[2..n],B), \\
\text{sim}(A,B[2..m]), \\
\text{sim}(A[2..n],B[2..m])+\eta(a_1,b_1)
\end{array}\right\}, & \text{otherwise}.
\end{array}\right.\)

These computations can be reformulated as finding a longest path on a directed weighted acyclic graph, commonly referred to as the _alignment graph_. This graph has as the vertex set the grid \([1..(n+1)]\times[1..(m+1)]\), where each node (_i,j_) is connected with an edge of weight zero to its right and upper neighbors, i.e., (_i_+1_,j_) and (_i,j_+1), if they are within the borders. Additionally, from each node \((i,j)\in[1..n]\times[1..m]\), there is an edge to (_i_+1_,j_+1) with weight \(\eta(a_i,b_j)\). Computing sim(_A,B_) translates to finding a longest path between (1,1) and (_n_+1_,m_+1) in this graph. Each time the longest path traverses an edge from (_i,j_) to (_i_+1_,j_+1) we map _a<sub>i</sub>_ to _b<sub>j</sub>_.

It is worth noting that in the literature several studies \[Sch95, Tis06, ACS08, Kle05\] have focused on computing all longest distances from the lower-left border to the upper-right border in an alignment graph. For both weighted and unweighted edit distance, this task can be accomplished in time O((_n+m_)<sup>2</sup>).

