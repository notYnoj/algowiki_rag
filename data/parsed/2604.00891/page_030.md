Minor, and Maximum-Weight Rooted Parallel Induced Minor. These examples will get progressively more technical and we recommend to read them in order. Our aim is to provide the necessary ingredients one after another so that each step on its own is as simple as possible to follow. Most of the aforementioned problems also have relevant special cases which we mentioned in the introduction. We will discuss those along the way.

## 4.1 A Simple-to-use Fragment

Here, we give a general recipe for how to apply Theorem 3. We then show how to use this recipe for showing that _k_-Subgraph Scoring can be solved in \(2^{\tilde{\mathcal{O}}(\sqrt{k})}n^{2.49}\) time. Finally, we show how to use this fact to show that problems like Maximum-Weight Independent Set, Weighted Partial Vertex Cover, Densest _k_-Subgraph, and Maximum (_k,n-k_)-Cut can be solved in the same time. We note that subexponential parameterized algorithms were already known for Maximum-Weight Independent Set \[vN20\] and Maximum (_k,n-k_)-Cut for undirected planar graphs \[FGIK24\], but was asked as a specific open question for Densest _k_-Subgraph \[FGIK24\] and was not known for Weighted Partial Vertex Cover or Maximum (_k,n-k_)-Cut for directed planar graphs. This result also generalizes in a straight-forward way to weighted variants of Maximum (_k,n-k_)-Cut and Densest _k_-Subgraph and we suspect that there are many more applications of _k_-Subgraph Scoring.

We now present the recipe for any problem \(\pi\) under consideration.

1. Decide for an appropriate function \(\gamma\) and constants \(\rho,\alpha_\pi\ge 1\).<tbc>

2. Define \(S_\pi\) and \(R_\pi\) and show that they can be computed/maintained in \(\mathcal{O}(\gamma(k)n^\rho)\) time (Requirements R2 and R3 in Theorem 3).<tbc>

3. Define an appropriate request version \(\pi\)-Request.<tbc>

4. Show that Requirement R1 of Theorem 3 holds, that is, there is an index _i_ such that we can remove each layer \(i+j\cdot(\alpha_\pi k+1)\) of a BFS layering for any _j_.<tbc>

5. Show that Requirement R4 of Theorem 3 is fulfilled, that is, given a separator _C_ and solutions to subproblems on either side of the separator, we can compute in \(\mathcal{O}(\gamma(k)n^\rho)\) time all partial solutions that do not intersect _C_ too much.<tbc>

6. Design an algorithm that given access to an oracle for \(\pi\)-Request solves \(\pi\) and analyze its running time and how many oracle calls it makes.

One also has to show that \(\pi\)-Request is computable but since this is obvious in all examples studied in this paper, we will ignore this step. We next show how to use this recipe and Theorem 3 to show a subexponential parameterized algorithm for _k_-Subgraph Scoring. Before doing so, we prove a small lemma that will be useful for all applications of Theorem 3.

**Lemma 11.** _Let_ (_C,_1) _be a pair that is measured with respect to two integers d and_ \(\alpha\)_, where_ \(\alpha\) _is a constant. Then, the number of possible pebble sets_ M _for_ (_C,_1) _is in_ \(\mathcal{O}(2^{80\alpha\sqrt{d}log^2(d)})\) _and all pebble sets can be computed in_ \(\mathcal{O}(2^{80\alpha\sqrt{d}log^2(d)}d)\) _time._

_Proof._ Note that by definition, \(|C_\mathrm{he}|\le 40\alpha\sqrt{d}\), \(|C_\mathrm{li}|\le 60\alpha dlog(d)\), and the number of possible pebble sets for (_C,_1) is at most \(2^{|C_\mathrm{hel}|}\genfrac(){pt}{2}{|C_\mathrm{li}|}{20\alpha\sqrt{d}log(d)}\). If \(d\le(60\alpha)^2\), that is, _d_ is constant, we get a con stant number of possible pebble sets. Otherwise, it holds that \(60\alpha log(d)<d\) because \(log(d)<\sqrt{d}\)<tbc>

