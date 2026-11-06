## 6 Faster Weighted and Unweighted Tree Edit Distance and APSP Equivalence

### Tree similarity.

Similarly, given two forests **F** and \(\mathbf{F}'\), define \(\eta(v,v'):=\delta(v,\varepsilon)+\delta(\varepsilon,v')-\delta(v,v')\). The mapping we consider for TED corresponds to two sequences of distinct nodes \(v_1,\dots v_k\in\mathbf{F}\) and \(v'_1,\dots v'_k\in\mathbf{F}'\) such that for all \(1\le i<j\le k\):

_v<sub>i</sub>_ is an ancestor of _v<sub>j</sub>_ in **F** if and only if \(v'_i\) is an ancestor of \(v'_j\) in \(\mathbf{F}'\),

_v<sub>j</sub>_ is an ancestor of _v<sub>i</sub>_ in **F** if and only if \(v'_j\) is an ancestor of \(v'_i\) in \(\mathbf{F}'\), and

if neither _v<sub>i</sub>_ nor _v<sub>j</sub>_ is the ancestor of the other, _v<sub>i</sub>_ comes before _v<sub>j</sub>_ in the pre-order traversal of **F** if and only if \(v'_i\) comes before \(v'_j\) in the pre-order traversal of **F**.

The _similarity between_ **F** _and_ \(\mathbf{F}'\), denoted as \(\mathrm{sim}(\mathbf{F},\mathbf{F}')\), maximizes \(\sum_{1\le i\le k}\eta(v_i,v'_i)\), where the maximum is taken over all such mappings.

As for strings, \(\mathrm{sim}(\mathbf{F},\mathbf{F}')=\sum_{v\in\mathbf{F}}\delta(v,\varepsilon)+\sum_{v^\prime\in\mathbf{F}^\prime}\delta(\varepsilon,v')-\mathrm{ed}(\mathbf{F},\mathbf{F}')\).

### Forest alignment graphs.

Suppose we are given \(\mathrm{sim}(\mathrm{sub}(v),\mathrm{sub}(v'))\) for all \(v\in\mathbf{F}\) and \(v'\in\mathbf{F}'\), where sub(_v_) indicates the subtree rooted at node _v_. Then, the value \(\mathrm{sim}(\mathbf{F},\mathbf{F}')\) can be computed using Shasha and Zhang’s recurrence scheme \[SZ89\]. Given forests **F** and \(\mathbf{F}'\) with pre-order _v_<sub>1</sub>_,...,v_<sub>|**F**|</sub> and \(v'_1,\dots,v'_{|\mathbf{F}^\prime|^\prime}\) they compute:

\(\mathrm{sim}(\mathbf{F},\mathbf{F}')=\left\{\begin{array}{ c c }
0, & \text{if}\mathbf{F}=\varnothing\text{or}\mathbf{F}'=\varnothing, \\
\mathrm{max}\left\{\begin{array}{ c c }
\mathrm{sim}(\mathbf{F}\backslash v_1,\mathbf{F}'), &  \\
\mathrm{sim}(\mathbf{F},\mathbf{F}'\backslash v'_1), &  \\
\mathrm{sim}(\mathbf{F}\backslash\mathrm{sub}(v_1),\mathbf{F}'\backslash\mathrm{sub}(v'_1))+\mathrm{sim}(\mathrm{sub}(v_1),\mathrm{sub}(v'_1))
\end{array}\right\}, & \text{otherwise}.
\end{array}\right.\)

Once again, these computations can be rephrased as finding the longest path in a directed acyclic graph with a grid as the vertex set, but only under the condition that we have the values \(\mathrm{sim}(\mathrm{sub}(v),\mathrm{sub}(v'))\) for all \(v\in\mathbf{F}\) and \(v'\in\mathbf{F}'\). With this condition in place, we can construct a grid \[1_.._(|**F**|+1)\] \(\times\) \[1_.._(|**F**|+1)\]. Similar to the case of strings, each node \((i,i')\) is connected to its right and upper neighbors with an edge of weight zero, i.e., \((i+1,i')\) and \((i,i'+1)\) (if they are within the borders). Additionally, from each node \((i,i')\in\) \[1_.._|**F**|\] \(\times\) \[1_.._|**F**|\], there is an edge to \((j,j')\) with weight \(\mathrm{sim}(\mathrm{sub}(v_i),\mathrm{sub}(v'_i))\). Here, _j_ and \(j'\) are the smallest integers \(j\ge i\) and \(j'\ge i'\) such that \(v_j\notin\mathrm{sub}(v_i)\) and \(v'_{j^\prime}\notin\mathrm{sub}(v'_{j^\prime})\).

For an illustration (and a more formal definition) of such an alignment graph, refer to Figure 6 in Section 4, where we reduce to APSP the problem of computing all longest distances from the lower-left border to the upper-right in a forest alignment graph.

## 2.2 Warm-up: TED on caterpillar trees.

To better understand our algorithm for TED, let us first examine a more restricted yet significant case.

### Caterpillar trees.

_Caterpillar trees_ consist of a central path with nodes labeled _c_<sub>1</sub>_,c_<sub>2</sub>_,...,c<sub>n</sub>_, where _c_<sub>1</sub> is the root. Additional, each central node _c<sub>i</sub>_ has both a left child _l<sub>i</sub>_ and a right child _r<sub>i</sub>_.<sup>3</sup>

Let us examine the similarity mapping for two such caterpillar trees **T** and \(\mathbf{T}'\), of size |**T**|=3_n_, \(|\mathbf{T}'|=3n'\) with node sets \(\{l_i,c_i,r_i\}_{i\in[1..n]}\) and \(\{l'_i,c'_i,r'_i\}_{i\in[1..n^\prime]}\). We examine such a mapping under an additional simplifying assumption: nodes from one side of the caterpillar **T** are always mapped to nodes of the same side of the caterpillar \(\mathbf{T}'\).

\(\blacksquare\) **Assumption A.** _The nodes_ {_c<sub>i</sub>}<sub>i</sub>,_ {_l<sub>i</sub>}<sub>i</sub> and_ {_r<sub>i</sub>}<sub>i</sub> are always only mapped by_ \(\mathrm{sim}(\mathbf{T},\mathbf{T}')\) _to nodes in_ \(\{c'_i\}_i\), \(\{l'_i\}_i\) _and_ \(\{r'_i\}_i\)_, respectively._

<sup>3</sup> In standard literature, caterpillar trees can take a more general form. Here, we focus on a specific type of caterpillar tree, though we continue to refer to them simply as caterpillar trees.

