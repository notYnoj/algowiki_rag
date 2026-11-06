Typically, low diameter decompositions require the number of edges between clusters to be small (see e.g. \[BNW22\]). For our application however, we will utilize something different: the sum of the size of the neighborhoods of each cluster is almost linear (i.e. _n_<sup>1+_o_(1)</sup>).<sup>8</sup> Formally, we develop a decomposition \(V_1\sqcup\cdots\sqcup V_k\) of the vertices satisfying:

1. diam(_V<sub>i</sub>_)=_n_<sup>_o_(1)</sup> for all _i_.<tbc>

2. \(\sum_i|N(V_i)|=n^{1+o(1)}\).

Before describing how to obtain such a decomposition (see Theorem 4.2), let us see how it is useful. Recall that we use level(_s_) to index the most recently computed layer of the shortest path tree rooted at _s_. Now, instead of computing _L(s,_level(_s_)+1) from _L(s,_level(_s_)) by considering all pairs of vertices, we compute \(L(s,\text{level}(s)+1)\cap N(V_i)\) from \(L(s,\text{level}(s))\cap V_i\) for all _i_ where \(V_i\cap L(s,\text{level}(s))\neq\emptyset\). Note that correctness follows from the fact that \(\{V_i\}_{i=1}^k\) cover _L(s,_level(_s_)) so that \(\{N(V_i)\}_{i=1}^k\) cover _L(s,_level(_s_)+1).

Since we do not consider _L(s,_level(_s_)) all at once, we need to keep track of which vertices in the layer whose neighborhoods we have already examined. Let A(_s_) denote the vertices in _L(s,_level(_s_)) which we still need to examine, called the active vertices. Note that A(_s_) is initialized to _L(s,_level(_s_)) and each iteration of the while loop removes some _V<sub>i</sub>_ from A(_s_).

We say _V<sub>i</sub>_ is relevant to _s_ if \(V_i\cap\mathcal{A}(s)\neq\emptyset\). For each cluster _V<sub>i</sub>_, denote score(_i_) the number of sources _V<sub>i</sub>_ is relevant to. We say a cluster _V<sub>i</sub>_ is _ready_ when \(\text{score}(i)\ge\frac{|S_\text{in}||N(V_i)|}{n^{1+o(1)}}\) . Observe that there is always one ready cluster. If not, by the second property of our decomposition, we have \(\sum_i\text{score}(i)<|S_\text{in}|\). However, since there is at least one cluster relevant to each source, we obtain a contradiction via \(\sum\text{score}(i)\ge|S_\text{in}|\).

We now describe our improved algorithm (see Theorem 5.1 for full algorithm).

Correctness follows from our discussion above. We proceed to analyze the running time, where we will bound the time required by all iterations of the while loop where _V<sub>i</sub>_ is chosen as the ready cluster.

First, we claim that for any fixed source _s_, _V<sub>i</sub>_ is relevant to _s_ for _n_<sup>_o_(1)</sup> iterations (see Lemma 5.5). This follows from the first property of our decomposition \((\text{diam}(V_i)\le n^{o(1)})\) so that _V<sub>i</sub>_ can intersect at most _n_<sup>_o_(1)</sup> distinct layers of the shortest path tree of _s_. The result follows from observing that _V<sub>i</sub>_ is relevant to _s_ for one iteration per layer of the shortest path tree (i.e. one value of level(_s_)).

Second, we claim that _V<sub>i</sub>_ is selected as a ready cluster in \(\frac{n^{1+o(1)}}{|N(V_i)|}\) iterations (see Lemma 5.6). Let _T(i_) denote all iterations where _V<sub>i</sub>_ is selected. Let \(S'(t)\) denote the set of sources _V<sub>i</sub>_ is relevant to in iteration \(t\in T(i)\). Then, over all iterations where _V<sub>i</sub>_ is selected, we have \(\sum_t|S'(t)|=|S_\text{in}|n^{o(1)}\). On the other hand, since _V<sub>i</sub>_ is ready, \(\text{score}(i)=|S'(t)|\ge\frac{|S_\text{in}||N(V_i)|}{n}\) . Thus, we have \(|T(i)|\le\frac{n^{1+o(1)}}{|N(V_i)|}\) .

We now bound the time required by all iterations where _V<sub>i</sub>_ is selected, breaking our analysis into two cases: small clusters and large clusters. For small clusters with \(|N(V_i)|\le\frac{n}{|S_\text{in}|}\), the _t_-th iteration requires time \(O(S'(t)|V_i||N(V_i)|)\). Since \(\sum_tS'(t)=|S_\text{in}|n^{o(1)}\), we bound the total time as \(\sum_tO(S'(t)|V_i||N(V_i)|)=n^{1+o(1)}|V_i|\). Summing over all small clusters, the total time bound is _n_<sup>2+_o_(1)</sup>.

For large clusters, the _t_-th iteration involves a matrix product of dimension \(S'(t)\times V_i\times N(V_i)\). Summing over all iterations, we obtain (see Lemma 5.7 for the deduction)<tbc>

\(\sum_{t\in T(i)}\mathsf{T}_\text{MUL}(S'(t),V_i,N(V_i))\le O\left(\frac{n^{1+o(1)}}{|N(V_i)|}\mathsf{T}_\text{MUL}\left(\frac{|S_\text{in}||N(V_i)|}{n},V_i,N(V_i)\right)\right).\)

<sup>8</sup>To avoid confusion, we call our decomposition a low diameter small neighborhood decomposition.

\begin{tabular}{cc}
1. Let \(\mathcal{A}(s)\leftarrow L(s,\text{level}(s))\) for all _s_. (Recall level\((s)\leftarrow 0\) and _L(s,_0)={_s}._) & \\
2. While not all distances computed, select a ready cluster _V<sub>i</sub>_: & \\
(a) Compute \(L(s,\text{level}(s)+1)\cap N(V_i)\) from \(L(s,\text{level}(s))\cap V_i\) for all _s_ that _V<sub>i</sub>_ is relevant to. & \\
(b) Remove _V<sub>i</sub>_ from A(_s_). & \\
(c) For any \(\mathcal{A}(s)=\emptyset\), increment level(_s_) and set \(\mathcal{A}(s)\leftarrow L(s,\text{level}(s))\). & \\
\end{tabular}

