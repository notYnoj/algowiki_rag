• Weighted Partial Vertex Cover<tbc>

• Maximum-Weight Induced Matching<tbc>

• Maximum-Weight Induced Forest

_The following problems can be solved in_ 2<sup>O(_k/_log(_k_))</sup>_n_<sup>2.49</sup> _time when parameterized by the size of the model (or the size of the pattern graph in the case of_ Subgraph Isomorphism_):_

• Minimum-Weight Rooted Simple Minor<tbc>

• Maximum-Weight Rooted Parallel Induced Minor<tbc>

• Minimum-Weight Subgraph Isomorphism<tbc>

• Maximum-Weight Induced Subgraph Isomorphism

Before we give an overview of how the framework works, let us be explicit about our perspective here. The main goal of our work is to improve the theoretical understanding of subexponential phenomena, and we focus exclusively on this aspect. We do not attempt to optimize our results from the perspective of algorithm engineering, and reducing the hidden constant in the exponent is an interesting challenge beyond the scope of this work. Moreover, the framework is technically involved and considerably less accessible than, for example, bidimensionality. This is perhaps unsurprising, since problems seem to become substantially more complicated as soon as one moves to weighted or directed graphs. Nonetheless, this raises the natural question of whether a simpler approach-- perhaps based on a logic fragment such as MSO--could achieve similar results. However, pursuing such a direction is hindered by the delicate boundary between problems that admit subexponential parameterized algorithms on planar graphs and those that do not. In particular, while the above theorem shows that Steiner Partition can be solved in subexponential parameterized time, even slight generalizations may break this property. For instance, the closely related Steiner Forest problem--a variant where different terminal sets are not necessarily contained in distinct connected components--does not admit a subexponential parameterized algorithm even on unweighted planar graphs, as shown by Pilipczuk, Pilipczuk, Sankowski, and van Leeuwen \[PPSvL18\].

## 1.2 Our Methods

We next give an overview of how the main results in this work are achieved. We start with a high-level overview of the general strategy using Independent Set as an illustrative example and show some potential pitfalls. This general strategy (avoiding the pitfalls) follows the algorithm by Nederlof \[Ned20\]. In a second step, we give a few more technical details regarding the algorithm and highlight the key distinctions between our algorithm and the one by Nederlof. Then, we show how to apply this general framework to different problems. The application for _k_-Subgraph Scoring will be quite simple and for Maximum-Weight Induced Forest and different variants of graph minors, we will set up increasingly complicated notions.

We now give a high-level overview of the general strategy. As a starting point, consider the classic divide-and-conquer strategy pioneered by Lipton and Tarjan in the context of planar separators \[LT80\]. Given a planar graph _G_=(_V,E_), an integer _k_, and a balanced (cycle) separator _C_ in _G_, we _guess_<sup>2</sup> which vertices of _C_ appear in the solution. We then remove _C_ and all neighbors of those chosen vertices from the graph, guess how many vertices of the solution lie in the interior<tbc>

<sup>2</sup>Whenever we say we "guess" something, we actually iterate over all possibilities, but for presentation and proof, we focus on the iteration that leads to an optimal solution.

