<tbc>**Algorithm 1** Building the term seed lists

**Require:** Collection D={_x_<sub>1</sub>_,...,x<sub>n</sub>_} of sparse vectors over vocabulary _V_ ; seeds per term _L_

**Return:** Seed lists \(\{H_t\}_{t\in V}\); per-term maximum weights \(\{w_t\}_{t\in V}\)

1: **for** each term \(t\in V\) **do**

2: \(H_t\leftarrow\) empty min-heap of capacity _L_, keyed on weight

3: \(w_t\leftarrow 0\)

4: **end for**

5: **for** each document \(d\in\mathcal{D}\) **do**

6: **for** each term _t_ with _x<sub>d</sub>_\[_t_\]_\>_0 **do**

7: \(w_t\leftarrow\mathrm{max}(w_t,x_d[t])\)

8: **if** |_H<sub>t</sub>|\<L_ **then**

9: push (_x<sub>d</sub>_\[_t_\]_,d_) onto _H<sub>t</sub>_

10: **else if** _x<sub>d</sub>_\[_t_\]_\>_min(_H<sub>t</sub>_) **then**

11: replace the minimum of _H<sub>t</sub>_ with (_x<sub>d</sub>_\[_t_\]_,d_)

12: **end if**

13: **end for**

14: **end for**

15: **return** {_H<sub>t</sub>},_{_w<sub>t</sub>_}

**Algorithm 2** Sparse PiPNN

**Require:** Sparse vectors {_x_<sub>1</sub>_,...,x<sub>n</sub>_}; neighbors per point within a leaf _k<sub>t</sub>_; degree bound _D_

**Return:** Graph _G_ with out-degree at most _D_

1: \(\mathcal{P}\leftarrow\) BallCarve({_x<sub>i</sub>_}) \(\triangleright\) **Sparse:** leaders scored via inverted index. See \[31\] for the full ball carving description.

2: **for** each leaf \(P\in\mathcal{P}\) **do**

3: build an inverted index over \(P\triangleright\) **Sparse:** replaces PiPNN’s dense GEMM

4: compute all pairwise inner products in _P_ from its posting lists

5: add each point’s _k<sub>t</sub>_ nearest neighbors in _P_ as candidate edges

6: **end for**

7: \(C\leftarrow\) HashPrune(candidates) \(\triangleright\) Rubel et al. \[31\]

8: \(G\leftarrow\) RobustPrune(C_,D_) \(\triangleright\) PiPNN, on inner products

9: **for** each point _p_ **do** \(\triangleright\) **Sparse:** refinement pass

10: \(\text{\textit{card}}\leftarrow\) beam search of _G_ for _x<sub>p</sub>_ from _p_’s term seeds

11: \(N(p)\leftarrow\) RobustPrune(\(\text{\textit{card}}\cup N(p),D\))

12: **end for**

no such traversal: the query’s non-zero components directly identify the posting lists where its answers are guaranteed to reside. Term-based entry point selection brings this advantage to graph search by initializing the search at nodes that carry large weight on the query’s most important terms, which leads to fewer wasted distance computations. Specifically, in the offline phase, described in Algorithm 1, we precompute for every vocabulary term \(t\in V\) a seed list _H<sub>t</sub>_ containing the _L_ documents with the largest weight on that term, that is, the _L_ documents _d_ maximizing _x<sub>d</sub>_\[_t_\], along with the largest weight on the term, _w<sub>t</sub>_=max_x<sub>d</sub>x<sub>d</sub>_\[_t_\]. Each seed list is maintained as a min-heap of capacity _L_, so the lists can be built in a single pass over the non-zero entries of the collection in \(O(\mathrm{nnz}\cdot\mathrm{log}L)\) time. The resulting table holds at most \(|V|\cdot L\) entries which concretely translates to roughly 8 MB of space on the MS<tbc>

<tbc>**Algorithm 3** GRIP Search

**Require:** Query _q_; graph _G_; full vectors {_x<sub>d</sub>_}; 8-bit routing sketches \(\{\tilde{x}_d\}\) of each document’s top-_R_ weights; seed lists {_H<sub>t</sub>_} and maxima {_w<sub>t</sub>_}; seed terms _T_; beam width _ef_; patience _P_

**Return:** Top-_k_ documents for _q_

1: \(\tilde{q}\leftarrow\) 8-bit quantization of _q_ \(\triangleright\) integer query table

2: \(\mathcal{T}\leftarrow\) the _T_ query terms of largest \(q_t\cdot w_t\)

3: \(S\leftarrow\bigcup_{t\in\mathcal{T}}H_t\triangleright\) term-based entry points

4: \(B\leftarrow\) BeamSearch\((G,\tilde{q},\{\tilde{x}_d\},S,ef,P)\triangleright\) routing on sketches; stop after _P_ expansions without top-_k_ change

5: **return** top _k_ of _B_ rescored with \(\langle q,x_d\rangle\triangleright\) exact rescoring

MARCO v1 8.8M passage collection, a negligible space overhead in comparison to the 8.8 GB used to store the remainder of the index. At query time, we use _w<sub>t</sub>_ to bound how much each query term can contribute to any document’s score: for every document \(d,q_t\cdot x_d[t]\le q_t\cdot w_t\). We select the _T_ query terms with the largest such upper bound, take the union of their seed lists \(S=\bigcup_{t\in\mathcal{T}}H_t\), which contains at most \(T\cdot L\) documents, and initialize the beam with every document in _S_. We set _L=_64 throughout and _T=_2 for SPLADE-CoCondenser and _T=_4 for SPARSEUP, each selected on held-out training queries disjoint from the evaluation queries.

## 3.2 Approximate Routing via Sparse Sketching

The second core optimization at the heart of GRIP is approximate routing via sparse sketching, which is inspired by the concentration of importance phenomenon of learned sparse embeddings identified by Bruch et al. \[5\]. In essence, concentration of importance states that a small fraction of the non-zero components of learned sparse vectors, which themselves are a small proportion of the total number of dimensions, contains the majority of the \(\ell_1\) mass of the vector. While Bruch et al. \[5\] utilize this insight in the design of Seismic, we leverage this same structure for faster graph-based traversal. To our knowledge, this is a novel optimization in the context of sparse graph ANN since prior graph-based systems for LSR such as PyANNS and GrassRMA adopt quantization techniques to represent the vectors in lower precision (as we also do in GRIP) but do not consider dropping low-magnitude non-zero components entirely. In particular, our sparse sketching scheme, as described in Algorithm 3, involves constructing, for every document _d_, a sketch \(\tilde{x}_d\) that retains only the _R_ largest-magnitude non-zero components of _x<sub>d</sub>_ and sets the remaining components to zero. Importantly, sketching affects only search: the graph itself is constructed on the full vectors, as are the seed lists, so the edges of the graph reflect exact similarities between documents.

We store these sketches as a second copy of the collection, quantized to 8 bits, and run the entire beam search over them: both the choice of which nodes to expand and the decision of when to terminate are made using the sketched scores \(\langle q,\tilde{x}_d\rangle\). Once the search terminates, we rescore every document in the final beam with its exact score \(\langle q,x_d\rangle\) against the full vectors and return the top _k_. Because the weights of learned sparse embeddings are non-negative, the sketched score is always a lower bound on the exact score,<tbc>

