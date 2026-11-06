grid minor if the vertices in the grid minor are too light. The treewidth-pattern-covering approach fails because the solution cannot be covered by a small number of connected patterns of size O(_k_), and Nederlof’s approach focuses on counting problems and not on weighted problems. The additional use of efficient inclusion-exclusion prohibits the approach to generalize to weighted problems. In fact, subexponential parameterized problems for weighted problems that might have solutions with many connected components seem to be very rare. We are only aware of such algorithms for Maximum-Weight Independent Set \[vN20\] and Weighted Vertex Cover \[LPS<sup>+</sup>25\]. This naturally raises the following question:

Is there a general framework for subexponential parameterized algorithms that find a disconnected _k_-vertex pattern _P_ of maximum/minimum weight?

In this paper, we develop generic algorithmic tools that allow us not only to address this question, but also to tackle related problems involving (rooted/induced) minors. The approach is deterministic and can also handle directed planar graphs.

## 1.1 Our Results

Our contribution is threefold. First, we introduce a framework to generate subexponential parameterized algorithms (usually running in \(2^{\tilde{\mathcal{O}}(\sqrt{k})}n^{2.49}\) time) for problems on weighted planar graphs that search for a set of _k_ vertices with a specified property. The framework also applies to cases where the number of potential patterns of a solution is exponential in the parameter. The framework is introduced in Section 3 and requires some definitions which we set up in Section 2. Second, we show how to apply this framework to prove that the following problem _k_-Subgraph Scoring can be solved in subexponential parameterized time when parameterized by _k_. This problem generalizes problems like Maximum-Weight Independent Set, Weighted Partial Vertex Cover, Densest _k_-Subgraph, Maximum (_k,n-k_)-Cut, and more.

_k_-Subgraph Scoring

**Input:** A directed graph _G_=(_V,A_), a vertex-cost function \(c:V\rightarrow\mathbb{N}\), a weight function \(w:V\cup A\rightarrow\mathbb{R}\), an integer _k_, and values \(\alpha_1,\alpha_2,\alpha_3,\beta,W\in\mathbb{R}\).<br>
**Question:** Is there a set _S_ of cost exactly _k_, that is, \(\sum_{v\in S}c(v)=k\) and

\(\alpha_1\big(\sum_{(u,v)\in Au,v\in S}w((u,v))\big)+\alpha_2\big(\sum_{(u,v)\in Au\in S,v\notin S}w((u,v))\big)+\alpha_3\big(\sum_{(u,v)\in Au\notin S,v\in S}w((u,v))\big)+\beta\big(\sum_{v\in S}w(S)\big)\ge W?\)

Note that when _c(v_)=1 for each vertex _v_, then _k_ is the number of vertices in the solution. Third, we show more involved applications of the framework in the form of Maximum-Weight Induced Forest and different notions of minors. All applications of our framework are shown in Section 4 and summarized in the following (see Section 2 for problem definitions).

**Theorem 1.** _The following problems can be solved in_ \(2^{\tilde{\mathcal{O}}(\sqrt{k})}n^{2.49}\) _time when parameterized by the size of the solution:_

• _k_-Subgraph Scoring<tbc>

• Densest _k_-Subgraph<tbc>

• Steiner Partition<tbc>

