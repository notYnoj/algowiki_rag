_T_<sub>1</sub>=(_V_<sub>_T_<sub>1</sub></sub>_,E_<sub>_T_<sub>1</sub></sub>) and _T_=(_V_<sub>_T_<sub>2</sub></sub>_,E_<sub>_T_<sub>2</sub></sub>) are isomorphic if an isomorphic mapping \(f:V_{T_1}\rightarrow V_{T_2}\) exists such that for each \(u\in V_{T_1}\), _u_ and _v=f(u_) have the same color assigned.

To check isomorphism of uncolored trees we use a classification number whose computation was only influenced by the structure of the tree. To check isomorphism of node-colored trees we additionally use the color of a node to compute a classification number, i.e., we add to each classification vector of a node _u_ the color of _u_ as the last entry of the vector.

\(\blacktriangleright\) **Theorem 20.** _Given two (unrooted) colored n-node trees T_<sub>1</sub> _and T_<sub>2</sub>_, there is an algorithm that outputs if T_<sub>1</sub> _and T_<sub>2</sub> _are isomorphic in O(n+b_) _time using O(n+b_) _bits exactly if the colors of all nodes of T_<sub>1</sub> _and T_<sub>2</sub> _can be written within O(b_) _bits._

**Proof.** We assume w.l.o.g. that both trees are rooted, otherwise we do the same as for uncolored tree, i.e., find the centers of both trees with Lemma 18 and repeat this theorem with the 4 possibilities to choose the correct roots. We start by describing a pre-processing step. We describe this for an _n_-node tree _T_. The process is then applied to _T_<sub>1</sub> and _T_<sub>2</sub>, respectively. Let color(u) ∈ {0,1}<sup>∗</sup> be the color of a node _u_ in _T_. First we transform _T_ into a colored ordinal tree (by using Corollary 12) represented by a balanced parenthesis representation.

Our general approach to check isomorphism remains the same, but we have to make sure that two nodes with non-isomorphic maximal subtrees cannot get the same classification number. We do this by adding the color of a node to the classification number, which changes the classification number from a tuple (_hu,q<sub>u</sub>_) to a triple (_hu,q<sub>u</sub>,_color(u)), where _hu_ is the height of _u_ in _T_, _q<sub>u</sub>_ is the number representing the structure of the maximal induced subtree and color(u) is (as defined) the color of _u_. The classification vector of the parent _v_ of _u_ includes then the color information of all its children, including _u_. By our computation of the classification number of _v_ (described in (C)) we ensure that the roots of the two trees get the same classification numbers exactly if their respective colors can be mapped in addition to having isomorphic subtrees.

To maintain the classification numbers and vectors we still use the data schema of Lemma 16, but have to account for the additional space of the colors.

Without modifications the running time increases to _O(n+b_) due to the construction of the balanced parenthesis representation of the ordinal tree with access to its colors and Lemma 16. For the same reasons our space bound increases to _O(n+b_) bits.

## 6 Forest Isomorphism

We now describe how to extend our algorithm to forests. The idea is to perform a problem reduction, from (colored) forest to colored tree isomorphism by carefully transforming the given forests into trees without altering their isomorphic properties. We then solve colored tree isomorphism which is also a solution for forest isomorphism.

A naive approach to transforming a forest into a single tree is to create a new node and connect it to an arbitrary node from each tree in the forest. However, this method is unreliable, as selecting the incorrect node for connection might lead to generating non-isomorphic trees from isomorphic forests, or vise-versa.

To address this, we utilize the fact that the bijective mapping between two isomorphic trees, _T_ and \(T'\), includes a mapping that aligns their centers. These centers can be either _unicentric_ (a single node) or _bicentric_ (a pair of nodes). In unicentric cases, the mapping between centers is straightforward and unique. However, in bicentric situations, the correct mapping is ambiguous due to the two possible ways to align the pair of nodes at each center.

