isolated vertices in \(G'\) as deleted). This means we always find a vertex of degree 2 in the next iteration (or we are finished).

Once this procedure terminates, _F_outer contains all edges part of the outer face, and _F_inner contains all other edges. Each iteration of the aforementioned loop requires _O_(1) time and there are _O(n_) iterations total. All data structures require _O(n_) bits. \(\blacktriangleleft\)

Using the previous lemma we can easily implement the outlined algorithm to compute a canonical representation _G_can=_S_min of a maximal outerplanar graph in linear time and bits.

\(\blacktriangleright\) **Theorem 29.** _Let G be a maximal outerplanar graph. We can compute and store a canonical representation G_can _of G in O(n_) _time and bits._

A simple isomorphism algorithm follows by comparing the canonical representations.

\(\blacktriangleright\) **Corollary 30.** _Let G and_ \(G'\) _be two maximal outerplanar graphs. We can test isomorphism of G and_ \(G'\) _in O(n_) _time and bits._

**Proof.** Using Theorem 29, compute canonical representations _G_can and \(G'_\text{can}\) of _G_ and \(G'\), respectively. Then _G_ and \(G'\) are isomorphic exactly if their canonical representations are equal. \(\blacktriangleleft\)

## 7.2 Biconnected Outerplanar Graphs

We continue with biconnected outerplanar graphs. Recall that a biconnected graph is a connected graph where the removal of any single vertex does not disconnect the graph. On a high level, we handle biconnected outerplanar graphs similar as maximal outerplanar graphs: we compute a canonical representation based on a hamilton cycle. Contrary to maximal outerplanar graphs, where the simple degree sequence uniquely identifies isomorphic graphs, this is not the case for biconnected outerplanar graphs. Colbourn and Booth [32] showed the following canonical representation of biconnected outerplanar graphs, which we show how to construct and store space-efficiently. Let _G_ be a biconnected outerplanar graph. First, construct a hamilton cycle _H_ of _G_. For two vertices \(u,v\in V(G)\) denote with _hamilton distance h(u,v_) the length of a shortest path between _u_ and _v_ that uses only outer edges. To construct a canonical representation _G_can of _G_ replace each vertex _u_ in _H_ with the sequence \(Su=(h(u,v):v\in N(u))\), ordered in increasing values. We refer to this as a _hamilton-distance sequence_. Colbourn and Booth showed that such a hamilton-distance sequence is canonical, up to the choice of the start vertex and clockwise or counterclockwise direction of the hamilton cycle. Analogous to the technique used for constructing a canonical representation for maximal outerplanar graphs, simply choosing the lexicographically smallest hamilton distance sequence produces a canonical representation _G_can of _G_. This again can easily be achieved using Duval’s algorithm (Lemma 27).

Using a standard representation the sequence requires \(\Theta(nlogn)\) bits to be stored. Contrary to the canonical representation for maximal outerplanar graphs we can not use self-delimiting number to store each number in the hamilton distance sequence, as the sum of distances is \(\omega(n)\) in some biconnected outerplanar graphs. Instead, we use a technique based on balanced parentheses to encode the distances, which we refer to as _compact hamilton- distance sequence_. Intuitively, each hamilton distance of a vertex _u_ to a vertex _v_ that is contained in the hamilton-distance sequence is encoded compactly as a pair of matching parenthesis in a balanced parenthesis string such that their distance in the string is equal (omitting negligible additional calculations) to the hamilton distance of _u_ and _v_. A compact hamilton-distance sequence _P_ that represents a hamilton-distance sequence _H_ allows us

