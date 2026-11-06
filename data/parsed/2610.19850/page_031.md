1: **Input:** A graph _G_.<br>
2: **Output:** All PMCs of _G_.<br>
# Base case #<br>
3: **if** _G is a clique_ **then**<br>
4: **return** {_V(G_)}<br>
# Induction step #<br>
5: \(\mathcal{C}\leftarrow\text{PMC-Traversal}(G\backslash\{a\})\) # C is a collection of vertex sets #<br>
6: \(\Pi\leftarrow\text{empty collection of vertex sets}\)<br>
7: **for** \(\Omega'\in\mathcal{C}\) **do**<br>
8: **if** \(\Omega'\) _PMC of G_ **then** \(\Pi\leftarrow\Pi\cup\{\Omega'\}\)<br>
9: **if** \(\Omega'\cup\{a\}\) _PMC of G_ **then** \(\Pi\leftarrow\Pi\cup\{\Omega'\cup\{a\}\}\)<br>
10: **for** _S minimal separator of G_ **do**<br>
11: **if** \(S\cup\{a\}\) _PMC of G_ **then** \(\Pi\leftarrow\Pi\cup\{S\cup\{a\}\}\)<br>
12: \(\widehat{\Pi}\leftarrow\text{copy}\) of \(\Pi\); # \(\Pi\) and \(\widehat{\Pi}\) contain all PMCs which are not _a_-nice (Definition 16). #<br>
13: \(\Pi_a\leftarrow\text{PMC-BFS}(G,\widehat{\Pi})\)<br>
14: **return** \(\Pi\cup\Pi_a\)

<tbc>Concretely, after line 12, set \(\widehat{\Pi}\) is made up of the PMCs of _G_ which either are PMCs of _G_\\{_a_} or contain _a_, where _a_ is the vertex withdrawn for the recursive call.

We provide below a property of PMC-BFS which will be useful for the complexity analysis of PMC-Traversal. The process used to compute the out-neighbors of a given PMC completely depends on the guess of two vertices: _u_<sup>∗</sup> and _b_<sup>∗</sup>. Hence, as announced, each PMC admits at most _n_<sup>2</sup> out-neighbors, considering a rough upper bound.

**Lemma 17.** _For any input_ \((G,\widehat{\Pi})\), PMC-BFS _can be executed in time at most_ \(O(n^3m|\Pi_G|)\).

_Proof._ For a given guess (_u_<sup>∗</sup>_,b_<sup>∗</sup>) in the neighboring process, a potential neighbor is built in _O(m_), using graph searches to determine both the _X_-close (_b_<sup>∗</sup>_,u_<sup>∗</sup>)-separator and component _C<sub>G</sub>_\[_b_<sup>∗</sup>_,S_<sup>∗</sup>\]. Then, we check whether the obtained set is a PMC in _O(nm_). Finally, we obtain a time complexity of _O(n_<sup>3</sup>_m_) to compute all neighbors of a given PMC \(\Omega'\). The BFS itself consumes \(O(n^2|\Pi_G|)\), given the rough upper bound of |N|. All in all, the most costly operation in PMC-BFS is the neighborhood computation, achieved overall in \(O(n^3m|\Pi_G|)\).

## 4.2 Shutters of active PMCs

From now on, we will give ourselves some PMC \(\Omega\) which can be considered as a "target PMC". Our objective is to prove that, using the neighborhood function between PMCs (Definition 20), there is a path in the PMC-graph \((\Pi_G,\mathcal{N})\) from some "already listed" PMC in \(\widehat{\Pi}\) to our target \(\Omega\) which is naturally supposed to be not already listed. As described in the previous subsection, our algorithm is recursive, and, we assume that PMCs of _G_\\{_a_}, for some vertex _a_, are already listed (line 8 of Algorithm 3). PMCs of _G_ containing _a_ are also listed easily in output-linear time (lines 9 and 11). Consequently, we assume that \(\Omega\) does not contain _a_ and is not a PMC of _G_\\{_a_}. Equivalently, we assume that \(\Omega\) is an _a_-nice PMC (Definition 16). As a consequence,<tbc>

**Algorithm 3:** PMC-Traversal

