To resolve this ambiguity, we introduce a colored unicentric node _w_ whenever a bicentric pair is identified, as per Rule 1 below (see Def. 21 and Fig. 5). This step allows us to connect the unicentric node of each tree in the forest to a new, single node _r_, effectively forming one comprehensive tree, as defined in Rule 2.

\(\blacktriangleright\) **Definition 21** (Forest to tree reduction)**.** _Choose a new arbitrary color c._

**_Rule 1_** _For each connected component with a bicentric pair of nodes_ {_u,v}, introduce a new c-colored node w, connecting w to both u and v while disconnecting u from v._

**_Rule 2_** _Insert a c-colored node r and connect it to the center of each connected component._

We want to remark that all newly introduced nodes have to be colored distinctively from the already existing nodes, in the case we are working with node-colored forests. This coloring ensures that these nodes can only be mapped to other introduced nodes. Consequently, Rule 1 does not alter any tree in a forest in such a way that it becomes isomorphic to a tree in another forest that already possessed a unicentric node. We refer to a reduction of a forest _F_ to a tree _T_ according to Definition 21 as a _tree reduction of F_.

The next lemma shows that our reduction from forest to tree isomorphism preserves their isomorphic property.

\(\blacktriangleright\) **Lemma 22.** _Two forests_ \(F,F'\) _are isomorphic exactly if their respective tree reductions_ \(T,T'\) _are isomorphic._

**Proof.** To show our claim we proof both directions.

\(\Rightarrow\) To demonstrate this implication, we must establish a bijection \(f'\) between _T_ and \(T'\). Assume that _f_ is an existing bijection between _F_ and \(F'\). Observe that our transformation exclusively adds colored nodes, but does not remove any nodes. Our goal is to extend _f_ to \(f'\) by incorporating mappings of the newly introduced colored nodes. First, consider the trees (in the forests _F_ and \(F'\)) that have a unicentric node. Those trees are mapped by _f_ from _F_ to \(F'\) and the same mapping can be used as mapping \(f'\) to map these nodes from _T_ to \(T'\). Next, let us consider the trees that are bicentric. Recall that _f_ maps two center nodes _u_ and _v_ of a bicentric tree of _F_ to two center nodes of a bicentric tree \(u'\) and \(v'\) in \(F'\). Then our construction introduces colored nodes _w_ and \(w'\) to _T<sub>F</sub>_ and \(T_{F^\prime}\), respectively, connected to each of these center nodes. First note that when removing all edges between nodes that form a bicenter in _F_ and \(F'\) during the process of creating a tree reduction, the isomorphism _f_ remains a valid isomorphism. Next, our tree reduction introduces respective parent nodes _w_ and \(w'\) of {_u,v_} and \(\{u',v'\}\). Again, _f_ can be trivially extended to map _w_ to \(w'\) as _w_ and \(w'\) have an equal number of isomorphic subtrees. Finally, we add root _r_ and \(r'\) to produce _T_ and \(T'\), and simply extending _f_ to map _r_ to \(r'\) produces our desired isomorphism \(f'\) that maps _T_ to \(T'\).

r w
u v
u v

**Figure 5** Left: a forest where one tree has a center consisting of one node and a tree that has a center consisting of two nodes {_u,v_}. Right: The forest transformed to a unique tree, where centers consisting of two nodes are "extended" with a new colored center _w_ and all trees are connected to a colored root _r_.

