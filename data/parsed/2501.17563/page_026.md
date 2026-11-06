6. Note that _R<sub>ij</sub>_ participates in two symmetric-looking frequency inequalities:<br>
\(R_{ij}+\sum_{a:i\in(j\unknown a)}Q_{jia}\le f_j\) and \(R_{ij}+\sum_{a:j\in(i\unknown a)}Q_{ija}\le f_i\). Observe that the _Q_ variables are not the same: In the first inequality they represent a directed relationship from _j_ to every node "behind" _i_, while in the second inequality it is a direction from _i_ to every node "behind" _j_. None of these _Q_ variables is related to the _Q_ variables in the capping inequalities of _R<sub>ij</sub>_, where the third node is _between i_ and _j_, not behind any of them. Also, not every node appears in some _Q_ related to _R<sub>ij</sub>_: nodes that branch out of the path between _i_ and _j_ do not define a colinear triplet.<tbc>

7. Some of the constraints are redundant. To see it best, consider two leaves _i_ and _j_. They do not have _Q_ variables for nodes behind them, therefore we get the two inequalities: \(R_{ij}\le f_j\) and \(R_{ij}\le f_i\). Depending on whether \(f_i\ge f_j\) or \(f_i\le f_j\), one inequality is redundant. More generally, even when _j_ is a leaf and _i_ is not, we could have redundancy if \(f_j\le f_i\). Explicitly, in this case \(R_{ij}\le f_i\) is redundant because it is implied by \(R_{ij}\le f_j-\sum_{a:i\in(j\unknown a)}Q_{jia}\le f_j\le f_i\).<tbc>

8. One can loosely interpret _f<sub>j</sub>_ as an amount of tokens to be endowed by _j_ to _i_ and any node behind _i_. Note that there is an inequality for _j_ with every node, so if we think of the topology as tree rooted in _j_ (as explained in item 2), _j_ has the same amount to endow to each subtree, with overlaps between subtrees. _R<sub>ij</sub>_ is the amount endowed to _i_, _Q<sub>jia</sub>_ is the amount endowed to _a_, and full endowment means equality instead of inequality. The fact that \(R_{ij}\equiv R_{ji}\) means that _i_ and _j_ must endow the same amount to each other. Because of the multiple budgets of each node and the overlap, this interpretation is not simply some kind of flow.

## 4.3 A Weak-Duality Invariant over STT Subtrees

The _weak duality theorem_ states that the dual value is bounded by the primal value. In this subsection we present this relation in an explicit STT-intuitive way. Specifically, given a fixed STT, _T_, we show that for each subtree _T<sub>i</sub>_ of _T_, rooted at _i_, the contribution to the dual value of the variables _R<sub>ab</sub>_ for _a_ and _b_ whose LCA (lowest common ancestor) is _i_, is bounded by the total frequency of the nodes in this subtree except for _i_ (which is the contribution to the primal value, of pushing the nodes one edge deeper when hanging the subtrees of _i_ under it). We denote \(T'_i\equiv T_i\backslash\{i\}\):

\(\sum_{a,b\in T_i^\prime LCA(a,b)=i}R_{ab}=\frac{1}{2}\cdot\sum_{a\in T_i^\prime}\sum_{b\in T_i^\prime LCA(a,b)=i}R_{ab}=\frac{1}{2}\cdot\sum_{a\in T_i^\prime}\sum_{b\in T_i^\prime LCA(a,b)=i}(Q_{aib}+Q_{bia})\)<br>
\(=\frac{1}{2}\cdot\sum_{a\in T_i^\prime}\big(\sum_{b\in T_i^\prime LCA(a,b)=i}Q_{aib}\big)+\frac{1}{2}\cdot\sum_{b\in T_i^\prime}\big(\sum_{a\in T_i^\prime LCA(a,b)=i}Q_{bia}\big)\)<br>
\(\le\frac{1}{(2)}\cdot\sum_{a\in T_i^\prime}\big(f_a-R_{ia}\big)+\frac{1}{2}\cdot\sum_{b\in T_i^\prime}\big(f_b-R_{ib}\big)=\sum_{a\in T_i^\prime} f_a-\sum_{a\in T_i^\prime} R_{ia},\)

where (1) is by the capping equalities and (2) is by the frequency inequalities. The factor of \(\frac{1}{2}\) is due to double-counting in the double-sum. Re-arranging the inequality we get:<tbc>

\(\sum_{a,b\in T_iLCA(a,b)=i}R_{ab}\le\sum_{a\in T_i^\prime} f_a\)

