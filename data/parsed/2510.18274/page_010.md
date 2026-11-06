**Algorithm 1:** A model-independent framework for computing minimum _s-t_ cuts.

**Input:** An undirected unweighted graph _G_=(_V,E_) with _n_ vertices.

**Output:** A minimum _s-t_ cut of _G_.

**Procedures:**

1. Compute a graph \(H\unknown G\) such that \(\nu(H)\ge\nu(G)-\Delta\) for some value \(\Delta\) to be set later.

1a. Compute a flow subgraph \(F\unknown H\) of value \(\nu(F)=\nu(H)\ge\nu(G)-\Delta\).

2. Compute a minimum _s-t_ cut in the residual network _G<sub>F</sub>_, and output it.

Algorithm 1: A model-independent framework for computing a minimum _s-t_ cut.

Note here that if we assume a correct answer _H_ following Step 1, the flow subgraph _F_ in Step 1a can be computed locally and free of costs in both computation models.

We first need to argue that this is a correct framework. This is done via following claim which gives a perfect reduction between all minimum _s-t_ cuts of _G<sub>F</sub>_ and all minimum _s-t_ cuts of _G_.

**Claim 3.1.** _Let G be an undirected unweighted graph and F be its flow subgraph. For any cut_ (_S,T), we have_ \(|E_G(S,T)|=\nu(F)+w_{G_F}(S,T)\).

_Proof._ First, observe that \(w_{G_F}(S,T)=|E_{G\backslash F}(S,T)|+2\cdot w_F(T,S)\). This is because we can write _G<sub>F</sub>_ as a union of two graphs: an undirected unweighted graph _G_\\_F_ (which contributes to the first term) and a directed graph which is a reversal of edges of _F_ with weights 2 (which contributes to the second term).

Observe further that \(\nu(F)=w_F(S,T)-w_F(T,S)\). This is because the edges of _F_ can be partitioned into \(\nu(F)\) disjoint _s-t_ directed paths. Each of those start at \(s\in S\) and ends at \(t\in T\). As such, it must cross from _S_ to _T_ exactly one more time than it crosses from _T_ to _S_. Thus, each of the \(\nu(F)\) disjoint _s-t_ directed paths contribute a value of 1 to _w<sub>F</sub>(S,T_)-_w<sub>F</sub>(T,S_).

Combining the two observations, we have:

\(\nu(F)+|E_{G_F}(S,T)|=w_F(S,T)+w_F(T,S)+|E_{G\backslash F}(S,T)|=|E_G(S,T)|\)

as wished.

We consider the implementation of Algorithm 1 in two computational models: the _cut-query model_ and the _two-player communication model_, where we aim to use the (modified) RSW algorithm as a baseline to implement Step 2 in both settings. However, applying the RSW algorithm to the residual graph _G<sub>F</sub>_ introduces two key challenges. First, we only have cut-query access to the original graph _G_, not to the residual graph _G<sub>F</sub>_. In fact, throughout our algorithm, we shall only need to make cut queries to the graph _G_\\_F_. Fortunately, since the flow graph _F_ is explicitly computed in Step 1a, we can simulate cut queries to _G_\\_F_ using a single query access to _G_ and the explicit description of _F_. Second, the residual graph _G<sub>F</sub>_ is a _mixed_ graph, containing both directed and undirected edges. As the RSW algorithm was originally designed for undirected graphs, it does not directly apply to this setting. To address this, we show that the RSW algorithm can be carefully modified to operate on mixed graphs in both computational models without altering its correctness.

